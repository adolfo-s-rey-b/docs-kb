[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/california_housing/load_data#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/california_housing/load_data)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/california_housing/load_data?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdatasets%2Fcalifornia_housing%2Fload_data&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/california_housing/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/california_housing/load_data#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.california\_housing.load\_data Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/california_housing/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/california_housing/load_data#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/california_housing.py#L9-L108)

Loads the California Housing dataset.

tf.keras.datasets.california_housing.load_data(
        version='large',
        path='california_housing.npz',
        test_split=0.2,
        seed=113
    )

This dataset was obtained from the [StatLib repository](https://www.dcc.fc.up.pt/%7Eltorgo/Regression/cal_housing.html)
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

|     |     |
| --- | --- |
| Args<br>---- |     |
| `version` | `"small"` or `"large"`. The small version contains 600 samples, the large version contains 20,640 samples. The purpose of the small version is to serve as an approximate replacement for the deprecated `boston_housing` dataset. |
| `path` | path where to cache the dataset locally (relative to `~/.keras/datasets`). |
| `test_split` | fraction of the data to reserve as test set. |
| `seed` | Random seed for shuffling the data before computing the test split. |

|     |
| --- |
| Returns<br>------- |     |
| Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`. |     |

**`x_train`, `x_test`**: numpy arrays with shape `(num_samples, 8)` containing either the training samples (for `x_train`), or test samples (for `y_train`).

**`y_train`, `y_test`**: numpy arrays of shape `(num_samples,)` containing the target scalars. The targets are float scalars typically between 25,000 and 500,000 that represent the home prices in dollars.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.