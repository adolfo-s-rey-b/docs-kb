None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Metrics](https://keras.io/keras_hub/api/metrics/)
 / Perplexity metric

Perplexity metric
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/metrics/perplexity.py#L8)

### `Perplexity` class

Copied!

`keras_hub.metrics.Perplexity(     from_logits=False, mask_token_id=None, dtype="float32", name="perplexity", **kwargs )`

Perplexity metric.

This class implements the perplexity metric. In short, this class calculates the cross entropy loss and takes its exponent. Note: This implementation is not suitable for fixed-size windows.

**Arguments**

*   **from\_logits**: bool. If True, `y_pred` (input to `update_state()`) should be the logits as returned by the model. Otherwise, `y_pred` is a tensor of probabilities.
*   **mask\_token\_id**: int. ID of the token to be masked. If provided, the mask is computed for this class. Note that if this field is provided, and if the `sample_weight` field in `update_state()` is also provided, we will compute the final `sample_weight` as the element-wise product of the mask and the `sample_weight`.
*   **dtype**: string or tf.dtypes.Dtype. Precision of metric computation. If not specified, it defaults to `"float32"`.
*   **name**: string. Name of the metric instance.
*   **\*\*kwargs**: Other keyword arguments.

**Examples**

1.  Calculate perplexity by calling update\_state() and result(). 1.1. `sample_weight`, and `mask_token_id` are not provided.

Copied!

`>>> np.random.seed(42) >>> perplexity = keras_hub.metrics.Perplexity(name="perplexity") >>> target = np.random.randint(10, size=[2, 5]) >>> logits = np.random.uniform(size=(2, 5, 10)) >>> perplexity.update_state(target, logits) >>> perplexity.result() <tf.Tensor: shape=(), dtype=float32, numpy=14.352535>`

1.2. `sample_weight` specified (masking token with ID 0).

Copied!

`>>> np.random.seed(42) >>> perplexity = keras_hub.metrics.Perplexity(name="perplexity") >>> target = np.random.randint(10, size=[2, 5]) >>> logits = np.random.uniform(size=(2, 5, 10)) >>> sample_weight = (target != 0).astype("float32") >>> perplexity.update_state(target, logits, sample_weight) >>> perplexity.result() <tf.Tensor: shape=(), dtype=float32, numpy=14.352535>`

1.  Call perplexity directly.

Copied!

`>>> np.random.seed(42) >>> perplexity = keras_hub.metrics.Perplexity(name="perplexity") >>> target = np.random.randint(10, size=[2, 5]) >>> logits = np.random.uniform(size=(2, 5, 10)) >>> perplexity(target, logits) <tf.Tensor: shape=(), dtype=float32, numpy=14.352535>`

1.  Provide the padding token ID and let the class compute the mask on its own.

Copied!

`>>> np.random.seed(42) >>> perplexity = keras_hub.metrics.Perplexity(mask_token_id=0) >>> target = np.random.randint(10, size=[2, 5]) >>> logits = np.random.uniform(size=(2, 5, 10)) >>> perplexity(target, logits) <tf.Tensor: shape=(), dtype=float32, numpy=14.352535>`

* * *

[Perplexity metric](https://keras.io/keras_hub/api/metrics/perplexity/#perplexity-metric)

[`Perplexity` class](https://keras.io/keras_hub/api/metrics/perplexity/#perplexity-class)