[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.copy\_to\_mesh Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/api.py#L167-L188)

Copies a tf.Tensor onto the DTensor device with the given layout.

tf.experimental.dtensor.copy_to_mesh(
        tensor: Any,
        layout: tf.experimental.dtensor.Layout,
        source_layout: Optional[tf.experimental.dtensor.Layout] = None
    ) -> tf.Tensor

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview) | *   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial) |

Copies a regular tf.Tensor onto the DTensor device. Use the mesh attached to `layout` as target mesh. This method currently only supports replicated layouts, or one-to-one copies for sharded layouts.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A regular tf.Tensor to be copied as a DTensor. |
| `layout` | Target layout (and mesh) for the result DTensor. |
| `source_layout` | Source layout of the tensor before copy. This argument is deprecated. |

|     |
| --- |
| Returns<br>------- |     |
| A DTensor on the DTensor device with the given layout. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.