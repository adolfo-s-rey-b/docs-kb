[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#distribute_datasets_from_function)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#experimental_distribute_dataset)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#experimental_local_results)
        
    *   [experimental\_make\_numpy\_dataset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#experimental_make_numpy_dataset)
        
    *   [experimental\_run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#experimental_run)
        
    *   [make\_dataset\_iterator](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#make_dataset_iterator)
        
    *   [make\_input\_fn\_iterator](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#make_input_fn_iterator)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#scope)
        
    *   [update\_config\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#update_config_proto)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.distribute.MirroredStrategy Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#distribute_datasets_from_function)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#experimental_distribute_dataset)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#experimental_local_results)
        
    *   [experimental\_make\_numpy\_dataset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#experimental_make_numpy_dataset)
        
    *   [experimental\_run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#experimental_run)
        
    *   [make\_dataset\_iterator](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#make_dataset_iterator)
        
    *   [make\_input\_fn\_iterator](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#make_input_fn_iterator)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#scope)
        
    *   [update\_config\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/MirroredStrategy#update_config_proto)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/mirrored_strategy.py#L293-L306)

Synchronous training across multiple replicas on one machine.

Inherits From: [`Strategy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/Strategy)

tf.compat.v1.distribute.MirroredStrategy(
        devices=None, cross_device_ops=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate single-worker multiple-GPU training](https://www.tensorflow.org/guide/migrate/mirrored_strategy) |

This strategy is typically used for training on one machine with multiple GPUs. For TPUs, use [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
. To use `MirroredStrategy` with multiple workers, please refer to [`tf.distribute.experimental.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/MultiWorkerMirroredStrategy)
.

For example, a variable created under a `MirroredStrategy` is a `MirroredVariable`. If no devices are specified in the constructor argument of the strategy then it will use all the available GPUs. If no GPUs are found, it will use the available CPUs. Note that TensorFlow treats all CPUs on a machine as a single device, and uses threads internally for parallelism.

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

While using distribution strategies, all the variable creation should be done within the strategy's scope. This will replicate the variables across all the replicas and keep them in sync using an all-reduce algorithm.

Variables created inside a `MirroredStrategy` which is wrapped with a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 are still `MirroredVariables`.

    x = []

`experimental_distribute_dataset` can be used to distribute the dataset across the replicas when writing your own training loop. If you are using `.fit` and `.compile` methods available in [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
, then [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
 will handle the distribution for you.

#### For example:

my_strategy = tf.distribute.MirroredStrategy()
    with my_strategy.scope():
      @tf.function
      def distribute_train_epoch(dataset):
        def replica_fn(input):
          # process input and return result
          return result
    
        total_result = 0
        for x in dataset:
          per_replica_result = my_strategy.run(replica_fn, args=(x,))
          total_result += my_strategy.reduce(tf.distribute.ReduceOp.SUM,
                                             per_replica_result, axis=None)
        return total_result
    
      dist_dataset = my_strategy.experimental_distribute_dataset(dataset)
      for _ in range(EPOCHS):
        train_result = distribute_train_epoch(dist_dataset)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `devices` | a list of device strings such as `['/gpu:0', '/gpu:1']`. If `None`, all available GPUs are used. If no GPUs are found, CPU is used. |
| `cross_device_ops` | optional, a descendant of `CrossDeviceOps`. If this is not set, `NcclAllReduce()` will be used by default. One would customize this if NCCL isn't available or if a special implementation that exploits the particular hardware is available. |

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1349-L1468)

experimental_distribute_dataset(
        dataset, options=None
    )

Creates [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 from [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

The returned [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 can be iterated over similar to regular datasets. NOTE: The user cannot add any more transformations to a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
. You can only create an iterator or examine the [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)
 of the data generated by it. See API docs of [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 to learn more.

The following is an example:

    global_batch_size = 2

Three key actions happening under the hood of this method are batching, sharding, and prefetching.

In the code snippet above, `dataset` is batched by `global_batch_size`, and calling `experimental_distribute_dataset` on it rebatches `dataset` to a new batch size that is equal to the global batch size divided by the number of replicas in sync. We iterate through it using a Pythonic for loop. `x` is a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 containing data for all replicas, and each replica gets data of the new batch size. [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run)
 will take care of feeding the right per-replica data in `x` to the right `replica_fn` executed on each replica.

Sharding contains autosharding across multiple workers and within every worker. First, in multi-worker distributed training (i.e. when you use [`tf.distribute.experimental.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/MultiWorkerMirroredStrategy)
 or [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
), autosharding a dataset over a set of workers means that each worker is assigned a subset of the entire dataset (if the right [`tf.data.experimental.AutoShardPolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy)
 is set). This is to ensure that at each step, a global batch size of non-overlapping dataset elements will be processed by each worker. Autosharding has a couple of different options that can be specified using [`tf.data.experimental.DistributeOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions)
. Then, sharding within each worker means the method will split the data among all the worker devices (if more than one a present). This will happen regardless of multi-worker autosharding.

By default, this method adds a prefetch transformation at the end of the user provided [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instance. The argument to the prefetch transformation which is `buffer_size` is equal to the number of replicas in sync.

If the above batch splitting and dataset sharding logic is undesirable, please use [`tf.distribute.Strategy.distribute_datasets_from_function`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#distribute_datasets_from_function)
 instead, which does not do any automatic batching or sharding for you.

For a tutorial on more usage and properties of this method, refer to the [tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_dataset)
. If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches)
.

|     |     |
| --- | --- |
| Args |     |
| `dataset` | [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> that will be sharded across all replicas using the rules stated above. |
| `options` | [`tf.distribute.InputOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions)<br> used to control options on how this dataset is distributed. |

|     |
| --- |
| Returns |     |
| A [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)<br>. |     |

### `experimental_local_results`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1894-L1912)

experimental_local_results(
        value
    )

Returns the list of all local per-replica values contained in `value`.

|     |     |
| --- | --- |
| Args |     |
| `value` | A value returned by `experimental_run()`, `run(), or a variable created in`scope\`. |

|     |
| --- |
| Returns |     |
| A tuple of values contained in `value` where ith element corresponds to ith replica. If `value` represents a single value, this returns `(value,).` |     |

### `experimental_make_numpy_dataset`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2298-L2327)

experimental_make_numpy_dataset(
        numpy_input, session=None
    )

Makes a tf.data.Dataset for input provided via a numpy array.

This avoids adding `numpy_input` as a large constant in the graph, and copies the data to the machine or machines that will be processing the input.

Note that you will likely need to use tf.distribute.Strategy.experimental\_distribute\_dataset with the returned dataset to further distribute it with the strategy.

#### Example:

numpy_input = np.ones([10], dtype=np.float32)
    dataset = strategy.experimental_make_numpy_dataset(numpy_input)
    dist_dataset = strategy.experimental_distribute_dataset(dataset)

|     |     |
| --- | --- |
| Args |     |
| `numpy_input` | A nest of NumPy input arrays that will be converted into a dataset. Note that lists of Numpy arrays are stacked, as that is normal [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> behavior. |
| `session` | (TensorFlow v1.x graph execution only) A session used for initialization. |

|     |
| --- |
| Returns |     |
| A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> representing `numpy_input`. |     |

### `experimental_run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2329-L2366)

experimental_run(
        fn, input_iterator=None
    )

Runs ops in `fn` on each replica, with inputs from `input_iterator`. (deprecated)

When eager execution is enabled, executes ops specified by `fn` on each replica. Otherwise, builds a graph to execute the ops on each replica.

Each replica will take a single, different input from the inputs provided by one `get_next` call on the input iterator.

`fn` may call [`tf.distribute.get_replica_context()`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context)
 to access members such as `replica_id_in_sync_group`.

|     |     |
| --- | --- |
| Args |     |
| `fn` | The function to run. The inputs to the function must match the outputs of `input_iterator.get_next()`. The output must be a [`tf.nest`](https://www.tensorflow.org/api_docs/python/tf/nest)<br> of `Tensor`s. |
| `input_iterator` | (Optional) input iterator from which the inputs are taken. |

|     |
| --- |
| Returns |     |
| Merged return value of `fn` across replicas. The structure of the return value is the same as the return value from `fn`. Each element in the structure can either be `PerReplica` (if the values are unsynchronized), `Mirrored` (if the values are kept in sync), or `Tensor` (if running on a single replica). |     |

### `make_dataset_iterator`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2230-L2254)

make_dataset_iterator(
        dataset
    )

Makes an iterator for input provided via `dataset`.

Data from the given dataset will be distributed evenly across all the compute replicas. We will assume that the input dataset is batched by the global batch size. With this assumption, we will make a best effort to divide each batch across all the replicas (one or more workers). If this effort fails, an error will be thrown, and the user should instead use `make_input_fn_iterator` which provides more control to the user, and does not try to divide a batch across replicas.

The user could also use `make_input_fn_iterator` if they want to customize which input is fed to which replica/worker etc.

|     |     |
| --- | --- |
| Args |     |
| `dataset` | [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> that will be distributed evenly across all replicas. |

|     |
| --- |
| Returns |     |
| An `tf.distribute.InputIterator` which returns inputs for each step of the computation. User should call `initialize` on the returned iterator. |     |

### `make_input_fn_iterator`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2256-L2296)

make_input_fn_iterator(
        input_fn,
        replication_mode=tf.distribute.InputReplicationMode.PER_WORKER
    )

Returns an iterator split across replicas created from an input function.

The `input_fn` should take an [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)
 object where information about batching and input sharding can be accessed:

def input_fn(input_context):
      batch_size = input_context.get_per_replica_batch_size(global_batch_size)
      d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
      return d.shard(input_context.num_input_pipelines,
                     input_context.input_pipeline_id)
    with strategy.scope():
      iterator = strategy.make_input_fn_iterator(input_fn)
      replica_results = strategy.experimental_run(replica_fn, iterator)

The [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 returned by `input_fn` should have a per-replica batch size, which may be computed using `input_context.get_per_replica_batch_size`.

|     |     |
| --- | --- |
| Args |     |
| `input_fn` | A function taking a [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)<br> object and returning a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>. |
| `replication_mode` | an enum value of [`tf.distribute.InputReplicationMode`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputReplicationMode)<br>. Only `PER_WORKER` is supported currently, which means there will be a single call to `input_fn` per worker. Replicas will dequeue from the local [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> on their worker. |

|     |
| --- |
| Returns |     |
| An iterator object that should first be `.initialize()`\-ed. It may then either be passed to `strategy.experimental_run()` or you can `iterator.get_next()` to get the next value to pass to `strategy.extended.call_for_each_replica()`. |     |

### `reduce`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2368-L2369)

reduce(
        reduce_op, value, axis=None
    )

Reduce `value` across replicas and return result on current device.

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

To see how this would look with multiple replicas, consider the same example with MirroredStrategy with 2 GPUs:

strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
    def step_fn():
      i = tf.distribute.get_replica_context().replica_id_in_sync_group
      return tf.identity(i)
    
    per_replica_result = strategy.run(step_fn)
    # Check devices on which per replica result is:
    strategy.experimental_local_results(per_replica_result)[0].device
    # /job:localhost/replica:0/task:0/device:GPU:0
    strategy.experimental_local_results(per_replica_result)[1].device
    # /job:localhost/replica:0/task:0/device:GPU:1
    
    total = strategy.reduce("SUM", per_replica_result, axis=None)
    # Check device on which reduced result is:
    total.device
    # /job:localhost/replica:0/task:0/device:CPU:0

This API is typically used for aggregating the results returned from different replicas, for reporting etc. For example, loss computed from different replicas can be averaged using this API before printing.

There are a number of different tf.distribute APIs for reducing values across replicas:

*   [`tf.distribute.ReplicaContext.all_reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_reduce)
    : This differs from [`Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#reduce)
     in that it is for replica context and does not copy the results to the host device. `all_reduce` should be typically used for reductions inside the training step such as gradients.
*   [`tf.distribute.StrategyExtended.reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#reduce_to)
     and [`tf.distribute.StrategyExtended.batch_reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#batch_reduce_to)
    : These APIs are more advanced versions of [`Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#reduce)
     as they allow customizing the destination of the result. They are also called in cross replica context.

_What should axis be?_

Given a per-replica value returned by `run`, say a per-example loss, the batch will be divided across all the replicas. This function allows you to aggregate across replicas and optionally also across batch elements by specifying the axis parameter accordingly.

For example, if you have a global batch size of 8 and 2 replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and `[4, 5, 6, 7]` will be on replica 1. With `axis=None`, `reduce` will aggregate only across replicas, returning `[0+4, 1+5, 2+6, 3+7]`. This is useful when each replica is computing a scalar or some other value that doesn't have a "batch" dimension (like a gradient or loss).

strategy.reduce("sum", per_replica_result, axis=None)

Sometimes, you will want to aggregate across both the global batch _and_ all replicas. You can get this behavior by specifying the batch dimension as the `axis`, typically `axis=0`. In this case it would return a scalar `0+1+2+3+4+5+6+7`.

strategy.reduce("sum", per_replica_result, axis=0)

If there is a last partial batch, you will need to specify an axis so that the resulting shape is consistent across replicas. So if the last batch has size 6 and it is divided into \[0, 1, 2, 3\] and \[4, 5\], you would get a shape mismatch unless you specify `axis=0`. If you specify [`tf.distribute.ReduceOp.MEAN`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp#MEAN)
, using `axis=0` will use the correct denominator of 6. Contrast this with computing `reduce_mean` to get a scalar value on each replica and this function to average those means, which will weigh some values `1/8` and others `1/4`.

|     |     |
| --- | --- |
| Args |     |
| `reduce_op` | a [`tf.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)<br> value specifying how values should be combined. Allows using string representation of the enum such as "SUM", "MEAN". |
| `value` | a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> instance, e.g. returned by [`Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run)<br>, to be combined into a single tensor. It can also be a regular tensor when used with `OneDeviceStrategy` or default strategy. |
| `axis` | specifies the dimension to reduce along within each replica's tensor. Should typically be set to the batch dimension, or `None` to only reduce across replicas (e.g. if the tensor has no batch dimension). |

|     |
| --- |
| Returns |     |
| A `Tensor`. |     |

### `run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1557-L1673)

run(
        fn, args=(), kwargs=None, options=None
    )

Invokes `fn` on each replica, with the given arguments.

This method is the primary way to distribute your computation with a tf.distribute object. It invokes `fn` on each replica. If `args` or `kwargs` have [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
, such as those produced by a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
 from [`tf.distribute.Strategy.experimental_distribute_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_dataset)
 or [`tf.distribute.Strategy.distribute_datasets_from_function`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#distribute_datasets_from_function)
, when `fn` is executed on a particular replica, it will be executed with the component of [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 that correspond to that replica.

`fn` is invoked under a replica context. `fn` may call [`tf.distribute.get_replica_context()`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context)
 to access members such as `all_reduce`. Please see the module-level docstring of tf.distribute for the concept of replica context.

All arguments in `args` or `kwargs` can be a nested structure of tensors, e.g. a list of tensors, in which case `args` and `kwargs` will be passed to the `fn` invoked on each replica. Or `args` or `kwargs` can be [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 containing tensors or composite tensors, i.e. [`tf.compat.v1.TensorInfo.CompositeTensor`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/TensorInfo/CompositeTensor)
, in which case each `fn` call will get the component of a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 corresponding to its replica. Note that arbitrary Python values that are not of the types above are not supported.

#### Example usage:

1.  Constant tensor input.
    
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        
2.  DistributedValues input.
    
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        
3.  Use [`tf.distribute.ReplicaContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext)
     to allreduce values.
    
    strategy = tf.distribute.MirroredStrategy(["gpu:0", "gpu:1"])
        

|     |     |
| --- | --- |
| Args |     |
| `fn` | The function to run on each replica. |
| `args` | Optional positional arguments to `fn`. Its element can be a tensor, a nested structure of tensors or a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>. |
| `kwargs` | Optional keyword arguments to `fn`. Its element can be a tensor, a nested structure of tensors or a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>. |
| `options` | An optional instance of [`tf.distribute.RunOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/RunOptions)<br> specifying the options to run `fn`. |

|     |
| --- |
| Returns |     |
| Merged return value of `fn` across replicas. The structure of the return value is the same as the return value from `fn`. Each element in the structure can either be [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>, `Tensor` objects, or `Tensor`s (for example, if running on a single replica). |     |

### `scope`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1223-L1315)

scope()

Context manager to make the strategy current and distribute variables.

This method returns a context manager, and is used as follows:

    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])

_What happens when Strategy.scope is entered?_

*   `strategy` is installed in the global context as the "current" strategy. Inside this scope, [`tf.distribute.get_strategy()`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy)
     will now return this strategy. Outside this scope, it returns the default no-op strategy.
*   Entering the scope also enters the "cross-replica context". See [`tf.distribute.StrategyExtended`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended)
     for an explanation on cross-replica and replica contexts.
*   Variable creation inside `scope` is intercepted by the strategy. Each strategy defines how it wants to affect the variable creation. Sync strategies like `MirroredStrategy`, `TPUStrategy` and `MultiWorkerMiroredStrategy` create variables replicated on each replica, whereas `ParameterServerStrategy` creates variables on the parameter servers. This is done using a custom [`tf.variable_creator_scope`](https://www.tensorflow.org/api_docs/python/tf/variable_creator_scope)
    .
*   In some strategies, a default device scope may also be entered: in `MultiWorkerMiroredStrategy`, a default device scope of "/CPU:0" is entered on each worker.

_What should be in scope and what should be outside?_

There are a number of requirements on what needs to happen inside the scope. However, in places where we have information about which strategy is in use, we often enter the scope for the user, so they don't have to do it explicitly (i.e. calling those either inside or outside the scope is OK).

*   Anything that creates variables that should be distributed variables must be called in a `strategy.scope`. This can be accomplished either by directly calling the variable creating function within the scope context, or by relying on another API like `strategy.run` or [`keras.Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
     to automatically enter it for you. Any variable that is created outside scope will not be distributed and may have performance implications. Some common objects that create variables in TF are Models, Optimizers, Metrics. Such objects should always be initialized in the scope, and any functions that may lazily create variables (e.g., [`Model.**call**()`](https://ai.google.dev/api/python/google/generativeai/protos/Model#__call__)
    , tracing a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    , etc.) should similarly be called within scope. Another source of variable creation can be a checkpoint restore - when variables are created lazily. Note that any variable created inside a strategy captures the strategy information. So reading and writing to these variables outside the `strategy.scope` can also work seamlessly, without the user having to enter the scope.
*   Some strategy APIs (such as `strategy.run` and `strategy.reduce`) which require to be in a strategy's scope, enter the scope automatically, which means when using those APIs you don't need to explicitly enter the scope yourself.
*   When a [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
     is created inside a `strategy.scope`, the Model object captures the scope information. When high level training framework methods such as `model.compile`, `model.fit`, etc. are then called, the captured scope will be automatically entered, and the associated strategy will be used to distribute the training etc. See a detailed example in [distributed keras tutorial](https://www.tensorflow.org/tutorials/distribute/keras)
    . WARNING: Simply calling `model(..)` does not automatically enter the captured scope -- only high level training framework APIs support this behavior: `model.compile`, `model.fit`, `model.evaluate`, `model.predict` and `model.save` can all be called inside or outside the scope.
*   The following can be either inside or outside the scope:
    *   Creating the input datasets
    *   Defining [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
        s that represent your training step
    *   Saving APIs such as [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
        . Loading creates variables, so that should go inside the scope if you want to train the model in a distributed way.
    *   Checkpoint saving. As mentioned above - `checkpoint.restore` may sometimes need to be inside scope if it creates variables.

|     |
| --- |
| Returns |     |
| A context manager. |     |

### `update_config_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2373-L2388)

update_config_proto(
        config_proto
    )

Returns a copy of `config_proto` modified for use with this strategy.

The updated config has something needed to run a strategy, e.g. configuration to run collective ops, or device filters to improve distributed training performance.

|     |     |
| --- | --- |
| Args |     |
| `config_proto` | a `tf.ConfigProto` object. |

|     |
| --- |
| Returns |     |
| The updated copy of the `config_proto`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.