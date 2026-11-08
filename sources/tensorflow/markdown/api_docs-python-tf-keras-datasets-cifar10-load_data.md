[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.cifar10.load\_data Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/cifar10.py#L13-L106)

Loads the CIFAR10 dataset.

tf.keras.datasets.cifar10.load_data()

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers) | *   [Convolutional Neural Network (CNN)](https://www.tensorflow.org/tutorials/images/cnn) |

This is a dataset of 50,000 32x32 color training images and 10,000 test images, labeled over 10 categories. See more info at the [CIFAR homepage](https://www.cs.toronto.edu/%7Ekriz/cifar.html)
.

#### The classes are:

| Label | Description |
| --- | --- |
| 0   | airplane |
| 1   | automobile |
| 2   | bird |
| 3   | cat |
| 4   | deer |
| 5   | dog |
| 6   | frog |
| 7   | horse |
| 8   | ship |
| 9   | truck |

|     |
| --- |
| Returns<br>------- |     |
| Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`. |     |

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes `(50000, 32, 32, 3)`, containing the training data. Pixel values range from 0 to 255.

**`y_train`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(50000, 1)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes `(10000, 32, 32, 3)`, containing the test data. Pixel values range from 0 to 255.

**`y_test`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(10000, 1)` for the test data.

#### Example:

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
    assert x_train.shape == (50000, 32, 32, 3)
    assert x_test.shape == (10000, 32, 32, 3)
    assert y_train.shape == (50000, 1)
    assert y_test.shape == (10000, 1)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.