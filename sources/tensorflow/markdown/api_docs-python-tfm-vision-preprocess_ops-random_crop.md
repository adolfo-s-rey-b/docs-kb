[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.random\_crop Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/random_crop#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L1184-L1230)

Randomly crop the image and boxes, filtering labels.

tfm.vision.preprocess_ops.random_crop(
        image,
        boxes,
        labels,
        min_scale=0.3,
        aspect_ratio_range=(0.5, 2.0),
        min_overlap_params=(0.0, 1.4, 0.2, 0.1),
        max_retry=50,
        seed=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | a 'Tensor' of shape \[height, width, 3\] representing the input image. |
| `boxes` | a 'Tensor' of shape \[N, 4\] representing the ground-truth bounding boxes with (ymin, xmin, ymax, xmax). |
| `labels` | a 'Tensor' of shape \[N,\] representing the class labels of the boxes. |
| `min_scale` | a 'float' in \[0.0, 1.0) indicating the lower bound of the random scale variable. |\
| `aspect_ratio_range` | a list of two 'float' that specifies the lower and upper bound of the random aspect ratio. |\
| `min_overlap_params` | a list of four 'float' representing the min value, max value, step size, and offset for the minimum overlap sample. |\
| `max_retry` | an 'int' representing the number of trials for cropping. If it is exhausted, no cropping will be performed. |\
| `seed` | the random number seed of int, but could be None. |\
\
|     |     |\
| --- | --- |\
| Returns<br>------- |     |\
| `image` | a Tensor representing the random cropped image. Can be the original image if max\_retry is exhausted. |\
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