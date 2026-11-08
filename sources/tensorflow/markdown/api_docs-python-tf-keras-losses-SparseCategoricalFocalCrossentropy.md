[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.SparseCategoricalFocalCrossentropy Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalFocalCrossentropy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/losses/losses.py#L1210-L1363)

Computes the sparse categorical focal crossentropy loss.

Inherits From: [`Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)

tf.keras.losses.SparseCategoricalFocalCrossentropy(
        alpha=0.25,
        gamma=2.0,
        from_logits=False,
        ignore_class=None,
        axis=-1,
        reduction='sum_over_batch_size',
        name='sparse_categorical_focal_crossentropy',
        dtype=None
    )

Use this crossentropy loss function when there are two or more label classes and labels are provided as integers. If you want to provide labels using a `one-hot` representation, please use `CategoricalFocalCrossentropy` loss.

Focal loss applies a modulating factor to down-weight easy examples and focus more on hard examples. For each example, the loss is:

`FL(p_t) = -alpha_t * (1 - p_t) ** gamma * log(p_t)`

where `p_t` is the predicted probability of the true class, `gamma` is the focusing parameter, and `alpha_t` is the weight for the true class. When `gamma=0`, there is no focal effect on the crossentropy loss.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `alpha` | A weight balancing factor for all classes. Defaults to `0.25`. It can be a list of floats or a scalar. If a list is provided, it must have the same length as the number of classes. |
| `gamma` | A focusing parameter. Defaults to `2.0`. It gradually reduces the importance given to easy examples. |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, `y_pred` is expected to encode a probability distribution. |
| `ignore_class` | Optional integer. The ID of a class to be ignored during loss computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255). By default (`ignore_class=None`), all classes are considered. |
| `axis` | The axis along which to compute crossentropy (the features axis). Defaults to `-1`. |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the loss instance. |
| `dtype` | The dtype of the loss's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to a different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

#### Examples:

    y_true = np.array([1, 2])

Usage with the `compile()` API:

model.compile(
        optimizer="adam",
        loss=keras.losses.SparseCategoricalFocalCrossentropy(),
    )

An out-of-range, non-ignored label produces a `NaN` loss value. An `alpha` vector with a statically known wrong length raises `ValueError`; if its length or the class dimension is only known at runtime, a mismatch produces `NaN` loss values. This prevents backend-dependent index selection in compiled and symbolic execution, where Keras does not have a portable runtime assertion primitive.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` |     |

Methods
-------

### `call`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/losses/losses.py#L1346-L1350)

call(
        y_true, y_pred
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/losses/losses.py#L70-L74)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/losses/losses.py#L1352-L1363)

get_config()

### `__call__`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/losses/losses.py#L1312-L1344)

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