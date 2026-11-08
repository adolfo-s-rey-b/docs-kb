[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsaved_model%2Fget_tensor_from_tensor_info&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.saved\_model.get\_tensor\_from\_tensor\_info Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/saved_model/utils_impl.py#L143-L187)

Returns the Tensor or CompositeTensor described by a TensorInfo proto. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.saved_model.utils.get_tensor_from_tensor_info`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/get_tensor_from_tensor_info)

tf.compat.v1.saved_model.get_tensor_from_tensor_info(
        tensor_info, graph=None, import_scope=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor_info` | A TensorInfo proto describing a Tensor or SparseTensor or CompositeTensor. |
| `graph` | The tf.Graph in which tensors are looked up. If None, the current default graph is used. |
| `import_scope` | If not None, names in `tensor_info` are prefixed with this string before lookup. |

|     |
| --- |
| Returns<br>------- |     |
| The Tensor or SparseTensor or CompositeTensor in `graph` described by `tensor_info`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `KeyError` | If `tensor_info` does not correspond to a tensor in `graph`. |
| `ValueError` | If `tensor_info` is malformed. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.