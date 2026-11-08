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
 / [Whisper](https://keras.io/keras_hub/api/models/whisper/)
 / WhisperBackbone model

WhisperBackbone model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/whisper/whisper_backbone.py#L23)

### `WhisperBackbone` class

Copied!

`keras_hub.models.WhisperBackbone(     vocabulary_size,     num_layers,     num_heads,     hidden_dim,     intermediate_dim,     num_mels=80,     dropout=0.0,     max_encoder_sequence_length=3000,     max_decoder_sequence_length=448,     dtype=None,     **kwargs )`

A Whisper encoder-decoder network for speech.

This class implements a Transformer-based encoder-decoder model as described in ["Robust Speech Recognition via Large-Scale Weak Supervision"](https://arxiv.org/abs/2212.04356)
. It includes the embedding lookups and transformer layers, but not the head for predicting the next token.

The default constructor gives a fully customizable, randomly initialized Whisper model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset()` constructor.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/openai/whisper)
.

**Arguments**

*   **vocabulary\_size**: int. The size of the token vocabulary.
*   **num\_layers**: int. The number of transformer encoder layers and transformer decoder layers.
*   **num\_heads**: int. The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads.
*   **hidden\_dim**: int. The size of the transformer encoding and pooler layers.
*   **intermediate\_dim**: int. The output dimension of the first Dense layer in a two-layer feedforward network for each transformer.
*   **num\_mels**: int. The number of mel-frequency filters. Defaults to `80`.
*   **dropout**: float. Dropout probability for the Transformer encoder.
*   **max\_encoder\_sequence\_length**: int. The maximum sequence length that the audio encoder can consume. Since the second convolutional layer in the encoder reduces the sequence length by half (stride of 2), we use `max_encoder_sequence_length // 2` as the sequence length for the positional embedding layer.
*   **max\_decoder\_sequence\_length**: int. The maximum sequence length that the text decoder can consume.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for model computations and weights. Note that some computations, such as softmax and layer normalization, will always be done at float32 precision regardless of dtype.

**Examples**

Copied!

`input_data = {     "encoder_features": np.ones(shape=(1, 12, 80), dtype="int32"),     "decoder_token_ids": np.ones(shape=(1, 12), dtype="int32"),     "decoder_padding_mask": np.array(         [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]     ), }  # Randomly initialized Whisper encoder-decoder model with a custom config. model = keras_hub.models.WhisperBackbone(     vocabulary_size=51864,     num_layers=4,     num_heads=4,     hidden_dim=256,     intermediate_dim=512,     max_encoder_sequence_length=128,     max_decoder_sequence_length=128, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`WhisperBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [whisper\_tiny\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_tiny_en/4) | 37.18M | 4-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_tiny\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_tiny_multi/4) | 37.76M | 4-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_base\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_base_multi/4) | 72.59M | 6-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_base\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_base_en/4) | 124.44M | 6-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_small\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_small_en/4) | 241.73M | 12-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_small\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_small_multi/4) | 241.73M | 12-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_medium\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_medium_en/4) | 763.86M | 24-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_medium\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_medium_multi/4) | 763.86M | 24-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_large\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_large_multi/4) | 1.54B | 32-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_large\_multi\_v2](https://www.kaggle.com/models/keras/whisper/keras/whisper_large_multi_v2/4) | 1.54B | 32-layer Whisper model. Trained for 2.5 epochs on 680,000 hours of labelled multilingual speech data. An improved of `whisper_large_multi`. |

* * *

[WhisperBackbone model](https://keras.io/keras_hub/api/models/whisper/whisper_backbone/#whisperbackbone-model)

[`WhisperBackbone` class](https://keras.io/keras_hub/api/models/whisper/whisper_backbone/#whisperbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/whisper/whisper_backbone/#frompreset-method)