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
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)
 [Model plotting utilities](https://keras.io/2/api/utils/model_plotting_utils/)
 [Structured data preprocessing utilities](https://keras.io/2/api/utils/feature_space/)
 [Python & NumPy utilities](https://keras.io/2/api/utils/python_utils/)
 [Backend utilities](https://keras.io/2/api/utils/backend_utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Utilities](https://keras.io/2/api/utils/)
 / Python & NumPy utilities

Python & NumPy utilities
========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/tf_utils.py#L39)

### `set_random_seed` function

Copied!

`tf_keras.utils.set_random_seed(seed)`

Sets all random seeds for the program (Python, NumPy, and TensorFlow).

You can use this utility to make almost any TF-Keras program fully deterministic. Some limitations apply in cases where network communications are involved (e.g. parameter server distribution), which creates additional sources of randomness, or when certain non-deterministic cuDNN ops are involved.

Calling this utility is equivalent to the following:

Copied!

`import random import numpy as np import tensorflow as tf random.seed(seed) np.random.seed(seed) tf.random.set_seed(seed)`

**Arguments**

*   **seed**: Integer, the random seed to use.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/dataset_utils.py#L32)

### `split_dataset` function

Copied!

`tf_keras.utils.split_dataset(     dataset, left_size=None, right_size=None, shuffle=False, seed=None )`

Split a dataset into a left half and a right half (e.g. train / test).

**Arguments**

*   **dataset**: A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
     object, or a list/tuple of arrays with the same length.
*   **left\_size**: If float (in the range `[0, 1]`), it signifies the fraction of the data to pack in the left dataset. If integer, it signifies the number of samples to pack in the left dataset. If `None`, it uses the complement to `right_size`. Defaults to `None`.
*   **right\_size**: If float (in the range `[0, 1]`), it signifies the fraction of the data to pack in the right dataset. If integer, it signifies the number of samples to pack in the right dataset. If `None`, it uses the complement to `left_size`. Defaults to `None`.
*   **shuffle**: Boolean, whether to shuffle the data before splitting it.
*   **seed**: A random seed for shuffling.

**Returns**

*   **A tuple of two [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
     objects**: the left and right splits.

**Example**

Copied!

`>>> data = np.random.random(size=(1000, 4)) >>> left_ds, right_ds = tf.keras.utils.split_dataset(data, left_size=0.8) >>> int(left_ds.cardinality()) 800 >>> int(right_ds.cardinality()) 200`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/data_utils.py#L193)

### `get_file` function

Copied!

`tf_keras.utils.get_file(     fname=None,     origin=None,     untar=False,     md5_hash=None,     file_hash=None,     cache_subdir="datasets",     hash_algorithm="auto",     extract=False,     archive_format="auto",     cache_dir=None, )`

Downloads a file from a URL if it not already in the cache.

By default the file at the url `origin` is downloaded to the cache\_dir `~/.keras`, placed in the cache\_subdir `datasets`, and given the filename `fname`. The final location of a file `example.txt` would therefore be `~/.keras/datasets/example.txt`.

Files in tar, tar.gz, tar.bz, and zip formats can also be extracted. Passing a hash will verify the file after download. The command line programs `shasum` and `sha256sum` can compute the hash.

**Example**

Copied!

`path_to_downloaded_file = tf.keras.utils.get_file(     origin="https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz",     extract=True, )`

**Arguments**

*   **fname**: Name of the file. If an absolute path `/path/to/file.txt` is specified the file will be saved at that location. If `None`, the name of the file at `origin` will be used.
*   **origin**: Original URL of the file.
*   **untar**: Deprecated in favor of `extract` argument. boolean, whether the file should be decompressed
*   **md5\_hash**: Deprecated in favor of `file_hash` argument. md5 hash of the file for verification
*   **file\_hash**: The expected hash string of the file after download. The sha256 and md5 hash algorithms are both supported.
*   **cache\_subdir**: Subdirectory under the TF-Keras cache dir where the file is saved. If an absolute path `/path/to/folder` is specified the file will be saved at that location.
*   **hash\_algorithm**: Select the hash algorithm to verify the file. options are `'md5'`, `'sha256'`, and `'auto'`. The default 'auto' detects the hash algorithm in use.
*   **extract**: True tries extracting the file as an Archive, like tar or zip.
*   **archive\_format**: Archive format to try for extracting the file. Options are `'auto'`, `'tar'`, `'zip'`, and `None`. `'tar'` includes tar, tar.gz, and tar.bz files. The default `'auto'` corresponds to `['tar', 'zip']`. None or an empty list will return no matches found.
*   **cache\_dir**: Location to store cached files, when None it defaults to `~/.keras/`.

**Returns**

Path to the downloaded file.

⚠️ **Warning on malicious downloads** ⚠️

Downloading something from the Internet carries a risk. NEVER download a file/archive if you do not trust the source. We recommend that you specify the `file_hash` argument (if the hash of the source file is known) to make sure that the file you are getting is the one you expect.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/generic_utils.py#L127)

### `Progbar` class

Copied!

`tf_keras.utils.Progbar(     target, width=30, verbose=1, interval=0.05, stateful_metrics=None, unit_name="step" )`

Displays a progress bar.

**Arguments**

*   **target**: Total number of steps expected, None if unknown.
*   **width**: Progress bar width on screen.
*   **verbose**: Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose)
*   **stateful\_metrics**: Iterable of string names of metrics that should _not_ be averaged over time. Metrics in this list will be displayed as-is. All others will be averaged by the progbar before display.
*   **interval**: Minimum visual progress update interval (in seconds).
*   **unit\_name**: Display name for step counts (usually "step" or "sample").

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/data_utils.py#L492)

### `Sequence` class

Copied!

`tf_keras.utils.Sequence()`

Base object for fitting to a sequence of data, such as a dataset.

Every `Sequence` must implement the `__getitem__` and the `__len__` methods. If you want to modify your dataset between epochs, you may implement `on_epoch_end`. The method `__getitem__` should return a complete batch.

Notes:

`Sequence` is a safer way to do multiprocessing. This structure guarantees that the network will only train once on each sample per epoch, which is not the case with generators.

**Examples**

Copied!

``from skimage.io import imread from skimage.transform import resize import numpy as np import math  # Here, `x_set` is list of path to the images # and `y_set` are the associated classes.  class CIFAR10Sequence(tf.keras.utils.Sequence):      def __init__(self, x_set, y_set, batch_size):         self.x, self.y = x_set, y_set         self.batch_size = batch_size      def __len__(self):         return math.ceil(len(self.x) / self.batch_size)      def __getitem__(self, idx):         low = idx * self.batch_size         # Cap upper bound at array length; the last batch may be smaller         # if the total number of items is not a multiple of batch size.         high = min(low + self.batch_size, len(self.x))         batch_x = self.x[low:high]         batch_y = self.y[low:high]          return np.array([             resize(imread(file_name), (200, 200))                for file_name in batch_x]), np.array(batch_y)``

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/np_utils.py#L23)

### `to_categorical` function

Copied!

`tf_keras.utils.to_categorical(y, num_classes=None, dtype="float32")`

Converts a class vector (integers) to binary class matrix.

E.g. for use with `categorical_crossentropy`.

**Arguments**

*   **y**: Array-like with class values to be converted into a matrix (integers from 0 to `num_classes - 1`).
*   **num\_classes**: Total number of classes. If `None`, this would be inferred as `max(y) + 1`.
*   **dtype**: The data type expected by the input. Default: `'float32'`.

**Returns**

A binary matrix representation of the input as a NumPy array. The class axis is placed last.

**Example**

Copied!

`>>> a = tf.keras.utils.to_categorical([0, 1, 2, 3], num_classes=4) >>> print(a) [[1. 0. 0. 0.]  [0. 1. 0. 0.]  [0. 0. 1. 0.]  [0. 0. 0. 1.]]`

Copied!

`>>> b = tf.constant([.9, .04, .03, .03, ...                  .3, .45, .15, .13, ...                  .04, .01, .94, .05, ...                  .12, .21, .5, .17], ...                 shape=[4, 4]) >>> loss = tf.keras.backend.categorical_crossentropy(a, b) >>> print(np.around(loss, 5)) [0.10536 0.82807 0.1011  1.77196]`

Copied!

`>>> loss = tf.keras.backend.categorical_crossentropy(a, a) >>> print(np.around(loss, 5)) [0. 0. 0. 0.]`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/np_utils.py#L80)

### `to_ordinal` function

Copied!

`tf_keras.utils.to_ordinal(y, num_classes=None, dtype="float32")`

Converts a class vector (integers) to an ordinal regression matrix.

This utility encodes class vector to ordinal regression/classification matrix where each sample is indicated by a row and rank of that sample is indicated by number of ones in that row.

**Arguments**

*   **y**: Array-like with class values to be converted into a matrix (integers from 0 to `num_classes - 1`).
*   **num\_classes**: Total number of classes. If `None`, this would be inferred as `max(y) + 1`.
*   **dtype**: The data type expected by the input. Default: `'float32'`.

**Returns**

An ordinal regression matrix representation of the input as a NumPy array. The class axis is placed last.

**Example**

Copied!

`>>> a = tf.keras.utils.to_ordinal([0, 1, 2, 3], num_classes=4) >>> print(a) [[0. 0. 0.]  [1. 0. 0.]  [1. 1. 0.]  [1. 1. 1.]]`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/np_utils.py#L128)

### `normalize` function

Copied!

`tf_keras.utils.normalize(x, axis=-1, order=2)`

Normalizes a Numpy array.

**Arguments**

*   **x**: Numpy array to normalize.
*   **axis**: axis along which to normalize.
*   **order**: Normalization order (e.g. `order=2` for L2 norm).

**Returns**

A normalized copy of the array.

* * *

[Python & NumPy utilities](https://keras.io/2/api/utils/python_utils/#python-amp-numpy-utilities)

[`set_random_seed` function](https://keras.io/2/api/utils/python_utils/#setrandomseed-function)

[`split_dataset` function](https://keras.io/2/api/utils/python_utils/#splitdataset-function)

[`get_file` function](https://keras.io/2/api/utils/python_utils/#getfile-function)

[`Progbar` class](https://keras.io/2/api/utils/python_utils/#progbar-class)

[`Sequence` class](https://keras.io/2/api/utils/python_utils/#sequence-class)

[`to_categorical` function](https://keras.io/2/api/utils/python_utils/#tocategorical-function)

[`to_ordinal` function](https://keras.io/2/api/utils/python_utils/#toordinal-function)

[`normalize` function](https://keras.io/2/api/utils/python_utils/#normalize-function)