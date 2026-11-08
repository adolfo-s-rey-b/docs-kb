[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#used-in-the-notebooks_1)
    
*   [With the "Functional API"](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#with_the_functional_api_2)
    
*   [By subclassing the Model class](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#by_subclassing_the_model_class_2)
    
*   [With the Sequential class](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#with_the_sequential_class_2)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#methods_2)
    *   [compile](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compile)
        
    *   [compile\_from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compile_from_config)
        
    *   [compiled\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compiled_loss)
        
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compute_loss)
        
    *   [compute\_metrics](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compute_metrics)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#evaluate)
        
    *   [export](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#export)
        
    *   [fit](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#fit)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#from_config)
        
    *   [get\_compile\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_compile_config)
        
    *   [get\_layer](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_layer)
        
    *   [get\_metrics\_result](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_metrics_result)
        
    *   [get\_quantization\_layer\_structure](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_quantization_layer_structure)
        
    *   [get\_state\_tree](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_state_tree)
        
    *   [load\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#load_weights)
        
    *   [loss](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#loss)
        
    *   [make\_predict\_function](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#make_predict_function)
        
    *   [make\_test\_function](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#make_test_function)
        
    *   [make\_train\_function](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#make_train_function)
        
    *   [predict](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#predict)
        
    *   [predict\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#predict_on_batch)
        
    *   [predict\_step](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#predict_step)
        
    *   [reset\_metrics](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#reset_metrics)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#save)
        
    *   [save\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#save_weights)
        
    *   [set\_state\_tree](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#set_state_tree)
        
    *   [stateless\_compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#stateless_compute_loss)
        
    *   [summary](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#summary)
        
    *   [test\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#test_on_batch)
        
    *   [test\_step](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#test_step)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#to_json)
        
    *   [train\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#train_on_batch)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#train_step)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Model Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#used-in-the-notebooks_1)
    
*   [With the "Functional API"](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#with_the_functional_api_2)
    
*   [By subclassing the Model class](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#by_subclassing_the_model_class_2)
    
*   [With the Sequential class](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#with_the_sequential_class_2)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#methods_2)
    *   [compile](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compile)
        
    *   [compile\_from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compile_from_config)
        
    *   [compiled\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compiled_loss)
        
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compute_loss)
        
    *   [compute\_metrics](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#compute_metrics)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#evaluate)
        
    *   [export](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#export)
        
    *   [fit](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#fit)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#from_config)
        
    *   [get\_compile\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_compile_config)
        
    *   [get\_layer](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_layer)
        
    *   [get\_metrics\_result](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_metrics_result)
        
    *   [get\_quantization\_layer\_structure](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_quantization_layer_structure)
        
    *   [get\_state\_tree](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#get_state_tree)
        
    *   [load\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#load_weights)
        
    *   [loss](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#loss)
        
    *   [make\_predict\_function](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#make_predict_function)
        
    *   [make\_test\_function](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#make_test_function)
        
    *   [make\_train\_function](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#make_train_function)
        
    *   [predict](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#predict)
        
    *   [predict\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#predict_on_batch)
        
    *   [predict\_step](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#predict_step)
        
    *   [reset\_metrics](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#reset_metrics)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#save)
        
    *   [save\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#save_weights)
        
    *   [set\_state\_tree](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#set_state_tree)
        
    *   [stateless\_compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#stateless_compute_loss)
        
    *   [summary](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#summary)
        
    *   [test\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#test_on_batch)
        
    *   [test\_step](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#test_step)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#to_json)
        
    *   [train\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#train_on_batch)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tf/keras/Model?version=stable#train_step)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L38-L1095)

A model grouping layers into an object with training/inference features.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.models.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)

tf.keras.Model(
        *args, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping)<br>    <br>*   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging)<br>    <br>*   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)<br>    <br>*   [Basic training loops](https://www.tensorflow.org/guide/basic_training_loops) | *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Load a pandas DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression) |

There are three ways to instantiate a `Model`:

With the "Functional API"
-------------------------

You start from `Input`, you chain layer calls to specify the model's forward pass, and finally, you create your model from inputs and outputs:

inputs = keras.Input(shape=(37,))
    x = keras.layers.Dense(32, activation="relu")(inputs)
    outputs = keras.layers.Dense(5, activation="softmax")(x)
    model = keras.Model(inputs=inputs, outputs=outputs)

A new Functional API model can also be created by using the intermediate tensors. This enables you to quickly extract sub-components of the model.

#### Example:

inputs = keras.Input(shape=(None, None, 3))
    processed = keras.layers.RandomCrop(width=128, height=128)(inputs)
    conv = keras.layers.Conv2D(filters=32, kernel_size=3)(processed)
    pooling = keras.layers.GlobalAveragePooling2D()(conv)
    feature = keras.layers.Dense(10)(pooling)
    
    full_model = keras.Model(inputs, feature)
    backbone = keras.Model(processed, conv)
    activations = keras.Model(conv, feature)

Note that the `backbone` and `activations` models are not created with [`keras.Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)
 objects, but with the tensors that originate from [`keras.Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)
 objects. Under the hood, the layers and weights will be shared across these models, so that user can train the `full_model`, and use `backbone` or `activations` to do feature extraction. The inputs and outputs of the model can be nested structures of tensors as well, and the created models are standard Functional API models that support all the existing APIs.

By subclassing the `Model` class
--------------------------------

In that case, you should define your layers in `__init__()` and you should implement the model's forward pass in `call()`.

class MyModel(keras.Model):
        def __init__(self):
            super().__init__()
            self.dense1 = keras.layers.Dense(32, activation="relu")
            self.dense2 = keras.layers.Dense(5, activation="softmax")
    
        def call(self, inputs):
            x = self.dense1(inputs)
            return self.dense2(x)
    
    model = MyModel()

If you subclass `Model`, you can optionally have a `training` argument (boolean) in `call()`, which you can use to specify a different behavior in training and inference:

class MyModel(keras.Model):
        def __init__(self):
            super().__init__()
            self.dense1 = keras.layers.Dense(32, activation="relu")
            self.dense2 = keras.layers.Dense(5, activation="softmax")
            self.dropout = keras.layers.Dropout(0.5)
    
        def call(self, inputs, training=False):
            x = self.dense1(inputs)
            x = self.dropout(x, training=training)
            return self.dense2(x)
    
    model = MyModel()

Once the model is created, you can config the model with losses and metrics with `model.compile()`, train the model with `model.fit()`, or use the model to do prediction with `model.predict()`.

With the `Sequential` class
---------------------------

In addition, [`keras.Sequential`](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential)
 is a special case of model where the model is purely a stack of single-input, single-output layers.

model = keras.Sequential([\
        keras.Input(shape=(None, None, 3)),\
        keras.layers.Conv2D(filters=32, kernel_size=3),\
    ])

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `compiled_metrics` |     |
| `distribute_reduction_method` |     |
| `distribute_strategy` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `jit_compile` |     |
| `layers` |     |
| `metrics_names` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `run_eagerly` |     |

Methods
-------

### `compile`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L38-L236)

compile(
        optimizer='rmsprop',
        loss=None,
        loss_weights=None,
        metrics=None,
        weighted_metrics=None,
        run_eagerly=False,
        steps_per_execution=1,
        jit_compile='auto',
        auto_scale_loss=True
    )

Configures the model for training.

#### Example:

model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=1e-3),
        loss=keras.losses.BinaryCrossentropy(),
        metrics=[\
            keras.metrics.BinaryAccuracy(),\
            keras.metrics.FalseNegatives(),\
        ],
    )

|     |     |
| --- | --- |
| Args |     |
| `optimizer` | String (name of optimizer) or optimizer instance. See [`keras.optimizers`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers)<br>. |
| `loss` | Loss function. May be a string (name of loss function), or a [`keras.losses.Loss`](https://www.tensorflow.org/api_docs/python/tf/keras/Loss)<br> instance. See [`keras.losses`](https://www.tensorflow.org/api_docs/python/tf/keras/losses)<br>. A loss function is any callable with the signature `loss = fn(y_true, y_pred)`, where `y_true` are the ground truth values, and `y_pred` are the model's predictions. `y_true` should have shape `(batch_size, d0, .. dN)` (except in the case of sparse loss functions such as sparse categorical crossentropy which expects integer arrays of shape `(batch_size, d0, .. dN-1)`). `y_pred` should have shape `(batch_size, d0, .. dN)`. The loss function should return a float tensor. |
| `loss_weights` | Optional list or dictionary specifying scalar coefficients (Python floats) to weight the loss contributions of different model outputs. The loss value that will be minimized by the model will then be the _weighted sum_ of all individual losses, weighted by the `loss_weights` coefficients. If a list, it is expected to have a 1:1 mapping to the model's outputs. If a dict, it is expected to map output names (strings) to scalar coefficients. |
| `metrics` | List of metrics to be evaluated by the model during training and testing. Each of this can be a string (name of a built-in function), function or a [`keras.metrics.Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)<br> instance. See [`keras.metrics`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics)<br>. Typically you will use `metrics=['accuracy']`. A function is any callable with the signature `result = fn(y_true, _pred)`. To specify different metrics for different outputs of a multi-output model, you could also pass a dictionary, such as `metrics={'a':'accuracy', 'b':['accuracy', 'mse']}`. You can also pass a list to specify a metric or a list of metrics for each output, such as `metrics=[['accuracy'], ['accuracy', 'mse']]` or `metrics=['accuracy', ['accuracy', 'mse']]`. When you pass the strings 'accuracy' or 'acc', we convert this to one of [`keras.metrics.BinaryAccuracy`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy)<br>, [`keras.metrics.CategoricalAccuracy`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/CategoricalAccuracy)<br>, [`keras.metrics.SparseCategoricalAccuracy`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalAccuracy)<br> based on the shapes of the targets and of the model output. A similar conversion is done for the strings `"crossentropy"` and `"ce"` as well. The metrics passed here are evaluated without sample weighting; if you would like sample weighting to apply, you can specify your metrics via the `weighted_metrics` argument instead. |
| `weighted_metrics` | List of metrics to be evaluated and weighted by `sample_weight` or `class_weight` during training and testing. |
| `run_eagerly` | Bool. If `True`, this model's forward pass will never be compiled. It is recommended to leave this as `False` when training (for best performance), and to set it to `True` when debugging. |
| `steps_per_execution` | Int. The number of batches to run during each a single compiled function call. Running multiple batches inside a single compiled function call can greatly improve performance on TPUs or small models with a large Python overhead. At most, one full epoch will be run each execution. If a number larger than the size of the epoch is passed, the execution will be truncated to the size of the epoch. Note that if `steps_per_execution` is set to `N`, [`Callback.on_batch_begin`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback#on_batch_begin)<br> and [`Callback.on_batch_end`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback#on_batch_end)<br> methods will only be called every `N` batches (i.e. before/after each compiled function execution). Not supported with the PyTorch backend. |
| `jit_compile` | Bool or `"auto"`. Whether to use XLA compilation when compiling a model. For `jax` and `tensorflow` backends, `jit_compile="auto"` enables XLA compilation if the model supports it, and disabled otherwise. For `torch` backend, `"auto"` will default to eager execution and `jit_compile=True` will run with `torch.compile` with the `"inductor"` backend. On the JAX backend, compilation happens on the first step and can take several seconds. JAX can persist the compiled result to disk and reuse it across runs and processes, so the same model only pays that cost once. Enable it before the first step with:<br><br>import jax<br>    jax.config.update("jax_compilation_cache_dir", "/path/to/cache")<br><br>See the JAX persistent compilation cache docs for the available thresholds. |
| `auto_scale_loss` | Bool. If `True` and the model dtype policy is `"mixed_float16"`, the passed optimizer will be automatically wrapped in a `LossScaleOptimizer`, which will dynamically scale the loss to prevent underflow. |

|     |
| --- |
| Note |     |
| Trainable variables are determined at `compile()` time. If you modify the `trainable` property of a layer after calling `compile()`, those changes will not take effect during `fit()` unless `compile()` is called again.<br><br>Recommended workflow when changing trainable variables:<br><br># Initial training with some layers<br>    model.compile(optimizer="adam", loss="mse")<br>    model.fit(x_train, y_train)<br>    <br>    # Change trainable flags<br>    layer.trainable = False  # or True<br>    <br>    # Recompile for the change to take effect<br>    model.compile(optimizer="adam", loss="mse")<br>    model.fit(x_train, y_train)<br><br>This behavior applies to all Keras backends and is also documented in the transfer learning guide. |     |

### `compile_from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L994-L1020)

compile_from_config(
        config
    )

Compiles the model with the information given in config.

This method uses the information in the config (optimizer, loss, metrics, etc.) to compile the model.

|     |     |
| --- | --- |
| Args |     |
| `config` | Dict containing information for compiling the model. |

### `compiled_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L693-L702)

compiled_loss(
        y, y_pred, sample_weight=None, regularization_losses=None
    )

### `compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L325-L402)

compute_loss(
        x=None, y=None, y_pred=None, sample_weight=None, training=True
    )

Compute the total loss, validate it, and return it.

Subclasses can optionally override this method to provide custom loss computation logic.

#### Example:

class MyModel(Model):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.loss_tracker = metrics.Mean(name='loss')
    
        def compute_loss(self, x, y, y_pred, sample_weight, training=True):
            loss = ops.mean((y_pred - y) ** 2)
            loss += ops.sum(self.losses)
            self.loss_tracker.update_state(loss)
            return loss
    
        def reset_metrics(self):
            self.loss_tracker.reset_state()
    
        @property
        def metrics(self):
            return [self.loss_tracker]
    
    inputs = layers.Input(shape=(10,), name='my_input')
    outputs = layers.Dense(10)(inputs)
    model = MyModel(inputs, outputs)
    model.add_loss(ops.sum(outputs))
    
    optimizer = SGD()
    model.compile(optimizer, loss='mse', steps_per_execution=10)
    dataset = ...
    model.fit(dataset, epochs=2, steps_per_epoch=10)
    print(f"Custom loss: {model.loss_tracker.result()}")

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. |
| `y` | Target data. |
| `y_pred` | Predictions returned by the model (output of `model(x)`) |
| `sample_weight` | Sample weights for weighting the loss function. |
| `training` | Whether we are training or evaluating the model. |

|     |
| --- |
| Returns |     |
| The total loss as a scalar tensor, or `None` if no loss results (which is the case when called by [`Model.test_step`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#test_step)<br>). |     |

### `compute_metrics`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L483-L527)

compute_metrics(
        x, y, y_pred, sample_weight=None
    )

Update metric states and collect all metrics to be returned.

Subclasses can optionally override this method to provide custom metric updating and collection logic. Custom metrics are not passed in `compile()`, they can be created in `__init__` or `build`. They are automatically tracked and returned by `self.metrics`.

#### Example:

class MyModel(Sequential):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.custom_metric = MyMetric(name="custom_metric")
    
        def compute_metrics(self, x, y, y_pred, sample_weight):
            # This super call updates metrics from `compile` and returns
            # results for all metrics listed in `self.metrics`.
            metric_results = super().compute_metrics(
                x, y, y_pred, sample_weight)
    
            # `metric_results` contains the previous result for
            # `custom_metric`, this is where we update it.
            self.custom_metric.update_state(x, y, y_pred, sample_weight)
            metric_results['custom_metric'] = self.custom_metric.result()
            return metric_results

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. |
| `y` | Target data. |
| `y_pred` | Predictions returned by the model output of `model.call(x)`. |
| `sample_weight` | Sample weights for weighting the loss function. |

|     |     |
| --- | --- |
| Returns |     |
| A `dict` containing values that will be passed to [`keras.callbacks.CallbackList.on_train_batch_end()`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/CallbackList#on_train_batch_end)<br>. Typically, the values of the metrics listed in `self.metrics` are returned. |     |
| `Example` | `{'loss': 0.2, 'accuracy': 0.7}`. |

### `evaluate`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L455-L519)

evaluate(
        x=None,
        y=None,
        batch_size=None,
        verbose='auto',
        sample_weight=None,
        steps=None,
        callbacks=None,
        return_dict=False,
        **kwargs
    )

Returns the loss value & metrics values for the model in test mode.

Computation is done in batches (see the `batch_size` arg.)

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. It can be:<br><br>*   A NumPy array (or array-like), or a list of arrays (in case the model has multiple inputs).<br>*   A backend-native tensor, or a list of tensors (in case the model has multiple inputs).<br>*   A dict mapping input names to the corresponding array/tensors, if the model has named inputs.<br>*   A [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>     returning `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>     yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A `torch.utils.data.DataLoader` yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A Python generator function yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`. |
| `y` | Target data. Like the input data `x`, it can be either NumPy array(s) or backend-native tensor(s). If `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or a Python generator function, `y` should not be specified since targets will be obtained from `x`. |
| `batch_size` | Integer or `None`. Number of samples per batch of computation. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your input data `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function since they generate batches. |
| `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = single line. `"auto"` becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g. in a production environment). Defaults to `"auto"`. |
| `sample_weight` | Optional NumPy array or tensor of weights for the training samples, used for weighting the loss function (during training only). You can either pass a flat (1D) NumPy array or tensor with the same length as the input samples (1:1 mapping between weights and samples), or in the case of temporal data, you can pass a 2D NumPy array or tensor with shape `(samples, sequence_length)` to apply a different weight to every timestep of every sample. This argument is not supported when `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function. Instead, provide `sample_weights` as the third element of `x`. Note that sample weighting does not apply to metrics specified via the `metrics` argument in `compile()`. To apply sample weighting to your metrics, you can specify them via the `weighted_metrics` in `compile()` instead. |
| `steps` | Integer or `None`. Total number of steps (batches of samples) to draw before declaring the evaluation round finished. If `steps` is `None`, it will run until `x` is exhausted. In the case of an infinitely repeating dataset, it will run indefinitely. |
| `callbacks` | List of [`keras.callbacks.Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)<br> instances. List of callbacks to apply during evaluation. |
| `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

|     |
| --- |
| Returns |     |
| Scalar test loss (if the model has a single output and no metrics) or list of scalars (if the model has multiple outputs and/or metrics). |     |

### `export`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L654-L862)

export(
        filepath,
        format='tf_saved_model',
        verbose=None,
        input_signature=None,
        **kwargs
    )

Export the model as an artifact for inference.

|     |     |
| --- | --- |
| Args |     |
| `filepath` | `str` or `pathlib.Path` object. The path to save the artifact. |
| `format` | `str`. The export format. Supported values: `"tf_saved_model"`, `"onnx"`, `"openvino"`, `"litert"`, and `"torch"`. Defaults to `"tf_saved_model"`. |
| `verbose` | `bool`. Whether to print a message during export. Defaults to `None`, which uses the default value set by different backends and formats. |
| `input_signature` | Optional. Specifies the shape and dtype of the model inputs. Can be a structure of [`keras.InputSpec`](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)<br>, [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)<br>, `backend.KerasTensor`, or backend tensor. If not provided, it will be automatically computed. Defaults to `None`. Note: With `format="litert"` and the PyTorch backend, dynamic input shapes are not supported. Any dynamic dimensions (i.e., `None` in input shapes) will be automatically replaced with `1` during export, which may cause runtime failures for other shapes. You must explicitly pass a fixed static `input_signature` matching your maximum runtime shape. |
| `**kwargs` | Additional keyword arguments.<br><br>*   `is_static`: Optional `bool`. Specific to the JAX backend and `format="tf_saved_model"`. Indicates whether `fn` is static. Set to `False` if `fn` involves state updates (e.g., RNG seeds and counters).<br>*   `jax2tf_kwargs`: Optional `dict`. Specific to the JAX backend and `format="tf_saved_model"`. Arguments for `jax2tf.convert`. See the documentation for [`jax2tf.convert`](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md)<br>    . If `native_serialization` and `polymorphic_shapes` are not provided, they will be automatically computed.<br>*   `opset_version`: Optional `int`. Specific to `format="onnx"`. An integer value that specifies the ONNX opset version.<br>*   LiteRT-specific options: Optional keyword arguments specific to `format="litert"`. These are passed directly to the TensorFlow Lite converter on the TensorFlow backend and include options like `optimizations`, `representative_dataset`, `experimental_new_quantizer`, `allow_custom_ops`, `enable_select_tf_ops`, etc. On the PyTorch backend, LiteRT export accepts `optimizations` plus the installed `litert_torch.convert()` keyword arguments such as `strict_export`, `dynamic_shapes` (note that standard ops do not support dynamic shapes, as noted below), `lightweight_conversion`, `enable_x64`, `runtime_constant_folding`, and `quant_config`.<br>*   PyTorch export options: Optional keyword arguments specific to `format="torch"`. These are passed directly to `torch.export.export` and include `strict`, `dynamic_shapes`, `prefer_deferred_runtime_asserts_over_guards`, and `preserve_module_call_signature`. |

**Note on LiteRT (TFLite) Export with PyTorch Backend:** With the PyTorch backend, LiteRT export (`format="litert"`) does not support dynamic input shapes. If no static signature is provided, any dynamic dimensions (represented as `None`) are automatically replaced with `1` during export. This can lead to runtime failures for other shapes. You must explicitly specify a fixed static `input_signature` (matching your maximum runtime dimensions) and pad your inputs to this static shape at runtime.

#### Examples:

Here's how to export a TensorFlow SavedModel for inference.

# Export the model as a TensorFlow SavedModel artifact
    model.export("path/to/location", format="tf_saved_model")
    
    # Load the artifact in a different process/environment
    reloaded_artifact = tf.saved_model.load("path/to/location")
    predictions = reloaded_artifact.serve(input_data)

Here's how to export an ONNX for inference.

# Export the model as a ONNX artifact
    model.export("path/to/location", format="onnx")
    
    # Load the artifact in a different process/environment
    ort_session = onnxruntime.InferenceSession("path/to/location")
    ort_inputs = {
        k.name: v for k, v in zip(ort_session.get_inputs(), input_data)
    }
    predictions = ort_session.run(None, ort_inputs)

Here's how to export a LiteRT (TFLite) for inference.

# Export the model as a LiteRT artifact
    model.export("path/to/location", format="litert")
    
    # Load the artifact in a different process/environment
    interpreter = tf.lite.Interpreter(model_path="path/to/location")
    interpreter.allocate_tensors()
    interpreter.set_tensor(
        interpreter.get_input_details()[0]['index'], input_data
    )
    interpreter.invoke()
    output_data = interpreter.get_tensor(
        interpreter.get_output_details()[0]['index']
    )

Here's how to export a PyTorch ExportedProgram for inference.

# Export the model as a PyTorch ExportedProgram artifact
    model.export("path/to/model.pt2", format="torch")
    
    # Load the artifact in a different process/environment
    import torch
    loaded_program = torch.export.load("path/to/model.pt2")
    predictions = loaded_program.module()(input_tensor)

### `fit`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L314-L453)

fit(
        x=None,
        y=None,
        batch_size=None,
        epochs=1,
        verbose='auto',
        callbacks=None,
        validation_split=0.0,
        validation_data=None,
        shuffle=True,
        class_weight=None,
        sample_weight=None,
        initial_epoch=0,
        steps_per_epoch=None,
        validation_steps=None,
        validation_batch_size=None,
        validation_freq=1
    )

Trains the model for a fixed number of epochs (dataset iterations).

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. It can be:<br><br>*   A NumPy array (or array-like), or a list of arrays (in case the model has multiple inputs).<br>*   A backend-native tensor, or a list of tensors (in case the model has multiple inputs).<br>*   A dict mapping input names to the corresponding array/tensors, if the model has named inputs.<br>*   A [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>     returning `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>     yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A `torch.utils.data.DataLoader` yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A Python generator function yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`. |
| `y` | Target data. Like the input data `x`, it can be either NumPy array(s) or backend-native tensor(s). If `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or a Python generator function, `y` should not be specified since targets will be obtained from `x`. |
| `batch_size` | Integer or `None`. Number of samples per gradient update. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your input data `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function since they generate batches. |
| `epochs` | Integer. Number of epochs to train the model. An epoch is an iteration over the entire `x` and `y` data provided (unless the `steps_per_epoch` flag is set to something other than None). Note that in conjunction with `initial_epoch`, `epochs` is to be understood as "final epoch". The model is not trained for a number of iterations given by `epochs`, but merely until the epoch of index `epochs` is reached. |
| `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = one line per epoch. "auto" becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g., in a production environment). Defaults to `"auto"`. |
| `callbacks` | List of [`keras.callbacks.Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)<br> instances. List of callbacks to apply during training. See [`keras.callbacks`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks)<br>. Note [`keras.callbacks.ProgbarLogger`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ProgbarLogger)<br> and [`keras.callbacks.History`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/History)<br> callbacks are created automatically and need not be passed to `model.fit()`. [`keras.callbacks.ProgbarLogger`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ProgbarLogger)<br> is created or not based on the `verbose` argument in `model.fit()`. |
| `validation_split` | Float between 0 and 1. Fraction of the training data to be used as validation data. The model will set apart this fraction of the training data, will not train on it, and will evaluate the loss and any model metrics on this data at the end of each epoch. The validation data is selected from the last samples in the `x` and `y` data provided, before shuffling. This argument is only supported when `x` and `y` are made of NumPy arrays or tensors. If both `validation_data` and `validation_split` are provided, `validation_data` will override `validation_split`. |
| `validation_data` | Data on which to evaluate the loss and any model metrics at the end of each epoch. The model will not be trained on this data. Thus, note the fact that the validation loss of data provided using `validation_split` or `validation_data` is not affected by regularization layers like noise and dropout. `validation_data` will override `validation_split`. It can be:*   A tuple `(x_val, y_val)` of NumPy arrays or tensors.<br>*   A tuple `(x_val, y_val, val_sample_weights)` of NumPy arrays.<br>*   A [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>    , a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>    , a `torch.utils.data.DataLoader` yielding `(inputs, targets)` or a Python generator function yielding `(x_val, y_val)` or `(inputs, targets, sample_weights)`. |
| `shuffle` | Boolean, whether to shuffle the training data before each epoch. This argument is ignored when `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function. |
| `class_weight` | Optional dictionary mapping class indices (integers) to a weight (float) value, used for weighting the loss function (during training only). This can be useful to tell the model to "pay more attention" to samples from an under-represented class. When `class_weight` is specified and targets have a rank of 2 or greater, either `y` must be one-hot encoded, or an explicit final dimension of `1` must be included for sparse class labels. |
| `sample_weight` | Optional NumPy array or tensor of weights for the training samples, used for weighting the loss function (during training only). You can either pass a flat (1D) NumPy array or tensor with the same length as the input samples (1:1 mapping between weights and samples), or in the case of temporal data, you can pass a 2D NumPy array or tensor with shape `(samples, sequence_length)` to apply a different weight to every timestep of every sample. This argument is not supported when `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function. Instead, provide `sample_weights` as the third element of `x`. Note that sample weighting does not apply to metrics specified via the `metrics` argument in `compile()`. To apply sample weighting to your metrics, you can specify them via the `weighted_metrics` in `compile()` instead. |
| `initial_epoch` | Integer. Epoch at which to start training (useful for resuming a previous training run). |
| `steps_per_epoch` | Integer or `None`. Total number of steps (batches of samples) before declaring one epoch finished and starting the next epoch. When training with input tensors or NumPy arrays, the default `None` means that the value used is the number of samples in your dataset divided by the batch size, or 1 if that cannot be determined. If `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function, the epoch will run until the input dataset is exhausted. When passing an infinitely repeating dataset, you must specify the `steps_per_epoch` argument, otherwise the training will run indefinitely. |
| `validation_steps` | Integer or `None`. Only relevant if `validation_data` is provided. Total number of steps (batches of samples) to draw before stopping when performing validation at the end of every epoch. If `validation_steps` is `None`, validation will run until the `validation_data` dataset is exhausted. In the case of an infinitely repeating dataset, it will run indefinitely. If `validation_steps` is specified and only part of the dataset is consumed, the evaluation will start from the beginning of the dataset at each epoch. This ensures that the same validation samples are used every time. |
| `validation_batch_size` | Integer or `None`. Number of samples per validation batch. If unspecified, will default to `batch_size`. Do not specify the `validation_batch_size` if your data is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function since they generate batches. |
| `validation_freq` | Only relevant if validation data is provided. Specifies how many training epochs to run before a new validation run is performed, e.g. `validation_freq=2` runs validation every 2 epochs. |

Unpacking behavior for iterator-like inputs: A common pattern is to pass an iterator like object such as a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 or a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)
 to `fit()`, which will in fact yield not only features (`x`) but optionally targets (`y`) and sample weights (`sample_weight`). Keras requires that the output of such iterator-likes be unambiguous. The iterator should return a tuple of length 1, 2, or 3, where the optional second and third elements will be used for `y` and `sample_weight` respectively. Any other type provided will be wrapped in a length-one tuple, effectively treating everything as `x`. When yielding dicts, they should still adhere to the top-level tuple structure, e.g. `({"x0": x0, "x1": x1}, y)`. Keras will not attempt to separate features, targets, and weights from the keys of a single dict. A notable unsupported data type is the `namedtuple`. The reason is that it behaves like both an ordered datatype (tuple) and a mapping datatype (dict). So given a namedtuple of the form: `namedtuple("example_tuple", ["y", "x"])` it is ambiguous whether to reverse the order of the elements when interpreting the value. Even worse is a tuple of the form: `namedtuple("other_tuple", ["x", "y", "z"])` where it is unclear if the tuple was intended to be unpacked into `x`, `y`, and `sample_weight` or passed through as a single element to `x`.

|     |
| --- |
| Returns |     |
| A `History` object. Its `History.history` attribute is a record of training loss values and metrics values at successive epochs, as well as validation loss values and validation metrics values (if applicable). |     |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L864-L917)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `get_compile_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L981-L992)

get_compile_config()

Returns a serialized config with information for compiling the model.

This method returns a config dictionary containing all the information (optimizer, loss, metrics, etc.) with which the model was compiled.

|     |
| --- |
| Returns |     |
| A dict containing information for compiling the model. |     |

### `get_layer`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L181-L220)

get_layer(
        name=None, index=None
    )

Retrieves a layer based on either its name (unique) or index.

If `name` and `index` are both provided, `index` will take precedence. Indices are based on order of horizontal graph traversal (bottom-up).

|     |     |
| --- | --- |
| Args |     |
| `name` | String, name of layer. |
| `index` | Integer, index of layer. |

|     |
| --- |
| Returns |     |
| A layer instance. |     |

### `get_metrics_result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L529-L546)

get_metrics_result()

Returns the model's metrics values as a dict.

If any of the metric result is a dict (containing multiple metrics), each of them gets added to the top level returned dict of this method.

|     |     |
| --- | --- |
| Returns |     |
| A `dict` containing values of the metrics listed in `self.metrics`. |     |
| `Example` | `{'loss': 0.2, 'accuracy': 0.7}`. |

### `get_quantization_layer_structure`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L427-L448)

get_quantization_layer_structure(
        mode=None
    )

Returns the quantization structure for the model.

This method is intended to be overridden by model authors to provide topology information required for structure-aware quantization modes like 'gptq'.

|     |     |
| --- | --- |
| Args |     |
| `mode` | The quantization mode. |

|     |
| --- |
| Returns |     |
| A dictionary describing the topology, e.g.: `{'pre_block_layers': [list], 'sequential_blocks': [list]}` or `None` if the mode does not require structure or is not supported. `'pre_block_layers'` is a list of layers that the inputs should be passed through, before being passed to the sequential blocks. For example, inputs to an LLM must first be passed through an embedding layer, followed by the transformer. |     |

### `get_state_tree`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L924-L1002)

get_state_tree(
        value_format='backend_tensor'
    )

Retrieves tree-like structure of model variables.

This method allows retrieval of different model variables (trainable, non-trainable, optimizer, and metrics). The variables are returned in a nested dictionary format, where the keys correspond to the variable names and the values are the nested representations of the variables.

|     |     |
| --- | --- |
| Returns |     |
| `dict` | A dictionary containing the nested representations of the requested variables. The keys are the variable names, and the values are the corresponding nested dictionaries. |
| `value_format` | One of `"backend_tensor"`, `"numpy_array"`. The kind of array to return as the leaves of the nested state tree. |

#### Example:

model = keras.Sequential([\
        keras.Input(shape=(1,), name="my_input"),\
        keras.layers.Dense(1, activation="sigmoid", name="my_dense"),\
    ], name="my_sequential")
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.fit(np.array([[1.0]]), np.array([[1.0]]))
    state_tree = model.get_state_tree()

The `state_tree` dictionary returned looks like:

{
        'metrics_variables': {
            'loss': {
                'count': ...,
                'total': ...,
            },
            'mean_absolute_error': {
                'count': ...,
                'total': ...,
            }
        },
        'trainable_variables': {
            'my_sequential': {
                'my_dense': {
                    'bias': ...,
                    'kernel': ...,
                }
            }
        },
        'non_trainable_variables': {},
        'optimizer_variables': {
            'adam': {
                    'iteration': ...,
                    'learning_rate': ...,
                    'my_sequential_my_dense_bias_momentum': ...,
                    'my_sequential_my_dense_bias_velocity': ...,
                    'my_sequential_my_dense_kernel_momentum': ...,
                    'my_sequential_my_dense_kernel_velocity': ...,
                }
            }
        }
    }

### `load_weights`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L377-L425)

load_weights(
        filepath, skip_mismatch=False, **kwargs
    )

Load the weights from a single file or sharded files.

Weights are loaded based on the network's topology. This means the architecture should be the same as when the weights were saved. Note that layers that don't have weights are not taken into account in the topological ordering, so adding or removing layers is fine as long as they don't have weights.

**Partial weight loading**

If you have modified your model, for instance by adding a new layer (with weights) or by changing the shape of the weights of a layer, you can choose to ignore errors and continue loading by setting `skip_mismatch=True`. In this case any layer with mismatching weights will be skipped. A warning will be displayed for each skipped layer.

**Sharding**

When loading sharded weights, it is important to specify `filepath` that ends with `*.weights.json` which is used as the configuration file. Additionally, the sharded files `*_xxxxx.weights.h5` must be in the same directory as the configuration file.

|     |     |
| --- | --- |
| Args |     |
| `filepath` | `str` or `pathlib.Path` object. Path where the weights will be saved. When sharding, the filepath must end in `.weights.json`. |
| `skip_mismatch` | Boolean, whether to skip loading of layers where there is a mismatch in the number of weights, or a mismatch in the shape of the weights. |

#### Example:

# Load the weights in a single file.
    model.load_weights("model.weights.h5")
    
    # Load the weights in sharded files.
    model.load_weights("model.weights.json")

### `loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L704-L711)

loss(
        y, y_pred, sample_weight=None
    )

### `make_predict_function`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L264-L312)

make_predict_function(
        force=False
    )

### `make_test_function`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L259-L262)

make_test_function(
        force=False
    )

### `make_train_function`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L254-L257)

make_train_function(
        force=False
    )

### `predict`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L521-L598)

predict(
        x, batch_size=None, verbose='auto', steps=None, callbacks=None
    )

Generates output predictions for the input samples.

Computation is done in batches. This method is designed for batch processing of large numbers of inputs. It is not intended for use inside of loops that iterate over your data and process small numbers of inputs at a time.

For small numbers of inputs that fit in one batch, directly use `__call__()` for faster execution, e.g., `model(x)`, or `model(x, training=False)` if you have layers such as `BatchNormalization` that behave differently during inference.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. It can be:<br><br>*   A NumPy array (or array-like), or a list of arrays (in case the model has multiple inputs).<br>*   A backend-native tensor, or a list of tensors (in case the model has multiple inputs).<br>*   A dict mapping input names to the corresponding array/tensors, if the model has named inputs.<br>*   A [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>    .<br>*   A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>    .<br>*   A `torch.utils.data.DataLoader`.<br>*   A Python generator function. |
| `batch_size` | Integer or `None`. Number of samples per batch of computation. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your input data `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function since they generate batches. |
| `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = single line. `"auto"` becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g. in a production environment). Defaults to `"auto"`. |
| `steps` | Total number of steps (batches of samples) to draw before declaring the prediction round finished. If `steps` is `None`, it will run until `x` is exhausted. In the case of an infinitely repeating dataset, it will run indefinitely. |
| `callbacks` | List of [`keras.callbacks.Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)<br> instances. List of callbacks to apply during prediction. |

|     |
| --- |
| Returns |     |
| NumPy array(s) of predictions. |     |

### `predict_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L658-L664)

predict_on_batch(
        x
    )

Returns predictions for a single batch of samples.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. It must be array-like. |

|     |
| --- |
| Returns |     |
| NumPy array(s) of predictions. |     |

### `predict_step`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L107-L113)

predict_step(
        data
    )

### `reset_metrics`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L310-L312)

reset_metrics()

### `save`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L273-L317)

save(
        filepath, overwrite=True, zipped=None, **kwargs
    )

Saves a model as a `.keras` file.

Note that `model.save()` is an alias for `keras.saving.save_model()`.

The saved `.keras` file contains:

*   The model's configuration (architecture)
*   The model's weights
*   The model's optimizer's state (if any)

Thus models can be reinstantiated in the exact same state.

|     |     |
| --- | --- |
| Args |     |
| `filepath` | `str` or `pathlib.Path` object. The path where to save the model. Must end in `.keras` (unless saving the model as an unzipped directory via `zipped=False`). |
| `overwrite` | Whether we should overwrite any existing model at the target location, or instead ask the user via an interactive prompt. |
| `zipped` | Whether to save the model as a zipped `.keras` archive (default when saving locally), or as an unzipped directory (default when saving on the Hugging Face Hub). |

#### Example:

model = keras.Sequential(
        [\
            keras.layers.Dense(5, input_shape=(3,)),\
            keras.layers.Softmax(),\
        ],
    )
    model.save("model.keras")
    loaded_model = keras.saving.load_model("model.keras")
    x = keras.random.uniform((10, 3))
    assert np.allclose(model.predict(x), loaded_model.predict(x))

### `save_weights`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L319-L375)

save_weights(
        filepath, overwrite=True, max_shard_size=None
    )

Saves all weights to a single file or sharded files.

By default, the weights will be saved in a single `.weights.h5` file. If sharding is enabled (`max_shard_size` is not `None`), the weights will be saved in multiple files, each with a size at most `max_shard_size` (in GB). Additionally, a configuration file `.weights.json` will contain the metadata for the sharded files.

The saved sharded files contain:

*   `*.weights.json`: The configuration file containing 'metadata' and 'weight\_map'.
*   `*_xxxxxx.weights.h5`: The sharded files containing only the weights.

|     |     |
| --- | --- |
| Args |     |
| `filepath` | `str` or `pathlib.Path` object. Path where the weights will be saved. When sharding, the filepath must end in `.weights.json`. If `.weights.h5` is provided, it will be overridden. |
| `overwrite` | Whether to overwrite any existing weights at the target location or instead ask the user via an interactive prompt. |
| `max_shard_size` | `int` or `float`. Maximum size in GB for each sharded file. If `None`, no sharding will be done. Defaults to `None`. |

#### Example:

# Instantiate a EfficientNetV2L model with about 454MB of weights.
    model = keras.applications.EfficientNetV2L(weights=None)
    
    # Save the weights in a single file.
    model.save_weights("model.weights.h5")
    
    # Save the weights in sharded files. Use `max_shard_size=0.25` means
    # each sharded file will be at most ~250MB.
    model.save_weights("model.weights.json", max_shard_size=0.25)
    
    # Load the weights in a new model with the same architecture.
    loaded_model = keras.applications.EfficientNetV2L(weights=None)
    loaded_model.load_weights("model.weights.h5")
    x = keras.random.uniform((1, 480, 480, 3))
    assert np.allclose(model.predict(x), loaded_model.predict(x))
    
    # Load the sharded weights in a new model with the same architecture.
    loaded_model = keras.applications.EfficientNetV2L(weights=None)
    loaded_model.load_weights("model.weights.json")
    x = keras.random.uniform((1, 480, 480, 3))
    assert np.allclose(model.predict(x), loaded_model.predict(x))

### `set_state_tree`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L1037-L1076)

set_state_tree(
        state_tree
    )

Assigns values to variables of the model.

This method takes a dictionary of nested variable values, which represents the state tree of the model, and assigns them to the corresponding variables of the model. The dictionary keys represent the variable names (e.g., `'trainable_variables'`, `'optimizer_variables'`), and the values are nested dictionaries containing the variable paths and their corresponding values.

|     |     |
| --- | --- |
| Args |     |
| `state_tree` | A dictionary representing the state tree of the model. The keys are the variable names, and the values are nested dictionaries representing the variable paths and their values. |

### `stateless_compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L439-L481)

stateless_compute_loss(
        trainable_variables,
        non_trainable_variables,
        metrics_variables,
        x=None,
        y=None,
        y_pred=None,
        sample_weight=None,
        training=True
    )

### `summary`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L222-L271)

summary(
        line_length=None,
        positions=None,
        print_fn=None,
        expand_nested=False,
        show_trainable=False,
        layer_range=None
    )

Prints a string summary of the network.

|     |     |
| --- | --- |
| Args |     |
| `line_length` | Total length of printed lines (e.g. set this to adapt the display to different terminal window sizes). |
| `positions` | Relative or absolute positions of log elements in each line. If not provided, becomes `[0.3, 0.6, 0.70, 1.]`. Defaults to `None`. |
| `print_fn` | Print function to use. By default, prints to `stdout`. If `stdout` doesn't work in your environment, change to `print`. It will be called on each line of the summary. You can set it to a custom function in order to capture the string summary. |
| `expand_nested` | Whether to expand the nested models. Defaults to `False`. |
| `show_trainable` | Whether to show if a layer is trainable. Defaults to `False`. |
| `layer_range` | a list or tuple of 2 strings, which is the starting layer name and ending layer name (both inclusive) indicating the range of layers to be printed in summary. It also accepts regex patterns instead of exact names. In this case, the start predicate will be the first element that matches `layer_range[0]` and the end predicate will be the last element that matches `layer_range[1]`. By default `None` considers all layers of the model. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if `summary()` is called before the model is built. |

### `test_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L635-L656)

test_on_batch(
        x, y=None, sample_weight=None, return_dict=False
    )

Test the model on a single batch of samples.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. Must be array-like. |
| `y` | Target data. Must be array-like. |
| `sample_weight` | Optional array of the same length as x, containing weights to apply to the model's loss for each sample. In the case of temporal data, you can pass a 2D array with shape `(samples, sequence_length)`, to apply a different weight to every timestep of every sample. |
| `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

|     |
| --- |
| Returns |     |
| A scalar loss value (when no metrics and `return_dict=False`), a list of loss and metric values (if there are metrics and `return_dict=False`), or a dict of metric and loss values (if `return_dict=True`). |     |

### `test_step`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L90-L105)

test_step(
        data
    )

### `to_json`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L636-L652)

to_json(
        **kwargs
    )

Returns a JSON string containing the network configuration.

To load a network from a JSON save file, use [`keras.models.model_from_json(json_string, custom_objects={...})`](https://www.tensorflow.org/api_docs/python/tf/keras/models/model_from_json)
.

|     |     |
| --- | --- |
| Args |     |
| `**kwargs` | Additional keyword arguments to be passed to `json.dumps()`. |

|     |
| --- |
| Returns |     |
| A JSON string. |     |

### `train_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L600-L633)

train_on_batch(
        x, y=None, sample_weight=None, class_weight=None, return_dict=False
    )

Runs a single gradient update on a single batch of data.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. Must be array-like. |
| `y` | Target data. Must be array-like. |
| `sample_weight` | Optional array of the same length as x, containing weights to apply to the model's loss for each sample. In the case of temporal data, you can pass a 2D array with shape `(samples, sequence_length)`, to apply a different weight to every timestep of every sample. |
| `class_weight` | Optional dictionary mapping class indices (integers) to a weight (float) to apply to the model's loss for the samples from this class during training. This can be useful to tell the model to "pay more attention" to samples from an under-represented class. When `class_weight` is specified and targets have a rank of 2 or greater, either `y` must be one-hot encoded, or an explicit final dimension of 1 must be included for sparse class labels. |
| `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

|     |
| --- |
| Returns |     |
| A scalar loss value (when no metrics and `return_dict=False`), a list of loss and metric values (if there are metrics and `return_dict=False`), or a dict of metric and loss values (if `return_dict=True`). |     |

### `train_step`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L53-L88)

train_step(
        data
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-04 UTC.