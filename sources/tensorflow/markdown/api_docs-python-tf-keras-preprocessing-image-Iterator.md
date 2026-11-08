[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#methods)
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#on_epoch_end)
        
    *   [reset](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#reset)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#__len__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.image.Iterator Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#methods)
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#on_epoch_end)
        
    *   [reset](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#reset)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#__len__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/image.py#L20-L126)

Base class for image data iterators.

Inherits From: [`PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)

tf.keras.preprocessing.image.Iterator(
        n, batch_size, shuffle, seed, **kwargs
    )

DEPRECATED.

Every `Iterator` must implement the `_get_batches_of_transformed_samples` method.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `n` | Integer, total number of samples in the dataset to loop over. |
| `batch_size` | Integer, size of a batch. |
| `shuffle` | Boolean, whether to shuffle the data between epochs. |
| `seed` | Random seeding for data shuffling. |
| `**kwargs` | Additional keyword arguments for the `PyDataset` base class, such as `workers`, `use_multiprocessing`, and `max_queue_size`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `max_queue_size` |     |
| `num_batches` | Number of batches in the PyDataset. |
| `use_multiprocessing` |     |
| `workers` |     |

Methods
-------

### `on_epoch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/data_adapters/py_dataset_adapter.py#L189-L191)

on_epoch_begin()

Method called at the beginning of every epoch.

### `on_epoch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/image.py#L77-L78)

on_epoch_end()

Method called at the end of every epoch.

### `reset`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/image.py#L80-L81)

reset()

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/image.py#L57-L72)

__getitem__(
        idx
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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/image.py#L106-L109)

__iter__()

### `__len__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/image.py#L74-L75)

__len__()

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| white\_list\_formats | `('png', 'jpg', 'jpeg', 'bmp', 'ppm', 'tif', 'tiff')` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.