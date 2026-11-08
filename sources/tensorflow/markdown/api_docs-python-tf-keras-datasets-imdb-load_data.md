[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.imdb.load\_data Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/imdb.py#L13-L144)

Loads the [IMDB dataset](https://ai.stanford.edu/%7Eamaas/data/sentiment/)
.

tf.keras.datasets.imdb.load_data(
        path='imdb.npz',
        num_words=None,
        skip_top=0,
        maxlen=None,
        seed=113,
        start_char=1,
        oov_char=2,
        index_from=3,
        **kwargs
    )

This is a dataset of 25,000 movies reviews from IMDB, labeled by sentiment (positive/negative). Reviews have been preprocessed, and each review is encoded as a list of word indexes (integers). For convenience, words are indexed by overall frequency in the dataset, so that for instance the integer "3" encodes the 3rd most frequent word in the data. This allows for quick filtering operations such as: "only consider the top 10,000 most common words, but eliminate the top 20 most common words".

As a convention, "0" does not stand for a specific word, but instead is used to encode the pad token.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | where to cache the data (relative to `~/.keras/dataset`). |
| `num_words` | integer or None. Words are ranked by how often they occur (in the training set) and only the `num_words` most frequent words are kept. Any less frequent word will appear as `oov_char` value in the sequence data. If None, all words are kept. Defaults to `None`. |
| `skip_top` | skip the top N most frequently occurring words (which may not be informative). These words will appear as `oov_char` value in the dataset. When 0, no words are skipped. Defaults to `0`. |
| `maxlen` | int or None. Maximum sequence length. Any longer sequence will be truncated. None, means no truncation. Defaults to `None`. |
| `seed` | int. Seed for reproducible data shuffling. |
| `start_char` | int. The start of a sequence will be marked with this character. 0 is usually the padding character. Defaults to `1`. |
| `oov_char` | int. The out-of-vocabulary character. Words that were cut out because of the `num_words` or `skip_top` limits will be replaced with this character. |
| `index_from` | int. Index actual words with this index and higher. |

|     |
| --- |
| Returns<br>------- |     |
| Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`. |     |

**`x_train`, `x_test`**: lists of sequences, which are lists of indexes (integers). If the num\_words argument was specific, the maximum possible index value is `num_words - 1`. If the `maxlen` argument was specified, the largest possible sequence length is `maxlen`.

**`y_train`, `y_test`**: lists of integer labels (1 or 0).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.