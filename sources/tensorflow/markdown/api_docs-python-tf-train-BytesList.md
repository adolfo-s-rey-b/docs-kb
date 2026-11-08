[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/BytesList#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/BytesList)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/BytesList?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/BytesList#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/BytesList#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.BytesList Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/BytesList#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/BytesList#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/example/feature.proto)

Used in [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 protos. Holds a list of byte-strings.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.BytesList`](https://www.tensorflow.org/api_docs/python/tf/train/BytesList)

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFRecord and tf.train.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning)<br>    <br>*   [Preprocessing data with TensorFlow Transform](https://www.tensorflow.org/tfx/tutorials/transform/census)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb) |

An `Example` proto is a representation of the following python type:

Dict[str,\
         Union[List[bytes],\
               List[int64],\
               List[float]]]

This proto implements the `List[bytes]` portion.

    from google.protobuf import text_format

Use [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)
 to extract tensors from a serialized `Example` proto:

    tf.io.parse_example(

See the [`tf.train.Example`](https://www.tensorflow.org/tutorials/load_data/tfrecord#tftrainexample)
 guide for usage details.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `value` | `repeated bytes value` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.