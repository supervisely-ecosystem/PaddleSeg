# cuda:11.1-cudnn8-runtime-ubuntu20.04 + py3.8 + opencv + other basic CV packages
# learn more here: https://github.com/supervisely/supervisely/blob/master/base_images/py/Dockerfile

FROM supervisely/base-py-sdk:6.1.98

COPY eiseg_models /eiseg_models

# install pytorch
RUN pip3 install supervisely==6.1.98 pre-commit yapf==0.26.0
RUN pip3 install flake8 pyyaml>=5.1 visualdl>=2.0.0
RUN pip3 install opencv-python tqdm scipy filelock
RUN pip3 install prettytable eiseg paddlepaddle paddlepaddle-gpu
RUN pip3 install pyqt5 qtpy paddleseg albumentations
RUN pip3 install cython wget diskcache==5.2.1

RUN ln -s /usr/lib/x86_64-linux-gnu/libcudnn.so.8 /usr/local/cuda/lib64/libcudnn.so && \
    ln -s /usr/local/cuda/lib64/libcublas.so.11 /usr/local/cuda/lib64/libcublas.so && \
    ln -s /usr/local/cuda/lib64/libcusolver.so.11 /usr/local/cuda/lib64/libcusolver.so