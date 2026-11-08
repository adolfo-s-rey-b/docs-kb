[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.static\_rnn Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/static_rnn#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/rnn.py#L1311-L1488)

Creates a recurrent neural network specified by RNNCell `cell`. (deprecated)

tf.compat.v1.nn.static_rnn(
        cell,
        inputs,
        initial_state=None,
        dtype=None,
        sequence_length=None,
        scope=None
    )

The simplest form of RNN network generated is:

  state = cell.zero_state(...)
      outputs = []
      for input_ in inputs:
        output, state = cell(input_, state)
        outputs.append(output)
      return (outputs, state)

However, a few other options are available:

An initial state can be provided. If the sequence\_length vector is provided, dynamic calculation is performed. This method of calculation does not compute the RNN steps past the maximum sequence length of the minibatch (thus saving computational time), and properly propagates the state at an example's sequence length to the final state output.

The dynamic calculation performed is, at time `t` for batch row `b`,

  (output, state)(b, t) =
        (t >= sequence_length(b))
          ? (zeros(cell.output_size), states(b, sequence_length(b) - 1))
          : cell(input(b, t), state(b, t - 1))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cell` | An instance of RNNCell. |
| `inputs` | A length T list of inputs, each a `Tensor` of shape `[batch_size, input_size]`, or a nested tuple of such elements. |
| `initial_state` | (optional) An initial state for the RNN. If `cell.state_size` is an integer, this must be a `Tensor` of appropriate type and shape `[batch_size, cell.state_size]`. If `cell.state_size` is a tuple, this should be a tuple of tensors having shapes `[batch_size, s] for s in cell.state_size`. |
| `dtype` | (optional) The data type for the initial state and expected output. Required if initial\_state is not provided or RNN state has a heterogeneous dtype. |
| `sequence_length` | Specifies the length of each sequence in inputs. An int32 or int64 vector (tensor) size `[batch_size]`, values in `[0, T)`. |\
| `scope` | VariableScope for the created subgraph; defaults to "rnn". |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A pair (outputs, state) where:<br><br>*   outputs is a length T list of outputs (one for each input), or a nested tuple of such elements.<br>    <br>*   state is the final state |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `TypeError` | If `cell` is not an instance of RNNCell. |\
| `ValueError` | If `inputs` is `None` or an empty list, or if the input depth (column size) cannot be inferred from inputs via shape inference. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.