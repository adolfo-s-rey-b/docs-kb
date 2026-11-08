[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Ftasks%2FTaggingTask&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.tasks.TaggingTask Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/tasks/TaggingTask#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/tagging.py#L81-L205)

Task object for tagging (e.g., NER or POS).

Inherits From: [`Task`](https://www.tensorflow.org/api_docs/python/tfm/core/base_task/Task)

tfm.nlp.tasks.TaggingTask(
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/tagging.py#L172-L190)

aggregate_logs(
        state=None, step_outputs=None
    )

Aggregates over logs returned from a validation step.

### `build_inputs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/tagging.py#L114-L139)

build_inputs(
        params: tfm.core.config_definitions.DataConfig,
        input_context=None
    )

Returns tf.data.Dataset for sentence\_prediction task.

### `build_losses`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/tagging.py#L104-L112)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L189-L192)

build_metrics(
        training: bool = True
    )

Gets streaming metrics for training/validation.

### `build_model`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/tagging.py#L85-L102)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/tagging.py#L141-L145)

inference_step(
        inputs, model: tf_keras.Model
    )

Performs the forward step.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/base_task.py#L194-L208)

process_metrics(
        metrics, labels, model_outputs, **kwargs
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/tagging.py#L192-L205)

reduce_aggregated_logs(
        aggregated_logs, global_step=None
    )

Reduces aggregated logs over validation steps.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/tasks/tagging.py#L147-L170)

validation_step(
        inputs, model: tf_keras.Model, metrics=None
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