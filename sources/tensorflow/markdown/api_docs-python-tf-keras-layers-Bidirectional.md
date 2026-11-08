[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#from_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#reset_states)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Bidirectional Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#args_1)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#call-arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#from_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#reset_state)
        
    *   [reset\_states](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional?version=stable#reset_states)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/bidirectional.py#L13-L549)

Bidirectional wrapper for RNNs.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Bidirectional(
        layer,
        merge_mode='concat',
        weights=None,
        backward_layer=None,
        **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Text classification with an RNN](https://www.tensorflow.org/text/tutorials/text_classification_rnn)<br>    <br>*   [Graph regularization for sentiment classification using synthesized graphs](https://www.tensorflow.org/neural_structured_learning/tutorials/graph_keras_lstm_imdb)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `layer` | [`keras.layers.RNN`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN)<br> instance, such as [`keras.layers.LSTM`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM)<br> or [`keras.layers.GRU`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GRU)<br>. It could also be a [`keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)<br> instance that meets the following criteria:<br><br>1.  Be a sequence-processing layer (accepts 3D+ inputs).<br>2.  Have a `go_backwards`, `return_sequences` and `return_state` attribute (with the same semantics as for the `RNN` class).<br>3.  Have an `input_spec` attribute.<br>4.  Implement serialization via `get_config()` and `from_config()`. Note that the recommended way to create new RNN layers is to write a custom RNN cell and use it with [`keras.layers.RNN`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN)<br>    , instead of subclassing [`keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)<br>     directly. When `return_sequences` is `True`, the output of the masked timestep will be zero regardless of the layer's original `zero_output_for_mask` value. |
| `merge_mode` | Mode by which outputs of the forward and backward RNNs will be combined. One of `{"sum", "mul", "concat", "ave", None}`. If `None`, the outputs will not be combined, they will be returned as a list. Defaults to `"concat"`. |
| `backward_layer` | Optional [`keras.layers.RNN`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RNN)<br>, or [`keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)<br> instance to be used to handle backwards input processing. If `backward_layer` is not provided, the layer instance passed as the `layer` argument will be used to generate the backward layer automatically. Note that the provided `backward_layer` layer should have properties matching those of the `layer` argument, in particular it should have the same values for `stateful`, `return_states`, `return_sequences`, etc. In addition, `backward_layer` and `layer` should have different `go_backwards` argument values. A `ValueError` will be raised if these requirements are not met. |

|     |
| --- |
| Call arguments<br>-------------- |     |
| The call arguments for this layer are the same as those of the wrapped RNN layer. Beware that when passing the `initial_state` argument during the call of this layer, the first half in the list of elements in the `initial_state` list will be passed to the forward RNN call and the last half in the list of elements will be passed to the backward RNN call. |     |

#### Examples:

model = Sequential([\
        Input(shape=(5, 10)),\
        Bidirectional(LSTM(10, return_sequences=True),\
        Bidirectional(LSTM(10)),\
        Dense(5, activation="softmax"),\
    ])
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    
    # With custom backward layer
    forward_layer = LSTM(10, return_sequences=True)
    backward_layer = LSTM(10, activation='relu', return_sequences=True,
                          go_backwards=True)
    model = Sequential([\
        Input(shape=(5, 10)),\
        Bidirectional(forward_layer, backward_layer=backward_layer),\
        Dense(5, activation="softmax"),\
    ])
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `states` |     |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/bidirectional.py#L532-L549)

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

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/bidirectional.py#L485-L489)

reset_state()

### `reset_states`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/bidirectional.py#L481-L483)

reset_states()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.