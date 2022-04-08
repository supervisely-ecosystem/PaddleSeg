# cuda:11.1-cudnn8-runtime-ubuntu20.04 + py3.8 + opencv + other bacis CV packages
# learn more here: https://github.com/supervisely/supervisely/blob/master/base_images/py/Dockerfile
FROM supervisely/base-py-sdk:6.9.2

COPY eiseg_models /eiseg_models

# install pytorch
RUN pip3 install supervisely==6.9.2 supervisely[apps]==6.9.2 pre-commit yapf==0.26.0
RUN pip3 install flake8 pyyaml>=5.1 visualdl>=2.0.0
RUN pip3 install opencv-python tqdm scipy filelock
RUN pip3 install prettytable eiseg paddlepaddle pyqt5
RUN pip3 install qtpy paddleseg albumentations
RUN pip3 install cython wget diskcache==5.2.1
