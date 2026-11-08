[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fpreprocessing%2Fsequence%2Fskipgrams&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#returns)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#note)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.sequence.skipgrams Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#returns)
    
*   [Note](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/skipgrams#note)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/sequence.py#L229-L328)

Generates skipgram word pairs.

tf.keras.preprocessing.sequence.skipgrams(
        sequence,
        vocabulary_size,
        window_size=4,
        negative_samples=1.0,
        shuffle=True,
        categorical=False,
        sampling_table=None,
        seed=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [word2vec](https://www.tensorflow.org/text/tutorials/word2vec) |

DEPRECATED.

This function transforms a sequence of word indexes (list of integers) into tuples of words of the form:

*   (word, word in the same window), with label 1 (positive samples).
*   (word, random word from the vocabulary), with label 0 (negative samples).

Read more about Skipgram in this gnomic paper by Mikolov et al.: [Efficient Estimation of Word Representations in Vector Space](http://arxiv.org/pdf/1301.3781v3.pdf)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sequence` | A word sequence (sentence), encoded as a list of word indices (integers). If using a `sampling_table`, word indices are expected to match the rank of the words in a reference dataset (e.g. 10 would encode the 10-th most frequently occurring token). Note that index 0 is expected to be a non-word and will be skipped. |
| `vocabulary_size` | Int, maximum possible word index + 1 |
| `window_size` | Int, size of sampling windows (technically half-window). The window of a word `w_i` will be `[i - window_size, i + window_size+1]`. |
| `negative_samples` | Float >= 0. 0 for no negative (i.e. random) samples. 1 for same number as positive samples. |
| `shuffle` | Whether to shuffle the word couples before returning them. |
| `categorical` | bool. if False, labels will be integers (eg. `[0, 1, 1 .. ]`), if `True`, labels will be categorical, e.g. `[[1,0],[0,1],[0,1] .. ]`. |
| `sampling_table` | 1D array of size `vocabulary_size` where the entry i encodes the probability to sample a word of rank i. |
| `seed` | Random seed. |

|     |
| --- |
| Returns<br>------- |     |
| couples, labels: where `couples` are int pairs and `labels` are either 0 or 1. |     |

|     |
| --- |
| Note<br>---- |     |
| By convention, index 0 in the vocabulary is a non-word and will be skipped. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.