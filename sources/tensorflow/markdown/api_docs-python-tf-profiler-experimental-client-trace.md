[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/trace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/trace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/trace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/trace#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/trace#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.profiler.experimental.client.trace Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/trace#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/trace#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/profiler_client.py#L24-L136)

Sends gRPC requests to one or more profiler servers to perform on-demand profiling.

tf.profiler.experimental.client.trace(
        service_addr,
        logdir,
        duration_ms,
        worker_list='',
        num_tracing_attempts=3,
        options=None
    )

This method will block the calling thread until it receives responses from all servers or until deadline expiration. Both single host and multiple host profiling are supported on CPU, GPU, and TPU. The profiled results will be saved by each server to the specified TensorBoard log directory (i.e. the directory you save your model checkpoints). Use the TensorBoard profile plugin to view the visualization and analysis results.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `service_addr` | A comma delimited string of gRPC addresses of the workers to profile. e.g. service\_addr='grpc://localhost:6009' service\_addr='grpc://10.0.0.2:8466,grpc://10.0.0.3:8466' service\_addr='grpc://localhost:12345,grpc://localhost:23456' |
| `logdir` | Path to save profile data to, typically a TensorBoard log directory. This path must be accessible to both the client and server. e.g. logdir='gs://your\_tb\_dir' |
| `duration_ms` | Duration of tracing or monitoring in milliseconds. Must be greater than zero. |
| `worker_list` | An optional TPU only configuration. The list of workers to profile in the current session. |
| `num_tracing_attempts` | Optional. Automatically retry N times when no trace event is collected (default 3). |
| `options` | profiler.experimental.ProfilerOptions namedtuple for miscellaneous profiler options. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | For when arguments fail validation checks. |
| `UnavailableError` | If no trace event was collected. |

Example usage (CPU/GPU):

  # Start a profiler server before your model runs.
      tf.profiler.experimental.server.start(6009)
      # (Model code goes here).
      # Send gRPC request to the profiler server to collect a trace of your model.
      tf.profiler.experimental.client.trace('grpc://localhost:6009',
                                            '/nfs/tb_log', 2000)

Example usage (Multiple GPUs):

  # E.g. your worker IP addresses are 10.0.0.2, 10.0.0.3, 10.0.0.4, and you
      # would like to schedule start of profiling 1 second from now, for a
      # duration of 2 seconds.
      options['delay_ms'] = 1000
      tf.profiler.experimental.client.trace(
          'grpc://10.0.0.2:8466,grpc://10.0.0.3:8466,grpc://10.0.0.4:8466',
          'gs://your_tb_dir',
          2000,
          options=options)

Example usage (TPU):

  # Send gRPC request to a TPU worker to collect a trace of your model. A
      # profiler service has been started in the TPU worker at port 8466.
      # E.g. your TPU IP address is 10.0.0.2 and you want to profile for 2 seconds
      # .
      tf.profiler.experimental.client.trace('grpc://10.0.0.2:8466',
                                            'gs://your_tb_dir', 2000)

Example usage (Multiple TPUs):

  # Send gRPC request to a TPU pod to collect a trace of your model on
      # multiple TPUs. A profiler service has been started in all the TPU workers
      # at the port 8466.
      # E.g. your TPU IP addresses are 10.0.0.2, 10.0.0.3, 10.0.0.4, and you want
      # to profile for 2 seconds.
      tf.profiler.experimental.client.trace(
          'grpc://10.0.0.2:8466',
          'gs://your_tb_dir',
          2000,
          '10.0.0.2:8466,10.0.0.3:8466,10.0.0.4:8466')

Launch TensorBoard and point it to the same logdir you provided to this API.

  # logdir can be gs://your_tb_dir as in the above examples.
      $ tensorboard --logdir=/tmp/tb_log

Open your browser and go to localhost:6006/#profile to view profiling results.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.