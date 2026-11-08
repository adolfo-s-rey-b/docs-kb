[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.MaskRCNNTask Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#methods)
    *   [aggregate\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#aggregate_logs)
        
    *   [build\_inputs](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#build_inputs)
        
    *   [build\_losses](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#build_losses)
        
    *   [build\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#build_metrics)
        
    *   [build\_model](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#build_model)
        
    *   [create\_optimizer](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#create_optimizer)
        
    *   [inference\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#inference_step)
        
    *   [initialize](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#initialize)
        
    *   [process\_compiled\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#process_compiled_metrics)
        
    *   [process\_metrics](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#process_metrics)
        
    *   [reduce\_aggregated\_logs](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#reduce_aggregated_logs)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#train_step)
        
    *   [validation\_step](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#validation_step)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L65-L643)

A single-replica view of training procedure.

Inherits From: [`Task`](https://www.tensorflow.org/api_docs/python/tfm/core/base_task/Task)

#### View aliases

**Main aliases**

[`tfm.vision.maskrcnn.MaskRCNNTask`](https://www.tensorflow.org/api_docs/python/tfm/vision/MaskRCNNTask)

tfm.vision.MaskRCNNTask(
        params, logging_dir: Optional[str] = None, name: Optional[str] = None
    )

Mask R-CNN task provides artifacts for training/evalution procedures, including loading/iterating over Datasets, initializing the model, calculating the loss, post-processing, and customized metrics with reduction.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L528-L566)

aggregate_logs(
        state: Optional[Any] = None, step_outputs: Optional[Dict[str, Any]] = None
    ) -> Optional[Any]

Optional aggregation over logs returned from a validation step.

### `build_inputs`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L131-L188)

build_inputs(
        params: tfm.vision.configs.maskrcnn.DataConfig,
        input_context: Optional[tf.distribute.InputContext] = None,
        dataset_fn: Optional[dataset_fn_lib.PossibleDatasetType] = None
    ) -> tf.data.Dataset

Builds input dataset.

### `build_losses`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L266-L302)

build_losses(
        outputs: Mapping[str, Any],
        labels: Mapping[str, Any],
        aux_losses: Optional[Any] = None
    ) -> Dict[str, tf.Tensor]

Builds Mask R-CNN losses.

### `build_metrics`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L339-L388)

build_metrics(
        training: bool = True
    )

Builds detection metrics.

### `build_model`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L74-L100)

build_model()

Builds Mask R-CNN model.

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L102-L129)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L616-L643)

reduce_aggregated_logs(
        aggregated_logs: Dict[str, Any], global_step: Optional[tf.Tensor] = None
    ) -> Dict[str, tf.Tensor]

Optional reduce of aggregated logs over validation steps.

### `train_step`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L390-L448)

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/tasks/maskrcnn.py#L493-L526)

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