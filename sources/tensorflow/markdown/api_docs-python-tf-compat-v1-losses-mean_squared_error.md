[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.mean\_squared\_error Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L621-L768)

Adds a Sum-of-Squares loss to the training procedure.

tf.compat.v1.losses.mean_squared_error(
        labels,
        predictions,
        weights=1.0,
        scope=None,
        loss_collection=ops.GraphKeys.LOSSES,
        reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
    )

Migrate to TF2
--------------

[`tf.compat.v1.losses.mean_squared_error`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error)
 is mostly compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. But, the `loss_collection` argument is ignored when executing eagerly and no loss will be written to the loss collections. You will need to either hold on to the return value manually or rely on [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
 loss tracking.

To switch to native TF2 style, instantiate the [`tf.keras.losses.MeanSquaredError`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError)
 class and call the object instead.

#### Structural Mapping to Native TF2

Before:

loss = tf.compat.v1.losses.mean_squared_error(
      labels=labels,
      predictions=predictions,
      weights=weights,
      reduction=reduction)

After:

loss_fn = tf.keras.losses.MeanSquaredError(
      reduction=reduction)
    loss = loss_fn(
      y_true=labels,
      y_pred=predictions,
      sample_weight=weights)

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `labels` | `y_true` | In `__call__()` method |
| `predictions` | `y_pred` | In `__call__()` method |
| `weights` | `sample_weight` | In `__call__()` method. The shape requirements for `sample_weight` is different from `weights`. Please check the [argument definition](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError#__call__)<br> for details. |
| `scope` | Not supported | \-  |
| `loss_collection` | Not supported | Losses should be tracked explicitly or with Keras APIs, for example, [add\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#add_loss)<br>, instead of via collections |
| `reduction` | `reduction` | In constructor. Value of [`tf.compat.v1.losses.Reduction.SUM_OVER_BATCH_SIZE`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#SUM_OVER_BATCH_SIZE)<br>, [`tf.compat.v1.losses.Reduction.SUM`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#SUM)<br>, [`tf.compat.v1.losses.Reduction.NONE`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#NONE)<br> in [`tf.compat.v1.losses.softmax_cross_entropy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy)<br> correspond to [`tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Reduction#SUM_OVER_BATCH_SIZE)<br>, [`tf.keras.losses.Reduction.SUM`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Reduction#SUM)<br>, [`tf.keras.losses.Reduction.NONE`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Reduction#NONE)<br>, respectively. If you used other value for `reduction`, including the default value [`tf.compat.v1.losses.Reduction.SUM_BY_NONZERO_WEIGHTS`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#SUM_BY_NONZERO_WEIGHTS)<br>, there is no directly corresponding value. Please modify the loss implementation manually. |

#### Before & After Usage Example

Before:

    y_true = [1, 2, 3]

    tf.compat.v1.losses.mean_squared_error(

After:

    y_true = [[1.0], [2.0], [3.0]]

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate LoggingTensorHook and StopAtStepHook to Keras callbacks](https://www.tensorflow.org/guide/migrate/logging_stop_hook)<br>    <br>*   [Migrate from Estimator to Keras APIs](https://www.tensorflow.org/guide/migrate/migrating_estimator)<br>    <br>*   [Migrate single-worker multiple-GPU training](https://www.tensorflow.org/guide/migrate/mirrored_strategy)<br>    <br>*   [Migrate multi-worker CPU/GPU training](https://www.tensorflow.org/guide/migrate/multi_worker_cpu_gpu_training)<br>    <br>*   [Migrate SessionRunHook to Keras callbacks](https://www.tensorflow.org/guide/migrate/sessionrunhook_callback) |

`weights` acts as a coefficient for the loss. If a scalar is provided, then the loss is simply scaled by the given value. If `weights` is a tensor of size `[batch_size]`, then the total loss for each sample of the batch is rescaled by the corresponding element in the `weights` vector. If the shape of `weights` matches the shape of `predictions`, then the loss of each measurable element of `predictions` is scaled by the corresponding value of `weights`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | The ground truth output tensor, same dimensions as 'predictions'. |
| `predictions` | The predicted outputs. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `losses` dimension). |
| `scope` | The scope for the operations performed in computing the loss. |
| `loss_collection` | collection to which the loss will be added. |
| `reduction` | Type of reduction to apply to loss. |

|     |
| --- |
| Returns<br>------- |     |
| Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same shape as `labels`; otherwise, it is scalar. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the shape of `predictions` doesn't match that of `labels` or if the shape of `weights` is invalid. Also if `labels` or `predictions` is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.