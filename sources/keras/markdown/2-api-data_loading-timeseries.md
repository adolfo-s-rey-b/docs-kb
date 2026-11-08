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
 [Image data loading](https://keras.io/2/api/data_loading/image/)
 [Timeseries data loading](https://keras.io/2/api/data_loading/timeseries/)
 [Text data loading](https://keras.io/2/api/data_loading/text/)
 [Audio data loading](https://keras.io/2/api/data_loading/audio/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Data loading](https://keras.io/2/api/data_loading/)
 / Timeseries data loading

Timeseries data loading
=======================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/timeseries_dataset.py#L24)

### `timeseries_dataset_from_array` function

Copied!

`tf_keras.utils.timeseries_dataset_from_array(     data,     targets,     sequence_length,     sequence_stride=1,     sampling_rate=1,     batch_size=128,     shuffle=False,     seed=None,     start_index=None,     end_index=None, )`

Creates a dataset of sliding windows over a timeseries provided as array.

This function takes in a sequence of data-points gathered at equal intervals, along with time series parameters such as length of the sequences/windows, spacing between two sequence/windows, etc., to produce batches of timeseries inputs and targets.

**Arguments**

*   **data**: Numpy array or eager tensor containing consecutive data points (timesteps). Axis 0 is expected to be the time dimension.
*   **targets**: Targets corresponding to timesteps in `data`. `targets[i]` should be the target corresponding to the window that starts at index `i` (see example 2 below). Pass `None` if you don't have target data (in this case the dataset will only yield the input data).
*   **sequence\_length**: Length of the output sequences (in number of timesteps).
*   **sequence\_stride**: Period between successive output sequences. For stride `s`, output samples would start at index `data[i]`, `data[i + s]`, `data[i + 2 * s]`, etc.
*   **sampling\_rate**: Period between successive individual timesteps within sequences. For rate `r`, timesteps `data[i], data[i + r], ... data[i + sequence_length]` are used for creating a sample sequence.
*   **batch\_size**: Number of timeseries samples in each batch (except maybe the last one). If `None`, the data will not be batched (the dataset will yield individual samples).
*   **shuffle**: Whether to shuffle output samples, or instead draw them in chronological order.
*   **seed**: Optional int; random seed for shuffling.
*   **start\_index**: Optional int; data points earlier (exclusive) than `start_index` will not be used in the output sequences. This is useful to reserve part of the data for test or validation.
*   **end\_index**: Optional int; data points later (exclusive) than `end_index` will not be used in the output sequences. This is useful to reserve part of the data for test or validation.

**Returns**

A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 instance. If `targets` was passed, the dataset yields tuple `(batch_of_sequences, batch_of_targets)`. If not, the dataset yields only `batch_of_sequences`.

Example 1:

Consider indices `[0, 1, ... 98]`. With `sequence_length=10, sampling_rate=2, sequence_stride=3`, `shuffle=False`, the dataset will yield batches of sequences composed of the following indices:

Copied!

`First sequence:  [0  2  4  6  8 10 12 14 16 18] Second sequence: [3  5  7  9 11 13 15 17 19 21] Third sequence:  [6  8 10 12 14 16 18 20 22 24] ... Last sequence:   [78 80 82 84 86 88 90 92 94 96]`

In this case the last 2 data points are discarded since no full sequence can be generated to include them (the next sequence would have started at index 81, and thus its last step would have gone over 98).

Example 2: Temporal regression.

Consider an array `data` of scalar values, of shape `(steps,)`. To generate a dataset that uses the past 10 timesteps to predict the next timestep, you would use:

Copied!

`data = tf.range(15) sequence_length = 10 input_data = data[:] targets = data[sequence_length:] dataset = tf.keras.utils.timeseries_dataset_from_array(     input_data, targets, sequence_length=sequence_length ) for batch in dataset:   inputs, targets = batch   # First sequence: steps [0-9]   assert np.array_equal(inputs[0], data[:sequence_length])   # Corresponding target: step 10   assert np.array_equal(targets[0], data[sequence_length])   break # To view the generated dataset for batch in dataset.as_numpy_iterator():   input, label = batch   print(f"Input:{input}, target:{label}")`

Example 3: Temporal regression for many-to-many architectures.

Consider two arrays of scalar values `X` and `Y`, both of shape `(100,)`. The resulting dataset should consist samples with 20 timestamps each. The samples should not overlap. To generate a dataset that uses the current timestamp to predict the corresponding target timestep, you would use:

Copied!

`X = np.arange(100) Y = X*2  sample_length = 20 input_dataset = tf.keras.utils.timeseries_dataset_from_array(     X, None, sequence_length=sample_length, sequence_stride=sample_length) target_dataset = tf.keras.utils.timeseries_dataset_from_array(     Y, None, sequence_length=sample_length, sequence_stride=sample_length)  for batch in zip(input_dataset, target_dataset):     inputs, targets = batch     assert np.array_equal(inputs[0], X[:sample_length])      # second sample equals output timestamps 20-40     assert np.array_equal(targets[1], Y[sample_length:2*sample_length])     break`

* * *

[Timeseries data loading](https://keras.io/2/api/data_loading/timeseries/#timeseries-data-loading)

[`timeseries_dataset_from_array` function](https://keras.io/2/api/data_loading/timeseries/#timeseriesdatasetfromarray-function)