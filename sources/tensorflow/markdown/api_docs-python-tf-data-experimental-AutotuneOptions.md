[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.AutotuneOptions Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/options.py#L193-L289)

Represents options for autotuning dataset performance.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.AutotuneOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions)

tf.data.experimental.AutotuneOptions()

options = tf.data.Options()
    options.autotune.enabled = False
    dataset = dataset.with_options(options)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `autotune_algorithm` | When autotuning is enabled (through `autotune`), determines the algorithm to use. |
| `cpu_budget` | When autotuning is enabled (through `autotune`), determines the CPU budget to use. Values greater than the number of schedulable CPU cores are allowed but may result in CPU contention. If None, defaults to the number of schedulable CPU cores. |
| `enabled` | Whether to automatically tune performance knobs. If None, defaults to True. |
| `initial_parallelism` | The initial parallelism to use for parallel transformations before autotune has a chance to run. A higher value can help with quick startup, but may cause the ram\_budget to temporarily be exceeded. Memory-sensitive datasets should consider setting this to `1` to avoid running out of memory. Defaults to 16. |
| `min_parallelism` | When true, `.map(num_parallel_calls=AUTOTUNE)` and `.batch(num_parallel_calls=AUTOTUNE)` will be at least parallelized by `min_parallelism` threads. |
| `ram_budget` | When autotuning is enabled (through `autotune`), determines the RAM budget to use. Values greater than the available RAM in bytes may result in OOM. If None, defaults to half of the available RAM in bytes. |

Methods
-------

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/util/options.py#L38-L44)

__eq__(
        other
    )

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/util/options.py#L46-L50)

__ne__(
        other
    )

Return self!=value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.