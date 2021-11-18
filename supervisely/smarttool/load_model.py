import os
import requests
import download_progress
import globals as g
from contrib.EISeg.eiseg.ui import Ui_EISeg
from util import MODELS
import supervisely_lib as sly
from supervisely_lib.io.fs import mkdir
from supervisely_lib.io.fs import download


def download_file_from_link(api, link, model_path, file_name, progress_message, app_logger):
    response = requests.head(link, allow_redirects=True)
    sizeb = int(response.headers.get('content-length', 0))
    progress_cb = download_progress.get_progress_cb(api, g.TASK_ID, progress_message, sizeb, is_size=True)
    download(link, model_path, cache=g.my_app.cache, progress=progress_cb)
    download_progress.reset_progress(api, g.TASK_ID)
    app_logger.info(f'{file_name} has been successfully downloaded')


def deploy(param_name):
    model_name = None
    model_link = None

    param_path = f"/eiseg_models/{param_name}"
    if param_name == 'hrnet18_ocr64_cocolvis.pdparams':
        model_name = 'HRNet18_OCR64'
        model_link = 'https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18_ocr64_cocolvis.pdparams'
    elif param_name == 'hrnet18s_ocr48_cocolvis.pdparams':
        model_name = 'HRNet18s_OCR48'
        model_link = 'https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18s_ocr48_cocolvis.pdparams'
    elif param_name == 'hrnet18_ocr64_human.pdparams':
        model_name = 'HRNet18_OCR64'
        model_link = 'https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18_ocr64_human.pdparams'
    elif param_name == 'hrnet18s_ocr48_human.pdparams':
        model_name = 'HRNet18s_OCR48'
        model_link = 'https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18s_ocr48_human.pdparams'

    if os.path.isfile(param_path) is False:
        param_dir = os.path.join(g.storage_dir, "param_dir")
        mkdir(param_dir)
        param_path = os.path.join(param_dir, param_name)
        download_file_from_link(g.api, model_link, param_path, param_name, f"Download {param_name}", g.my_app.logger)
    else:
        g.my_app.logger.info(f"{param_name} has been loaded from docker image")

    model = MODELS[model_name]()
    g.model = model
    model.load_param(param_path)
    sly.logger.info("🟩 Model has been successfully deployed")
