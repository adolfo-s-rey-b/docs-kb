[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.FixedLenSequenceFeature Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_config.py#L361-L393)

Configuration for parsing a variable-length input feature into a `Tensor`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.FixedLenSequenceFeature`](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature)
, [`tf.compat.v1.io.FixedLenSequenceFeature`](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature)

tf.io.FixedLenSequenceFeature(
        shape, dtype, allow_missing=False, default_value=None
    )

The resulting `Tensor` of parsing a single `SequenceExample` or `Example` has a static `shape` of `[None] + shape` and the specified `dtype`. The resulting `Tensor` of parsing a `batch_size` many `Example`s has a static `shape` of `[batch_size, None] + shape` and the specified `dtype`. The entries in the `batch` from different `Examples` will be padded with `default_value` to the maximum length present in the `batch`.

To treat a sparse input as dense, provide `allow_missing=True`; otherwise, the parse functions will fail on any examples missing this feature.

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `shape` | Shape of input data for dimension 2 and higher. First dimension is of variable length `None`. |
| `dtype` | Data type of input. |
| `allow_missing` | Whether to allow this feature to be missing from a feature list item. Is available only for parsing `SequenceExample` not for parsing `Examples`. |
| `default_value` | Scalar value to be used to pad multiple `Example`s to their maximum length. Irrelevant for parsing a single `Example` or `SequenceExample`. Defaults to "" for dtype string and 0 otherwise (optional). |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `shape` | A `namedtuple` alias for field number 0 |
| `dtype` | A `namedtuple` alias for field number 1 |
| `allow_missing` | A `namedtuple` alias for field number 2 |
| `default_value` | A `namedtuple` alias for field number 3 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.