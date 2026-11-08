[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/monitor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/monitor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/monitor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/monitor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/monitor#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.profiler.experimental.client.monitor Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/monitor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/client/monitor#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/profiler_client.py#L139-L170)

Sends grpc requests to profiler server to perform on-demand monitoring.

tf.profiler.experimental.client.monitor(
        service_addr, duration_ms, level=1
    )

The monitoring result is a light weight performance summary of your model execution. This method will block the caller thread until it receives the monitoring result. This method currently supports Cloud TPU only.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `service_addr` | gRPC address of profiler service e.g. grpc://10.0.0.2:8466. |
| `duration_ms` | Duration of monitoring in ms. |
| `level` | Choose a monitoring level between 1 and 2 to monitor your job. Level 2 is more verbose than level 1 and shows more metrics. |

|     |
| --- |
| Returns<br>------- |     |
| A string of monitoring output. |     |

#### Example usage:

  # Continuously send gRPC requests to the Cloud TPU to monitor the model
      # execution.
    
      for query in range(0, 100):
        print(
          tf.profiler.experimental.client.monitor('grpc://10.0.0.2:8466', 1000))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.