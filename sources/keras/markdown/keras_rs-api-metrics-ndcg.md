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
 / [Metrics](https://keras.io/keras_rs/api/metrics/)
 / nDCG metric

nDCG metric
===========

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/metrics/ndcg.py#L24)

### `NDCG` class

Copied!

`keras_rs.metrics.NDCG(     k: int | None = None,     gain_fn: Callable[[Any], Any] = default_gain_fn,     rank_discount_fn: Callable[[Any], Any] = default_rank_discount_fn,     **kwargs: Any )`

Computes Normalised Discounted Cumulative Gain (nDCG).

This metric evaluates ranking quality. It normalizes the Discounted Cumulative Gain (DCG) with the Ideal Discounted Cumulative Gain (IDCG) for each list. The metric processes true relevance labels in `y_true` (graded relevance scores (non-negative numbers where higher values indicate greater relevance)) against predicted scores in `y_pred`. The scores in `y_pred` are used to determine the rank order of items, by sorting in descending order. A normalized score (between 0 and 1) is returned. A score of 1 represents the perfect ranking according to true relevance (within the top-k), while 0 typically represents a ranking with no relevant items. Higher scores indicate better ranking quality relative to the best possible ranking.

For each list of predicted scores `s` in `y_pred` and the corresponding list of true labels `y` in `y_true`, the per-query nDCG score is calculated as follows:

Copied!

`nDCG@k = DCG@k / IDCG@k`

where DCG@k is calculated based on the predicted ranking (`y_pred`):

Copied!

`DCG@k(y') = sum_{i=1}^{k} (gain_fn(y'_i) / rank_discount_fn(i))`

And IDCG@k is the Ideal DCG, calculated using the same formula but on items sorted perfectly by their _true relevance_ (`y_true`):

Copied!

`IDCG@k(y'') = sum_{i=1}^{k} (gain_fn(y''_i) / rank_discount_fn(i))`

where:

*   `y'_i`: True relevance of the item at rank `i` in the ranking induced by `y_pred`.
*   `y''_i` True relevance of the item at rank `i` in the _ideal_ ranking (sorted by `y_true` descending).
*   `gain_fn` is the user-provided function mapping relevance to gain. The default function (`default_gain_fn`) is typically equivalent to `lambda y: 2**y - 1`.
*   `rank_discount_fn` is the user-provided function mapping rank `i` (1-based) to a discount value. The default function (`default_rank_discount_fn`) is typically equivalent to `lambda rank: 1 / log2(rank + 1)`.
*   If IDCG@k is 0 (e.g., no relevant items), nDCG@k is defined as 0.
*   The final result often aggregates these per-list nDCG scores, potentially involving normalization by list-specific weights, to produce a weighted average.

The final nDCG score reported is typically the weighted average of these per-query scores across all queries/lists in the dataset.

Note: `sample_weight` is handled differently for ranking metrics. For batched inputs, `sample_weight` can be scalar, 1D, 2D. The scalar case and 1D case (list-wise weights) are straightforward. The 2D case (item- wise weights) is different, in the sense that the sample weights are aggregated to get 1D weights. For more details, refer to `keras_rs.src.metrics.ranking_metrics_utils.get_list_weights`.

**Arguments**

*   **gain\_fn**: callable. Maps relevance scores (`y_true`) to gain values. The default implements `2**y - 1`.
*   **rank\_discount\_fn**: function. Maps rank positions to discount values. The default (`default_rank_discount_fn`) implements `1 / log2(rank + 1)`.
*   **k**: int. The number of top-ranked items to consider (the 'k' in 'top-k'). Must be a positive integer.
*   **shuffle\_ties**: bool. Whether to randomly shuffle scores before sorting. This is done to break ties. Defaults to `True`.
*   **seed**: int. Random seed used for shuffling.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the metric's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Example**

Copied!

`>>> batch_size = 2 >>> list_size = 5 >>> labels = np.random.randint(0, 3, size=(batch_size, list_size)) >>> scores = np.random.random(size=(batch_size, list_size)) >>> metric = keras_rs.metrics.NDCG()( ...     y_true=labels, y_pred=scores ... )`

Mask certain elements (can be used for uneven inputs):

Copied!

`>>> batch_size = 2 >>> list_size = 5 >>> labels = np.random.randint(0, 3, size=(batch_size, list_size)) >>> scores = np.random.random(size=(batch_size, list_size)) >>> mask = np.random.randint(0, 2, size=(batch_size, list_size), dtype=bool) >>> metric = keras_rs.metrics.NDCG()( ...     y_true={"labels": labels, "mask": mask}, y_pred=scores ... )`

* * *

[nDCG metric](https://keras.io/keras_rs/api/metrics/ndcg/#ndcg-metric)

[`NDCG` class](https://keras.io/keras_rs/api/metrics/ndcg/#ndcg-class)