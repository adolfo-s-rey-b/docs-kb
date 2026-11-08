None

[KerasRS](https://keras.io/keras_rs/)

[API documentation](https://keras.io/keras_rs/api/)
 [Embedding Layers](https://keras.io/keras_rs/api/embedding_layers/)
 [Feature Interaction Layers](https://keras.io/keras_rs/api/feature_interaction_layers/)
 [Retrieval Layers](https://keras.io/keras_rs/api/retrieval_layers/)
 [Losses](https://keras.io/keras_rs/api/losses/)
 [Metrics](https://keras.io/keras_rs/api/metrics/)
 [Examples](https://keras.io/keras_rs/examples/)

► [KerasRS](https://keras.io/keras_rs/)
 / [API documentation](https://keras.io/keras_rs/api/)
 / [Retrieval Layers](https://keras.io/keras_rs/api/retrieval_layers/)
 / HardNegativeMining layer

HardNegativeMining layer
========================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/hard_negative_mining.py#L13)

### `HardNegativeMining` class

Copied!

`keras_rs.layers.HardNegativeMining(num_hard_negatives: int, **kwargs: Any)`

Filter logits and labels to return hard negatives.

The output will include logits and labels for the requested number of hard negatives as well as the positive candidate.

**Arguments**

*   **num\_hard\_negatives**: How many hard negatives to return.
*   **\*\*kwargs**: Args to pass to the base class.

**Example**

Copied!

``# Create layer with the configured number of hard negatives to mine. hard_negative_mining = keras_rs.layers.HardNegativeMining(     num_hard_negatives=10 )  # This will retrieve the top 10 negative candidates plus the positive # candidate from `labels` for each row. out_logits, out_labels = hard_negative_mining(in_logits, in_labels)``

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/hard_negative_mining.py#L43)

### `call` method

Copied!

`HardNegativeMining.call(logits: Any, labels: Any)`

Filters logits and labels with per-query hard negative mining.

The result will include logits and labels for `num_hard_negatives` negatives as well as the positive candidate.

**Arguments**

*   **logits**: The logits tensor, typically `[batch_size, num_candidates]` but can have more dimensions or be 1D as `[num_candidates]`.
*   **labels**: The one-hot labels tensor, must be the same shape as `logits`.

**Returns**

A tuple containing two tensors with the last dimension of `num_candidates` replaced with `num_hard_negatives + 1`.

*   logits: `[..., num_hard_negatives + 1]` tensor of logits.
*   labels: `[..., num_hard_negatives + 1]` one-hot tensor of labels.

* * *

[HardNegativeMining layer](https://keras.io/keras_rs/api/retrieval_layers/hard_negative_mining/#hardnegativemining-layer)

[`HardNegativeMining` class](https://keras.io/keras_rs/api/retrieval_layers/hard_negative_mining/#hardnegativemining-class)

[`call` method](https://keras.io/keras_rs/api/retrieval_layers/hard_negative_mining/#call-method)