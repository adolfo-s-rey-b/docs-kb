[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/Options#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/Options)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/Options?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/Options#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/Options#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/Options#methods)
    *   [merge](https://www.tensorflow.org/api_docs/python/tf/data/Options#merge)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/Options#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/Options#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.Options Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/Options#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/Options#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/Options#methods)
    *   [merge](https://www.tensorflow.org/api_docs/python/tf/data/Options#merge)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/Options#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/Options#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/options.py#L579-L825)

Represents options for [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)

tf.data.Options()

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input)<br>    <br>*   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras) |

A [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)
 object can be, for instance, used to control which static optimizations to apply to the input pipeline graph or whether to use performance modeling to dynamically tune the parallelism of operations such as [`tf.data.Dataset.map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map)
 or [`tf.data.Dataset.interleave`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)
.

The options are set for the entire dataset and are carried over to datasets created through tf.data transformations.

The options can be set by constructing an `Options` object and using the [`tf.data.Dataset.with_options(options)`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#with_options)
 transformation, which returns a dataset with the options set.

    dataset = tf.data.Dataset.range(42)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `autotune` | The autotuning options associated with the dataset. See [`tf.data.experimental.AutotuneOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneOptions)<br> for more details. |
| `dataset_name` | A name for the dataset, to help in debugging. |
| `deterministic` | Whether the outputs need to be produced in deterministic order. If None, defaults to True. |
| `experimental_deterministic` | DEPRECATED. Use `deterministic` instead. |
| `experimental_distribute` | The distribution strategy options associated with the dataset. See [`tf.data.experimental.DistributeOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions)<br> for more details. |
| `experimental_external_state_policy` | This option can be used to override the default policy for how to handle external state when serializing a dataset or checkpointing its iterator. There are three settings available - IGNORE: External state is ignored without a warning; WARN: External state is ignored and a warning is logged; FAIL: External state results in an error. |
| `experimental_optimization` | The optimization options associated with the dataset. See [`tf.data.experimental.OptimizationOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/OptimizationOptions)<br> for more details. |
| `experimental_service` | The tf.data service options associated with the dataset. See [`tf.data.experimental.ServiceOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions)<br> for more details. |
| `experimental_slack` | Whether to introduce 'slack' in the last `prefetch` of the input pipeline, if it exists. This may reduce CPU contention with accelerator host-side activity at the start of a step. The slack frequency is determined by the number of devices attached to this input pipeline. If None, defaults to False. |
| `experimental_symbolic_checkpoint` | Whether to checkpoint internal input pipeline state maintaining cursors into data sources that identify last element(s) produced as output to the tf.data consumer. This is alternative to the default 'explicit' checkpointing which stores the internal input pipeline state in the checkpoint. Note that symbolic checkpointing is not supported for transformations that can reorder elements. |
| `experimental_threading` | DEPRECATED. Use `threading` instead. |
| `experimental_warm_start` | Whether to start background threads of asynchronous transformations upon iterator creation, as opposed to during the first call to `next()`. Defaults to `False`. This improves the latency of the initial 'next()' calls at the expense of requiring more memory to hold prefetched elements between the time of iterator construction and usage. |
| `framework_type` | The list of frameworks that are used to generate this pipeline, used for telemetry. |
| `threading` | The threading options associated with the dataset. See [`tf.data.ThreadingOptions`](https://www.tensorflow.org/api_docs/python/tf/data/ThreadingOptions)<br> for more details. |

Methods
-------

### `merge`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/options.py#L811-L825)

merge(
        options
    )

Merges itself with the given [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)
.

If this object and the `options` to merge set an option differently, a warning is generated and this object's value is updated with the `options` object's value.

|     |     |
| --- | --- |
| Args |     |
| `options` | The [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)<br> to merge with. |

|     |
| --- |
| Returns |     |
| New [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)<br> object which is the result of merging self with the input [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)<br>. |     |

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