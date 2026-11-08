[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#used-in-the-notebooks)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#examples)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.type\_spec\_from\_value Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#used-in-the-notebooks)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#examples)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/type_spec.py#L960-L1006)

Returns a [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
 that represents the given `value`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.type_spec_from_value`](https://www.tensorflow.org/api_docs/python/tf/type_spec_from_value)

tf.type_spec_from_value(
        value
    ) -> tf.TypeSpec

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) |

|     |
| --- |
| Examples<br>-------- |     |
| >>> tf.type_spec_from_value(tf.constant([1, 2, 3]))<br>    TensorSpec(shape=(3,), dtype=tf.int32, name=None)<br>    >>> tf.type_spec_from_value(np.array([4.0, 5.0], np.float64))<br>    TensorSpec(shape=(2,), dtype=tf.float64, name=None)<br>    >>> tf.type_spec_from_value(tf.ragged.constant([[1, 2], [3, 4, 5]]))<br>    RaggedTensorSpec(TensorShape([2, None]), tf.int32, 1, tf.int64)<br><br>    example_input = tf.ragged.constant([[1, 2], [3]]) |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A value that can be accepted or returned by TensorFlow APIs. Accepted types for `value` include [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, any value that can be converted to [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> using [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)<br>, and any subclass of `CompositeTensor` (such as [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>). |

|     |
| --- |
| Returns<br>------- |     |
| A `TypeSpec` that is compatible with `value`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If a TypeSpec cannot be built for `value`, because its type is not supported. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.