[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fmodels%2Fclone_model&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.models.clone\_model Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/cloning.py#L13-L209)

Clone a Functional or Sequential `Model` instance.

tf.keras.models.clone_model(
        model,
        input_tensors=None,
        clone_function=None,
        call_function=None,
        recursive=False,
        **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [Federated Learning for Text Generation](https://www.tensorflow.org/federated/tutorials/federated_learning_for_text_generation) |

Model cloning is similar to calling a model on new inputs, except that it creates new layers (and thus new weights) instead of sharing the weights of the existing layers.

Note that `clone_model` will not preserve the uniqueness of shared objects within the model (e.g. a single variable attached to two distinct layers will be restored as two separate variables).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `model` | Instance of `Model` (could be a Functional model or a Sequential model). |
| `input_tensors` | optional list of input tensors or InputLayer objects to build the model upon. If not provided, new `Input` objects will be created. |
| `clone_function` | Callable with signature `fn(layer)` to be used to clone each layer in the target model (except `Input` instances). It takes as argument the layer instance to be cloned, and returns the corresponding layer instance to be used in the model copy. If unspecified, this callable defaults to the following serialization/deserialization function: `lambda layer: layer.__class__.from_config(layer.get_config())`. By passing a custom callable, you can customize your copy of the model, e.g. by wrapping certain layers of interest (you might want to replace all `LSTM` instances with equivalent `Bidirectional(LSTM(...))` instances, for example). Defaults to `None`. |
| `call_function` | Callable with signature `fn(layer, *args, **kwargs)` to be used to call each cloned layer and a set of inputs. It takes the layer instance, the call arguments and keyword arguments, and returns the call outputs. If unspecified, this callable defaults to the regular `__call__()` method: `def fn(layer, *args, **kwargs): return layer(*args, **kwargs)`. By passing a custom callable, you can insert new layers before or after a given layer. Note: this argument can only be used with Functional models. |
| `recursive` | Boolean. Whether to recursively clone any Sequential or Functional models encountered in the original Sequential/Functional model. If `False`, then inner models are cloned by calling `clone_function()`. If `True`, then inner models are cloned by calling `clone_model()` with the same `clone_function`, `call_function`, and `recursive` arguments. Note that in this case, `call_function` will not be propagated to any Sequential model (since it is not applicable to Sequential models). |

|     |
| --- |
| Returns<br>------- |     |
| An instance of `Model` reproducing the behavior of the original model, on top of new inputs tensors, using newly instantiated weights. The cloned model may behave differently from the original model if a custom `clone_function` or `call_function` modifies a layer or layer call. |     |

#### Example:

# Create a test Sequential model.
    model = keras.Sequential([\
        keras.layers.Input(shape=(728,)),\
        keras.layers.Dense(32, activation='relu'),\
        keras.layers.Dense(1, activation='sigmoid'),\
    ])
    # Create a copy of the test model (with freshly initialized weights).
    new_model = clone_model(model)

Using a `clone_function` to make a model deterministic by setting the random seed everywhere:

def clone_function(layer):
        config = layer.get_config()
        if "seed" in config:
            config["seed"] = 1337
        return layer.__class__.from_config(config)
    
    new_model = clone_model(model, clone_function=clone_function)

Using a `call_function` to add a `Dropout` layer after each `Dense` layer (without recreating new layers):

def call_function(layer, *args, **kwargs):
        out = layer(*args, **kwargs)
        if isinstance(layer, keras.layers.Dense):
            out = keras.layers.Dropout(0.5)(out)
        return out
    
    new_model = clone_model(
        model,
        clone_function=lambda x: x,  # Reuse the same layers.
        call_function=call_function,
    )

Note that subclassed models cannot be cloned by default, since their internal layer structure is not known. To achieve equivalent functionality as `clone_model` in the case of a subclassed model, simply make sure that the model class implements `get_config()` (and optionally `from_config()`), and call:

new_model = model.__class__.from_config(model.get_config())

In the case of a subclassed model, you cannot using a custom `clone_function`.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.