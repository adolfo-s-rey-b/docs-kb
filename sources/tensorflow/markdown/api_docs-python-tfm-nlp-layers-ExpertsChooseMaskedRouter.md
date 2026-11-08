[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.ExpertsChooseMaskedRouter Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ExpertsChooseMaskedRouter#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/moe.py#L237-L318)

Masked matmul router using experts choose tokens assignment.

tfm.nlp.layers.ExpertsChooseMaskedRouter(
        num_experts: int,
        *,
        jitter_noise: float = 0.0,
        use_bias: bool = True,
        kernel_initializer: _InitializerType = _DEFAULT_KERNEL_INITIALIZER,
        bias_initializer: _InitializerType = _DEFAULT_BIAS_INITIALIZER,
        router_z_loss_weight: float = 0.0,
        export_metrics: bool = True,
        name: str = 'router',
        **kwargs
    )

This router uses the same mechanism as in Mixture-of-Experts with Expert Choice ([https://arxiv.org/abs/2202.09368](https://arxiv.org/abs/2202.09368)
): each expert selects its top expert\_capacity tokens. An individual token may be processed by multiple experts or none at all.

Uses Keras add\_loss() and add\_metric() APIs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_experts` | Number of experts. |
| `jitter_noise` | Amplitude of jitter noise applied to router logits. |
| `use_bias` | Whether or not to use the bias term in computing the router weights. |
| `kernel_initializer` | Kernel initializer for router weights. |
| `bias_initializer` | Bias initializer for router weights. |
| `router_z_loss_weight` | Weight for router\_z\_loss. Use non-zero values if running into training instability (esp. with dtype 'bfloat16' or lower). |
| `export_metrics` | Whether to export metrics using Keras add\_metric API. |
| `name` | Layer name. |
| `**kwargs` | Forwarded to super. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/moe.py#L138-L172)

call(
        inputs: tf.Tensor, *, expert_capacity: int, training: Optional[bool] = None
    ) -> RouterOutput

Computes dispatch and combine arrays for routing to experts.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Inputs to send to experts of shape \[num\_groups, tokens\_per\_group, hidden\_dim\]. |
| `expert_capacity` | Each group will send this many tokens to each expert. |
| `training` | If true, apply jitter noise during routing. If not provided taken from tf\_keras.backend. |

|     |
| --- |
| Returns |     |
| Router indices or mask arrays (depending on router type). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.