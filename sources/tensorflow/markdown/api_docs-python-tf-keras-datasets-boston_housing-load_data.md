[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing/load_data#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing/load_data)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing/load_data?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdatasets%2Fboston_housing%2Fload_data&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing/load_data#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.boston\_housing.load\_data Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing/load_data#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/boston_housing.py#L7-L74)

Loads the Boston Housing dataset.

tf.keras.datasets.boston_housing.load_data(
        path='boston_housing.npz', test_split=0.2, seed=113
    )

This is a dataset taken from the StatLib library which is maintained at Carnegie Mellon University.

Samples contain 13 attributes of houses at different locations around the Boston suburbs in the late 1970s. Targets are the median values of the houses at a location (in k$).

The attributes themselves are defined in the [StatLib website](http://lib.stat.cmu.edu/datasets/boston)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | path where to cache the dataset locally (relative to `~/.keras/datasets`). |
| `test_split` | fraction of the data to reserve as test set. |
| `seed` | Random seed for shuffling the data before computing the test split. |

|     |
| --- |
| Returns<br>------- |     |
| Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`. |     |

**x\_train, x\_test**: NumPy arrays with shape `(num_samples, 13)` containing either the training samples (for x\_train), or test samples (for y\_train).

**y\_train, y\_test**: NumPy arrays of shape `(num_samples,)` containing the target scalars. The targets are float scalars typically between 10 and 50 that represent the home prices in k$.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.