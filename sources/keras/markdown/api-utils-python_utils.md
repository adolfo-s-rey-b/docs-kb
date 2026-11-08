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
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)
 [Experiment management utilities](https://keras.io/api/utils/experiment_management_utils/)
 [Model plotting utilities](https://keras.io/api/utils/model_plotting_utils/)
 [Structured data preprocessing utilities](https://keras.io/api/utils/feature_space/)
 [Tensor utilities](https://keras.io/api/utils/tensor_utils/)
 [Bounding boxes](https://keras.io/api/utils/bounding_boxes/)
 [Python & NumPy utilities](https://keras.io/api/utils/python_utils/)
 [Bounding boxes utilities](https://keras.io/api/utils/bounding_boxes_utils/)
 [Visualization utilities](https://keras.io/api/utils/visualization_utils/)
 [Preprocessing utilities](https://keras.io/api/utils/preprocessing_utils/)
 [Backend utilities](https://keras.io/api/utils/backend_utils/)
 [Scikit-Learn API wrappers](https://keras.io/api/utils/sklearn_wrappers/)
 [Keras configuration utilities](https://keras.io/api/utils/config_utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Utilities](https://keras.io/api/utils/)
 / Python & NumPy utilities

Python & NumPy utilities
========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/rng_utils.py#L14)

### `set_random_seed` function

Copied!

`keras.utils.set_random_seed(seed)`

Sets all random seeds (Python, NumPy, and backend framework, e.g. TF).

You can use this utility to make almost any Keras program fully deterministic. Some limitations apply in cases where network communications are involved (e.g. parameter server distribution), which creates additional sources of randomness, or when certain non-deterministic cuDNN ops are involved.

Calling this utility does the following:

Copied!

`import random random.seed(seed)  import numpy as np np.random.seed(seed)  import tensorflow as tf  # Only if TF is installed tf.random.set_seed(seed)  import torch  # Only if the backend is 'torch' torch.manual_seed(seed)`

Additionally, it resets the global Keras `SeedGenerator`, which is used by `keras.random` functions when the `seed` is not provided.

Note that the TensorFlow seed is set even if you're not using TensorFlow as your backend framework, since many workflows leverage [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 pipelines (which feature random shuffling). Likewise many workflows might leverage NumPy APIs.

**Arguments**

*   **seed**: Integer, the random seed to use.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/dataset_utils.py#L17)

### `split_dataset` function

Copied!

`keras.utils.split_dataset(     dataset,     left_size=None,     right_size=None,     shuffle=False,     seed=None,     preferred_backend=None, )`

Splits a dataset into a left half and a right half (e.g. train / test).

**Arguments**

*   **dataset**: A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    , a `torch.utils.data.Dataset` object, or a list/tuple of arrays with the same length.
*   **left\_size**: If float (in the range `[0, 1]`), it signifies the fraction of the data to pack in the left dataset. If integer, it signifies the number of samples to pack in the left dataset. If `None`, defaults to the complement to `right_size`. Defaults to `None`.
*   **right\_size**: If float (in the range `[0, 1]`), it signifies the fraction of the data to pack in the right dataset. If integer, it signifies the number of samples to pack in the right dataset. If `None`, defaults to the complement to `left_size`. Defaults to `None`.
*   **shuffle**: Boolean, whether to shuffle the data before splitting it.
*   **seed**: A random seed for shuffling.
*   **preferred\_backend**: String, specifying which backend (e.g.; "tensorflow", "torch") to use. If `None`, the backend is inferred from the type of `dataset` - if `dataset` is a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    , "tensorflow" backend is used, if `dataset` is a `torch.utils.data.Dataset`, "torch" backend is used, and if `dataset` is a list/tuple/np.array the current Keras backend is used. Defaults to `None`.

**Returns**

A tuple of two dataset objects, the left and right splits. The exact type of the returned objects depends on the `preferred_backend`. For example, with a "tensorflow" backend, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 objects are returned. With a "torch" backend, `torch.utils.data.Dataset` objects are returned.

**Example**

Copied!

`>>> data = np.random.random(size=(1000, 4)) >>> left_ds, right_ds = keras.utils.split_dataset(data, left_size=0.8) >>> # For a tf.data.Dataset, you can use .cardinality() >>> # >>> int(left_ds.cardinality()) >>> # 800 >>> # For a torch.utils.data.Dataset, you can use len() >>> # >>> len(left_ds) >>> # 800`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/data_adapters/data_adapter_utils.py#L54)

### `pack_x_y_sample_weight` function

Copied!

`keras.utils.pack_x_y_sample_weight(x, y=None, sample_weight=None)`

Packs user-provided data into a tuple.

This is a convenience utility for packing data into the tuple formats that `Model.fit()` uses.

**Example**

Copied!

`>>> x = ops.ones((10, 1)) >>> data = pack_x_y_sample_weight(x) >>> isinstance(data, ops.Tensor) True >>> y = ops.ones((10, 1)) >>> data = pack_x_y_sample_weight(x, y) >>> isinstance(data, tuple) True >>> x, y = data`

**Arguments**

*   **x**: Features to pass to `Model`.
*   **y**: Ground-truth targets to pass to `Model`.
*   **sample\_weight**: Sample weight for each element.

**Returns**

Tuple in the format used in `Model.fit()`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/data_adapters/data_adapter_utils.py#L11)

### `unpack_x_y_sample_weight` function

Copied!

`keras.utils.unpack_x_y_sample_weight(data)`

Unpacks user-provided data tuple.

This is a convenience utility to be used when overriding `Model.train_step`, `Model.test_step`, or `Model.predict_step`. This utility makes it easy to support data of the form `(x,)`, `(x, y)`, or `(x, y, sample_weight)`.

**Example**

Copied!

``>>> features_batch = ops.ones((10, 5)) >>> labels_batch = ops.zeros((10, 5)) >>> data = (features_batch, labels_batch) >>> # `y` and `sample_weight` will default to `None` if not provided. >>> x, y, sample_weight = unpack_x_y_sample_weight(data) >>> sample_weight is None True``

**Arguments**

*   **data**: A tuple of the form `(x,)`, `(x, y)`, or `(x, y, sample_weight)`.

**Returns**

The unpacked tuple, with `None`s for `y` and `sample_weight` if they are not provided.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/file_utils.py#L213)

### `get_file` function

Copied!

`keras.utils.get_file(     fname=None,     origin=None,     untar=False,     md5_hash=None,     file_hash=None,     cache_subdir="datasets",     hash_algorithm="auto",     extract=False,     archive_format="auto",     cache_dir=None,     force_download=False, )`

Downloads a file from a URL if it not already in the cache.

By default the file at the url `origin` is downloaded to the cache\_dir `~/.keras`, placed in the cache\_subdir `datasets`, and given the filename `fname`. The final location of a file `example.txt` would therefore be `~/.keras/datasets/example.txt`. Files in `.tar`, `.tar.gz`, `.tar.bz`, and `.zip` formats can also be extracted.

Passing a hash will verify the file after download. The command line programs `shasum` and `sha256sum` can compute the hash.

**Example**

Copied!

`path_to_downloaded_file = get_file(     origin="https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz",     extract=True )`

**Arguments**

*   **fname**: If the target is a single file, this is your desired local name for the file. If `None`, the name of the file at `origin` will be used. If downloading and extracting a directory archive, the provided `fname` will be used as extraction directory name (only if it doesn't have an extension).
*   **origin**: Original URL of the file.
*   **untar**: Deprecated in favor of `extract` argument. Boolean, whether the file is a tar archive that should be extracted.
*   **md5\_hash**: Deprecated in favor of `file_hash` argument. md5 hash of the file for file integrity verification.
*   **file\_hash**: The expected hash string of the file after download. The sha256 and md5 hash algorithms are both supported.
*   **cache\_subdir**: Subdirectory under the Keras cache dir where the file is saved. If an absolute path, e.g. `"/path/to/folder"` is specified, the file will be saved at that location.
*   **hash\_algorithm**: Select the hash algorithm to verify the file. options are `"md5'`, `"sha256'`, and `"auto'`. The default 'auto' detects the hash algorithm in use.
*   **extract**: If `True`, extracts the archive. Only applicable to compressed archive files like tar or zip.
*   **archive\_format**: Archive format to try for extracting the file. Options are `"auto'`, `"tar'`, `"zip'`, and `None`. `"tar"` includes tar, tar.gz, and tar.bz files. The default `"auto"` corresponds to `["tar", "zip"]`. None or an empty list will return no matches found.
*   **cache\_dir**: Location to store cached files, when None it defaults ether `$KERAS_HOME` if the `KERAS_HOME` environment variable is set or `~/.keras/`.
*   **force\_download**: If `True`, the file will always be re-downloaded regardless of the cache state.

**Returns**

Path to the downloaded file.

**⚠️ Warning on malicious downloads ⚠️**

Downloading something from the Internet carries a risk. NEVER download a file/archive if you do not trust the source. We recommend that you specify the `file_hash` argument (if the hash of the source file is known) to make sure that the file you are getting is the one you expect.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/progbar.py#L12)

### `Progbar` class

Copied!

`keras.utils.Progbar(     target,     width=20,     verbose=1,     interval=0.05,     stateful_metrics=None,     stateless_metrics=None,     unit_name="step", )`

Displays a progress bar.

If neither of `stateful_metrics` and `stateless_metrics` is provided, all metrics are assumed to be stateless (averaged by the progress bar before display).

**Arguments**

*   **target**: Total number of steps expected, None if unknown.
*   **width**: Progress bar width on screen.
*   **verbose**: Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose)
*   **stateful\_metrics**: Iterable of string names of metrics that should _not_ be averaged over time. Metrics in this list will be displayed as-is. If provided, do not provide `stateless_metrics`.
*   **stateless\_metrics**: Iterable of string names of metrics that _should_ be averaged over time. Metrics in this list will be averaged by the progbar before display. If provided, do not provide `stateful_metrics`.
*   **interval**: Minimum visual progress update interval (in seconds).
*   **unit\_name**: Display name for step counts (usually "step" or "sample").

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/numerical_utils.py#L38)

### `to_categorical` function

Copied!

`keras.utils.to_categorical(x, num_classes=None)`

Converts a class vector (integers) to binary class matrix.

E.g. for use with `categorical_crossentropy`.

**Arguments**

*   **x**: Array-like with class values to be converted into a matrix (integers from 0 to `num_classes - 1`).
*   **num\_classes**: Total number of classes. If `None`, this would be inferred as `max(x) + 1`. Defaults to `None`.

**Returns**

A binary matrix representation of the input as a NumPy array. The class axis is placed last.

**Example**

Copied!

`>>> a = keras.utils.to_categorical([0, 1, 2, 3], num_classes=4) >>> print(a) [[1. 0. 0. 0.]  [0. 1. 0. 0.]  [0. 0. 1. 0.]  [0. 0. 0. 1.]]`

Copied!

`>>> b = np.array([.9, .04, .03, .03, ...               .3, .45, .15, .13, ...               .04, .01, .94, .05, ...               .12, .21, .5, .17]).reshape(4,4) >>> loss = keras.ops.categorical_crossentropy(a, b) >>> print(np.around(loss, 5)) [0.10536 0.82807 0.1011  1.77196]`

Copied!

`>>> loss = keras.ops.categorical_crossentropy(a, a) >>> print(np.around(loss, 5)) [0. 0. 0. 0.]`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/numerical_utils.py#L8)

### `normalize` function

Copied!

`keras.utils.normalize(x, axis=-1, order=2)`

Normalizes an array.

If the input is a NumPy array, a NumPy array will be returned. If it's a backend tensor, a backend tensor will be returned.

**Arguments**

*   **x**: Array to normalize.
*   **axis**: axis along which to normalize.
*   **order**: Normalization order (e.g. `order=2` for L2 norm).

**Returns**

A normalized copy of the array.

* * *

[Python & NumPy utilities](https://keras.io/api/utils/python_utils/#python-amp-numpy-utilities)

[`set_random_seed` function](https://keras.io/api/utils/python_utils/#setrandomseed-function)

[`split_dataset` function](https://keras.io/api/utils/python_utils/#splitdataset-function)

[`pack_x_y_sample_weight` function](https://keras.io/api/utils/python_utils/#packxysampleweight-function)

[`unpack_x_y_sample_weight` function](https://keras.io/api/utils/python_utils/#unpackxysampleweight-function)

[`get_file` function](https://keras.io/api/utils/python_utils/#getfile-function)

[`Progbar` class](https://keras.io/api/utils/python_utils/#progbar-class)

[`to_categorical` function](https://keras.io/api/utils/python_utils/#tocategorical-function)

[`normalize` function](https://keras.io/api/utils/python_utils/#normalize-function)