[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist/load_data#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist/load_data)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist/load_data?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist/load_data#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist/load_data#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.fashion\_mnist.load\_data Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist/load_data#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist/load_data#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/fashion_mnist.py#L12-L96)

Loads the Fashion-MNIST dataset.

tf.keras.datasets.fashion_mnist.load_data()

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data) | *   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [Introduction to the Keras Tuner](https://www.tensorflow.org/tutorials/keras/keras_tuner)<br>    <br>*   [Quantum data](https://www.tensorflow.org/quantum/tutorials/quantum_data)<br>    <br>*   [Examining the TensorFlow Graph](https://www.tensorflow.org/tensorboard/graphs) |

This is a dataset of 60,000 28x28 grayscale images of 10 fashion categories, along with a test set of 10,000 images. This dataset can be used as a drop-in replacement for MNIST.

#### The classes are:

| Label | Description |
| --- | --- |
| 0   | T-shirt/top |
| 1   | Trouser |
| 2   | Pullover |
| 3   | Dress |
| 4   | Coat |
| 5   | Sandal |
| 6   | Shirt |
| 7   | Sneaker |
| 8   | Bag |
| 9   | Ankle boot |

Returns
-------

Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`.

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes `(60000, 28, 28)`, containing the training data.

**`y_train`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(60000,)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes (10000, 28, 28), containing the test data.

**`y_test`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(10000,)` for the test data.

#### Example:

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    assert x_train.shape == (60000, 28, 28)
    assert x_test.shape == (10000, 28, 28)
    assert y_train.shape == (60000,)
    assert y_test.shape == (10000,)

#### License:

The copyright for Fashion-MNIST is held by Zalando SE. Fashion-MNIST is licensed under the [MIT license](https://github.com/zalandoresearch/fashion-mnist/blob/master/LICENSE)
.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.