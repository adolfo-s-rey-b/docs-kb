[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.tasks.ElectraPretrainTask Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/ElectraPretrainTask#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/electra_task.py#L85-L248)

ELECTRA Pretrain Task (Masked LM + Replaced Token Detection).

Inherits From: [`Task`](https://www.tensorflow.org/api_docs/python/tfm/core/base_task/Task)

tfm.nlp.tasks.ElectraPretrainTask(
        params, logging_dir: Optional[str] = None, name: Optional[str] = None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | the task configuration instance, which can be any of dataclass, ConfigDict, namedtuple, etc. |
| `logging_dir` | a string pointing to where the model, summaries etc. will be saved. You can also write additional stuff in this directory. |
| `name` | the task name. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `logging_dir` |     |
| `task_config` |     |

Methods
-------

### `aggregate_logs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L325-L342)

aggregate_logs(
        state, step_logs
    )

Optional aggregation over logs returned from a validation step.

Given step\_logs from a validation step, this function aggregates the logs after each eval\_step() (see eval\_reduce() function in official/core/base\_trainer.py). It runs on CPU and can be used to aggregate metrics during validation, when there are too many metrics that cannot fit into TPU memory. Note that this may increase latency due to data transfer between TPU and CPU. Also, the step output from a validation step may be a tuple with elements from replicas, and a concatenation of the elements is needed in such case.

|     |     |
| --- | --- |
| Args |     |
| `state` | The current state of training, for example, it can be a sequence of metrics. |
| `step_logs` | Logs from a validation step. Can be a dictionary. |

### `build_inputs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/electra_task.py#L139-L162)

build_inputs(
        params, input_context=None
    )

Returns tf.data.Dataset for pretraining.

### `build_losses`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/electra_task.py#L92-L137)

build_losses(
        labels, model_outputs, metrics, aux_losses=None
    ) -> tf.Tensor

Standard interface to compute losses.

|     |     |
| --- | --- |
| Args |     |
| `labels` | optional label tensors. |
| `model_outputs` | a nested structure of output tensors. |
| `aux_losses` | auxiliary loss tensors, i.e. `losses` in keras.Model. |

|     |
| --- |
| Returns |     |
| The total loss tensor. |     |

### `build_metrics`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/electra_task.py#L164-L181)

build_metrics(
        training=None
    )

Gets streaming metrics for training/validation.

### `build_model`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/electra_task.py#L89-L90)

build_model()

\[Optional\] Creates model architecture.

|     |
| --- |
| Returns |     |
| A model instance. |     |

### `create_optimizer`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L72-L111)

@classmethod

Creates an TF optimizer from configurations.

|     |     |
| --- | --- |
| Args |     |
| `optimizer_config` | the parameters of the Optimization settings. |
| `runtime_config` | the parameters of the runtime. |
| `dp_config` | the parameter of differential privacy. |

|     |
| --- |
| Returns |     |
| A tf.optimizers.Optimizer object. |     |

### `inference_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L311-L323)

inference_step(
        inputs, model: tf_keras.Model
    )

Performs the forward step.

With distribution strategies, this method runs on devices.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | a dictionary of input tensors. |
| `model` | the keras.Model. |

|     |
| --- |
| Returns |     |
| Model outputs. |     |

### `initialize`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L113-L142)

initialize(
        model: tf_keras.Model
    )

\[Optional\] A callback function used as CheckpointManager's init\_fn.

This function will be called when no checkpoint is found for the model. If there is a checkpoint, the checkpoint will be loaded and this function will not be called. You can use this callback function to load a pretrained checkpoint, saved under a directory other than the model\_dir.

|     |     |
| --- | --- |
| Args |     |
| `model` | The keras.Model built or used by this task. |

### `process_compiled_metrics`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L210-L221)

process_compiled_metrics(
        compiled_metrics, labels, model_outputs
    )

Process and update compiled\_metrics.

call when using compile/fit API.

|     |     |
| --- | --- |
| Args |     |
| `compiled_metrics` | the compiled metrics (model.compiled\_metrics). |
| `labels` | a tensor or a nested structure of tensors. |
| `model_outputs` | a tensor or a nested structure of tensors. For example, output of the keras model built by self.build\_model. |

### `process_metrics`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/electra_task.py#L183-L198)

process_metrics(
        metrics, labels, model_outputs
    )

Process and update metrics.

Called when using custom training loop API.

|     |     |
| --- | --- |
| Args |     |
| `metrics` | a nested structure of metrics objects. The return of function self.build\_metrics. |
| `labels` | a tensor or a nested structure of tensors. |
| `model_outputs` | a tensor or a nested structure of tensors. For example, output of the keras model built by self.build\_model. |
| `**kwargs` | other args. |

### `reduce_aggregated_logs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L344-L360)

reduce_aggregated_logs(
        aggregated_logs, global_step: Optional[tf.Tensor] = None
    )

Optional reduce of aggregated logs over validation steps.

This function reduces aggregated logs at the end of validation, and can be used to compute the final metrics. It runs on CPU and in each eval\_end() in base trainer (see eval\_end() function in official/core/base\_trainer.py).

|     |     |
| --- | --- |
| Args |     |
| `aggregated_logs` | Aggregated logs over multiple validation steps. |
| `global_step` | An optional variable of global step. |

|     |
| --- |
| Returns |     |
| A dictionary of reduced results. |     |

### `train_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/electra_task.py#L200-L228)

train_step(
        inputs,
        model: tf_keras.Model,
        optimizer: tf_keras.optimizers.Optimizer,
        metrics
    )

Does forward and backward.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | a dictionary of input tensors. |
| `model` | the model, forward pass definition. |
| `optimizer` | the optimizer for this training step. |
| `metrics` | a nested structure of metrics objects. |

|     |
| --- |
| Returns |     |
| A dictionary of logs. |     |

### `validation_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/electra_task.py#L230-L248)

validation_step(
        inputs, model: tf_keras.Model, metrics
    )

Validatation step.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | a dictionary of input tensors. |
| `model` | the keras.Model. |
| `metrics` | a nested structure of metrics objects. |

|     |
| --- |
| Returns |     |
| A dictionary of logs. |     |

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| loss | `'loss'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.