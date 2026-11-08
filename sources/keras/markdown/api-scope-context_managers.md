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
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Scope classes](https://keras.io/api/scope/scope_classes/)
 [Context Managers](https://keras.io/api/scope/context_managers/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Scope](https://keras.io/api/scope/)
 / Context Managers

Context Managers
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend.py#L75)

### `device` function

Copied!

`keras.device(device_name)`

Context manager for backend-agnostic device placement.

Use this context manager to control on which device operations are performed and tensors are allocated. This works across all backends (TensorFlow, JAX, PyTorch). This is useful for memory management, data preprocessing, and multi-device setups.

**Arguments**

*   **device\_name**: String specifying the device in format `"device_type:device_index"`. For example: `"cpu:0"`, `"gpu:0"`, `"gpu:1"`. For the PyTorch backend, `"gpu"` is automatically converted to `"cuda"`.

**Example**

Basic usage with CPU and GPU:

Copied!

`# Allocate tensors on CPU with keras.device("cpu:0"):     cpu_tensor = keras.ops.ones((2, 2))  # Allocate tensors on GPU (if available) with keras.device("gpu:0"):     gpu_tensor = keras.ops.ones((2, 2))`

Practical example with CPU preprocessing and GPU training:

Copied!

`# Create dummy data and model x_raw = np.random.rand(128, 784) y_train = np.random.randint(0, 10, size=(128,)) model = keras.Sequential([     keras.Input(shape=(784,)),     keras.layers.Dense(10) ]) model.compile(     optimizer="adam",     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True) )  # Preprocess data on CPU with keras.device("cpu:0"):     x_processed = keras.ops.cast(x_raw, "float32")  # Train on GPU (if available) with keras.device("gpu:0"):     model.fit(x_processed, y_train, epochs=2)`

Use cases:

*   **Memory management**: Keep large tensors on CPU to save GPU memory
*   **Data preprocessing**: Process data on CPU before training on GPU
*   **GPU / TPU setups**: Control what runs on GPU / TPU vs CPU
*   **Multi-device setups**: Control which device receives which tensors

Device naming conventions:

*   `"cpu:0"` - First CPU
*   `"gpu:0"` - First GPU (works across all backends)
*   `"gpu:1"` - Second GPU

Note: For distributed training across multiple devices, see the [distributed training guides](https://keras.io/guides/distributed_training/)
.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend.py#L70)

### `name_scope` class

Copied!

`keras.name_scope(name, **kwargs)`

Creates a sub-namespace for variable paths.

**Arguments**

*   **name**: Name of the current scope (string).
*   **caller**: Optional ID of a caller object (e.g. class instance).
*   **deduplicate**: If `True`, if `caller` was passed, and the previous caller matches the current caller, and the previous name matches the current name, do not reenter a new namespace.
*   **override\_parent**: Can be used to provide an absolute path which would override any previously opened name scopes.

* * *

[Context Managers](https://keras.io/api/scope/context_managers/#context-managers)

[`device` function](https://keras.io/api/scope/context_managers/#device-function)

[`name_scope` class](https://keras.io/api/scope/context_managers/#namescope-class)