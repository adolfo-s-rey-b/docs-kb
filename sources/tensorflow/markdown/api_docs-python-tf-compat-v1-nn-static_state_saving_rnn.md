[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.static\_state\_saving\_rnn Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_state_saving_rnn#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/rnn.py#L1491-L1586)

RNN that accepts a state saver for time-truncated RNN calculation. (deprecated)

tf.compat.v1.nn.static_state_saving_rnn(
        cell, inputs, state_saver, state_name, sequence_length=None, scope=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cell` | An instance of `RNNCell`. |
| `inputs` | A length T list of inputs, each a `Tensor` of shape `[batch_size, input_size]`. |
| `state_saver` | A state saver object with methods `state` and `save_state`. |
| `state_name` | Python string or tuple of strings. The name to use with the state\_saver. If the cell returns tuples of states (i.e., `cell.state_size` is a tuple) then `state_name` should be a tuple of strings having the same length as `cell.state_size`. Otherwise it should be a single string. |
| `sequence_length` | (optional) An int32/int64 vector size \[batch\_size\]. See the documentation for rnn() for more details about sequence\_length. |
| `scope` | VariableScope for the created subgraph; defaults to "rnn". |

|     |
| --- |
| Returns<br>------- |     |
| A pair (outputs, state) where: outputs is a length T list of outputs (one for each input) states is the final state |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `cell` is not an instance of RNNCell. |
| `ValueError` | If `inputs` is `None` or an empty list, or if the arity and type of `state_name` does not match that of `cell.state_size`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.