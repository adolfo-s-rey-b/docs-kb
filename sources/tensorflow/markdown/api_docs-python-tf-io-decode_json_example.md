[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_json\_example Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_ops.py#L1138-L1220)

Convert JSON-encoded Example records to binary protocol buffer strings.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.decode_json_example`](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example)
, [`tf.compat.v1.io.decode_json_example`](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example)

tf.io.decode_json_example(
        json_examples, name=None
    )

This op converts JSON-serialized [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 (maybe created with `json_format.MessageToJson`, following the [standard JSON mapping](https://developers.google.com/protocol-buffers/docs/proto3#json)
) to a binary-serialized [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 (equivalent to [`Example.SerializeToString()`](https://www.tensorflow.org/api_docs/python/tf/train/BytesList#SerializeToString)
) suitable for conversion to tensors with [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)
.

Here is a [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 proto:

    example = tf.train.Example(

Here it is converted to JSON:

    from google.protobuf import json_format

This op converts the above json string to a binary proto:

    example_binary = tf.io.decode_json_example(example_json)

The OP works on string tensors of andy shape:

    tf.io.decode_json_example([\
\
This resulting binary-string is equivalent to [`Example.SerializeToString()`](https://www.tensorflow.org/api_docs/python/tf/train/BytesList#SerializeToString)\
, and can be converted to Tensors using [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)\
 and related functions:\
\
    tf.io.parse_example(\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `json_examples` | A string tensor containing json-serialized `tf.Example` protos. |\
| `name` | A name for the op. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A string Tensor containing the binary-serialized `tf.Example` protos. |     |\
\
|     |\
| --- |\
| Raises<br>------ |     |\
| [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)<br>: If the JSON could not be converted to a `tf.Example` |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.