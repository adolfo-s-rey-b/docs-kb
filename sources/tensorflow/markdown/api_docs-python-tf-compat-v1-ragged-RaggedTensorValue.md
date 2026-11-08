[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#methods)
    *   [to\_list](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#to_list)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.ragged.RaggedTensorValue Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#methods)
    *   [to\_list](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue#to_list)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor_value.py#L24-L114)

Represents the value of a `RaggedTensor`.

tf.compat.v1.ragged.RaggedTensorValue(
        values, row_splits
    )

See [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 for a description of ragged tensors.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | A numpy array of any type and shape; or a RaggedTensorValue. |
| `row_splits` | A 1-D int32 or int64 numpy array. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` | The numpy dtype of values in this tensor. |
| `flat_values` | The innermost `values` array for this ragged tensor value. |
| `nested_row_splits` | The row\_splits for all ragged dimensions in this ragged tensor value. |
| `ragged_rank` | The number of ragged dimensions in this ragged tensor value. |
| `row_splits` | The split indices for the ragged tensor value. |
| `shape` | A tuple indicating the shape of this RaggedTensorValue. |
| `values` | The concatenated values for all rows in this tensor. |

Methods
-------

### `to_list`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_tensor_value.py#L105-L114)

to_list()

Returns this ragged tensor value as a nested Python list.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.