# cuda:11.1-cudnn8-runtime-ubuntu20.04 + py3.8 + opencv + other bacis CV packages
# learn more here: https://github.com/supervisely/supervisely/blob/master/base_images/py/Dockerfile
FROM supervisely/base-py-sdk:6.1.98

RUN mkdir /eiseg_models
# download checkpoints
RUN wget -O /eiseg_models/hrnet18_ocr64_cocolvis.pdparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18_ocr64_cocolvis.pdparams
RUN wget -O /eiseg_models/hrnet18s_ocr48_cocolvis.pdparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18s_ocr48_cocolvis.pdparams
RUN wget -O /eiseg_models/hrnet18_ocr64_human.pdparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18_ocr64_human.pdparams
RUN wget -O /eiseg_models/hrnet18s_ocr48_human.pdparams https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/hrnet18s_ocr48_human.pdparams

# install pytorch
RUN pip3 install supervisely==6.1.98 pre-commit yapf==0.26.0
RUN pip3 install flake8 pyyaml>=5.1 visualdl>=2.0.0
RUN pip3 install opencv-python tqdm scipy filelock
RUN pip3 install prettytable eiseg paddlepaddle pyqt5
RUN pip3 install qtpy paddleseg albumentations
RUN pip3 install cython wget diskcache==5.2.1
