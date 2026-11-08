[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsaved_model%2Fbuild_tensor_info&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.build\_tensor\_info Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/utils_impl.py#L41-L68)

Utility function to build TensorInfo proto from a Tensor. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.utils.build_tensor_info`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/build_tensor_info)

tf.compat.v1.saved_model.build_tensor_info(
        tensor
    )

Migrate to TF2
--------------

This API is not compatible with eager execution as `tensor` needs to be a graph tensor, and there is no replacement for it in TensorFlow 2.x. To start writing programs using TensorFlow 2.x, please refer to the [Effective TensorFlow 2](https://www.tensorflow.org/guide/effective_tf2)
 guide.

Description
-----------

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | Tensor or SparseTensor whose name, dtype and shape are used to build the TensorInfo. For SparseTensors, the names of the three constituent Tensors are used. |

|     |
| --- |
| Returns<br>------- |     |
| A TensorInfo protocol buffer constructed based on the supplied argument. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If eager execution is enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.