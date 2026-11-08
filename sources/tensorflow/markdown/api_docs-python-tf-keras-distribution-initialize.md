[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/initialize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/initialize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/initialize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/initialize#args)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/initialize#example)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distribution.initialize Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/initialize#args)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/initialize#example)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L64-L151)

Initialize the distribution system for multi-host/process setting.

tf.keras.distribution.initialize(
        job_addresses=None, num_processes=None, process_id=None
    )

Calling `initialize` will prepare the backend for execution on multi-host GPU or TPUs. It should be called before any computations.

Note that the parameters can also be injected via environment variables, which can be better controlled by the launch script at startup time. For certain backend that also rely on the environment variables to configure, Keras will properly forward them.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `job_addresses` | string. Comma separated IP addresses for all the jobs that will form the whole computation cluster. Note that for JAX backend, only the address for job 0 (coodinator) is needed. For certain runtime like cloud TPU, this value can be `None`, and the backend will figure it out with the TPU environment variables. You can also config this value via environment variable `KERAS_DISTRIBUTION_JOB_ADDRESSES`. |
| `num_processes` | int. The number of worker/processes that will form the whole computation cluster. For certain runtime like cloud TPU, this value can be `None`, and the backend will figure it out with the TPU environment variables. You can also configure this value via environment variable `KERAS_DISTRIBUTION_NUM_PROCESSES`. |
| `process_id` | int. The ID number of the current worker/process. The value should be ranged from `0` to `num_processes - 1`. `0` will indicate the current worker/process is the master/coordinate job. You can also configure this value via environment variable `KERAS_DISTRIBUTION_PROCESS_ID`. |

|     |
| --- |
| Example<br>------- |     |
| Suppose there are two GPU processes, and process 0 is running at address `10.0.0.1:1234`, and process 1 is running at address `10.0.0.2:2345`. To configure such cluster, you can run<br><br>On process 0:<br><br>keras.distribute.initialize(<br>        job_addresses="10.0.0.1:1234,10.0.0.2:2345",<br>        num_processes=2,<br>        process_id=0)<br><br>On process 1:<br><br>keras.distribute.initialize(<br>        job_addresses="10.0.0.1:1234,10.0.0.2:2345",<br>        num_processes=2,<br>        process_id=1)<br><br>or via the environment variables: On process 0:<br><br>os.environ[<br>        "KERAS_DISTRIBUTION_JOB_ADDRESSES"] = "10.0.0.1:1234,10.0.0.2:2345"<br>    os.environ["KERAS_DISTRIBUTION_NUM_PROCESSES"] = "2"<br>    os.environ["KERAS_DISTRIBUTION_PROCESS_ID"] = "0"<br>    keras.distribute.initialize()<br><br>On process 1:<br><br>os.environ[<br>        "KERAS_DISTRIBUTION_JOB_ADDRESSES"] = "10.0.0.1:1234,10.0.0.2:2345"<br>    os.environ["KERAS_DISTRIBUTION_NUM_PROCESSES"] = "2"<br>    os.environ["KERAS_DISTRIBUTION_PROCESS_ID"] = "1"<br>    keras.distribute.initialize()<br><br>Also note that for JAX backend, the `job_addresses` can be further reduced to just the master/coordinator address, which is `10.0.0.1:1234`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.