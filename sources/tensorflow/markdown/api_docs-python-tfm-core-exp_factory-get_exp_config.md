[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/exp_factory/get_exp_config#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/exp_factory/get_exp_config)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/exp_factory/get_exp_config?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.exp\_factory.get\_exp\_config Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/exp_factory.py#L29-L32)

Looks up the `ExperimentConfig` according to the `exp_name`.

tfm.core.exp_factory.get_exp_config(
        exp_name: str
    ) -> tfm.core.base_trainer.ExperimentConfig

Allowed values for `exp_name`:

| `exp_name` | Description |
| --- | --- |
| [`cascadercnn_spinenet_coco`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/cascadercnn_spinenet_coco) | COCO object detection with Cascade RCNN-RS with SpineNet backbone. |
| [`deit_imagenet_pretrain`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_deit_pretrain) | Image classification on imagenet with vision transformer. |
| [`fasterrcnn_resnetfpn_coco`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/fasterrcnn_resnetfpn_coco) | COCO object detection with Faster R-CNN. |
| [`image_classification`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification) | Image classification general. |
| [`maskrcnn_mobilenet_coco`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/maskrcnn_mobilenet_coco) | COCO object detection with Mask R-CNN with MobileNet backbone. |
| [`maskrcnn_resnetfpn_coco`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/maskrcnn_resnetfpn_coco) | COCO object detection with Mask R-CNN. |
| [`maskrcnn_spinenet_coco`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/maskrcnn/maskrcnn_spinenet_coco) | COCO object detection with Mask R-CNN with SpineNet backbone. |
| [`mnv2_deeplabv3_cityscapes`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/mnv2_deeplabv3_cityscapes) | Image segmentation on cityscapes with mobilenetv2 deeplabv3. |
| [`mnv2_deeplabv3_pascal`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/mnv2_deeplabv3_pascal) | Image segmentation on pascal with mobilenetv2 deeplabv3. |
| [`mnv2_deeplabv3plus_cityscapes`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/mnv2_deeplabv3plus_cityscapes) | Image segmentation on cityscapes with mobilenetv2 deeplabv3plus. |
| [`mobilenet_imagenet`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_mobilenet) | Image classification on imagenet with mobilenet. |
| [`resnet_imagenet`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet) | Image classification on imagenet with resnet. |
| [`resnet_rs_imagenet`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_resnetrs) | Image classification on imagenet with resnet-rs. |
| [`retinanet`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/retinanet) | RetinaNet general config. |
| [`retinanet_mobile_coco`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/retinanet_spinenet_mobile_coco) | COCO object detection with mobile RetinaNet. |
| [`retinanet_resnetfpn_coco`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/retinanet_resnetfpn_coco) | COCO object detection with RetinaNet. |
| [`retinanet_spinenet_coco`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/retinanet/retinanet_spinenet_coco) | COCO object detection with RetinaNet using SpineNet backbone. |
| [`revnet_imagenet`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_revnet) | Returns a revnet config for image classification on imagenet. |
| [`seg_deeplabv3_pascal`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/seg_deeplabv3_pascal) | Image segmentation on pascal voc with resnet deeplabv3. |
| [`seg_deeplabv3plus_cityscapes`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/seg_deeplabv3plus_cityscapes) | Image segmentation on cityscapes with resnet deeplabv3+. |
| [`seg_deeplabv3plus_pascal`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/seg_deeplabv3plus_pascal) | Image segmentation on pascal voc with resnet deeplabv3+. |
| [`seg_resnetfpn_pascal`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/seg_resnetfpn_pascal) | Image segmentation on pascal voc with resnet-fpn. |
| [`semantic_segmentation`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/semantic_segmentation/semantic_segmentation) | Semantic segmentation general. |
| [`video_classification`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification) | Video classification general. |
| [`video_classification_kinetics400`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_kinetics400) | Video classification on Kinetics 400 with resnet. |
| [`video_classification_kinetics600`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_kinetics600) | Video classification on Kinetics 600 with resnet. |
| [`video_classification_kinetics700`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_kinetics700) | Video classification on Kinetics 700 with resnet. |
| [`video_classification_kinetics700_2020`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_kinetics700_2020) | Video classification on Kinetics 700 2020 with resnet. |
| [`video_classification_ucf101`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/video_classification/video_classification_ucf101) | Video classification on UCF-101 with resnet. |
| [`vit_imagenet_finetune`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_vit_finetune) | Image classification on imagenet with vision transformer. |
| [`vit_imagenet_pretrain`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs/image_classification/image_classification_imagenet_vit_pretrain) | Image classification on imagenet with vision transformer. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.