[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature#used-in-the-notebooks)
    
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.FixedLenFeature Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature#used-in-the-notebooks)
    
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_config.py#L341-L358)

Configuration for parsing a fixed-length input feature.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.FixedLenFeature`](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature)
, [`tf.compat.v1.io.FixedLenFeature`](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature)

tf.io.FixedLenFeature(
        shape, dtype, default_value=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data) | *   [TFRecord and tf.train.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)<br>    <br>*   [](https://www.tensorflow.org/tfx/transform/get_started)<br>    <br>*   [Recommending movies: retrieval using a sequential model](https://www.tensorflow.org/recommenders/examples/sequential_retrieval)<br>    <br>*   [Graph regularization for document classification using natural graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_mlp_cora)<br>    <br>*   [Passage Ranking using TFR-BERT](https://www.tensorflow.org/ranking/tutorials/tfr_bert) |

To treat sparse input as dense, provide a `default_value`; otherwise, the parse functions will fail on any examples missing this feature.

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `shape` | Shape of input data. |
| `dtype` | Data type of input. |
| `default_value` | Value to be used if an example is missing this feature. It must be compatible with `dtype` and of the specified `shape`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `shape` | A `namedtuple` alias for field number 0 |
| `dtype` | A `namedtuple` alias for field number 1 |
| `default_value` | A `namedtuple` alias for field number 2 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.