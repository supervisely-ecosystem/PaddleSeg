import os
from diskcache import Cache
import supervisely_lib as sly
from supervisely_lib.io.fs import mkdir


my_app = sly.AppService()
api: sly.Api = my_app.public_api

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
TASK_ID = int(os.environ["TASK_ID"])

cache_item_expire_time = 600

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

prob_thresh = float(os.environ['modal.state.thresh'])
param_name = os.environ['modal.state.modelName'] + '.pdparams'

param_path = os.path.join(param_dir, param_name)

if param_name == 'hrnet18_ocr64_cocolvis.pdparams':
    model_name = 'HRNet18_OCR64'
    model_link = 'https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18_ocr64_cocolvis.pdparams'
else:
    model_name = 'HRNet18s_OCR48'
    model_link = 'https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18s_ocr48_cocolvis.pdparams'
elif param_name == 'hrnet18_ocr64_human.pdparams':
    model_name = 'HRNet18_OCR64'
    model_link = 'https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18_ocr64_human.pdparams'
elif param_name == 'hrnet18s_ocr48_human.pdparams':
    model_name = 'HRNet18s_OCR48'
    model_link = 'https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18s_ocr48_human.pdparams'


download_file_from_link(api, model_link, param_path, param_name, f"Download {param_name}", my_app.logger)

model = MODELS[model_name]()
model.load_param(param_path)

my_predictor_params = {"brs_mode": "NoBRS", "zoom_in_params": {"skip_clicks": -1, "target_size": (400, 400), "expansion_ratio": 1.4},
                       "predictor_params": {"net_clicks_limit": None, "max_size": 800}}