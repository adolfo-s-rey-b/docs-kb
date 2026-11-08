[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Ftasks%2FQuestionAnsweringTask&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#reduce_aggregated_logs)
        
    *   [set\_preprocessed\_eval\_input\_path](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#set_preprocessed_eval_input_path)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.tasks.QuestionAnsweringTask Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#reduce_aggregated_logs)
        
    *   [set\_preprocessed\_eval\_input\_path](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#set_preprocessed_eval_input_path)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/QuestionAnsweringTask#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L76-L320)

Task object for question answering.

Inherits From: [`Task`](https://www.tensorflow.org/api_docs/python/tfm/core/base_task/Task)

tfm.nlp.tasks.QuestionAnsweringTask(
        params: tfm.core.config_definitions.TaskConfig,
        logging_dir=None,
        name=None
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L265-L281)

aggregate_logs(
        state=None, step_outputs=None
    )

Optional aggregation over logs returned from a validation step.

Given step\_logs from a validation step, this function aggregates the logs after each eval\_step() (see eval\_reduce() function in official/core/base\_trainer.py). It runs on CPU and can be used to aggregate metrics during validation, when there are too many metrics that cannot fit into TPU memory. Note that this may increase latency due to data transfer between TPU and CPU. Also, the step output from a validation step may be a tuple with elements from replicas, and a concatenation of the elements is needed in such case.

|     |     |
| --- | --- |
| Args |     |
| `state` | The current state of training, for example, it can be a sequence of metrics. |
| `step_logs` | Logs from a validation step. Can be a dictionary. |

### `build_inputs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L201-L218)

build_inputs(
        params, input_context=None
    )

Returns tf.data.Dataset for sentence\_prediction task.

### `build_losses`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L117-L130)

build_losses(
        labels, model_outputs, aux_losses=None
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L220-L232)

build_metrics(
        training=None
    )

Gets streaming metrics for training/validation.

### `build_model`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L102-L115)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L242-L249)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L234-L240)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L283-L320)

reduce_aggregated_logs(
        aggregated_logs, global_step=None
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

### `set_preprocessed_eval_input_path`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L98-L100)

set_preprocessed_eval_input_path(
        eval_input_path
    )

Sets the path to the preprocessed eval data.

### `train_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L223-L280)

train_step(
        inputs,
        model: tf_keras.Model,
        optimizer: tf_keras.optimizers.Optimizer,
        metrics=None
    )

Does forward and backward.

With distribution strategies, this method runs on devices.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/question_answering.py#L251-L263)

validation_step(
        inputs, model: tf_keras.Model, metrics=None
    )

Validation step.

With distribution strategies, this method runs on devices.

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