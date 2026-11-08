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
 / Retrieval layer

Retrieval layer
===============

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/retrieval.py#L10)

### `Retrieval` class

Copied!

`keras_rs.layers.Retrieval(k: int = 10, return_scores: bool = True, **kwargs: Any)`

Retrieval base abstract class.

This layer provides a common interface for all retrieval layers. In order to implement a custom retrieval layer, this abstract class should be subclassed.

**Arguments**

*   **k**: int. Number of candidates to retrieve.
*   **return\_scores**: bool. When `True`, this layer returns a tuple with the top scores and the top identifiers. When `False`, this layer returns a single tensor with the top identifiers.

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/retrieval.py#L85)

### `call` method

Copied!

`Retrieval.call(inputs: Any)`

Returns the top candidates for the query passed as input.

**Arguments**

*   **inputs**: the query for which to return top candidates.

**Returns**

A tuple with the top scores and the top identifiers if `returns_scores` is True, otherwise a tensor with the top identifiers.

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/retrieval.py#L70)

### `update_candidates` method

Copied!

`Retrieval.update_candidates(     candidate_embeddings: Any, candidate_ids: typing.Any | None = None )`

Update the set of candidates and optionally their candidate IDs.

**Arguments**

*   **candidate\_embeddings**: The candidate embeddings.
*   **candidate\_ids**: The identifiers for the candidates. If `None`, the indices of the candidates are returned instead.

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/retrieval.py#L101)

### `compute_score` method

Copied!

`Retrieval.compute_score(query_embedding: Any, candidate_embedding: Any)`

Computes the standard dot product score from queries and candidates.

**Arguments**

*   **query\_embedding**: Tensor of query embedding corresponding to the queries for which to retrieve top candidates.
*   **candidate\_embedding**: Tensor of candidate embeddings.

**Returns**

The dot product of queries and candidates.

* * *

[Retrieval layer](https://keras.io/keras_rs/api/retrieval_layers/retrieval/#retrieval-layer)

[`Retrieval` class](https://keras.io/keras_rs/api/retrieval_layers/retrieval/#retrieval-class)

[`call` method](https://keras.io/keras_rs/api/retrieval_layers/retrieval/#call-method)

[`update_candidates` method](https://keras.io/keras_rs/api/retrieval_layers/retrieval/#updatecandidates-method)

[`compute_score` method](https://keras.io/keras_rs/api/retrieval_layers/retrieval/#computescore-method)