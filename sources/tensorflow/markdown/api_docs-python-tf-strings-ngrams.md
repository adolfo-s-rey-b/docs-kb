[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.ngrams Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L673-L826)

Create a tensor of n-grams based on `data`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.ngrams`](https://www.tensorflow.org/api_docs/python/tf/strings/ngrams)

tf.strings.ngrams(
        data,
        ngram_width,
        separator=' ',
        pad_values=None,
        padding_width=None,
        preserve_short_sequences=False,
        name=None
    )

Creates a tensor of n-grams based on `data`. The n-grams are created by joining windows of `width` adjacent strings from the inner axis of `data` using `separator`.

The input data can be padded on both the start and end of the sequence, if desired, using the `pad_values` argument. If set, `pad_values` should contain either a tuple of strings or a single string; the 0th element of the tuple will be used to pad the left side of the sequence and the 1st element of the tuple will be used to pad the right side of the sequence. The `padding_width` arg controls how many padding values are added to each side; it defaults to `ngram_width-1`.

If this op is configured to not have padding, or if it is configured to add padding with `padding_width` set to less than ngram\_width-1, it is possible that a sequence, or a sequence plus padding, is smaller than the ngram width. In that case, no ngrams will be generated for that sequence. This can be prevented by setting `preserve_short_sequences`, which will cause the op to always generate at least one ngram per non-empty sequence.

#### Examples:

    tf.strings.ngrams(["A", "B", "C", "D"], 2).numpy()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A Tensor or RaggedTensor containing the source data for the ngrams. |
| `ngram_width` | The width(s) of the ngrams to create. If this is a list or tuple, the op will return ngrams of all specified arities in list order. Values must be non-Tensor integers greater than 0. |
| `separator` | The separator string used between ngram elements. Must be a string constant, not a Tensor. |
| `pad_values` | A tuple of (left\_pad\_value, right\_pad\_value), a single string, or None. If None, no padding will be added; if a single string, then that string will be used for both left and right padding. Values must be Python strings. Should be set when `padding_width` is not None. |
| `padding_width` | If set, `padding_width` pad values will be added to both sides of each sequence. Defaults to `ngram_width`\-1. Must be greater than<br><br>1.  (Note that 1-grams are never padded, regardless of this value.) |
| `preserve_short_sequences` | If true, then ensure that at least one ngram is generated for each input sequence. In particular, if an input sequence is shorter than `min(ngram_width) + 2*pad_width`, then generate a single ngram containing the entire sequence. If false, then no ngrams are generated for these short input sequences. |
| `name` | The op name. |

|     |
| --- |
| Returns<br>------- |     |
| A RaggedTensor of ngrams. If `data.shape=[D1...DN, S]`, then `output.shape=[D1...DN, NUM_NGRAMS]`, where `NUM_NGRAMS=S-ngram_width+1+2*padding_width`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `pad_values` is set to an invalid type. |
| `ValueError` | if `pad_values`, `padding_width`, or `ngram_width` is set to an invalid value. |
| `ValueError` | if `padding_width` is not None and `pad_values` is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.