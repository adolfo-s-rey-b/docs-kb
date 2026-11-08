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
 / MoonshineAudioToTextPreprocessor layer

MoonshineAudioToTextPreprocessor layer
======================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/moonshine/moonshine_audio_to_text_preprocessor.py#L16)

### `MoonshineAudioToTextPreprocessor` class

Copied!

`keras_hub.models.MoonshineAudioToTextPreprocessor(     audio_converter, tokenizer, decoder_sequence_length=1024, **kwargs )`

Moonshine Seq2Seq LM preprocessor for audio-to-text tasks.

This preprocessor converts raw audio and text inputs into a format suitable for the `MoonshineAudioToText` model. It processes audio waveforms using `MoonshineAudioConverter` for basic preprocessing (padding, normalization) and tokenizes text using `MoonshineTokenizer` for the decoder. It supports training and generation.

**Arguments**

*   **audio\_converter**: A `MoonshineAudioConverter` instance to process audio.
*   **tokenizer**: A `MoonshineTokenizer` instance to tokenize text.
*   **decoder\_sequence\_length**: int, optional. Maximum length for decoder token sequences. Defaults to 1024.
*   **\*\*kwargs**: Additional keyword arguments for the parent class.

**Examples**

Copied!

`import keras from keras_hub.layers import MoonshineAudioConverter from keras_hub.models import MoonshineTokenizer  # Create audio converter and tokenizer instances. audio_converter = MoonshineAudioConverter() tokenizer = MoonshineTokenizer.from_preset("moonshine_base")  # Initialize the preprocessor. preprocessor = keras_hub.models.MoonshineAudioToTextPreprocessor(     audio_converter=audio_converter,     tokenizer=tokenizer,     decoder_sequence_length=8 )  # Prepare input data (audio tensor and text). inputs = {     "audio": keras.random.normal((1, 16000)),     "text": ["the quick brown fox"] }  # Process the inputs for training. x, y, sample_weight = preprocessor(inputs)  # Check output keys and shapes (shapes depend on padding/truncation). print(x.keys()) # dict_keys(['encoder_input_values', 'encoder_padding_mask', # 'decoder_token_ids', 'decoder_padding_mask']). print(x["encoder_input_values"].shape) # e.g., (1, 16000, 1) / padded length print(x["encoder_padding_mask"].shape) # e.g., (1, 16000) or padded length print(x["decoder_token_ids"].shape) # (1, 8) print(x["decoder_padding_mask"].shape) # (1, 8) print(y.shape) # (1, 8) - Labels print(sample_weight.shape) # (1, 8) - Sample weights  # Process inputs for generation. gen_inputs = preprocessor.generate_preprocess(inputs) print(gen_inputs.keys()) # dict_keys(['encoder_input_values', 'encoder_padding_mask', # 'decoder_token_ids', 'decoder_padding_mask']).`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`MoonshineAudioToTextPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

Instantiate a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Preprocessor` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

As there are usually multiple preprocessing classes for a given model, this method should be called on a specific subclass like `keras_hub.models.BertTextClassifierPreprocessor.from_preset()`.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a preprocessor for Gemma generation. preprocessor = keras_hub.models.CausalLMPreprocessor.from_preset(     "gemma_2b_en", )  # Load a preprocessor for Bert classification. preprocessor = keras_hub.models.TextClassifierPreprocessor.from_preset(     "bert_base_en", )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [moonshine\_tiny\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_tiny_en/1) | 27.09M | Moonshine tiny model for English speech recognition. Developed by Useful Sensors for real-time transcription. |
| [moonshine\_base\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_base_en/1) | 61.51M | Moonshine base model for English speech recognition. Developed by Useful Sensors for real-time transcription. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.MoonshineAudioToTextPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[MoonshineAudioToTextPreprocessor layer](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text_preprocessor/#moonshineaudiototextpreprocessor-layer)

[`MoonshineAudioToTextPreprocessor` class](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text_preprocessor/#moonshineaudiototextpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text_preprocessor/#tokenizer-property)