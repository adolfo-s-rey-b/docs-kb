[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/experimental#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/config/experimental#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/config/experimental#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.config.experimental Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/config/experimental#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/config/experimental#functions)
    

Public API for tf.\_api.v2.config.experimental namespace

Classes
-------

[`class ClusterDeviceFilters`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/ClusterDeviceFilters)
: Represent a collection of device filters for the remote workers in cluster.

[`class VirtualDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration)
: Configuration class for a logical devices.

Functions
---------

[`disable_mlir_bridge(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/disable_mlir_bridge)
: Disables experimental MLIR-Based TensorFlow Compiler Bridge.

[`enable_mlir_bridge(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_mlir_bridge)
: Enables experimental MLIR-Based TensorFlow Compiler Bridge.

[`enable_op_determinism(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_op_determinism)
: Configures TensorFlow ops to run deterministically.

[`enable_tensor_float_32_execution(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_tensor_float_32_execution)
: Enable or disable the use of TensorFloat-32 on supported hardware.

[`get_device_details(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_details)
: Returns details about a physical devices.

[`get_device_policy(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_device_policy)
: Gets the current device policy.

[`get_memory_growth(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_growth)
: Get if memory growth is enabled for a `PhysicalDevice`.

[`get_memory_info(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_info)
: Get memory info for the chosen device, as a dict.

[`get_memory_usage(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_memory_usage)
: Get the current memory usage, in bytes, for the chosen device. (deprecated)

[`get_synchronous_execution(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/get_synchronous_execution)
: Gets whether operations are executed synchronously or asynchronously.

[`get_virtual_device_configuration(...)`](https://www.tensorflow.org/api_docs/python/tf/config/get_logical_device_configuration)
: Get the virtual device configuration for a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
.

[`get_visible_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/config/get_visible_devices)
: Get the list of visible physical devices.

[`list_logical_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/config/list_logical_devices)
: Return a list of logical devices created by runtime.

[`list_physical_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)
: Return a list of physical devices visible to the host runtime.

[`reset_memory_stats(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/reset_memory_stats)
: Resets the tracked memory stats for the chosen device.

[`set_device_policy(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_device_policy)
: Sets the current thread device policy.

[`set_memory_growth(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth)
: Set if memory growth should be enabled for a `PhysicalDevice`.

[`set_synchronous_execution(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_synchronous_execution)
: Specifies whether operations are executed synchronously or asynchronously.

[`set_virtual_device_configuration(...)`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)
: Set the logical device configuration for a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice)
.

[`set_visible_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices)
: Set the list of visible devices.

[`tensor_float_32_execution_enabled(...)`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/tensor_float_32_execution_enabled)
: Returns whether TensorFloat-32 is enabled.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.