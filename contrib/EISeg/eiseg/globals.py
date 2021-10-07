import os
import supervisely_lib as sly
from diskcache import Cache
from supervisely_lib.io.fs import mkdir
from ui import Ui_EISeg
from util import MODELS
from supervisely_lib.io.fs import download
import requests
import dl_progress


def download_file_from_link(api, link, model_path, file_name, progress_message, app_logger):
    response = requests.head(link, allow_redirects=True)
    sizeb = int(response.headers.get('content-length', 0))
    progress_cb = dl_progress.get_progress_cb(api, TASK_ID, progress_message, sizeb, is_size=True)
    download(link, model_path, cache=my_app.cache, progress=progress_cb)
    dl_progress.reset_progress(api, TASK_ID)
    app_logger.info(f'{file_name} has been successfully downloaded')


my_app = sly.AppService()
api: sly.Api = my_app.public_api

TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
PROJECT_ID = int(os.environ["modal.state.slyProjectId"])
TASK_ID = int(os.environ["TASK_ID"])

storage_dir = os.path.join(my_app.data_dir, "storage_dir")
mkdir(storage_dir, True)
work_dir = os.path.join(storage_dir, "work_dir")
mkdir(work_dir)

img_dir = os.path.join(work_dir, "img")

cache_dir = os.path.join(storage_dir, "cache_dir")
mkdir(cache_dir)
cache = Cache(directory=cache_dir)
cache_item_limit = 30
mkdir(cache_dir)

param_dir = os.path.join(storage_dir, "param_dir")
mkdir(param_dir)
param_name = 'hrnet18_ocr64_cocolvis.pdparams'
param_path = os.path.join(param_dir, param_name)

modelName = 'HRNet18_OCR64'
model_link = 'https://bj.bcebos.com/paddleseg/dygraph/interactive_segmentation/ritm/hrnet18_ocr64_cocolvis.pdparams'

download_file_from_link(api, model_link, param_path, param_name, f"Download {param_name}", my_app.logger)

model = MODELS[modelName]()
model.load_param(param_path)

prob_thresh = 0.5
my_predictor_params = {"brs_mode": "NoBRS", "zoom_in_params": {"skip_clicks": -1, "target_size": (400, 400), "expansion_ratio": 1.4},
                       "predictor_params": {"net_clicks_limit": None, "max_size": 800}}