[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_x64_mode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_x64_mode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_x64_mode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fconfig%2Fset_x64_mode&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_x64_mode#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_x64_mode#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.config.set\_x64\_mode Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_x64_mode#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_x64_mode#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/backend/config.py#L112-L150)

Sets how Keras handles 64-bit dtypes.

tf.keras.config.set_x64_mode(
        mode
    )

64-bit dtypes are `int64`, `uint64`, `float64` and `complex128`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mode` | One of:<br><br>*   `"off"` (default): the result dtype of every op is capped to 32-bit, e.g. adding two `int64` tensors gives an `int32` tensor.<br>*   `"explicit_x64"`: a 64-bit input gives a 64-bit output. Inputs that are all 32-bit, Python scalars and default dtypes stay 32-bit. This mirrors JAX's `jax_explicit_x64_dtypes="allow"`, which Keras turns on for you on the JAX backend.<br>*   `"enable_x64"`: not supported yet. |

The mode can also be set with the `KERAS_X64_MODE` environment variable or the `"x64_mode"` field of `~/.keras/keras.json`. Set it before creating tensors or models. Supported on the `jax`, `numpy` and `torch` backends. On the JAX backend, Keras turns on the matching JAX flag. If JAX's own 64-bit flags are already on and don't match `mode`, Keras warns and keeps `mode`.

#### Example:

    keras.config.set_x64_mode("explicit_x64")

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `mode` is unknown, not supported yet, or not supported on the current backend. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.