[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/is_tensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/is_tensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/is_tensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/is_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/is_tensor#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.is\_tensor Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/is_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/is_tensor#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_util.py#L1256-L1290)

Checks whether `x` is a TF-native type that can be passed to many TF ops.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.is_tensor`](https://www.tensorflow.org/api_docs/python/tf/is_tensor)

tf.is_tensor(
        x
    )

Use `is_tensor` to differentiate types that can ingested by TensorFlow ops without any conversion (e.g., [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
, [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
, and [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
) from types that need to be converted into tensors before they are ingested (e.g., numpy `ndarray` and Python scalars).

For example, in the following code block:

if not tf.is_tensor(t):
      t = tf.convert_to_tensor(t)
    return t.shape, t.dtype

we check to make sure that `t` is a tensor (and convert it if not) before accessing its `shape` and `dtype`. (But note that not all TensorFlow native types have shapes or dtypes; [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 is an example of a TensorFlow native type that has neither shape nor dtype.)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A python object to check. |

|     |
| --- |
| Returns<br>------- |     |
| `True` if `x` is a TensorFlow-native type. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.