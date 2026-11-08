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
 / MNIST digits classification dataset

MNIST digits classification dataset
===================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/mnist.py#L9)

### `load_data` function

Copied!

`keras.datasets.mnist.load_data(path="mnist.npz")`

Loads the MNIST dataset.

This is a dataset of 60,000 28x28 grayscale images of the 10 digits, along with a test set of 10,000 images. More info can be found at the [MNIST homepage](http://yann.lecun.com/exdb/mnist/)
.

**Arguments**

*   **path**: path where to cache the dataset locally (relative to `~/.keras/datasets`).

**Returns**

*   **Tuple of NumPy arrays**: `(x_train, y_train), (x_test, y_test)`.

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes `(60000, 28, 28)`, containing the training data. Pixel values range from 0 to 255.

**`y_train`**: `uint8` NumPy array of digit labels (integers in range 0-9) with shape `(60000,)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes `(10000, 28, 28)`, containing the test data. Pixel values range from 0 to 255.

**`y_test`**: `uint8` NumPy array of digit labels (integers in range 0-9) with shape `(10000,)` for the test data.

**Example**

Copied!

`(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data() assert x_train.shape == (60000, 28, 28) assert x_test.shape == (10000, 28, 28) assert y_train.shape == (60000,) assert y_test.shape == (10000,)`

License:

Yann LeCun and Corinna Cortes hold the copyright of MNIST dataset, which is a derivative work from original NIST datasets. MNIST dataset is made available under the terms of the [Creative Commons Attribution-Share Alike 3.0 license.](https://creativecommons.org/licenses/by-sa/3.0/)

* * *

[MNIST digits classification dataset](https://keras.io/api/datasets/mnist/#mnist-digits-classification-dataset)

[`load_data` function](https://keras.io/api/datasets/mnist/#loaddata-function)