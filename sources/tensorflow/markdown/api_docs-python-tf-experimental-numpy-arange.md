[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/arange#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/arange)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/arange?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fnumpy%2Farange&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/arange#used-in-the-notebooks)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.numpy.arange Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/arange#used-in-the-notebooks)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/numpy_ops/np_array_ops.py#L259-L301)

TensorFlow variant of NumPy's `arange`.

tf.experimental.numpy.arange(
        start, stop=None, step=1, dtype=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [NumPy API on TensorFlow](https://www.tensorflow.org/guide/tf_numpy) |

Unsupported arguments: `start_or_stop`, `device`, `like`.

Returns `step`\-separated values in the range \[start, stop).\
\
Args: start: Start of the interval. Included in the range. stop: End of the interval. If not specified, `start` is treated as 0 and `start` value is used as `stop`. If specified, it is not included in the range if `step` is integer. When `step` is floating point, it may or may not be included. step: The difference between 2 consecutive values in the output range. It is recommended to use `linspace` instead of using non-integer values for `step`. dtype: Optional. Type of the resulting ndarray. Could be a python type, a NumPy type or a TensorFlow `DType`. If not provided, the largest type of `start`, `stop`, `step` is used.\
\
Raises: ValueError: If step is zero.\
\
See the NumPy documentation for [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)\
.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.