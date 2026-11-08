[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#args)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#references)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.CategoricalGeneralizedCrossEntropy Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#args)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#references)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalGeneralizedCrossEntropy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1536-L1613)

Computes the Generalized Cross Entropy loss between `y_true` & `y_pred`.

Inherits From: [`Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)

tf.keras.losses.CategoricalGeneralizedCrossEntropy(
        q=0.5,
        reduction='sum_over_batch_size',
        name='categorical_generalized_cross_entropy',
        dtype=None
    )

Generalized Cross Entropy (GCE) is a noise-robust loss function that provides better robustness against noisy labels than standard cross entropy. It generalizes both cross entropy and mean absolute error through the parameter q, where values closer to 1 make the loss more robust to noisy labels.

#### Formula:

loss = (1 - p**q) / q

where `p` is the predicted probability for the true class and `q` is the noise parameter.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `q` | Float in range `(0, 1)`. It is the noise parameter. Controls the behavior of the loss:<br><br>*   As `q` approaches 0: Behaves more like cross entropy<br>*   As `q` approaches 1: Behaves more like mean absolute error Defaults to `0.5` |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the loss instance. |
| `dtype` | The dtype of the loss's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

#### Example:

y_true = np.array([0, 1, 0, 1])
    y_pred = np.array([[0.7, 0.3], [0.2, 0.8], [0.6, 0.4], [0.4, 0.6]])
    keras.losses.CategoricalGeneralizedCrossEntropy()(y_true, y_pred)

|     |
| --- |
| References<br>---------- |     |
| *   [Zhang, Sabuncu, 2018](https://arxiv.org/abs/1805.07836)<br>     ("Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels") |     |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1606-L1613)

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