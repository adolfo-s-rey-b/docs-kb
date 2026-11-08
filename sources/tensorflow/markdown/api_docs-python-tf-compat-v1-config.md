[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/config#main-content)

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
    

Module: tf.compat.v1.config Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

Public API for tf.\_api.v2.config namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/config/experimental)
 module: Public API for tf.\_api.v2.config.experimental namespace

[`optimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/config/optimizer)
 module: Public API for tf.\_api.v2.config.optimizer namespace

[`threading`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/config/threading)
 module: Public API for tf.\_api.v2.config.threading namespace

Classes
-------

[`class LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice)
: Abstraction for a logical device initialized by the runtime.

[`class LogicalDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)
: Configuration class for a logical devices.

[`class PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
: Abstraction for a locally visible physical device.

Functions
---------

[`experimental_connect_to_cluster(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_cluster)
: Connects to the given cluster.

[`experimental_connect_to_host(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental_connect_to_host)
: Connects to a single machine to enable remote execution on it.

[`experimental_functions_run_eagerly(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental_functions_run_eagerly)
: Returns the value of the `experimental_run_functions_eagerly` setting. (deprecated)

[`experimental_run_functions_eagerly(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental_run_functions_eagerly)
: Enables / disables eager execution of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
s. (deprecated)

[`functions_run_eagerly(...)`](https://www.tensorflow.org/api_docs/python/tf/config/functions_run_eagerly)
: Returns the value of the `run_functions_eagerly` setting.

[`get_logical_device_configuration(...)`](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration)
: Get the virtual device configuration for a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
.

[`get_soft_device_placement(...)`](https://www.tensorflow.org/api_docs/python/tf/config/get_soft_device_placement)
: Return status of soft device placement flag.

[`get_visible_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/config/get_visible_devices)
: Get the list of visible physical devices.

[`list_logical_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices)
: Return a list of logical devices created by runtime.

[`list_physical_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)
: Return a list of physical devices visible to the host runtime.

[`run_functions_eagerly(...)`](https://www.tensorflow.org/api_docs/python/tf/config/run_functions_eagerly)
: Enables / disables eager execution of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
s.

[`set_logical_device_configuration(...)`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)
: Set the logical device configuration for a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
.

[`set_soft_device_placement(...)`](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement)
: Enable or disable soft device placement.

[`set_visible_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices)
: Set the list of visible devices.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.