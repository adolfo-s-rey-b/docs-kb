None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [MNIST digits classification dataset](https://keras.io/api/datasets/mnist/)
 [CIFAR10 small images classification dataset](https://keras.io/api/datasets/cifar10/)
 [CIFAR100 small images classification dataset](https://keras.io/api/datasets/cifar100/)
 [IMDB movie review sentiment classification dataset](https://keras.io/api/datasets/imdb/)
 [Reuters newswire classification dataset](https://keras.io/api/datasets/reuters/)
 [Fashion MNIST dataset, an alternative to MNIST](https://keras.io/api/datasets/fashion_mnist/)
 [California Housing price regression dataset](https://keras.io/api/datasets/california_housing/)
 [Boston Housing price regression dataset](https://keras.io/api/datasets/boston_housing/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Built-in small datasets](https://keras.io/api/datasets/)
 / Boston Housing price regression dataset

Boston Housing price regression dataset
=======================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/boston_housing.py#L7)

### `load_data` function

Copied!

`keras.datasets.boston_housing.load_data(     path="boston_housing.npz", test_split=0.2, seed=113 )`

Loads the Boston Housing dataset.

This is a dataset taken from the StatLib library which is maintained at Carnegie Mellon University.

**WARNING:** This dataset has an ethical problem: the authors of this dataset included a variable, "B", that may appear to assume that racial self-segregation influences house prices. As such, we strongly discourage the use of this dataset, unless in the context of illustrating ethical issues in data science and machine learning.

Samples contain 13 attributes of houses at different locations around the Boston suburbs in the late 1970s. Targets are the median values of the houses at a location (in k$).

The attributes themselves are defined in the [StatLib website](http://lib.stat.cmu.edu/datasets/boston)
.

**Arguments**

*   **path**: path where to cache the dataset locally (relative to `~/.keras/datasets`).
*   **test\_split**: fraction of the data to reserve as test set.
*   **seed**: Random seed for shuffling the data before computing the test split.

**Returns**

*   **Tuple of NumPy arrays**: `(x_train, y_train), (x_test, y_test)`.

**x\_train, x\_test**: NumPy arrays with shape `(num_samples, 13)` containing either the training samples (for x\_train), or test samples (for y\_train).

**y\_train, y\_test**: NumPy arrays of shape `(num_samples,)` containing the target scalars. The targets are float scalars typically between 10 and 50 that represent the home prices in k$.

* * *

[Boston Housing price regression dataset](https://keras.io/api/datasets/boston_housing/#boston-housing-price-regression-dataset)

[`load_data` function](https://keras.io/api/datasets/boston_housing/#loaddata-function)