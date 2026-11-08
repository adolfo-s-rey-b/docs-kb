[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#compute_gradients)
        
    *   [get\_chief\_queue\_runner](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_chief_queue_runner)
        
    *   [get\_init\_tokens\_op](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_init_tokens_op)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_slot_names)
        
    *   [make\_session\_run\_hook](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#make_session_run_hook)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.SyncReplicasOptimizer Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#methods)
    *   [apply\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#apply_gradients)
        
    *   [compute\_gradients](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#compute_gradients)
        
    *   [get\_chief\_queue\_runner](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_chief_queue_runner)
        
    *   [get\_init\_tokens\_op](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_init_tokens_op)
        
    *   [get\_name](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_name)
        
    *   [get\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_slot)
        
    *   [get\_slot\_names](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#get_slot_names)
        
    *   [make\_session\_run\_hook](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#make_session_run_hook)
        
    *   [minimize](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#minimize)
        
    *   [variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#variables)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SyncReplicasOptimizer#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L41-L442)

Class to synchronize, aggregate gradients and pass them to the optimizer.

Inherits From: [`Optimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Optimizer)

tf.compat.v1.train.SyncReplicasOptimizer(
        opt,
        replicas_to_aggregate,
        total_num_replicas=None,
        variable_averages=None,
        variables_to_average=None,
        use_locking=False,
        name='sync_replicas'
    )

This class is deprecated. For synchronous training, please use [Distribution Strategies](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/distribute)
.

In a typical asynchronous training environment, it's common to have some stale gradients. For example, with a N-replica asynchronous training, gradients will be applied to the variables N times independently. Depending on each replica's training speed, some gradients might be calculated from copies of the variable from several steps back (N-1 steps on average). This optimizer avoids stale gradients by collecting gradients from all replicas, averaging them, then applying them to the variables in one shot, after which replicas can fetch the new variables and continue.

The following accumulators/queue are created:

*   N `gradient accumulators`, one per variable to train. Gradients are pushed to them and the chief worker will wait until enough gradients are collected and then average them before applying to variables. The accumulator will drop all stale gradients (more details in the accumulator op).
*   1 `token` queue where the optimizer pushes the new global\_step value after all variables are updated.

The following local variable is created:

*   `sync_rep_local_step`, one per replica. Compared against the global\_step in each accumulator to check for staleness of the gradients.

The optimizer adds nodes to the graph to collect gradients and pause the trainers until variables are updated. For the Parameter Server job:

1.  An accumulator is created for each variable, and each replica pushes the gradients into the accumulators instead of directly applying them to the variables.
2.  Each accumulator averages once enough gradients (replicas\_to\_aggregate) have been accumulated.
3.  Apply the averaged gradients to the variables.
4.  Only after all variables have been updated, increment the global step.
5.  Only after step 4, pushes `global_step` in the `token_queue`, once for each worker replica. The workers can now fetch the global step, use it to update its local\_step variable and start the next batch. Please note that some workers can consume multiple minibatches, while some may not consume even one. This is because each worker fetches minibatches as long as a token exists. If one worker is stuck for some reason and does not consume a token, another worker can use it.

#### For the replicas:

1.  Start a step: fetch variables and compute gradients.
2.  Once the gradients have been computed, push them into gradient accumulators. Each accumulator will check the staleness and drop the stale.
3.  After pushing all the gradients, dequeue an updated value of global\_step from the token queue and record that step to its local\_step variable. Note that this is effectively a barrier.
4.  Start the next batch.

### Usage

# Create any optimizer to update the variables, say a simple SGD:
    opt = GradientDescentOptimizer(learning_rate=0.1)
    
    # Wrap the optimizer with sync_replicas_optimizer with 50 replicas: at each
    # step the optimizer collects 50 gradients before applying to variables.
    # Note that if you want to have 2 backup replicas, you can change
    # total_num_replicas=52 and make sure this number matches how many physical
    # replicas you started in your job.
    opt = tf.compat.v1.train.SyncReplicasOptimizer(opt, replicas_to_aggregate=50,
                                   total_num_replicas=50)
    
    # Some models have startup_delays to help stabilize the model but when using
    # sync_replicas training, set it to 0.
    
    # Now you can call `minimize()` or `compute_gradients()` and
    # `apply_gradients()` normally
    training_op = opt.minimize(total_loss, global_step=self.global_step)
    
    
    # You can create the hook which handles initialization and queues.
    sync_replicas_hook = opt.make_session_run_hook(is_chief)

In the training program, every worker will run the train\_op as if not synchronized.

with training.MonitoredTrainingSession(
        master=workers[worker_id].target, is_chief=is_chief,
        hooks=[sync_replicas_hook]) as mon_sess:
      while not mon_sess.should_stop():
        mon_sess.run(training_op)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `opt` | The actual optimizer that will be used to compute and apply the gradients. Must be one of the Optimizer classes. |
| `replicas_to_aggregate` | number of replicas to aggregate for each variable update. |
| `total_num_replicas` | Total number of tasks/workers/replicas, could be different from replicas\_to\_aggregate. If total\_num\_replicas > replicas\_to\_aggregate: it is backup\_replicas + replicas\_to\_aggregate. If total\_num\_replicas < replicas\_to\_aggregate: Replicas compute multiple batches per update to variables. |
| `variable_averages` | Optional `ExponentialMovingAverage` object, used to maintain moving averages for the variables passed in `variables_to_average`. |
| `variables_to_average` | a list of variables that need to be averaged. Only needed if variable\_averages is passed in. |
| `use_locking` | If True use locks for update operation. |
| `name` | string. Optional name of the returned operation. |

Methods
-------

### `apply_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L215-L338)

apply_gradients(
        grads_and_vars, global_step=None, name=None
    )

Apply gradients to variables.

This contains most of the synchronization implementation and also wraps the apply\_gradients() from the real optimizer.

|     |     |
| --- | --- |
| Args |     |
| `grads_and_vars` | List of (gradient, variable) pairs as returned by compute\_gradients(). |
| `global_step` | Optional Variable to increment by one after the variables have been updated. |
| `name` | Optional name for the returned operation. Default to the name passed to the Optimizer constructor. |

|     |     |
| --- | --- |
| Returns |     |
| `train_op` | The op to dequeue a token so the replicas can exit this batch and start the next one. This is executed by each replica. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the grads\_and\_vars is empty. |
| `ValueError` | If global step is not provided, the staleness cannot be checked. |

### `compute_gradients`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L197-L213)

compute_gradients(
        *args, **kwargs
    )

Compute gradients of "loss" for the variables in "var\_list".

This simply wraps the compute\_gradients() from the real optimizer. The gradients will be aggregated in the apply\_gradients() so that user can modify the gradients like clipping with per replica global norm if needed. The global norm with aggregated gradients can be bad as one replica's huge gradients can hurt the gradients from other replicas.

|     |     |
| --- | --- |
| Args |     |
| `*args` | Arguments for compute\_gradients(). |
| `**kwargs` | Keyword arguments for compute\_gradients(). |

|     |
| --- |
| Returns |     |
| A list of (gradient, variable) pairs. |     |

### `get_chief_queue_runner`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L340-L358)

get_chief_queue_runner()

Returns the QueueRunner for the chief to execute.

This includes the operations to synchronize replicas: aggregate gradients, apply to variables, increment global step, insert tokens to token queue.

Note that this can only be called after calling apply\_gradients() which actually generates this queuerunner.

|     |
| --- |
| Returns |     |
| A `QueueRunner` for chief to execute. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If this is called before apply\_gradients(). |

### `get_init_tokens_op`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L399-L438)

get_init_tokens_op(
        num_tokens=-1
    )

Returns the op to fill the sync\_token\_queue with the tokens.

This is supposed to be executed in the beginning of the chief/sync thread so that even if the total\_num\_replicas is less than replicas\_to\_aggregate, the model can still proceed as the replicas can compute multiple steps per variable update. Make sure: `num_tokens >= replicas_to_aggregate - total_num_replicas`.

|     |     |
| --- | --- |
| Args |     |
| `num_tokens` | Number of tokens to add to the queue. |

|     |
| --- |
| Returns |     |
| An op for the chief/sync replica to fill the token queue. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If this is called before apply\_gradients(). |
| `ValueError` | If num\_tokens are smaller than replicas\_to\_aggregate - total\_num\_replicas. |

### `get_name`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L460-L461)

get_name()

### `get_slot`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L360-L372)

get_slot(
        *args, **kwargs
    )

Return a slot named "name" created for "var" by the Optimizer.

This simply wraps the get\_slot() from the actual optimizer.

|     |     |
| --- | --- |
| Args |     |
| `*args` | Arguments for get\_slot(). |
| `**kwargs` | Keyword arguments for get\_slot(). |

|     |
| --- |
| Returns |     |
| The `Variable` for the slot if it was created, `None` otherwise. |     |

### `get_slot_names`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L385-L397)

get_slot_names(
        *args, **kwargs
    )

Return a list of the names of slots created by the `Optimizer`.

This simply wraps the get\_slot\_names() from the actual optimizer.

|     |     |
| --- | --- |
| Args |     |
| `*args` | Arguments for get\_slot(). |
| `**kwargs` | Keyword arguments for get\_slot(). |

|     |
| --- |
| Returns |     |
| A list of strings. |     |

### `make_session_run_hook`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L440-L442)

make_session_run_hook(
        is_chief, num_tokens=-1
    )

Creates a hook to handle SyncReplicasHook ops such as initialization.

### `minimize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/optimizer.py#L463-L521)

minimize(
        loss,
        global_step=None,
        var_list=None,
        gate_gradients=GATE_OP,
        aggregation_method=None,
        colocate_gradients_with_ops=False,
        name=None,
        grad_loss=None
    )

Add operations to minimize `loss` by updating `var_list`.

This method simply combines calls `compute_gradients()` and `apply_gradients()`. If you want to process the gradient before applying them call `compute_gradients()` and `apply_gradients()` explicitly instead of using this function.

|     |     |
| --- | --- |
| Args |     |
| `loss` | A `Tensor` containing the value to minimize. |
| `global_step` | Optional `Variable` to increment by one after the variables have been updated. |
| `var_list` | Optional list or tuple of `Variable` objects to update to minimize `loss`. Defaults to the list of variables collected in the graph under the key `GraphKeys.TRAINABLE_VARIABLES`. |
| `gate_gradients` | How to gate the computation of gradients. Can be `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`. |
| `aggregation_method` | Specifies the method used to combine gradient terms. Valid values are defined in the class `AggregationMethod`. |
| `colocate_gradients_with_ops` | If True, try colocating gradients with the corresponding op. |
| `name` | Optional name for the returned operation. |
| `grad_loss` | Optional. A `Tensor` holding the gradient computed for `loss`. |

|     |
| --- |
| Returns |     |
| An Operation that updates the variables in `var_list`. If `global_step` was not `None`, that operation also increments `global_step`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If some of the variables are not `Variable` objects. |

#### eager compatibility

When eager execution is enabled, `loss` should be a Python function that takes no arguments and computes the value to be minimized. Minimization (and gradient computation) is done with respect to the elements of `var_list` if not None, else with respect to any trainable variables created during the execution of the `loss` function. `gate_gradients`, `aggregation_method`, `colocate_gradients_with_ops` and `grad_loss` are ignored when eager execution is enabled.

### `variables`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/sync_replicas_optimizer.py#L374-L383)

variables()

Fetches a list of optimizer variables in the default graph.

This wraps `variables()` from the actual optimizer. It does not include the `SyncReplicasOptimizer`'s local step.

|     |
| --- |
| Returns |     |
| A list of variables. |     |

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| GATE\_GRAPH | `2` |
| GATE\_NONE | `0` |
| GATE\_OP | `1` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.