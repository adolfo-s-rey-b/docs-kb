[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#call)
        
    *   [get\_embedding\_lookup\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#get_embedding_lookup_table)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.XLNetBase Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#call)
        
    *   [get\_embedding\_lookup\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/XLNetBase#get_embedding_lookup_table)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/xlnet_base.py#L415-L710)

Base XLNet model.

tfm.nlp.networks.XLNetBase(
        vocab_size,
        num_layers,
        hidden_size,
        num_attention_heads,
        head_size,
        inner_size,
        dropout_rate,
        attention_dropout_rate,
        attention_type,
        bi_data,
        initializer,
        two_stream=False,
        tie_attention_biases=True,
        memory_length=None,
        clamp_length=-1,
        reuse_length=None,
        inner_activation='relu',
        use_cls_mask=False,
        embedding_width=None,
        **kwargs
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `vocab_size` | int, the number of tokens in vocabulary. |
| `num_layers` | int, the number of layers. |
| `hidden_size` | int, the hidden size. |
| `num_attention_heads` | int, the number of attention heads. |
| `head_size` | int, the dimension size of each attention head. |
| `inner_size` | int, the hidden size in feed-forward layers. |
| `dropout_rate` | float, dropout rate. |
| `attention_dropout_rate` | float, dropout rate on attention probabilities. |
| `attention_type` | str, "uni" or "bi". |
| `bi_data` | bool, whether to use bidirectional input pipeline. Usually set to True during pretraining and False during finetuning. |
| `initializer` | A tf initializer. |
| `two_stream` | bool, whether or not to use `TwoStreamRelativeAttention` used in the XLNet pretrainer. If `False`, then it will use `MultiHeadRelativeAttention` as in Transformer XL. |
| `tie_attention_biases` | bool, whether or not to tie the biases together. Usually set to `True`. Used for backwards compatibility. |
| `memory_length` | int, the number of tokens to cache. |
| `same_length` | bool, whether to use the same attention length for each token. |
| `clamp_length` | int, clamp all relative distances larger than clamp\_length. -1 means no clamping. |
| `reuse_length` | int, the number of tokens in the currect batch to be cached and reused in the future. |
| `inner_activation` | str, "relu" or "gelu". |
| `use_cls_mask` | bool, whether or not cls mask is included in the input sequences. |
| `embedding_width` | The width of the word embeddings. If the embedding width is not equal to hidden size, embedding parameters will be factorized into two matrices in the shape of \["vocab\_size", "embedding\_width"\] and ["embedding\_width", "hidden\_size"](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/%22embedding_width%22%20is%20usually%20much%0Asmaller%20than "hidden_size")<br>. |
| `embedding_layer` | The word embedding layer. `None` means we will create a new embedding layer. Otherwise, we will reuse the given embedding layer. This parameter is originally added for ELECTRA model which needs to tie the generator embeddings with the discriminator embeddings. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/xlnet_base.py#L606-L710)

call(
        inputs
    )

Implements call() for the layer.

### `get_embedding_lookup_table`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/xlnet_base.py#L580-L582)

get_embedding_lookup_table()

Returns the embedding layer weights.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.