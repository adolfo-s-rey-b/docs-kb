[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DeviceMesh#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DeviceMesh)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DeviceMesh?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DeviceMesh#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DeviceMesh#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distribution.DeviceMesh Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DeviceMesh#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DeviceMesh#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L154-L233)

A cluster of computation devices for distributed computation.

tf.keras.distribution.DeviceMesh(
        shape, axis_names, devices=None
    )

This API is aligned with `jax.sharding.Mesh`, which represents the computation devices in the global context.

See more details in [jax.sharding.Mesh](https://jax.readthedocs.io/en/latest/jax.sharding.html#jax.sharding.Mesh)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | tuple of list of integers. The shape of the overall `DeviceMesh`, e.g. `(8,)` for a data parallel only distribution, or `(4, 2)` for a model+data parallel distribution. |
| `axis_names` | List of string. The logical name of the each axis for the `DeviceMesh`. The length of the `axis_names` should match to the rank of the `shape`. The `axis_names` will be used to match/create the `TensorLayout` when distribute the data and variables. |
| `devices` | Optional list of devices. Defaults to all the available devices locally from [`keras.distribution.list_devices()`](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/list_devices)<br>. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `axis_names` |     |
| `backend_mesh` |     |
| `devices` |     |
| `shape` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.