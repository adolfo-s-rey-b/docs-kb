[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.parse\_single\_sequence\_example Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_ops.py#L693-L804)

Parses a single `SequenceExample` proto.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.parse_single_sequence_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example)
, [`tf.compat.v1.parse_single_sequence_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_single_sequence_example)

tf.io.parse_single_sequence_example(
        serialized,
        context_features=None,
        sequence_features=None,
        example_name=None,
        name=None
    )

Parses a single serialized [`SequenceExample`](https://www.tensorflow.org/code/tensorflow/core/example/example.proto)
 proto given in `serialized`.

This op parses a serialized sequence example into a tuple of dictionaries, each mapping keys to `Tensor` and `SparseTensor` objects. The first dictionary contains mappings for keys appearing in `context_features`, and the second dictionary contains mappings for keys appearing in `sequence_features`.

At least one of `context_features` and `sequence_features` must be provided and non-empty.

The `context_features` keys are associated with a `SequenceExample` as a whole, independent of time / frame. In contrast, the `sequence_features` keys provide a way to access variable-length data within the `FeatureList` section of the `SequenceExample` proto. While the shapes of `context_features` values are fixed with respect to frame, the frame dimension (the first dimension) of `sequence_features` values may vary between `SequenceExample` protos, and even between `feature_list` keys within the same `SequenceExample`.

`context_features` contains `VarLenFeature`, `RaggedFeature`, and `FixedLenFeature` objects. Each `VarLenFeature` is mapped to a `SparseTensor`; each `RaggedFeature` is mapped to a `RaggedTensor`; and each `FixedLenFeature` is mapped to a `Tensor`, of the specified type, shape, and default value.

`sequence_features` contains `VarLenFeature`, `RaggedFeature`, and `FixedLenSequenceFeature` objects. Each `VarLenFeature` is mapped to a `SparseTensor`; each `RaggedFeature` is mapped to a `RaggedTensor`; and each `FixedLenSequenceFeature` is mapped to a `Tensor`, each of the specified type. The shape will be `(T,) + df.dense_shape` for `FixedLenSequenceFeature` `df`, where `T` is the length of the associated `FeatureList` in the `SequenceExample`. For instance, `FixedLenSequenceFeature([])` yields a scalar 1-D `Tensor` of static shape `[None]` and dynamic shape `[T]`, while `FixedLenSequenceFeature([k])` (for `int k >= 1`) yields a 2-D matrix `Tensor` of static shape `[None, k]` and dynamic shape `[T, k]`.

Each `SparseTensor` corresponding to `sequence_features` represents a ragged vector. Its indices are `[time, index]`, where `time` is the `FeatureList` entry and `index` is the value's index in the list of values associated with that time.

`FixedLenFeature` entries with a `default_value` and `FixedLenSequenceFeature` entries with `allow_missing=True` are optional; otherwise, we will fail if that `Feature` or `FeatureList` is missing from any example in `serialized`.

`example_name` may contain a descriptive name for the corresponding serialized proto. This may be useful for debugging purposes, but it has no effect on the output. If not `None`, `example_name` must be a scalar.

Note that the batch version of this function, `tf.parse_sequence_example`, is written for better memory efficiency and will be faster on large `SequenceExample`s.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `serialized` | A scalar (0-D Tensor) of type string, a single binary serialized `SequenceExample` proto. |
| `context_features` | A mapping of feature keys to `FixedLenFeature` or `VarLenFeature` or `RaggedFeature` values. These features are associated with a `SequenceExample` as a whole. |
| `sequence_features` | A mapping of feature keys to `FixedLenSequenceFeature` or `VarLenFeature` or `RaggedFeature` values. These features are associated with data within the `FeatureList` section of the `SequenceExample` proto. |
| `example_name` | A scalar (0-D Tensor) of strings (optional), the name of the serialized proto. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A tuple of two `dict`s, each mapping keys to `Tensor`s and `SparseTensor`s and `RaggedTensor`s.<br><br>*   The first dict contains the context key/values.<br>*   The second dict contains the feature\_list key/values. |     |

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