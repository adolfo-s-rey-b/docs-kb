[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flosses%2FTversky&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.Tversky Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Tversky#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1376-L1441)

Computes the Tversky loss value between `y_true` and `y_pred`.

Inherits From: [`Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)

tf.keras.losses.Tversky(
        alpha=0.5,
        beta=0.5,
        reduction='sum_over_batch_size',
        name='tversky',
        axis=None,
        dtype=None
    )

This loss function is weighted by the alpha and beta coefficients that penalize false positives and false negatives.

With `alpha=0.5` and `beta=0.5`, the loss value becomes equivalent to Dice Loss.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `alpha` | The coefficient controlling incidence of false positives. Defaults to `0.5`. |
| `beta` | The coefficient controlling incidence of false negatives. Defaults to `0.5`. |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the loss instance. |
| `dtype` | The dtype of the loss's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

|     |
| --- |
| Returns<br>------- |     |
| Tversky loss value. |     |

#### Reference:

*   [Salehi et al., 2017](https://arxiv.org/abs/1706.05721)
    

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1436-L1441)

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