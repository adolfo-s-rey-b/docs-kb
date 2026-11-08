[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.RowIdInitializer Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L1522-L1534)

An initializer that initializes the table with vocabulary ids.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.RowIdInitializer`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/RowIdInitializer)

tf.tpu.experimental.embedding.RowIdInitializer(
        offset: int = 0
    )

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L1529-L1534)

__call__(
        shape: Union[Sequence[int], tf.TensorShape],
        dtype: tf.dtypes.DType
    ) -> core.Tensor

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.