[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental\_connect\_to\_cluster Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/remote.py#L76-L275)

Connects to the given cluster.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental_connect_to_cluster`](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster)

tf.config.experimental_connect_to_cluster(
        cluster_spec_or_resolver,
        job_name='localhost',
        task_index=0,
        protocol=None,
        make_master_device_default=True,
        cluster_device_filters=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding)<br>    <br>*   [Migrate from TPUEstimator to TPUStrategy](https://www.tensorflow.org/guide/migrate/tpu_estimator)<br>    <br>*   [Use TPUs](https://www.tensorflow.org/guide/tpu) | *   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index)<br>    <br>*   [Solve GLUE tasks using BERT on TPU](https://www.tensorflow.org/text/tutorials/bert_glue) |

Will make devices on the cluster available to use. Note that calling this more than once will work, but will invalidate any tensor handles on the old remote devices.

If the given local job name is not present in the cluster specification, it will be automatically added, using an unused port on the localhost.

Device filters can be specified to isolate groups of remote tasks to avoid undesired accesses between workers. Workers accessing resources or launching ops / functions on filtered remote devices will result in errors (unknown devices). For any remote task, if no device filter is present, all cluster devices will be visible; if any device filter is specified, it can only see devices matching at least one filter. Devices on the task itself are always visible. Device filters can be particially specified.

For example, for a cluster set up for parameter server training, the following device filters might be specified:

cdf = tf.config.experimental.ClusterDeviceFilters()
    # For any worker, only the devices on PS nodes and itself are visible
    for i in range(num_workers):
      cdf.set_device_filters('worker', i, ['/job:ps'])
    # Similarly for any ps, only the devices on workers and itself are visible
    for i in range(num_ps):
      cdf.set_device_filters('ps', i, ['/job:worker'])
    
    tf.config.experimental_connect_to_cluster(cluster_def,
                                              cluster_device_filters=cdf)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cluster_spec_or_resolver` | A `ClusterSpec` or `ClusterResolver` describing the cluster. |
| `job_name` | The name of the local job. |
| `task_index` | The local task index. |
| `protocol` | The communication protocol, such as `"grpc"`. If unspecified, will use the default from `python/platform/remote_utils.py`. |
| `make_master_device_default` | If True and a cluster resolver is passed, will automatically enter the master task device scope, which indicates the master becomes the default device to run ops. It won't do anything if a cluster spec is passed. Will throw an error if the caller is currently already in some device scope. |
| `cluster_device_filters` | an instance of `tf.train.experimental/ClusterDeviceFilters` that specify device filters to the remote tasks in cluster. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.