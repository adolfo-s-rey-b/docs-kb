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
 / RemoveAccidentalHits layer

RemoveAccidentalHits layer
==========================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/remove_accidental_hits.py#L12)

### `RemoveAccidentalHits` class

Copied!

`keras_rs.layers.RemoveAccidentalHits(     activity_regularizer=None,     trainable=True,     dtype=None,     autocast=True,     name=None,     **kwargs )`

Zeroes the logits of accidental negatives.

Zeroes the logits of negative candidates that have the same ID as the positive candidate in that row.

**Example**

Copied!

``# Create layer with the configured number of hard negatives to mine. remove_accidental_hits = keras_rs.layers.RemoveAccidentalHits()  # This will zero the logits of negative candidates that have the same ID as # the positive candidate from `labels` so as to not negatively impact the # true positive. logits = remove_accidental_hits(logits, labels, candidate_ids)``

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/remove_accidental_hits.py#L32)

### `call` method

Copied!

`RemoveAccidentalHits.call(logits: Any, labels: Any, candidate_ids: Any)`

Zeroes selected logits.

For each row in the batch, zeroes the logits of negative candidates that have the same ID as the positive candidate in that row.

**Arguments**

*   **logits**: The logits tensor, typically `[batch_size, num_candidates]` but can have more dimensions or be 1D as `[num_candidates]`.
*   **labels**: The one-hot labels tensor, must be the same shape as `logits`.
*   **candidate\_ids**: The candidate identifiers tensor, can be `[num_candidates]` or `[batch_size, num_candidates]` or have more dimensions as long as they match the last dimensions of `labels`.

**Returns**

The modified logits with the same shape as the input logits.

* * *

[RemoveAccidentalHits layer](https://keras.io/keras_rs/api/retrieval_layers/remove_accidental_hits/#removeaccidentalhits-layer)

[`RemoveAccidentalHits` class](https://keras.io/keras_rs/api/retrieval_layers/remove_accidental_hits/#removeaccidentalhits-class)

[`call` method](https://keras.io/keras_rs/api/retrieval_layers/remove_accidental_hits/#call-method)