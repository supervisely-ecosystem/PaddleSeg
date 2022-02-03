### Fast-SCNN

<<<<<<< HEAD
Fast-SCNN is a real-time oriented semantic segmentation network. Based on the dual-branch structure, depthwise separable convolution and inverted-residual modules are extensively used, and feature fusion is used to construct a Pyramid Pooling Module to fuse context information. This enables Fast-SCNN to learn rich details while remaining efficient. The biggest feature of Fast-SCNN is "small and fast", that is, the model only needs small FLOPs during inference calculation, and can quickly infer a good result. The entire network structure is as follows:

![img](./images/Fast-SCNN.png)

<div align = "center">Fast-SCNN</div>

For details, please refer to[Fast-SCNN: Fast Semantic Segmentation Network](https://arxiv.org/abs/1902.04502).
=======
Fast-SCNN 是一个面向实时的语义分割网络。在双分支的结构基础上，大量使用了深度可分离卷积和逆残差（inverted-residual）模块，并且使用特征融合构造金字塔池化模块 (Pyramid Pooling Module)来融合上下文信息。这使得Fast-SCNN在保持高效的情况下能学习到丰富的细节信息。Fast-SCNN最大的特点是“小快灵”，即该模型在推理计算时仅需要较小的FLOPs，就可以快速推理出一个不错的结果。整个网络结构如下：

![img](./images/Fast-SCNN.png)

<div align = "center">Fast-SCNN结构图</div>

具体原理细节请参考[Fast-SCNN: Fast Semantic Segmentation Network](https://arxiv.org/abs/1902.04502)
>>>>>>> 9c8570af (add new models)
