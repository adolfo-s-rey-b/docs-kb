[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#methods)
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#get_config)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#on_epoch_end)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#to_json)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#__len__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.sequence.TimeseriesGenerator Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#returns)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#methods)
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#get_config)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#on_epoch_end)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#to_json)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator#__len__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/sequence.py#L12-L184)

Utility class for generating batches of temporal data.

Inherits From: [`PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)

tf.keras.preprocessing.sequence.TimeseriesGenerator(
        data,
        targets,
        length,
        sampling_rate=1,
        stride=1,
        start_index=0,
        end_index=None,
        shuffle=False,
        reverse=False,
        batch_size=128,
        **kwargs
    )

DEPRECATED.

This class takes in a sequence of data-points gathered at equal intervals, along with time series parameters such as stride, length of history, etc., to produce batches for training/validation.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `data` | Indexable generator (such as list or Numpy array) containing consecutive data points (timesteps). The data should be at 2D, and axis 0 is expected to be the time dimension. |
| `targets` | Targets corresponding to timesteps in `data`. It should have same length as `data`. |
| `length` | Length of the output sequences (in number of timesteps). |
| `sampling_rate` | Period between successive individual timesteps within sequences. For rate `r`, timesteps `data[i]`, `data[i-r]`, ... `data[i - length]` are used for create a sample sequence. |
| `stride` | Period between successive output sequences. For stride `s`, consecutive output samples would be centered around `data[i]`, `data[i+s]`, `data[i+2*s]`, etc. |
| `start_index` | Data points earlier than `start_index` will not be used in the output sequences. This is useful to reserve part of the data for test or validation. |
| `end_index` | Data points later than `end_index` will not be used in the output sequences. This is useful to reserve part of the data for test or validation. |
| `shuffle` | Whether to shuffle output samples, or instead draw them in chronological order. |
| `reverse` | Boolean: if `true`, timesteps in each output sample will be in reverse chronological order. |
| `batch_size` | Number of timeseries samples in each batch (except maybe the last one). |
| `**kwargs` | Additional keyword arguments for the `PyDataset` base class, such as `workers`, `use_multiprocessing`, and `max_queue_size`. |

|     |
| --- |
| Returns<br>------- |     |
| A PyDataset instance. |     |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `max_queue_size` |     |
| `num_batches` | Number of batches in the PyDataset. |
| `use_multiprocessing` |     |
| `workers` |     |

Methods
-------

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/sequence.py#L130-L167)

get_config()

Returns the TimeseriesGenerator configuration as Python dictionary.

|     |
| --- |
| Returns |     |
| A Python dictionary with the TimeseriesGenerator configuration. |     |

### `on_epoch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/data_adapters/py_dataset_adapter.py#L189-L191)

on_epoch_begin()

Method called at the beginning of every epoch.

### `on_epoch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/data_adapters/py_dataset_adapter.py#L193-L195)

on_epoch_end()

Method called at the end of every epoch.

### `to_json`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/sequence.py#L169-L184)

to_json(
        **kwargs
    )

Returns a JSON string containing the generator's configuration.

|     |     |
| --- | --- |
| Args |     |
| `**kwargs` | Additional keyword arguments to be passed to `json.dumps()`. |

|     |
| --- |
| Returns |     |
| A JSON string containing the tokenizer configuration. |     |

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/sequence.py#L105-L128)

__getitem__(
        index
    )

Gets batch at position `index`.

|     |     |
| --- | --- |
| Args |     |
| `index` | position of the batch in the PyDataset. |

|     |
| --- |
| Returns |     |
| A batch |     |

### `__iter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/data_adapters/py_dataset_adapter.py#L158-L171)

__iter__()

### `__len__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/sequence.py#L100-L103)

__len__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.