# ROOTS
import sys
from pathlib import Path
import supervisely_lib as sly
import functools
import math


# repo_root_source_dir = str(Path(sys.argv[0]).parents[2])
# sly.logger.info(f"Repo root source directory: {repo_root_source_dir}")
# sys.path.append(repo_root_source_dir)
#
# app_root_source_dir = str(Path(sys.argv[0]).parents[1])
# sly.logger.info(f"App root source directory: {app_root_source_dir}")
# sys.path.append(app_root_source_dir)
#
# sources_dir = str(Path(sys.argv[0]).parents[0])
# sly.logger.info(f"Source directory: {sources_dir}")
# sys.path.append(sources_dir)


import globals as g
import functions as f
import load_model
import mask_image


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
    bbox = sly.Rectangle(y1, x1, y2, x2)

    base_image_np = f.download_image_from_context(context)
    crop_np = sly.image.crop(base_image_np, bbox)
    height, width = crop_np.shape[:2]
    cropped_shape = (height, width)
    resized_shape = None

    max_crop_dim = 1000
    if height > max_crop_dim or width > max_crop_dim:
        base_height = 720
        base_width = 800

        ap_ratio = width / height
        if height > width:
            new_height = base_height
            new_width = math.ceil(new_height * ap_ratio)
        else:
            new_width = base_width
            new_height = math.ceil(new_width / ap_ratio)

        resized_shape = (new_height, new_width)
        crop_np = sly.image.resize(crop_np, resized_shape)

    pos_points, neg_points = f.get_pos_neg_points_list_from_context_bbox_relative(x1, y1, pos_points, neg_points,
                                                                                  cropped_shape, resized_shape)
    clicks_list = f.get_click_list_from_points(pos_points, neg_points)

    res_mask = mask_image.get_mask_from_clicks(crop_np, clicks_list)

    bitmap = f.get_bitmap_from_mask(res_mask, cropped_shape)
    bitmap_origin, bitmap_data = f.unpack_bitmap(bitmap, y1, x1)

    request_id = context["request_id"]
    g.my_app.send_response(request_id,
                           data={"origin": bitmap_origin, "bitmap": bitmap_data, "success": True, "error": None})


def main():
    sly.logger.info("Script arguments", extra={
        "context.teamId": g.TEAM_ID,
        "model_name": g.MODEL_NAME
    })
    load_model.deploy(g.MODEL_NAME)
    g.my_app.run()


if __name__ == "__main__":
    sly.main_wrapper("main", main)
