[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/split)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/split?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/split#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/split#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/strings/split#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/split#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.split Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/strings/split#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/split#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/strings/split#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/split#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L467-L526)

Split elements of `input` based on `sep` into a `RaggedTensor`.

tf.strings.split(
        input, sep=None, maxsplit=-1, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [Load and preprocess images](https://www.tensorflow.org/tutorials/load_data/images)<br>    <br>*   [Using text and neural network features](https://www.tensorflow.org/decision_forests/tutorials/intermediate_colab)<br>    <br>*   [Sending Different Data To Particular Clients With federated\_language.federated\_select](https://www.tensorflow.org/federated/tutorials/federated_select)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

Let N be the size of `input` (typically N will be the batch size). Split each element of `input` based on `sep` and return a `RaggedTensor` containing the split tokens. Empty tokens are ignored.

#### Example:

    tf.strings.split('hello world').numpy()

If `sep` is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings. For example, `input` of `"1<>2<><>3"` and `sep` of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty string, consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.

Note that the above mentioned behavior matches python's str.split.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A string `Tensor` of rank `N`, the strings to split. If `rank(input)` is not known statically, then it is assumed to be `1`. |
| `sep` | `0-D` string `Tensor`, the delimiter string. |
| `maxsplit` | An `int`. If `maxsplit > 0`, limit of the split of the result. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If sep is not a string. |

|     |
| --- |
| Returns<br>------- |     |
| A `RaggedTensor` of rank `N+1`, the strings split according to the delimiter. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.