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
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)
 [Experiment management utilities](https://keras.io/api/utils/experiment_management_utils/)
 [Model plotting utilities](https://keras.io/api/utils/model_plotting_utils/)
 [Structured data preprocessing utilities](https://keras.io/api/utils/feature_space/)
 [Tensor utilities](https://keras.io/api/utils/tensor_utils/)
 [Bounding boxes](https://keras.io/api/utils/bounding_boxes/)
 [Python & NumPy utilities](https://keras.io/api/utils/python_utils/)
 [Bounding boxes utilities](https://keras.io/api/utils/bounding_boxes_utils/)
 [Visualization utilities](https://keras.io/api/utils/visualization_utils/)
 [Preprocessing utilities](https://keras.io/api/utils/preprocessing_utils/)
 [Backend utilities](https://keras.io/api/utils/backend_utils/)
 [Scikit-Learn API wrappers](https://keras.io/api/utils/sklearn_wrappers/)
 [Keras configuration utilities](https://keras.io/api/utils/config_utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Utilities](https://keras.io/api/utils/)
 / Backend utilities

Backend utilities
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/naming.py#L34)

### `get_uid` function

Copied!

`keras.backend.get_uid(prefix="")`

Associates a string prefix with an integer counter.

**Arguments**

*   **prefix**: String prefix to index.

**Returns**

Unique integer ID.

**Example**

Copied!

`>>> get_uid('dense') 1 >>> get_uid('dense') 2`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/dtypes.py#L280)

### `result_type` function

Copied!

`keras.backend.result_type(*dtypes)`

Returns the type from applying the Keras type promotion rules.

In general, each argument is first parsed by `backend.standardize_dtype`, and the resulting dtype is determined by the least upper bound of the type promotion lattice.

Note: This function attempts to match the result of `jnp.result_type`.

**Arguments**

*   **dtypes**: Input dtypes.

**Returns**

The result dtype.

**Examples**

Copied!

`>>> x = keras.ops.ones((1,), dtype="bfloat16") >>> keras.backend.result_type(x.dtype, int) "bfloat16"`

Copied!

`>>> x = keras.ops.ones((1,), dtype="int32") >>> y = keras.ops.ones((1,), dtype="float32") >>> keras.backend.result_type(x.dtype, y.dtype) "float32"`

Copied!

`>>> z= keras.ops.ones((1,), dtype='complex64') >>> keras.backend.result_type(z.dtype, int) "float64"`

* * *

[Backend utilities](https://keras.io/api/utils/backend_utils/#backend-utilities)

[`get_uid` function](https://keras.io/api/utils/backend_utils/#getuid-function)

[`result_type` function](https://keras.io/api/utils/backend_utils/#resulttype-function)