[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#methods)
    *   [batch\_reduce\_to](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#batch_reduce_to)
        
    *   [broadcast\_to](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#broadcast_to)
        
    *   [call\_for\_each\_replica](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#call_for_each_replica)
        
    *   [colocate\_vars\_with](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#colocate_vars_with)
        
    *   [experimental\_make\_numpy\_dataset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#experimental_make_numpy_dataset)
        
    *   [experimental\_run\_steps\_on\_iterator](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#experimental_run_steps_on_iterator)
        
    *   [non\_slot\_devices](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#non_slot_devices)
        
    *   [read\_var](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#read_var)
        
    *   [reduce\_to](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#reduce_to)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#update)
        
    *   [update\_non\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#update_non_slot)
        
    *   [value\_container](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#value_container)
        
    *   [variable\_created\_in\_scope](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#variable_created_in_scope)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.distribute.StrategyExtended Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#methods)
    *   [batch\_reduce\_to](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#batch_reduce_to)
        
    *   [broadcast\_to](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#broadcast_to)
        
    *   [call\_for\_each\_replica](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#call_for_each_replica)
        
    *   [colocate\_vars\_with](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#colocate_vars_with)
        
    *   [experimental\_make\_numpy\_dataset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#experimental_make_numpy_dataset)
        
    *   [experimental\_run\_steps\_on\_iterator](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#experimental_run_steps_on_iterator)
        
    *   [non\_slot\_devices](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#non_slot_devices)
        
    *   [read\_var](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#read_var)
        
    *   [reduce\_to](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#reduce_to)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#update)
        
    *   [update\_non\_slot](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#update_non_slot)
        
    *   [value\_container](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#value_container)
        
    *   [variable\_created\_in\_scope](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/StrategyExtended#variable_created_in_scope)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3115-L3360)

Additional APIs for algorithms that need to be distribution-aware.

Inherits From: [`StrategyExtended`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended)

tf.compat.v1.distribute.StrategyExtended(
        container_strategy
    )

Some common use cases of functions on this page:

*   _Locality_

[`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 can have the same _locality_ as a _distributed variable_, which leads to a mirrored value residing on the same devices as the variable (as opposed to the compute devices). Such values may be passed to a call to [`tf.distribute.StrategyExtended.update`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#update)
 to update the value of a variable. You may use [`tf.distribute.StrategyExtended.colocate_vars_with`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#colocate_vars_with)
 to give a variable the same locality as another variable. You may convert a "PerReplica" value to a variable's locality by using [`tf.distribute.StrategyExtended.reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#reduce_to)
 or [`tf.distribute.StrategyExtended.batch_reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#batch_reduce_to)
.

*   _How to update a distributed variable_

A distributed variable is variables created on multiple devices. As discussed in the [glossary](https://www.tensorflow.org/api_docs/python/tf/distribute)
, mirrored variable and SyncOnRead variable are two examples. The standard pattern for updating distributed variables is to:

1.  In your function passed to [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run)
    , compute a list of (update, variable) pairs. For example, the update might be a gradient of the loss with respect to the variable.
2.  Switch to cross-replica mode by calling `tf.distribute.get_replica_context().merge_call()` with the updates and variables as arguments.
3.  Call [`tf.distribute.StrategyExtended.reduce_to(VariableAggregation.SUM, t, v)`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#reduce_to)
     (for one variable) or [`tf.distribute.StrategyExtended.batch_reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#batch_reduce_to)
     (for a list of variables) to sum the updates.
4.  Call [`tf.distribute.StrategyExtended.update(v)`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#update)
     for each variable to update its value.

Steps 2 through 4 are done automatically by class [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 if you call its [`tf.keras.optimizers.Optimizer.apply_gradients`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#apply_gradients)
 method in a replica context.

In fact, a higher-level solution to update a distributed variable is by calling `assign` on the variable as you would do to a regular [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
. You can call the method in both _replica context_ and _cross-replica context_. For a _mirrored variable_, calling `assign` in _replica context_ requires you to specify the `aggregation` type in the variable constructor. In that case, the context switching and sync described in steps 2 through 4 are handled for you. If you call `assign` on _mirrored variable_ in _cross-replica context_, you can only assign a single value or assign values from another mirrored variable or a mirrored [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
. For a _SyncOnRead variable_, in _replica context_, you can simply call `assign` on it and no aggregation happens under the hood. In _cross-replica context_, you can only assign a single value to a SyncOnRead variable. One example case is restoring from a checkpoint: if the `aggregation` type of the variable is [`tf.VariableAggregation.SUM`](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation#SUM)
, it is assumed that replica values were added before checkpointing, so at the time of restoring, the value is divided by the number of replicas and then assigned to each replica; if the `aggregation` type is [`tf.VariableAggregation.MEAN`](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation#MEAN)
, the value is assigned to each replica directly.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `experimental_between_graph` | Whether the strategy uses between-graph replication or not.<br><br>This is expected to return a constant value that will not be changed throughout its life cycle. |
| `experimental_require_static_shapes` | Returns `True` if static shape is required; `False` otherwise. |
| `experimental_should_init` | Whether initialization is needed. |
| `parameter_devices` | Returns the tuple of all devices used to place variables. |
| `should_checkpoint` | Whether checkpointing is needed. |
| `should_save_summary` | Whether saving summaries is needed. |
| `worker_devices` | Returns the tuple of all devices used to for compute replica execution. |

Methods
-------

### `batch_reduce_to`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2758-L2831)

batch_reduce_to(
        reduce_op, value_destination_pairs, options=None
    )

Combine multiple `reduce_to` calls into one for faster execution.

Similar to `reduce_to`, but accepts a list of (value, destinations) pairs. It's more efficient than reduce each value separately.

This API currently can only be called in cross-replica context. Other variants to reduce values across replicas are:

*   [`tf.distribute.StrategyExtended.reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#reduce_to)
    : the non-batch version of this API.
*   [`tf.distribute.ReplicaContext.all_reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_reduce)
    : the counterpart of this API in replica context. It supports both batched and non-batched all-reduce.
*   [`tf.distribute.Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#reduce)
    : a more convenient method to reduce to the host in cross-replica context.

See `reduce_to` for more information.

@tf.function def step\_fn(var):

def merge\_fn(strategy, value, var): # All-reduce the value. Note that `value` here is a # [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
. reduced = strategy.extended.batch\_reduce\_to( tf.distribute.ReduceOp.SUM, \[(value, var)\])\[0\] strategy.extended.update(var, lambda var, value: var.assign(value), args=(reduced,))

value = tf.identity(1.) tf.distribute.get\_replica\_context().merge\_call(merge\_fn, args=(value, var))

def run(strategy): with strategy.scope(): v = tf.Variable(0.) strategy.run(step\_fn, args=(v,)) return v

run(tf.distribute.MirroredStrategy(\["GPU:0", "GPU:1"\])) MirroredVariable:{ 0: , 1: } run(tf.distribute.experimental.CentralStorageStrategy( compute\_devices=\["GPU:0", "GPU:1"\], parameter\_device="CPU:0")) run(tf.distribute.OneDeviceStrategy("GPU:0"))

|     |     |
| --- | --- |
| Args |     |
| `reduce_op` | a [`tf.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)<br> value specifying how values should be combined. Allows using string representation of the enum such as "SUM", "MEAN". |
| `value_destination_pairs` | a sequence of (value, destinations) pairs. See `tf.distribute.Strategy.reduce_to` for descriptions. |
| `options` | a [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br>. Options to perform collective operations. This overrides the default options if the [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> takes one in the constructor. See [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br> for details of the options. |

|     |
| --- |
| Returns |     |
| A list of reduced values, one per pair in `value_destination_pairs`. |     |

### `broadcast_to`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3143-L3158)

broadcast_to(
        tensor, destinations
    )

Mirror a tensor on one device to all worker devices.

|     |     |
| --- | --- |
| Args |     |
| `tensor` | A Tensor value to broadcast. |
| `destinations` | A mirrored variable or device string specifying the destination devices to copy `tensor` to. |

|     |
| --- |
| Returns |     |
| A value mirrored to `destinations` devices. |     |

### `call_for_each_replica`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3215-L3263)

call_for_each_replica(
        fn, args=(), kwargs=None
    )

Run `fn` once per replica.

`fn` may call `tf.get_replica_context()` to access methods such as `replica_id_in_sync_group` and `merge_call()`.

`merge_call()` is used to communicate between the replicas and re-enter the cross-replica context. All replicas pause their execution having encountered a `merge_call()` call. After that the `merge_fn`\-function is executed. Its results are then unwrapped and given back to each replica call. After that execution resumes until `fn` is complete or encounters another `merge_call()`. Example:

# Called once in "cross-replica" context.
    def merge_fn(distribution, three_plus_replica_id):
      # sum the values across replicas
      return sum(distribution.experimental_local_results(three_plus_replica_id))
    
    # Called once per replica in `distribution`, in a "replica" context.
    def fn(three):
      replica_ctx = tf.get_replica_context()
      v = three + replica_ctx.replica_id_in_sync_group
      # Computes the sum of the `v` values across all replicas.
      s = replica_ctx.merge_call(merge_fn, args=(v,))
      return s + v
    
    with distribution.scope():
      # in "cross-replica" context
      ...
      merged_results = distribution.run(fn, args=[3])
      # merged_results has the values from every replica execution of `fn`.
      # This statement prints a list:
      print(distribution.experimental_local_results(merged_results))

|     |     |
| --- | --- |
| Args |     |
| `fn` | function to run (will be run once per replica). |
| `args` | Tuple or list with positional arguments for `fn`. |
| `kwargs` | Dict with keyword arguments for `fn`. |

|     |
| --- |
| Returns |     |
| Merged return value of `fn` across all replicas. |     |

### `colocate_vars_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2596-L2641)

colocate_vars_with(
        colocate_with_variable
    )

Scope that controls which devices variables will be created on.

No operations should be added to the graph inside this scope, it should only be used when creating variables (some implementations work by changing variable creation, others work by using a tf.compat.v1.colocate\_with() scope).

This may only be used inside `self.scope()`.

#### Example usage:

with strategy.scope():
      var1 = tf.Variable(...)
      with strategy.extended.colocate_vars_with(var1):
        # var2 and var3 will be created on the same device(s) as var1
        var2 = tf.Variable(...)
        var3 = tf.Variable(...)
    
      def fn(v1, v2, v3):
        # operates on v1 from var1, v2 from var2, and v3 from var3
    
      # `fn` runs on every device `var1` is on, `var2` and `var3` will be there
      # too.
      strategy.extended.update(var1, fn, args=(var2, var3))

|     |     |
| --- | --- |
| Args |     |
| `colocate_with_variable` | A variable created in this strategy's `scope()`. Variables created while in the returned context manager will be on the same set of devices as `colocate_with_variable`. |

|     |
| --- |
| Returns |     |
| A context manager. |     |

### `experimental_make_numpy_dataset`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3120-L3138)

experimental_make_numpy_dataset(
        numpy_input, session=None
    )

Makes a dataset for input provided via a numpy array.

This avoids adding `numpy_input` as a large constant in the graph, and copies the data to the machine or machines that will be processing the input.

|     |     |
| --- | --- |
| Args |     |
| `numpy_input` | A nest of NumPy input arrays that will be distributed evenly across all replicas. Note that lists of Numpy arrays are stacked, as that is normal [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> behavior. |
| `session` | (TensorFlow v1.x graph execution only) A session used for initialization. |

|     |
| --- |
| Returns |     |
| A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> representing `numpy_input`. |     |

### `experimental_run_steps_on_iterator`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3163-L3209)

experimental_run_steps_on_iterator(
        fn, iterator, iterations=1, initial_loop_values=None
    )

Run `fn` with input from `iterator` for `iterations` times.

This method can be used to run a step function for training a number of times using input from a dataset.

|     |     |
| --- | --- |
| Args |     |
| `fn` | function to run using this distribution strategy. The function must have the following signature: `def fn(context, inputs)`. `context` is an instance of `MultiStepContext` that will be passed when `fn` is run. `context` can be used to specify the outputs to be returned from `fn` by calling `context.set_last_step_output`. It can also be used to capture non tensor outputs by `context.set_non_tensor_output`. See `MultiStepContext` documentation for more information. `inputs` will have same type/structure as `iterator.get_next()`. Typically, `fn` will use `call_for_each_replica` method of the strategy to distribute the computation over multiple replicas. |
| `iterator` | Iterator of a dataset that represents the input for `fn`. The caller is responsible for initializing the iterator as needed. |
| `iterations` | (Optional) Number of iterations that `fn` should be run. Defaults to 1. |
| `initial_loop_values` | (Optional) Initial values to be passed into the loop that runs `fn`. Defaults to `None`. initial\_loop\_values argument when we have a mechanism to infer the outputs of `fn`. |

|     |
| --- |
| Returns |     |
| Returns the `MultiStepContext` object which has the following properties, among other things:<br><br>*   run\_op: An op that runs `fn` `iterations` times.<br>*   last\_step\_outputs: A dictionary containing tensors set using `context.set_last_step_output`. Evaluating this returns the value of the tensors after the last iteration.<br>*   non\_tensor\_outputs: A dictionary containing anything that was set by `fn` by calling `context.set_non_tensor_output`. |     |

### `non_slot_devices`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3313-L3332)

non_slot_devices(
        var_list
    )

Device(s) for non-slot variables.

This method returns non-slot devices where non-slot variables are placed. Users can create non-slot variables on these devices by using a block:

with tf.distribute.StrategyExtended.colocate_vars_with(tf.distribute.StrategyExtended.non_slot_devices(...)):
      ...

|     |     |
| --- | --- |
| Args |     |
| `var_list` | The list of variables being optimized, needed with the default [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br>. |

|     |
| --- |
| Returns |     |
| A sequence of devices for non-slot variables. |     |

### `read_var`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3268-L3281)

read_var(
        v
    )

Reads the value of a variable.

Returns the aggregate value of a replica-local variable, or the (read-only) value of any other variable.

|     |     |
| --- | --- |
| Args |     |
| `v` | A variable allocated within the scope of this [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br>. |

|     |
| --- |
| Returns |     |
| A tensor representing the value of `v`, aggregated across replicas if necessary. |     |

### `reduce_to`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2667-L2753)

reduce_to(
        reduce_op, value, destinations, options=None
    )

Combine (via e.g. sum or mean) values across replicas.

`reduce_to` aggregates [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 and distributed variables. It supports both dense values and [`tf.IndexedSlices`](https://www.tensorflow.org/api_docs/python/tf/IndexedSlices)
.

This API currently can only be called in cross-replica context. Other variants to reduce values across replicas are:

*   [`tf.distribute.StrategyExtended.batch_reduce_to`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#batch_reduce_to)
    : the batch version of this API.
*   [`tf.distribute.ReplicaContext.all_reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#all_reduce)
    : the counterpart of this API in replica context. It supports both batched and non-batched all-reduce.
*   [`tf.distribute.Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#reduce)
    : a more convenient method to reduce to the host in cross-replica context.

`destinations` specifies where to reduce the value to, e.g. "GPU:0". You can also pass in a `Tensor`, and the destinations will be the device of that tensor. For all-reduce, pass the same to `value` and `destinations`.

It can be used in [`tf.distribute.ReplicaContext.merge_call`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReplicaContext#merge_call)
 to write code that works for all [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
.

@tf.function def step\_fn(var):

def merge\_fn(strategy, value, var): # All-reduce the value. Note that `value` here is a # [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
. reduced = strategy.extended.reduce\_to(tf.distribute.ReduceOp.SUM, value, destinations=var) strategy.extended.update(var, lambda var, value: var.assign(value), args=(reduced,))

value = tf.identity(1.) tf.distribute.get\_replica\_context().merge\_call(merge\_fn, args=(value, var))

def run(strategy): with strategy.scope(): v = tf.Variable(0.) strategy.run(step\_fn, args=(v,)) return v

run(tf.distribute.MirroredStrategy(\["GPU:0", "GPU:1"\])) MirroredVariable:{ 0: , 1: } run(tf.distribute.experimental.CentralStorageStrategy( compute\_devices=\["GPU:0", "GPU:1"\], parameter\_device="CPU:0")) run(tf.distribute.OneDeviceStrategy("GPU:0"))

|     |     |
| --- | --- |
| Args |     |
| `reduce_op` | a [`tf.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)<br> value specifying how values should be combined. Allows using string representation of the enum such as "SUM", "MEAN". |
| `value` | a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>, or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> like object. |
| `destinations` | a [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)<br>, a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>, a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> alike object, or a device string. It specifies the devices to reduce to. To perform an all-reduce, pass the same to `value` and `destinations`. Note that if it's a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>, the value is reduced to the devices of that variable, and this method doesn't update the variable. |
| `options` | a [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br>. Options to perform collective operations. This overrides the default options if the [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> takes one in the constructor. See [`tf.distribute.experimental.CommunicationOptions`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationOptions)<br> for details of the options. |

|     |
| --- |
| Returns |     |
| A tensor or value reduced to `destinations`. |     |

### `update`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2932-L3008)

update(
        var, fn, args=(), kwargs=None, group=True
    )

Run `fn` to update `var` using inputs mirrored to the same devices.

[`tf.distribute.StrategyExtended.update`](https://www.tensorflow.org/api_docs/python/tf/distribute/StrategyExtended#update)
 takes a distributed variable `var` to be updated, an update function `fn`, and `args` and `kwargs` for `fn`. It applies `fn` to each component variable of `var` and passes corresponding values from `args` and `kwargs`. Neither `args` nor `kwargs` may contain per-replica values. If they contain mirrored values, they will be unwrapped before calling `fn`. For example, `fn` can be `assign_add` and `args` can be a mirrored DistributedValues where each component contains the value to be added to this mirrored variable `var`. Calling `update` will call `assign_add` on each component variable of `var` with the corresponding tensor value on that device.

#### Example usage:

strategy = tf.distribute.MirroredStrategy(['GPU:0', 'GPU:1']) # With 2
    devices
    with strategy.scope():
      v = tf.Variable(5.0, aggregation=tf.VariableAggregation.SUM)
    def update_fn(v):
      return v.assign(1.0)
    result = strategy.extended.update(v, update_fn)
    # result is
    # Mirrored:{
    #  0: tf.Tensor(1.0, shape=(), dtype=float32),
    #  1: tf.Tensor(1.0, shape=(), dtype=float32)
    # }

If `var` is mirrored across multiple devices, then this method implements logic as following:

results = {}
    for device, v in var:
      with tf.device(device):
        # args and kwargs will be unwrapped if they are mirrored.
        results[device] = fn(v, *args, **kwargs)
    return merged(results)

Otherwise, this method returns `fn(var, *args, **kwargs)` colocated with `var`.

|     |     |
| --- | --- |
| Args |     |
| `var` | Variable, possibly mirrored to multiple devices, to operate on. |
| `fn` | Function to call. Should take the variable as the first argument. |
| `args` | Tuple or list. Additional positional arguments to pass to `fn()`. |
| `kwargs` | Dict with keyword arguments to pass to `fn()`. |
| `group` | Boolean. Defaults to True. If False, the return value will be unwrapped. |

|     |
| --- |
| Returns |     |
| By default, the merged return value of `fn` across all replicas. The merged result has dependencies to make sure that if it is evaluated at all, the side effects (updates) will happen on every replica. If instead "group=False" is specified, this function will return a nest of lists where each list has an element per replica, and the caller is responsible for ensuring all elements are executed. |     |

### `update_non_slot`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3283-L3308)

update_non_slot(
        colocate_with, fn, args=(), kwargs=None, group=True
    )

Runs `fn(*args, **kwargs)` on `colocate_with` devices.

Used to update non-slot variables.

|     |     |
| --- | --- |
| Args |     |
| `colocate_with` | Devices returned by `non_slot_devices()`. |
| `fn` | Function to execute. |
| `args` | Tuple or list. Positional arguments to pass to `fn()`. |
| `kwargs` | Dict with keyword arguments to pass to `fn()`. |
| `group` | Boolean. Defaults to True. If False, the return value will be unwrapped. |

|     |
| --- |
| Returns |     |
| Return value of `fn`, possibly merged across devices. |     |

### `value_container`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L3034-L3047)

value_container(
        value
    )

Returns the container that this per-replica `value` belongs to.

|     |     |
| --- | --- |
| Args |     |
| `value` | A value returned by `run()` or a variable created in `scope()`. |

|     |
| --- |
| Returns |     |
| A container that `value` belongs to. If value does not belong to any container (including the case of container having been destroyed), returns the value itself. `value in experimental_local_results(value_container(value))` will always be true. |     |

### `variable_created_in_scope`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L2570-L2594)

variable_created_in_scope(
        v
    )

Tests whether `v` was created while this strategy scope was active.

Variables created inside the strategy scope are "owned" by it:

    strategy = tf.distribute.MirroredStrategy()

Variables created outside the strategy are not owned by it:

    strategy = tf.distribute.MirroredStrategy()

|     |     |
| --- | --- |
| Args |     |
| `v` | A [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> instance. |

|     |
| --- |
| Returns |     |
| True if `v` was created inside the scope, False if not. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.