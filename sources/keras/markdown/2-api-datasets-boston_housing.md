None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [MNIST digits classification dataset](https://keras.io/2/api/datasets/mnist/)
 [CIFAR10 small images classification dataset](https://keras.io/2/api/datasets/cifar10/)
 [CIFAR100 small images classification dataset](https://keras.io/2/api/datasets/cifar100/)
 [IMDB movie review sentiment classification dataset](https://keras.io/2/api/datasets/imdb/)
 [Reuters newswire classification dataset](https://keras.io/2/api/datasets/reuters/)
 [Fashion MNIST dataset, an alternative to MNIST](https://keras.io/2/api/datasets/fashion_mnist/)
 [Boston Housing price regression dataset](https://keras.io/2/api/datasets/boston_housing/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Built-in small datasets](https://keras.io/2/api/datasets/)
 / Boston Housing price regression dataset

Boston Housing price regression dataset
=======================================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/datasets/boston_housing.py#L27)

### `load_data` function

Copied!

`tf_keras.datasets.boston_housing.load_data(     path="boston_housing.npz", test_split=0.2, seed=113, cache_dir=None )`

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
*   **cache\_dir**: directory where to cache the dataset locally. When None, defaults to `~/.keras/datasets`.

**Returns**

*   **Tuple of Numpy arrays**: `(x_train, y_train), (x_test, y_test)`.

**x\_train, x\_test**: numpy arrays with shape `(num_samples, 13)` containing either the training samples (for x\_train), or test samples (for y\_train).

**y\_train, y\_test**: numpy arrays of shape `(num_samples,)` containing the target scalars. The targets are float scalars typically between 10 and 50 that represent the home prices in k$.

* * *

[Boston Housing price regression dataset](https://keras.io/2/api/datasets/boston_housing/#boston-housing-price-regression-dataset)

[`load_data` function](https://keras.io/2/api/datasets/boston_housing/#loaddata-function)