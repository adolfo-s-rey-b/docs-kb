[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fpreprocessing%2Ftimeseries_dataset_from_array&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.timeseries\_dataset\_from\_array Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/timeseries_dataset_utils.py#L9-L232)

Creates a dataset of sliding windows over a timeseries provided as array.

#### View aliases

**Main aliases**

[`tf.keras.utils.timeseries_dataset_from_array`](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/timeseries_dataset_from_array)

tf.keras.preprocessing.timeseries_dataset_from_array(
        data,
        targets,
        sequence_length,
        sequence_stride=1,
        sampling_rate=1,
        batch_size=128,
        shuffle=False,
        seed=None,
        start_index=None,
        end_index=None,
        format='tf'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series) |

This function takes in a sequence of data-points gathered at equal intervals, along with time series parameters such as length of the sequences/windows, spacing between two sequence/windows, etc., to produce batches of timeseries inputs and targets.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | Numpy array or eager tensor containing consecutive data points (timesteps). Axis 0 is expected to be the time dimension. |
| `targets` | Targets corresponding to timesteps in `data`. `targets[i]` should be the target corresponding to the window that starts at index `i` (see example 2 below). Pass `None` if you don't have target data (in this case the dataset will only yield the input data). |
| `sequence_length` | Length of the output sequences (in number of timesteps). |
| `sequence_stride` | Period between successive output sequences. For stride `s`, output samples would start at index `data[i]`, `data[i + s]`, `data[i + 2 * s]`, etc. |
| `sampling_rate` | Period between successive individual timesteps within sequences. For rate `r`, timesteps `data[i], data[i + r], ... data[i + sequence_length]` are used for creating a sample sequence. |
| `batch_size` | Number of timeseries samples in each batch (except maybe the last one). If `None`, the data will not be batched (the dataset will yield individual samples). |
| `shuffle` | Whether to shuffle output samples, or instead draw them in chronological order. |
| `seed` | Optional int; random seed for shuffling. |
| `start_index` | Optional int; data points earlier (exclusive) than `start_index` will not be used in the output sequences. This is useful to reserve part of the data for test or validation. |
| `end_index` | Optional int; data points later (exclusive) than `end_index` will not be used in the output sequences. This is useful to reserve part of the data for test or validation. |
| `format` | Optional string; either `"tf"` (default) for a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, or `"grain"` for a Grain dataset. Grain datasets are framework-agnostic and work with JAX, PyTorch, and NumPy backends without requiring TensorFlow. |

Returns
-------

A dataset instance. If `format="tf"`, returns a `tf.data.Dataset`. If `format="grain"`, returns a Grain `IterDataset` (or `MapDataset` when `batch_size` is `None`). If `targets` was passed, the dataset yields tuple `(batch_of_sequences, batch_of_targets)`. If not, the dataset yields only `batch_of_sequences`.

#### Example 1:

Consider indices `[0, 1, ... 98]`. With `sequence_length=10, sampling_rate=2, sequence_stride=3`, `shuffle=False`, the dataset will yield batches of sequences composed of the following indices:

First sequence:  [0  2  4  6  8 10 12 14 16 18]
    Second sequence: [3  5  7  9 11 13 15 17 19 21]
    Third sequence:  [6  8 10 12 14 16 18 20 22 24]
    ...
    Last sequence:   [78 80 82 84 86 88 90 92 94 96]

In this case the last 2 data points are discarded since no full sequence can be generated to include them (the next sequence would have started at index 81, and thus its last step would have gone over 98).

Example 2: Temporal regression.

Consider an array `data` of scalar values, of shape `(steps,)`. To generate a dataset that uses the past 10 timesteps to predict the next timestep, you would use:

input_data = data[:-10]
    targets = data[10:]
    dataset = timeseries_dataset_from_array(
        input_data, targets, sequence_length=10)
    for batch in dataset:
      inputs, targets = batch
      assert np.array_equal(inputs[0], data[:10])  # First sequence: steps [0-9]
      # Corresponding target: step 10
      assert np.array_equal(targets[0], data[10])
      break

Example 3: Temporal regression for many-to-many architectures.

Consider two arrays of scalar values `X` and `Y`, both of shape `(100,)`. The resulting dataset should consist samples with 20 timestamps each. The samples should not overlap. To generate a dataset that uses the current timestamp to predict the corresponding target timestep, you would use:

X = np.arange(100)
    Y = X*2
    
    sample_length = 20
    input_dataset = timeseries_dataset_from_array(
        X, None, sequence_length=sample_length, sequence_stride=sample_length)
    target_dataset = timeseries_dataset_from_array(
        Y, None, sequence_length=sample_length, sequence_stride=sample_length)
    
    for batch in zip(input_dataset, target_dataset):
        inputs, targets = batch
        assert np.array_equal(inputs[0], X[:sample_length])
    
        # second sample equals output timestamps 20-40
        assert np.array_equal(targets[1], Y[sample_length:2*sample_length])
        break

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.