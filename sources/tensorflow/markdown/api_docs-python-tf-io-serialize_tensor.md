[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/serialize_tensor#main-content)

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
    

tf.io.serialize\_tensor Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/io_ops.py#L137-L214)

Transforms a Tensor into a serialized TensorProto proto.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.serialize_tensor`](https://www.tensorflow.org/api_docs/python/tf/io/serialize_tensor)
, [`tf.compat.v1.serialize_tensor`](https://www.tensorflow.org/api_docs/python/tf/io/serialize_tensor)

tf.io.serialize_tensor(
        tensor, name=None
    )

This operation transforms data in a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 into a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 of type [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)
 containing the data in a binary string in little-endian format. This operation can transform scalar data and linear arrays, but it is most useful in converting multidimensional arrays into a format accepted by binary storage formats such as a `TFRecord` or [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
.

#### See also:

*   [`tf.io.parse_tensor`](https://www.tensorflow.org/api_docs/python/tf/io/parse_tensor)
    : inverse operation of [`tf.io.serialize_tensor`](https://www.tensorflow.org/api_docs/python/tf/io/serialize_tensor)
     that transforms a scalar string containing a serialized Tensor in little-endian format into a Tensor of a specified type.
*   [`tf.ensure_shape`](https://www.tensorflow.org/api_docs/python/tf/ensure_shape)
    : `parse_tensor` cannot statically determine the shape of the parsed tensor. Use [`tf.ensure_shape`](https://www.tensorflow.org/api_docs/python/tf/ensure_shape)
     to set the static shape when running under a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    
*   `.SerializeToString`, serializes a proto to a binary-string

Example of serializing scalar data:

    t = tf.constant(1)

Example of storing non-scalar data into a [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
:

    t1 = [[1, 2]]

Serialize the data using [`tf.io.serialize_tensor`](https://www.tensorflow.org/api_docs/python/tf/io/serialize_tensor)
.

    serialized_nonscalar = tf.io.serialize_tensor(nonscalar)

Store the data in a [`tf.train.Feature`](https://www.tensorflow.org/api_docs/python/tf/train/Feature)
.

    feature_of_bytes = tf.train.Feature(

Put the [`tf.train.Feature`](https://www.tensorflow.org/api_docs/python/tf/train/Feature)
 message into a [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
.

    features_for_example = {

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |
| `name` | string. Optional name for the op. |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor of dtype string. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.