import functools, os
import functions as f
import supervisely_lib as sly
import globals as g


# ROOTS
import sys
from pathlib import Path

root_source_dir = str(Path(sys.argv[0]).parents[1])
sly.logger.info(f"Root source directory: {root_source_dir}")
sys.path.append(root_source_dir)

sly_sources_dir = str(Path(sys.argv[0]).parents[0])
sly.logger.info(f"Source directory: {sly_sources_dir}")
sys.path.append(sly_sources_dir)


def send_error_data(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = None
        try:
            value = func(*args, **kwargs)
        except Exception as e:
            request_id = kwargs["context"]["request_id"]
            g.my_app.send_response(request_id, data={"error": repr(e)})
        return value

    return wrapper


@g.my_app.callback("smart_segmentation")
@sly.timeit
@send_error_data
def smart_segmentation(api: sly.Api, task_id, context, state, app_logger):

    x1, y1, x2, y2 = f.get_smart_bbox(context["crop"])
    pos_points, neg_points = f.get_pos_neg_points_list_from_context(context)
    img_path = os.path.join(g.img_dir, "base_image.png")
    base_image_np = f.get_image_by_hash(context["image_hash"], img_path)
    bitmap = f.get_bitmap_from_points(pos_points, neg_points, base_image_np, (x1, y1, x2, y2))
    bitmap_origin, bitmap_data = f.unpack_bitmap(bitmap)

    request_id = context["request_id"]
    g.my_app.send_response(request_id, data={"origin": bitmap_origin, "bitmap": bitmap_data, "success": True, "error": None})


def main():
    sly.logger.info("Script arguments", extra={
        "context.teamId": g.TEAM_ID,
        "context.workspaceId": g.WORKSPACE_ID,
        "context.projectId": g.PROJECT_ID
    })

    g.my_app.run()


if __name__ == "__main__":
    sly.main_wrapper("main", main)