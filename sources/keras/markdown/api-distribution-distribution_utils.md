None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [LayoutMap API](https://keras.io/api/distribution/layout_map/)
 [DataParallel API](https://keras.io/api/distribution/data_parallel/)
 [ModelParallel API](https://keras.io/api/distribution/model_parallel/)
 [Distribution utilities](https://keras.io/api/distribution/distribution_utils/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Multi-device distribution](https://keras.io/api/distribution/)
 / Distribution utilities

Distribution utilities
======================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L921)

### `set_distribution` function

Copied!

`keras.distribution.set_distribution(value)`

Set the distribution as the global distribution setting.

**Arguments**

*   **value**: a `Distribution` instance.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L915)

### `distribution` function

Copied!

`keras.distribution.distribution()`

Retrieve the current distribution from global context.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L21)

### `list_devices` function

Copied!

`keras.distribution.list_devices(device_type=None)`

Return all the available devices based on the device type.

Note: in a distributed setting, global devices are returned.

When `device_type` is not provided, devices of the default type are returned. This function nevers return a mix of device types, for instance GPUs and CPUs.

**Arguments**

*   **device\_type**: string, one of `"cpu"`, `"gpu"` or `"tpu"`. Defaults to `"gpu"` or `"tpu"` if available when `device_type` is not provided. Otherwise returns the `"cpu"` devices.

Return: List of string, the devices that are available for distributed computation. Each device is formatted as "device\_type:id", for instance "gpu:1" or "cpu:0".

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L64)

### `initialize` function

Copied!

`keras.distribution.initialize(     job_addresses=None, num_processes=None, process_id=None )`

Initialize the distribution system for multi-host/process setting.

Calling `initialize` will prepare the backend for execution on multi-host GPU or TPUs. It should be called before any computations.

Note that the parameters can also be injected via environment variables, which can be better controlled by the launch script at startup time. For certain backend that also rely on the environment variables to configure, Keras will properly forward them.

**Arguments**

*   **job\_addresses**: string. Comma separated IP addresses for all the jobs that will form the whole computation cluster. Note that for JAX backend, only the address for job 0 (coodinator) is needed. For certain runtime like cloud TPU, this value can be `None`, and the backend will figure it out with the TPU environment variables. You can also config this value via environment variable `KERAS_DISTRIBUTION_JOB_ADDRESSES`.
*   **num\_processes**: int. The number of worker/processes that will form the whole computation cluster. For certain runtime like cloud TPU, this value can be `None`, and the backend will figure it out with the TPU environment variables. You can also configure this value via environment variable `KERAS_DISTRIBUTION_NUM_PROCESSES`.
*   **process\_id**: int. The ID number of the current worker/process. The value should be ranged from `0` to `num_processes - 1`. `0` will indicate the current worker/process is the master/coordinate job. You can also configure this value via environment variable `KERAS_DISTRIBUTION_PROCESS_ID`.

**Example**

Suppose there are two GPU processes, and process 0 is running at address `10.0.0.1:1234`, and process 1 is running at address `10.0.0.2:2345`. To configure such cluster, you can run

On process 0:

Copied!

`keras.distribute.initialize(     job_addresses="10.0.0.1:1234,10.0.0.2:2345",     num_processes=2,     process_id=0)`

On process 1:

Copied!

`keras.distribute.initialize(     job_addresses="10.0.0.1:1234,10.0.0.2:2345",     num_processes=2,     process_id=1)`

or via the environment variables: On process 0:

Copied!

`os.environ[     "KERAS_DISTRIBUTION_JOB_ADDRESSES"] = "10.0.0.1:1234,10.0.0.2:2345" os.environ["KERAS_DISTRIBUTION_NUM_PROCESSES"] = "2" os.environ["KERAS_DISTRIBUTION_PROCESS_ID"] = "0" keras.distribute.initialize()`

On process 1:

Copied!

`os.environ[     "KERAS_DISTRIBUTION_JOB_ADDRESSES"] = "10.0.0.1:1234,10.0.0.2:2345" os.environ["KERAS_DISTRIBUTION_NUM_PROCESSES"] = "2" os.environ["KERAS_DISTRIBUTION_PROCESS_ID"] = "1" keras.distribute.initialize()`

Also note that for JAX backend, the `job_addresses` can be further reduced to just the master/coordinator address, which is `10.0.0.1:1234`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L45)

### `get_device_count` function

Copied!

`keras.distribution.get_device_count(device_type=None)`

Returns the number of available devices based on the device type.

When `device_type` is not provided, the count of devices of the default type is returned. This function nevers counts a mix of device types, for instance GPUs and CPUs.

**Arguments**

*   **device\_type**: string, one of `"cpu"`, `"gpu"` or `"tpu"`. Defaults to `"gpu"` or `"tpu"` if available when `device_type` is not provided. Otherwise returns the `"cpu"` devices.

**Returns**

*   **int**: The total number of devices for the specified type.

* * *

[Distribution utilities](https://keras.io/api/distribution/distribution_utils/#distribution-utilities)

[`set_distribution` function](https://keras.io/api/distribution/distribution_utils/#setdistribution-function)

[`distribution` function](https://keras.io/api/distribution/distribution_utils/#distribution-function)

[`list_devices` function](https://keras.io/api/distribution/distribution_utils/#listdevices-function)

[`initialize` function](https://keras.io/api/distribution/distribution_utils/#initialize-function)

[`get_device_count` function](https://keras.io/api/distribution/distribution_utils/#getdevicecount-function)