[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftest%2FBenchmark&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#methods)
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#evaluate)
        
    *   [is\_abstract](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#is_abstract)
        
    *   [report\_benchmark](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#report_benchmark)
        
    *   [run\_op\_benchmark](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#run_op_benchmark)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.Benchmark Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#methods)
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#evaluate)
        
    *   [is\_abstract](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#is_abstract)
        
    *   [report\_benchmark](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#report_benchmark)
        
    *   [run\_op\_benchmark](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark#run_op_benchmark)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/benchmark.py#L287-L420)

Abstract class that provides helpers for TensorFlow benchmarks.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.Benchmark`](https://www.tensorflow.org/api_docs/python/tf/test/Benchmark)

tf.test.Benchmark()

Methods
-------

### `evaluate`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/benchmark.py#L410-L420)

evaluate(
        tensors
    )

Evaluates tensors and returns numpy values.

|     |     |
| --- | --- |
| Args |     |
| `tensors` | A Tensor or a nested list/tuple of Tensors. |

|     |
| --- |
| Returns |     |
| tensors numpy values. |     |

### `is_abstract`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/benchmark.py#L297-L301)

@classmethod

### `report_benchmark`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/benchmark.py#L242-L271)

report_benchmark(
        iters=None,
        cpu_time=None,
        wall_time=None,
        throughput=None,
        extras=None,
        name=None,
        metrics=None
    )

Report a benchmark.

|     |     |
| --- | --- |
| Args |     |
| `iters` | (optional) How many iterations were run |
| `cpu_time` | (optional) Median or mean cpu time in seconds. |
| `wall_time` | (optional) Median or mean wall time in seconds. |
| `throughput` | (optional) Throughput (in MB/s) |
| `extras` | (optional) Dict mapping string keys to additional benchmark info. Values may be either floats or values that are convertible to strings. |
| `name` | (optional) Override the BenchmarkEntry name with `name`. Otherwise it is inferred from the top-level method name. |
| `metrics` | (optional) A list of dict, where each dict has the keys below name (required), string, metric name value (required), double, metric value min\_value (optional), double, minimum acceptable metric value max\_value (optional), double, maximum acceptable metric value |

### `run_op_benchmark`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/benchmark.py#L303-L408)

run_op_benchmark(
        sess,
        op_or_tensor,
        feed_dict=None,
        burn_iters=2,
        min_iters=10,
        store_trace=False,
        store_memory_usage=True,
        name=None,
        extras=None,
        mbs=0
    )

Run an op or tensor in the given session. Report the results.

|     |     |
| --- | --- |
| Args |     |
| `sess` | `Session` object to use for timing. |
| `op_or_tensor` | `Operation` or `Tensor` to benchmark. |
| `feed_dict` | A `dict` of values to feed for each op iteration (see the `feed_dict` parameter of `Session.run`). |
| `burn_iters` | Number of burn-in iterations to run. |
| `min_iters` | Minimum number of iterations to use for timing. |
| `store_trace` | Boolean, whether to run an extra untimed iteration and store the trace of iteration in returned extras. The trace will be stored as a string in Google Chrome trace format in the extras field "full\_trace\_chrome\_format". Note that trace will not be stored in test\_log\_pb2.TestResults proto. |
| `store_memory_usage` | Boolean, whether to run an extra untimed iteration, calculate memory usage, and store that in extras fields. |
| `name` | (optional) Override the BenchmarkEntry name with `name`. Otherwise it is inferred from the top-level method name. |
| `extras` | (optional) Dict mapping string keys to additional benchmark info. Values may be either floats or values that are convertible to strings. |
| `mbs` | (optional) The number of megabytes moved by this op, used to calculate the ops throughput. |

|     |
| --- |
| Returns |     |
| A `dict` containing the key-value pairs that were passed to `report_benchmark`. If `store_trace` option is used, then `full_chrome_trace_format` will be included in return dictionary even though it is not passed to `report_benchmark` with `extras`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.