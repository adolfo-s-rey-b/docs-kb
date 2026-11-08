[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.CategoricalFocalCrossentropy Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalFocalCrossentropy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1019-L1170)

Computes the alpha balanced focal crossentropy loss.

Inherits From: [`Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)

tf.keras.losses.CategoricalFocalCrossentropy(
        alpha=0.25,
        gamma=2.0,
        from_logits=False,
        label_smoothing=0.0,
        axis=-1,
        reduction='sum_over_batch_size',
        name='categorical_focal_crossentropy',
        dtype=None
    )

Use this crossentropy loss function when there are two or more label classes and if you want to handle class imbalance without using `class_weights`. We expect labels to be provided in a `one_hot` representation.

According to [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)
, it helps to apply a focal factor to down-weight easy examples and focus more on hard examples. The general formula for the focal loss (FL) is as follows:

`FL(p_t) = (1 - p_t) ** gamma * log(p_t)`

where `p_t` is defined as follows: `p_t = output if y_true == 1, else 1 - output`

`(1 - p_t) ** gamma` is the `modulating_factor`, where `gamma` is a focusing parameter. When `gamma` = 0, there is no focal effect on the cross entropy. `gamma` reduces the importance given to simple examples in a smooth manner.

The authors use alpha-balanced variant of focal loss (FL) in the paper: `FL(p_t) = -alpha * (1 - p_t) ** gamma * log(p_t)`

where `alpha` is the weight factor for the classes. If `alpha` = 1, the loss won't be able to handle class imbalance properly as all classes will have the same weight. This can be a constant or a list of constants. If alpha is a list, it must have the same length as the number of classes.

The formula above can be generalized to: `FL(p_t) = alpha * (1 - p_t) ** gamma * CrossEntropy(y_true, y_pred)`

where minus comes from `CrossEntropy(y_true, y_pred)` (CE).

Extending this to multi-class case is straightforward: `FL(p_t) = alpha * (1 - p_t) ** gamma * CategoricalCE(y_true, y_pred)`

In the snippet below, there is `num_classes` floating pointing values per example. The shape of both `y_pred` and `y_true` are `(batch_size, num_classes)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `alpha` | A weight balancing factor for all classes, default is `0.25` as mentioned in the reference. It can be a list of floats or a scalar. In the multi-class case, alpha may be set by inverse class frequency by using `compute_class_weight` from `sklearn.utils`. |
| `gamma` | A focusing parameter, default is `2.0` as mentioned in the reference. It helps to gradually reduce the importance given to simple (easy) examples in a smooth manner. |
| `from_logits` | Whether `output` is expected to be a logits tensor. By default, we consider that `output` encodes a probability distribution. |
| `label_smoothing` | Float in \[0, 1\]. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels. |
| `axis` | The axis along which to compute crossentropy (the features axis). Defaults to `-1`. |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the loss instance. |
| `dtype` | The dtype of the loss's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

#### Examples:

#### Standalone usage:

    y_true = [[0., 1., 0.], [0., 0., 1.]]

    # Calling with 'sample_weight'.

    # Using 'sum' reduction type.

    # Using 'none' reduction type.

Usage with the `compile()` API:

model.compile(optimizer='adam',
                  loss=keras.losses.CategoricalFocalCrossentropy())

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1159-L1170)

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