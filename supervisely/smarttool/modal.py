import errno
import os
import sly_train_globals as g
from sly_utils import get_progress_cb
import supervisely_lib as sly


def get_models_list():
    return [
        {
            "Model type": "High precision model",
            "Applicable scene": "Suitable for general labeling",
            "Model structure": "HRNet18_OCR64",
            "Model name": "static_hrnet18_ocr64_cocolvis"
        },
        {
            "Model type": "Lightweight model",
            "Applicable scene": "Suitable for general labeling",
            "Model structure": "HRNet18s_OCR48",
            "Model name": "static_hrnet18s_ocr48_cocolvis"
        },
        {
            "Model type": "High precision model",
            "Applicable scene": "Suitable for human portrait labeling",
            "Model structure": "HRNet18_OCR64",
            "Model name": "static_hrnet18_ocr64_human"
        },
        {
            "Model type": "Lightweight model",
            "Applicable scene": "Suitable for human portrait labeling",
            "Model structure": "HRNet18s_OCR48",
            "Model name": "static_hrnet18s_ocr48_human"
        },
        {
            "Model type": "High precision model",
            "Applicable scene": "Suitable for general labeling",
            "Model structure": "EdgeFlow",
            "Model name": "static_edgeflow_cocolvis"
        },
        {
            "Model type": "Lightweight model",
            "Applicable scene": "Suitable for human portrait labeling",
            "Model structure": "HRNet18s_OCR48",
            "Model name": "static_hrnet18_ocr48_rsbuilding_instance"
        },
        {
            "Model type": "Lightweight model",
            "Applicable scene": "Suitable for medical scenes of liver labeling",
            "Model structure": "HRNet18s_OCR48",
            "Model name": "static_hrnet18s_ocr48_lits"
        },
    ]


def get_table_columns():
    return [
        {"key": "Model", "title": "Model", "subtitle": None},
        {"key": "Size", "title": "Size", "subtitle": "(pixels)"},
        {"key": "mAP^val", "title": "mAP<sub>val</sub>", "subtitle": "0.5:0.95"},
        {"key": "mAP^test", "title": "mAP<sub>test</sub>", "subtitle": "0.5:0.95"},
        {"key": "mAP^val_0.5", "title": "mAP<sub>val</sub>", "subtitle": "0.5"},
        {"key": "Speed", "title": "Speed", "subtitle": "V100 (ms)"},
        {"key": "Params", "title": "Params", "subtitle": "(M)"},
        {"key": "FLOPS", "title": "FLOPS", "subtitle": "640 (B)"},
    ]


def init(data, state):
    data["models"] = get_models_list()
    data["modelColumns"] = get_table_columns()
    state["selectedModel"] = "YOLOv5s"
    state["weightsInitialization"] = "coco"

    # @TODO: for debug
    #state["weightsPath"] = "/yolov5_train/coco128_002/2390/weights/best.pt"
    state["weightsPath"] = ""


def prepare_weights(state):
    if state["weightsInitialization"] == "custom":
        # download custom weights
        weights_path_remote = state["weightsPath"]
        if not weights_path_remote.endswith(".pt"):
            raise ValueError(f"Weights file has unsupported extension {sly.fs.get_file_ext(weights_path_remote)}. "
                             f"Supported: '.pt'")
        weights_path_local = os.path.join(g.my_app.data_dir, sly.fs.get_file_name_with_ext(weights_path_remote))
        file_info = g.api.file.get_info_by_path(g.team_id, weights_path_remote)
        if file_info is None:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), weights_path_remote)
        progress_cb = get_progress_cb("Download weights", file_info.sizeb, is_size=True)
        g.api.file.download(g.team_id, weights_path_remote, weights_path_local, g.my_app.cache, progress_cb)

        state["_weightsPath"] = weights_path_remote
        state["weightsPath"] = weights_path_local
    else:
        model_name = state['selectedModel'].lower()
        state["weightsPath"] = f"{model_name}.pt"
        sly.logger.info("Pretrained COCO weights will be added automatically")