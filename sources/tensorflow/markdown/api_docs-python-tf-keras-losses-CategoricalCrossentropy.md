[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flosses%2FCategoricalCrossentropy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.CategoricalCrossentropy Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L915-L1016)

Computes the crossentropy loss between the labels and predictions.

Inherits From: [`Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)

tf.keras.losses.CategoricalCrossentropy(
        from_logits=False,
        label_smoothing=0.0,
        axis=-1,
        reduction='sum_over_batch_size',
        name='categorical_crossentropy',
        dtype=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging) | *   [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)<br>    <br>*   [Retraining an Image Classifier](https://www.tensorflow.org/hub/tutorials/tf2_image_retraining)<br>    <br>*   [Implement Differential Privacy with TensorFlow Privacy](https://www.tensorflow.org/responsible_ai/privacy/tutorials/classification_privacy)<br>    <br>*   [Assess privacy risks with the TensorFlow Privacy Report](https://www.tensorflow.org/responsible_ai/privacy/tutorials/privacy_report)<br>    <br>*   [On-Device Training with TensorFlow Lite](https://www.tensorflow.org/lite/examples/on_device_training/overview) |

Use this crossentropy loss function when there are two or more label classes. We expect labels to be provided in a `one_hot` representation. If you want to provide labels as integers, please use `SparseCategoricalCrossentropy` loss. There should be `num_classes` floating point values per feature, i.e., the shape of both `y_pred` and `y_true` are `[batch_size, num_classes]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `label_smoothing` | Float in \[0, 1\]. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels. |
| `axis` | The axis along which to compute crossentropy (the features axis). Defaults to `-1`. |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the loss instance. |
| `dtype` | The dtype of the loss's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

#### Examples:

#### Standalone usage:

    y_true = np.array([[0, 1, 0], [0, 0, 1]])

    # Calling with 'sample_weight'.

    # Using 'sum' reduction type.

    # Using 'none' reduction type.

Usage with the `compile()` API:

model.compile(optimizer='sgd',
                  loss=keras.losses.CategoricalCrossentropy())

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1007-L1016)

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