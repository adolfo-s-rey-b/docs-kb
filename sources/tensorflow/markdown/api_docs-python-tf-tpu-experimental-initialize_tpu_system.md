[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2Finitialize_tpu_system&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.initialize\_tpu\_system Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py#L58-L73)

Initialize the TPU devices.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.initialize_tpu_system`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/initialize_tpu_system)

tf.tpu.experimental.initialize_tpu_system(
        cluster_resolver=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding)<br>    <br>*   [Migrate from TPUEstimator to TPUStrategy](https://www.tensorflow.org/guide/migrate/tpu_estimator)<br>    <br>*   [Use TPUs](https://www.tensorflow.org/guide/tpu) | *   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer)<br>    <br>*   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index)<br>    <br>*   [Image classification with Model Garden](https://www.tensorflow.org/tfmodels/vision/image_classification)<br>    <br>*   [Instance Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)<br>    <br>*   [Object detection with Model Garden](https://www.tensorflow.org/tfmodels/vision/object_detection) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cluster_resolver` | A tf.distribute.cluster\_resolver.TPUClusterResolver, which provides information about the TPU cluster. |

|     |
| --- |
| Returns<br>------- |     |
| The tf.tpu.Topology object for the topology of the TPU cluster. If called inside tf.function, it returns the serialized topology object instead. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If running inside a tf.function. |
| `NotFoundError` | If no TPU devices found in eager mode. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.