[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_with_boxes_and_labels#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_with_boxes_and_labels)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_with_boxes_and_labels?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_with_boxes_and_labels#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_with_boxes_and_labels#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.random\_crop\_image\_with\_boxes\_and\_labels Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_with_boxes_and_labels#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop_image_with_boxes_and_labels#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L1021-L1181)

Crops a random slice from the input image.

tfm.vision.preprocess_ops.random_crop_image_with_boxes_and_labels(
        img,
        boxes,
        labels,
        min_scale,
        aspect_ratio_range,
        min_overlap_params,
        max_retry
    )

The function will correspondingly recompute the bounding boxes and filter out outside boxes and their labels.

#### References:

\[1\] End-to-End Object Detection with Transformers [https://arxiv.org/abs/2005.12872](https://arxiv.org/abs/2005.12872)

The preprocessing steps:

1.  Sample a minimum IoU overlap.
2.  For each trial, sample the new image width, height, and top-left corner.
3.  Compute the IoUs of bounding boxes with the cropped image and retry if the maximum IoU is below the sampled threshold.
4.  Find boxes whose centers are in the cropped image.
5.  Compute new bounding boxes in the cropped region and only select those boxes' labels.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `img` | a 'Tensor' of shape \[height, width, 3\] representing the input image. |
| `boxes` | a 'Tensor' of shape \[N, 4\] representing the ground-truth bounding boxes with (ymin, xmin, ymax, xmax). |
| `labels` | a 'Tensor' of shape \[N,\] representing the class labels of the boxes. |
| `min_scale` | a 'float' in \[0.0, 1.0) indicating the lower bound of the random scale variable. |\
| `aspect_ratio_range` | a list of two 'float' that specifies the lower and upper bound of the random aspect ratio. |\
| `min_overlap_params` | a list of four 'float' representing the min value, max value, step size, and offset for the minimum overlap sample. |\
| `max_retry` | an 'int' representing the number of trials for cropping. If it is exhausted, no cropping will be performed. |\
\
|     |     |\
| --- | --- |\
| Returns<br>------- |     |\
| `img` | a Tensor representing the random cropped image. Can be the original image if max\_retry is exhausted. |\
| `boxes` | a Tensor representing the bounding boxes in the cropped image. |\
| `labels` | a Tensor representing the new bounding boxes' labels. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.