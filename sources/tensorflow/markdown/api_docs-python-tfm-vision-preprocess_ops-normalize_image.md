[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_image#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_image)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_image?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_image#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.normalize\_image Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_image#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/normalize_image#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/preprocess_ops.py#L78-L115)

Normalizes the image to zero mean and unit variance.

tfm.vision.preprocess_ops.normalize_image(
        image: tf.Tensor,
        offset: Sequence[float] = tfm.vision.preprocess_ops.MEAN_NORM,
        scale: Sequence[float] = tfm.vision.preprocess_ops.STDDEV_NORM
    ) -> tf.Tensor

This function normalizes the input image by subtracting the `offset` and dividing by the `scale`.

**Important Note about Input Types and Normalization:**

*   **Integer Images:** If the input `image` is an integer type (e.g., `uint8`), the provided `offset` and `scale` values should be already **normalized** to the range \[0, 1\]. This is because the function converts integer images to float32 with values in the range \[0, 1\] before the normalization happens.
    
*   **Float Images:** If the input `image` is a float type (e.g., `float32`), the `offset` and `scale` values should be in the **same range** as the image data.
    
    *   If the image has values in \[0, 1\], the `offset` and `scale` should also be in \[0, 1\].
    *   If the image has values in \[0, 255\], the `offset` and `scale` should also be in \[0, 255\].

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> in either: (1) float dtype with values in range \[0, 1) or \[0, 255\], or (2) int type with values in range \[0, 255\]. |\
| `offset` | A tuple of mean values to be subtracted from the image. |\
| `scale` | A tuple of normalization factors. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A normalized image tensor. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.