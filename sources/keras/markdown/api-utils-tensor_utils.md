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
 / Tensor utilities

Tensor utilities
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation_utils.py#L466)

### `get_source_inputs` function

Copied!

`keras.utils.get_source_inputs(tensor)`

Returns the list of input tensors necessary to compute `tensor`.

Output will always be a list of tensors (potentially with 1 element).

**Arguments**

*   **tensor**: The tensor to start from.

**Returns**

List of input tensors.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L414)

### `is_keras_tensor` function

Copied!

`keras.utils.is_keras_tensor(x)`

Returns whether `x` is a Keras tensor.

A "Keras tensor" is a _symbolic tensor_, such as a tensor that was created via `Input()`. A "symbolic tensor" can be understood as a placeholder – it does not contain any actual numerical data, only a shape and dtype. It can be used for building Functional models, but it cannot be used in actual computations.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L661)

### `is_float_dtype` function

Copied!

`keras.backend.is_float_dtype(dtype)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L667)

### `is_int_dtype` function

Copied!

`keras.backend.is_int_dtype(dtype)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/variables.py#L570)

### `standardize_dtype` function

Copied!

`keras.backend.standardize_dtype(dtype)`

* * *

[Tensor utilities](https://keras.io/api/utils/tensor_utils/#tensor-utilities)

[`get_source_inputs` function](https://keras.io/api/utils/tensor_utils/#getsourceinputs-function)

[`is_keras_tensor` function](https://keras.io/api/utils/tensor_utils/#iskerastensor-function)

[`is_float_dtype` function](https://keras.io/api/utils/tensor_utils/#isfloatdtype-function)

[`is_int_dtype` function](https://keras.io/api/utils/tensor_utils/#isintdtype-function)

[`standardize_dtype` function](https://keras.io/api/utils/tensor_utils/#standardizedtype-function)