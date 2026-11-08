[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar100/load_data#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar100/load_data)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar100/load_data?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar100/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar100/load_data#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.cifar100.load\_data Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar100/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar100/load_data#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/cifar100.py#L13-L86)

Loads the CIFAR100 dataset.

tf.keras.datasets.cifar100.load_data(
        label_mode='fine'
    )

This is a dataset of 50,000 32x32 color training images and 10,000 test images, labeled over 100 fine-grained classes that are grouped into 20 coarse-grained classes. See more info at the [CIFAR homepage](https://www.cs.toronto.edu/%7Ekriz/cifar.html)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `label_mode` | one of `"fine"`, `"coarse"`. If it is `"fine"`, the category labels are the fine-grained labels, and if it is `"coarse"`, the output labels are the coarse-grained superclasses. |

|     |
| --- |
| Returns<br>------- |     |
| Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`. |     |

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes `(50000, 32, 32, 3)`, containing the training data. Pixel values range from 0 to 255.

**`y_train`**: `uint8` NumPy array of labels (integers in range 0-99) with shape `(50000, 1)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes `(10000, 32, 32, 3)`, containing the test data. Pixel values range from 0 to 255.

**`y_test`**: `uint8` NumPy array of labels (integers in range 0-99) with shape `(10000, 1)` for the test data.

#### Example:

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar100.load_data()
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