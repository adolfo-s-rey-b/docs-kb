[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.ElectraPretrainer Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/ElectraPretrainer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/electra_pretrainer.py#L26-L224)

ELECTRA network training model.

tfm.nlp.models.ElectraPretrainer(
        generator_network,
        discriminator_network,
        vocab_size,
        num_classes,
        num_token_predictions,
        mlm_activation=None,
        mlm_initializer='glorot_uniform',
        output_type='logits',
        disallow_correct=False,
        **kwargs
    )

This is an implementation of the network structure described in "ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators" ( [https://arxiv.org/abs/2003.10555](https://arxiv.org/abs/2003.10555)
).

The ElectraPretrainer allows a user to pass in two transformer models, one for generator, the other for discriminator, and instantiates the masked language model (at generator side) and classification networks (at discriminator side) that are used to create the training objectives.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `generator_network` | A transformer network for generator, this network should output a sequence output and an optional classification output. |
| `discriminator_network` | A transformer network for discriminator, this network should output a sequence output |
| `vocab_size` | Size of generator output vocabulary |
| `num_classes` | Number of classes to predict from the classification network for the generator network (not used now) |
| `num_token_predictions` | Number of tokens to predict from the masked LM. |
| `mlm_activation` | The activation (if any) to use in the masked LM and classification networks. If None, no activation will be used. |
| `mlm_initializer` | The initializer (if any) to use in the masked LM and classification networks. Defaults to a Glorot uniform initializer. |
| `output_type` | The output style for this network. Can be either `logits` or `predictions`. |
| `disallow_correct` | Whether to disallow the generator to generate the exact same token in the original sentence |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` | Returns a dictionary of items to be additionally checkpointed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/electra_pretrainer.py#L116-L174)

call(
        inputs
    )

ELECTRA forward pass.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | A dict of all inputs, same as the standard BERT model. |

|     |     |
| --- | --- |
| Returns |     |
| `outputs` | A dict of pretrainer model outputs, including (1) lm\_outputs: A `[batch_size, num_token_predictions, vocab_size]` tensor indicating logits on masked positions. (2) sentence\_outputs: A `[batch_size, num_classes]` tensor indicating logits for nsp task. (3) disc\_logits: A `[batch_size, sequence_length]` tensor indicating logits for discriminator replaced token detection task. (4) disc\_label: A `[batch_size, sequence_length]` tensor indicating target labels for discriminator replaced token detection task. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.