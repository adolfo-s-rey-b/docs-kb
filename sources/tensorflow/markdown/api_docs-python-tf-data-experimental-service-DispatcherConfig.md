[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.service.DispatcherConfig Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/service/server_lib.py#L44-L127)

Configuration class for tf.data service dispatchers.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.service.DispatcherConfig`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/service/DispatcherConfig)

tf.data.experimental.service.DispatcherConfig(
        port=0,
        protocol=None,
        work_dir=None,
        fault_tolerant_mode=False,
        worker_addresses=None,
        job_gc_check_interval_ms=None,
        job_gc_timeout_ms=None,
        worker_timeout_ms=None,
        worker_max_concurrent_snapshots=0
    )

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `port` | Specifies the port to bind to. A value of 0 indicates that the server may bind to any available port. |
| `protocol` | The protocol to use for communicating with the tf.data service, e.g. "grpc". |
| `work_dir` | A directory to store dispatcher state in. This argument is required for the dispatcher to be able to recover from restarts. |
| `fault_tolerant_mode` | Whether the dispatcher should write its state to a journal so that it can recover from restarts. Dispatcher state, including registered datasets and created jobs, is synchronously written to the journal before responding to RPCs. If `True`, `work_dir` must also be specified. |
| `worker_addresses` | If the job uses auto-sharding, it needs to specify a fixed list of worker addresses that will register with the dispatcher. The worker addresses should be in the format `"host"` or `"host:port"`, where `"port"` is an integer, named port, or `%port%` to match any port. |
| `job_gc_check_interval_ms` | How often the dispatcher should scan through to delete old and unused jobs, in milliseconds. If not set, the runtime will select a reasonable default. A higher value will reduce load on the dispatcher, while a lower value will reduce the time it takes for the dispatcher to garbage collect expired jobs. |
| `job_gc_timeout_ms` | How long a job needs to be unused before it becomes a candidate for garbage collection, in milliseconds. A value of -1 indicates that jobs should never be garbage collected. If not set, the runtime will select a reasonable default. A higher value will cause jobs to stay around longer with no consumers. This is useful if there is a large gap in time between when consumers read from the job. A lower value will reduce the time it takes to reclaim the resources from expired jobs. |
| `worker_timeout_ms` | How long to wait for a worker to heartbeat before considering it missing. If not set, the runtime will select a reasonable default. |
| `worker_max_concurrent_snapshots` | The maximum number of snapshots a worker can concurrently process. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `port` | A `namedtuple` alias for field number 0 |
| `protocol` | A `namedtuple` alias for field number 1 |
| `work_dir` | A `namedtuple` alias for field number 2 |
| `fault_tolerant_mode` | A `namedtuple` alias for field number 3 |
| `worker_addresses` | A `namedtuple` alias for field number 4 |
| `job_gc_check_interval_ms` | A `namedtuple` alias for field number 5 |
| `job_gc_timeout_ms` | A `namedtuple` alias for field number 6 |
| `worker_timeout_ms` | A `namedtuple` alias for field number 7 |
| `worker_max_concurrent_snapshots` | A `namedtuple` alias for field number 8 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.