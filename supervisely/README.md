<div align="center" markdown>
<img src="https://i.imgur.com/1bJgrIn.png"/>

# Efficient Interactive Segmentation

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Use">How To Use</a> •
  <a href="#Results">Results</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/PaddleSeg)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/PaddleSeg)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/PaddleSeg&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/PaddleSeg&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/PaddleSeg&counter=runs&label=runs&123)](https://supervise.ly)

</div>

## Overview

SAMPLE TEXT

<p float="left">
  <img src="https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/overview_1.gif?raw=true" style="width:49%;"/>
  <img src="https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/overview_2.gif?raw=true" style="width:49%;"/>
</p>


**state-of-the art click-based interactive segmentation integrated into Supervisely Image Annotator**


## Overview

Application key points:  
- Manually selected ROI
- Capability to correct prediction errors on the fly
- Select from [4 pretrained models](../README.md#evaluation)
- Models are class agnostic you can segment any object from any industry
- Ability to share application session with team members as an Admin (Enterprise edition only)

RITM Interactive segmentation algorithms allow users to explicitly control the predictions using interactive input at several iterations, in contrast to common semantic and instance segmentation algorithms that can only input an image and output a segmentation mask in one pass. Such interaction makes it possible to select an object of interest and correct prediction errors.

<img src="https://i.imgur.com/8RaxwK2.png" style="width:100%;"/>

Besides segmenting new objects, proposed method allows to correct external masks, e.g. produced by other
instance or semantic segmentation models. A user can fix false negative and false positive regions with positive (green)
and negative (red) clicks, respectively.

# How to run

1. Add [RITM interactive segmentation smart tool](https://ecosystem.supervise.ly/apps/ritm-interactive-segmentation) to your team from Ecosystem.

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/ritm-interactive-segmentation" src="https://i.imgur.com/mQJpKgA.png" width="600px" style='padding-bottom: 20px'/>  

2. Run app from **Plugins & Apps** page:

<img src="https://i.imgur.com/nTZTuVh.png" width="100%"/>

3. Select options in modal window and press the `Run` button.
 
<div align="center" markdown>
<img src="https://i.imgur.com/ZF6OZIg.png" width="500"/>
</div>

# How to use

`Place for video guide`

## Controls:

| Key                                                           | Description                               |
| ------------------------------------------------------------- | ------------------------------------------|
| <kbd>Left Mouse Button</kbd>                                  | Place a positive click                    |
| <kbd>Right Mouse Button</kbd>                                 | Place a negative click                    |
| <kbd>Scroll Wheel</kbd>                                       | Zoom an image in and out                  |
| <kbd>Right Mouse Button</kbd> + <br> <kbd>Move Mouse</kbd>    | Move an image                             |
| <kbd>Space</kbd>                                              | Finish the current object mask            |
| <kbd>Shift + H</kbd>                                          | Higlight instances with random colors     |
| <kbd>Ctrl + H</kbd>                                           | Hide all labels                           |


# Demo

We have prepared a videos and demonstrated how EISEG works for the different domains:


<table>
  <tr style="width: 100%">
    <td>
       <a data-key="sly-embeded-video-link" href="https://youtu.be/5t8cQOvaknE" data-video-code="5t8cQOvaknE">     <img src="https://i.imgur.com/8b3pU1Y.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
    </td>
    <td>
      <a data-key="sly-embeded-video-link" href="https://youtu.be/ImlaIwX9-nE" data-video-code="ImlaIwX9-nE"> <img src="https://i.imgur.com/97iXSJb.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
    </td>
      </tr>
    <tr style="width: 100%">
      <td>
        <a data-key="sly-embeded-video-link" href="https://youtu.be/c1sCQKTt4bg" data-video-code="c1sCQKTt4bg">     <img src="https://i.imgur.com/Vz4kZqh.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
      </td>
      <td>
        <a data-key="sly-embeded-video-link" href="https://youtu.be/cBp6-VPdKQA" data-video-code="cBp6-VPdKQA"> <img src="https://i.imgur.com/pSQWzUV.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
      </td> 
    </tr>
    <tr style="width: 100%">  
      <td>
        <a data-key="sly-embeded-video-link" href="https://youtu.be/uYhrJz44g0M" data-video-code="uYhrJz44g0M">     <img src="https://i.imgur.com/lapuFFU.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
      </td>
      <td>
        <a data-key="sly-embeded-video-link" href="https://youtu.be/zj5ojW3079Y" data-video-code="zj5ojW3079Y"> <img src="https://i.imgur.com/4fL2X7R.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
      </td>
    </tr>
    <tr style="width: 100%">
      <td>
      <a data-key="sly-embeded-video-link" href="https://youtu.be/6wiKb-TX934" data-video-code="6wiKb-TX934">     <img src="https://i.imgur.com/OteFM2A.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
      </td>
      <td>
        <a data-key="sly-embeded-video-link" href="https://youtu.be/n5qbdvO3fIw" data-video-code="n5qbdvO3fIw">   <img src="https://i.imgur.com/ymFptmd.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
      </td> 
    </tr>
  </table>
  
  
# Manual object correction

<a data-key="sly-embeded-video-link" href="https://youtu.be/6pMUHn0jNGE" data-video-code="6pMUHn0jNGE">
    <img src="https://i.imgur.com/skXXok8.png" alt="SLY_EMBEDED_VIDEO_LINK"  width="700px">
</a>

# Acknowledgment

This app is based on the great work `Reviving Iterative Training with Mask Guidance for Interactive Segmentation` ([paper](https://arxiv.org/abs/2102.06583),  [github](https://github.com/saic-vul/ritm_interactive_segmentation)). ![GitHub Org's stars](https://img.shields.io/github/stars/saic-vul/ritm_interactive_segmentation?style=social)
