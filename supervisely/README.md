<div align="center" markdown>
<img src="https://i.imgur.com/1bJgrIn.png"/>

# Efficient Interactive Segmentation
  
  <p align="center"><b>state-of-the art click-based interactive segmentation integrated into Supervisely Image Annotator</b></p>

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-to-run">How to run</a> •
  <a href="#How-to-use">How to use</a> •
  <a href="#Demo">Demo</a> •
  <a href="#Manual-object-correction">Manual object correction</a> •
  <a href="#Acknowledgment">Acknowledgment</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/PaddleSeg)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/PaddleSeg)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/PaddleSeg&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/PaddleSeg&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/PaddleSeg&counter=runs&label=runs&123)](https://supervise.ly)

</div>


# Overview

Application key points:  
- Manually selected ROI
- Capability to correct prediction errors on the fly
- Select from [4 pretrained models](../contrib/EISeg/README.md#模型准备)
- Models are class agnostic you can segment any object from any industry
- Ability to share application session with team members as an Admin (Enterprise edition only)

EISeg (Efficient Interactive Segmentation) is an efficient and intelligent interactive segmentation and annotation software developed based on flying paddles. Covers high-quality interactive segmentation models in different directions such as high-precision and lightweight, which is convenient for developers to quickly implement semantic and instance label labeling, and reduce labeling costs. In addition, by applying the annotations obtained by EISeg to other segmentation models provided by PaddleSeg for training, a high-precision model of a customized scene can be obtained, and the entire process of segmentation tasks from data annotation to model training and prediction can be opened up.

<p float="left">
  <img src="https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/overview_1.gif?raw=true" style="width:49%;"/>
  <img src="https://github.com/supervisely-ecosystem/PaddleSeg/releases/download/v2.2.1/overview_2.gif?raw=true" style="width:49%;"/>
</p>

# How to run

### ⚠️ Notice  
 * The application may already be launched by the instance administrator (**Enterprise**) or the Supervisely team (**Community**). If the app is not available in dropdown menu in Labeling tool, please contact us. If the Smart Tool responds slowly, please run additional application sessions in your team.
 * **Enterprise only**: You can share started application with all users on your instance using **share** button in front of running session. We recommend to run multiple sessions if large number of users are using Smart Tool simultaneously.

---

1. Add [EISeg interactive segmentation SmartTool](https://ecosystem.supervise.ly/apps/PaddleSeg) to your team from Ecosystem.

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/PaddleSeg" src="https://i.imgur.com/xp7xFz6.png" width="600px" style='padding-bottom: 20px'/>  

2. Run app from **Plugins & Apps** page:

<img src="https://i.imgur.com/uWMA1x3.png" width="100%"/>

3. Select options in modal window and press the `Run` button.
 
<div align="center" markdown>
<img src="https://i.imgur.com/ZJZRg17.png" width="500"/>
</div>

# How to use

<a data-key="sly-embeded-video-link" href="https://youtu.be/atYG2NQ_WCQ" data-video-code="atYG2NQ_WCQ"> <img src="https://i.imgur.com/zDKk6pC.png" alt="SLY_EMBEDED_VIDEO_LINK"  width="70%"> </a>  


## Controls

| Key                                                           | Description                               |
| ------------------------------------------------------------- | ------------------------------------------|
| <kbd>Left Mouse Button</kbd>                                  | Place a positive click                    |
| <kbd>Right Mouse Button</kbd>                                 | Place a negative click                    |
| <kbd>Scroll Wheel</kbd>                                       | Zoom an image in and out                  |
| <kbd>Right Mouse Button</kbd> + <br> <kbd>Move Mouse</kbd>    | Move an image                             |
| <kbd>Space</kbd>                                              | Finish the current object mask            |
| <kbd>Shift + H</kbd>                                          | Higlight instances with random colors     |
| <kbd>Ctrl + H</kbd>                                           | Hide all labels                           |


<p align="left"> <img align="center" src="https://i.imgur.com/jxySekj.png" width="50"> <b>—</b> Auto add positivie point to rectangle button (<b>ON</b> by default for SmartTool apps) </p>

<div align="center" markdown>
<img src="https://i.imgur.com/dlaLrsi.png" width="90%"/>
</div>

<p align="left"> <img align="center" src="https://i.imgur.com/kiwbBkj.png" width="200"> <b>—</b> SmartTool selector button, switch between SmartTool apps and models</p>

<div align="center" markdown>
<img src="https://i.imgur.com/FATcNZU.png" width="90%"/>
</div>

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

This app is based on the great work by `PaddleSeg` Team ([paper](https://arxiv.org/pdf/2101.06175.pdf),  [github](https://github.com/PaddlePaddle/PaddleSeg)). ![GitHub Org's stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleSeg?style=social)
