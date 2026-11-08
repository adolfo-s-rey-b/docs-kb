None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Model Architectures](https://keras.io/keras_hub/api/models/)
 / [Bart](https://keras.io/keras_hub/api/models/bart/)
 / BartBackbone model

BartBackbone model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/bart/bart_backbone.py#L15)

### `BartBackbone` class

Copied!

`keras_hub.models.BartBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     dropout=0.1,     max_sequence_length=1024,     dtype=None,     **kwargs )`

BART encoder-decoder network.

This class implements a Transformer-based encoder-decoder model as described in ["BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension"](https://arxiv.org/abs/1910.13461)
.

The default constructor gives a fully customizable, randomly initialized BART model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/facebookresearch/fairseq/)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer encoder layers and transformer decoder layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding and pooler layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **dropout**: float. Dropout probability for the Transformer encoder.
*   **max\_sequence\_length**: int. The maximum sequence length that this encoder can consume. If None, `max_sequence_length` uses the value from sequence length. This determines the variable shape for positional embeddings.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "encoder_token_ids": np.ones(shape=(1, 12), dtype="int32"),     "encoder_padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]     ),     "decoder_token_ids": np.ones(shape=(1, 12), dtype="int32"),     "decoder_padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]     ), }  # Pretrained BART encoder. model = keras_hub.models.BartBackbone.from_preset("bart_base_en") model(input_data)  # Randomly initialized BART encoder-decoder model with a custom config model = keras_hub.models.BartBackbone(     vocabulary_size=50265,     num_layers=6,     num_heads=12,     hidden_dim=768,     intermediate_dim=3072,     max_sequence_length=12, ) output = model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`BartBackbone.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as a one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a ModelScope handle like `'modelscope://user/bert_base_en'`
5.  a path to a local preset directory like `'./bert_base_en'`

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Backbone.from_preset()`, or from a model class like `keras_hub.models.GemmaBackbone.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

For any `Backbone` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma backbone with pre-trained weights. model = keras_hub.models.Backbone.from_preset(     "gemma_2b_en", )  # Load a Bert backbone with a pre-trained config and random weights. model = keras_hub.models.Backbone.from_preset(     "bert_base_en",     load_weights=False, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [bart\_base\_en](https://www.kaggle.com/models/keras/bart/keras/bart_base_en/3) | 139.42M | 6-layer BART model where case is maintained. Trained on BookCorpus, English Wikipedia and CommonCrawl. |
| [bart\_large\_en](https://www.kaggle.com/models/keras/bart/keras/bart_large_en/3) | 406.29M | 12-layer BART model where case is maintained. Trained on BookCorpus, English Wikipedia and CommonCrawl. |
| [bart\_large\_en\_cnn](https://www.kaggle.com/models/keras/bart/keras/bart_large_en_cnn/3) | 406.29M | The `bart_large_en` backbone model fine-tuned on the CNN+DM summarization dataset. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.BartBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[BartBackbone model](https://keras.io/keras_hub/api/models/bart/bart_backbone/#bartbackbone-model)

[`BartBackbone` class](https://keras.io/keras_hub/api/models/bart/bart_backbone/#bartbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/bart/bart_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/bart/bart_backbone/#tokenembedding-property)