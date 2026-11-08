[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#call)
        
    *   [get\_embedding\_layer](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#get_embedding_layer)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#get_embedding_table)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.BertEncoder Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#call)
        
    *   [get\_embedding\_layer](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#get_embedding_layer)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/BertEncoder#get_embedding_table)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/bert_encoder.py#L342-L642)

Bi-directional Transformer-based encoder network.

tfm.nlp.networks.BertEncoder(
        vocab_size,
        hidden_size=768,
        num_layers=12,
        num_attention_heads=12,
        max_sequence_length=512,
        type_vocab_size=16,
        inner_dim=3072,
        inner_activation=(lambda x: tf_keras.activations.gelu(x, approximate=True)),
        output_dropout=0.1,
        attention_dropout=0.1,
        initializer=tf_keras.initializers.TruncatedNormal(stddev=0.02),
        output_range=None,
        embedding_width=None,
        embedding_layer=None,
        norm_first=False,
        dict_outputs=False,
        return_all_encoder_outputs=False,
        return_attention_scores: bool = False,
        return_word_embeddings: bool = False,
        **kwargs
    )

This network implements a bi-directional Transformer-based encoder as described in "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" ([https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
). It includes the embedding lookups and transformer layers, but not the masked language model or classification task networks.

The default values for this object are taken from the BERT-Base implementation in "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding".

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocab_size` | The size of the token vocabulary. |
| `hidden_size` | The size of the transformer hidden layers. |
| `num_layers` | The number of transformer layers. |
| `num_attention_heads` | The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads. |
| `max_sequence_length` | The maximum sequence length that this encoder can consume. If None, max\_sequence\_length uses the value from sequence length. This determines the variable shape for positional embeddings. |
| `type_vocab_size` | The number of types that the 'type\_ids' input can take. |
| `inner_dim` | The output dimension of the first Dense layer in a two-layer feedforward network for each transformer. |
| `inner_activation` | The activation for the first Dense layer in a two-layer feedforward network for each transformer. |
| `output_dropout` | Dropout probability for the post-attention and output dropout. |
| `attention_dropout` | The dropout rate to use for the attention layers within the transformer layers. |
| `initializer` | The initialzer to use for all weights in this encoder. |
| `output_range` | The sequence output range, \[0, output\_range), by slicing the target sequence of the last transformer layer. `None` means the entire target sequence will attend to the source sequence, which yields the full output. |\
| `embedding_width` | The width of the word embeddings. If the embedding width is not equal to hidden size, embedding parameters will be factorized into two matrices in the shape of \['vocab\_size', 'embedding\_width'\] and ['embedding\_width', 'hidden\_size'](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/'embedding_width'%20is%20usually%20much%0Asmaller%20than "hidden_size")<br>. |\
| `embedding_layer` | An optional Layer instance which will be called to generate embeddings for the input word IDs. |\
| `norm_first` | Whether to normalize inputs to attention and intermediate dense layers. If set False, output of attention and intermediate dense layers is normalized. |\
| `dict_outputs` | Whether to use a dictionary as the model outputs. |\
| `return_all_encoder_outputs` | Whether to output sequence embedding outputs of all encoder transformer layers. Note: when the following `dict_outputs` argument is True, all encoder outputs are always returned in the dict, keyed by `encoder_outputs`. |\
| `return_attention_scores` | Whether to add an additional output containing the attention scores of all transformer layers. This will be a list of length `num_layers`, and each element will be in the shape \[batch\_size, num\_attention\_heads, seq\_dim, seq\_dim\]. |\
| `return_word_embeddings` | If true, also return the input word embedding sequence in the bert inference output. |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `pooler_layer` | The pooler dense layer after the transformer layers. |\
| `transformer_layers` | List of Transformer layers in the encoder. |\
\
Methods\
-------\
\
### `call`\
\
call(\
        inputs, training=None, mask=None\
    )\
\
Calls the model on new inputs and returns the outputs as tensors.\
\
In this case `call()` just reapplies all ops in the graph to the new inputs (e.g. build a new computational graph from the provided inputs).\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `inputs` | Input tensor, or dict/list/tuple of input tensors. |\
| `training` | Boolean or boolean scalar tensor, indicating whether to run the `Network` in training mode or inference mode. |\
| `mask` | A mask or list of masks. A mask can be either a boolean tensor or None (no mask). For more details, check the guide [here](https://www.tensorflow.org/guide/keras/masking_and_padding)<br>. |\
\
|     |\
| --- |\
| Returns |     |\
| A tensor if there is a single output, or a list of tensors if there are more than one outputs. |     |\
\
### `get_embedding_layer`\
\
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/bert_encoder.py#L615-L616)\
\
get_embedding_layer()\
\
### `get_embedding_table`\
\
[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/bert_encoder.py#L612-L613)\
\
get_embedding_table()\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-06 UTC.