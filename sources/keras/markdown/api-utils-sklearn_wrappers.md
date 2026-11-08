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
 / Scikit-Learn API wrappers

Scikit-Learn API wrappers
=========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/wrappers/sklearn_wrapper.py#L195)

### `SKLearnClassifier` class

Copied!

`keras.wrappers.SKLearnClassifier(     model, warm_start=False, model_kwargs=None, fit_kwargs=None )`

scikit-learn compatible classifier wrapper for Keras models.

Note that there are sources of randomness in model initialization and training. Refer to [Reproducibility in Keras Models](https://keras.io/examples/keras_recipes/reproducibility_recipes/)
 on how to control randomness.

**Arguments**

*   **model**: `Model`. An instance of `Model`, or a callable returning such an object. Note that if input is a `Model`, it will be cloned using [`keras.models.clone_model`](https://keras.io/api/models/model_saving_apis/model_config_serialization#clonemodel-function)
     before being fitted, unless `warm_start=True`. The `Model` instance needs to be passed as already compiled. If callable, it must accept at least `X` and `y` as keyword arguments. Other arguments must be accepted if passed as `model_kwargs` by the user.
*   **warm\_start**: bool, defaults to `False`. Whether to reuse the model weights from the previous fit. If `True`, the given model won't be cloned and the weights from the previous fit will be reused.
*   **model\_kwargs**: dict, defaults to `None`. Keyword arguments passed to `model`, if `model` is callable.
*   **fit\_kwargs**: dict, defaults to `None`. Keyword arguments passed to `model.fit`. These can also be passed directly to the `fit` method of the scikit-learn wrapper. The values passed directly to the `fit` method take precedence over these.

**Attributes**

*   \__model_ \_\_: `Model` The fitted model.
*   \__history_ \_\_: dict The history of the fit, returned by `model.fit`.
*   \__classes_ \_\_: array-like, shape=(n\_classes,) The classes labels.

**Example**

Here we use a function which creates a basic MLP model dynamically choosing the input and output shapes. We will use this to create our scikit-learn model.

Copied!

`from keras.layers import Dense, Input from keras.models import Model  def dynamic_model(X, y, loss, layers=[10]):     # Creates a basic MLP model dynamically choosing the input and     # output shapes.     n_features_in = X.shape[1]     inp = Input(shape=(n_features_in,))      hidden = inp     for layer_size in layers:         hidden = Dense(layer_size, activation="relu")(hidden)      n_outputs = y.shape[1] if len(y.shape) > 1 else 1     out = Dense(n_outputs, activation="softmax")(hidden)     model = Model(inp, out)     model.compile(loss=loss, optimizer="rmsprop")      return model`

You can then use this function to create a scikit-learn compatible model and fit it on some data.

Copied!

`from sklearn.datasets import make_classification from keras.wrappers import SKLearnClassifier  X, y = make_classification(n_samples=1000, n_features=10) est = SKLearnClassifier(     model=dynamic_model,     model_kwargs={         "loss": "categorical_crossentropy",         "layers": [20, 20, 20],     }, )  est.fit(X, y, epochs=5)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/wrappers/sklearn_wrapper.py#L320)

### `SKLearnRegressor` class

Copied!

`keras.wrappers.SKLearnRegressor(     model, warm_start=False, model_kwargs=None, fit_kwargs=None )`

scikit-learn compatible regressor wrapper for Keras models.

Note that there are sources of randomness in model initialization and training. Refer to [Reproducibility in Keras Models](https://keras.io/examples/keras_recipes/reproducibility_recipes/)
 on how to control randomness.

**Arguments**

*   **model**: `Model`. An instance of `Model`, or a callable returning such an object. Note that if input is a `Model`, it will be cloned using [`keras.models.clone_model`](https://keras.io/api/models/model_saving_apis/model_config_serialization#clonemodel-function)
     before being fitted, unless `warm_start=True`. The `Model` instance needs to be passed as already compiled. If callable, it must accept at least `X` and `y` as keyword arguments. Other arguments must be accepted if passed as `model_kwargs` by the user.
*   **warm\_start**: bool, defaults to `False`. Whether to reuse the model weights from the previous fit. If `True`, the given model won't be cloned and the weights from the previous fit will be reused.
*   **model\_kwargs**: dict, defaults to `None`. Keyword arguments passed to `model`, if `model` is callable.
*   **fit\_kwargs**: dict, defaults to `None`. Keyword arguments passed to `model.fit`. These can also be passed directly to the `fit` method of the scikit-learn wrapper. The values passed directly to the `fit` method take precedence over these.

**Attributes**

*   \__model_ \_\_: `Model` The fitted model.

**Example**

Here we use a function which creates a basic MLP model dynamically choosing the input and output shapes. We will use this to create our scikit-learn model.

Copied!

`from keras.layers import Dense, Input from keras.models import Model  def dynamic_model(X, y, loss, layers=[10]):     # Creates a basic MLP model dynamically choosing the input and     # output shapes.     n_features_in = X.shape[1]     inp = Input(shape=(n_features_in,))      hidden = inp     for layer_size in layers:         hidden = Dense(layer_size, activation="relu")(hidden)      n_outputs = y.shape[1] if len(y.shape) > 1 else 1     out = Dense(n_outputs)(hidden)     model = Model(inp, out)     model.compile(loss=loss, optimizer="rmsprop")      return model`

You can then use this function to create a scikit-learn compatible model and fit it on some data.

Copied!

`from sklearn.datasets import make_regression from keras.wrappers import SKLearnRegressor  X, y = make_regression(n_samples=1000, n_features=10) est = SKLearnRegressor(     model=dynamic_model,     model_kwargs={         "loss": "mse",         "layers": [20, 20, 20],     }, )  est.fit(X, y, epochs=5)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/wrappers/sklearn_wrapper.py#L412)

### `SKLearnTransformer` class

Copied!

`keras.wrappers.SKLearnTransformer(     model, warm_start=False, model_kwargs=None, fit_kwargs=None )`

scikit-learn compatible transformer wrapper for Keras models.

Note that this is a scikit-learn compatible transformer, and not a transformer in the deep learning sense.

Also note that there are sources of randomness in model initialization and training. Refer to [Reproducibility in Keras Models](https://keras.io/examples/keras_recipes/reproducibility_recipes/)
 on how to control randomness.

**Arguments**

*   **model**: `Model`. An instance of `Model`, or a callable returning such an object. Note that if input is a `Model`, it will be cloned using [`keras.models.clone_model`](https://keras.io/api/models/model_saving_apis/model_config_serialization#clonemodel-function)
     before being fitted, unless `warm_start=True`. The `Model` instance needs to be passed as already compiled. If callable, it must accept at least `X` and `y` as keyword arguments. Other arguments must be accepted if passed as `model_kwargs` by the user.
*   **warm\_start**: bool, defaults to `False`. Whether to reuse the model weights from the previous fit. If `True`, the given model won't be cloned and the weights from the previous fit will be reused.
*   **model\_kwargs**: dict, defaults to `None`. Keyword arguments passed to `model`, if `model` is callable.
*   **fit\_kwargs**: dict, defaults to `None`. Keyword arguments passed to `model.fit`. These can also be passed directly to the `fit` method of the scikit-learn wrapper. The values passed directly to the `fit` method take precedence over these.

**Attributes**

*   \__model_ \_\_: `Model` The fitted model.
*   \__history_ \_\_: dict The history of the fit, returned by `model.fit`.

**Example**

A common use case for a scikit-learn transformer, is to have a step which gives you the embedding of your data. Here we assume `my_package.my_model` is a Keras model which takes the input and gives embeddings of the data, and `my_package.my_data` is your dataset loader.

Copied!

`from my_package import my_model, my_data from keras.wrappers import SKLearnTransformer from sklearn.frozen import FrozenEstimator # requires scikit-learn>=1.6 from sklearn.pipeline import make_pipeline from sklearn.ensemble import HistGradientBoostingClassifier  X, y = my_data()  trs = FrozenEstimator(SKLearnTransformer(model=my_model)) pipe = make_pipeline(trs, HistGradientBoostingClassifier()) pipe.fit(X, y)`

Note that in the above example, `FrozenEstimator` prevents any further training of the transformer step in the pipeline, which can be the case if you don't want to change the embedding model at hand.

* * *

[Scikit-Learn API wrappers](https://keras.io/api/utils/sklearn_wrappers/#scikitlearn-api-wrappers)

[`SKLearnClassifier` class](https://keras.io/api/utils/sklearn_wrappers/#sklearnclassifier-class)

[`SKLearnRegressor` class](https://keras.io/api/utils/sklearn_wrappers/#sklearnregressor-class)

[`SKLearnTransformer` class](https://keras.io/api/utils/sklearn_wrappers/#sklearntransformer-class)