[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#get_initial_state)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.StackedRNNCells Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#methods_2)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#from_config)
        
    *   [get\_initial\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells?version=stable#get_initial_state)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/stacked_rnn_cells.py#L8-L138)

Wrapper allowing a stack of RNN cells to behave as a single cell.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.StackedRNNCells(
        cells, **kwargs
    )

Used to implement efficient stacked RNNs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cells` | List of RNN cell instances. |

#### Example:

batch_size = 3
    sentence_length = 5
    num_features = 2
    new_shape = (batch_size, sentence_length, num_features)
    x = np.reshape(np.arange(30), new_shape)
    
    rnn_cells = [keras.layers.LSTMCell(128) for _ in range(2)]
    stacked_lstm = keras.layers.StackedRNNCells(rnn_cells)
    lstm_layer = keras.layers.RNN(stacked_lstm)
    
    result = lstm_layer(x)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output_size` |     |
| `state_size` |     |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/stacked_rnn_cells.py#L129-L138)

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

### `get_initial_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/rnn/stacked_rnn_cells.py#L62-L85)

get_initial_state(
        batch_size=None
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.