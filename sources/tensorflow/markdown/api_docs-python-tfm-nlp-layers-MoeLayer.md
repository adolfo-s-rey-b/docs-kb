[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Flayers%2FMoeLayer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.MoeLayer Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MoeLayer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/moe.py#L494-L653)

Sparse MoE layer with per-token routing.

tfm.nlp.layers.MoeLayer(
        experts: tfm.nlp.layers.FeedForwardExperts,
        router: MaskedRouter,
        *,
        train_capacity_factor: float = 1.0,
        eval_capacity_factor: float = 1.0,
        examples_per_group: float = 1.0,
        name: str = 'moe',
        **kwargs
    )

In this TF implementation, all experts need to fit onto a single device allowing for batch parallelism only.

Uses Keras add\_loss() and add\_metric() APIs.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `experts` | Instance of FeedForwardExperts. Needs to have the same num\_experts as the router. |
| `router` | Instance of MaskedRouter to route the tokens to the different experts. |
| `train_capacity_factor` | Scaling factor to increase the expert token capacity during training. This factor plays an analogous, but slightly different, role depending on the routing assignment algorithm:<br><br>*   For "tokens choose" routing, the capacity factor only affects the maximum number of tokens that an expert will process. It does not affect how many experts a given token is routed to; see the num\_selected\_experts attributes of "tokens choose" routers.<br>*   For "experts choose" routing, because experts always fill their buffer, increasing the capacity factor will increase the number of tokens that an expert will process AND will indirectly increase the number of experts that a given token is routed to. |
| `eval_capacity_factor` | As above, but used during evaluation. |
| `examples_per_group` | Number of examples to form a group. Router then performs top\_k token selection for each expert on a per group basis. E.g. when `examples_per_group=4.0`, tokens are assigned to experts in groups formed from 4 examples. When `examples_per_group=0.5`, each example is split into 2 groups. `examples_per_group` must divide the local batch size. A larger group size will result in slower but more accurate top-k and sorting computations, whereas a smaller group size will result in faster but more approximate (and potentially less stable) routing choices. In practice, we find that imperfect routing choices are tolerable and recommend choosing a group size on the order of 4096 tokens, although this number will vary based on model configuration and size. |
| `name` | Layer name. |
| `**kwargs` | Forwarded to super. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `num_experts` | Number of experts (i.e. number of independent feed-forward blocks). |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/moe.py#L562-L610)

call(
        inputs: tf.Tensor, *, training: Optional[bool] = None
    ) -> tf.Tensor

Applies MoeLayer.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Batch of input embeddings of shape \[batch\_size, seq\_length, hidden\_dim\]. |
| `training` | Only apply dropout and jitter noise during training. If not provided taken from tf\_keras.backend. |

|     |
| --- |
| Returns |     |
| Transformed inputs with same shape as inputs: \[batch\_size, seq\_length, hidden\_dim\]. |     |

|     |
| --- |
| Raises |     |
| ValueError if we cannot find a group\_size satisfying given requirements. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.