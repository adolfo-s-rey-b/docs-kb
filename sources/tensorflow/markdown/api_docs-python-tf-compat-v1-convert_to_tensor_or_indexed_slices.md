[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.convert\_to\_tensor\_or\_indexed\_slices Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor_or_indexed_slices#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/indexed_slices.py#L277-L299)

Converts the given object to a `Tensor` or an `IndexedSlices`.

tf.compat.v1.convert_to_tensor_or_indexed_slices(
        value, dtype=None, name=None
    )

If `value` is an `IndexedSlices` or `SparseTensor` it is returned unmodified. Otherwise, it is converted to a `Tensor` using `convert_to_tensor()`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | An `IndexedSlices`, `SparseTensor`, or an object that can be consumed by `convert_to_tensor()`. |
| `dtype` | (Optional.) The required `DType` of the returned `Tensor` or `IndexedSlices`. |
| `name` | (Optional.) A name to use if a new `Tensor` is created. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`, `IndexedSlices`, or `SparseTensor` based on `value`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `dtype` does not match the element type of `value`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.