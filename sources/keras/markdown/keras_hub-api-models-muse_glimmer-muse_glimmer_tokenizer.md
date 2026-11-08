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
 / [MuseGlimmer](https://keras.io/keras_hub/api/models/muse_glimmer/)
 / MuseGlimmerTokenizer

MuseGlimmerTokenizer
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_tokenizer.py#L24)

### `MuseGlimmerTokenizer` class

Copied!

`keras_hub.tokenizers.MuseGlimmerTokenizer(     vocabulary=None,     merges=None,     bos_token="<|begin_of_text|>",     eos_token="<|end_of_text|>",     pad_token="<|finetune_right_pad|>",     eot_token="<|eot|>",     image_token_id=200092,     video_token_id=200091,     image_start_token="<|image_start|>",     image_end_token="<|image_end|>",     video_start_token="<|vid_start|>",     video_end_token="<|vid_end|>",     video_separator_token="<|vid_frame_separator|>",     **kwargs )`

A MuseGlimmer byte-level BPE tokenizer.

Uses the regex pre-tokenizer split from the checkpoint's `tokenizer.json`. The split separates camelCase words and keeps combining marks inside words. `image_token_id`/`video_token_id` are fixed placeholder ids (per `config.json`) that the preprocessor expands to per-patch image/video feature positions — they are not resolved from a named special-token string, since the checkpoint assigns them directly by id among its ~2,043 reserved special tokens.

**Arguments**

*   **vocabulary**: dict or None. Maps token strings to integer ids.
*   **merges**: list or None. BPE merge rules.
*   **bos\_token**: str. Beginning-of-sequence token.
*   **eos\_token**: str. End-of-sequence token.
*   **pad\_token**: str. Padding token.
*   **eot\_token**: str or `None`. End-of-turn token. `generate()` stops at this token and at `eos_token`. Defaults to `"<|eot|>"`.
*   **image\_token\_id**: int. Placeholder token id expanded to per-patch image embeddings by the preprocessor. Defaults to `200092`.
*   **video\_token\_id**: int. Placeholder token id expanded to per-frame video embeddings by the preprocessor. Defaults to `200091`.
*   **image\_start\_token**: str. Token before the image tokens. Defaults to `"<|image_start|>"`.
*   **image\_end\_token**: str. Token after the image tokens. Defaults to `"<|image_end|>"`.
*   **video\_start\_token**: str. Token before the video tokens. Defaults to `"<|vid_start|>"`.
*   **video\_end\_token**: str. Token after the video tokens. Defaults to `"<|vid_end|>"`.
*   **video\_separator\_token**: str. Token between the temporal groups of a video. Defaults to `"<|vid_frame_separator|>"`.

The five delimiter tokens follow the Hugging Face processor layout. The vocabulary must contain all of them.

**Example**

Copied!

`tokenizer = keras_hub.models.MuseGlimmerTokenizer.from_preset(     "muse_glimmer_30b" )  # Unbatched input. tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`MuseGlimmerTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [muse\_glimmer\_30b\_assistant](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b_assistant/1) | 2.56B | MuseGlimmer 30B DFlash Assistant model: 5-layer speculative-decoding drafter for the 30B model. Drafts a 16-token block-diffusion denoised block per forward pass, conditioned on the target model's hidden states. This model must NOT be used standalone. It is designed exclusively as a draft model used from the target model's generation loop. |
| [muse\_glimmer\_30b](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b/1) | 29.78B | 30B-parameter dense causal decoder with an attached windowed-attention perception encoder, distilled from Muse Spark for local agentic use. |

* * *

[MuseGlimmerTokenizer](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_tokenizer/#museglimmertokenizer)

[`MuseGlimmerTokenizer` class](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_tokenizer/#museglimmertokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_tokenizer/#frompreset-method)