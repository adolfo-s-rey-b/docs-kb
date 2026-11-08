[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_host#main-content)

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
    

tf.config.experimental\_connect\_to\_host Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/remote.py#L37-L73)

Connects to a single machine to enable remote execution on it.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental_connect_to_host`](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_host)

tf.config.experimental_connect_to_host(
        remote_host=None, job_name='worker'
    )

Will make devices on the remote host available to use. Note that calling this more than once will work, but will invalidate any tensor handles on the old remote devices.

Using the default job\_name of worker, you can schedule ops to run remotely as follows:

# When eager execution is enabled, connect to the remote host.
    tf.config.experimental_connect_to_host("exampleaddr.com:9876")
    
    with ops.device("job:worker/replica:0/task:1/device:CPU:0"):
      # The following tensors should be resident on the remote device, and the op
      # will also execute remotely.
      x1 = array_ops.ones([2, 2])
      x2 = array_ops.ones([2, 2])
      y = math_ops.matmul(x1, x2)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `remote_host` | a single or a list the remote server addr in host-port format. |
| `job_name` | The job name under which the new server will be accessible. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if remote\_host is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.