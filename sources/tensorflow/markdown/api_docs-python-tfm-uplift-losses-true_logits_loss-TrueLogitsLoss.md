[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.losses.true\_logits\_loss.TrueLogitsLoss Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#get_config)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/losses/true_logits_loss/TrueLogitsLoss#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/losses/true_logits_loss.py#L26-L102)

Computes any arbitrary loss between the labels and the true logits tensor.

tfm.uplift.losses.true_logits_loss.TrueLogitsLoss(
        loss_fn: Callable[[Any, tf.Tensor], tf.Tensor],
        name: str = 'true_logits_loss',
        reduction=tf_keras.losses.Reduction.AUTO,
        **loss_fn_kwargs
    )

Note that the prediction tensor is expected to be of a tensor of type `TwoTowerTrainingOutputs`.

Example standalone usage:

    y_true = tf.ones((3, 1))

Example usage with the `compile()` API:

model.compile(
        optimizer='sgd'.
        loss=TrueLogitsLoss(
            loss_fn=tf_keras.losses.categorical_crossentropy,
            name="categorical_crossentropy",
            from_logits=True
        )
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `loss_fn` | The loss function to apply between the labels and true logits tensor, with signature `loss_fn(y_true, y_pred, **loss_fn_kwargs)`. |
| `name` | Optional name for the instance. |
| `reduction` | Type of `tf_keras.losses.Reduction` to apply to loss. Default value is `AUTO`. `AUTO` indicates that the reduction option will be determined by the usage context. For almost all cases this defaults to `SUM_OVER_BATCH_SIZE`. When used under a [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br>, except via [`Model.compile()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile)<br> and [`Model.fit()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)<br>, using `AUTO` or `SUM_OVER_BATCH_SIZE` will raise an error. |
| `**loss_fn_kwargs` | The keyword arguments that are passed on to `loss_fn`. |

Methods
-------

### `from_config`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/losses/true_logits_loss.py#L99-L102)

@classmethod

Instantiates a `Loss` from its config (output of `get_config()`).

|     |     |
| --- | --- |
| Args |     |
| `config` | Output of `get_config()`. |

|     |
| --- |
| Returns |     |
| A [`keras.losses.Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)<br> instance. |     |

### `get_config`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/recommendation/uplift/losses/true_logits_loss.py#L94-L97)

get_config() -> Mapping[str, Any]

Returns the config dictionary for a `Loss` instance.

### `__call__`

__call__(
        y_true, y_pred, sample_weight=None
    )

Invokes the `Loss` instance.

|     |     |
| --- | --- |
| Args |     |
| `y_true` | Ground truth values. shape = `[batch_size, d0, .. dN]`, except sparse loss functions such as sparse categorical crossentropy where shape = `[batch_size, d0, .. dN-1]` |
| `y_pred` | The predicted values. shape = `[batch_size, d0, .. dN]` |
| `sample_weight` | Optional `sample_weight` acts as a coefficient for the loss. If a scalar is provided, then the loss is simply scaled by the given value. If `sample_weight` is a tensor of size `[batch_size]`, then the total loss for each sample of the batch is rescaled by the corresponding element in the `sample_weight` vector. If the shape of `sample_weight` is `[batch_size, d0, .. dN-1]` (or can be broadcasted to this shape), then each loss element of `y_pred` is scaled by the corresponding value of `sample_weight`. (Note on`dN-1`: all loss functions reduce by 1 dimension, usually axis=-1.) |

|     |
| --- |
| Returns |     |
| Weighted loss float `Tensor`. If `reduction` is `NONE`, this has shape `[batch_size, d0, .. dN-1]`; otherwise, it is scalar. (Note `dN-1` because all loss functions reduce by 1 dimension, usually axis=-1.) |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the shape of `sample_weight` is invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.