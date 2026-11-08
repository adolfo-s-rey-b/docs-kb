[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#arguments)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#methods)
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#compute_loss)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#get_config)
        
    *   [validate\_model\_compatibility](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#validate_model_compatibility)
        
    *   [validate\_outputs](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#validate_outputs)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distillation.LogitsDistillation Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#arguments)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#methods)
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#compute_loss)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#get_config)
        
    *   [validate\_model\_compatibility](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#validate_model_compatibility)
        
    *   [validate\_outputs](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation#validate_outputs)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L260-L390)

Distillation loss that transfers knowledge from final model outputs.

Inherits From: [`DistillationLoss`](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss)

tf.keras.distillation.LogitsDistillation(
        temperature=3.0, loss='kl_divergence'
    )

This distillation loss applies temperature scaling to the teacher's logits before computing the loss between teacher and student predictions. It's the most common approach for knowledge distillation.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `temperature` | Temperature for softmax scaling. Higher values produce softer probability distributions that are easier for the student to learn. Typical values range from 3-5. Defaults to 3.0. |
| `loss` | Loss function to use for distillation. Can be:<br><br>*   String identifier (e.g., 'kl\_divergence', 'categorical\_crossentropy')<br>*   Keras loss instance<br>*   Nested structure of losses matching the model output structure<br>*   `None` to skip distillation for that output (useful for multi-output models where you only want to distill some outputs) At least one loss must be non-`None`. Defaults to 'kl\_divergence'. |

Examlpe(s):

# Basic logits distillation with KL divergence
    distillation_loss = LogitsDistillation(temperature=3.0)
    
    # With categorical crossentropy loss
    distillation_loss = LogitsDistillation(
        temperature=4.0,
        loss="categorical_crossentropy"
    )
    
    # With custom loss instance
    distillation_loss = LogitsDistillation(
        temperature=4.0,
        loss=keras.losses.CategoricalCrossentropy(from_logits=True)
    )
    
    # For multi-output models
    distillation_loss = LogitsDistillation(
        temperature=3.0,
        loss=["kl_divergence", "categorical_crossentropy"]
    )
    
    # For multi-output models, only distill some outputs
    distillation_loss = LogitsDistillation(
        temperature=3.0,
        loss=["kl_divergence", None]  # Skip second output
    )

Methods
-------

### `compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L333-L376)

compute_loss(
        teacher_outputs, student_outputs, **kwargs
    )

Compute distillation loss using the configured loss function.

|     |     |
| --- | --- |
| Arguments |     |
| `teacher_outputs` | Logits from teacher model. Can be a single tensor, list/tuple of tensors, or dict of tensors. |
| `student_outputs` | Logits from student model. Can be a single tensor, list/tuple of tensors, or dict of tensors. |
| `**kwargs` | Additional arguments (ignored). |

|     |
| --- |
| Returns |     |
| Distillation loss tensor. |     |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L385-L390)

@classmethod

Create instance from configuration.

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L378-L383)

get_config()

Get configuration for serialization.

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