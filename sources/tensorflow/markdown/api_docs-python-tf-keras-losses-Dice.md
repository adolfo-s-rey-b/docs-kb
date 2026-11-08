[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Dice#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.Dice Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1302-L1373)

Computes the Dice loss value between `y_true` and `y_pred`.

Inherits From: [`Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)

tf.keras.losses.Dice(
        reduction='sum_over_batch_size',
        name='dice',
        axis=None,
        dtype=None
    )

#### Formula:

loss = 1 - (2 * sum(y_true * y_pred)) / (sum(y_true) + sum(y_pred))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the loss instance. |
| `axis` | Tuple for which dimensions the loss is calculated. Defaults to `None`. |
| `dtype` | The dtype of the loss's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

|     |
| --- |
| Returns<br>------- |     |
| Dice loss value. |     |

#### Example:

    y_true = [[[[1.0], [1.0]], [[0.0], [0.0]]],\
\
    loss = keras.losses.Dice()(y_true, y_pred)\
\
    y_true = np.array(y_true)\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `dtype` |     |\
\
Methods\
-------\
\
### `call`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L28-L34)\
\
call(\
        y_true, y_pred\
    )\
\
### `from_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L42-L46)\
\
@classmethod\
\
### `get_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1370-L1373)\
\
get_config()\
\
### `__call__`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/loss.py#L56-L85)\
\
__call__(\
        y_true, y_pred, sample_weight=None\
    )\
\
Call self as a function.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.