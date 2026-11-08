[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.SemanticSegmentationTask Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L35-L376)

A task for semantic segmentation.

Inherits From: [`Task`](https://www.tensorflow.org/api_docs/python/tfm/core/base_task/Task)

#### View aliases

**Main aliases**

[`tfm.vision.semantic_segmentation.SemanticSegmentationTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/SemanticSegmentationTask)

tfm.vision.SemanticSegmentationTask(
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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L340-L356)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L89-L129)

build_inputs(
        params: tfm.vision.configs.semantic_segmentation.DataConfig,
        input_context: Optional[tf.distribute.InputContext] = None
    )

Builds classification input.

### `build_losses`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L131-L170)

build_losses(
        labels: Mapping[str, tf.Tensor],
        model_outputs: Union[Mapping[str, tf.Tensor], tf.Tensor],
        aux_losses: Optional[Any] = None
    )

Segmentation loss.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L194-L224)

build_metrics(
        training: bool = True
    )

Gets streaming metrics for training/validation.

### `build_model`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L39-L59)

build_model()

Builds segmentation model.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L336-L338)

inference_step(
        inputs: tf.Tensor, model: tf_keras.Model
    )

Performs the forward step.

### `initialize`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L61-L87)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L172-L192)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L358-L376)

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

### `train_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L226-L284)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/semantic_segmentation.py#L286-L334)

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