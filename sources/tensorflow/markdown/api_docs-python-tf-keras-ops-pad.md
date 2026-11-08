[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#note)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#note_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.pad Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#args)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#note)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#note_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L6787-L6820)

Pad a tensor.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.pad`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/pad)

tf.keras.ops.pad(
        x, pad_width, mode='constant', constant_values=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Tensor to pad. |
| `pad_width` | Number of values padded to the edges of each axis. `((before_1, after_1), ...(before_N, after_N))` unique pad widths for each axis. `((before, after),)` yields same before and after pad for each axis. `(pad,)` or `int` is a shortcut for `before = after = pad` width for all axes. |
| `mode` | One of `"constant"`, `"edge"`, `"linear_ramp"`, `"maximum"`, `"mean"`, `"median"`, `"minimum"`, `"reflect"`, `"symmetric"`, `"wrap"`, `"empty"`, `"circular"`. Defaults to `"constant"`. |
| `constant_values` | value to pad with if `mode == "constant"`. Defaults to `0`. A `ValueError` is raised if not None and `mode != "constant"`. |

|     |
| --- |
| Note<br>---- |     |
| Torch backend only supports modes `"constant"`, `"reflect"`, `"symmetric"` and `"circular"`. Only Torch backend supports `"circular"` mode. |     |

|     |
| --- |
| Note<br>---- |     |
| Tensorflow backend only supports modes `"constant"`, `"reflect"` and `"symmetric"`. |     |

|     |
| --- |
| Returns<br>------- |     |
| Padded tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.