[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/get_word_index#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/get_word_index)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/get_word_index?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdatasets%2Fimdb%2Fget_word_index&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/get_word_index#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/get_word_index#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.imdb.get\_word\_index Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/get_word_index#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/get_word_index#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/imdb.py#L147-L192)

Retrieves a dict mapping words to their index in the IMDB dataset.

tf.keras.datasets.imdb.get_word_index(
        path='imdb_word_index.json'
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | where to cache the data (relative to `~/.keras/dataset`). |

|     |
| --- |
| Returns<br>------- |     |
| The word index dictionary. Keys are word strings, values are their index. |     |

#### Example:

# Use the default parameters to keras.datasets.imdb.load_data
    start_char = 1
    oov_char = 2
    index_from = 3
    # Retrieve the training sequences.
    (x_train, _), _ = keras.datasets.imdb.load_data(
        start_char=start_char, oov_char=oov_char, index_from=index_from
    )
    # Retrieve the word index file mapping words to indices
    word_index = keras.datasets.imdb.get_word_index()
    # Reverse the word index to obtain a dict mapping indices to words
    # And add `index_from` to indices to sync with `x_train`
    inverted_word_index = dict(
        (i + index_from, word) for (word, i) in word_index.items()
    )
    # Update `inverted_word_index` to include `start_char` and `oov_char`
    inverted_word_index[start_char] = "[START]"
    inverted_word_index[oov_char] = "[OOV]"
    # Decode the first sequence in the dataset
    decoded_sequence = " ".join(inverted_word_index[i] for i in x_train[0])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.