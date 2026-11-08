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
 / [Moonshine](https://keras.io/keras_hub/api/models/moonshine/)
 / MoonshineBackbone model

MoonshineBackbone model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/moonshine/moonshine_backbone.py#L56)

### `MoonshineBackbone` class

Copied!

`keras_hub.models.MoonshineBackbone(     vocabulary_size,     filter_dim,     encoder_num_layers,     decoder_num_layers,     hidden_dim,     intermediate_dim,     encoder_num_heads,     decoder_num_heads,     feedforward_expansion_factor=4,     encoder_use_swiglu_activation=False,     decoder_use_swiglu_activation=True,     max_position_embeddings=2048,     pad_head_dim_to_multiple_of=None,     partial_rotary_factor=0.62,     dropout=0.0,     initializer_range=0.02,     rope_theta=10000.0,     attention_bias=False,     attention_dropout=0.0,     dtype=None,     **kwargs )`

Moonshine backbone with integrated audio feature extraction.

This class implements an encoder-decoder backbone, as used in the Moonshine ASR system. It includes initial convolutional layers for audio feature extraction followed by `MoonshineEncoderBlock` instances for processing these features and `MoonshineDecoderBlock` instances for generating output sequences.

**Arguments**

*   **vocabulary\_size**: int. The size of the vocabulary for the embedding layers.
*   **filter\_dim**: int. The number of filters for the initial convolutional feature extractor layers. Typically matches `hidden_dim`.
*   **encoder\_num\_layers**: int. The number of stacked encoder blocks.
*   **decoder\_num\_layers**: int. The number of stacked decoder blocks.
*   **hidden\_dim**: int. The dimensionality of the model's hidden representations and embeddings.
*   **intermediate\_dim**: int. The dimensionality of the intermediate representations in feedforward networks.
*   **encoder\_num\_heads**: int. The number of attention heads in the encoder's multi-head attention.
*   **decoder\_num\_heads**: int. The number of attention heads in the decoder's multi-head attention.
*   **feedforward\_expansion\_factor**: int, optional. A multiplier applied to `intermediate_dim` to determine the total width of the feedforward network. Defaults to 4.
*   **encoder\_use\_swiglu\_activation**: bool, optional. When True, uses SwiGLU in the encoder feedforward network. Defaults to False.
*   **decoder\_use\_swiglu\_activation**: bool, optional. When True, uses SwiGLU in the decoder feedforward network. Defaults to True.
*   **max\_position\_embeddings**: int, optional. The maximum sequence length for position embeddings. Defaults to 2048.
*   **pad\_head\_dim\_to\_multiple\_of**: int, optional. If specified, pads the head dimension to be a multiple of this value for performance optimization. Defaults to None.
*   **partial\_rotary\_factor**: float, optional. The fraction of dimensions to apply rotary position embeddings to. Defaults to 0.62.
*   **dropout**: float, optional. The dropout probability for input dropout layers. Defaults to 0.0.
*   **initializer\_range**: float, optional. The standard deviation of the truncated normal initializer for weights. Defaults to 0.02.
*   **rope\_theta**: float, optional. The base frequency for rotary position embeddings. Defaults to 10,000.0.
*   **attention\_bias**: bool, optional. Whether to use bias in attention mechanisms. Defaults to False.
*   **attention\_dropout**: float, optional. The dropout probability for attention mechanisms. Defaults to 0.0.
*   **dtype**: str, optional. The dtype to use for model computations and weights. Defaults to None.

**Examples**

Copied!

`import numpy as np import keras from keras_hub.models import MoonshineBackbone  # Create random input data for demonstration. # Input is now raw-ish audio features (e.g., from MoonshineAudioConverter). encoder_raw_input_values = np.random.rand(1, 16000, 1).astype("float32") # Mask corresponding to the raw input time dimension encoder_padding_mask = np.ones((1, 16000), dtype="bool") decoder_token_ids = np.random.randint(     0, 1000, size=(1, 20), dtype="int32" ) decoder_padding_mask = np.ones((1, 20), dtype="bool")  # Initialize the Moonshine backbone with specific parameters. backbone = MoonshineBackbone(     vocabulary_size=10000,     filter_dim=256,     encoder_num_layers=6,     decoder_num_layers=6,     hidden_dim=256,     intermediate_dim=512,     encoder_num_heads=8,     decoder_num_heads=8,     feedforward_expansion_factor=4,     decoder_use_swiglu_activation=True,     encoder_use_swiglu_activation=False, )  # Forward pass through the model. outputs = backbone(     {         "encoder_input_values": encoder_raw_input_values,         "encoder_padding_mask": encoder_padding_mask,         "decoder_token_ids": decoder_token_ids,         "decoder_padding_mask": decoder_padding_mask,     } )  # Display the outputs. print("Encoder output shape:", outputs["encoder_sequence_output"].shape) print("Decoder output shape:", outputs["decoder_sequence_output"].shape)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MoonshineBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [moonshine\_tiny\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_tiny_en/1) | 27.09M | Moonshine tiny model for English speech recognition. Developed by Useful Sensors for real-time transcription. |
| [moonshine\_base\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_base_en/1) | 61.51M | Moonshine base model for English speech recognition. Developed by Useful Sensors for real-time transcription. |

* * *

### `token_embedding` property

Copied!

`keras_hub.models.MoonshineBackbone.token_embedding`

A [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 instance for embedding token ids.

This layer embeds integer token ids to the hidden dim of the model.

* * *

[MoonshineBackbone model](https://keras.io/keras_hub/api/models/moonshine/moonshine_backbone/#moonshinebackbone-model)

[`MoonshineBackbone` class](https://keras.io/keras_hub/api/models/moonshine/moonshine_backbone/#moonshinebackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/moonshine/moonshine_backbone/#frompreset-method)

[`token_embedding` property](https://keras.io/keras_hub/api/models/moonshine/moonshine_backbone/#tokenembedding-property)