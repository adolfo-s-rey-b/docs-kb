[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.BinaryFocalCrossentropy Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryFocalCrossentropy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L727-L912)

Computes focal cross-entropy loss between true labels and predictions.

Inherits From: [`Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)

tf.keras.losses.BinaryFocalCrossentropy(
        apply_class_balancing=False,
        alpha=0.25,
        gamma=2.0,
        from_logits=False,
        label_smoothing=0.0,
        axis=-1,
        reduction='sum_over_batch_size',
        name='binary_focal_crossentropy',
        dtype=None
    )

Binary cross-entropy loss is often used for binary (0 or 1) classification tasks. The loss function requires the following inputs:

*   `y_true` (true label): This is either 0 or 1.
*   `y_pred` (predicted value): This is the model's prediction, i.e, a single floating-point value which either represents a [logit](https://en.wikipedia.org/wiki/Logit)
    , (i.e, value in \[-inf, inf\] when `from_logits=True`) or a probability (i.e, value in `[0., 1.]` when `from_logits=False`).

According to [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)
, it helps to apply a "focal factor" to down-weight easy examples and focus more on hard examples. By default, the focal tensor is computed as follows:

`focal_factor = (1 - output) ** gamma` for class 1 `focal_factor = output ** gamma` for class 0 where `gamma` is a focusing parameter. When `gamma=0`, this function is equivalent to the binary crossentropy loss.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `apply_class_balancing` | A bool, whether to apply weight balancing on the binary classes 0 and 1. |
| `alpha` | A weight balancing factor for class 1, default is `0.25` as mentioned in reference [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)<br>. The weight for class 0 is `1.0 - alpha`. |
| `gamma` | A focusing parameter used to compute the focal factor, default is `2.0` as mentioned in the reference [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)<br>. |
| `from_logits` | Whether to interpret `y_pred` as a tensor of [logit](https://en.wikipedia.org/wiki/Logit)<br> values. By default, we assume that `y_pred` are probabilities (i.e., values in `[0, 1]`). |
| `label_smoothing` | Float in `[0, 1]`. When `0`, no smoothing occurs. When > `0`, we compute the loss between the predicted labels and a smoothed version of the true labels, where the smoothing squeezes the labels towards `0.5`. Larger values of `label_smoothing` correspond to heavier smoothing. |
| `axis` | The axis along which to compute crossentropy (the features axis). Defaults to `-1`. |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the loss instance. |
| `dtype` | The dtype of the loss's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

#### Examples:

With the `compile()` API:

model.compile(
        loss=keras.losses.BinaryFocalCrossentropy(
            gamma=2.0, from_logits=True),
        ...
    )

As a standalone function:

    # Example 1: (batch_size = 1, number of samples = 4)

    # Apply class weight

    # Example 2: (batch_size = 2, number of samples = 4)

    # Apply class weight

    # Using 'sample_weight' attribute with focal effect

    # Apply class weight

    # Using 'sum' reduction` type.

    # Apply class weight

    # Using 'none' reduction type.

    # Apply class weight

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` |     |

Methods
-------

### `call`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L28-L34)

call(
        y_true, y_pred
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L42-L46)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L900-L912)

get_config()

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/loss.py#L56-L85)

__call__(
        y_true, y_pred, sample_weight=None
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.