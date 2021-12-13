import os
from diskcache import Cache
import supervisely_lib as sly
from supervisely_lib.io.fs import mkdir


my_app = sly.AppService()
api: sly.Api = my_app.public_api

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])

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

CONTROLLER = None
MODEL_NAME = os.environ["modal.state.modelName"]
PROB_THRESH = float(os.environ['modal.state.thresh'])
