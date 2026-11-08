[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.stack\_dynamic\_partitions Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_array_ops.py#L575-L678)

Stacks dynamic partitions of a Tensor or RaggedTensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.stack_dynamic_partitions`](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions)

tf.ragged.stack_dynamic_partitions(
        data, partitions, num_partitions, name=None
    )

Returns a RaggedTensor `output` with `num_partitions` rows, where the row `output[i]` is formed by stacking all slices `data[j1...jN]` such that `partitions[j1...jN] = i`. Slices of `data` are stacked in row-major order.

If `num_partitions` is an `int` (not a `Tensor`), then this is equivalent to `tf.ragged.stack(tf.dynamic_partition(data, partitions, num_partitions))`.

#### Example:

    data           = ['a', 'b', 'c', 'd', 'e']

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A `Tensor` or `RaggedTensor` containing the values to stack. |
| `partitions` | An `int32` or `int64` `Tensor` or `RaggedTensor` specifying the partition that each slice of `data` should be added to. `partitions.shape` must be a prefix of `data.shape`. Values must be greater than or equal to zero, and less than `num_partitions`. `partitions` is not required to be sorted. |
| `num_partitions` | An `int32` or `int64` scalar specifying the number of partitions to output. This determines the number of rows in `output`. |
| `name` | A name prefix for the returned tensor (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `RaggedTensor` containing the stacked partitions. The returned tensor has the same dtype as `data`, and its shape is `[num_partitions, (D)] + data.shape[partitions.rank:]`, where `(D)` is a ragged dimension whose length is the number of data slices stacked for each `partition`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.