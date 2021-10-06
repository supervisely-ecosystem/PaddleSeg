import supervisely_lib as sly
import globals as g
import cv2
import numpy as np
from inference import clicker
from inference.predictor import get_predictor


prob_thresh = 0.5
modelName = 'HRNet18_OCR64'
paramPath = '/home/andrew/alex_work/supervisely-research/PaddleSeg/hrnet18_ocr64_cocolvis.pdparams'
my_predictor_params = {"brs_mode": "NoBRS", "zoom_in_params": {"skip_clicks": -1, "target_size": (400, 400), "expansion_ratio": 1.4},
                       "predictor_params": {"net_clicks_limit": None, "max_size": 800}}


def get_points_from_image(labels):
    clicks = {"pos": [], "neg": []}
    for label in labels:
        if label.geometry.geometry_name() == "point":
            if label.obj_class.name == "pos":
                click_coords = label.geometry.to_json()["points"]["exterior"][0]
                clicks["pos"].append(click_coords)
            if label.obj_class.name == "neg":
                click_coords = label.geometry.to_json()["points"]["exterior"][0]
                clicks["neg"].append(click_coords)
    return clicks


@g.my_app.callback("demo")
@sly.timeit
def demo(api: sly.Api, task_id, context, state, app_logger):

    meta_json = api.project.get_meta(g.PROJECT_ID)
    meta = sly.ProjectMeta.from_json(meta_json)

    ann_info = api.annotation.download(g.IMAGE_ID)
    ann = sly.Annotation.from_json(ann_info.annotation, meta)

    clicks = get_points_from_image(ann.labels)

    image = api.image.download_np(g.IMAGE_ID)
    result_mask = np.zeros(image.shape[:2], dtype=np.uint8)

    my_predictor = get_predictor(g.model.model, **my_predictor_params)
    my_predictor.set_input_image(image)
    my_clicker = clicker.Clicker()

    for point in clicks['pos']:
        click = clicker.Click(is_positive=True, coords=(point[1], point[0]))
        my_clicker.add_click(click)
    for point in clicks['neg']:
        click = clicker.Click(is_positive=False, coords=(point[1], point[0]))
        my_clicker.add_click(click)
    pred = my_predictor.get_prediction(my_clicker)

    object_mask = pred > prob_thresh
    #polygon = util.get_polygon(object_mask.astype(np.uint8) * 255)
    result_mask[object_mask] = 1

    cv2.imwrite('test.png', result_mask*255)

    g.my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "context.teamId": g.TEAM_ID,
        "context.workspaceId": g.WORKSPACE_ID,
        "modal.state.slyProjectId": g.PROJECT_ID
    })

    # Run application service
    g.my_app.run(initial_events=[{"command": "demo"}])


if __name__ == "__main__":

    sly.main_wrapper("main", main)