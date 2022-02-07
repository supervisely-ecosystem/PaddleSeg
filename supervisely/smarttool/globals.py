import os
from diskcache import Cache
import supervisely_lib as sly
from supervisely_lib.io.fs import mkdir


my_app = sly.AppService()
api: sly.Api = my_app.public_api

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])

work_dir = os.path.join(my_app.data_dir, "work_dir")
mkdir(work_dir, True)
img_dir = os.path.join(work_dir, "img")

# Create Cache
cache_dir = os.path.join(work_dir, "diskcache")
cache = Cache(directory=cache_dir)
cache_item_expire_time = 600  # seconds
mkdir(cache_dir)
mkdir(img_dir)

CONTROLLER = None
MODEL_NAME = os.environ["modal.state.selectedModel"]
PROB_THRESH = float(os.environ['modal.state.thresh'])