None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)
 [Model plotting utilities](https://keras.io/2/api/utils/model_plotting_utils/)
 [Structured data preprocessing utilities](https://keras.io/2/api/utils/feature_space/)
 [Python & NumPy utilities](https://keras.io/2/api/utils/python_utils/)
 [Backend utilities](https://keras.io/2/api/utils/backend_utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Utilities](https://keras.io/2/api/utils/)
 / Model plotting utilities

Model plotting utilities
========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/vis_utils.py#L381)

### `plot_model` function

Copied!

`tf_keras.utils.plot_model(     model,     to_file="model.png",     show_shapes=False,     show_dtype=False,     show_layer_names=True,     rankdir="TB",     expand_nested=False,     dpi=96,     layer_range=None,     show_layer_activations=False,     show_trainable=False, )`

Converts a TF-Keras model to dot format and save to a file.

**Example**

Copied!

`input = tf.keras.Input(shape=(100,), dtype='int32', name='input') x = tf.keras.layers.Embedding(     output_dim=512, input_dim=10000, input_length=100)(input) x = tf.keras.layers.LSTM(32)(x) x = tf.keras.layers.Dense(64, activation='relu')(x) x = tf.keras.layers.Dense(64, activation='relu')(x) x = tf.keras.layers.Dense(64, activation='relu')(x) output = tf.keras.layers.Dense(1, activation='sigmoid', name='output')(x) model = tf.keras.Model(inputs=[input], outputs=[output]) dot_img_file = '/tmp/model_1.png' tf.keras.utils.plot_model(model, to_file=dot_img_file, show_shapes=True)`

**Arguments**

*   **model**: A TF-Keras model instance
*   **to\_file**: File name of the plot image.
*   **show\_shapes**: whether to display shape information.
*   **show\_dtype**: whether to display layer dtypes.
*   **show\_layer\_names**: whether to display layer names.
*   **rankdir**: `rankdir` argument passed to PyDot, a string specifying the format of the plot: 'TB' creates a vertical plot; 'LR' creates a horizontal plot.
*   **expand\_nested**: Whether to expand nested models into clusters.
*   **dpi**: Dots per inch.
*   **layer\_range**: input of `list` containing two `str` items, which is the starting layer name and ending layer name (both inclusive) indicating the range of layers for which the plot will be generated. It also accepts regex patterns instead of exact name. In such case, start predicate will be the first element it matches to `layer_range[0]` and the end predicate will be the last element it matches to `layer_range[1]`. By default `None` which considers all layers of model. Note that you must pass range such that the resultant subgraph must be complete.
*   **show\_layer\_activations**: Display layer activations (only for layers that have an `activation` property).
*   **show\_trainable**: whether to display if a layer is trainable. Displays 'T' when the layer is trainable and 'NT' when it is not trainable.

**Raises**

*   **ImportError**: if graphviz or pydot are not available.
*   **ValueError**: if `plot_model` is called before the model is built.

**Returns**

A Jupyter notebook Image object if Jupyter is installed. This enables in-line display of the model plots in notebooks.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/vis_utils.py#L80)

### `model_to_dot` function

Copied!

`tf_keras.utils.model_to_dot(     model,     show_shapes=False,     show_dtype=False,     show_layer_names=True,     rankdir="TB",     expand_nested=False,     dpi=96,     subgraph=False,     layer_range=None,     show_layer_activations=False,     show_trainable=False, )`

Convert a TF-Keras model to dot format.

**Arguments**

*   **model**: A TF-Keras model instance.
*   **show\_shapes**: whether to display shape information.
*   **show\_dtype**: whether to display layer dtypes.
*   **show\_layer\_names**: whether to display layer names.
*   **rankdir**: `rankdir` argument passed to PyDot, a string specifying the format of the plot: 'TB' creates a vertical plot; 'LR' creates a horizontal plot.
*   **expand\_nested**: whether to expand nested models into clusters.
*   **dpi**: Dots per inch.
*   **subgraph**: whether to return a `pydot.Cluster` instance.
*   **layer\_range**: input of `list` containing two `str` items, which is the starting layer name and ending layer name (both inclusive) indicating the range of layers for which the `pydot.Dot` will be generated. It also accepts regex patterns instead of exact name. In such case, start predicate will be the first element it matches to `layer_range[0]` and the end predicate will be the last element it matches to `layer_range[1]`. By default `None` which considers all layers of model. Note that you must pass range such that the resultant subgraph must be complete.
*   **show\_layer\_activations**: Display layer activations (only for layers that have an `activation` property).
*   **show\_trainable**: whether to display if a layer is trainable. Displays 'T' when the layer is trainable and 'NT' when it is not trainable.

**Returns**

A `pydot.Dot` instance representing the TF-Keras model or a `pydot.Cluster` instance representing nested model if `subgraph=True`.

**Raises**

*   **ValueError**: if `model_to_dot` is called before the model is built.
*   **ImportError**: if pydot is not available.

* * *

[Model plotting utilities](https://keras.io/2/api/utils/model_plotting_utils/#model-plotting-utilities)

[`plot_model` function](https://keras.io/2/api/utils/model_plotting_utils/#plotmodel-function)

[`model_to_dot` function](https://keras.io/2/api/utils/model_plotting_utils/#modeltodot-function)