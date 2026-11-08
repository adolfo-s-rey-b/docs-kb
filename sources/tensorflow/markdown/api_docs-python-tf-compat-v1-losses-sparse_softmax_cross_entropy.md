[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.sparse\_softmax\_cross\_entropy Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#raises)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/losses_impl.py#L1046-L1102)

Cross-entropy loss using [`tf.nn.sparse_softmax_cross_entropy_with_logits`](https://www.tensorflow.org/api_docs/python/tf/nn/sparse_softmax_cross_entropy_with_logits)
.

tf.compat.v1.losses.sparse_softmax_cross_entropy(
        labels,
        logits,
        weights=1.0,
        scope=None,
        loss_collection=ops.GraphKeys.LOSSES,
        reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrate early stopping](https://www.tensorflow.org/guide/migrate/early_stopping) |

`weights` acts as a coefficient for the loss. If a scalar is provided, then the loss is simply scaled by the given value. If `weights` is a tensor of shape `[batch_size]`, then the loss weights apply to each corresponding sample.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | `Tensor` of shape `[d_0, d_1, ..., d_{r-1}]` (where `r` is rank of `labels` and result) and dtype `int32` or `int64`. Each entry in `labels` must be an index in `[0, num_classes)`. Other values will raise an exception when this op is run on CPU, and return `NaN` for corresponding loss and gradient rows on GPU. |\
| `logits` | Unscaled log probabilities of shape `[d_0, d_1, ..., d_{r-1}, num_classes]` and dtype `float16`, `float32` or `float64`. |\
| `weights` | Coefficients for the loss. This must be scalar or broadcastable to `labels` (i.e. same rank and each dimension is either 1 or the same). |\
| `scope` | the scope for the operations performed in computing the loss. |\
| `loss_collection` | collection to which the loss will be added. |\
| `reduction` | Type of reduction to apply to loss. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| Weighted loss `Tensor` of the same type as `logits`. If `reduction` is `NONE`, this has the same shape as `labels`; otherwise, it is scalar. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If the shapes of `logits`, `labels`, and `weights` are incompatible, or if any of them are None. |\
\
eager compatibility\
-------------------\
\
The `loss_collection` argument is ignored when executing eagerly. Consider holding on to the return value or collecting losses via a [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)\
.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.