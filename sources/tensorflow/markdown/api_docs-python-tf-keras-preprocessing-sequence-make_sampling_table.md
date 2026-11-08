[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.sequence.make\_sampling\_table Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/sequence.py#L187-L226)

Generates a word rank-based probabilistic sampling table.

tf.keras.preprocessing.sequence.make_sampling_table(
        size, sampling_factor=1e-05
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [word2vec](https://www.tensorflow.org/text/tutorials/word2vec) |

DEPRECATED.

Used for generating the `sampling_table` argument for `skipgrams`. `sampling_table[i]` is the probability of sampling the word i-th most common word in a dataset (more common words should be sampled less frequently, for balance).

The sampling probabilities are generated according to the sampling distribution used in word2vec:

p(word) = (min(1, sqrt(word_frequency / sampling_factor) /
        (word_frequency / sampling_factor)))

We assume that the word frequencies follow Zipf's law (s=1) to derive a numerical approximation of frequency(rank):

`frequency(rank) ~ 1/(rank * (log(rank) + gamma) + 1/2 - 1/(12*rank))` where `gamma` is the Euler-Mascheroni constant.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `size` | Int, number of possible words to sample. |
| `sampling_factor` | The sampling factor in the word2vec formula. |

|     |
| --- |
| Returns<br>------- |     |
| A 1D Numpy array of length `size` where the ith entry is the probability that a word of rank i should be sampled. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.