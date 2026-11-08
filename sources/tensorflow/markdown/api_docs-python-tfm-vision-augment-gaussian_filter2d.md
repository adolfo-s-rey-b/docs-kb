[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.gaussian\_filter2d Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/gaussian_filter2d#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L192-L278)

Performs Gaussian blur on image(s).

tfm.vision.augment.gaussian_filter2d(
        image: tf.Tensor,
        filter_shape: Union[List[int], Tuple[int, ...], int],
        sigma: Union[List[float], Tuple[float, float], float] = 1.0,
        padding: str = 'REFLECT',
        constant_values: Union[int, tf.Tensor] = 0,
        name: Optional[str] = None
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | Either a 2-D `Tensor` of shape `[height, width]`, a 3-D `Tensor` of shape `[height, width, channels]`, or a 4-D `Tensor` of shape `[batch_size, height, width, channels]`. |
| `filter_shape` | An `integer` or `tuple`/`list` of 2 integers, specifying the height and width of the 2-D gaussian filter. Can be a single integer to specify the same value for all spatial dimensions. |
| `sigma` | A `float` or `tuple`/`list` of 2 floats, specifying the standard deviation in x and y direction the 2-D gaussian filter. Can be a single float to specify the same value for all spatial dimensions. |
| `padding` | A `string`, one of "REFLECT", "CONSTANT", or "SYMMETRIC". The type of padding algorithm to use, which is compatible with `mode` argument in [`tf.pad`](https://www.tensorflow.org/api_docs/python/tf/pad)<br>. For more details, please refer to https://www.tensorflow.org/api\_docs/python/tf/pad. |
| `constant_values` | A `scalar`, the pad value to use in "CONSTANT" padding mode. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| 2-D, 3-D or 4-D `Tensor` of the same dtype as input. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `image` is not 2, 3 or 4-dimensional, if `padding` is other than "REFLECT", "CONSTANT" or "SYMMETRIC", if `filter_shape` is invalid, or if `sigma` is invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.