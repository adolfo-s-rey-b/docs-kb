[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_proto Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto#returns)
    

The op extracts fields from a serialized protocol buffers message into tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.decode_proto`](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto)

tf.io.decode_proto(
        bytes: Annotated[Any, _atypes.String],
        message_type: str,
        field_names,
        output_types,
        descriptor_source: str = 'local://',
        message_format: str = 'binary',
        sanitize: bool = False,
        name=None
    )

The `decode_proto` op extracts fields from a serialized protocol buffers message into tensors. The fields in `field_names` are decoded and converted to the corresponding `output_types` if possible.

A `message_type` name must be provided to give context for the field names. The actual message descriptor can be looked up either in the linked-in descriptor pool or a filename provided by the caller using the `descriptor_source` attribute.

Each output tensor is a dense tensor. This means that it is padded to hold the largest number of repeated elements seen in the input minibatch. (The shape is also padded by one to prevent zero-sized dimensions). The actual repeat counts for each example in the minibatch can be found in the `sizes` output. In many cases the output of `decode_proto` is fed immediately into tf.squeeze if missing values are not a concern. When using tf.squeeze, always pass the squeeze dimension explicitly to avoid surprises.

For the most part, the mapping between Proto field types and TensorFlow dtypes is straightforward. However, there are a few special cases:

*   A proto field that contains a submessage or group can only be converted to `DT_STRING` (the serialized submessage). This is to reduce the complexity of the API. The resulting string can be used as input to another instance of the decode\_proto op.
    
*   TensorFlow lacks support for unsigned integers. The ops represent uint64 types as a `DT_INT64` with the same twos-complement bit pattern (the obvious way). Unsigned int32 values can be represented exactly by specifying type `DT_INT64`, or using twos-complement if the caller specifies `DT_INT32` in the `output_types` attribute.
    
*   `map` fields are not directly decoded. They are treated as `repeated` fields, of the appropriate entry type. The proto-compiler defines entry types for each map field. The type-name is the field name, converted to "CamelCase" with "Entry" appended. The [`tf.train.Features.FeatureEntry`](https://www.tensorflow.org/api_docs/python/tf/train/Features/FeatureEntry)
     message is an example of one of these implicit `Entry` types.
    
*   `enum` fields should be read as int32.
    

Both binary and text proto serializations are supported, and can be chosen using the `format` attribute.

The `descriptor_source` attribute selects the source of protocol descriptors to consult when looking up `message_type`. This may be:

*   An empty string or "local://", in which case protocol descriptors are created for C++ (not Python) proto definitions linked to the binary.
    
*   A file, in which case protocol descriptors are created from the file, which is expected to contain a `FileDescriptorSet` serialized as a string. NOTE: You can build a `descriptor_source` file using the `--descriptor_set_out` and `--include_imports` options to the protocol compiler `protoc`.
    
*   A "bytes://", in which protocol descriptors are created from `<bytes>`, which is expected to be a `FileDescriptorSet` serialized as a string.
    

#### Here is an example:

The, internal, `Summary.Value` proto contains a `oneof {float simple_value; Image image; ...}`

    from google.protobuf import text_format

The following can decode both fields from the serialized strings:

    sizes, [simple_value, image]  = tf.io.decode_proto(

The `sizes` has the same shape as the input, with an additional axis across the fields that were decoded. Here the first column of `sizes` is the size of the decoded `simple_value` field:

    print(sizes)

The result tensors each have one more index than the input byte-strings. The valid elements of each result tensor are indicated by the appropriate column of `sizes`. The invalid elements are padded with a default value:

    print(simple_value)

Nested protos are extracted as string tensors:

    print(image.dtype)

To convert to a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 representation use:

    tf.RaggedTensor.from_tensor(simple_value, lengths=sizes[:, 0]).to_list()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `bytes` | A `Tensor` of type `string`. Tensor of serialized protos with shape `batch_shape`. |
| `message_type` | A `string`. Name of the proto message type to decode. |
| `field_names` | A list of `strings`. List of strings containing proto field names. An extension field can be decoded by using its full name, e.g. EXT\_PACKAGE.EXT\_FIELD\_NAME. |
| `output_types` | A list of `tf.DTypes`. List of TF types to use for the respective field in field\_names. |
| `descriptor_source` | An optional `string`. Defaults to `"local://"`. Either the special value `local://` or a path to a file containing a serialized `FileDescriptorSet`. |
| `message_format` | An optional `string`. Defaults to `"binary"`. Either `binary` or [`text`](https://www.tensorflow.org/text/api_docs/python/text)<br>. |
| `sanitize` | An optional `bool`. Defaults to `False`. Whether to sanitize the result or not. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (sizes, values). |     |
| `sizes` | A `Tensor` of type `int32`. |
| `values` | A list of `Tensor` objects of type `output_types`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.