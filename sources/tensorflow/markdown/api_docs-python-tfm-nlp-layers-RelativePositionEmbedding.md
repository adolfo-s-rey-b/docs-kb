[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.RelativePositionEmbedding Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/RelativePositionEmbedding#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/position_embedding.py#L97-L174)

Creates a positional embedding.

tfm.nlp.layers.RelativePositionEmbedding(
        hidden_size: int,
        min_timescale: float = 1.0,
        max_timescale: float = 10000.0,
        **kwargs
    )

This layer calculates the position encoding as a mix of sine and cosine functions with geometrically increasing wavelengths. Defined and formulized in "Attention is All You Need", section 3.5. ([https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `hidden_size` | Size of the hidden layer. |
| `min_timescale` | Minimum scale that will be applied at each position |
| `max_timescale` | Maximum scale that will be applied at each position. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/position_embedding.py#L139-L174)

call(
        inputs, length=None
    )

Implements call() for the layer.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | An tensor whose second dimension will be used as `length`. If `None`, the other `length` argument must be specified. |
| `length` | An optional integer specifying the number of positions. If both `inputs` and `length` are spcified, `length` must be equal to the second dimension of `inputs`. |

|     |
| --- |
| Returns |     |
| A tensor in shape of `(length, hidden_size)`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.