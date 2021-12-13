<<<<<<< HEAD
English | [简体中文](README_cn.md)

# Web deployment

## 1 Introduction
Taking the deployment of portrait segmentation on MacOS Chrome as an example, this paper introduces how to use the front-end inference engine [Paddle.js](https://github.com/PaddlePaddle/Paddle.js) to deploy the segmentation model. The second part of the document describes how to use the portrait segmentation model js library [@paddlejs-models/humanseg](https://github.com/PaddlePaddle/Paddle.js/tree/master/packages/paddlejs-models/humanseg), the third Section introduces key APIs.

## 2. Use

### 2.1 Requirements
* Install Node (https://nodejs.org/zh-cn/download/)
* Confirm whether the installation is successful, execute it on the command line
````sh
# Display the installed node version number, which means successful installation
node -v
````
### 2.2 Steps
````sh
# clone Paddle.js
git clone https://github.com/PaddlePaddle/PaddleSeg.git

# Enter the deploy web example directory and install dependencies
cd PaddleSeg/deploy/web/example/ && npm install

# Execute
npm run dev

# Visit http://0.0.0.0:8866/ to experience the application of portrait segmentation and processing
````


### 2.3 Effect display

![image](https://user-images.githubusercontent.com/10822846/118273079-127bf480-b4f6-11eb-84c0-8a0bbc7c7433.png)

## 3. Key API Introduction

## 3.1 Introduction @paddlejs-models/humanseg
The npm library [@paddlejs-models/humanseg](https://github.com/PaddlePaddle/Paddle.js/tree/master/packages/paddlejs-models/humanseg) encapsulates the front-end inference engine [Paddle.js](https://github.com/PaddlePaddle/Paddle.js) and calculation scheme [paddlejs-backend-webgl](https://github.com/PaddlePaddle/Paddle.js/tree/master/packages/paddlejs-backend-webgl), The computing scheme is GPU-accelerated through WebGL.
So just import the library @paddlejs-models/humanseg, no need to introduce additional inference engine and calculation scheme.

## 3.1.1 API Introduction
@paddlejs-models/humanseg exposes four APIs:
* load
Call the load API to complete the initialization of the inference engine. Download the humanseg_lite_inference web model, generate the neural network according to the model structure and parameter file, and complete the model warm-up.

* getGrayValue
Pass the image to be processed to the getGrayValue API, and get the inference result after execution.

* drawHumanSeg
Draw portraits. Pass the canvas element and the inference result to the drawHumanSeg API, you can pass the background information through this element, and the segmented portrait will be drawn on this canvas.

* drawMask
Draw a portrait mask. Pass in the canvas element and inference result, and pass in the parameter dark to configure whether to use dark mode. The effect will be drawn on the incoming canvas element.

## 3.2 How to use @paddlejs-models/humanseg

```js
// import
=======
# Web 端部署

## 1.介绍

飞桨针对不同场景，提供了多个预测引擎部署模型（如下图），更多详细信息请参考[文档](https://paddleinference.paddlepaddle.org.cn/product_introduction/summary.html)。

![inference_ecosystem](https://user-images.githubusercontent.com/52520497/130720374-26947102-93ec-41e2-8207-38081dcc27aa.png)

本文以人像分割在 MacOS Chrome 的部署为例，介绍如何使用前端推理引擎 [Paddle.js](https://github.com/PaddlePaddle/Paddle.js) 对分割模型进行部署。文档第二部分介绍如何使用人像分割模型 js 库 [@paddlejs-models/humanseg](https://github.com/PaddlePaddle/Paddle.js/tree/master/packages/paddlejs-models/humanseg)，第三部分介绍重点 API。

## 2. 使用

### 2.1 要求
* 安装 Node （https://nodejs.org/zh-cn/download/）
* 确认是否安装成功，在命令行执行
```sh
# 显示所安 node 版本号，即表示成功安装
node -v
```
### 2.2 步骤
```sh
# clone Paddle.js
git clone https://github.com/PaddlePaddle/PaddleSeg.git

# 进入 deploy web example 目录，安装依赖
cd PaddleSeg/deploy/web/example/ && npm install

# 执行命令
npm run dev

# 访问 http://0.0.0.0:8866/ ，即可体验人像分割处理图片应用
```

### 2.3 效果展示

![image](./image/figure1.png)

## 3. 重点 API 介绍

## 3.1 @paddlejs-models/humanseg 介绍
npm 库 [@paddlejs-models/humanseg](https://github.com/PaddlePaddle/Paddle.js/tree/master/packages/paddlejs-models/humanseg) 封装了前端推理引擎 [Paddle.js](https://github.com/PaddlePaddle/Paddle.js) 和计算方案 [paddlejs-backend-webgl](https://github.com/PaddlePaddle/Paddle.js/tree/master/packages/paddlejs-backend-webgl)，该计算方案通过 WebGL 获得 GPU 加速。
所以只需引入库 @paddlejs-models/humanseg 即可，无需再额外引入推理引擎和计算方案。

## 3.1.1 API 介绍

@paddlejs-models/humanseg 暴露了四个 API：
* load
调用 load API 完成推理引擎初始化。下载humanseg_lite_inference web 模型，根据模型结构和参数文件生成神经网络，并完成模型预热。

* getGrayValue
给 getGrayValue API 传入需要处理的图片，执行后获得推理结果。

* drawHumanSeg
绘制人像。给 drawHumanSeg API 传入 canvas 画布元素和推理结果，可以通过该元素传递背景信息，分割后的人像将绘制在此 canvas上。

* drawMask
绘制人像遮罩。传入 canvas 画布元素和推理结果，同时传入参数 dark 配置是否使用暗黑模式。效果将绘制在传入的 canvas 画布元素上。

## 3.2 如何使用 @paddlejs-models/humanseg

```js
// 引入
>>>>>>> 9c8570af (add new models)
import * as humanseg from '@paddlejs-models/humanseg';

// load humanseg model
await humanseg.load();

// get the seg value [192 * 192];
const { data } = await humanseg.getGrayValue(img);

// draw human segmentation
const canvas1 = document.getElementById('demo1') as HTMLCanvasElement;
humanseg.drawHumanSeg(canvas1, data);

// draw the background mask
const canvas2 = document.getElementById('demo2') as HTMLCanvasElement;
humanseg.drawMask(canvas2, data, true);

```
