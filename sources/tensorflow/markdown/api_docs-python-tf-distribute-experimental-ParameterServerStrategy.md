[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fexperimental%2FParameterServerStrategy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#distribute_datasets_from_function)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#experimental_distribute_dataset)
        
    *   [experimental\_distribute\_values\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#experimental_distribute_values_from_function)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#experimental_local_results)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#gather)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.ParameterServerStrategy Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#methods)
    *   [distribute\_datasets\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#distribute_datasets_from_function)
        
    *   [experimental\_distribute\_dataset](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#experimental_distribute_dataset)
        
    *   [experimental\_distribute\_values\_from\_function](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#experimental_distribute_values_from_function)
        
    *   [experimental\_local\_results](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#experimental_local_results)
        
    *   [gather](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#gather)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#reduce)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#run)
        
    *   [scope](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy#scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/parameter_server_strategy_v2.py#L72-L579)

An multi-worker tf.distribute strategy with parameter servers.

Inherits From: [`Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)

#### View aliases

**Main aliases**

[`tf.distribute.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)

tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver: tf.distribute.cluster_resolver.ClusterResolver,
        variable_partitioner: tf.distribute.experimental.partitioners.Partitioner = None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate multi-worker CPU/GPU training](https://www.tensorflow.org/guide/migrate/multi_worker_cpu_gpu_training) | *   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) |

Parameter server training is a common data-parallel method to scale up a machine learning model on multiple machines. A parameter server training cluster consists of workers and parameter servers. Variables are created on parameter servers and they are read and updated by workers in each step. By default, workers read and update these variables independently without synchronizing with each other. Under this configuration, it is known as asynchronous training.

In TensorFlow 2, we recommend an architecture based on central coordination for parameter server training. Each worker and parameter server runs a [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)
, and on top of that, a coordinator task is responsible for creating resources on workers and parameter servers, dispatching functions, and coordinating the training. The coordinator uses a [`tf.distribute.experimental.coordinator.ClusterCoordinator`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator)
 to coordinate the cluster, and a [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
 to define variables on parameter servers and computation on workers.

For the training to work, the coordinator dispatches [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
s to be executed on remote workers. Upon receiving requests from the coordinator, a worker executes the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 by reading the variables from parameter servers, executing the ops, and updating the variables on the parameter servers. Each of the worker only processes the requests from the coordinator, and communicates with parameter servers, without direct interactions with other workers in the cluster.

As a result, failures of some workers do not prevent the cluster from continuing the work, and this allows the cluster to train with instances that can be occasionally unavailable (e.g. preemptible or spot instances). The coordinator and parameter servers though, must be available at all times for the cluster to make progress.

Note that the coordinator is not one of the training workers. Instead, it creates resources such as variables and datasets, dispatches [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
s, saves checkpoints and so on. In addition to workers, parameter servers and the coordinator, an optional evaluator can be run on the side that periodically reads the checkpoints saved by the coordinator and runs evaluations against each checkpoint.

`ParameterServerStrategy` is supported with two training APIs: [Custom Training Loop (CTL)](https://www.tensorflow.org/tutorials/distribute/custom_training)
 and [Keras Training API, also known as `Model.fit`](https://www.tensorflow.org/tutorials/distribute/keras)
. CTL is recommended when users prefer to define the details of their training loop, and [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
 is recommended when users prefer a high-level abstraction and handling of training.

When using a CTL, `ParameterServerStrategy` has to work in conjunction with a [`tf.distribute.experimental.coordinator.ClusterCoordinator`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator)
 object.

When using [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
, currently only the `tf.keras.utils.experimental.DatasetCreator` input type is supported.

**Example code for coordinator**

This section provides code snippets that are intended to be run on (the only) one task that is designated as the coordinator. Note that `cluster_resolver`, `variable_partitioner`, and `dataset_fn` arguments are explained in the following "Cluster setup", "Variable partitioning", and "Dataset preparation" sections.

With a CTL,

# Prepare a strategy to use with the cluster and variable partitioning info.
    strategy = tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver=...,
        variable_partitioner=...)
    coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
        strategy=strategy)
    
    # Prepare a distribute dataset that will place datasets on the workers.
    distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn=...)
    
    with strategy.scope():
      model = ...
      optimizer, metrics = ...  # Keras optimizer/metrics are great choices
      checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)
      checkpoint_manager = tf.train.CheckpointManager(
          checkpoint, checkpoint_dir, max_to_keep=2)
      # `load_checkpoint` infers initial epoch from `optimizer.iterations`.
      initial_epoch = load_checkpoint(checkpoint_manager) or 0
    
    @tf.function
    def worker_fn(iterator):
    
      def replica_fn(inputs):
        batch_data, labels = inputs
        # calculate gradient, applying gradient, metrics update etc.
    
      strategy.run(replica_fn, args=(next(iterator),))
    
    for epoch in range(initial_epoch, num_epoch):
      distributed_iterator = iter(distributed_dataset)  # Reset iterator state.
      for step in range(steps_per_epoch):
    
        # Asynchronously schedule the `worker_fn` to be executed on an arbitrary
        # worker. This call returns immediately.
        coordinator.schedule(worker_fn, args=(distributed_iterator,))
    
      # `join` blocks until all scheduled `worker_fn`s finish execution. Once it
      # returns, we can read the metrics and save checkpoints as needed.
      coordinator.join()
      logging.info('Metric result: %r', metrics.result())
      train_accuracy.reset_states()
      checkpoint_manager.save()

With [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
,

# Prepare a strategy to use with the cluster and variable partitioning info.
    strategy = tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver=...,
        variable_partitioner=...)
    
    # A dataset function takes a `input_context` and returns a `Dataset`
    def dataset_fn(input_context):
      dataset = tf.data.Dataset.from_tensors(...)
      return dataset.repeat().shard(...).batch(...).prefetch(...)
    
    # With `Model.fit`, a `DatasetCreator` needs to be used.
    input = tf.keras.utils.experimental.DatasetCreator(dataset_fn=...)
    
    with strategy.scope():
      model = ...  # Make sure the `Model` is created within scope.
    model.compile(optimizer="rmsprop", loss="mse", steps_per_execution=..., ...)
    
    # Optional callbacks to checkpoint the model, back up the progress, etc.
    callbacks = [tf.keras.callbacks.ModelCheckpoint(...), ...]
    
    # `steps_per_epoch` is required with `ParameterServerStrategy`.
    model.fit(input, epochs=..., steps_per_epoch=..., callbacks=callbacks)

**Example code for worker and parameter servers**

In addition to the coordinator, there should be tasks designated as "worker" or "ps". They should run the following code to start a TensorFlow server, waiting for coordinator's requests:

# Provide a `tf.distribute.cluster_resolver.ClusterResolver` that serves
    # the cluster information. See below "Cluster setup" section.
    cluster_resolver = ...
    
    server = tf.distribute.Server(
        cluster_resolver.cluster_spec(),
        job_name=cluster_resolver.task_type,
        task_index=cluster_resolver.task_id,
        protocol="grpc")
    
    # Blocking the process that starts a server from exiting.
    server.join()

**Cluster setup**

In order for the tasks in the cluster to know other tasks' addresses, a [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)
 is required to be used in coordinator, worker, and ps. The [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)
 is responsible for providing the cluster information, as well as the task type and id of the current task. See [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)
 for more information.

If `TF_CONFIG` environment variable is set, a [`tf.distribute.cluster_resolver.TFConfigClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver)
 should be used as well.

Since there are assumptions in [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
 around the naming of the task types, "chief", "ps", and "worker" should be used in the [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)
 to refer to the coordinator, parameter servers, and workers, respectively.

The following example demonstrates setting `TF_CONFIG` for the task designated as a parameter server (task type "ps") and index 1 (the second task), in a cluster with 1 chief, 2 parameter servers, and 3 workers. Note that it needs to be set before the use of [`tf.distribute.cluster_resolver.TFConfigClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver)
.

Example code for cluster setup:

os.environ['TF_CONFIG'] = '''
    {
      "cluster": {
        "chief": ["chief.example.com:2222"],
        "ps": ["ps0.example.com:2222", "ps1.example.com:2222"],
        "worker": ["worker0.example.com:2222", "worker1.example.com:2222",\
                   "worker2.example.com:2222"]
      },
      "task": {
        "type": "ps",
        "index": 1
      }
    }
    '''

If you prefer to run the same binary for all tasks, you will need to let the binary branch into different roles at the beginning of the program:

# If coordinator, create a strategy and start the training program.
    if cluster_resolver.task_type == 'chief':
      strategy = tf.distribute.experimental.ParameterServerStrategy(
          cluster_resolver)
      ...
    
    # If worker/ps, create a server
    elif cluster_resolver.task_type in ("worker", "ps"):
      server = tf.distribute.Server(...)
      ...

Alternatively, you can also start a bunch of TensorFlow servers in advance and connect to them later. The coordinator can be in the same cluster or on any machine that has connectivity to workers and parameter servers. This is covered in our guide and tutorial.

**Variable creation with `strategy.scope()`**

[`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
 follows the [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
 API contract where variable creation is expected to be inside the context manager returned by `strategy.scope()`, in order to be correctly placed on parameter servers in a round-robin manner:

# In this example, we're assuming having 3 ps.
    strategy = tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver=...)
    coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
        strategy=strategy)
    
    # Variables should be created inside scope to be placed on parameter servers.
    # If created outside scope such as `v1` here, it would be placed on the
    # coordinator.
    v1 = tf.Variable(initial_value=0.0)
    
    with strategy.scope():
      v2 = tf.Variable(initial_value=1.0)
      v3 = tf.Variable(initial_value=2.0)
      v4 = tf.Variable(initial_value=3.0)
      v5 = tf.Variable(initial_value=4.0)
    
    # v2 through v5 are created in scope and are distributed on parameter servers.
    # Default placement is round-robin but the order should not be relied on.
    assert v2.device == "/job:ps/replica:0/task:0/device:CPU:0"
    assert v3.device == "/job:ps/replica:0/task:1/device:CPU:0"
    assert v4.device == "/job:ps/replica:0/task:2/device:CPU:0"
    assert v5.device == "/job:ps/replica:0/task:0/device:CPU:0"

See [`distribute.Strategy.scope`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#scope)
 for more information.

**Variable partitioning**

Having dedicated servers to store variables means being able to divide up, or "shard" the variables across the ps. Partitioning large variable among ps is a commonly used technique to boost training throughput and mitigate memory constraints. It enables parallel computations and updates on different shards of a variable, and often yields better load balancing across parameter servers. Without sharding, models with large variables (e.g, embeddings) that can't fit into one machine's memory would otherwise be unable to train.

With [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
, if a `variable_partitioner` is provided to `__init__` and certain conditions are satisfied, the resulting variables created in scope are sharded across the parameter servers, in a round-robin fashion. The variable reference returned from [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 becomes a type that serves as the container of the sharded variables. One can access `variables` attribute of this container for the actual variable components. If building model with [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
 or Keras, the variable components are collected in the `variables` alike attributes.

It is recommended to use size-based partitioners like [`tf.distribute.experimental.partitioners.MinSizePartitioner`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/MinSizePartitioner)
 to avoid partitioning small variables, which could have negative impact on model training speed.

# Partition the embedding layer into 2 shards.
    variable_partitioner = (
      tf.distribute.experimental.partitioners.MinSizePartitioner(
        min_shard_bytes=(256 << 10),
        max_shards = 2))
    strategy = tf.distribute.experimental.ParameterServerStrategy(
      cluster_resolver=...,
      variable_partitioner = variable_partitioner)
    with strategy.scope():
      embedding = tf.keras.layers.Embedding(input_dim=1024, output_dim=1024)
    assert len(embedding.variables) == 2
    assert isinstance(embedding.variables[0], tf.Variable)
    assert isinstance(embedding.variables[1], tf.Variable)
    assert embedding.variables[0].shape == (512, 1024)
    assert embedding.variables[1].shape == (512, 1024)

The sharded variable container can be converted to a `Tensor` via [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)
. This means the container can be directly used in most Python Ops where such `Tensor` conversion automatically happens. For example, in the above code snippet, `x * self.w` would implicitly apply the said tensor conversion. Note that such conversion can be expensive, as the variable components need to be transferred from multiple parameter servers to where the value is used.

[`tf.nn.embedding_lookup`](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup)
 on the other hand doesn't apply the tensor conversion, and performs parallel lookups on the variable components instead. This is crucial to scale up embedding lookups when the embedding table variable is large.

When a partitioned variable is saved to a `SavedModel`, it will be saved as if it is one single variable. This improves serving efficiency by eliminating a number of Ops that handle the partition aspects.

Known limitations of variable partitioning:

*   Number of partitions must not change across Checkpoint saving/loading.
    
*   After saving partitioned variables to a SavedModel, the SavedModel can't be loaded via [`tf.saved_model.load`](https://www.tensorflow.org/api_docs/python/tf/saved_model/load)
    .
    
*   Partition variable doesn't directly work with [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
    , please use the `variables` attributes to get the actual variable components and use them in gradient APIs instead.
    

**Dataset preparation**

With [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
, a dataset is created in each of the workers to be used for training. This is done by creating a `dataset_fn` that takes no argument and returns a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, and passing the `dataset_fn` into `tf.distribute.experimental.coordinator. ClusterCoordinator.create_per_worker_dataset`. We recommend the dataset to be shuffled and repeated to have the examples run through the training as evenly as possible.

def dataset_fn():
      filenames = ...
      dataset = tf.data.Dataset.from_tensor_slices(filenames)
    
      # Dataset is recommended to be shuffled, and repeated.
      return dataset.shuffle(buffer_size=...).repeat().batch(batch_size=...)
    
    coordinator =
        tf.distribute.experimental.coordinator.ClusterCoordinator(strategy=...)
    distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn)

**Limitations**

*   [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
     in TF2 is experimental, and the API is subject to further changes.
    
*   When using [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
    , [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
     must be used with a `tf.keras.utils.experimental.DatasetCreator`, and `steps_per_epoch` must be specified.
    

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cluster_resolver` | a [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> object. |
| `variable_partitioner` | a [`distribute.experimental.partitioners.Partitioner`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners/Partitioner)<br> that specifies how to partition variables. If `None`, variables will not be partitioned.<br><br>*   Predefined partitioners in [`tf.distribute.experimental.partitioners`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/partitioners)<br>     can be used for this argument. A commonly used partitioner is `MinSizePartitioner(min_shard_bytes = 256 << 10, max_shards = num_ps)`, which allocates at least 256K per shard, and each ps gets at most one shard.<br>    <br>*   `variable_partitioner` will be called for each variable created under strategy `scope` to instruct how the variable should be partitioned. Variables that have only one partition along the partitioning axis (i.e., no need for partition) will be created as a normal [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>    .<br>    <br>*   Only the first / outermost axis partitioning is supported.<br>    <br>*   Div partition strategy is used to partition variables. Assuming we assign consecutive integer ids along the first axis of a variable, then ids are assigned to shards in a contiguous manner, while attempting to keep each shard size identical. If the ids do not evenly divide the number of shards, each of the first several shards will be assigned one more id. For instance, a variable whose first dimension is 13 has 13 ids, and they are split across 5 shards as: `[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.<br>    <br>*   Variables created under `strategy.extended.colocate_vars_with` will not be partitioned. |

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
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1557-L1673)\
\
run(\
        fn, args=(), kwargs=None, options=None\
    )\
\
Invokes `fn` on each replica, with the given arguments.\
\
This method is the primary way to distribute your computation with a tf.distribute object. It invokes `fn` on each replica. If `args` or `kwargs` have [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)\
, such as those produced by a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)\
 from [`tf.distribute.Strategy.experimental_distribute_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_dataset)\
 or [`tf.distribute.Strategy.distribute_datasets_from_function`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#distribute_datasets_from_function)\
, when `fn` is executed on a particular replica, it will be executed with the component of [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)\
 that correspond to that replica.\
\
`fn` is invoked under a replica context. `fn` may call [`tf.distribute.get_replica_context()`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_replica_context)\
 to access members such as `all_reduce`. Please see the module-level docstring of tf.distribute for the concept of replica context.\
\
All arguments in `args` or `kwargs` can be a nested structure of tensors, e.g. a list of tensors, in which case `args` and `kwargs` will be passed to the `fn` invoked on each replica. Or `args` or `kwargs` can be [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)\
 containing tensors or composite tensors, i.e. [`tf.compat.v1.TensorInfo.CompositeTensor`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/TensorInfo/CompositeTensor)\
, in which case each `fn` call will get the component of a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)\
 corresponding to its replica. Note that arbitrary Python values that are not of the types above are not supported.\
\
#### Example usage:\
\
1.  Constant tensor input.\
    \
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])\
        \
2.  DistributedValues input.\
    \
    strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])\
        \
3.  Use [`tf.distribute.ReplicaContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext)\
     to allreduce values.\
    \
    strategy = tf.distribute.MirroredStrategy(["gpu:0", "gpu:1"])\
        \
\
|     |     |\
| --- | --- |\
| Args |     |\
| `fn` | The function to run on each replica. |\
| `args` | Optional positional arguments to `fn`. Its element can be a tensor, a nested structure of tensors or a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>. |\
| `kwargs` | Optional keyword arguments to `fn`. Its element can be a tensor, a nested structure of tensors or a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>. |\
| `options` | An optional instance of [`tf.distribute.RunOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/RunOptions)<br> specifying the options to run `fn`. |\
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