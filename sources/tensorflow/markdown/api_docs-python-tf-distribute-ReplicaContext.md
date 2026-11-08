[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#methods)
    *   [all\_gather](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_gather)
        
    *   [all\_reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_reduce)
        
    *   [merge\_call](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#merge_call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.ReplicaContext Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#methods)
    *   [all\_gather](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_gather)
        
    *   [all\_reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_reduce)
        
    *   [merge\_call](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#merge_call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3669-L3917)

A class with a collection of APIs that can be called in a replica context.

tf.distribute.ReplicaContext(
        strategy, replica_id_in_sync_group
    )

You can use [`tf.distribute.get_replica_context`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context)
 to get an instance of `ReplicaContext`, which can only be called inside the function passed to [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run)
.

    strategy = tf.distribute.MirroredStrategy(['GPU:0', 'GPU:1'])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `strategy` | A [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br>. |
| `replica_id_in_sync_group` | An integer, a `Tensor` or None. Prefer an integer whenever possible to avoid issues with nested [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>. It accepts a `Tensor` only to be compatible with `tpu.replicate`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `devices` | Returns the devices this replica is to be executed on, as a tuple of strings. (deprecated) |
| `num_replicas_in_sync` | Returns number of replicas that are kept in sync. |
| `replica_id_in_sync_group` | Returns the id of the replica.<br><br>This identifies the replica among all replicas that are kept in sync. The value of the replica id can range from 0 to [`tf.distribute.ReplicaContext.num_replicas_in_sync`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#num_replicas_in_sync)<br> - 1. |
| `strategy` | The current [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> object. |

Methods
-------

### `all_gather`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3674-L3829)

all_gather(
        value, axis, options=None
    )

All-gathers `value` across all replicas along `axis`.

For all strategies except [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
, the input `value` on different replicas must have the same rank, and their shapes must be the same in all dimensions except the `axis`\-th dimension. In other words, their shapes cannot be different in a dimension `d` where `d` does not equal to the `axis` argument. For example, given a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 with component tensors of shape `(1, 2, 3)` and `(1, 3, 3)` on two replicas, you can call `all_gather(..., axis=1, ...)` on it, but not `all_gather(..., axis=0, ...)` or `all_gather(..., axis=2, ...)`. However, with [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
, all tensors must have exactly the same rank and same shape.

You can pass in a single tensor to all-gather:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

You can also pass in a nested structure of tensors to all-gather, say, a list:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

What if you are all-gathering tensors with different shapes on different replicas? Consider the following example with two replicas, where you have `value` as a nested structure consisting of two items to all-gather, `a` and `b`.

*   On Replica 0, `value` is `{'a': [0], 'b': [[0, 1]]}`.
*   On Replica 1, `value` is `{'a': [1], 'b': [[2, 3], [4, 5]]}`.
*   Result for `all_gather` with `axis=0` (on each of the replicas) is:
    
    {'a': [1, 2], 'b': [[0, 1], [2, 3], [4, 5]]}
    

|     |     |
| --- | --- |
| Args |     |
| `value` | a nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> which [`tf.nest.flatten`](https://www.tensorflow.org/api_docs/python/tf/nest/flatten)<br> accepts, or a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> instance. The structure of the [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> need to be same on all replicas. The underlying tensor constructs can only be dense tensors with non-zero rank, NOT [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br>. |
| `axis` | 0-D int32 Tensor. Dimension along which to gather. |
| `options` | a [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br>. Options to perform collective operations. This overrides the default options if the [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> takes one in the constructor. See [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br> for details of the options. |

|     |
| --- |
| Returns |     |
| A nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> with the gathered values. The structure is the same as `value`. |     |

### `all_reduce`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3546-L3656)

all_reduce(
        reduce_op, value, options=None
    )

All-reduces `value` across all replicas.

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

It supports batched operations. You can pass a list of values and it attempts to batch them when possible. You can also specify `options` to indicate the desired batching behavior, e.g. batch the values into multiple packs so that they can better overlap with computations.

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

Note that all replicas need to participate in the all-reduce, otherwise this operation hangs. Note that if there're multiple all-reduces, they need to execute in the same order on all replicas. Dispatching all-reduce based on conditions is usually error-prone.

Known limitation: if `value` contains [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
, attempting to compute gradient w.r.t `value` would result in an error.

This API currently can only be called in the replica context. Other variants to reduce values across replicas are:

*   [`tf.distribute.StrategyExtended.reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#reduce_to)
    : the reduce and all-reduce API in the cross-replica context.
*   [`tf.distribute.StrategyExtended.batch_reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#batch_reduce_to)
    : the batched reduce and all-reduce API in the cross-replica context.
*   [`tf.distribute.Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#reduce)
    : a more convenient method to reduce to the host in cross-replica context.

|     |     |
| --- | --- |
| Args |     |
| `reduce_op` | a [`tf.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)<br> value specifying how values should be combined. Allows using string representation of the enum such as "SUM", "MEAN". |
| `value` | a potentially nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br> which [`tf.nest.flatten`](https://www.tensorflow.org/api_docs/python/tf/nest/flatten)<br> accepts. The structure and the shapes of `value` need to be same on all replicas. |
| `options` | a [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br>. Options to perform collective operations. This overrides the default options if the [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> takes one in the constructor. See [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br> for details of the options. |

|     |
| --- |
| Returns |     |
| A nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> with the reduced values. The structure is the same as `value`. |     |

### `merge_call`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3445-L3478)

merge_call(
        merge_fn, args=(), kwargs=None
    )

Merge args across replicas and run `merge_fn` in a cross-replica context.

This allows communication and coordination when there are multiple calls to the step\_fn triggered by a call to `strategy.run(step_fn, ...)`.

See [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run)
 for an explanation.

If not inside a distributed scope, this is equivalent to:

strategy = tf.distribute.get_strategy()
    with cross-replica-context(strategy):
      return merge_fn(strategy, *args, **kwargs)

|     |     |
| --- | --- |
| Args |     |
| `merge_fn` | Function that joins arguments from threads that are given as PerReplica. It accepts [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> object as the first argument. |
| `args` | List or tuple with positional per-thread arguments for `merge_fn`. |
| `kwargs` | Dict with keyword per-thread arguments for `merge_fn`. |

|     |
| --- |
| Returns |     |
| The return value of `merge_fn`, except for `PerReplica` values which are unpacked. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.