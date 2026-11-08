[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Flosses%2Fsoftmax_cross_entropy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.softmax\_cross\_entropy Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L837-L992)

Creates a cross-entropy loss using tf.nn.softmax\_cross\_entropy\_with\_logits\_v2.

tf.compat.v1.losses.softmax_cross_entropy(
        onehot_labels,
        logits,
        weights=1.0,
        label_smoothing=0,
        scope=None,
        loss_collection=ops.GraphKeys.LOSSES,
        reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
    )

Migrate to TF2
--------------

[`tf.compat.v1.losses.softmax_cross_entropy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy)
 is mostly compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. But, the `loss_collection` argument is ignored when executing eagerly and no loss will be written to the loss collections. You will need to either hold on to the return value manually or rely on [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
 loss tracking.

To switch to native TF2 style, instantiate the [`tf.keras.losses.CategoricalCrossentropy`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy)
 class with `from_logits` set as `True` and call the object instead.

#### Structural Mapping to Native TF2

Before:

loss = tf.compat.v1.losses.softmax_cross_entropy(
      onehot_labels=onehot_labels,
      logits=logits,
      weights=weights,
      label_smoothing=smoothing)

After:

loss_fn = tf.keras.losses.CategoricalCrossentropy(
      from_logits=True,
      label_smoothing=smoothing)
    loss = loss_fn(
      y_true=onehot_labels,
      y_pred=logits,
      sample_weight=weights)

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| \-  | `from_logits` | Set `from_logits` as True to have identical behavior |
| `onehot_labels` | `y_true` | In `__call__()` method |
| `logits` | `y_pred` | In `__call__()` method |
| `weights` | `sample_weight` | In `__call__()` method |
| `label_smoothing` | `label_smoothing` | In constructor |
| `scope` | Not supported | \-  |
| `loss_collection` | Not supported | Losses should be tracked explicitly or with Keras APIs, for example, [add\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#add_loss)<br>, instead of via collections |
| `reduction` | `reduction` | In constructor. Value of [`tf.compat.v1.losses.Reduction.SUM_OVER_BATCH_SIZE`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#SUM_OVER_BATCH_SIZE)<br>, [`tf.compat.v1.losses.Reduction.SUM`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#SUM)<br>, [`tf.compat.v1.losses.Reduction.NONE`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#NONE)<br> in [`tf.compat.v1.losses.softmax_cross_entropy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy)<br> correspond to [`tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Reduction#SUM_OVER_BATCH_SIZE)<br>, [`tf.keras.losses.Reduction.SUM`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Reduction#SUM)<br>, [`tf.keras.losses.Reduction.NONE`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/Reduction#NONE)<br>, respectively. If you used other value for `reduction`, including the default value [`tf.compat.v1.losses.Reduction.SUM_BY_NONZERO_WEIGHTS`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction#SUM_BY_NONZERO_WEIGHTS)<br>, there is no directly corresponding value. Please modify the loss implementation manually. |

#### Before & After Usage Example

Before:

    y_true = [[0, 1, 0], [0, 0, 1]]

After:

    cce = tf.keras.losses.CategoricalCrossentropy(from_logits=True,

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging) |

`weights` acts as a coefficient for the loss. If a scalar is provided, then the loss is simply scaled by the given value. If `weights` is a tensor of shape `[batch_size]`, then the loss weights apply to each corresponding sample.

If `label_smoothing` is nonzero, smooth the labels towards 1/num\_classes: new\_onehot\_labels = onehot\_labels \* (1 - label\_smoothing)

                    + label_smoothing / num_classes

Note that `onehot_labels` and `logits` must have the same shape, e.g. `[batch_size, num_classes]`. The shape of `weights` must be broadcastable to loss, whose shape is decided by the shape of `logits`. In case the shape of `logits` is `[batch_size, num_classes]`, loss is a `Tensor` of shape `[batch_size]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `onehot_labels` | One-hot-encoded labels. |
| `logits` | Logits outputs of the network. |
| `weights` | Optional `Tensor` that is broadcastable to loss. |
| `label_smoothing` | If greater than 0 then smooth the labels. |
| `scope` | the scope for the operations performed in computing the loss. |
| `loss_collection` | collection to which the loss will be added. |
| `reduction` | Type of reduction to apply to loss. |

|     |
| --- |
| Returns<br>------- |     |
| Weighted loss `Tensor` of the same type as `logits`. If `reduction` is `NONE`, this has shape `[batch_size]`; otherwise, it is scalar. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the shape of `logits` doesn't match that of `onehot_labels` or if the shape of `weights` is invalid or if `weights` is None. Also if `onehot_labels` or `logits` is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.