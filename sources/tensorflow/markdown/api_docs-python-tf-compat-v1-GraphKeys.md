[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphKeys#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphKeys)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphKeys?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphKeys#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.GraphKeys Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/GraphKeys#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5281-L5422)

Standard names to use for graph collections.

The standard library uses various well-known names to collect and retrieve values associated with a graph. For example, the `tf.Optimizer` subclasses default to optimizing the variables collected under `tf.GraphKeys.TRAINABLE_VARIABLES` if none is specified, but it is also possible to pass an explicit list of variables.

The following standard keys are defined:

*   `GLOBAL_VARIABLES`: the default collection of `Variable` objects, shared across distributed environment (model variables are subset of these). See [`tf.compat.v1.global_variables`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables)
     for more details. Commonly, all `TRAINABLE_VARIABLES` variables will be in `MODEL_VARIABLES`, and all `MODEL_VARIABLES` variables will be in `GLOBAL_VARIABLES`.
*   `LOCAL_VARIABLES`: the subset of `Variable` objects that are local to each machine. Usually used for temporarily variables, like counters.
*   `MODEL_VARIABLES`: the subset of `Variable` objects that are used in the model for inference (feed forward).
*   `TRAINABLE_VARIABLES`: the subset of `Variable` objects that will be trained by an optimizer. See [`tf.compat.v1.trainable_variables`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/trainable_variables)
     for more details.
*   `SUMMARIES`: the summary `Tensor` objects that have been created in the graph. See [`tf.compat.v1.summary.merge_all`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/summary/merge_all)
     for more details.
*   `QUEUE_RUNNERS`: the `QueueRunner` objects that are used to produce input for a computation. See [`tf.compat.v1.train.start_queue_runners`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/start_queue_runners)
     for more details.
*   `MOVING_AVERAGE_VARIABLES`: the subset of `Variable` objects that will also keep moving averages. See [`tf.compat.v1.moving_average_variables`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/moving_average_variables)
     for more details.
*   `REGULARIZATION_LOSSES`: regularization losses collected during graph construction.

The following standard keys are _defined_, but their collections are **not** automatically populated as many of the others are:

*   `WEIGHTS`
*   `BIASES`
*   `ACTIVATIONS`

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| ACTIVATIONS | `'activations'` |
| ASSET\_FILEPATHS | `'asset_filepaths'` |
| BIASES | `'biases'` |
| CONCATENATED\_VARIABLES | `'concatenated_variables'` |
| COND\_CONTEXT | `'cond_context'` |
| EVAL\_STEP | `'eval_step'` |
| GLOBAL\_STEP | `'global_step'` |
| GLOBAL\_VARIABLES | `'variables'` |
| INIT\_OP | `'init_op'` |
| LOCAL\_INIT\_OP | `'local_init_op'` |
| LOCAL\_RESOURCES | `'local_resources'` |
| LOCAL\_VARIABLES | `'local_variables'` |
| LOSSES | `'losses'` |
| METRIC\_VARIABLES | `'metric_variables'` |
| MODEL\_VARIABLES | `'model_variables'` |
| MOVING\_AVERAGE\_VARIABLES | `'moving_average_variables'` |
| QUEUE\_RUNNERS | `'queue_runners'` |
| READY\_FOR\_LOCAL\_INIT\_OP | `'ready_for_local_init_op'` |
| READY\_OP | `'ready_op'` |
| REGULARIZATION\_LOSSES | `'regularization_losses'` |
| RESOURCES | `'resources'` |
| SAVEABLE\_OBJECTS | `'saveable_objects'` |
| SAVERS | `'savers'` |
| SUMMARIES | `'summaries'` |
| SUMMARY\_OP | `'summary_op'` |
| TABLE\_INITIALIZERS | `'table_initializer'` |
| TRAINABLE\_RESOURCE\_VARIABLES | `'trainable_resource_variables'` |
| TRAINABLE\_VARIABLES | `'trainable_variables'` |
| TRAIN\_OP | `'train_op'` |
| UPDATE\_OPS | `'update_ops'` |
| VARIABLES | `'variables'` |
| WEIGHTS | `'weights'` |
| WHILE\_CONTEXT | `'while_context'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.