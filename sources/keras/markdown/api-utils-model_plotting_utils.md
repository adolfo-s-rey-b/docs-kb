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
 / Model plotting utilities

Model plotting utilities
========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/model_visualization.py#L409)

### `plot_model` function

Copied!

`keras.utils.plot_model(     model,     to_file="model.png",     show_shapes=False,     show_dtype=False,     show_layer_names=False,     rankdir="TB",     expand_nested=False,     dpi=200,     show_layer_activations=False,     show_trainable=False,     splines="ortho",     **kwargs )`

Converts a Keras model to dot format and save to a file.

**Example**

Copied!

`inputs = ... outputs = ... model = keras.Model(inputs=inputs, outputs=outputs)  dot_img_file = '/tmp/model_1.png' keras.utils.plot_model(model, to_file=dot_img_file, show_shapes=True)`

**Arguments**

*   **model**: A Keras model instance
*   **to\_file**: File name of the plot image.
*   **show\_shapes**: whether to display shape information.
*   **show\_dtype**: whether to display layer dtypes.
*   **show\_layer\_names**: whether to display layer names.
*   **rankdir**: `rankdir` argument passed to PyDot, a string specifying the format of the plot: `"TB"` creates a vertical plot; `"LR"` creates a horizontal plot.
*   **expand\_nested**: whether to expand nested Functional models into clusters.
*   **dpi**: Image resolution in dots per inch.
*   **show\_layer\_activations**: Display layer activations (only for layers that have an `activation` property).
*   **show\_trainable**: whether to display if a layer is trainable.
*   **splines**: Controls how edges are drawn. Defaults to `"ortho"` (right-angle lines). Other options include `"curved"`, `"polyline"`, `"spline"`, and `"line"`.

**Returns**

A Jupyter notebook Image object if Jupyter is installed. This enables in-line display of the model plots in notebooks.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/model_visualization.py#L194)

### `model_to_dot` function

Copied!

`keras.utils.model_to_dot(     model,     show_shapes=False,     show_dtype=False,     show_layer_names=True,     rankdir="TB",     expand_nested=False,     dpi=200,     subgraph=False,     show_layer_activations=False,     show_trainable=False,     splines="ortho",     **kwargs )`

Convert a Keras model to dot format.

**Arguments**

*   **model**: A Keras model instance.
*   **show\_shapes**: whether to display shape information.
*   **show\_dtype**: whether to display layer dtypes.
*   **show\_layer\_names**: whether to display layer names.
*   **rankdir**: `rankdir` argument passed to PyDot, a string specifying the format of the plot: `"TB"` creates a vertical plot; `"LR"` creates a horizontal plot.
*   **expand\_nested**: whether to expand nested Functional models into clusters.
*   **dpi**: Image resolution in dots per inch.
*   **subgraph**: whether to return a `pydot.Cluster` instance.
*   **show\_layer\_activations**: Display layer activations (only for layers that have an `activation` property).
*   **show\_trainable**: whether to display if a layer is trainable.
*   **splines**: Controls how edges are drawn. Defaults to `"ortho"` (right-angle lines). Other options include `"curved"`, `"polyline"`, `"spline"`, and `"line"`.

**Returns**

A `pydot.Dot` instance representing the Keras model or a `pydot.Cluster` instance representing nested model if `subgraph=True`.

* * *

[Model plotting utilities](https://keras.io/api/utils/model_plotting_utils/#model-plotting-utilities)

[`plot_model` function](https://keras.io/api/utils/model_plotting_utils/#plotmodel-function)

[`model_to_dot` function](https://keras.io/api/utils/model_plotting_utils/#modeltodot-function)