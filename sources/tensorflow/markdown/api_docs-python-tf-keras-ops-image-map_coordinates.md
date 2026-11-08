[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/map_coordinates#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/map_coordinates)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/map_coordinates?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/map_coordinates#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/map_coordinates#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.map\_coordinates Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/map_coordinates#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/map_coordinates#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L963-L1015)

Map the input array to new coordinates by interpolation.

tf.keras.ops.image.map_coordinates(
        inputs, coordinates, order, fill_mode='constant', fill_value=0
    )

Note that interpolation near boundaries differs from the scipy function, because we fixed an outstanding bug [scipy/issues/2640](https://github.com/scipy/scipy/issues/2640)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | The input array. |
| `coordinates` | The coordinates at which inputs is evaluated. |
| `order` | The order of the spline interpolation. The order must be `0` or `1`. `0` indicates the nearest neighbor and `1` indicates the linear interpolation. |
| `fill_mode` | Points outside the boundaries of the inputs are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"mirror"` and `"reflect"`. Defaults to `"constant"`.<br><br>*   `"constant"`: `(k k k k \| a b c d \| k k k k)` The inputs is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.<br>*   `"nearest"`: `(a a a a \| a b c d \| d d d d)` The inputs is extended by the nearest pixel.<br>*   `"wrap"`: `(a b c d \| a b c d \| a b c d)` The inputs is extended by wrapping around to the opposite edge.<br>*   `"mirror"`: `(c d c b \| a b c d \| c b a b)` The inputs is extended by mirroring about the edge.<br>*   `"reflect"`: `(d c b a \| a b c d \| d c b a)` The inputs is extended by reflecting about the edge of the last pixel. |
| `fill_value` | Value used for points outside the boundaries of the inputs if `fill_mode="constant"`. Defaults to `0`. |

|     |
| --- |
| Returns<br>------- |     |
| Output input or batch of inputs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.