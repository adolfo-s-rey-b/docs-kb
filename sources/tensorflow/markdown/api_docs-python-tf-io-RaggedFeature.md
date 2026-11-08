[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#used-in-the-notebooks)
    
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#child_classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.RaggedFeature Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#used-in-the-notebooks)
    
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature#child_classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_config.py#L54-L263)

Configuration for passing a RaggedTensor input feature.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.RaggedFeature`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature)

tf.io.RaggedFeature(
        dtype,
        value_key=None,
        partitions=(),
        row_splits_dtype=tf.dtypes.int32,
        validate=False
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) | *   [TensorFlow Ranking Keras pipeline for distributed training](https://www.tensorflow.org/ranking/tutorials/ranking_dnn_distributed) |

`value_key` specifies the feature key for a variable-length list of values; and `partitions` specifies zero or more feature keys for partitioning those values into higher dimensions. Each element of `partitions` must be one of the following:

*   `tf.io.RaggedFeature.RowSplits(key: string)`
*   `tf.io.RaggedFeature.RowLengths(key: string)`
*   `tf.io.RaggedFeature.RowStarts(key: string)`
*   `tf.io.RaggedFeature.RowLimits(key: string)`
*   `tf.io.RaggedFeature.ValueRowIds(key: string)`
*   `tf.io.RaggedFeature.UniformRowLength(length: int)`.

Where `key` is a feature key whose values are used to partition the values. Partitions are listed from outermost to innermost.

*   If `len(partitions) == 0` (the default), then:
    
    *   A feature from a single `tf.Example` is parsed into a 1D [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
        .
    *   A feature from a batch of `tf.Example`s is parsed into a 2D [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
        , where the outer dimension is the batch dimension, and the inner (ragged) dimension is the feature length in each example.
*   If `len(partitions) == 1`, then:
    
    *   A feature from a single `tf.Example` is parsed into a 2D [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
        , where the values taken from the `value_key` are separated into rows using the partition key.
    *   A feature from a batch of `tf.Example`s is parsed into a 3D [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
        , where the outer dimension is the batch dimension, the two inner dimensions are formed by separating the `value_key` values from each example into rows using that example's partition key.
*   If `len(partitions) > 1`, then:
    
    *   A feature from a single `tf.Example` is parsed into a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
         whose rank is `len(partitions)+1`, and whose ragged\_rank is `len(partitions)`.
        
    *   A feature from a batch of `tf.Example`s is parsed into a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
         whose rank is `len(partitions)+2` and whose ragged\_rank is `len(partitions)+1`, where the outer dimension is the batch dimension.
        

There is one exception: if the final (i.e., innermost) element(s) of `partitions` are `UniformRowLength`s, then the values are simply reshaped (as a higher-dimensional [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
), rather than being wrapped in a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
.

#### Examples

    import google.protobuf.text_format as pbtext

    features = {

    feature_dict = tf.io.parse_single_example(example_batch[0], features)

    feature_dict = tf.io.parse_example(example_batch, features)

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `dtype` | Data type of the `RaggedTensor`. Must be one of: [`tf.dtypes.int64`](https://www.tensorflow.org/api_docs/python/tf/dtypes#int64)<br>, [`tf.dtypes.float32`](https://www.tensorflow.org/api_docs/python/tf/dtypes#float32)<br>, [`tf.dtypes.string`](https://www.tensorflow.org/api_docs/python/tf/dtypes#string)<br>. |
| `value_key` | (Optional.) Key for a `Feature` in the input `Example`, whose parsed `Tensor` will be the resulting [`RaggedTensor.flat_values`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#flat_values)<br>. If not specified, then it defaults to the key for this `RaggedFeature`. |
| `partitions` | (Optional.) A list of objects specifying the row-partitioning tensors (from outermost to innermost). Each entry in this list must be one of:<br><br>*   `tf.io.RaggedFeature.RowSplits(key: string)`<br>*   `tf.io.RaggedFeature.RowLengths(key: string)`<br>*   `tf.io.RaggedFeature.RowStarts(key: string)`<br>*   `tf.io.RaggedFeature.RowLimits(key: string)`<br>*   `tf.io.RaggedFeature.ValueRowIds(key: string)`<br>*   `tf.io.RaggedFeature.UniformRowLength(length: int)`. Where `key` is a key for a `Feature` in the input `Example`, whose parsed `Tensor` will be the resulting row-partitioning tensor. |
| `row_splits_dtype` | (Optional.) Data type for the row-partitioning tensor(s). One of `int32` or `int64`. Defaults to `int32`. |
| `validate` | (Optional.) Boolean indicating whether or not to validate that the input values form a valid RaggedTensor. Defaults to `False`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` | A `namedtuple` alias for field number 0 |
| `value_key` | A `namedtuple` alias for field number 1 |
| `partitions` | A `namedtuple` alias for field number 2 |
| `row_splits_dtype` | A `namedtuple` alias for field number 3 |
| `validate` | A `namedtuple` alias for field number 4 |

Child Classes
-------------

[`class RowLengths`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature/RowLengths)

[`class RowLimits`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature/RowLimits)

[`class RowSplits`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature/RowSplits)

[`class RowStarts`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature/RowStarts)

[`class UniformRowLength`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature/UniformRowLength)

[`class ValueRowIds`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature/ValueRowIds)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.