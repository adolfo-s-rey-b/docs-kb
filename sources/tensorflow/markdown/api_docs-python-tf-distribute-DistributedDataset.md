[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2FDistributedDataset&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset#methods)
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset#__iter__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.DistributedDataset Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset#methods)
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset#__iter__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/distribute.py#L307-L508)

Represents a dataset distributed among devices and machines.

A [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 could be thought of as a "distributed" dataset. When you use [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
 API to scale training to multiple devices or machines, you also need to distribute the input data, which leads to a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 instance, instead of a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instance in the non-distributed case. In TF 2.x, [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 objects are Python iterables.

There are two APIs to create a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 object: [`tf.distribute.Strategy.experimental_distribute_dataset(dataset)`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_dataset)
and [`tf.distribute.Strategy.distribute_datasets_from_function(dataset_fn)`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#distribute_datasets_from_function)
. _When to use which?_ When you have a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instance, and the regular batch splitting (i.e. re-batch the input [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instance with a new batch size that is equal to the global batch size divided by the number of replicas in sync) and autosharding (i.e. the [`tf.data.experimental.AutoShardPolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy)
 options) work for you, use the former API. Otherwise, if you are _not_ using a canonical [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instance, or you would like to customize the batch splitting or sharding, you can wrap these logic in a `dataset_fn` and use the latter API. Both API handles prefetch to device for the user. For more details and examples, follow the links to the APIs.

There are two main usages of a `DistributedDataset` object:

1.  Iterate over it to generate the input for a single device or multiple devices, which is a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
     instance. To do this, you can:
    
    *   use a pythonic for-loop construct:
    
    global_batch_size = 4
        
    
    Placing the loop inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
     will give a performance boost. However `break` and `return` are currently not supported if the loop is placed inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    . We also don't support placing the loop inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
     when using [`tf.distribute.experimental.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/MultiWorkerMirroredStrategy)
     or [`tf.distribute.experimental.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TPUStrategy)
     with multiple workers.
    
    *   use `__iter__` to create an explicit iterator, which is of type [`tf.distribute.DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)
        
    
    global_batch_size = 4
        
    
    To achieve a performance improvement, you can also wrap the `strategy.run` call with a [`tf.range`](https://www.tensorflow.org/api_docs/python/tf/range)
     inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    . This runs multiple steps in a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    . Autograph will convert it to a [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)
     on the worker. However, it is less flexible comparing with running a single step inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    . For example, you cannot run things eagerly or arbitrary python code within the steps.
    
2.  Inspect the [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
     of the data generated by `DistributedDataset`.
    
    [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
     generates [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
     as input to the devices. If you pass the input to a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
     and would like to specify the shape and type of each Tensor argument to the function, you can pass a [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
     object to the `input_signature` argument of the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    . To get the [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
     of the input, you can use the `element_spec` property of the [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
     or [`tf.distribute.DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)
     object.
    
    For example:
    
    global_batch_size = 4
      

Visit the [tutorial](https://www.tensorflow.org/tutorials/distribute/input)
 on distributed input for more examples and caveats.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `element_spec` | The type specification of an element of this [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)<br>.<br><br>    global_batch_size = 16 |

Methods
-------

### `__iter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/distribute.py#L456-L478)

__iter__()

Creates an iterator for the [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
.

The returned iterator implements the Python Iterator protocol.

#### Example usage:

    global_batch_size = 4

|     |
| --- |
| Returns |     |
| An [`tf.distribute.DistributedIterator`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedIterator)<br> instance for the given [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)<br> object to enumerate over the distributed data. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.