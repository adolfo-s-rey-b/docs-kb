[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.VideoClassificationTask Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L30-L369)

A task for video classification.

Inherits From: [`Task`](https://www.tensorflow.org/api_docs/python/tfm/core/base_task/Task)

#### View aliases

**Main aliases**

[`tfm.vision.video_classification.VideoClassificationTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/VideoClassificationTask)

tfm.vision.VideoClassificationTask(
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L126-L157)

build_inputs(
        params: tfm.vision.configs.video_classification.DataConfig,
        input_context: Optional[tf.distribute.InputContext] = None
    )

Builds classification input.

### `build_losses`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L159-L207)

build_losses(
        labels: Any, model_outputs: Any, aux_losses: Optional[Any] = None
    )

Sparse categorical cross entropy loss.

|     |     |
| --- | --- |
| Args |     |
| `labels` | labels. |
| `model_outputs` | Output logits of the classifier. |
| `aux_losses` | auxiliarly loss tensors, i.e. `losses` in keras.Model. |

|     |
| --- |
| Returns |     |
| The total loss tensor. |     |

### `build_metrics`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L209-L239)

build_metrics(
        training: bool = True
    )

Gets streaming metrics for training/validation.

### `build_model`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L57-L80)

build_model()

Builds video classification model.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L357-L369)

inference_step(
        features: tf.Tensor, model: tf_keras.Model
    )

Performs the forward step.

### `initialize`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L82-L105)

initialize(
        model: tf_keras.Model
    )

Loads pretrained checkpoint.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L241-L255)

process_metrics(
        metrics: List[Any], labels: Any, model_outputs: Any
    )

Process and update metrics.

Called when using custom training loop API.

|     |     |
| --- | --- |
| Args |     |
| `metrics` | a nested structure of metrics objects. The return of function self.build\_metrics. |
| `labels` | a tensor or a nested structure of tensors. |
| `model_outputs` | a tensor or a nested structure of tensors. For example, output of the keras model built by self.build\_model. |

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L257-L321)

train_step(
        inputs: Tuple[Any, Any],
        model: tf_keras.Model,
        optimizer: tf_keras.optimizers.Optimizer,
        metrics: Optional[List[Any]] = None
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/video_classification.py#L323-L355)

validation_step(
        inputs: Tuple[Any, Any],
        model: tf_keras.Model,
        metrics: Optional[List[Any]] = None
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