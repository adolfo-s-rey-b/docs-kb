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
 / [Mistral3](https://keras.io/keras_hub/api/models/mistral3/)
 / Mistral3Tokenizer

Mistral3Tokenizer
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mistral3/mistral3_tokenizer.py#L26)

### `Mistral3Tokenizer` class

Copied!

`keras_hub.tokenizers.Mistral3Tokenizer(     vocabulary=None, merges=None, split_pattern=None, control_tokens=None, **kwargs )`

Mistral3 Tekken tokenizer layer based on byte-level BPE.

Handles Mistral3's Tekken (tiktoken-style byte-level BPE) vocabulary. It is based on [`keras_hub.tokenizers.BytePairTokenizer`](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer#bytepairtokenizer-class)
, uses the Tekken pre-tokenization regex instead of the GPT-2/Llama3 pattern hardcoded in the base class, and registers the special image tokens (`"[IMG]"`, `"[IMG_BREAK]"`, `"[IMG_END]"`) used by multimodal Mistral3/Pixtral models to mark image placeholder positions in a prompt.

Not a subclass of `keras_hub.models.MistralTekkenTokenizer`: that class builds its `unsplittable_tokens` list inline in `__init__` before calling the `BytePairTokenizer` constructor, which doesn't leave a clean extension point for adding the vision tokens via inheritance.

The `vocabulary` and `merges` are usually produced from a `tekken.json` file by the Hugging Face conversion path; see `keras_hub.src.utils.transformers.convert_mistral3`.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **vocabulary**: A dict mapping token strings to integer ids, or a path to a vocabulary JSON file.
*   **merges**: A list of BPE merge rules, or a path to a merges file.
*   **split\_pattern**: str, optional. The Tekken pre-tokenization regex. Defaults to the pattern shared by known Mistral3 checkpoints.
*   **control\_tokens**: list of str, optional. Extra reserved control tokens (e.g. `"[INST]"`) to register as unsplittable, in addition to the start/end/vision tokens. Defaults to `None`.

**Examples**

Copied!

`tokenizer = keras_hub.models.Mistral3Tokenizer.from_preset(     "hf://mistralai/Mistral-Small-3.2-24B-Instruct-2506", ) tokenizer("The quick brown fox jumped.") tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`Mistral3Tokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [ministral\_3\_3b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_base_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_instruct_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_reasoning_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [shieldstral\_1.0\_3b\_en](https://www.kaggle.com/models/keras/shieldstral/keras/shieldstral_1.0_3b_en/1) | 3.85B | 3 billion parameter, 26-layer Shieldstral model with a Pixtral vision encoder. The model checks text and image content against a safety policy written in natural language. The model returns one safety score for each input. |
| [ministral\_3\_8b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_base_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_instruct_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_reasoning_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_base_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_instruct_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_reasoning_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_base\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_base_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, pretrained Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_instruct\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_instruct_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.2\_24b\_instruct\_2506\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.2_24b_instruct_2506_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. An updated version of mistral\_small\_3.1\_24b\_instruct\_2503\_en with improved instruction-following and reduced repetition. |
| [devstral\_small\_2\_24b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/devstral2/keras/devstral_small_2_24b_instruct_2512_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Devstral Small 2 model for agentic software engineering, with a Pixtral vision encoder for image input. |
| [magistral\_small\_2509\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2509_en/1) | 24.01B | 24 billion parameter, 40-layer, reasoning-tuned Magistral Small model with a Pixtral vision encoder for image input. |

* * *

[Mistral3Tokenizer](https://keras.io/keras_hub/api/models/mistral3/mistral3_tokenizer/#mistral3tokenizer)

[`Mistral3Tokenizer` class](https://keras.io/keras_hub/api/models/mistral3/mistral3_tokenizer/#mistral3tokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mistral3/mistral3_tokenizer/#frompreset-method)