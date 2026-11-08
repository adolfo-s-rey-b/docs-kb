[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.OptimizationOptions Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/options.py#L334-L493)

Represents options for dataset optimizations.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.OptimizationOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions)

tf.data.experimental.OptimizationOptions()

You can set the optimization options of a dataset through the `experimental_optimization` property of [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)
; the property is an instance of [`tf.data.experimental.OptimizationOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions)
.

options = tf.data.Options()
    options.experimental_optimization.noop_elimination = True
    options.experimental_optimization.apply_default_optimizations = False
    dataset = dataset.with_options(options)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `apply_default_optimizations` | Whether to apply default graph optimizations. If False, only graph optimizations that have been explicitly enabled will be applied. |
| `filter_fusion` | Whether to fuse filter transformations. If None, defaults to False. |
| `filter_parallelization` | Whether to parallelize stateless filter transformations. If None, defaults to False. |
| `inject_prefetch` | Whether to inject prefetch transformation as the last transformation when the last transformation is a synchronous transformation. If None, defaults to True. |
| `map_and_batch_fusion` | Whether to fuse map and batch transformations. If None, defaults to True. |
| `map_and_filter_fusion` | Whether to fuse map and filter transformations. If None, defaults to False. |
| `map_fusion` | Whether to fuse map transformations with `num_parallel_calls` set to [`tf.data.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data#AUTOTUNE)<br>, no captured inputs and same `deterministic` value. If None, defaults to False. |
| `map_parallelization` | Whether to parallelize stateless map transformations. If None, defaults to True. |
| `noop_elimination` | Whether to eliminate no-op transformations. If None, defaults to True. |
| `parallel_batch` | Whether to parallelize copying of batch elements. If None, defaults to True. |
| `seq_interleave_prefetch` | Whether to replace parallel interleave using a sequential interleave that prefetches elements from its input iterators. If None, defaults to False. |
| `shuffle_and_repeat_fusion` | Whether to fuse shuffle and repeat transformations. If None, defaults to True. |

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