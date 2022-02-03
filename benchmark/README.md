<<<<<<< HEAD
# PaddleSeg 下benchmark模型执行说明

=======
<<<<<<< HEAD
English | [简体中文](README_CN.md)

# Benchmark Introduction

The content is as follow:

```
=======
# PaddleSeg 下benchmark模型执行说明

>>>>>>> 9c8570af (add new models)
>>>>>>> PaddlePaddle-release/2.4
├── README.md  
├── configs  
│   ├── cityscapes_30imgs.yml  
│   ├── fastscnn.yml  
│   ├── ocrnet_hrnetw48.yml  
│   └── segformer_b0.yml  
├── deeplabv3p.yml  
├── hrnet.yml  
├── hrnet48.yml  
├── run_all.sh  
├── run_benchmark.sh  
├── run_fp16.sh  
└── run_fp32.sh  
<<<<<<< HEAD
## 环境
使用Docker配置Paddle的GPU环境。
=======
<<<<<<< HEAD
```

## Environment
Use Docker to configure the environment.
=======
## 环境
使用Docker配置Paddle的GPU环境。
>>>>>>> 9c8570af (add new models)
>>>>>>> PaddlePaddle-release/2.4
* docker image: paddlepaddle/paddle:latest-gpu-cuda10.1-cudnn7
* CUDA 10.1 + cudnn7
* paddle=2.1.2
* py=37
<<<<<<< HEAD
## 测试步骤
### 执行训练Benchmark测试
=======
<<<<<<< HEAD

## Test
### Training Test
=======
## 测试步骤
### 执行训练Benchmark测试
>>>>>>> 9c8570af (add new models)
>>>>>>> PaddlePaddle-release/2.4

```
git clone https://github.com/PaddlePaddle/PaddleSeg.git
cd PaddleSeg
bash benchmark/run_all.sh
```
<<<<<<< HEAD
=======
<<<<<<< HEAD
### How to Open Profiling
 Add the following parameter when training.
 `--profiler_options="batch_range=[50, 60]; profile_path=model.profile`
=======
>>>>>>> PaddlePaddle-release/2.4
### Profiling开关使用方式
```bash
 # 调用train.py时加上该参数 --profiler_options="batch_range=[50, 60]; profile_path=model.profile"
```




<<<<<<< HEAD
=======
>>>>>>> 9c8570af (add new models)
>>>>>>> PaddlePaddle-release/2.4
