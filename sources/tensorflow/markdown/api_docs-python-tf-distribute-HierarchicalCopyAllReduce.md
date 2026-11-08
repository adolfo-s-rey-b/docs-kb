[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2FHierarchicalCopyAllReduce&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#methods)
    *   [batch\_reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#batch_reduce)
        
    *   [broadcast](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#broadcast)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#reduce)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.HierarchicalCopyAllReduce Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#methods)
    *   [batch\_reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#batch_reduce)
        
    *   [broadcast](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#broadcast)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce#reduce)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cross_device_ops.py#L996-L1036)

Hierarchical copy all-reduce implementation of CrossDeviceOps.

Inherits From: [`CrossDeviceOps`](https://www.tensorflow.org/api_docs/python/tf/distribute/CrossDeviceOps)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.HierarchicalCopyAllReduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce)

tf.distribute.HierarchicalCopyAllReduce(
        num_packs=1
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training) |

It reduces to one GPU along edges in some hierarchy and broadcasts back to each GPU along the same path. For the batch API, tensors will be repacked or aggregated for more efficient cross-device transportation.

This is a reduction created for Nvidia DGX-1 which assumes GPUs connects like that on DGX-1 machine. If you have different GPU inter-connections, it is likely that it would be slower than [`tf.distribute.ReductionToOneDevice`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReductionToOneDevice)
.

For reduces that are not all-reduce, it falls back to [`tf.distribute.ReductionToOneDevice`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReductionToOneDevice)
.

Here is how you can use `HierarchicalCopyAllReduce` in [`tf.distribute.MirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy)
:

  strategy = tf.distribute.MirroredStrategy(
        cross_device_ops=tf.distribute.HierarchicalCopyAllReduce())

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_packs` | a non-negative integer. The number of packs to split values into. If zero, no packing will be done. |

|     |
| --- |
| Raises<br>------ |     |
| ValueError if `num_packs` is negative. |     |

Methods
-------

### `batch_reduce`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cross_device_ops.py#L400-L447)

batch_reduce(
        reduce_op, value_destination_pairs, options=None
    )

Reduce values to destinations in batches.

See [`tf.distribute.StrategyExtended.batch_reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#batch_reduce_to)
. This can only be called in the cross-replica context.

|     |     |
| --- | --- |
| Args |     |
| `reduce_op` | a [`tf.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)<br> specifying how values should be combined. |
| `value_destination_pairs` | a sequence of (value, destinations) pairs. See [`tf.distribute.CrossDeviceOps.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/CrossDeviceOps#reduce)<br> for descriptions. |
| `options` | a [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br>. See [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br> for details. |

|     |
| --- |
| Returns |     |
| A list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>, one per pair in `value_destination_pairs`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if `value_destination_pairs` is not an iterable of tuples of [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> and destinations. |

### `broadcast`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cross_device_ops.py#L449-L466)

broadcast(
        tensor, destinations
    )

Broadcast `tensor` to `destinations`.

This can only be called in the cross-replica context.

|     |     |
| --- | --- |
| Args |     |
| `tensor` | a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> like object. The value to broadcast. |
| `destinations` | a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>, a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>, a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> alike object, or a device string. It specifies the devices to broadcast to. Note that if it's a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>, the value is broadcasted to the devices of that variable, this method doesn't update the variable. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>. |     |

### `reduce`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/cross_device_ops.py#L275-L321)

reduce(
        reduce_op, per_replica_value, destinations, options=None
    )

Reduce `per_replica_value` to `destinations`.

See [`tf.distribute.StrategyExtended.reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#reduce_to)
. This can only be called in the cross-replica context.

|     |     |
| --- | --- |
| Args |     |
| `reduce_op` | a [`tf.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)<br> specifying how values should be combined. |
| `per_replica_value` | a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>, or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> like object. |
| `destinations` | a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>, a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>, a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> alike object, or a device string. It specifies the devices to reduce to. To perform an all-reduce, pass the same to `value` and `destinations`. Note that if it's a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>, the value is reduced to the devices of that variable, and this method doesn't update the variable. |
| `options` | a [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br>. See [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br> for details. |

|     |
| --- |
| Returns |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> or [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if per\_replica\_value can't be converted to a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> or if destinations is not a string, [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> or [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.