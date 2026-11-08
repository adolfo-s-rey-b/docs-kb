[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#methods)
    *   [coordinator\_for\_async](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#coordinator_for_async)
        
    *   [create\_eval\_loop\_fn](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#create_eval_loop_fn)
        
    *   [create\_train\_loop\_fn](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#create_train_loop_fn)
        
    *   [distribute\_dataset](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#distribute_dataset)
        
    *   [eval\_begin](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#eval_begin)
        
    *   [eval\_end](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#eval_end)
        
    *   [eval\_reduce](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#eval_reduce)
        
    *   [eval\_step](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#eval_step)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#evaluate)
        
    *   [init\_async](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#init_async)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#initialize)
        
    *   [join](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#join)
        
    *   [next\_eval\_inputs](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#next_eval_inputs)
        
    *   [next\_train\_inputs](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#next_train_inputs)
        
    *   [train](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#train)
        
    *   [train\_loop\_begin](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#train_loop_begin)
        
    *   [train\_loop\_end](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#train_loop_end)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#train_step)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.base\_trainer.Trainer Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#methods)
    *   [coordinator\_for\_async](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#coordinator_for_async)
        
    *   [create\_eval\_loop\_fn](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#create_eval_loop_fn)
        
    *   [create\_train\_loop\_fn](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#create_train_loop_fn)
        
    *   [distribute\_dataset](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#distribute_dataset)
        
    *   [eval\_begin](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#eval_begin)
        
    *   [eval\_end](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#eval_end)
        
    *   [eval\_reduce](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#eval_reduce)
        
    *   [eval\_step](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#eval_step)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#evaluate)
        
    *   [init\_async](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#init_async)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#initialize)
        
    *   [join](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#join)
        
    *   [next\_eval\_inputs](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#next_eval_inputs)
        
    *   [next\_train\_inputs](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#next_train_inputs)
        
    *   [train](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#train)
        
    *   [train\_loop\_begin](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#train_loop_begin)
        
    *   [train\_loop\_end](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#train_loop_end)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/core/base_trainer/Trainer#train_step)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L136-L498)

Implements the common trainer shared for TensorFlow models.

tfm.core.base_trainer.Trainer(
        config: tfm.core.base_trainer.ExperimentConfig,
        task: tfm.core.base_task.Task,
        model: tf_keras.Model,
        optimizer: tf.optimizers.Optimizer,
        train: bool = True,
        evaluate: bool = True,
        train_dataset: Optional[Union[tf.data.Dataset, tf.distribute.DistributedDataset]] = None,
        validation_dataset: Optional[Union[tf.data.Dataset, tf.distribute.DistributedDataset]] = None,
        checkpoint_exporter=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `config` | An `ExperimentConfig` instance specifying experiment config. |
| `task` | A base\_task.Task instance. |
| `model` | The model instance, e.g. a tf\_keras.Model instance. |
| `optimizer` | tf.optimizers.Optimizer instance. |
| `train` | bool, whether or not this trainer will be used for training. default to True. |
| `evaluate` | bool, whether or not this trainer will be used for evaluation. default to True. |
| `train_dataset` | a dataset object created for training. With tf.distribute, it needs to be a `DistributedDataset`. |
| `validation_dataset` | a dataset object created for evaluation. With tf.distribute, it needs to be a `DistributedDataset`. The evaluator will create a dataset iterator for each eval round, so the dataset does not need to repeat. |
| `checkpoint_exporter` | an object that has the `maybe_export_checkpoint` interface. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint` | Accesses the training checkpoint. |
| `checkpoint_exporter` | Accesses the checkpoint exporter. |
| `config` |     |
| `eval_dataset` | The current evaluation dataset. |
| `global_step` |     |
| `model` |     |
| `optimizer` |     |
| `strategy` |     |
| `task` |     |
| `train_dataset` | The current training dataset. |
| `train_loss` | Accesses the training loss metric object. |
| `train_metrics` | Accesses all training metric objects. |
| `validation_loss` | Accesses the validation loss metric object. |
| `validation_metrics` | Accesses all validation metric metric objects. |

Methods
-------

### `coordinator_for_async`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L50-L57)

coordinator_for_async() -> tf.distribute.experimental.coordinator.ClusterCoordinator

### `create_eval_loop_fn`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L78-L96)

create_eval_loop_fn(
        has_state: bool
    )

Creates a training loop from the given step function and options.

### `create_train_loop_fn`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L64-L76)

create_train_loop_fn()

Creates a eval loop from the given step function and options.

### `distribute_dataset`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L98-L123)

distribute_dataset(
        dataset_or_fn, *args, **kwargs
    )

A utility function to help create a [`tf.distribute.DistributedDataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedDataset)
.

|     |     |
| --- | --- |
| Args |     |
| `dataset_or_fn` | A instance of [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, or a "dataset function" returning a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>. If it is a function, it may optionally have an argument named `input_context` which will be passed a [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)<br> instance. |
| `*args` | Any positional arguments to pass through to `dataset_or_fn`. |
| `**kwargs` | Any keyword arguments to pass through to `dataset_or_fn`. |

|     |
| --- |
| Returns |     |
| A distributed Dataset. |     |

### `eval_begin`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L402-L409)

eval_begin()

Sets up metrics.

### `eval_end`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L465-L495)

eval_end(
        aggregated_logs=None
    )

Processes evaluation results.

### `eval_reduce`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L497-L498)

eval_reduce(
        state=None, step_outputs=None
    )

A function to perform per-step reduction on the evaluation outputs.

This is useful for passing state throughout evaluation, especially in cases where maintaining or accumulating state is hard to accomplish using `tf.metrics.Metric` or other [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
\-based approaches. For instance, it can be used to easily accumulate all per-example losses from the full evaluation for subsequent processing in `eval_end()`.

|     |     |
| --- | --- |
| Args |     |
| `state` | A state being maintained throughout the evaluation. |
| `step_outputs` | Outputs from the current evaluation step. |

|     |
| --- |
| Returns |     |
| An output which is passed as the `state` argument to this function for the next step. After evaluation is finished, the output from last step will be passed to `eval_end`. |     |

### `eval_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L436-L463)

eval_step(
        iterator
    )

See base class.

### `evaluate`

evaluate(
        num_steps: tf.Tensor
    ) -> Optional[runner.Output]

Implements `num_steps` steps of evaluation.

|     |     |
| --- | --- |
| Args |     |
| `num_steps` | The number of evaluation steps to run. When this is -1, evaluation proceeds until a call to `eval_step` raises a `StopIteration` or [`tf.errors.OutOfRangeError`](https://www.tensorflow.org/api_docs/python/tf/errors/OutOfRangeError)<br>. |

|     |
| --- |
| Returns |     |
| The output of `self.eval_end()`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If `options.use_tf_while_loop` is `True` and `num_steps` is unspecified. |

### `init_async`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L39-L48)

init_async()

Initializes the Async Trainer base class.

### `initialize`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L322-L330)

initialize()

A callback function.

This function will be called when no checkpoint found for the model. If there is a checkpoint, the checkpoint will be loaded and this function will not be called. Tasks may use this callback function to load a pretrained checkpoint, saved under a directory other than the model\_dir.

### `join`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L59-L62)

join()

Join all async steps. Only useful in aysnc training.

### `next_eval_inputs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L411-L434)

next_eval_inputs(
        iterator
    )

Fetches the next inputs for the model during eval.

This method consumes the input iterator and returns the next inputs for the model and an additional logs dict. The output dict remains in the host (not sent to GPUs/TPUs) and is merged with the model outputs which will be processed later in `aggregate_logs`. This is useful for sending extra logs downstream that are not compatible with the accelerators.

|     |     |
| --- | --- |
| Args |     |
| `iterator` | Dataset iterator to generate the next inputs from. |

|     |
| --- |
| Returns |     |
| The inputs to the model, and an additional logs dictionnary. The logs are not passed to the model, instead they are merged with model output logs. |     |

### `next_train_inputs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L361-L381)

next_train_inputs(
        iterator
    )

Fetches the next inputs for the model during train.

This method consumes the input iterator and returns the next inputs for the model.

This method provides a way to control how to fetch the next model input, and what data to send to the model.

|     |     |
| --- | --- |
| Args |     |
| `iterator` | Dataset iterator to generate the next inputs from. |

|     |
| --- |
| Returns |     |
| The inputs to the model. |     |

### `train`

train(
        num_steps: tf.Tensor
    ) -> Optional[runner.Output]

Implements `num_steps` steps of training.

|     |     |
| --- | --- |
| Args |     |
| `num_steps` | The number of training steps to run. This corresponds directly to the number of calls made to `train_step`. |

|     |
| --- |
| Returns |     |
| The output of `train_loop_end`. |     |

### `train_loop_begin`

train_loop_begin()

Called once at the beginning of the training loop.

This method is always called in eager mode, and is a good place to reset metrics that accumulate values over multiple steps of training.

Note that this method is called before dataset iterator creation.

### `train_loop_end`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L342-L359)

train_loop_end()

See base class.

### `train_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_trainer.py#L383-L400)

train_step(
        iterator
    )

See base class.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.