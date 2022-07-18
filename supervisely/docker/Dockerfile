# cuda:11.1-cudnn8-runtime-ubuntu20.04 + py3.8 + opencv + other bacis CV packages
# learn more here: https://github.com/supervisely/supervisely/blob/master/base_images/py/Dockerfile
FROM supervisely/base-py-sdk:6.14.0

RUN mkdir /eiseg_models
# download checkpoints
RUN wget -O /eiseg_models/static_edgeflow_cocolvis.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_edgeflow_cocolvis.pdiparams
RUN wget -O /eiseg_models/static_edgeflow_cocolvis.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_edgeflow_cocolvis.pdmodel

RUN wget -O /eiseg_models/static_hrnet18s_ocr48_aluminium.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_aluminium.pdiparams
RUN wget -O /eiseg_models/static_hrnet18s_ocr48_aluminium.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_aluminium.pdmodel

RUN wget -O /eiseg_models/static_hrnet18s_ocr48_cocolvis.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_cocolvis.pdiparams
RUN wget -O /eiseg_models/static_hrnet18s_ocr48_cocolvis.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_cocolvis.pdmodel

RUN wget -O /eiseg_models/static_hrnet18s_ocr48_human.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_human.pdiparams
RUN wget -O /eiseg_models/static_hrnet18s_ocr48_human.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_human.pdmodel

RUN wget -O /eiseg_models/static_hrnet18s_ocr48_lits.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_lits.pdiparams
RUN wget -O /eiseg_models/static_hrnet18s_ocr48_lits.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_lits.pdmodel

RUN wget -O /eiseg_models/static_hrnet18s_ocr48_MRSpineSeg.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_MRSpineSeg.pdiparams
RUN wget -O /eiseg_models/static_hrnet18s_ocr48_MRSpineSeg.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18s_ocr48_MRSpineSeg.pdmodel

RUN wget -O /eiseg_models/static_hrnet18_ocr48_rsbuilding_instance.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr48_rsbuilding_instance.pdiparams
RUN wget -O /eiseg_models/static_hrnet18_ocr48_rsbuilding_instance.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr48_rsbuilding_instance.pdmodel

RUN wget -O /eiseg_models/static_hrnet18_ocr64_cocolvis.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr64_cocolvis.pdiparams
RUN wget -O /eiseg_models/static_hrnet18_ocr64_cocolvis.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr64_cocolvis.pdmodel

RUN wget -O /eiseg_models/static_hrnet18_ocr64_human.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr64_human.pdiparams
RUN wget -O /eiseg_models/static_hrnet18_ocr64_human.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_hrnet18_ocr64_human.pdmodel

RUN wget -O /eiseg_models/static_resnet18_deeplab_chest_xray.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_resnet18_deeplab_chest_xray.pdiparams
RUN wget -O /eiseg_models/static_resnet18_deeplab_chest_xray.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_resnet18_deeplab_chest_xray.pdmodel

RUN wget -O /eiseg_models/static_resnet50_deeplab_chest_xray.pdiparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_resnet50_deeplab_chest_xray.pdiparams
RUN wget -O /eiseg_models/static_resnet50_deeplab_chest_xray.pdmodel https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.3.4/static_resnet50_deeplab_chest_xray.pdmodel

# install pytorch
RUN pip3 install supervisely==6.14.0 supervisely[apps]==6.14.0 supervisely[extras]==6.14.0
RUN pip3 install pre-commit yapf==0.26.0 flake8 pyyaml>=5.1 visualdl>=2.0.0
RUN pip3 install opencv-python tqdm scipy filelock
RUN pip3 install prettytable eiseg paddlepaddle pyqt5
RUN pip3 install qtpy paddleseg albumentations
RUN pip3 install cython wget diskcache==5.2.1
