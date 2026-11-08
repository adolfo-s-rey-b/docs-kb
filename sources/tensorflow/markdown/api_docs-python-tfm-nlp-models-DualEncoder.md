[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.DualEncoder Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/DualEncoder#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/dual_encoder.py#L23-L162)

A dual encoder model based on a transformer-based encoder.

tfm.nlp.models.DualEncoder(
        network: tf_keras.Model,
        max_seq_length: int = 32,
        normalize: bool = True,
        logit_scale: float = 1.0,
        logit_margin: float = 0.0,
        output: str = 'logits',
        **kwargs
    ) -> None

This is an implementation of the dual encoder network structure based on the transfomer stack, as described in ["Language-agnostic BERT Sentence Embedding"](https://arxiv.org/abs/2007.01852)

The DualEncoder allows a user to pass in a transformer stack, and build a dual encoder model based on the transformer stack.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `network` | A transformer network which should output an encoding output. |
| `max_seq_length` | The maximum allowed sequence length for transformer. |
| `normalize` | If set to True, normalize the encoding produced by transfomer. |
| `logit_scale` | The scaling factor of dot products when doing training. |
| `logit_margin` | The margin between positive and negative when doing training. |
| `output` | The output style for this network. Can be either `logits` or `predictions`. If set to `predictions`, it will output the embedding producted by transformer network. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` | Returns a dictionary of items to be additionally checkpointed. |

Methods
-------

### `call`

call(
        inputs, training=None, mask=None
    )

Calls the model on new inputs and returns the outputs as tensors.

In this case `call()` just reapplies all ops in the graph to the new inputs (e.g. build a new computational graph from the provided inputs).

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. |
| `training` | Boolean or boolean scalar tensor, indicating whether to run the `Network` in training mode or inference mode. |
| `mask` | A mask or list of masks. A mask can be either a boolean tensor or None (no mask). For more details, check the guide [here](https://www.tensorflow.org/guide/keras/masking_and_padding)<br>. |

|     |
| --- |
| Returns |     |
| A tensor if there is a single output, or a list of tensors if there are more than one outputs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.