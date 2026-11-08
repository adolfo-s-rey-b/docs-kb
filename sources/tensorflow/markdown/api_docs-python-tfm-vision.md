[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/vision#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.vision Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/vision#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/vision#classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/tensorflow_models/vision/__init__.py)

TensorFlow Models Vision Libraries.

Modules
-------

[`anchor`](https://www.tensorflow.org/api_docs/python/tfm/vision/anchor)
 module: Anchor box and labeler definition.

[`augment`](https://www.tensorflow.org/api_docs/python/tfm/vision/augment)
 module: Augmentation policies for enhanced image/video preprocessing.

[`backbones`](https://www.tensorflow.org/api_docs/python/tfm/vision/backbones)
 module: Backbones package definition.

[`box_matcher`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher)
 module: Box matcher implementation.

[`box_ops`](https://www.tensorflow.org/api_docs/python/tfm/vision/box_ops)
 module: Box related ops.

[`classification_model`](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model)
 module: Build classification models.

[`configs`](https://www.tensorflow.org/api_docs/python/tfm/vision/configs)
 module: Configs package definition.

[`decoders`](https://www.tensorflow.org/api_docs/python/tfm/vision/decoders)
 module: Decoders package definition.

[`factory`](https://www.tensorflow.org/api_docs/python/tfm/vision/factory)
 module: Factory methods to build models.

[`factory_3d`](https://www.tensorflow.org/api_docs/python/tfm/vision/factory_3d)
 module: Factory methods to build models.

[`heads`](https://www.tensorflow.org/api_docs/python/tfm/vision/heads)
 module: Heads package definition.

[`image_classification`](https://www.tensorflow.org/api_docs/python/tfm/vision/image_classification)
 module: Image classification task definition.

[`iou_similarity`](https://www.tensorflow.org/api_docs/python/tfm/vision/iou_similarity)
 module: Region Similarity Calculators.

[`layers`](https://www.tensorflow.org/api_docs/python/tfm/vision/layers)
 module: Layers package definition.

[`mask_ops`](https://www.tensorflow.org/api_docs/python/tfm/vision/mask_ops)
 module: Utility functions for segmentations.

[`maskrcnn`](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn)
 module: MaskRCNN task definition.

[`maskrcnn_model`](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model)
 module: R-CNN(-RS) models.

[`models`](https://www.tensorflow.org/api_docs/python/tfm/vision/models)
 module: Models under Vision package.

[`nms`](https://www.tensorflow.org/api_docs/python/tfm/vision/nms)
 module: Tensorflow implementation of non max suppression.

[`preprocess_ops`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops)
 module: Preprocessing ops.

[`preprocess_ops_3d`](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops_3d)
 module: Utils for processing video dataset features.

[`retinanet`](https://www.tensorflow.org/api_docs/python/tfm/vision/retinanet)
 module: RetinaNet task definition.

[`retinanet_model`](https://www.tensorflow.org/api_docs/python/tfm/vision/retinanet_model)
 module: RetinaNet.

[`sampling_ops`](https://www.tensorflow.org/api_docs/python/tfm/vision/sampling_ops)
 module: Class to subsample minibatches by balancing positives and negatives.

[`segmentation_model`](https://www.tensorflow.org/api_docs/python/tfm/vision/segmentation_model)
 module: Build segmentation models.

[`semantic_segmentation`](https://www.tensorflow.org/api_docs/python/tfm/vision/semantic_segmentation)
 module: Image segmentation task definition.

[`serving`](https://www.tensorflow.org/api_docs/python/tfm/vision/serving)
 module: Tools for exporting models.

[`spatial_transform_ops`](https://www.tensorflow.org/api_docs/python/tfm/vision/spatial_transform_ops)
 module: Spatial transform ops.

[`target_gather`](https://www.tensorflow.org/api_docs/python/tfm/vision/target_gather)
 module: Definition of target gather, which gathers targets from indices.

[`video_classification`](https://www.tensorflow.org/api_docs/python/tfm/vision/video_classification)
 module: Video classification task definition.

[`video_classification_model`](https://www.tensorflow.org/api_docs/python/tfm/vision/video_classification_model)
 module: Build video classification models.

Classes
-------

[`class ImageClassificationTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/ImageClassificationTask)
: A task for image classification.

[`class MaskRCNNTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask)
: A single-replica view of training procedure.

[`class RetinaNetTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/RetinaNetTask)
: A single-replica view of training procedure.

[`class SemanticSegmentationTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask)
: A task for semantic segmentation.

[`class VideoClassificationTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask)
: A task for video classification.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.