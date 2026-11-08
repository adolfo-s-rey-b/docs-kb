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
 / DCG metric

DCG metric
==========

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/metrics/dcg.py#L24)

### `DCG` class

Copied!

`keras_rs.metrics.DCG(     k: int | None = None,     gain_fn: Callable[[Any], Any] = default_gain_fn,     rank_discount_fn: Callable[[Any], Any] = default_rank_discount_fn,     **kwargs: Any )`

Computes Discounted Cumulative Gain (DCG).

This metric evaluates ranking quality. It computes the sum of the graded relevance scores of items, applying a configurable discount based on position. The metric processes true relevance labels in `y_true` (graded relevance scores (non-negative numbers where higher values indicate greater relevance)) against predicted scores in `y_pred`. The scores in `y_pred` are used to determine the rank order of items, by sorting in descending order. Scores are non-negative, with higher values indicating better ranking quality (highly relevant items are ranked higher). The score for a single list is not bounded or normalized, i.e., it does not lie in a range.

For each list of predicted scores `s` in `y_pred` and the corresponding list of true labels `y` in `y_true`, the per-query DCG score is calculated as follows:

Copied!

`DCG@k(y', w') = sum_{i=1}^{k} (gain_fn(y'_i) / rank_discount_fn(i))`

where:

*   `y'_i` is the true relevance score of the item ranked at position `i` (obtained by sorting `y_true` according to `y_pred`).
*   `gain_fn` is the user-provided function mapping relevance `y'_i` to a gain value. The default function (`default_gain_fn`) is typically equivalent to `lambda y: 2**y - 1`.
*   `rank_discount_fn` is the user-provided function mapping rank `i` to a discount value. The default function (`default_rank_discount_fn`) is typically equivalent to `lambda rank: 1 / log2(rank + 1)`.
*   The final result aggregates these per-list scores.

The final DCG score reported is typically the weighted average of these per-query scores across all queries/lists in the dataset.

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

`>>> batch_size = 2 >>> list_size = 5 >>> labels = np.random.randint(0, 3, size=(batch_size, list_size)) >>> scores = np.random.random(size=(batch_size, list_size)) >>> metric = keras_rs.metrics.DCG()( ...     y_true=labels, y_pred=scores ... )`

Mask certain elements (can be used for uneven inputs):

Copied!

`>>> batch_size = 2 >>> list_size = 5 >>> labels = np.random.randint(0, 3, size=(batch_size, list_size)) >>> scores = np.random.random(size=(batch_size, list_size)) >>> mask = np.random.randint(0, 2, size=(batch_size, list_size), dtype=bool) >>> metric = keras_rs.metrics.DCG()( ...     y_true={"labels": labels, "mask": mask}, y_pred=scores ... )`

* * *

[DCG metric](https://keras.io/keras_rs/api/metrics/dcg/#dcg-metric)

[`DCG` class](https://keras.io/keras_rs/api/metrics/dcg/#dcg-class)