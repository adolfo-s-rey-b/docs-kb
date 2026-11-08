[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition#raises)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.dynamic\_partition Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition#raises)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition#returns)
    

Partitions `data` into `num_partitions` tensors using indices from `partitions`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.dynamic_partition`](https://www.tensorflow.org/api_docs/python/tf/dynamic_partition)

tf.dynamic_partition(
        data: Annotated[Any, TV_DynamicPartition_T],
        partitions: Annotated[Any, _atypes.Int32],
        num_partitions: int,
        name=None
    )

For each index tuple `js` of size `partitions.ndim`, the slice `data[js, ...]` becomes part of `outputs[partitions[js]]`. The slices with `partitions[js] = i` are placed in `outputs[i]` in lexicographic order of `js`, and the first dimension of `outputs[i]` is the number of entries in `partitions` equal to `i`. In detail,

    outputs[i].shape = [sum(partitions == i)] + data.shape[partitions.ndim:]
    
        outputs[i] = pack([data[js, ...] for js if partitions[js] == i])

`data.shape` must start with `partitions.shape`.

#### For example:

    # Scalar partitions.
        partitions = 1
        num_partitions = 2
        data = [10, 20]
        outputs[0] = []  # Empty with shape [0, 2]
        outputs[1] = [[10, 20]]
    
        # Vector partitions.
        partitions = [0, 0, 1, 1, 0]
        num_partitions = 2
        data = [10, 20, 30, 40, 50]
        outputs[0] = [10, 20, 50]
        outputs[1] = [30, 40]

See `dynamic_stitch` for an example on how to merge partitions back.

![](https://www.tensorflow.org/images/DynamicPartition.png)

|     |
| --- |
| Raises<br>------ |     |
| *   `InvalidArgumentError` in following cases:<br>*   If partitions is not in range `[0, num_partiions)`<br>*   If `partitions.shape` does not match prefix of `data.shape` argument. |     |\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `data` | A `Tensor`. |\
| `partitions` | A `Tensor` of type `int32`. Any shape. Indices in the range `[0, num_partitions)`. |\
| `num_partitions` | An `int` that is `>= 1`. The number of partitions to output. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A list of `num_partitions` `Tensor` objects with the same type as `data`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2024-04-26 UTC.