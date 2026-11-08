[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.SparseFeature Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_config.py#L266-L338)

Configuration for parsing a sparse input feature from an `Example`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.SparseFeature`](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature)
, [`tf.compat.v1.io.SparseFeature`](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature)

tf.io.SparseFeature(
        index_key, value_key, dtype, size, already_sorted=False
    )

Note, preferably use `VarLenFeature` (possibly in combination with a `SequenceExample`) in order to parse out `SparseTensor`s instead of `SparseFeature` due to its simplicity.

Closely mimicking the `SparseTensor` that will be obtained by parsing an `Example` with a `SparseFeature` config, a `SparseFeature` contains a

*   `value_key`: The name of key for a `Feature` in the `Example` whose parsed `Tensor` will be the resulting [`SparseTensor.values`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor#values)
    .
    
*   `index_key`: A list of names - one for each dimension in the resulting `SparseTensor` whose `indices[i][dim]` indicating the position of the `i`\-th value in the `dim` dimension will be equal to the `i`\-th value in the Feature with key named `index_key[dim]` in the `Example`.
    
*   `size`: A list of ints for the resulting [`SparseTensor.dense_shape`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor#dense_shape)
    .
    

For example, we can represent the following 2D `SparseTensor`

SparseTensor(indices=[[3, 1], [20, 0]],
                 values=[0.5, -1.0]
                 dense_shape=[100, 3])

with an `Example` input proto

features {
      feature { key: "val" value { float_list { value: [ 0.5, -1.0 ] } } }
      feature { key: "ix0" value { int64_list { value: [ 3, 20 ] } } }
      feature { key: "ix1" value { int64_list { value: [ 1, 0 ] } } }
    }

and `SparseFeature` config with 2 `index_key`s

SparseFeature(index_key=["ix0", "ix1"],
                  value_key="val",
                  dtype=tf.float32,
                  size=[100, 3])

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `index_key` | A single string name or a list of string names of index features. For each key the underlying feature's type must be `int64` and its length must always match that of the `value_key` feature. To represent `SparseTensor`s with a `dense_shape` of `rank` higher than 1 a list of length `rank` should be used. |
| `value_key` | Name of value feature. The underlying feature's type must be `dtype` and its length must always match that of all the `index_key`s' features. |
| `dtype` | Data type of the `value_key` feature. |
| `size` | A Python int or list thereof specifying the dense shape. Should be a list if and only if `index_key` is a list. In that case the list must be equal to the length of `index_key`. Each for each entry `i` all values in the `index_key`\[i\] feature must be in `[0, size[i])`. |\
| `already_sorted` | A Python boolean to specify whether the values in `value_key` are already sorted by their index position. If so skip sorting. False by default (optional). |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `index_key` | A `namedtuple` alias for field number 0 |\
| `value_key` | A `namedtuple` alias for field number 1 |\
| `dtype` | A `namedtuple` alias for field number 2 |\
| `size` | A `namedtuple` alias for field number 3 |\
| `already_sorted` | A `namedtuple` alias for field number 4 |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.