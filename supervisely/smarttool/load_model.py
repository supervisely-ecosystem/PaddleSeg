import requests
import download_progress
import globals as g
import supervisely_lib as sly
from supervisely_lib.io.fs import download
from eiseg.controller import InteractiveController


def download_file_from_link(api, link, model_path, file_name, progress_message, app_logger):
    response = requests.head(link, allow_redirects=True)
    sizeb = int(response.headers.get('content-length', 0))
    progress_cb = download_progress.get_progress_cb(api, g.TASK_ID, progress_message, sizeb, is_size=True)
    download(link, model_path, cache=g.my_app.cache, progress=progress_cb)
    download_progress.reset_progress(api, g.TASK_ID)
    app_logger.info(f'{file_name} has been successfully downloaded')


def deploy(model_name):
    # model_path = f"/eiseg_models/{model_name}/{model_name}.pdiparams"
    model_path = f"/home/paul/Documents/Work/Applications/PaddleSeg/supervisely/docker/eiseg_models/{model_name}/{model_name}.pdiparams"

    if model_name == "static_edgeflow_cocolvis":
        with_mask = False
    else:
        with_mask = True

    predictor_params = {
        "brs_mode": "NoBRS",
        "with_flip": False,
        "zoom_in_params": {
            "skip_clicks": -1,
            "target_size": (400, 400),
            "expansion_ratio": 10,
        },
        "predictor_params": {
            "net_clicks_limit": None,
            "max_size": 800,
            "with_mask": with_mask,
        },
    }

    g.CONTROLLER = InteractiveController(predictor_params, prob_thresh=g.PROB_THRESH)
    g.CONTROLLER.setModel(model_path)
    sly.logger.info("🟩 Model has been successfully deployed")
