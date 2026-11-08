[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/slice#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/slice)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/slice?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/slice#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/slice#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/slice#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.slice Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/slice#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/slice#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/slice#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L940-L992)

Extracts a slice from a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.slice`](https://www.tensorflow.org/api_docs/python/tf/slice)

tf.slice(
        input_, begin, size, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to tensor slicing](https://www.tensorflow.org/guide/tensor_slicing)<br>    <br>*   [TFLite Authoring Tool](https://www.tensorflow.org/lite/guide/authoring)<br>    <br>*   [TensorFlow Lite Model Analyzer](https://www.tensorflow.org/lite/guide/model_analyzer) | *   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb) |

See also [`tf.strided_slice`](https://www.tensorflow.org/api_docs/python/tf/strided_slice)
.

This operation extracts a slice of size `size` from a tensor `input_` starting at the location specified by `begin`. The slice `size` is represented as a tensor shape, where `size[i]` is the number of elements of the 'i'th dimension of `input_` that you want to slice. The starting location (`begin`) for the slice is represented as an offset in each dimension of `input_`. In other words, `begin[i]` is the offset into the i'th dimension of `input_` that you want to slice from.

Note that [`tf.Tensor.**getitem**`](https://www.tensorflow.org/api_docs/python/tf/Tensor#__getitem__)
 is typically a more pythonic way to perform slices, as it allows you to write `foo[3:7, :-2]` instead of `tf.slice(foo, [3, 0], [4, foo.get_shape()[1]-2])`.

`begin` is zero-based; `size` is one-based. If `size[i]` is -1, all remaining elements in dimension i are included in the slice. In other words, this is equivalent to setting:

`size[i] = input_.dim_size(i) - begin[i]`

This operation requires that:

`0 <= begin[i] <= begin[i] + size[i] <= Di for i in [0, n]`

#### For example:

t = tf.constant([[[1, 1, 1], [2, 2, 2]],\
                     [[3, 3, 3], [4, 4, 4]],\
                     [[5, 5, 5], [6, 6, 6]]])
    tf.slice(t, [1, 0, 0], [1, 1, 3])  # [[[3, 3, 3]]]
    tf.slice(t, [1, 0, 0], [1, 2, 3])  # [[[3, 3, 3],\
                                       #   [4, 4, 4]]]
    tf.slice(t, [1, 0, 0], [2, 1, 3])  # [[[3, 3, 3]],\
                                       #  [[5, 5, 5]]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_` | A `Tensor`. |
| `begin` | An `int16`, `int32` or `int64` `Tensor`. |
| `size` | An `int16`, `int32` or `int64` `Tensor`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` the same type as `input_`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.