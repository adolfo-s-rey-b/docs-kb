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
 / [DiffusionGemma](https://keras.io/keras_hub/api/models/diffusion_gemma/)
 / DiffusionGemmaTokenizer

DiffusionGemmaTokenizer
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/diffusion_gemma/diffusion_gemma_tokenizer.py#L8)

### `DiffusionGemmaTokenizer` class

Copied!

`keras_hub.tokenizers.DiffusionGemmaTokenizer(     proto, has_vision_tokens=True, has_audio_tokens=False, has_video_tokens=True, **kwargs )`

DiffusionGemma tokenizer based on SentencePiece.

The tokenizer converts strings to integer sequences. The tokenizer provides `from_preset()` to load a matching vocabulary.

**Arguments**

*   **proto**: A path to a SentencePiece proto file or serialized proto bytes.

**Examples**

Copied!

`tokenizer = keras_hub.models.DiffusionGemmaTokenizer.from_preset(     "diffusion_gemma_26b_a4b_it" ) tokenizer("The quick brown fox jumped.")`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`DiffusionGemmaTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

Instantiate a `keras_hub.models.Tokenizer` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Tokenizer` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Tokenizer.from_preset()`, or from a model class like `keras_hub.models.GemmaTokenizer.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a preset tokenizer. tokenizer = keras_hub.tokenizer.Tokenizer.from_preset("bert_base_en")  # Tokenize some input. tokenizer("The quick brown fox tripped.")  # Detokenize some input. tokenizer.detokenize([5, 6, 7, 8, 9])`

| Preset | Parameters | Description |
| --- | --- | --- |
| [diffusion\_gemma\_26b\_a4b\_it](https://www.kaggle.com/models/keras/diffusion-gemma/keras/diffusion_gemma_26b_a4b_it/1) | 25.82B | DiffusionGemma 26B MoE instruction-tuned model. 25.8B total parameters (3.8B active), 30 layers, 128 experts. |

* * *

[DiffusionGemmaTokenizer](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_tokenizer/#diffusiongemmatokenizer)

[`DiffusionGemmaTokenizer` class](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_tokenizer/#diffusiongemmatokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_tokenizer/#frompreset-method)