[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters#methods)
    *   [set\_device\_filters](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters#set_device_filters)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.experimental.ClusterDeviceFilters Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters#methods)
    *   [set\_device\_filters](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters#set_device_filters)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L495-L574)

Represent a collection of device filters for the remote workers in cluster.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.experimental.ClusterDeviceFilters`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters)

tf.config.experimental.ClusterDeviceFilters()

Set device filters for selective jobs and tasks. For each remote worker, the device filters are a list of strings. When any filters are present, the remote worker will ignore all devices which do not match any of its filters. Each filter can be partially specified, e.g. "/job:ps", "/job:worker/replica:3", etc. Note that a device is always visible to the worker it is located on.

For example, to set the device filters for a parameter server cluster:

cdf = tf.config.experimental.ClusterDeviceFilters()
    for i in range(num_workers):
      cdf.set_device_filters('worker', i, ['/job:ps'])
    for i in range(num_ps):
      cdf.set_device_filters('ps', i, ['/job:worker'])
    
    tf.config.experimental_connect_to_cluster(cluster_def,
                                              cluster_device_filters=cdf)

The device filters can be partically specified. For remote tasks that do not have device filters specified, all devices will be visible to them.

Methods
-------

### `set_device_filters`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/server_lib.py#L533-L539)

set_device_filters(
        job_name, task_index, device_filters
    )

Set the device filters for given job name and task id.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.