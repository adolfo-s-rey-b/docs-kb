[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_compressed#main-content)

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
    

tf.io.decode\_compressed Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

Decompress strings.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.decode_compressed`](https://www.tensorflow.org/api_docs/python/tf/io/decode_compressed)
, [`tf.compat.v1.io.decode_compressed`](https://www.tensorflow.org/api_docs/python/tf/io/decode_compressed)

tf.io.decode_compressed(
        bytes: Annotated[Any, _atypes.String],
        compression_type: str = '',
        name=None
    ) -> Annotated[Any, _atypes.String]

This op decompresses each element of the `bytes` input `Tensor`, which is assumed to be compressed using the given `compression_type`.

The `output` is a string `Tensor` of the same shape as `bytes`, each element containing the decompressed data from the corresponding element in `bytes`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bytes` | A `Tensor` of type `string`. A Tensor of string which is compressed. |
| `compression_type` | An optional `string`. Defaults to `""`. A scalar containing either (i) the empty string (no compression), (ii) "ZLIB", or (iii) "GZIP". |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `string`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.