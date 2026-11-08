[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#arguments)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#methods)
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#compute_loss)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#get_config)
        
    *   [validate\_model\_compatibility](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#validate_model_compatibility)
        
    *   [validate\_outputs](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#validate_outputs)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distillation.FeatureDistillation Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#arguments)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#methods)
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#compute_loss)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#get_config)
        
    *   [validate\_model\_compatibility](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#validate_model_compatibility)
        
    *   [validate\_outputs](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation#validate_outputs)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L86-L257)

Feature distillation loss.

Inherits From: [`DistillationLoss`](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/DistillationLoss)

tf.keras.distillation.FeatureDistillation(
        loss='mse', teacher_layer_name=None, student_layer_name=None
    )

Feature distillation transfers knowledge from intermediate layers of the teacher model to corresponding layers of the student model. This approach helps the student learn better internal representations and often leads to better performance compared to logits-only distillation.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `loss` | Loss function to use for feature distillation. Can be:<br><br>*   String identifier (e.g., 'mse', 'cosine\_similarity', 'mae')<br>*   Keras loss instance<br>*   Nested structure of losses matching the layer output structure<br>*   `None` to skip distillation for that output (useful for multi-output models where you only want to distill some outputs) At least one loss must be non-`None`. Defaults to 'mse'. |
| `teacher_layer_name` | Name of the teacher layer to extract features from. If `None`, uses the final output. Defaults to `None`. |
| `student_layer_name` | Name of the student layer to extract features from. If `None`, uses the final output. Defaults to `None`. |

Examlpe(s):

# Basic feature distillation from final outputs
    distillation_loss = FeatureDistillation(loss="mse")
    
    # Distill from specific intermediate layers
    distillation_loss = FeatureDistillation(
        loss="mse",
        teacher_layer_name="dense_1",
        student_layer_name="dense_1"
    )
    
    # Use cosine similarity for different feature sizes
    distillation_loss = FeatureDistillation(
        loss="cosine_similarity",
        teacher_layer_name="conv2d_2",
        student_layer_name="conv2d_1"
    )
    
    # With custom loss instance
    distillation_loss = FeatureDistillation(
        loss=keras.losses.MeanAbsoluteError()
    )
    
    # For multi-output models
    distillation_loss = FeatureDistillation(
        loss=["mse", "cosine_similarity"]
    )
    
    # For multi-output models, only distill some outputs
    distillation_loss = FeatureDistillation(
        loss=["mse", None, "cosine_similarity"]  # Skip middle output
    )

Methods
-------

### `compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L218-L242)

compute_loss(
        teacher_outputs, student_outputs, **kwargs
    )

Compute feature distillation loss using extracted features.

|     |     |
| --- | --- |
| Arguments |     |
| `teacher_outputs` | Extracted features from teacher layer. |
| `student_outputs` | Extracted features from student layer. |
| `**kwargs` | Additional arguments (ignored). |

|     |
| --- |
| Returns |     |
| Scalar distillation loss tensor. |     |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L252-L257)

@classmethod

Create instance from configuration.

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L244-L250)

get_config()

Get configuration for serialization.

### `validate_model_compatibility`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L160-L202)

validate_model_compatibility(
        teacher, student
    )

Validate that teacher and student models are compatible for feature distillation.

### `validate_outputs`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distillation_loss.py#L204-L216)

validate_outputs(
        teacher_outputs, student_outputs
    )

Validate that outputs are compatible for feature distillation.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.