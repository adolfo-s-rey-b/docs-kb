[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.parse\_example Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_ops.py#L310-L313)

Parses `Example` protos into a `dict` of tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/parse_example)

tf.compat.v1.parse_example(
        serialized, features, name=None, example_names=None
    )

Parses a number of serialized [`Example`](https://www.tensorflow.org/code/tensorflow/core/example/example.proto)
 protos given in `serialized`. We refer to `serialized` as a batch with `batch_size` many entries of individual `Example` protos.

`example_names` may contain descriptive names for the corresponding serialized protos. These may be useful for debugging purposes, but they have no effect on the output. If not `None`, `example_names` must be the same length as `serialized`.

This op parses serialized examples into a dictionary mapping keys to `Tensor` `SparseTensor`, and `RaggedTensor` objects. `features` is a Mapping from keys to `VarLenFeature`, `SparseFeature`, `RaggedFeature`, and `FixedLenFeature` objects. Each `VarLenFeature` and `SparseFeature` is mapped to a `SparseTensor`; each `FixedLenFeature` is mapped to a `Tensor`; and each `RaggedFeature` is mapped to a `RaggedTensor`.

Each `VarLenFeature` maps to a `SparseTensor` of the specified type representing a ragged matrix. Its indices are `[batch, index]` where `batch` identifies the example in `serialized`, and `index` is the value's index in the list of values associated with that feature and example.

Each `SparseFeature` maps to a `SparseTensor` of the specified type representing a Tensor of `dense_shape` `[batch_size] + SparseFeature.size`. Its `values` come from the feature in the examples with key `value_key`. A `values[i]` comes from a position `k` in the feature of an example at batch entry `batch`. This positional information is recorded in `indices[i]` as `[batch, index_0, index_1, ...]` where `index_j` is the `k-th` value of the feature in the example at with key [`SparseFeature.index_key[j]`](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature#index_key)
. In other words, we split the indices (except the first index indicating the batch entry) of a `SparseTensor` by dimension into different features of the `Example`. Due to its complexity a `VarLenFeature` should be preferred over a `SparseFeature` whenever possible.

Each `FixedLenFeature` `df` maps to a `Tensor` of the specified type (or [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)
 if not specified) and shape `(serialized.size(),) + df.shape`.

`FixedLenFeature` entries with a `default_value` are optional. With no default value, we will fail if that `Feature` is missing from any example in `serialized`.

Each `FixedLenSequenceFeature` `df` maps to a `Tensor` of the specified type (or [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)
 if not specified) and shape `(serialized.size(), None) + df.shape`. All examples in `serialized` will be padded with `default_value` along the second dimension.

Each `RaggedFeature` maps to a `RaggedTensor` of the specified type. It is formed by stacking the `RaggedTensor` for each example, where the `RaggedTensor` for each individual example is constructed using the tensors specified by `RaggedTensor.values_key` and [`RaggedTensor.partition`](https://www.tensorflow.org/tfx/tf_metadata/api_docs/python/tfmd/proto/schema_pb2/TensorRepresentation/RaggedTensor#partition)
. See the [`tf.io.RaggedFeature`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature)
 documentation for details and examples.

#### Examples:

For example, if one expects a [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)
 `VarLenFeature` `ft` and three serialized `Example`s are provided:

serialized = [\
      features\
        { feature { key: "ft" value { float_list { value: [1.0, 2.0] } } } },\
      features\
        { feature []},\
      features\
        { feature { key: "ft" value { float_list { value: [3.0] } } }\
    ]

then the output will look like:

{"ft": SparseTensor(indices=[[0, 0], [0, 1], [2, 0]],
                        values=[1.0, 2.0, 3.0],
                        dense_shape=(3, 2)) }

If instead a `FixedLenSequenceFeature` with `default_value = -1.0` and `shape=[]` is used then the output will look like:

{"ft": [[1.0, 2.0], [3.0, -1.0]]}

Given two `Example` input protos in `serialized`:

[\
      features {\
        feature { key: "kw" value { bytes_list { value: [ "knit", "big" ] } } }\
        feature { key: "gps" value { float_list { value: [] } } }\
      },\
      features {\
        feature { key: "kw" value { bytes_list { value: [ "emmy" ] } } }\
        feature { key: "dank" value { int64_list { value: [ 42 ] } } }\
        feature { key: "gps" value { } }\
      }\
    ]

And arguments

example_names: ["input0", "input1"],
    features: {
        "kw": VarLenFeature(tf.string),
        "dank": VarLenFeature(tf.int64),
        "gps": VarLenFeature(tf.float32),
    }

Then the output is a dictionary:

{
      "kw": SparseTensor(
          indices=[[0, 0], [0, 1], [1, 0]],
          values=["knit", "big", "emmy"]
          dense_shape=[2, 2]),
      "dank": SparseTensor(
          indices=[[1, 0]],
          values=[42],
          dense_shape=[2, 1]),
      "gps": SparseTensor(
          indices=[],
          values=[],
          dense_shape=[2, 0]),
    }

For dense results in two serialized `Example`s:

[\
      features {\
        feature { key: "age" value { int64_list { value: [ 0 ] } } }\
        feature { key: "gender" value { bytes_list { value: [ "f" ] } } }\
       },\
       features {\
        feature { key: "age" value { int64_list { value: [] } } }\
        feature { key: "gender" value { bytes_list { value: [ "f" ] } } }\
      }\
    ]

#### We can use arguments:

example_names: ["input0", "input1"],
    features: {
        "age": FixedLenFeature([], dtype=tf.int64, default_value=-1),
        "gender": FixedLenFeature([], dtype=tf.string),
    }

And the expected output is:

{
      "age": [[0], [-1]],
      "gender": [["f"], ["f"]],
    }

An alternative to `VarLenFeature` to obtain a `SparseTensor` is `SparseFeature`. For example, given two `Example` input protos in `serialized`:

[\
      features {\
        feature { key: "val" value { float_list { value: [ 0.5, -1.0 ] } } }\
        feature { key: "ix" value { int64_list { value: [ 3, 20 ] } } }\
      },\
      features {\
        feature { key: "val" value { float_list { value: [ 0.0 ] } } }\
        feature { key: "ix" value { int64_list { value: [ 42 ] } } }\
      }\
    ]

And arguments

example_names: ["input0", "input1"],
    features: {
        "sparse": SparseFeature(
            index_key="ix", value_key="val", dtype=tf.float32, size=100),
    }

Then the output is a dictionary:

{
      "sparse": SparseTensor(
          indices=[[0, 3], [0, 20], [1, 42]],
          values=[0.5, -1.0, 0.0]
          dense_shape=[2, 100]),
    }

See the [`tf.io.RaggedFeature`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature)
 documentation for examples showing how `RaggedFeature` can be used to obtain `RaggedTensor`s.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `serialized` | A vector (1-D Tensor) of strings, a batch of binary serialized `Example` protos. |
| `features` | A mapping of feature keys to `FixedLenFeature`, `VarLenFeature`, `SparseFeature`, and `RaggedFeature` values. |
| `example_names` | A vector (1-D Tensor) of strings (optional), the names of the serialized protos in the batch. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `dict` mapping feature keys to `Tensor`, `SparseTensor`, and `RaggedTensor` values. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if any feature is invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.