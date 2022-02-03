<<<<<<< HEAD
English | [简体中文](data_prepare_cn.md)

# Dataset Preparation

PaddleSeg currently supports the dataset of CityScapes, ADE20K, Pascal VOC and so on.
When loading a dataset, the system automatically triggers the download (except for Cityscapes dataset) if the data does not exist locally.

## CityScapes Dataset
Cityscapes is a dataset of semantically understood images of urban street scenes. It mainly contains street scenes from 50 different cities, with 5000 (2048 x 1024) high quality pixel-level annotated images of urban driving scenes. It contains 19 categories. There are 2975 training sets, 500 validation sets and 1525 test sets.

Due to restrictions, please visit [CityScapes website](https://www.cityscapes-dataset.com/)to download dataset.
We recommend that you store dataset in `PaddleSeg/data` for full compatibility with our config files. Please organize the dataset into the following structure after downloading:

```
=======
# 数据集准备

PaddleSeg目前支持CityScapes、ADE20K、Pascal VOC等数据集的加载，在加载数据集时，如若本地不存在对应数据，则会自动触发下载(除Cityscapes数据集).

## 关于CityScapes数据集
Cityscapes是关于城市街道场景的语义理解图片数据集。它主要包含来自50个不同城市的街道场景，
拥有5000张（2048 x 1024）城市驾驶场景的高质量像素级注释图像，包含19个类别。其中训练集2975张， 验证集500张和测试集1525张。

由于协议限制，请自行前往[CityScapes官网](https://www.cityscapes-dataset.com/)下载数据集，
我们建议您将数据集存放于`PaddleSeg/data`中，以便与我们配置文件完全兼容。数据集下载后请组织成如下结构：

>>>>>>> 9c8570af (add new models)
    cityscapes
    |
    |--leftImg8bit
    |  |--train
    |  |--val
    |  |--test
    |
    |--gtFine
    |  |--train
    |  |--val
    |  |--test
<<<<<<< HEAD
```

Run the following command to convert labels:
=======

运行下列命令进行标签转换：
>>>>>>> 9c8570af (add new models)
```shell
pip install cityscapesscripts
python tools/convert_cityscapes.py --cityscapes_path data/cityscapes --num_workers 8
```
<<<<<<< HEAD
where `cityscapes_path` should be adjusted according to the actual dataset path. `num_workers` determines the number of processes to be started. The value can be adjusted as required.

## Pascal VOC 2012 dataset
[Pascal VOC 2012](http://host.robots.ox.ac.uk/pascal/VOC/) is mainly object segmentation, including 20 categories and background classes, including 1464 training sets and 1449 validation sets.
Generally, we will use [SBD(Semantic Boundaries Dataset)](http://home.bharathh.info/pubs/codes/SBD/download.html) to expand the dataset. Theer are 10582 training sets after expanding.
Run the following commands to download the SBD dataset and use it to expand:
```shell
python tools/voc_augment.py --voc_path data/VOCdevkit --num_workers 8
```
where `voc_path`should be adjusted according to the actual dataset path.

**Note** Before running, make sure you have executed the following commands in the PaddleSeg directory:
```shell
export PYTHONPATH=`pwd`
# In Windows, run the following command
# set PYTHONPATH=%cd%
```

## ADE20K Dataset
[ADE20K](http://sceneparsing.csail.mit.edu/) published by MIT that can be used for a variety of tasks such as scene perception, segmentation, and multi-object recognition.
It covers 150 semantic categories, including 20210 training sets and 2000 validation sets.

## Coco Stuff Dataset
Coco Stuff is a pixel-level semantically segmented dataset based on Coco datasets. It covers 172 catefories, including 80 'thing' classes, 91 'stuff' classes amd one 'unlabeled' classes. 'unlabeled' is ignored and the index is set to 255 which has not contribution to loss. The training version is therefore provided in 171 categories. There are 118k training sets, 5k validation sets.

Before using Coco Stuff dataset， please go to [COCO-Stuff website](https://github.com/nightrome/cocostuff) to download dataset or download [coco2017 training sets with origin images](http://images.cocodataset.org/zips/train2017.zip), [coco2017 validation sets with origin images](http://images.cocodataset.org/zips/val2017.zip) and [annotations images](http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/stuffthingmaps_trainval2017.zip)
We recommend that you store dataset in `PaddleSeg/data` for full compatibility with our config files. Please organize the dataset into the following structure after downloading:

```
=======
其中`cityscapes_path`应根据实际数据集路径进行调整。 `num_workers`决定启动的进程数，可根据实际情况进行调整大小。

## 关于Pascal VOC 2012数据集
[Pascal VOC 2012](http://host.robots.ox.ac.uk/pascal/VOC/)数据集以对象分割为主，包含20个类别和背景类，其中训练集1464张，验证集1449张。
通常情况下会利用[SBD(Semantic Boundaries Dataset)](http://home.bharathh.info/pubs/codes/SBD/download.html)进行扩充，扩充后训练集10582张。
运行下列命令进行SBD数据集下载并进行扩充：
```shell
python tools/voc_augment.py --voc_path data/VOCdevkit --num_workers 8
```
其中`voc_path`应根据实际数据集路径进行调整。

**注意** 运行前请确保在PaddleSeg目录下执行过下列命令：
```shell
export PYTHONPATH=`pwd`
# windows下请执行相面的命令
# set PYTHONPATH=%cd%
```

## 关于ADE20K数据集
[ADE20K](http://sceneparsing.csail.mit.edu/)由MIT发布的可用于场景感知、分割和多物体识别等多种任务的数据集。
其涵盖了150个语义类别，包括训练集20210张，验证集2000张。

## 关于Coco Stuff数据集
Coco Stuff是基于Coco数据集的像素级别语义分割数据集。它主要覆盖172个类别，包含80个'thing'，91个'stuff'和1个'unlabeled',我们忽略'unlabeled'类别，并将其index设为255，不记录损失。因此提供的训练版本为171个类别。其中，训练集118k, 验证集5k.

在使用Coco Stuff数据集前， 请自行前往[COCO-Stuff主页](https://github.com/nightrome/cocostuff)下载数据集，或者下载[coco2017训练集原图](http://images.cocodataset.org/zips/train2017.zip), [coco2017验证集原图](http://images.cocodataset.org/zips/val2017.zip)及[标注图](http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/stuffthingmaps_trainval2017.zip)
我们建议您将数据集存放于`PaddleSeg/data`中，以便与我们配置文件完全兼容。数据集下载后请组织成如下结构：

>>>>>>> 9c8570af (add new models)
    cocostuff
    |
    |--images
    |  |--train2017
    |  |--val2017
    |
    |--annotations
    |  |--train2017
    |  |--val2017
<<<<<<< HEAD
```

Run the following command to convert labels:
=======

运行下列命令进行标签转换：
>>>>>>> 9c8570af (add new models)

```shell
python tools/convert_cocostuff.py --annotation_path /PATH/TO/ANNOTATIONS --save_path /PATH/TO/CONVERT_ANNOTATIONS
```
<<<<<<< HEAD
where `annotation_path` should be filled according to the `cocostuff/annotations` actual path. `save_path` determines the location of the converted label.

Where, the labels of the labeled images are taken in sequence from 0, 1, ... and cannot be separated. If there are pixels that need to be ignored, they should be labeled to 255.

## Pascal Context Dataset
Pascal Context is a pixel-level semantically segmented dataset based on the Pascal VOC 2010 dataset with additional annotations. The conversion script we provide supports 60 categories, with index 0 being the background category. There are 4996 training sets and 5104 verification sets in this dataset.


Before using Pascal Context dataset， Please download [VOC2010](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCtrainval_03-May-2010.tar) firstly，then go to [Pascal-Context home page](https://www.cs.stanford.edu/~roozbeh/pascal-context/)to download dataset and [annotations](https://codalabuser.blob.core.windows.net/public/trainval_merged.json)
We recommend that you store dataset in `PaddleSeg/data` for full compatibility with our config files. Please organize the dataset into the following structure after downloading:

```
=======
其中`annotation_path`应根据下载cocostuff/annotations文件夹的实际路径填写。 `save_path`决定转换后标签的存放位置。


其中，标注图像的标签从0,1依次取值，不可间隔。若有需要忽略的像素，则按255进行标注。

## 关于Pascal Context数据集
Pascal Context是基于PASCAL VOC 2010数据集额外标注的像素级别的语义分割数据集。我们提供的转换脚本支持60个类别，index为0是背景类别。该数据集中中训练集4996, 验证集5104张. 


在使用Pascal Context数据集前， 请先下载[VOC2010](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCtrainval_03-May-2010.tar)，随后自行前往[Pascal-Context主页](https://www.cs.stanford.edu/~roozbeh/pascal-context/)下载数据集及[标注](https://codalabuser.blob.core.windows.net/public/trainval_merged.json)
我们建议您将数据集存放于`PaddleSeg/data`中，以便与我们配置文件完全兼容。数据集下载后请组织成如下结构：

>>>>>>> 9c8570af (add new models)
    VOC2010
    |
    |--Annotations
    |
    |--ImageSets
    |
    |--SegmentationClass
    |  
    |--JPEGImages
    |
    |--SegmentationObject
    |
    |--trainval_merged.json
<<<<<<< HEAD
```

Run the following command to convert labels:
=======
    
 
运行下列命令进行标签转换：
>>>>>>> 9c8570af (add new models)

```shell
python tools/convert_voc2010.py --voc_path /PATH/TO/VOC ----annotation_path /PATH/TO/JSON
```
<<<<<<< HEAD
where `voc_path` should be filled according to the voc2010 actual path. `annotation_path` is the trainval_merged.json saved path.


Where, the labels of the labeled images are taken in sequence from 0, 1, 2, ... and cannot be separated. If there are pixels that need to be ignored, they should be labeled to 255 (default ignored value). When using Pascal Context dataset, [Detail](https://github.com/zhanghang1989/detail-api) need to be installed.


## Custom Dataset

If you need to use a custom dataset for training, prepare the data as following steps.

1.The following structure is recommended

```
=======
其中`voc_path`应根据下载VOC2010文件夹的实际路径填写。 `annotation_path`决定下载trainval_merged.json的存放位置。



其中，标注图像的标签从0，1，2依次取值，不可间隔。若有需要忽略的像素，则按255(默认的忽略值）进行标注。在使用Pascal Context数据集时，需要安装[Detail](https://github.com/zhanghang1989/detail-api).

## 自定义数据集

如果您需要使用自定义数据集进行训练，请按照以下步骤准备数据.

1.推荐整理成如下结构

>>>>>>> 9c8570af (add new models)
    custom_dataset
        |
        |--images
        |  |--image1.jpg
        |  |--image2.jpg
        |  |--...
        |
        |--labels
        |  |--label1.jpg
        |  |--label2.png
        |  |--...
        |
        |--train.txt
        |
        |--val.txt
        |
        |--test.txt
<<<<<<< HEAD
```

The content of train.txt and val.txt is as following：

```
    images/image1.jpg labels/label1.png
    images/image2.jpg labels/label2.png
    ...
```

2.The labels of the labeled images are taken in sequence from 0, 1, ... and cannot be separated. If there are pixels that need to be ignored, they should be labeled to 255.

You can configure a custom dataset as following：
=======

其中train.txt和val.txt的内容如下所示：

    images/image1.jpg labels/label1.png
    images/image2.jpg labels/label2.png
    ...

2.标注图像的标签从0,1依次取值，不可间隔。若有需要忽略的像素，则按255进行标注。

可按如下方式对自定义数据集进行配置：
>>>>>>> 9c8570af (add new models)
```yaml
train_dataset:
  type: Dataset
  dataset_root: custom_dataset
  train_path: custom_dataset/train.txt
  num_classes: 2
  transforms:
    - type: ResizeStepScaling
      min_scale_factor: 0.5
      max_scale_factor: 2.0
      scale_step_size: 0.25
    - type: RandomPaddingCrop
      crop_size: [512, 512]
    - type: RandomHorizontalFlip
    - type: Normalize
  mode: train
```
