[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.LinearTransformLayer Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/LinearTransformLayer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mixing.py#L197-L245)

Dense, linear transformation layer.

tfm.nlp.layers.LinearTransformLayer(
        kernel_initializer: _Initializer = default_kernel_initializer,
        name: str = 'linear_transform',
        **kwargs
    )

Applies matrix multiplications over sequence and hidden dimensions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `kernel_initializer` | Initialization scheme for kernel. |
| `name` | Name for layer. |
| `**kwargs` | Keyword arguments. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mixing.py#L230-L245)

call(
        query: tf.Tensor, value: tf.Tensor, **kwargs
    ) -> tf.Tensor

Applies layer to `query`.

|     |     |
| --- | --- |
| Args |     |
| `query` | Batch of input embeddings, typically of shape \[batch\_size, max\_seq\_length, hidden\_dim\]. |
| `value` | Unused. Included to match attention layer API. |
| `**kwargs` | Optional arguments to catch unused attention keyword arguments. |

|     |
| --- |
| Returns |     |
| Linearly transformed `query` inputs with shape \[batch\_size, max\_seq\_length, hidden\_dim\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.