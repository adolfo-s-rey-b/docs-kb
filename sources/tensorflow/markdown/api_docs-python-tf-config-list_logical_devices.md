[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.list\_logical\_devices Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L473-L509)

Return a list of logical devices created by runtime.

#### View aliases

**Main aliases**

[`tf.config.experimental.list_logical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.list_logical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices)
, [`tf.compat.v1.config.list_logical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices)

tf.config.list_logical_devices(
        device_type=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use a GPU](https://www.tensorflow.org/guide/gpu)<br>    <br>*   [NumPy API on TensorFlow](https://www.tensorflow.org/guide/tf_numpy)<br>    <br>*   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding)<br>    <br>*   [Migrate from TPUEstimator to TPUStrategy](https://www.tensorflow.org/guide/migrate/tpu_estimator)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution) | *   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input)<br>    <br>*   [Image classification with Model Garden](https://www.tensorflow.org/tfmodels/vision/image_classification)<br>    <br>*   [TFF simulations with accelerators](https://www.tensorflow.org/federated/tutorials/simulations_with_accelerators) |

Logical devices may correspond to physical devices or remote devices in the cluster. Operations and tensors may be placed on these devices by using the `name` of the [`tf.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
.

Calling [`tf.config.list_logical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices)
 triggers the runtime to configure any [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
 visible to the runtime, thereby preventing further configuration. To avoid runtime initialization, call [`tf.config.list_physical_devices`](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)
 instead.

#### For example:

    logical_devices = tf.config.list_logical_devices('GPU')

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_type` | (optional string) Only include devices matching this device type. For example "CPU" or "GPU". |
| `Notes` | 1.  If provided with any numerical values or any string other than supported device type such as 'CPU' it returns an empty list instead of raising error. 2. For default value it returns all logical devices |

|     |
| --- |
| Returns<br>------- |     |
| List of initialized `LogicalDevice`s |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.