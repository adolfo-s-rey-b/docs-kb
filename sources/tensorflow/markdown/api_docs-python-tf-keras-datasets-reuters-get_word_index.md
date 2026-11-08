[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/reuters/get_word_index#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/reuters/get_word_index)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/reuters/get_word_index?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/reuters/get_word_index#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/reuters/get_word_index#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.reuters.get\_word\_index Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/reuters/get_word_index#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/reuters/get_word_index#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/reuters.py#L141-L168)

Retrieves a dict mapping words to their index in the Reuters dataset.

tf.keras.datasets.reuters.get_word_index(
        path='reuters_word_index.json'
    )

Actual word indices starts from 3, with 3 indices reserved for: 0 (padding), 1 (start), 2 (oov).

E.g. word index of 'the' is 1, but the in the actual training data, the index of 'the' will be 1 + 3 = 4. Vice versa, to translate word indices in training data back to words using this mapping, indices need to subtract 3.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | where to cache the data (relative to `~/.keras/dataset`). |

|     |
| --- |
| Returns<br>------- |     |
| The word index dictionary. Keys are word strings, values are their index. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.