[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/dynamic_stitch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/dynamic_stitch)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/dynamic_stitch?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dynamic_stitch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dynamic_stitch#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.dynamic\_stitch Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dynamic_stitch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dynamic_stitch#returns)
    

Interleave the values from the `data` tensors into a single tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.dynamic_stitch`](https://www.tensorflow.org/api_docs/python/tf/dynamic_stitch)

tf.dynamic_stitch(
        indices: Annotated[List[Any], _atypes.Int32],
        data: Annotated[List[Any], TV_DynamicStitch_T],
        name=None
    ) -> Annotated[Any, TV_DynamicStitch_T]

Builds a merged tensor such that

    merged[indices[m][i, ..., j], ...] = data[m][i, ..., j, ...]

For example, if each `indices[m]` is scalar or vector, we have

    # Scalar indices:
        merged[indices[m], ...] = data[m][...]
    
        # Vector indices:
        merged[indices[m][i], ...] = data[m][i, ...]

Each `data[i].shape` must start with the corresponding `indices[i].shape`, and the rest of `data[i].shape` must be constant w.r.t. `i`. That is, we must have `data[i].shape = indices[i].shape + constant`. In terms of this `constant`, the output shape is

merged.shape = [max(indices) + 1] + constant

Values are merged in order, so if an index appears in both `indices[m][i]` and `indices[n][j]` for `(m,i) < (n,j)` the slice `data[n][j]` will appear in the merged result. If you do not need this guarantee, ParallelDynamicStitch might perform better on some devices.

#### For example:

    indices[0] = 6
        indices[1] = [4, 1]
        indices[2] = [[5, 2], [0, 3]]
        data[0] = [61, 62]
        data[1] = [[41, 42], [11, 12]]
        data[2] = [[[51, 52], [21, 22]], [[1, 2], [31, 32]]]
        merged = [[1, 2], [11, 12], [21, 22], [31, 32], [41, 42],\
                  [51, 52], [61, 62]]

This method can be used to merge partitions created by `dynamic_partition` as illustrated on the following example:

    # Apply function (increments x_i) on elements for which a certain condition
        # apply (x_i != -1 in this example).
        x=tf.constant([0.1, -1., 5.2, 4.3, -1., 7.4])
        condition_mask=tf.not_equal(x,tf.constant(-1.))
        partitioned_data = tf.dynamic_partition(
            x, tf.cast(condition_mask, tf.int32) , 2)
        partitioned_data[1] = partitioned_data[1] + 1.0
        condition_indices = tf.dynamic_partition(
            tf.range(tf.shape(x)[0]), tf.cast(condition_mask, tf.int32) , 2)
        x = tf.dynamic_stitch(condition_indices, partitioned_data)
        # Here x=[1.1, -1., 6.2, 5.3, -1, 8.4], the -1. values remain
        # unchanged.

![](https://www.tensorflow.org/images/DynamicStitch.png)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `indices` | A list of at least 1 `Tensor` objects with type `int32`. |
| `data` | A list with the same length as `indices` of `Tensor` objects with the same type. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `data`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.