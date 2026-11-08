[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fexperimental%2FCentralStorageStrategy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#distribute_datasets_from_function)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#experimental_distribute_dataset)
        
    *   [experimental\_distribute\_values\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#experimental_distribute_values_from_function)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#experimental_local_results)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#gather)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.CentralStorageStrategy Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#distribute_datasets_from_function)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#experimental_distribute_dataset)
        
    *   [experimental\_distribute\_values\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#experimental_distribute_values_from_function)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#experimental_local_results)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#gather)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy#scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/central_storage_strategy.py#L23-L209)

A one-machine strategy that puts all variables on a single device.

Inherits From: [`Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)

tf.distribute.experimental.CentralStorageStrategy(
        compute_devices=None, parameter_device=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training) |

Variables are assigned to local CPU or the only GPU. If there is more than one GPU, compute operations (other than variable update operations) will be replicated across all GPUs.

#### For Example:

strategy = tf.distribute.experimental.CentralStorageStrategy()
    # Create a dataset
    ds = tf.data.Dataset.range(5).batch(2)
    # Distribute that dataset
    dist_dataset = strategy.experimental_distribute_dataset(ds)
    
    with strategy.scope():
      @tf.function
      def train_step(val):
        return val + 1
    
      # Iterate over the distributed dataset
      for x in dist_dataset:
        # process dataset elements
        strategy.run(train_step, args=(x,))

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `cluster_resolver` | Returns the cluster resolver associated with this strategy.<br><br>In general, when using a multi-worker [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)<br> strategy such as [`tf.distribute.experimental.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/MultiWorkerMirroredStrategy)<br> or [`tf.distribute.TPUStrategy()`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)<br>, there is a [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> associated with the strategy used, and such an instance is returned by this property.<br><br>Strategies that intend to have an associated [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> must set the relevant attribute, or override this property; otherwise, `None` is returned by default. Those strategies should also provide information regarding what is returned by this property.<br><br>Single-worker strategies usually do not have a [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>, and in those cases this property will return `None`.<br><br>The [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> may be useful when the user needs to access information such as the cluster spec, task type or task id. For example,<br><br>os.environ['TF_CONFIG'] = json.dumps({<br>      'cluster': {<br>          'worker': ["localhost:12345", "localhost:23456"],<br>          'ps': ["localhost:34567"]<br>      },<br>      'task': {'type': 'worker', 'index': 0}<br>    })<br>    <br>    # This implicitly uses TF_CONFIG for the cluster and current task info.<br>    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()<br>    <br>    ...<br>    <br>    if strategy.cluster_resolver.task_type == 'worker':<br>      # Perform something that's only applicable on workers. Since we set this<br>      # as a worker above, this block will run on this particular instance.<br>    elif strategy.cluster_resolver.task_type == 'ps':<br>      # Perform something that's only applicable on parameter servers. Since we<br>      # set this as a worker above, this block will not run on this particular<br>      # instance.<br><br>For more information, please see [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>'s API docstring. |
| `extended` | [`tf.distribute.StrategyExtended`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended)<br> with additional methods. |
| `num_replicas_in_sync` | Returns number of replicas over which gradients are aggregated. |

Methods
-------

### `distribute_datasets_from_function`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1470-L1547)

distribute_datasets_from_function(
        dataset_fn, options=None
    )

Distributes [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instances created by calls to `dataset_fn`.

The argument `dataset_fn` that users pass in is an input function that has a [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)
 argument and returns a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instance. It is expected that the returned dataset from `dataset_fn` is already batched by per-replica batch size (i.e. global batch size divided by the number of replicas in sync) and sharded. [`tf.distribute.Strategy.distribute_datasets_from_function`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#distribute_datasets_from_function)
 does not batch or shard the [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instance returned from the input function. `dataset_fn` will be called on the CPU device of each of the workers and each generates a dataset where every replica on that worker will dequeue one batch of inputs (i.e. if a worker has two replicas, two batches will be dequeued from the `Dataset` every step).

This method can be used for several purposes. First, it allows you to specify your own batching and sharding logic. (In contrast, `tf.distribute.experimental_distribute_dataset` does batching and sharding for you.) For example, where `experimental_distribute_dataset` is unable to shard the input files, this method might be used to manually shard the dataset (avoiding the slow fallback behavior in `experimental_distribute_dataset`). In cases where the dataset is infinite, this sharding can be done by creating dataset replicas that differ only in their random seed.

The `dataset_fn` should take an [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)
 instance where information about batching and input replication can be accessed.

You can use `element_spec` property of the [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 returned by this API to query the [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
 of the elements returned by the iterator. This can be used to set the `input_signature` property of a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. Follow [`tf.distribute.DistributedDataset.element_spec`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset#element_spec)
 to see an example.

For a tutorial on more usage and properties of this method, refer to the [tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_datasets_from_function)
). If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches)
.

|     |     |
| --- | --- |
| Args |     |
| `dataset_fn` | A function taking a [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)<br> instance and returning a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>. |
| `options` | [`tf.distribute.InputOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions)<br> used to control options on how this dataset is distributed. |

|     |
| --- |
| Returns |     |
| A [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)<br>. |     |

### `experimental_distribute_dataset`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/central_storage_strategy.py#L73-L109)

experimental_distribute_dataset(
        dataset, options=None
    )

Distributes a tf.data.Dataset instance provided via dataset.

The returned dataset is a wrapped strategy dataset which creates a multidevice iterator under the hood. It prefetches the input data to the specified devices on the worker. The returned distributed dataset can be iterated over similar to how regular datasets can.

#### For Example:

strategy = tf.distribute.CentralStorageStrategy()  # with 1 CPU and 1 GPU
    dataset = tf.data.Dataset.range(10).batch(2)
    dist_dataset = strategy.experimental_distribute_dataset(dataset)
    for x in dist_dataset:
      print(x)  # Prints PerReplica values [0, 1], [2, 3],...

Args: dataset: [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 to be prefetched to device. options: [`tf.distribute.InputOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions)
 used to control options on how this dataset is distributed.

|     |
| --- |
| Returns |     |
| A "distributed `Dataset`" that the caller can iterate over. |     |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/central_storage_strategy.py#L111-L125)

experimental_local_results(
        value
    )

Returns the list of all local per-replica values contained in `value`.

In `CentralStorageStrategy` there is a single worker so the value returned will be all the values on that worker.

|     |     |
| --- | --- |
| Args |     |
| `value` | A value returned by `run()`, `extended.call_for_each_replica()`, or a variable created in `scope`. |

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
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/central_storage_strategy.py#L145-L209)\
\
reduce(\
        reduce_op, value, axis\
    )\
\
Reduce `value` across replicas.\
\
Given a per-replica value returned by `run`, say a per-example loss, the batch will be divided across all the replicas. This function allows you to aggregate across replicas and optionally also across batch elements. For example, if you have a global batch size of 8 and 2 replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and `[4, 5, 6, 7]` will be on replica 1. By default, `reduce` will just aggregate across replicas, returning `[0+4, 1+5, 2+6, 3+7]`. This is useful when each replica is computing a scalar or some other value that doesn't have a "batch" dimension (like a gradient). More often you will want to aggregate across the global batch, which you can get by specifying the batch dimension as the `axis`, typically `axis=0`. In this case it would return a scalar `0+1+2+3+4+5+6+7`.\
\
If there is a last partial batch, you will need to specify an axis so that the resulting shape is consistent across replicas. So if the last batch has size 6 and it is divided into \[0, 1, 2, 3\] and \[4, 5\], you would get a shape mismatch unless you specify `axis=0`. If you specify [`tf.distribute.ReduceOp.MEAN`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp#MEAN)\
, using `axis=0` will use the correct denominator of 6. Contrast this with computing `reduce_mean` to get a scalar value on each replica and this function to average those means, which will weigh some values `1/8` and others `1/4`.\
\
#### For Example:\
\
strategy = tf.distribute.experimental.CentralStorageStrategy(\
        compute_devices=['CPU:0', 'GPU:0'], parameter_device='CPU:0')\
    ds = tf.data.Dataset.range(10)\
    # Distribute that dataset\
    dist_dataset = strategy.experimental_distribute_dataset(ds)\
    \
    with strategy.scope():\
      @tf.function\
      def train_step(val):\
        # pass through\
        return val\
    \
      # Iterate over the distributed dataset\
      for x in dist_dataset:\
        result = strategy.run(train_step, args=(x,))\
    \
    result = strategy.reduce(tf.distribute.ReduceOp.SUM, result,\
                             axis=None).numpy()\
    # result: array([ 4,  6,  8, 10])\
    \
    result = strategy.reduce(tf.distribute.ReduceOp.SUM, result, axis=0).numpy()\
    # result: 28\
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
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/central_storage_strategy.py#L127-L143)\
\
run(\
        fn, args=(), kwargs=None, options=None\
    )\
\
Run `fn` on each replica, with the given arguments.\
\
In `CentralStorageStrategy`, `fn` is called on each of the compute replicas, with the provided "per replica" arguments specific to that device.\
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
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1223-L1315)\
\
scope()\
\
Context manager to make the strategy current and distribute variables.\
\
This method returns a context manager, and is used as follows:\
\
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])\
\
_What happens when Strategy.scope is entered?_\
\
*   `strategy` is installed in the global context as the "current" strategy. Inside this scope, [`tf.distribute.get_strategy()`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy)\
     will now return this strategy. Outside this scope, it returns the default no-op strategy.\
*   Entering the scope also enters the "cross-replica context". See [`tf.distribute.StrategyExtended`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended)\
     for an explanation on cross-replica and replica contexts.\
*   Variable creation inside `scope` is intercepted by the strategy. Each strategy defines how it wants to affect the variable creation. Sync strategies like `MirroredStrategy`, `TPUStrategy` and `MultiWorkerMiroredStrategy` create variables replicated on each replica, whereas `ParameterServerStrategy` creates variables on the parameter servers. This is done using a custom [`tf.variable_creator_scope`](https://www.tensorflow.org/api_docs/python/tf/variable_creator_scope)\
    .\
*   In some strategies, a default device scope may also be entered: in `MultiWorkerMiroredStrategy`, a default device scope of "/CPU:0" is entered on each worker.\
\
_What should be in scope and what should be outside?_\
\
There are a number of requirements on what needs to happen inside the scope. However, in places where we have information about which strategy is in use, we often enter the scope for the user, so they don't have to do it explicitly (i.e. calling those either inside or outside the scope is OK).\
\
*   Anything that creates variables that should be distributed variables must be called in a `strategy.scope`. This can be accomplished either by directly calling the variable creating function within the scope context, or by relying on another API like `strategy.run` or [`keras.Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)\
     to automatically enter it for you. Any variable that is created outside scope will not be distributed and may have performance implications. Some common objects that create variables in TF are Models, Optimizers, Metrics. Such objects should always be initialized in the scope, and any functions that may lazily create variables (e.g., [`Model.**call**()`](https://ai.google.dev/api/python/google/generativeai/protos/Model#__call__)\
    , tracing a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)\
    , etc.) should similarly be called within scope. Another source of variable creation can be a checkpoint restore - when variables are created lazily. Note that any variable created inside a strategy captures the strategy information. So reading and writing to these variables outside the `strategy.scope` can also work seamlessly, without the user having to enter the scope.\
*   Some strategy APIs (such as `strategy.run` and `strategy.reduce`) which require to be in a strategy's scope, enter the scope automatically, which means when using those APIs you don't need to explicitly enter the scope yourself.\
*   When a [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)\
     is created inside a `strategy.scope`, the Model object captures the scope information. When high level training framework methods such as `model.compile`, `model.fit`, etc. are then called, the captured scope will be automatically entered, and the associated strategy will be used to distribute the training etc. See a detailed example in [distributed keras tutorial](https://www.tensorflow.org/tutorials/distribute/keras)\
    . WARNING: Simply calling `model(..)` does not automatically enter the captured scope -- only high level training framework APIs support this behavior: `model.compile`, `model.fit`, `model.evaluate`, `model.predict` and `model.save` can all be called inside or outside the scope.\
*   The following can be either inside or outside the scope:\
    *   Creating the input datasets\
    *   Defining [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)\
        s that represent your training step\
    *   Saving APIs such as [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)\
        . Loading creates variables, so that should go inside the scope if you want to train the model in a distributed way.\
    *   Checkpoint saving. As mentioned above - `checkpoint.restore` may sometimes need to be inside scope if it creates variables.\
\
|     |\
| --- |\
| Returns |     |\
| A context manager. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.