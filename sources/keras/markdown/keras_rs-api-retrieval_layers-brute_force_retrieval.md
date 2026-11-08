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
 / BruteForceRetrieval layer

BruteForceRetrieval layer
=========================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/brute_force_retrieval.py#L10)

### `BruteForceRetrieval` class

Copied!

`keras_rs.layers.BruteForceRetrieval(     candidate_embeddings: typing.Any | None = None,     candidate_ids: typing.Any | None = None,     k: int = 10,     return_scores: bool = True,     **kwargs: Any )`

Brute force top-k retrieval.

This layer maintains a set of candidates and is able to exactly retrieve the top-k candidates for a given query. It does this by computing the scores for all of the candidates for the query and extracting the top ones. The returned top-k candidates are sorted by score.

By default, this layer returns a tuple with the top scores and top identifiers, but it can be configured to return a single tensor with the top identifiers.

The identifiers for the candidates can be specified as a tensor. If not provided, the IDs used are simply the candidate indices.

Note that the serialization of this layer does not preserve the candidates and only saves the `k` and `return_scores` arguments. One has to call `update_candidates` after deserializing the layers.

**Arguments**

*   **candidate\_embeddings**: The candidate embeddings. If `None`, candidates must be provided using `update_candidates` before using this layer.
*   **candidate\_ids**: The identifiers for the candidates. If `None` the indices of the candidates are returned instead.
*   **k**: Number of candidates to retrieve.
*   **return\_scores**: When `True`, this layer returns a tuple with the top scores and the top identifiers. When `False`, this layer returns a single tensor with the top identifiers.
*   **\*\*kwargs**: Args to pass to the base class.

**Example**

Copied!

`retrieval = keras_rs.layers.BruteForceRetrieval(k=100)  # At some later point, we update the candidates. retrieval.update_candidates(candidate_embeddings, candidate_ids)  # We can then retrieve the top candidates for any number of queries. # Scores are stored highest first. Scores correspond to ids in the same row. tops_scores, top_ids = retrieval(query_embeddings)`

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/brute_force_retrieval.py#L126)

### `call` method

Copied!

`BruteForceRetrieval.call(inputs: Any)`

Returns the top candidates for the query passed as input.

**Arguments**

*   **inputs**: the query for which to return top candidates.

**Returns**

A tuple with the top scores and the top identifiers if `returns_scores` is True, otherwise a tensor with the top identifiers.

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/brute_force_retrieval.py#L81)

### `update_candidates` method

Copied!

`BruteForceRetrieval.update_candidates(     candidate_embeddings: Any, candidate_ids: typing.Any | None = None )`

Update the set of candidates and optionally their candidate IDs.

**Arguments**

*   **candidate\_embeddings**: The candidate embeddings.
*   **candidate\_ids**: The identifiers for the candidates. If `None`, the indices of the candidates are returned instead.

* * *

[BruteForceRetrieval layer](https://keras.io/keras_rs/api/retrieval_layers/brute_force_retrieval/#bruteforceretrieval-layer)

[`BruteForceRetrieval` class](https://keras.io/keras_rs/api/retrieval_layers/brute_force_retrieval/#bruteforceretrieval-class)

[`call` method](https://keras.io/keras_rs/api/retrieval_layers/brute_force_retrieval/#call-method)

[`update_candidates` method](https://keras.io/keras_rs/api/retrieval_layers/brute_force_retrieval/#updatecandidates-method)