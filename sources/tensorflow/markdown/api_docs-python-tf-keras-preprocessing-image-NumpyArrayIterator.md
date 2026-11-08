[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fpreprocessing%2Fimage%2FNumpyArrayIterator&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#methods)
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#on_epoch_end)
        
    *   [reset](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#reset)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#__len__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.image.NumpyArrayIterator Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#methods)
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#on_epoch_end)
        
    *   [reset](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#reset)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#__len__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/image.py#L519-L678)

Iterator yielding data from a Numpy array.

Inherits From: [`Iterator`](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/Iterator)
, [`PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)

tf.keras.preprocessing.image.NumpyArrayIterator(
        x,
        y,
        image_data_generator,
        batch_size=32,
        shuffle=False,
        sample_weight=None,
        seed=None,
        data_format=None,
        save_to_dir=None,
        save_prefix='',
        save_format='png',
        subset=None,
        ignore_class_split=False,
        dtype=None
    )

DEPRECATED.

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