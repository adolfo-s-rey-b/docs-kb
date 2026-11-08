[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Flayers%2FFeedForwardExperts&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.FeedForwardExperts Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/FeedForwardExperts#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/moe.py#L399-L491)

Feed-forward layer with multiple experts.

tfm.nlp.layers.FeedForwardExperts(
        num_experts: int,
        d_ff: int,
        *,
        inner_dropout: float = 0.0,
        output_dropout: float = 0.0,
        activation: Callable[[tf.Tensor], tf.Tensor] = tf_keras.activations.gelu,
        kernel_initializer: _InitializerType = _DEFAULT_KERNEL_INITIALIZER,
        bias_initializer: _InitializerType = _DEFAULT_BIAS_INITIALIZER,
        name: str = 'experts',
        **kwargs
    )

Note that call() takes inputs with shape \[num\_groups, num\_experts, expert\_capacity, hidden\_dim\] which is different from the usual \[batch\_size, seq\_len, hidden\_dim\] used by the FeedForward layer.

The experts are independent FeedForward layers of the same shape, i.e. the kernel doesn't have shape \[hidden\_dim, out\_dim\], but \[num\_experts, hidden\_dim, out\_dim\].

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_experts` | Number of experts (i.e. number of independent feed-forward blocks). |
| `d_ff` | Dimension of feed-forward layer of each expert. |
| `inner_dropout` | The dropout probability to be applied after intermediate activations. |
| `output_dropout` | The dropout probability to be applied after output layer. |
| `activation` | (Nonlinear) transform applied in layer. |
| `kernel_initializer` | Initialization scheme for kernel. |
| `bias_initializer` | Initialization scheme for bias. |
| `name` | Layer name. |
| `**kwargs` | Forwarded to super. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/moe.py#L471-L491)

call(
        inputs: tf.Tensor, *, training: Optional[bool] = None
    ) -> tf.Tensor

Applies layer to inputs.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Inputs of shape \[num\_groups, num\_experts, expert\_capacity, hidden\_dim\]. |
| `training` | Only apply dropout during training. |

|     |
| --- |
| Returns |     |
| Transformed inputs with the same shape as inputs \[num\_groups, num\_experts, expert\_capacity, hidden\_dim\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.