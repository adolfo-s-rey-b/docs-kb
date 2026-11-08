[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parse_example_dataset#main-content)

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
    

tf.data.experimental.parse\_example\_dataset Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/parsing_ops.py#L105-L161)

A transformation that parses `Example` protos into a `dict` of tensors. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.parse_example_dataset`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parse_example_dataset)

tf.data.experimental.parse_example_dataset(
        features, num_parallel_calls=1, deterministic=None
    )

Parses a number of serialized `Example` protos given in `serialized`. We refer to `serialized` as a batch with `batch_size` many entries of individual `Example` protos.

This op parses serialized examples into a dictionary mapping keys to `Tensor`, `SparseTensor`, and `RaggedTensor` objects. `features` is a dict from keys to `VarLenFeature`, `RaggedFeature`, `SparseFeature`, and `FixedLenFeature` objects. Each `VarLenFeature` and `SparseFeature` is mapped to a `SparseTensor`; each `RaggedFeature` is mapped to a `RaggedTensor`; and each `FixedLenFeature` is mapped to a `Tensor`. See [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example)
 for more details about feature dictionaries.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `dict` mapping feature keys to `FixedLenFeature`, `VarLenFeature`, `RaggedFeature`, and `SparseFeature` values. |
| `num_parallel_calls` | (Optional.) A [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of parsing processes to call in parallel. |
| `deterministic` | (Optional.) A boolean controlling whether determinism should be traded for performance by allowing elements to be produced out of order if some parsing calls complete faster than others. If `deterministic` is `None`, the [`tf.data.Options.deterministic`](https://www.tensorflow.org/api_docs/python/tf/data/Options#deterministic)<br> dataset option (`True` by default) is used to decide whether to produce elements deterministically. |

|     |
| --- |
| Returns<br>------- |     |
| A dataset transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if features argument is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.