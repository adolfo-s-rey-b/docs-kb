[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#distribute_datasets_from_function)
        
    *   [experimental\_assign\_to\_logical\_device](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_assign_to_logical_device)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_distribute_dataset)
        
    *   [experimental\_distribute\_values\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_distribute_values_from_function)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_local_results)
        
    *   [experimental\_replicate\_to\_logical\_devices](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_replicate_to_logical_devices)
        
    *   [experimental\_split\_to\_logical\_devices](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_split_to_logical_devices)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#gather)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.TPUStrategy Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#distribute_datasets_from_function)
        
    *   [experimental\_assign\_to\_logical\_device](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_assign_to_logical_device)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_distribute_dataset)
        
    *   [experimental\_distribute\_values\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_distribute_values_from_function)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_local_results)
        
    *   [experimental\_replicate\_to\_logical\_devices](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_replicate_to_logical_devices)
        
    *   [experimental\_split\_to\_logical\_devices](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_split_to_logical_devices)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#gather)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/tpu_strategy.py#L242-L663)

Synchronous training on TPUs and TPU Pods.

Inherits From: [`Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)

tf.distribute.TPUStrategy(
        tpu_cluster_resolver=None,
        experimental_device_assignment=None,
        experimental_spmd_xla_partitioning=False
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding)<br>    <br>*   [Migrate from TPUEstimator to TPUStrategy](https://www.tensorflow.org/guide/migrate/tpu_estimator)<br>    <br>*   [Use TPUs](https://www.tensorflow.org/guide/tpu) | *   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index)<br>    <br>*   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer)<br>    <br>*   [Solve GLUE tasks using BERT on TPU](https://www.tensorflow.org/text/tutorials/bert_glue) |

To construct a TPUStrategy object, you need to run the initialization code as below:

    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')

While using distribution strategies, the variables created within the strategy's scope will be replicated across all the replicas and can be kept in sync using all-reduce algorithms.

To run TF2 programs on TPUs, you can either use `.compile` and `.fit` APIs in [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
 with TPUStrategy, or write your own customized training loop by calling `strategy.run` directly. Note that TPUStrategy doesn't support pure eager execution, so please make sure the function passed into `strategy.run` is a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 or `strategy.run` is called inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 if eager behavior is enabled. See more details in https://www.tensorflow.org/guide/tpu.

`distribute_datasets_from_function` and `experimental_distribute_dataset` APIs can be used to distribute the dataset across the TPU workers when writing your own training loop. If you are using `fit` and `compile` methods available in [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
, then Keras will handle the distribution for you.

An example of writing customized training loop on TPUs:

    with strategy.scope():

    def dataset_fn(ctx):

    @tf.function()

    train_step(iterator)

For the advanced use cases like model parallelism, you can set `experimental_device_assignment` argument when creating TPUStrategy to specify number of replicas and number of logical devices. Below is an example to initialize TPU system with 2 logical devices and 1 replica.

    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')

Then you can run a [`tf.add`](https://www.tensorflow.org/api_docs/python/tf/math/add)
 operation only on logical device 0.

    @tf.function()

`experimental_spmd_xla_partitioning` enables the experimental XLA SPMD feature for model parallelism. This flag can reduce the compilation time and HBM requirements. When running in this mode, every input tensor must either be partitioned (via `strategy.experimental_split_to_logical_devices`) or fully replicated (via `strategy.experimental_replicate_to_logical_devices`) to all logical devices. And calling `strategy.experimental_assign_to_logical_device` will result in a ValueError in this mode.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tpu_cluster_resolver` | A [`tf.distribute.cluster_resolver.TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)<br> instance, which provides information about the TPU cluster. If None, it will assume running on a local TPU worker. |
| `experimental_device_assignment` | Optional [`tf.tpu.experimental.DeviceAssignment`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/DeviceAssignment)<br> to specify the placement of replicas on the TPU cluster. |
| `experimental_spmd_xla_partitioning` | If True, enable the SPMD (Single Program Multiple Data) mode in XLA compiler. This flag only affects the performance of XLA compilation and the HBM requirement of the compiled TPU program. Ceveat: if this flag is True, calling [`tf.distribute.TPUStrategy.experimental_assign_to_logical_device`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy#experimental_assign_to_logical_device)<br> will result in a ValueError. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `cluster_resolver` | Returns the cluster resolver associated with this strategy.<br><br>[`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)<br> provides the associated [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br>. If the user provides one in `__init__`, that instance is returned; if the user does not, a default [`tf.distribute.cluster_resolver.TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)<br> is provided. |
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

### `experimental_assign_to_logical_device`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/tpu_strategy.py#L453-L514)

experimental_assign_to_logical_device(
        tensor, logical_device_id
    )

Adds annotation that `tensor` will be assigned to a logical device.

This adds an annotation to `tensor` specifying that operations on `tensor` will be invoked on logical core device id `logical_device_id`. When model parallelism is used, the default behavior is that all ops are placed on zero-th logical device.

# Initializing TPU system with 2 logical devices and 4 replicas.
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    topology = tf.tpu.experimental.initialize_tpu_system(resolver)
    device_assignment = tf.tpu.experimental.DeviceAssignment.build(
        topology,
        computation_shape=[1, 1, 1, 2],
        num_replicas=4)
    strategy = tf.distribute.TPUStrategy(
        resolver, experimental_device_assignment=device_assignment)
    iterator = iter(inputs)
    
    @tf.function()
    def step_fn(inputs):
      output = tf.add(inputs, inputs)
    
      # Add operation will be executed on logical device 0.
      output = strategy.experimental_assign_to_logical_device(output, 0)
      return output
    
    strategy.run(step_fn, args=(next(iterator),))

|     |     |
| --- | --- |
| Args |     |
| `tensor` | Input tensor to annotate. |
| `logical_device_id` | Id of the logical core to which the tensor will be assigned. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | The logical device id presented is not consistent with total number of partitions specified by the device assignment or the TPUStrategy is constructed with `experimental_spmd_xla_partitioning=True`. |

|     |
| --- |
| Returns |     |
| Annotated tensor with identical value as `tensor`. |     |

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

### `experimental_replicate_to_logical_devices`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/tpu_strategy.py#L617-L663)

experimental_replicate_to_logical_devices(
        tensor
    )

Adds annotation that `tensor` will be replicated to all logical devices.

This adds an annotation to tensor `tensor` specifying that operations on `tensor` will be invoked on all logical devices.

# Initializing TPU system with 2 logical devices and 4 replicas.
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    topology = tf.tpu.experimental.initialize_tpu_system(resolver)
    device_assignment = tf.tpu.experimental.DeviceAssignment.build(
        topology,
        computation_shape=[1, 1, 1, 2],
        num_replicas=4)
    strategy = tf.distribute.TPUStrategy(
        resolver, experimental_device_assignment=device_assignment)
    
    iterator = iter(inputs)
    
    @tf.function()
    def step_fn(inputs):
      images, labels = inputs
      images = strategy.experimental_split_to_logical_devices(
        inputs, [1, 2, 4, 1])
    
      # model() function will be executed on 8 logical devices with `inputs`
      # split 2 * 4  ways.
      output = model(inputs)
    
      # For loss calculation, all logical devices share the same logits
      # and labels.
      labels = strategy.experimental_replicate_to_logical_devices(labels)
      output = strategy.experimental_replicate_to_logical_devices(output)
      loss = loss_fn(labels, output)
    
      return loss
    
    strategy.run(step_fn, args=(next(iterator),))

Args: tensor: Input tensor to annotate.

|     |
| --- |
| Returns |     |
| Annotated tensor with identical value as `tensor`. |     |

### `experimental_split_to_logical_devices`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/tpu_strategy.py#L516-L615)

experimental_split_to_logical_devices(
        tensor, partition_dimensions
    )

Adds annotation that `tensor` will be split across logical devices.

This adds an annotation to tensor `tensor` specifying that operations on `tensor` will be split among multiple logical devices. Tensor `tensor` will be split across dimensions specified by `partition_dimensions`. The dimensions of `tensor` must be divisible by corresponding value in `partition_dimensions`.

For example, for system with 8 logical devices, if `tensor` is an image tensor with shape (batch\_size, width, height, channel) and `partition_dimensions` is \[1, 2, 4, 1\], then `tensor` will be split 2 in width dimension and 4 way in height dimension and the split tensor values will be fed into 8 logical devices.

# Initializing TPU system with 8 logical devices and 1 replica.
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    topology = tf.tpu.experimental.initialize_tpu_system(resolver)
    device_assignment = tf.tpu.experimental.DeviceAssignment.build(
        topology,
        computation_shape=[1, 2, 2, 2],
        num_replicas=1)
    # Construct the TPUStrategy. Since we are going to split the image across
    # logical devices, here we set `experimental_spmd_xla_partitioning=True`
    # so that the partitioning can be compiled in SPMD mode, which usually
    # results in faster compilation and smaller HBM requirement if the size of
    # input and activation tensors are much bigger than that of the model
    # parameters. Note that this flag is suggested but not a hard requirement
    # for `experimental_split_to_logical_devices`.
    strategy = tf.distribute.TPUStrategy(
        resolver, experimental_device_assignment=device_assignment,
        experimental_spmd_xla_partitioning=True)
    
    iterator = iter(inputs)
    
    @tf.function()
    def step_fn(inputs):
      inputs = strategy.experimental_split_to_logical_devices(
        inputs, [1, 2, 4, 1])
    
      # model() function will be executed on 8 logical devices with `inputs`
      # split 2 * 4  ways.
      output = model(inputs)
      return output
    
    strategy.run(step_fn, args=(next(iterator),))

Args: tensor: Input tensor to annotate. partition\_dimensions: An unnested list of integers with the size equal to rank of `tensor` specifying how `tensor` will be partitioned. The product of all elements in `partition_dimensions` must be equal to the total number of logical devices per replica.

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | 1) If the size of partition\_dimensions does not equal to rank of `tensor` or 2) if product of elements of `partition_dimensions` does not match the number of logical devices per replica defined by the implementing DistributionStrategy's device specification or 3) if a known size of `tensor` is not divisible by corresponding value in `partition_dimensions`. |

|     |
| --- |
| Returns |     |
| Annotated tensor with identical value as `tensor`. |     |

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
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1675-L1869)\
\
reduce(\
        reduce_op, value, axis\
    )\
\
Reduce `value` across replicas and return result on current device.\
\
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])\
\
To see how this would look with multiple replicas, consider the same example with MirroredStrategy with 2 GPUs:\
\
strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])\
    def step_fn():\
      i = tf.distribute.get_replica_context().replica_id_in_sync_group\
      return tf.identity(i)\
    \
    per_replica_result = strategy.run(step_fn)\
    # Check devices on which per replica result is:\
    strategy.experimental_local_results(per_replica_result)[0].device\
    # /job:localhost/replica:0/task:0/device:GPU:0\
    strategy.experimental_local_results(per_replica_result)[1].device\
    # /job:localhost/replica:0/task:0/device:GPU:1\
    \
    total = strategy.reduce("SUM", per_replica_result, axis=None)\
    # Check device on which reduced result is:\
    total.device\
    # /job:localhost/replica:0/task:0/device:CPU:0\
\
This API is typically used for aggregating the results returned from different replicas, for reporting etc. For example, loss computed from different replicas can be averaged using this API before printing.\
\
There are a number of different tf.distribute APIs for reducing values across replicas:\
\
*   [`tf.distribute.ReplicaContext.all_reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_reduce)\
    : This differs from [`Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#reduce)\
     in that it is for replica context and does not copy the results to the host device. `all_reduce` should be typically used for reductions inside the training step such as gradients.\
*   [`tf.distribute.StrategyExtended.reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#reduce_to)\
     and [`tf.distribute.StrategyExtended.batch_reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#batch_reduce_to)\
    : These APIs are more advanced versions of [`Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#reduce)\
     as they allow customizing the destination of the result. They are also called in cross replica context.\
\
_What should axis be?_\
\
Given a per-replica value returned by `run`, say a per-example loss, the batch will be divided across all the replicas. This function allows you to aggregate across replicas and optionally also across batch elements by specifying the axis parameter accordingly.\
\
For example, if you have a global batch size of 8 and 2 replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and `[4, 5, 6, 7]` will be on replica 1. With `axis=None`, `reduce` will aggregate only across replicas, returning `[0+4, 1+5, 2+6, 3+7]`. This is useful when each replica is computing a scalar or some other value that doesn't have a "batch" dimension (like a gradient or loss).\
\
strategy.reduce("sum", per_replica_result, axis=None)\
\
Sometimes, you will want to aggregate across both the global batch _and_ all replicas. You can get this behavior by specifying the batch dimension as the `axis`, typically `axis=0`. In this case it would return a scalar `0+1+2+3+4+5+6+7`.\
\
strategy.reduce("sum", per_replica_result, axis=0)\
\
If there is a last partial batch, you will need to specify an axis so that the resulting shape is consistent across replicas. So if the last batch has size 6 and it is divided into \[0, 1, 2, 3\] and \[4, 5\], you would get a shape mismatch unless you specify `axis=0`. If you specify [`tf.distribute.ReduceOp.MEAN`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp#MEAN)\
, using `axis=0` will use the correct denominator of 6. Contrast this with computing `reduce_mean` to get a scalar value on each replica and this function to average those means, which will weigh some values `1/8` and others `1/4`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `reduce_op` | a [`tf.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)<br> value specifying how values should be combined. Allows using string representation of the enum such as "SUM", "MEAN". |\
| `value` | a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br> instance, e.g. returned by [`Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run)<br>, to be combined into a single tensor. It can also be a regular tensor when used with `OneDeviceStrategy` or default strategy. |\
| `axis` | specifies the dimension to reduce along within each replica's tensor. Should typically be set to the batch dimension, or `None` to only reduce across replicas (e.g. if the tensor has no batch dimension). |\
\
|     |\
| --- |\
| Returns |     |\
| A `Tensor`. |     |\
\
### `run`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/tpu_strategy.py#L384-L440)\
\
run(\
        fn, args=(), kwargs=None, options=None\
    )\
\
Run the computation defined by `fn` on each TPU replica.\
\
Executes ops specified by `fn` on each replica. If `args` or `kwargs` have [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)\
, such as those produced by a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)\
 from [`tf.distribute.Strategy.experimental_distribute_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_dataset)\
 or [`tf.distribute.Strategy.distribute_datasets_from_function`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#distribute_datasets_from_function)\
, when `fn` is executed on a particular replica, it will be executed with the component of [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)\
 that correspond to that replica.\
\
`fn` may call [`tf.distribute.get_replica_context()`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context)\
 to access members such as `all_reduce`.\
\
All arguments in `args` or `kwargs` should either be nest of tensors or [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)\
 containing tensors or composite tensors.\
\
#### Example usage:\
\
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')\
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
| Merged return value of `fn` across replicas. The structure of the return value is the same as the return value from `fn`. Each element in the structure can either be [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>, `Tensor` objects, or `Tensor`s (for example, if running on a single replica). |     |\
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