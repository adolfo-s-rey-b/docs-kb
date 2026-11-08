[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.SparseCoreEmbeddingConfig Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_v3.py#L81-L92)

Config for sparsecore embedding.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.SparseCoreEmbeddingConfig`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/SparseCoreEmbeddingConfig)

tf.tpu.experimental.embedding.SparseCoreEmbeddingConfig(
        disable_table_stacking: bool = False,
        max_ids_per_chip_per_sample: int = 64,
        max_ids_per_table: Optional[Dict[str, int]] = None,
        max_unique_ids_per_table: Optional[Dict[str, int]] = None,
        allow_id_dropping: bool = False,
        initialize_tables_on_host: bool = True,
        enable_fast_table_initialization: bool = False
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `disable_table_stacking` | Dataclass field |
| `max_ids_per_chip_per_sample` | Dataclass field |
| `max_ids_per_table` | Dataclass field |
| `max_unique_ids_per_table` | Dataclass field |
| `allow_id_dropping` | Dataclass field |
| `initialize_tables_on_host` | Dataclass field |
| `enable_fast_table_initialization` | Dataclass field |

Methods
-------

### `__eq__`

__eq__(
        other
    )

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| allow\_id\_dropping | `False` |
| disable\_table\_stacking | `False` |
| enable\_fast\_table\_initialization | `False` |
| initialize\_tables\_on\_host | `True` |
| max\_ids\_per\_chip\_per\_sample | `64` |
| max\_ids\_per\_table | `None` |
| max\_unique\_ids\_per\_table | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.