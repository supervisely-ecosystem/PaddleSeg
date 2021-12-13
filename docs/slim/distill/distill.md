<<<<<<< HEAD
# Model Distillation Tutorial

# 1. Introduction

Based on the idea of teacher and student, model distillation uses big teacher model to teach small student model in the training stage, which is a common method of model compression.
Compared to training the small model alone, model distillation is usually benficial for higher accuracy.
If you are interested in the theory of model distillation, there are a survey in [arxiv](https://arxiv.org/abs/2006.05525).

Based on PaddleSlim, PaddleSeg provides the module of model distillation. The key points of using model distillation are as follows:
* Chose the teacher and student models
* Train the teacher model
* Set the config files of model distillation
* Training of model distillation, namely train the student with the guidance of the teacher model

In this tutorial, we demonstrate a demo of model distillation, and then present the advanced usage of model distillation.

# 2. Model Distillation Demo

### 2.1 Requirements

Please follow [installation document](../../install.md) to install the requirements of PaddleSeg.

Besides, run the following instructions to install PaddleSlim.
=======
# 模型蒸馏教程

## 1 简介

模型蒸馏基于”教师-学生模型“的思想，使用大的教师模型指导小的学生模型进行训练，是一种常见的模型压缩方法。相比于单独训练学生模型，模型蒸馏通常可以提升学生模型的精度。

常规的模型训练中，模型前向计算的输出和真实label计算得到常规loss，再进行梯度反向传播。
常见的模型蒸馏训练中，教师模型只有前向计算，学生模型有前向计算和反向传播，有多个loss指导学生模型进行训练：学生模型前向计算的输出和真实label计算得到常规loss；学生模型前向计算的输出和教师模型前向计算的输出计算得到蒸馏loss。
更多模型蒸馏的介绍，请参考[Survey](https://arxiv.org/abs/2006.05525)。

PaddleSeg基于PaddleSlim，集成了模型蒸馏的功能，主要使用步骤是：
* 选定学生模型和教师模型；
* 训练教师模型；
* 蒸馏参数配置；
* 进行模型蒸馏的训练，得到训练好的学生模型。

以下，我们首先以一个模型蒸馏的示例进行说明，然后介绍一些高阶使用方法。

## 2 模型蒸馏示例

### 2.1 环境准备

请参考[安装文档](../../install.md)准备好PaddleSeg的基础环境，测试是否安装成功。

安装PaddleSlim。
>>>>>>> 9c8570af (add new models)

```shell
git clone https://github.com/PaddlePaddle/PaddleSlim.git

<<<<<<< HEAD
# checkout to special commit 
git reset --hard 15ef0c7dcee5a622787b7445f21ad9d1dea0a933

# install
python setup.py install
```

### 2.2 Chose the Teacher and Student Models

In this demo, DeepLabV3P_ResNet50_vd is the teacher model and  DeepLabV3P_ResNet18_vd is the student model. Besides, we use the optic disc segmentation dataset for simplicity.

### 2.3 Train the Teacher Model

The config file of the teacher model is `PaddleSeg/configs/quick_start/deeplabv3p_resnet50_os8_optic_disc_512x512_1k_teacher.yml`.

Run the following instructions in the root directory of PaddleSeg to train the teacher model.

```shell
export CUDA_VISIBLE_DEVICES=0  # Set GPU for Linux
# set CUDA_VISIBLE_DEVICES=0   # Seg GPU for Windows 

=======
# 切换到特定commit id
git reset --hard 15ef0c7dcee5a622787b7445f21ad9d1dea0a933

# 安装
python setup.py install
```

### 2.2 选定学生和教师模型

示例中，我们使用视盘分割（optic disc segmentation）数据集，教师模型是以ResNet50_vd为Backbone的DeepLabV3P（简称DeepLabV3P_ResNet50_vd），学生模型是以ResNet18_vd为Backbone的DeepLabV3P（简称DeepLabV3P_ResNet18_vd）。

### 2.3 训练教师模型

教师模型DeepLabV3P_ResNet50_vd的config文件在`PaddleSeg/configs/quick_start/deeplabv3p_resnet50_os8_optic_disc_512x512_1k_teacher.yml`，具体参数不再赘述。

执行如下命令，指定使用的GPU卡。

```
# Linux下，设置1张可用的卡
export CUDA_VISIBLE_DEVICES=0

# windows下请执行以下命令
# set CUDA_VISIBLE_DEVICES=0
```

在PaddleSeg根目录下执行如下命令，训练教师模型。

```
>>>>>>> 9c8570af (add new models)
python train.py \
    --config configs/quick_start/deeplabv3p_resnet50_os8_optic_disc_512x512_1k_teacher.yml \
    --do_eval \
    --use_vdl \
    --save_interval 250 \
    --num_workers 3 \
    --seed 0 \
    --save_dir output/deeplabv3p_resnet50
```

<<<<<<< HEAD
After the traing, the mIoU of the teacher model is 91.54% and the trained weights are saved in `output/deeplabv3p_resnet50/best_model/model.pdparams`.

### 2.4 Train the Student Model (Optional)

In this step, we train the student model without the guidance of the teacher model.  

The config file of the student model is `PaddleSeg/configs/quick_start/deeplabv3p_resnet18_os8_optic_disc_512x512_1k_student.yml`.

Run the following instructions in the root directory of PaddleSeg to train the student model alone.

```shell
export CUDA_VISIBLE_DEVICES=0  # Set GPU for Linux
# set CUDA_VISIBLE_DEVICES=0   # Seg GPU for Windows 

=======
训练结束后，教师模型的mIou为91.54%(实际可能有点差异)，对应的权重保存在`output/deeplabv3p_resnet50/best_model/model.pdparams`。

### 2.4 训练学生模型

为了和蒸馏训练对比学生模型的精度，这里先单独训练学生模型。此步骤非必须，只是为了对比观察，大家可以视情况跳过。

学生模型DeepLabV3P_ResNet18_vd的config文件在`PaddleSeg/configs/quick_start/deeplabv3p_resnet18_os8_optic_disc_512x512_1k_student.yml`。

在PaddleSeg根目录下执行如下命令，训练学生模型。

```
>>>>>>> 9c8570af (add new models)
python train.py \
    --config configs/quick_start/deeplabv3p_resnet18_os8_optic_disc_512x512_1k_student.yml \
    --do_eval \
    --use_vdl \
    --save_interval 250 \
    --num_workers 3 \
    --seed 0 \
    --save_dir output/deeplabv3p_resnet18
```

<<<<<<< HEAD
The mIoU of the student model is 83.93% and the trained weights are saved in `output/deeplabv3p_resnet18/best_model/model.pdparams`.


### 2.5 Set the Config File of Model Distillation

The training of model distillation needs the config files of the teacher and student models.

We open the teacher config file (`PaddleSeg/configs/quick_start/deeplabv3p_resnet50_os8_optic_disc_512x512_1k_teacher.yml`) and set the pretrained in the last line as the path of the teacher model's weights as follows.

```shell
=======
训练结束后，教师模型的mIou为83.93%(实际可能有点差异)，对应的权重保存在`output/deeplabv3p_resnet18/best_model/model.pdparams`。

### 2.5 蒸馏配置

修改教师模型的config文件（`PaddleSeg/configs/quick_start/deeplabv3p_resnet50_os8_optic_disc_512x512_1k_teacher.yml`），将文件中最后一行pretrained字段设置为”训练教师模型”步骤中的权重路径，如下所示。

```
>>>>>>> 9c8570af (add new models)
model:
  type: DeepLabV3P
  backbone:
    type: ResNet50_vd
    output_stride: 8
    multi_grid: [1, 2, 4]
    pretrained: Null
  num_classes: 2
  backbone_indices: [0, 3]
  aspp_ratios: [1, 12, 24, 36]
  aspp_out_channels: 256
  align_corners: False
  pretrained: output/deeplabv3p_resnet50/best_model/model.pdparams
```

<<<<<<< HEAD
It is not necessary to modify the config file of the student model. Note that, the config file has normal loss and distillation loss.

```shell
=======
学生模型的config文件中，除了常规loss，还新增了distill_loss，如下所示。
常规loss是配置学生模型输出和真实label的损失计算，distill_loss是配置学生模型输出和教师模型输出的损失计算，types表示loss类型，coef是loss的比例系数。distill_loss types目前仅支持设置为KLLoss。

```
>>>>>>> 9c8570af (add new models)
loss:
  types:
    - type: CrossEntropyLoss
  coef: [1]

# distill_loss is used for distillation
distill_loss:
  types:
    - type: KLLoss
  coef: [3]
```

<<<<<<< HEAD
### 2.6 Training of Model Distillation

With the config files of the teacher and student models, run the following instructions in the root directory of PaddleSeg to train the student model with the guidance of the teacher model.

```shell
export CUDA_VISIBLE_DEVICES=0  # Set GPU for Linux
# set CUDA_VISIBLE_DEVICES=0   # Seg GPU for Windows 

=======
### 2.6 蒸馏训练

基于学生和教师模型的配置文件，在PaddleSeg根目录下执行如下命令，调用蒸馏的接口`slim/distill/distill_train.py`，进行蒸馏训练。

```
>>>>>>> 9c8570af (add new models)
python slim/distill/distill_train.py \
       --teather_config ./configs/quick_start/deeplabv3p_resnet50_os8_optic_disc_512x512_1k_teacher.yml \
       --student_config ./configs/quick_start/deeplabv3p_resnet18_os8_optic_disc_512x512_1k_student.yml \
       --do_eval \
       --use_vdl \
       --save_interval 250 \
       --num_workers 3 \
       --seed 0 \
       --save_dir output/deeplabv3p_resnet18_distill
```

<<<<<<< HEAD
The script of `slim/distill/distill_train.py` creates the teacher model, creates the student model, loads dataset to train the student model while the teacher model is fixed. 

After the training, the mIoU of the student model is 85.79% and the trained weights are saved in `output/deeplabv3p_resnet18_distill/best_model`.

Compared the accuracy of these two student models, the model distillation imporves the mIoU by 1.86%.

## 3. Advanced Usage of Model Distillation

### 3.1 Single-Machine Multiple-GPUs Training

In order to accelerate the training of model distillation with single machine multiple GPUs, we export `CUDA_VISIBLE_DEVICES` and use `paddle.distributed.launch` to start the script as follows. Note that, PaddlePaddle does not support single machine multiple GPUs training on Windows.

```shell
export CUDA_VISIBLE_DEVICES=0,1,2,3 # use four GPUs
=======
在蒸馏训练中，使用教师模型配置文件中model配置信息创建教师模型，使用学生模型配置文件中model配置信息创建学生模型，使用学生模型中dataset、loss、optimizer等配置信息执行训练。

注意，蒸馏训练会加载两个模型，显存占用较大(9G)，所以大家需要根据实际情况调整batch_size。

蒸馏训练结束后，学生模型的mIoU是85.79%(实际可能有点差异)，对应权重保存在`output/deeplabv3p_resnet18_distill/best_model`。

对比发现，单独训练的学生模型mIoU是83.93%，蒸馏训练的学生模型mIoU是85.79%，mIoU提高了1.86%。

## 3 高阶使用方法

### 3.1 多卡训练

如果模型蒸馏想要使用多卡训练，需要将环境变量CUDA_VISIBLE_DEVICES指定为多卡（不指定时默认使用所有的gpu)，并使用`paddle.distributed.launch`启动训练脚本。注意，由于windows下不支持nccl，无法使用多卡训练。

```
export CUDA_VISIBLE_DEVICES=0,1,2,3 # 设置4张可用的卡
>>>>>>> 9c8570af (add new models)

python -m paddle.distributed.launch slim/distill/distill_train.py \
       --teather_config ./configs/quick_start/deeplabv3p_resnet50_os8_optic_disc_512x512_1k_teacher.yml \
       --student_config ./configs/quick_start/deeplabv3p_resnet18_os8_optic_disc_512x512_1k_student.yml \
       --do_eval \
       --use_vdl \
       --save_interval 250 \
       --num_workers 3 \
       --seed 0 \
       --save_dir output/deeplabv3p_resnet18_distill
```

<<<<<<< HEAD
### 3.2 The Weights of Losses

In the config file of the student model, the `coef` means the weight of the according loss, such as the normal loss and distill_loss.
You can adjust the weights of different losses to imporve the accuracy.


### 3.3 Use Intermediate Tensors for Distillation 

Model distillation only utilizes the output tensors of the teacher and student models in the above demo for simplicity. 
In fact, we can also use intermediate tensors for model distillation.

* Chose the intermediate tensors in the teacher and student models

It requires the intermediate tensors in the teacher and student models have the same shape for now.

* Set the intermediate tensors for distillation

In Paddeseg, the `slim/distill/distill_config.py` file has a "prepare_distill_adaptor" function. We utilize the StudentAdaptor and TeatherAdaptor class to set the intermediate tensors for model distillation.

Generally speaking, PaddlePaddle has two types of api. The first type is layer api, of which the base class is "paddle.nn.Layer", such as "paddle.nn.Conv2D". The second type is function api, such as paddle.reshape.

If the intermediate tensor is the output of layer api, we set the `mapping_layers['name_index'] = 'layer_name'` outside the block of `if self.add_tensor`.
If the intermediate tensor is the output of function api, we set the `mapping_layers['name_index'] = 'tensor_name'.` inside the block of `if self.add_tensor`.


```Python
def prepare_distill_adaptor():
    """
    Prepare the distill adaptors for student and teacher model.
    The adaptors set the intermediate feature tensors that used for distillation.
    """

    class StudentAdaptor(AdaptorBase):
        def mapping_layers(self):
            mapping_layers = {}
            # the interior tensor is the output of layer api
            # mapping_layers['hidden_0'] = 'layer_name'
            if self.add_tensor:
                # the interior tensor is the output of function api
                # mapping_layers["hidden_0"] = self.model.logit_list
                pass
            return mapping_layers

    class TeatherAdaptor(AdaptorBase):
        def mapping_layers(self):
            mapping_layers = {}
            # mapping_layers['hidden_0'] = 'layer_name'
            if self.add_tensor:
                # mapping_layers["hidden_0"] = self.model.logit_list
                pass
            return mapping_layers

    return StudentAdaptor, TeatherAdaptor
```

For example, The output tensors of the "nn.Conv2D" (layer api) and the "paddle.reshape" (function api) are unsed for distillation in the next model.
Then, the corresponding StudentAdaptor is showed as follows.

```python
=======
### 3.2 调整loss的系数

在学生模型的配置文件中，大家可以调整常规loss和distill_loss的coef系数，提高学生模型的精度。


### 3.3 使用内部Tensor计算蒸馏loss

上述示例为了简单起见，我们只使用了学生模型和教师模型的输出Tensor计算蒸馏loss。此外，我们也支持使用模型内部Tensor进行蒸馏。

1）选定学生和教师模型的内部Tensor

目前，PaddleSeg支持选定学生和教师模型中相同维度的内部Tensor进行蒸馏。所以，要求大家熟悉模型内部结构和内部Tensor的维度。

2）设置模型内部Tensor

在`slim/distill/distill_config.py`文件的prepare_distill_adaptor函数中，可以通过StudentAdaptor类和TeatherAdaptor类分别设置学生和教师模型的内部Tensor，用于后面的蒸馏。我们以设置StudentAdaptor类为例进行说明，TeatherAdaptor类设置方法相同。

有必要提前说明，Paddle的API有两类：第一类是Layer API（继承paddle.nn.Layer，比如paddle.nn.Conv2D）；第二类是Function API（不继承paddle.nn.Layer，比如paddle.reshape）。分辨特定API类别的方法是，首先在Paddle官网搜该API，然后点击源码查看内部实现是类还是函数，分别是Layer API和Function API。

StudentAdaptor类继承AdaptorBase类，我们修改mapping_layers字典来设置内部Tensor。

如果选定的内部Tensor是Layer API的输出，设置方法是`mapping_layers['name_index'] = 'layer_name'`。

如果选定的内部Tensor是Layer API的输出，设置方法是在`if self.add_tensor`内部修改`mapping_layers['name_index'] = 'tensor_name'.`。

举例，定义如下模型。

```
>>>>>>> 9c8570af (add new models)
class Model(nn.Layer):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2D(3, 3, 3, padding=1)
<<<<<<< HEAD
=======
        self.conv2 = nn.Conv2D(3, 3, 3, padding=1)
        self.conv3 = nn.Conv2D(3, 3, 3, padding=1)
>>>>>>> 9c8570af (add new models)
        self.fc = nn.Linear(3072, 10)

    def forward(self, x):
        conv1_out = self.conv1(x)
<<<<<<< HEAD
        self.reshape_out = paddle.reshape(conv1_out, shape=[x.shape[0], -1])  # note that `self.reshape_out`
=======
        conv2_out = self.conv2(self.conv1_out)
        conv3_out = self.conv3(conv2_out)
        self.reshape_out = paddle.reshape(self.conv3_out, shape=[x.shape[0], -1])
>>>>>>> 9c8570af (add new models)
        out = self.fc(self.reshape_out)
        return out
```

<<<<<<< HEAD
```python
class StudentAdaptor(AdaptorBase):
    def mapping_layers(self):
        mapping_layers = {}
        mapping_layers['hidden_0'] = 'conv1'   # The output of layer api
        if self.add_tensor:
            mapping_layers["hidden_1"] = self.model.reshape_out # The output of function api
        return mapping_layers
```

* Set the config of Distillation

Follow the above example, we define the "prepare_distill_config" function in `slim/distill/distill_config.py` to set the config of distillation.
In detail, the feature_type and s_feature_idx determine the tensor name in student model. The feature_type and t_feature_idx determine the tensor name in teacher model. The loss_function determine the type of distillation loss.

```python
=======
选定第二个卷积的输出Tensor和reshape后的Tensor作为蒸馏的内部Tensor，则StudentAdaptor配置如下。
对于第二个卷积的输出Tensor，是Layer API的输出，直接定义`mapping_layers['hidden_0'] = 'conv2'`（conv2是Layer名字）。
reshape后的Tensor，是Function API的输出，首先需要在模型定义中将该Tensor定义为类变量，然后在`if self.add_tensor`中定义`mapping_layers["hidden_1"] = self.model.reshape_out`（self.model.reshape_out是tensor在模型中的名字）。


```
class StudentAdaptor(AdaptorBase):
    def mapping_layers(self):
        mapping_layers = {}
        mapping_layers['hidden_0'] = 'conv2'   # The output of Layer API
        if self.add_tensor:
            mapping_layers["hidden_1"] = self.model.reshape_out # The output of Function API
        return mapping_layers
```

3）配置蒸馏参数

第二步设置学生和教师模型的内部Tensor后，接下来配置蒸馏的参数。

在`slim/distill/distill_config.py`文件的prepare_distill_config函数中，我们修改distill_config来配置蒸馏的参数。

复用第二步的示例，我们可以定义如下的蒸馏参数。
* config_1中feature_type表示使用内部tensor的类别
* s_feature_idx和t_feature_idx分别表示使用学生和教师模型的index
* loss_function表示两个内部Tensor蒸馏计算的Loss方式，目前只支持设置为SegChannelwiseLoss
* weight表示多个Loss加权求和时，该Loss的加权系数
* 可以定义多组内部Tensor进行蒸馏

```
>>>>>>> 9c8570af (add new models)
def prepare_distill_config():
    """
    Prepare the distill config.
    """
    config_1 = {
        'feature_type': 'hidden',
        's_feature_idx': 0,
        't_feature_idx': 0,
        'loss_function': 'SegChannelwiseLoss',
        'weight': 1.0
    }
    config_2 = {
        'feature_type': 'hidden',
        's_feature_idx': 1,
        't_feature_idx': 1,
        'loss_function': 'SegChannelwiseLoss',
        'weight': 1.0
    }
    distill_config = [config_1, config_2]

    return distill_config
```

<<<<<<< HEAD
* Training for Distillation

Use the same method as above to run the `slim/distill/distill_train.py`.
=======
4）蒸馏训练

在`slim/distill/distill_config.py`文件中设置模型内部Tensor和配置蒸馏参数后，可以进行蒸馏训练。

内部Tensor和输出Tensor可以同时用于模型蒸馏，只需要同时在配置文件中设置相应参数。
>>>>>>> 9c8570af (add new models)
