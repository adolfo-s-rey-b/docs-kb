[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.PositionalEncoding Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/PositionalEncoding#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L482-L647)

Creates a network layer that adds a sinusoidal positional encoding.

tfm.vision.layers.PositionalEncoding(
        initializer: tf_keras.initializers.Initializer = 'zeros',
        cache_encoding: bool = False,
        state_prefix: Optional[str] = None,
        **kwargs
    )

Positional encoding is incremented across frames, and is added to the input. The positional encoding is first weighted at 0 so that the network can choose to ignore it. This implements:

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin. Attention Is All You Need. ([https://arxiv.org/pdf/1706.03762.pdf](https://arxiv.org/pdf/1706.03762.pdf)
).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initializer` | A `str` of initializer for weighting the positional encoding. |
| `cache_encoding` | A `bool`. If True, cache the positional encoding tensor after calling build. Otherwise, rebuild the tensor for every call. Setting this to False can be useful when we want to input a variable number of frames, so the positional encoding tensor can change shape. |
| `state_prefix` | a prefix string to identify states. |
| `**kwargs` | Additional keyword arguments to be passed to this layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L608-L647)

call(
        inputs: tf.Tensor,
        states: Optional[States] = None,
        output_states: bool = True
    ) -> Union[tf.Tensor, Tuple[tf.Tensor, States]]

Calls the layer with the given inputs.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | An input [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |
| `states` | A `dict` of states such that, if any of the keys match for this layer, will overwrite the contents of the buffer(s). Expected keys include `state_prefix + '_pos_enc_frame_count'`. |
| `output_states` | A `bool`. If True, returns the output tensor and output states. Returns just the output tensor otherwise. |

|     |
| --- |
| Returns |     |
| An output [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> (and optionally the states if `output_states=True`). |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If using 'channels\_first' data format. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.