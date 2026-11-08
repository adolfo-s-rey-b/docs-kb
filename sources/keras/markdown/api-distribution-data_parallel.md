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
 / DataParallel API

DataParallel API
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L532)

### `DataParallel` class

Copied!

`keras.distribution.DataParallel(     device_mesh=None, devices=None, auto_shard_dataset=True )`

Distribution for data parallelism.

You can choose to create this instance by either specifying the `device_mesh` or `devices` arguments (but not both).

The `device_mesh` argument is expected to be a `DeviceMesh` instance, and is expected to be 1D only. In case that the mesh has multiple axes, then the first axis will be treated as the data parallel dimension (and a warning will be raised).

When a list of `devices` are provided, they will be used to construct a 1D mesh.

When both `mesh` and `devices` are absent, then `list_devices()` will be used to detect any available devices and create a 1D mesh from them.

**Arguments**

*   **device\_mesh**: Optional `DeviceMesh` instance.
*   **devices**: Optional list of devices.
*   **auto\_shard\_dataset**: Automatically shard the dataset amongst processes in a multi-process setting. Set to `False` if the dataset is already sharded across hosts. Defaults to `True`.

* * *

[DataParallel API](https://keras.io/api/distribution/data_parallel/#dataparallel-api)

[`DataParallel` class](https://keras.io/api/distribution/data_parallel/#dataparallel-class)