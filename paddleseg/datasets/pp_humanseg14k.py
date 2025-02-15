<<<<<<< HEAD:paddleseg/datasets/stare.py
# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
=======
# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
>>>>>>> PaddlePaddle-release/2.4:paddleseg/datasets/pp_humanseg14k.py
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

<<<<<<< HEAD:paddleseg/datasets/stare.py
from paddleseg.utils.download import download_file_and_uncompress
from paddleseg.utils import seg_env
=======
from .dataset import Dataset
>>>>>>> PaddlePaddle-release/2.4:paddleseg/datasets/pp_humanseg14k.py
from paddleseg.cvlibs import manager
from paddleseg.transforms import Compose
from paddleseg.datasets import Dataset

URL = 'https://bj.bcebos.com/paddleseg/dataset/stare/stare.zip'


@manager.DATASETS.add_component
<<<<<<< HEAD:paddleseg/datasets/stare.py
class STARE(Dataset):
    """
    STARE dataset is processed from the STARE(STructured Analysis of the Retina) project.
    (https://cecas.clemson.edu/~ahoover/stare/)

    Args:
        transforms (list): Transforms for image.
        dataset_root (str): The dataset directory. Default: None
        edge (bool): whether extract edge infor in the output
        mode (str, optional): Which part of dataset to use. it is one of ('train', 'val', 'test'). Default: 'train'.
=======
class PPHumanSeg14K(Dataset):
    """
    This is the PP-HumanSeg14K Dataset.

    This dataset was introduced in the work:
    Chu, Lutao, et al. "PP-HumanSeg: Connectivity-Aware Portrait Segmentation with a Large-Scale Teleconferencing Video Dataset." Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision. 2022.

    This dataset is divided into training set, validation set and test set. The training set includes 8770 pictures, the validation set includes 2431 pictures, and the test set includes 2482 pictures.

    Args:
        dataset_root (str, optional): The dataset directory. Default: None.
        transforms (list, optional): Transforms for image. Default: None.
        mode (str, optional): Which part of dataset to use. It is one of ('train', 'val'). Default: 'train'.
        edge (bool, optional): Whether to compute edge while training. Default: False.
>>>>>>> PaddlePaddle-release/2.4:paddleseg/datasets/pp_humanseg14k.py
    """
    NUM_CLASSES = 2

    def __init__(self,
                 dataset_root=None,
                 transforms=None,
                 edge=False,
                 mode='train'):
        self.dataset_root = dataset_root
        self.transforms = Compose(transforms)
        mode = mode.lower()
        self.mode = mode
        self.edge = edge
        self.file_list = list()
        self.num_classes = self.NUM_CLASSES
        self.ignore_index = 255

        if mode not in ['train', 'val', 'test']:
            raise ValueError(
                "`mode` should be 'train', 'val' or 'test', but got {}.".format(
                    mode))

        if self.transforms is None:
            raise ValueError("`transforms` is necessary, but it is None.")

        if self.dataset_root is None:
            self.dataset_root = download_file_and_uncompress(
                url=URL,
                savepath=seg_env.DATA_HOME,
                extrapath=seg_env.DATA_HOME)
        elif not os.path.exists(self.dataset_root):
            self.dataset_root = os.path.normpath(self.dataset_root)
            savepath, extraname = self.dataset_root.rsplit(
                sep=os.path.sep, maxsplit=1)  # data  STARE
            self.dataset_root = download_file_and_uncompress(
                url=URL,
                savepath=savepath,
                extrapath=savepath,
                extraname=extraname)

        if mode == 'train':
            file_path = os.path.join(self.dataset_root, 'train_list.txt')
        elif mode == 'val':
            file_path = os.path.join(self.dataset_root, 'val_list.txt')

        with open(file_path, 'r') as f:
            for line in f:
                items = line.strip().split(' ')
                if len(items) != 2:
                    if mode == 'train' or mode == 'val':
                        raise Exception(
                            "File list format incorrect! It should be"
                            " image_name label_name\\n")
                    image_path = os.path.join(self.dataset_root, items[0])
                    grt_path = None
                else:
                    image_path = os.path.join(self.dataset_root, items[0])
                    grt_path = os.path.join(self.dataset_root, items[1])
                self.file_list.append([image_path, grt_path])
