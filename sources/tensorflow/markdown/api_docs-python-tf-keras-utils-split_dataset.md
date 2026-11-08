[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/split_dataset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/split_dataset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/split_dataset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/split_dataset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/split_dataset#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.split\_dataset Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/split_dataset#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/split_dataset#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/dataset_utils.py#L17-L86)

Splits a dataset into a left half and a right half (e.g. train / test).

tf.keras.utils.split_dataset(
        dataset,
        left_size=None,
        right_size=None,
        shuffle=False,
        seed=None,
        preferred_backend=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, a `torch.utils.data.Dataset` object, or a list/tuple of arrays with the same length. |
| `left_size` | If float (in the range `[0, 1]`), it signifies the fraction of the data to pack in the left dataset. If integer, it signifies the number of samples to pack in the left dataset. If `None`, defaults to the complement to `right_size`. Defaults to `None`. |
| `right_size` | If float (in the range `[0, 1]`), it signifies the fraction of the data to pack in the right dataset. If integer, it signifies the number of samples to pack in the right dataset. If `None`, defaults to the complement to `left_size`. Defaults to `None`. |
| `shuffle` | Boolean, whether to shuffle the data before splitting it. |
| `seed` | A random seed for shuffling. |
| `preferred_backend` | String, specifying which backend (e.g.; "tensorflow", "torch") to use. If `None`, the backend is inferred from the type of `dataset` - if `dataset` is a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, "tensorflow" backend is used, if `dataset` is a `torch.utils.data.Dataset`, "torch" backend is used, and if `dataset` is a list/tuple/np.array the current Keras backend is used. Defaults to `None`. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple of two dataset objects, the left and right splits. The exact type of the returned objects depends on the `preferred_backend`. For example, with a "tensorflow" backend, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> objects are returned. With a "torch" backend, `torch.utils.data.Dataset` objects are returned. |     |

#### Example:

    data = np.random.random(size=(1000, 4))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.