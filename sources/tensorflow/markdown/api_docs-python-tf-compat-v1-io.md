[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io?version=stable#modules_2)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io?version=stable#functions_2)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.io Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io?version=stable#modules_2)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io?version=stable#functions_2)
    

See Stable See Nightly

Public API for tf.\_api.v2.io namespace

Modules
-------

[`gfile`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/gfile)
 module: Public API for tf.\_api.v2.io.gfile namespace

Classes
-------

[`class FixedLenFeature`](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenFeature)
: Configuration for parsing a fixed-length input feature.

[`class FixedLenSequenceFeature`](https://www.tensorflow.org/api_docs/python/tf/io/FixedLenSequenceFeature)
: Configuration for parsing a variable-length input feature into a `Tensor`.

[`class PaddingFIFOQueue`](https://www.tensorflow.org/api_docs/python/tf/queue/PaddingFIFOQueue)
: A FIFOQueue that supports batching variable-sized tensors by padding.

[`class PriorityQueue`](https://www.tensorflow.org/api_docs/python/tf/queue/PriorityQueue)
: A queue implementation that dequeues elements in prioritized order.

[`class QueueBase`](https://www.tensorflow.org/api_docs/python/tf/queue/QueueBase)
: Base class for queue implementations.

[`class RaggedFeature`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature)
: Configuration for passing a RaggedTensor input feature.

[`class RandomShuffleQueue`](https://www.tensorflow.org/api_docs/python/tf/queue/RandomShuffleQueue)
: A queue implementation that dequeues elements in a random order.

[`class SparseFeature`](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature)
: Configuration for parsing a sparse input feature from an `Example`.

[`class TFRecordCompressionType`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/TFRecordCompressionType)
: The type of compression for the record.

[`class TFRecordOptions`](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordOptions)
: Options used for manipulating TFRecord files.

[`class TFRecordWriter`](https://www.tensorflow.org/api_docs/python/tf/io/TFRecordWriter)
: A class to write records to a TFRecords file.

[`class VarLenFeature`](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature)
: Configuration for parsing a variable-length input feature.

Functions
---------

[`decode_and_crop_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_and_crop_jpeg)
: Decode and Crop a JPEG-encoded image to a uint8 tensor.

[`decode_base64(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_base64)
: Decode web-safe base64-encoded strings.

[`decode_bmp(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_bmp)
: Decode the first frame of a BMP-encoded image to a uint8 tensor.

[`decode_compressed(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_compressed)
: Decompress strings.

[`decode_csv(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_csv)
: Convert CSV records to tensors. Each column maps to one tensor.

[`decode_gif(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_gif)
: Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

[`decode_image(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
: Function for `decode_bmp`, `decode_gif`, `decode_jpeg`, and `decode_png`.

[`decode_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg)
: Decode a JPEG-encoded image to a uint8 tensor.

[`decode_json_example(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_json_example)
: Convert JSON-encoded Example records to binary protocol buffer strings.

[`decode_jxl(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_jxl)
: Decode a JPEG XL encoded image to a uint8 tensor.

[`decode_png(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_png)
: Decode a PNG-encoded image to a uint8 or uint16 tensor.

[`decode_proto(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_proto)
: The op extracts fields from a serialized protocol buffers message into tensors.

[`decode_raw(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/decode_raw)
: Convert raw byte strings into tensors. (deprecated arguments)

[`decode_webp(...)`](https://www.tensorflow.org/api_docs/python/tf/io/decode_webp)
: Decode a WebP-encoded image to a uint8 tensor.

[`deserialize_many_sparse(...)`](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse)
: Deserialize and concatenate `SparseTensors` from a serialized minibatch.

[`encode_base64(...)`](https://www.tensorflow.org/api_docs/python/tf/io/encode_base64)
: Encode strings into web-safe base64 format.

[`encode_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/io/encode_jpeg)
: JPEG-encode an image.

[`encode_png(...)`](https://www.tensorflow.org/api_docs/python/tf/io/encode_png)
: PNG-encode an image.

[`encode_proto(...)`](https://www.tensorflow.org/api_docs/python/tf/io/encode_proto)
: The op serializes protobuf messages provided in the input tensors.

[`extract_jpeg_shape(...)`](https://www.tensorflow.org/api_docs/python/tf/io/extract_jpeg_shape)
: Extract the shape information of a JPEG-encoded image.

[`is_jpeg(...)`](https://www.tensorflow.org/api_docs/python/tf/io/is_jpeg)
: Convenience function to check if the 'contents' encodes a JPEG image.

[`match_filenames_once(...)`](https://www.tensorflow.org/api_docs/python/tf/io/match_filenames_once)
: Save the list of files matching pattern, so it is only computed once.

[`matching_files(...)`](https://www.tensorflow.org/api_docs/python/tf/io/matching_files)
: Returns the set of files matching one or more glob patterns.

[`parse_example(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example)
: Parses `Example` protos into a `dict` of tensors.

[`parse_sequence_example(...)`](https://www.tensorflow.org/api_docs/python/tf/io/parse_sequence_example)
: Parses a batch of `SequenceExample` protos.

[`parse_single_example(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_single_example)
: Parses a single `Example` proto.

[`parse_single_sequence_example(...)`](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example)
: Parses a single `SequenceExample` proto.

[`parse_tensor(...)`](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor)
: Transforms a serialized tensorflow.TensorProto proto into a Tensor.

[`read_file(...)`](https://www.tensorflow.org/api_docs/python/tf/io/read_file)
: Reads the contents of file.

[`serialize_many_sparse(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_many_sparse)
: Serialize `N`\-minibatch `SparseTensor` into an `[N, 3]` `Tensor`.

[`serialize_sparse(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/serialize_sparse)
: Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

[`serialize_tensor(...)`](https://www.tensorflow.org/api_docs/python/tf/io/serialize_tensor)
: Transforms a Tensor into a serialized TensorProto proto.

[`tf_record_iterator(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/tf_record_iterator)
: An iterator that read the records from a TFRecords file. (deprecated)

[`write_file(...)`](https://www.tensorflow.org/api_docs/python/tf/io/write_file)
: Writes `contents` to the file at input `filename`.

[`write_graph(...)`](https://www.tensorflow.org/api_docs/python/tf/io/write_graph)
: Writes a graph proto to a file.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.