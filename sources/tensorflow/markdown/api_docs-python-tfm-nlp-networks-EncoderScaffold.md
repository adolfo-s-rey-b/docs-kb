[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#call)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#get_embedding_table)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.EncoderScaffold Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#call)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/EncoderScaffold#get_embedding_table)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/encoder_scaffold.py#L28-L396)

Bi-directional Transformer-based encoder network scaffold.

tfm.nlp.networks.EncoderScaffold(
        pooled_output_dim,
        pooler_layer_initializer=tf_keras.initializers.TruncatedNormal(stddev=0.02),
        embedding_cls=None,
        embedding_cfg=None,
        embedding_data=None,
        num_hidden_instances=1,
        hidden_cls=tfm.nlp.layers.Transformer,
        hidden_cfg=None,
        mask_cls=tfm.nlp.layers.SelfAttentionMask,
        mask_cfg=None,
        layer_norm_before_pooling=False,
        return_all_layer_outputs=False,
        dict_outputs=False,
        layer_idx_as_attention_seed=False,
        feed_layer_idx=False,
        recursive=False,
        **kwargs
    )

This network allows users to flexibly implement an encoder similar to the one described in "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" ([https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
).

In this network, users can choose to provide a custom embedding subnetwork (which will replace the standard embedding logic) and/or a custom hidden layer class (which will replace the Transformer instantiation in the encoder). For each of these custom injection points, users can pass either a class or a class instance. If a class is passed, that class will be instantiated using the `embedding_cfg` or `hidden_cfg` argument, respectively; if an instance is passed, that instance will be invoked. (In the case of hidden\_cls, the instance will be invoked 'num\_hidden\_instances' times.

If the hidden\_cls is not overridden, a default transformer layer will be instantiated.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pooled_output_dim` | The dimension of pooled output. |
| `pooler_layer_initializer` | The initializer for the classification layer. |
| `embedding_cls` | The class or instance to use to embed the input data. This class or instance defines the inputs to this encoder and outputs (1) embeddings tensor with shape `(batch_size, seq_length, hidden_size)` and (2) attention masking with tensor `(batch_size, seq_length, seq_length)`. If `embedding_cls` is not set, a default embedding network (from the original BERT paper) will be created. |
| `embedding_cfg` | A dict of kwargs to pass to the embedding\_cls, if it needs to be instantiated. If `embedding_cls` is not set, a config dict must be passed to `embedding_cfg` with the following values: `vocab_size`: The size of the token vocabulary. `type_vocab_size`: The size of the type vocabulary. `hidden_size`: The hidden size for this encoder. `max_seq_length`: The maximum sequence length for this encoder. `seq_length`: The sequence length for this encoder. `initializer`: The initializer for the embedding portion of this encoder. `dropout_rate`: The dropout rate to apply before the encoding layers. |
| `embedding_data` | A reference to the embedding weights that will be used to train the masked language model, if necessary. This is optional, and only needed if (1) you are overriding `embedding_cls` and (2) are doing standard pretraining. |
| `num_hidden_instances` | The number of times to instantiate and/or invoke the hidden\_cls. |
| `hidden_cls` | Three types of input are supported: (1) class (2) instance (3) list of classes or instances, to encode the input data. If `hidden_cls` is not set, a KerasBERT transformer layer will be used as the encoder class. If `hidden_cls` is a list of classes or instances, these classes (instances) are sequentially instantiated (invoked) on top of embedding layer. Mixing classes and instances in the list is allowed. |
| `hidden_cfg` | A dict of kwargs to pass to the hidden\_cls, if it needs to be instantiated. If hidden\_cls is not set, a config dict must be passed to `hidden_cfg` with the following values: `num_attention_heads`: The number of attention heads. The hidden size must be divisible by `num_attention_heads`. `intermediate_size`: The intermediate size of the transformer. `intermediate_activation`: The activation to apply in the transfomer. `dropout_rate`: The overall dropout rate for the transformer layers. `attention_dropout_rate`: The dropout rate for the attention layers. `kernel_initializer`: The initializer for the transformer layers. |
| `mask_cls` | The class to generate masks passed into hidden\_cls() from inputs and 2D mask indicating positions we can attend to. It is the caller's job to make sure the output of the mask\_layer can be used by hidden\_layer. A mask\_cls is usually mapped to a hidden\_cls. |
| `mask_cfg` | A dict of kwargs pass to mask\_cls. |
| `layer_norm_before_pooling` | Whether to add a layer norm before the pooling layer. You probably want to turn this on if you set `norm_first=True` in transformer layers. |
| `return_all_layer_outputs` | Whether to output sequence embedding outputs of all encoder transformer layers. |
| `dict_outputs` | Whether to use a dictionary as the model outputs. |
| `layer_idx_as_attention_seed` | Whether to include layer\_idx in attention\_cfg in hidden\_cfg. |
| `feed_layer_idx` | whether the scaffold should feed layer index to hidden\_cls. |
| `recursive` | whether to pass the second return of the hidden layer as the last element among the inputs. None will be passed as the initial state. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `embedding_network` |     |
| `hidden_layers` | List of hidden layers in the encoder. |
| `pooler_layer` | The pooler dense layer after the transformer layers. |

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

### `get_embedding_table`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/encoder_scaffold.py#L360-L377)

get_embedding_table()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.