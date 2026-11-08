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
 / Experiment management utilities

Experiment management utilities
===============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L12)

### `Config` class

Copied!

`keras.utils.Config(**kwargs)`

A Config is a dict-like container for named values.

It offers a few advantages over a plain dict:

*   Setting and retrieving values via attribute setting / getting.
*   Ability to freeze the config to ensure no accidental config modifications occur past a certain point in your program.
*   Easy serialization of the whole config as JSON.

**Examples**

Copied!

`# Create a config via constructor arguments config = Config("learning_rate"=0.1, "momentum"=0.9)  # Then keep adding to it via attribute-style setting config.use_ema = True config.ema_overwrite_frequency = 100  # You can also add attributes via dict-like access config["seed"] = 123  # You can retrieve entries both via attribute-style # access and dict-style access assert config.seed == 100 assert config["learning_rate"] == 0.1`

A config behaves like a dict:

Copied!

`config = Config("learning_rate"=0.1, "momentum"=0.9) for k, v in config.items():     print(f"{k}={v}")  print(f"keys: {list(config.keys())}") print(f"values: {list(config.values())}")`

In fact, it can be turned into one:

Copied!

`config = Config("learning_rate"=0.1, "momentum"=0.9) dict_config = config.as_dict()`

You can easily serialize a config to JSON:

Copied!

`config = Config("learning_rate"=0.1, "momentum"=0.9)  json_str = config.to_json()`

You can also freeze a config to prevent further changes:

Copied!

`config = Config() config.optimizer = "adam" config.seed = 123  # Freeze the config to prevent changes. config.freeze() assert config.frozen  config.foo = "bar"  # This will raise an error.`

* * *

[Experiment management utilities](https://keras.io/api/utils/experiment_management_utils/#experiment-management-utilities)

[`Config` class](https://keras.io/api/utils/experiment_management_utils/#config-class)