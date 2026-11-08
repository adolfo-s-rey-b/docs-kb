[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdistribution%2FTensorLayout&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distribution.TensorLayout Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/TensorLayout#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L236-L300)

A layout to apply to a tensor.

tf.keras.distribution.TensorLayout(
        axes, device_mesh=None
    )

This API is aligned with `jax.sharding.NamedSharding`.

See more details in [jax.sharding.NamedSharding](https://jax.readthedocs.io/en/latest/jax.sharding.html#jax.sharding.NamedSharding)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `axes` | tuple of strings that should map to the `axis_names` in a `DeviceMesh`. For any dimensions that doesn't need any sharding, A `None` can be used a placeholder. |
| `device_mesh` | Optional `DeviceMesh` that will be used to create the layout. The actual mapping of tensor to physical device is not known until the mesh is specified. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `axes` |     |
| `backend_layout` |     |
| `device_mesh` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.