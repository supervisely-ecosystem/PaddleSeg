import os

import download_progress
import globals as g
import paddle
import requests
import supervisely_lib as sly
from eiseg.controller import InteractiveController
from supervisely_lib.io.fs import download, mkdir


def download_file_from_link(api, link, model_path, file_name, progress_message, app_logger):
    response = requests.head(link, allow_redirects=True)
    sizeb = int(response.headers.get('content-length', 0))
    progress_cb = download_progress.get_progress_cb(api, g.TASK_ID, progress_message, sizeb, is_size=True)
    download(link, model_path, cache=g.my_app.cache, progress=progress_cb)
    download_progress.reset_progress(api, g.TASK_ID)
    app_logger.info(f'{file_name} has been successfully downloaded')


def deploy(model_name):
    available_models = {
        "static_hrnet18_ocr64_cocolvis":
            (
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr64_cocolvis.pdiparams",
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr64_cocolvis.pdmodel"),
        "static_hrnet18s_ocr48_cocolvis":
            (
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_cocolvis.pdiparams",
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_cocolvis.pdmodel"),
        "static_hrnet18_ocr64_human":
            (
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr64_human.pdiparams",
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr64_human.pdmodel"),
        "static_hrnet18s_ocr48_human":
            (
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_human.pdiparams",
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_human.pdmodel"),
        "static_edgeflow_cocolvis":
            (
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_edgeflow_cocolvis.pdiparams",
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_edgeflow_cocolvis.pdmodel"),
        "static_hrnet18_ocr48_rsbuilding_instance":
            (
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr48_rsbuilding_instance.pdiparams",
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr48_rsbuilding_instance.pdmodel"),
        "static_hrnet18s_ocr48_lits":
            (
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_lits.pdiparams",
                "https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_edgeflow_cocolvis.pdmodel")
    }

    pdiparams_link, pdmodel_link = available_models[model_name]
    param_path = f"/eiseg_models/{model_name}/{model_name}.pdiparams"
    if os.path.isfile(param_path) is False:
        model_dir = os.path.join(g.work_dir, "eiseg_models", model_name)
        mkdir(model_dir)
        param_path = os.path.join(model_dir, f"{model_name}.pdiparams")
        model_path = os.path.join(model_dir, f"{model_name}.pdmodel")
        download_file_from_link(g.api, pdiparams_link, param_path, model_name, f"Download {model_name}.pdiparams",
                                g.my_app.logger)
        download_file_from_link(g.api, pdmodel_link, model_path, model_name, f"Download {model_name}.pdmodel",
                                g.my_app.logger)
    else:
        g.my_app.logger.info(f"{model_name} has been loaded from docker image")

    with_mask = True
    if model_name == "static_edgeflow_cocolvis":
        with_mask = False

    predictor_params = {'brs_mode': 'NoBRS', 'with_flip': False,
                        'zoom_in_params': {'skip_clicks': -1, 'target_size': (400, 400), 'expansion_ratio': 1.4},
                        'predictor_params': {'net_clicks_limit': None, 'max_size': 800, 'with_mask': with_mask}}

    # use_gpu = False
    support_gpu = paddle.device.is_compiled_with_cuda()
    sly.logger.info(f"🟩 SUPPORT GPU: {support_gpu}")


    if g.DEVICE == "gpu" and support_gpu:
        paddle.device.set_device(g.DEVICE)
        use_gpu = True
        sly.logger.info(f"🟩 USE GPU: {use_gpu}")
        device = paddle.device.get_device()
    else:
        paddle.device.set_device(g.DEVICE)
        use_gpu = False
        device = paddle.device.get_device()


    g.CONTROLLER = InteractiveController(predictor_params=predictor_params, prob_thresh=g.PROB_THRESH)
    g.CONTROLLER.setModel(param_path=param_path, use_gpu=use_gpu)
    sly.logger.info(f"🟩 Model has been successfully deployed on device: '{device}'")
