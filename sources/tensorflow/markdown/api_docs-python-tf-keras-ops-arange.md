[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arange#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arange)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arange?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Farange&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arange#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arange#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.arange Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arange#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arange#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/numpy.py#L720-L769)

Return evenly spaced values within a given interval.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.arange`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/arange)

tf.keras.ops.arange(
        start, stop=None, step=None, dtype=None
    )

`arange` can be called with a varying number of positional arguments:

*   `arange(stop)`: Values are generated within the half-open interval `[0, stop)` (in other words, the interval including start but excluding stop).\
*   `arange(start, stop)`: Values are generated within the half-open interval `[start, stop)`.\
*   `arange(start, stop, step)`: Values are generated within the half-open interval `[start, stop)`, with spacing between values given by step.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `start` | Integer or real, representing the start of the interval. The interval includes this value. |\
| `stop` | Integer or real, representing the end of the interval. The interval does not include this value, except in some cases where `step` is not an integer and floating point round-off affects the length of `out`. Defaults to `None`. |\
| `step` | Integer or real, represent the spacing between values. For any output `out`, this is the distance between two adjacent values, `out[i+1] - out[i]`. The default step size is 1. If `step` is specified as a position argument, `start` must also be given. |\
| `dtype` | The type of the output array. If `dtype` is not given, infer the data type from the other input arguments. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| Tensor of evenly spaced values. For floating point arguments, the length of the result is `ceil((stop - start)/step)`. Because of floating point overflow, this rule may result in the last element of out being greater than stop. |     |\
\
#### Examples:\
\
    keras.ops.arange(3)\
\
    keras.ops.arange(3.0)\
\
    keras.ops.arange(3, 7)\
\
    keras.ops.arange(3, 7, 2)\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.