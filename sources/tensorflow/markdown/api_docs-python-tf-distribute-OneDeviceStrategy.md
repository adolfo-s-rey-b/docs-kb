[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#distribute_datasets_from_function)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#experimental_distribute_dataset)
        
    *   [experimental\_distribute\_values\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#experimental_distribute_values_from_function)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#experimental_local_results)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#gather)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.OneDeviceStrategy Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#distribute_datasets_from_function)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#experimental_distribute_dataset)
        
    *   [experimental\_distribute\_values\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#experimental_distribute_values_from_function)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#experimental_local_results)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#gather)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/one_device_strategy.py#L38-L236)

A distribution strategy for running on a single device.

Inherits From: [`Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)

tf.distribute.OneDeviceStrategy(
        device
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load)<br>    <br>*   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index)<br>    <br>*   [Image classification with Model Garden](https://www.tensorflow.org/tfmodels/vision/image_classification)<br>    <br>*   [Instance Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)<br>    <br>*   [Object detection with Model Garden](https://www.tensorflow.org/tfmodels/vision/object_detection) |

Using this strategy will place any variables created in its scope on the specified device. Input distributed through this strategy will be prefetched to the specified device. Moreover, any functions called via `strategy.run` will also be placed on the specified device as well.

Typical usage of this strategy could be testing your code with the tf.distribute.Strategy API before switching to other strategies which actually distribute to multiple devices/machines.

#### For example:

strategy = tf.distribute.OneDeviceStrategy(device="/gpu:0")
    
    with strategy.scope():
      v = tf.Variable(1.0)
      print(v.device)  # /job:localhost/replica:0/task:0/device:GPU:0
    
    def step_fn(x):
      return x * 2
    
    result = 0
    for i in range(10):
      result += strategy.run(step_fn, args=(i,))
    print(result)  # 90

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device` | Device string identifier for the device on which the variables should be placed. See class docs for more details on how the device is used. Examples: "/cpu:0", "/gpu:0", "/device:CPU:0", "/device:GPU:0" |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `cluster_resolver` | Returns the cluster resolver associated with this strategy.<br><br>In general, when using a multi-worker [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)<br> strategy such as [`tf.distribute.experimental.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/MultiWorkerMirroredStrategy)<br> or [`tf.distribute.TPUStrategy()`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)<br>, there is a [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> associated with the strategy used, and such an instance is returned by this property.<br><br>Strategies that intend to have an associated [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> must set the relevant attribute, or override this property; otherwise, `None` is returned by default. Those strategies should also provide information regarding what is returned by this property.<br><br>Single-worker strategies usually do not have a [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>, and in those cases this property will return `None`.<br><br>The [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> may be useful when the user needs to access information such as the cluster spec, task type or task id. For example,<br><br>os.environ['TF_CONFIG'] = json.dumps({<br>      'cluster': {<br>          'worker': ["localhost:12345", "localhost:23456"],<br>          'ps': ["localhost:34567"]<br>      },<br>      'task': {'type': 'worker', 'index': 0}<br>    })<br>    <br>    # This implicitly uses TF_CONFIG for the cluster and current task info.<br>    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()<br>    <br>    ...<br>    <br>    if strategy.cluster_resolver.task_type == 'worker':<br>      # Perform something that's only applicable on workers. Since we set this<br>      # as a worker above, this block will run on this particular instance.<br>    elif strategy.cluster_resolver.task_type == 'ps':<br>      # Perform something that's only applicable on parameter servers. Since we<br>      # set this as a worker above, this block will not run on this particular<br>      # instance.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s API docstring. |
| `extended` | [`tf.distribute.StrategyExtended`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended)<br> with additional methods. |
| `num_replicas_in_sync` | Returns number of replicas over which gradients are aggregated. |

Methods
-------

### `distribute_datasets_from_function`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/one_device_strategy.py#L111-L153)

distribute_datasets_from_function(
        dataset_fn, options=None
    )

Distributes [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instances created by calls to `dataset_fn`.

`dataset_fn` will be called once for each worker in the strategy. In this case, we only have one worker and one device so `dataset_fn` is called once.

The `dataset_fn` should take an [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)
 instance where information about batching and input replication can be accessed:

def dataset_fn(input_context):
      batch_size = input_context.get_per_replica_batch_size(global_batch_size)
      d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
      return d.shard(
          input_context.num_input_pipelines, input_context.input_pipeline_id)
    
    inputs = strategy.distribute_datasets_from_function(dataset_fn)
    
    for batch in inputs:
      replica_results = strategy.run(replica_fn, args=(batch,))

|     |     |
| --- | --- |
| Args |     |
| `dataset_fn` | A function taking a [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)<br> instance and returning a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>. |
| `options` | [`tf.distribute.InputOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions)<br> used to control options on how this dataset is distributed. |

|     |
| --- |
| Returns |     |
| A "distributed `Dataset`", which the caller can iterate over like regular datasets. |     |

### `experimental_distribute_dataset`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/one_device_strategy.py#L82-L109)

experimental_distribute_dataset(
        dataset, options=None
    )

Distributes a tf.data.Dataset instance provided via dataset.

In this case, there is only one device, so this is only a thin wrapper around the input dataset. It will, however, prefetch the input data to the specified device. The returned distributed dataset can be iterated over similar to how regular datasets can.

#### Example:

strategy = tf.distribute.OneDeviceStrategy()
    dataset = tf.data.Dataset.range(10).batch(2)
    dist_dataset = strategy.experimental_distribute_dataset(dataset)
    for x in dist_dataset:
      print(x)  # [0, 1], [2, 3],...

Args: dataset: [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 to be prefetched to device. options: [`tf.distribute.InputOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions)
 used to control options on how this dataset is distributed. Returns: A "distributed `Dataset`" that the caller can iterate over.

### `experimental_distribute_values_from_function`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2030-L2107)

experimental_distribute_values_from_function(
        value_fn
    )

Generates [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 from `value_fn`.

This function is to generate [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 to pass into `run`, `reduce`, or other methods that take distributed values when not using datasets.

|     |     |
| --- | --- |
| Args |     |
| `value_fn` | The function to run to generate values. It is called for each replica with `tf.distribute.ValueContext` as the sole argument. It must return a Tensor or a type that can be converted to a Tensor. |

|     |
| --- |
| Returns |     |
| A [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> containing a value for each replica. |     |

#### Example usage:

1.  Return constant value per replica:
    
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        
2.  Distribute values in array based on replica\_id:
    
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        
3.  Specify values using num\_replicas\_in\_sync:
    
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        
4.  Place values on devices and distribute:
    
    strategy = tf.distribute.TPUStrategy()
        worker_devices = strategy.extended.worker_devices
        multiple_values = []
        for i in range(strategy.num_replicas_in_sync):
          with tf.device(worker_devices[i]):
            multiple_values.append(tf.constant(1.0))
        
        def value_fn(ctx):
          return multiple_values[ctx.replica_id_in_sync_group]
        
        distributed_values = strategy.
          experimental_distribute_values_from_function(
          value_fn)
    

### `experimental_local_results`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/one_device_strategy.py#L155-L169)

experimental_local_results(
        value
    )

Returns the list of all local per-replica values contained in `value`.

In `OneDeviceStrategy`, the `value` is always expected to be a single value, so the result is just the value in a tuple.

|     |     |
| --- | --- |
| Args |     |
| `value` | A value returned by `experimental_run()`, `run()`, `extended.call_for_each_replica()`, or a variable created in `scope`. |

|     |
| --- |
| Returns |     |
| A tuple of values contained in `value`. If `value` represents a single value, this returns `(value,).` |     |

### `gather`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2109-L2214)

gather(
        value, axis
    )

Gather `value` across replicas along `axis` to the current device.

Given a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 or [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
\-like object `value`, this API gathers and concatenates `value` across replicas along the `axis`\-th dimension. The result is copied to the "current" device, which would typically be the CPU of the worker on which the program is running. For [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
, it is the first TPU host. For multi-client [`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
, this is the CPU of each worker.

This API can only be called in the cross-replica context. For a counterpart in the replica context, see [`tf.distribute.ReplicaContext.all_gather`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_gather)
.

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

Consider the following example for more combinations:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1", "GPU:2", "GPU:3"])

|     |     |
| --- | --- |
| Args |     |
| `value` | a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> instance, e.g. returned by [`Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run)<br>, to be combined into a single tensor. It can also be a regular tensor when used with [`tf.distribute.OneDeviceStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy)<br> or the default strategy. The tensors that constitute the DistributedValues can only be dense tensors with non-zero rank, NOT a [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)<br>. |
| `axis` | 0-D int32 Tensor. Dimension along which to gather. Must be in the range \[0, rank(value)). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor` that's the concatenation of `value` across replicas along `axis` dimension. |     |\
\
### `reduce`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/one_device_strategy.py#L189-L220)\
\
reduce(\
        reduce_op, value, axis\
    )\
\
Reduce `value` across replicas.\
\
In `OneDeviceStrategy`, there is only one replica, so if axis=None, value is simply returned. If axis is specified as something other than None, such as axis=0, value is reduced along that axis and returned.\
\
#### Example:\
\
t = tf.range(10)\
    \
    result = strategy.reduce(tf.distribute.ReduceOp.SUM, t, axis=None).numpy()\
    # result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\
    \
    result = strategy.reduce(tf.distribute.ReduceOp.SUM, t, axis=0).numpy()\
    # result: 45\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `reduce_op` | A [`tf.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)<br> value specifying how values should be combined. |\
| `value` | A "per replica" value, e.g. returned by `run` to be combined into a single tensor. |\
| `axis` | Specifies the dimension to reduce along within each replica's tensor. Should typically be set to the batch dimension, or `None` to only reduce across replicas (e.g. if the tensor has no batch dimension). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. |     |\
\
### `run`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/one_device_strategy.py#L171-L187)\
\
run(\
        fn, args=(), kwargs=None, options=None\
    )\
\
Run `fn` on each replica, with the given arguments.\
\
In `OneDeviceStrategy`, `fn` is simply called within a device scope for the given device, with the provided arguments.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `fn` | The function to run. The output must be a [`tf.nest`](https://www.tensorflow.org/api_docs/python/tf/nest)<br> of `Tensor`s. |\
| `args` | (Optional) Positional arguments to `fn`. |\
| `kwargs` | (Optional) Keyword arguments to `fn`. |\
| `options` | (Optional) An instance of [`tf.distribute.RunOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/RunOptions)<br> specifying the options to run `fn`. |\
\
|     |\
| --- |\
| Returns |     |\
| Return value from running `fn`. |     |\
\
### `scope`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/one_device_strategy.py#L222-L236)\
\
scope()\
\
Returns a context manager selecting this Strategy as current.\
\
Inside a `with strategy.scope():` code block, this thread will use a variable creator set by `strategy`, and will enter its "cross-replica context".\
\
In `OneDeviceStrategy`, all variables created inside `strategy.scope()` will be on `device` specified at strategy construction time. See example in the docs for this class.\
\
|     |\
| --- |\
| Returns |     |\
| A context manager to use for creating variables with this strategy. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.