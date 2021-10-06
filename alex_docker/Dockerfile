FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
	    git \
	    curl \
        libglib2.0-0 \
        software-properties-common \
        python3.6-dev \
        python3-pip \
        python3-tk

WORKDIR /tmp

RUN pip3 install --upgrade pip

RUN pip3 install pyqt5
RUN pip3 install qtpy
RUN pip3 install opencv-python
RUN pip3 install scipy
RUN pip3 install paddleseg
RUN pip3 install albumentations
RUN pip3 install cython
RUN pip3 install pyyaml
RUN apt-get install wget
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install eiseg
RUN pip3 install paddlepaddle
RUN pip3 install setuptools

WORKDIR /src
