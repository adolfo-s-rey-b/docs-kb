[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.pad\_sequences Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/sequence_utils.py#L6-L139)

Pads sequences to the same length.

#### View aliases

**Main aliases**

[`tf.keras.preprocessing.sequence.pad_sequences`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences)

tf.keras.utils.pad_sequences(
        sequences,
        maxlen=None,
        dtype='int32',
        padding='pre',
        truncating='pre',
        value=0.0
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding) | *   [Wiki Talk Comments Toxicity Prediction](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_Wiki_Case_Study) |

This function transforms a list (of length `num_samples`) of sequences (lists of integers) into a 2D NumPy array of shape `(num_samples, num_timesteps)`. `num_timesteps` is either the `maxlen` argument if provided, or the length of the longest sequence in the list.

Sequences that are shorter than `num_timesteps` are padded with `value` until they are `num_timesteps` long.

Sequences longer than `num_timesteps` are truncated so that they fit the desired length.

The position where padding or truncation happens is determined by the arguments `padding` and `truncating`, respectively. Pre-padding or removing values from the beginning of the sequence is the default.

    sequence = [[1], [2, 3], [4, 5, 6]]

    keras.utils.pad_sequences(sequence, value=-1)

    keras.utils.pad_sequences(sequence, padding='post')

    keras.utils.pad_sequences(sequence, maxlen=2)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sequences` | List of sequences (each sequence is a list of integers). |
| `maxlen` | Optional Int, maximum length of all sequences. If not provided, sequences will be padded to the length of the longest individual sequence. |
| `dtype` | (Optional, defaults to `"int32"`). Type of the output sequences. To pad sequences with variable length strings, you can use `object`. |
| `padding` | String, "pre" or "post" (optional, defaults to `"pre"`): pad either before or after each sequence. |
| `truncating` | String, "pre" or "post" (optional, defaults to `"pre"`): remove values from sequences larger than `maxlen`, either at the beginning or at the end of the sequences. |
| `value` | Float or String, padding value. (Optional, defaults to `0.`) |

|     |
| --- |
| Returns<br>------- |     |
| NumPy array with shape `(len(sequences), maxlen)` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.