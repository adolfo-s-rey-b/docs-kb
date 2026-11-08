[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fnumpy%2Fexperimental_enable_numpy_behavior&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.numpy.experimental\_enable\_numpy\_behavior Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/experimental_enable_numpy_behavior#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/numpy_ops/np_config.py#L25-L58)

Enable NumPy behavior on Tensors.

tf.experimental.numpy.experimental_enable_numpy_behavior(
        prefer_float32=False, dtype_conversion_mode='legacy'
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [TF-NumPy Type Promotion](https://www.tensorflow.org/guide/tf_numpy_type_promotion)<br>    <br>*   [NumPy API on TensorFlow](https://www.tensorflow.org/guide/tf_numpy) |

Enabling NumPy behavior has three effects:

*   It adds to [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     some common NumPy methods such as `T`, `reshape` and `ravel`.
*   It changes dtype promotion in [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     operators to be compatible with NumPy. For example, `tf.ones([], tf.int32) + tf.ones([], tf.float32)` used to throw a "dtype incompatible" error, but after this it will return a float64 tensor (obeying NumPy's promotion rules).
*   It enhances [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
    's indexing capability to be on par with [NumPy's](https://numpy.org/doc/stable/reference/arrays.indexing.html)
    .

|     |     |
| --- | --- |
| Args<br>---- |     |
| `prefer_float32` | Controls whether dtype inference will use float32 for Python floats, or float64 (the default and the NumPy-compatible behavior). |
| `dtype_conversion_mode` | a string that specifies promotion mode. This string corresponds to a PromoMode Enum and can be 'off', 'legacy', 'safe', or 'all'. 'safe' or 'all' mode enables the auto dtype conversion semantics. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.