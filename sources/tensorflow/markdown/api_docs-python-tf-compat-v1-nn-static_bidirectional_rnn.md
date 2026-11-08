[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.static\_bidirectional\_rnn Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_bidirectional_rnn#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/rnn.py#L1589-L1684)

Creates a bidirectional recurrent neural network. (deprecated)

tf.compat.v1.nn.static_bidirectional_rnn(
        cell_fw,
        cell_bw,
        inputs,
        initial_state_fw=None,
        initial_state_bw=None,
        dtype=None,
        sequence_length=None,
        scope=None
    )

Similar to the unidirectional case above (rnn) but takes input and builds independent forward and backward RNNs with the final forward and backward outputs depth-concatenated, such that the output will have the format \[time\]\[batch\]\[cell\_fw.output\_size + cell\_bw.output\_size\]. The input\_size of forward and backward cell must match. The initial state for both directions is zero by default (but can be set optionally) and no intermediate states are ever returned -- the network is fully unrolled for the given (passed in) length(s) of the sequence(s) or completely unrolled if length(s) is not given.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cell_fw` | An instance of RNNCell, to be used for forward direction. |
| `cell_bw` | An instance of RNNCell, to be used for backward direction. |
| `inputs` | A length T list of inputs, each a tensor of shape \[batch\_size, input\_size\], or a nested tuple of such elements. |
| `initial_state_fw` | (optional) An initial state for the forward RNN. This must be a tensor of appropriate type and shape `[batch_size, cell_fw.state_size]`. If `cell_fw.state_size` is a tuple, this should be a tuple of tensors having shapes `[batch_size, s] for s in cell_fw.state_size`. |
| `initial_state_bw` | (optional) Same as for `initial_state_fw`, but using the corresponding properties of `cell_bw`. |
| `dtype` | (optional) The data type for the initial state. Required if either of the initial states are not provided. |
| `sequence_length` | (optional) An int32/int64 vector, size `[batch_size]`, containing the actual lengths for each of the sequences. |
| `scope` | VariableScope for the created subgraph; defaults to "bidirectional\_rnn" |

|     |
| --- |
| Returns<br>------- |     |
| A tuple (outputs, output\_state\_fw, output\_state\_bw) where: outputs is a length `T` list of outputs (one for each input), which are depth-concatenated forward and backward outputs. output\_state\_fw is the final state of the forward rnn. output\_state\_bw is the final state of the backward rnn. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `cell_fw` or `cell_bw` is not an instance of `RNNCell`. |
| `ValueError` | If inputs is None or an empty list. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.