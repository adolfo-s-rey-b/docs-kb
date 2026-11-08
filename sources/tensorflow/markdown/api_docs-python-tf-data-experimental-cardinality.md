[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdata%2Fexperimental%2Fcardinality&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.cardinality Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/cardinality.py#L33-L64)

Returns the cardinality of `dataset`, if known.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.cardinality`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/cardinality)

tf.data.experimental.cardinality(
        dataset
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Transfer learning and fine-tuning](https://www.tensorflow.org/tutorials/images/transfer_learning)<br>    <br>*   [Load and preprocess images](https://www.tensorflow.org/tutorials/load_data/images)<br>    <br>*   [Classify text with BERT](https://www.tensorflow.org/text/tutorials/classify_text_with_bert) |

The operation returns the cardinality of `dataset`. The operation may return [`tf.data.experimental.INFINITE_CARDINALITY`](https://www.tensorflow.org/api_docs/python/tf/data/experimental#INFINITE_CARDINALITY)
 if `dataset` contains an infinite number of elements or [`tf.data.experimental.UNKNOWN_CARDINALITY`](https://www.tensorflow.org/api_docs/python/tf/data/experimental#UNKNOWN_CARDINALITY)
 if the analysis fails to determine the number of elements in `dataset` (e.g. when the dataset source is a file).

    dataset = tf.data.Dataset.range(42)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> for which to determine cardinality. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> `Tensor` representing the cardinality of `dataset`. If the cardinality is infinite or unknown, the operation returns the named constant `INFINITE_CARDINALITY` and `UNKNOWN_CARDINALITY` respectively. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.