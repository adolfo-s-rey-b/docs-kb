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
 / MeanAveragePrecision metric

MeanAveragePrecision metric
===========================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/metrics/mean_average_precision.py#L17)

### `MeanAveragePrecision` class

Copied!

`keras_rs.metrics.MeanAveragePrecision(     k: int | None = None,     shuffle_ties: bool = True,     seed: int | keras.src.random.seed_generator.SeedGenerator | None = None,     **kwargs: Any )`

Computes Mean Average Precision (MAP).

This metric evaluates ranking quality. It calculates the average of precision values computed after each relevant item present in the ranked list. The metric processes true relevance labels in `y_true` (binary indicators (0 or 1) of relevance) against predicted scores in `y_pred`. The scores in `y_pred` are used to determine the rank order of items, by sorting in descending order. Scores range from 0 to 1, with higher values indicating that relevant items are generally positioned higher in the ranking.

For each list of predicted scores `s` in `y_pred` and the corresponding list of true labels `y` in `y_true`, the per-query MAP score is calculated as follows:

The formula for average precision is defined below. MAP is the mean over average precision computed for each list.

Copied!

`AP(y, s) = sum_j (P@j(y, s) * rel(j)) / sum_i y_i rel(j) = y_i if rank(s_i) = j`

where:

*   `j` represents the rank position (starting from 1).
*   `sum_j` indicates a summation over all ranks `j` from 1 up to the list size (or `k`).
*   `P@j(y, s)` denotes the Precision at rank `j`, calculated as the number of relevant items found within the top `j` positions divided by `j`.
*   `rel(j)` represents the relevance of the item specifically at rank `j`. `rel(j)` is 1 if the item at rank `j` is relevant, and 0 otherwise.
*   `y_i` is the true relevance label of the original item `i` before ranking.
*   `rank(s_i)` is the rank position assigned to item `i` based on its score `s_i`.
*   `sum_i y_i` calculates the total number of relevant items in the original list `y`.

The final MAP score reported is typically the weighted average of these per-query scores across all queries/lists in the dataset.

Note: `sample_weight` is handled differently for ranking metrics. For batched inputs, `sample_weight` can be scalar, 1D, 2D. The scalar case and 1D case (list-wise weights) are straightforward. The 2D case (item- wise weights) is different, in the sense that the sample weights are aggregated to get 1D weights. For more details, refer to `keras_rs.src.metrics.ranking_metrics_utils.get_list_weights`.

**Arguments**

*   **k**: int. The number of top-ranked items to consider (the 'k' in 'top-k'). Must be a positive integer.
*   **shuffle\_ties**: bool. Whether to randomly shuffle scores before sorting. This is done to break ties. Defaults to `True`.
*   **seed**: int. Random seed used for shuffling.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the metric's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Example**

Copied!

`>>> batch_size = 2 >>> list_size = 5 >>> labels = np.random.randint(0, 2, size=(batch_size, list_size)) >>> scores = np.random.random(size=(batch_size, list_size)) >>> metric = keras_rs.metrics.MeanAveragePrecision()( ...     y_true=labels, y_pred=scores ... )`

Mask certain elements (can be used for uneven inputs):

Copied!

`>>> batch_size = 2 >>> list_size = 5 >>> labels = np.random.randint(0, 2, size=(batch_size, list_size)) >>> scores = np.random.random(size=(batch_size, list_size)) >>> mask = np.random.randint(0, 2, size=(batch_size, list_size), dtype=bool) >>> metric = keras_rs.metrics.MeanAveragePrecision()( ...     y_true={"labels": labels, "mask": mask}, y_pred=scores ... )`

* * *

[MeanAveragePrecision metric](https://keras.io/keras_rs/api/metrics/mean_average_precision/#meanaverageprecision-metric)

[`MeanAveragePrecision` class](https://keras.io/keras_rs/api/metrics/mean_average_precision/#meanaverageprecision-class)