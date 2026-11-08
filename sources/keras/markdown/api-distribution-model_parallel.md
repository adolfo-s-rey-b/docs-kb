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
 / ModelParallel API

ModelParallel API
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L628)

### `ModelParallel` class

Copied!

`keras.distribution.ModelParallel(     layout_map=None, batch_dim_name=None, auto_shard_dataset=True, **kwargs )`

Distribution that shards model variables.

Compare to `DataParallel` which replicates the variables across all devices, `ModelParallel` allows you to shard variables in addition to the input data.

To construct a `ModelParallel` distribution, you need to provide a `DeviceMesh` and a `LayoutMap`.

1.  `DeviceMesh` contains physical device information. The axis names in the mesh will be used to map the variable and data layout.
2.  `LayoutMap` contains the mapping between variable paths to their corresponding `TensorLayout`.

**Example**

Copied!

``devices = list_devices()    # Assume there are 8 devices.  # Create a mesh with 2 devices for data parallelism and 4 devices for # model parallelism. device_mesh = DeviceMesh(shape=(2, 4), axis_names=('batch', 'model'),                          devices=devices) # Create a layout map that shard the `Dense` layer and `Conv2D` # layer variables on the last dimension. # Based on the `device_mesh`, this means the variables # will be split across 4 devices. Any other variable that doesn't # match any key in the layout map will be fully replicated. layout_map = LayoutMap(device_mesh) layout_map['.*dense.*kernel'] = (None, 'model') layout_map['.*dense.*bias'] = ('model',) layout_map['.*conv2d.*kernel'] = (None, None, None, 'model') layout_map['.*conv2d.*bias'] = ('model',)  distribution = ModelParallel(     layout_map=layout_map,     batch_dim_name='batch', )  # Set the global distribution, or via `with distribution.scope():` set_distribution(distribution)  model = model_creation() model.compile() model.fit(data)``

You can quickly update the device mesh shape to change the sharding factor of the variables. E.g.

Copied!

`# With only the shape change for the device mesh, the variables will be # sharded across 8 devices instead of 4, which further reduces the memory # footprint of variables on each of the device. device_mesh = DeviceMesh(     shape=(1, 8),     axis_names=('batch', 'model'),     devices=devices, )`

To figure out a proper layout mapping rule for all the model variables, you can first list out all the model variable paths, which will be used as the key to map the variables to `TensorLayout`.

e.g.

Copied!

`model = create_model() for v in model.variables:     print(v.path)`

**Arguments**

*   **layout\_map**: `LayoutMap` instance which map the variable path to the corresponding tensor layout.
*   **batch\_dim\_name**: Optional string, the axis name in the device mesh (of the `layout_map` object) that will be used to distribute data. If unspecified, the first axis from the device mesh will be used.
*   **auto\_shard\_dataset**: Automatically shard the dataset amongst processes in a multi-process setting. Set to `False` if the dataset is already sharded across hosts. Defaults to `True`.

* * *

[ModelParallel API](https://keras.io/api/distribution/model_parallel/#modelparallel-api)

[`ModelParallel` class](https://keras.io/api/distribution/model_parallel/#modelparallel-class)