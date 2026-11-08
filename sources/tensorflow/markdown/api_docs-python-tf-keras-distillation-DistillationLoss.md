[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdistillation%2FDistillationLoss&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#methods)
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#compute_loss)
        
    *   [validate\_model\_compatibility](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#validate_model_compatibility)
        
    *   [validate\_outputs](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#validate_outputs)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distillation.DistillationLoss Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#methods)
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#compute_loss)
        
    *   [validate\_model\_compatibility](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#validate_model_compatibility)
        
    *   [validate\_outputs](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss#validate_outputs)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L32-L83)

Base class for distillation loss computation.

Distillation losses define how to compute the distillation loss between teacher and student outputs. Each loss implements a specific approach to knowledge transfer, from simple logits matching to feature-based distillation.

To create custom distillation losses, subclass this class and override the `compute_loss` method.

Methods
-------

### `compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L45-L60)

compute_loss(
        teacher_outputs, student_outputs, **kwargs
    )

Compute distillation loss between teacher and student outputs.

This method should implement the specific distillation logic for transferring knowledge from teacher to student.

|     |     |
| --- | --- |
| Arguments |     |
| `teacher_outputs` | Outputs from the teacher model. Can be a single tensor or a list/tuple of tensors for multi-output models. |
| `student_outputs` | Outputs from the student model. Can be a single tensor or a list/tuple of tensors for multi-output models. |
| `**kwargs` | Additional arguments for custom distillation\_loss. |

|     |
| --- |
| Returns |     |
| Distillation loss tensor. |     |

### `validate_model_compatibility`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L73-L83)

validate_model_compatibility(
        teacher, student
    )

Validate that teacher and student models are compatible.

|     |     |
| --- | --- |
| Arguments |     |
| `teacher` | The teacher model. |
| `student` | The student model. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If models are not compatible with this distillation loss. |

### `validate_outputs`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L62-L71)

validate_outputs(
        teacher_outputs, student_outputs
    )

Validate that teacher and student outputs are compatible.

|     |     |
| --- | --- |
| Arguments |     |
| `teacher_outputs` | Outputs from the teacher model. |
| `student_outputs` | Outputs from the student model. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If outputs are not compatible. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.