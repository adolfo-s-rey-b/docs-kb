[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fdtensor&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.experimental.dtensor Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor#other-members)
    

Public API for tf.\_api.v2.experimental.dtensor namespace

Classes
-------

[`class DTensorCheckpoint`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint)
: Manages saving/restoring trackable values to disk, for DTensor. (deprecated)

[`class DTensorDataset`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorDataset)
: A dataset of DTensors.

[`class DVariable`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DVariable)
: A replacement for tf.Variable which follows initial value placement.

[`class Layout`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout)
: Represents the layout information of a DTensor.

[`class Mesh`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh)
: Represents a Mesh configuration over a certain list of Mesh Dimensions.

Functions
---------

[`barrier(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/barrier)
: Runs a barrier on the mesh.

[`call_with_layout(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/call_with_layout)
: Calls a function in the DTensor device scope if `layout` is not None.

[`check_layout(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/check_layout)
: Asserts that the layout of the DTensor is `layout`.

[`client_id(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/client_id)
: Returns this client's ID.

[`copy_to_mesh(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/copy_to_mesh)
: Copies a tf.Tensor onto the DTensor device with the given layout.

[`create_distributed_mesh(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_distributed_mesh)
: Creates a distributed mesh.

[`create_mesh(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_mesh)
: Creates a single-client mesh.

[`create_tpu_mesh(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/create_tpu_mesh)
: Returns a distributed TPU mesh optimized for AllReduce ring reductions.

[`default_mesh(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/default_mesh)
: Sets the default DTensor device mesh to use for enclosed functions.

[`device_name(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/device_name)
: Returns the singleton DTensor device's name.

[`enable_save_as_bf16(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/enable_save_as_bf16)
: Allows float32 DVariables to be checkpointed and restored as bfloat16.

[`fetch_layout(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/fetch_layout)
: Fetches the layout of a DTensor.

[`full_job_name(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/full_job_name)
: Returns the fully qualified TF job name for this or another task.

[`get_default_mesh(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/get_default_mesh)
: Return the default mesh under the current dtensor device context.

[`heartbeat_enabled(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/heartbeat_enabled)
: Returns true if DTensor heartbeat service is enabled.

[`initialize_accelerator_system(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system)
: Initializes accelerators and communication fabrics for DTensor.

[`initialize_multi_client(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system)
: Initializes accelerators and communication fabrics for DTensor.

[`initialize_tpu_system(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/initialize_accelerator_system)
: Initializes accelerators and communication fabrics for DTensor.

[`is_dtensor(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/is_dtensor)
: Check whether the input tensor is a DTensor.

[`job_name(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/job_name)
: Returns the job name used by all clients in this DTensor cluster.

[`jobs(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/jobs)
: Returns a list of job names of all clients in this DTensor cluster.

[`local_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/local_devices)
: Returns a list of device specs configured on this client.

[`name_based_restore(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_restore)
: Restores from checkpoint\_prefix to name based DTensors.

[`name_based_save(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_save)
: Saves name based Tensor into a Checkpoint.

[`num_clients(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/num_clients)
: Returns the number of clients in this DTensor cluster.

[`num_global_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/num_global_devices)
: Returns the number of devices of device\_type in this DTensor cluster.

[`num_local_devices(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/num_local_devices)
: Returns the number of devices of device\_type configured on this client.

[`pack(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/pack)
: Packs [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 components into a DTensor.

[`preferred_device_type(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/preferred_device_type)
: Returns the preferred device type for the accelerators.

[`relayout(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout)
: Changes the layout of `tensor`.

[`relayout_like(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout_like)
: Changes the layout of `tensor` to the same as `layout_tensor`.

[`run_on(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/run_on)
: Runs enclosed functions in the DTensor device scope. (deprecated)

[`sharded_save(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/sharded_save)
: Saves given named tensor slices in a sharded, multi-client safe fashion.

[`shutdown_accelerator_system(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/shutdown_accelerator_system)
: Shuts down the accelerator system.

[`shutdown_tpu_system(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/shutdown_accelerator_system)
: Shuts down the accelerator system.

[`unpack(...)`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/unpack)
: Unpacks a DTensor into [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 components.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| MATCH | `'match'` |
| UNSHARDED | `'unsharded'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.