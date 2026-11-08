[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reverse_sequence?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reverse_sequence?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reverse_sequence?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reverse_sequence?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reverse_sequence?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.reverse\_sequence Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reverse_sequence?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/reverse_sequence?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L4658-L4721)

Reverses variable length slices. (deprecated arguments) (deprecated arguments)

tf.compat.v1.reverse_sequence(
        input,
        seq_lengths,
        seq_axis=None,
        batch_axis=None,
        name=None,
        seq_dim=None,
        batch_dim=None
    )

This op first slices `input` along the dimension `batch_axis`, and for each slice `i`, reverses the first `seq_lengths[i]` elements along the dimension `seq_axis`.

The elements of `seq_lengths` must obey `seq_lengths[i] <= input.dims[seq_axis]`, and `seq_lengths` must be a vector of length `input.dims[batch_axis]`.

The output slice `i` along dimension `batch_axis` is then given by input slice `i`, with the first `seq_lengths[i]` slices along dimension `seq_axis` reversed.

#### Example usage:

    seq_lengths = [7, 2, 3, 5]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. The input to reverse. |
| `seq_lengths` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 1-D with length `input.dims(batch_axis)` and `max(seq_lengths) <= input.dims(seq_axis)` |
| `seq_axis` | An `int`. The dimension which is partially reversed. |
| `batch_axis` | An optional `int`. Defaults to `0`. The dimension along which reversal is performed. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor. Has the same type as input. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.