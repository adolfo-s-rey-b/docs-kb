[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Flayers%2FMoeLayerWithBackbone&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.MoeLayerWithBackbone Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayerWithBackbone#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/moe.py#L656-L721)

Sparse MoE layer plus a FeedForward layer evaluated for all tokens.

tfm.nlp.layers.MoeLayerWithBackbone(
        moe: tfm.nlp.layers.MoeLayer,
        backbone_d_ff: int,
        *,
        inner_dropout: float = 0.0,
        output_dropout: float = 0.0,
        activation: Callable[[tf.Tensor], tf.Tensor] = tf_keras.activations.gelu,
        kernel_initializer: _InitializerType = _DEFAULT_KERNEL_INITIALIZER,
        bias_initializer: _InitializerType = _DEFAULT_BIAS_INITIALIZER,
        name: str = 'moe_with_backbone',
        **kwargs
    )

Uses Keras add\_loss() and add\_metric() APIs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `moe` | Instance of MoeLayer with experts and router. |
| `backbone_d_ff` | Dimension of feed-forward layer of a lightweight backbone, which is evaluated for all tokens. |
| `inner_dropout` | The dropout probability to be applied after intermediate activations for the backbone. |
| `output_dropout` | The dropout probability to be applied after the output of the backbone. |
| `activation` | (Nonlinear) transform applied in the backbone. |
| `kernel_initializer` | Initialization scheme for kernels in the backbone. |
| `bias_initializer` | Initialization scheme for biases in the backbone. |
| `name` | Layer name. |
| `**kwargs` | Forwarded to super. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/moe.py#L703-L721)

call(
        inputs: tf.Tensor, *, training: Optional[bool] = None
    ) -> tf.Tensor

Applies MoeLayerWithBackbone layer.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Batch of input embeddings of shape \[batch\_size, seq\_length, hidden\_dim\]. |
| `training` | Only apply dropout and jitter noise during training. If not provided taken from tf\_keras.backend. |

|     |
| --- |
| Returns |     |
| Transformed inputs with same shape as inputs: \[batch\_size, seq\_length, hidden\_dim\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.