[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/Features#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.Features Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/example/feature.proto)

Used in [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 protos. Contains the mapping from keys to `Feature`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.Features`](https://www.tensorflow.org/api_docs/python/tf/train/Features)

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFRecord and tf.train.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning)<br>    <br>*   [Instance Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)<br>    <br>*   [Semantic Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation) |

An `Example` proto is a representation of the following python type:

Dict[str,\
         Union[List[bytes],\
               List[int64],\
               List[float]]]

This proto implements the `Dict`.

    int_feature = tf.train.Feature(

Use [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)
 to extract tensors from a serialized `Example` proto:

    tf.io.parse_example(

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `feature` | `repeated FeatureEntry feature` |

Child Classes
-------------

[`class FeatureEntry`](https://www.tensorflow.org/api_docs/python/tf/train/Features/FeatureEntry)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.