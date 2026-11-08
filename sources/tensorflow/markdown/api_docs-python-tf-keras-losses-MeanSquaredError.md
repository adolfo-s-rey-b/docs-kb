[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.MeanSquaredError Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#call)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L52-L98)

Computes the mean of squares of errors between labels and predictions.

Inherits From: [`Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)

tf.keras.losses.MeanSquaredError(
        reduction='sum_over_batch_size',
        name='mean_squared_error',
        dtype=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Basic training loops](https://www.tensorflow.org/guide/basic_training_loops) | *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)<br>    <br>*   [Hello, many worlds](https://www.tensorflow.org/quantum/tutorials/hello_many_worlds)<br>    <br>*   [Recommending movies: ranking](https://www.tensorflow.org/recommenders/examples/basic_ranking) |

#### Formula:

loss = mean(square(y_true - y_pred))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the loss instance. |
| `dtype` | The dtype of the loss's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

#### Examples:

    y_true = keras.ops.array([1.0, 0.0, 1.0])

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L97-L98)

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

Last updated 2026-11-05 UTC.