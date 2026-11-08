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
 / [Losses](https://keras.io/keras_rs/api/losses/)
 / ListMLELoss

ListMLELoss
===========

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/losses/list_mle_loss.py#L12)

### `ListMLELoss` class

Copied!

`keras_rs.losses.ListMLELoss(temperature: float = 1.0, **kwargs: Any)`

Implements ListMLE (Maximum Likelihood Estimation) loss for ranking.

ListMLE loss is a listwise ranking loss that maximizes the likelihood of the ground truth ranking. It works by: 1. Sorting items by their relevance scores (labels) 2. Computing the probability of observing this ranking given the predicted scores 3. Maximizing this likelihood (minimizing negative log-likelihood)

The loss is computed as the negative log-likelihood of the ground truth ranking given the predicted scores:

Copied!

`loss = -sum(log(exp(s_i) / sum(exp(s_j) for j >= i)))`

where s\_i is the predicted score for item i in the sorted order.

**Arguments**

*   **temperature**: Temperature parameter for scaling logits. Higher values make the probability distribution more uniform. Defaults to 1.0.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`.

**Examples**

Copied!

`# Basic usage loss_fn = ListMLELoss()  # With temperature scaling loss_fn = ListMLELoss(temperature=0.5)  # Example with synthetic data y_true = [[3, 2, 1, 0]]  # Relevance scores y_pred = [[0.8, 0.6, 0.4, 0.2]]  # Predicted scores loss = loss_fn(y_true, y_pred)`

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/losses/list_mle_loss.py#L160)

### `call` method

Copied!

`ListMLELoss.call(y_true: Any, y_pred: Any)`

Compute the ListMLE loss.

**Arguments**

*   **y\_true**: tensor or dict. Ground truth values. If tensor, of shape `(list_size)` for unbatched inputs or `(batch_size, list_size)` for batched inputs. If an item has a label of -1, it is ignored in loss computation. If it is a dictionary, it should have two keys: `"labels"` and `"mask"`. `"mask"` can be used to ignore elements in loss computation.
*   **y\_pred**: tensor. The predicted values, of shape `(list_size)` for unbatched inputs or `(batch_size, list_size)` for batched inputs. Should be of the same shape as `y_true`.

**Returns**

The loss tensor of shape \[batch\_size\].

* * *

[ListMLELoss](https://keras.io/keras_rs/api/losses/list_mle_loss/#listmleloss)

[`ListMLELoss` class](https://keras.io/keras_rs/api/losses/list_mle_loss/#listmleloss-class)

[`call` method](https://keras.io/keras_rs/api/losses/list_mle_loss/#call-method)