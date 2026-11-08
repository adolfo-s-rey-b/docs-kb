[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#methods)
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
        
    *   [save\_checkpoint\_if\_preempted](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#save_checkpoint_if_preempted)
        
    *   [watch\_preemption\_scope](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#watch_preemption_scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.PreemptionCheckpointHandler Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#methods)
    *   [run](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
        
    *   [save\_checkpoint\_if\_preempted](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#save_checkpoint_if_preempted)
        
    *   [watch\_preemption\_scope](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#watch_preemption_scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/failure_handling/failure_handling.py#L336-L1264)

Preemption and error handler for synchronous training.

tf.distribute.experimental.PreemptionCheckpointHandler(
        cluster_resolver,
        checkpoint_or_checkpoint_manager,
        checkpoint_dir=None,
        termination_config=None
    )

A `PreemptionCheckpointHandler` coordinates all workers to save a checkpoint upon receiving a preemption signal. It also helps disseminate application error messages accurately among the cluster. When a `PreemptionCheckpointHandler` object is created, it restores values from the latest checkpoint file if any exists.

Right after the initialization, the object starts to watch out for termination signal for any member in the cluster. If receiving a signal, the next time the worker executes [`PreemptionCheckpointHandler.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
, the `PreemptionCheckpointHandler` will align all workers to save a checkpoint. Then, if an `exit_fn` is configured via [`tf.distribute.experimental.TerminationConfig`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig)
, it will be invoked. Otherwise, the process will simply exit and later the platform should restart it.

For users of [`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
, the core API is [`PreemptionCheckpointHandler.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
:

strategy = tf.distribute.MultiWorkerMirroredStrategy()
    
    trained_epoch = tf.Variable(initial_value=tf.constant(0, dtype=tf.dtypes.int64), name='epoch')
    step_in_epoch = tf.Variable(initial_value=tf.constant(0, dtype=tf.dtypes.int64), name='step_in_epoch')
    
    with strategy.scope():
      dataset, model, optimizer = ...
    
      checkpoint = tf.train.Checkpoint(optimizer=optimizer,
                                       model=model,
                                       trained_epoch=trained_epoch,
                                       step_in_epoch=step_in_epoch)
    
      preemption_checkpoint_handler = tf.distribute.experimental.PreemptionCheckpointHandler(cluster_resolver, checkpoint, checkpoint_dir)
    
    while trained_epoch.numpy() < NUM_EPOCH:
    
      while step_in_epoch.numpy() < STEPS_PER_EPOCH:
    
        # distributed_train_function contains a call to strategy.run.
        loss += preemption_checkpoint_handler.run(distributed_train_function, args=(next(iterator),))
        # For users of MultiWorkerMirroredStrategy, usually
        # STEPS_PER_TRAIN_FUNCTION = 1.
        step_in_epoch.assign_add(STEPS_PER_TRAIN_FUNCTION)
        ...
    
      epoch.assign_add(1)
      step_in_epoch.assign(0)

For users of [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
, the core APIs are [`PreemptionCheckpointHandler.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
 and [`PreemptionCheckpointHandler.watch_preemption_scope`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#watch_preemption_scope)
:

strategy = tf.distribute.TPUStrategy(tpu_cluster_resolver)
    
    # Rest of TPU init omitted, see documentation for TPUSTrategy.
    
    with preemption_checkpoint_handler.watch_preemption_scope():
      while trained_epoch.numpy() < NUM_EPOCH:
    
        while step_in_epoch.numpy() < STEPS_PER_EPOCH:
    
          # distributed_train_function contains a call to strategy.run.
          loss += preemption_checkpoint_handler.run(distributed_train_function, args=(next(iterator),))
    
          # For users of TPUStrategy, usually STEPS_PER_TRAIN_FUNCTION >> 1 since
          # clustering multiple steps within a tf.function amortizes the overhead
          # of launching a multi-device function on TPU Pod.
          step_in_epoch.assign_add(STEPS_PER_TRAIN_FUNCTION)
          ...
    
        epoch.assign_add(1)
        step_in_epoch.assign(0)

Not all interruptions come with advance notice so that the `PreemptionCheckpointHandler` can handle them, e.g., those caused by hardware failure. For a user who saves checkpoints for these cases themselves outside the `PreemptionCheckpointHandler`, if they are using a [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
, pass it as the `checkpoint_or_checkpoint_manager` argument to the `PreemptionCheckpointHandler`. If they do not have a [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
 but are directly working with [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
, we advise saving the checkpoints in the directory that's passed as the `checkpoint_dir` argument. In this way, at the program beginning, `PreemptionCheckpointHandler` can restore the latest checkpoint from the directory, no matter it's saved by the user themselves or saved by the `PreemptionCheckpointHandler` before preemption happens.

**A note on the platform:**

`PreemptionCheckpointHandler` can only handle the kind of termination with advance notice. For now, the API recognizes the termination signal for CPU, GPU, and TPU on Google Borg and CPU and GPU on the Google Cloud Platform. In these cases, `PreemptionCheckpointHandler` will automatically adopt the correct preemption/maintenance notification detection mechanism. Users of other platforms can configure a detection monitoring behavior through the [`tf.distribute.experimental.TerminationConfig`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig)
. Customization for the exit behavior and grace period length could also be done here.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cluster_resolver` | a [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> object. You may also obtain it through the `cluster_resolver` attribute of the distribution strategy in use. |
| `checkpoint_or_checkpoint_manager` | a [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br> or a [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br>. If you are using a [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br> to manage checkpoints outside the `PreemptionCheckpointHandler` for backup purpose as well, pass it as `checkpoint_or_checkpoint_manager` argument. Otherwise, pass a [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> and the `PreemptionCheckpointHandler` will create a [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br> to manage it in the `checkpoint_dir`. |
| `checkpoint_dir` | a directory where the `PreemptionCheckpointHandler` saves and restores checkpoints. When a `PreemptionCheckpointHandler` is created, the latest checkpoint in the `checkpoint_dir` will be restored. (This is not needed if a [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br> instead of a [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> is passed as the `checkpoint_or_checkpoint_manager` argument.) |
| `termination_config` | optional, a [`tf.distribute.experimental.TerminationConfig`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig)<br> object to configure for a platform other than Google Borg or GCP. |

Methods
-------

### `run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/failure_handling/failure_handling.py#L805-L895)

run(
        distributed_train_function, *args, **kwargs
    )

Runs a training function with error and preemption handling.

This function handles the preemption signal from any peer in the cluster by saving the training progress and exiting gracefully. It will also broadcast any program error encountered during the execution of `distributed_train_function` to all workers so that they can raise the same error.

The `distributed_train_function` argument should be a distributed train function (i.e., containing a call to [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run)
). For [`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
 users, we recommend passing in a single-step `distributed_train_function` to [`PreemptionCheckpointHandler.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
 so that the checkpoint can be saved in time in case a preemption signal or maintenance notice is sent.

Besides the preemption and error handling part, `PreemptionCheckpointHandler.run(distributed_train_function, *args, **kwargs)` has the same effect and output as `distributed_train_function(*args, **kwargs)`. `distributed_train_function` can return either some or no result. The following is a shortened example:

@tf.function
    def distributed_train_step(iterator):
      # A distributed single-step training function.
    
      def step_fn(inputs):
        # A per-replica single-step training function.
        x, y = inputs
        ...
        return loss
    
      per_replica_losses = strategy.run(step_fn, args=(next(iterator),))
      return strategy.reduce(
          tf.distribute.ReduceOp.SUM, per_replica_losses, axis=None)
    
    for epoch in range(preemption_handler.total_run_calls // STEPS_PER_EPOCH,
                       EPOCHS_TO_RUN):
      iterator = iter(multi_worker_dataset)
      total_loss = 0.0
      num_batches = 0
    
      for step in range(preemption_handler.total_run_calls % STEPS_PER_EPOCH,
                        STEPS_PER_EPOCH):
        total_loss += preemption_handler.run(distributed_train_step)
        num_batches += 1
    
      train_loss = total_loss / num_batches
      print('Epoch: %d, train_loss: %f.' %(epoch.numpy(), train_loss))
    
      train_accuracy.reset_states()

|     |     |
| --- | --- |
| Args |     |
| `distributed_train_function` | A (single-step) distributed training function. |
| `*args` | args for `distributed_train_function`. |
| `**kwargs` | kwargs for `distributed_train_function`. |

|     |
| --- |
| Raises |     |
| Program error encountered by any member in the cluster while executing the `distributed_train_function`, or any error from the program error propagation process. |     |

|     |
| --- |
| Returns |     |
| Result of running the `distributed_train_function`. |     |

### `save_checkpoint_if_preempted`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/failure_handling/failure_handling.py#L930-L997)

save_checkpoint_if_preempted(
        *args, **kwargs
    )

Saves a checkpoint if a preemption signal has been made available.

This is an alternative API for [`PreemptionCheckpointHandler.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
 and [`PreemptionCheckpointHandler.watch_preemption_scope`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#watch_preemption_scope)
. This method works for both [`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
 and [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
. However, **for TPUStrategy, this method will add a synchronization point between workers and the coordinator** and thus may have performance implication. If this is a concern, use the combination of [`PreemptionCheckpointHandler.watch_preemption_scope`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#watch_preemption_scope)
 and [`PreemptionCheckpointHandler.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
 instead.

strategy = tf.distribute.TPUStrategy(tpu_cluster_resolver)
    # initialization omitted
    
    with strategy.scope():
      # Save in the checkpoint.
      trained_step = tf.Variable(initial_value=tf.constant(0, dtype=tf.dtypes.int64), name='trained_step', aggregation=tf.VariableAggregation.ONLY_FIRST_REPLICA)
    
      checkpoint_manager = tf.train.CheckpointManager(checkpoint, directory, max_to_keep=1)
      preemption_handler = tf.distribute.experimental.PreemptionCheckpointHandler(cluster_resolver, checkpoint_manager)
    
    while trained_step.numpy() < NUM_STEPS:
      # Train STEPS_IN_FUNCTION steps at once.
      train_multi_step_function()
      trained_step.assign_add(STEPS_IN_FUNCTION)
      preemption_handler.save_checkpoint_if_preempted()

|     |     |
| --- | --- |
| Args |     |
| `*args` | args for [`tf.train.CheckpointManager.save()`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#save)<br> to save checkpoint. |
| `**kwargs` | kwargs for [`tf.train.CheckpointManager.save()`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#save)<br> to save. |

### `watch_preemption_scope`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/failure_handling/failure_handling.py#L999-L1056)

@tf_contextlib.contextmanager

Syncs error and maybe save checkpoint for usage with TPUStrategy.

#### Example usage:

with preemption_checkpoint_handler.watch_preemption_scope():
      while trained_step.numpy() < NUM_STEPS:
    
        # distributed_train_function contains a call to strategy.run.
        loss += preemption_checkpoint_handler.run(distributed_train_function, args=(next(iterator),))
        trained_step.assign_add(STEPS_PER_TRAIN_FUNCTION)

In this workflow, [`PreemptionCheckpointHandler.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler#run)
 will flag preemption signal received, and `watch_preemption_scope` will handle the preemption signal by saving a checkpoint and then either exit to restart or execute a user-passed `exit_fn` in [`tf.distribute.experimental.TerminationConfig`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/TerminationConfig)
. If no preemption signal is received during execution of ops and function inside the scope, `watch_preemption_scope` ensures the completion of all async op and function execution when exiting and will raises exceptions if async execution results in an error state.

|     |
| --- |
| Yields |     |
| None |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.