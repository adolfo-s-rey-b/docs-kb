[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.initialize\_accelerator\_system Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/accelerator_util.py#L114-L265)

Initializes accelerators and communication fabrics for DTensor.

#### View aliases

**Main aliases**

[`tf.experimental.dtensor.initialize_multi_client`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system)
, [`tf.experimental.dtensor.initialize_tpu_system`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system)

tf.experimental.dtensor.initialize_accelerator_system(
        device_type: Optional[str] = None,
        enable_coordination_service: Optional[bool] = True,
        num_logical_cpu_devices: Optional[int] = None,
        experimental_reset_context: Optional[bool] = False,
        experimental_enable_megcore: Optional[bool] = False
    ) -> str

DTensor configures TensorFlow to run in the local mode or multi-client mode.

*   In local mode, a mesh can only use devices attached to the current process.
*   In multi-client mode, a mesh can span across devices from multiple clients.

If `DTENSOR_JOBS` is non-empty, DTensor configures TensorFlow to run in the multi-client mode using the distributed runtime. In multi-client mode devices on different clients can communicate with each other.

The following environment variables controls the behavior of this function.

*   `DTENSOR_JOBS`: string, a comma separated list. Each item in the list is of format `{hostname}:{port}`. If empty, DTensor runs in the local mode. Examples of valid `DTENSOR_JOBS` values:
    *   4 clients on localhost: `localhost:10000,localhost:10001,localhost:10002,localhost:10003`
    *   2 clients on host1, 2 clients on host2 `host1:10000,host1:10001,host2:10000,host2:10003` If the hostnames are BNS addresses, the items must be sorted in alphabetical order.
*   `DTENSOR_CLIENT_ID`: integer, between `0` to `num_clients - 1`, to identify the client id of the current process. The default value is `0`.
*   `DTENSOR_JOB_NAME`: string, a string for the name of the TensorFlow job. The job name controls the job name section of the TensorFlow DeviceSpecs, e.g., `job:worker` in `/job:worker/replica:0/task:0/device:TPU:0` when the job name is `worker`. The default value is `localhost` in local mode, and `worker` when in the multi-client mode. All DTensor clients within the same multi-client cluster share the same job name.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_type` | Type of accelerator to use, can be CPU, GPU, or TPU. If None, uses [`tf.experimental.dtensor.preferred_device_type()`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/preferred_device_type)<br>. |
| `enable_coordination_service` | If true, enable distributed coordination service to make sure that workers know the devices on each other, when there is more than 1 client. |
| `num_logical_cpu_devices` | the number of logical CPU devices per DTensor client. Default to the current number of logical CPU (`dtensor.num_local_devices("CPU")`),when `device_type` is CPU, otherwise set automatially to match the number of local GPU/TPU devices. |
| `experimental_reset_context` | Reset the tensorflow context. Behaviors of existing TensorFlow objects (e.g. Tensors) are undefined. Set this to True as an escape hatch, if there is no clear way to refactor your code to call initialize\_accelerator\_system() before calling TensorFlow APIs that initialize the context. |
| `experimental_enable_megcore` | Optionally enable megcore in backend. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `device_type` | the type of accelerator that was initialized. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.