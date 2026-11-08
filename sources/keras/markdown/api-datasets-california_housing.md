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
 / California Housing price regression dataset

California Housing price regression dataset
===========================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/california_housing.py#L9)

### `load_data` function

Copied!

`keras.datasets.california_housing.load_data(     version="large", path="california_housing.npz", test_split=0.2, seed=113 )`

Loads the California Housing dataset.

This dataset was obtained from the [StatLib repository](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html)
.

It's a continuous regression dataset with 20,640 samples with 8 features each.

The target variable is a scalar: the median house value for California districts, in dollars.

The 8 input features are the following:

*   MedInc: median income in block group
*   HouseAge: median house age in block group
*   AveRooms: average number of rooms per household
*   AveBedrms: average number of bedrooms per household
*   Population: block group population
*   AveOccup: average number of household members
*   Latitude: block group latitude
*   Longitude: block group longitude

This dataset was derived from the 1990 U.S. census, using one row per census block group. A block group is the smallest geographical unit for which the U.S. Census Bureau publishes sample data (a block group typically has a population of 600 to 3,000 people).

A household is a group of people residing within a home. Since the average number of rooms and bedrooms in this dataset are provided per household, these columns may take surprisingly large values for block groups with few households and many empty houses, such as vacation resorts.

**Arguments**

*   **version**: `"small"` or `"large"`. The small version contains 600 samples, the large version contains 20,640 samples. The purpose of the small version is to serve as an approximate replacement for the deprecated `boston_housing` dataset.
*   **path**: path where to cache the dataset locally (relative to `~/.keras/datasets`).
*   **test\_split**: fraction of the data to reserve as test set.
*   **seed**: Random seed for shuffling the data before computing the test split.

**Returns**

*   **Tuple of Numpy arrays**: `(x_train, y_train), (x_test, y_test)`.

**`x_train`, `x_test`**: numpy arrays with shape `(num_samples, 8)` containing either the training samples (for `x_train`), or test samples (for `y_train`).

**`y_train`, `y_test`**: numpy arrays of shape `(num_samples,)` containing the target scalars. The targets are float scalars typically between 25,000 and 500,000 that represent the home prices in dollars.

* * *

[California Housing price regression dataset](https://keras.io/api/datasets/california_housing/#california-housing-price-regression-dataset)

[`load_data` function](https://keras.io/api/datasets/california_housing/#loaddata-function)