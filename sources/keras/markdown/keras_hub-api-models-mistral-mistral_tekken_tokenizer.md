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
 / [Mistral](https://keras.io/keras_hub/api/models/mistral/)
 / MistralTekkenTokenizer

MistralTekkenTokenizer
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mistral/mistral_tokenizer.py#L79)

### `MistralTekkenTokenizer` class

Copied!

`keras_hub.tokenizers.MistralTekkenTokenizer(     vocabulary=None, merges=None, split_pattern=None, **kwargs )`

Mistral Tekken tokenizer layer based on byte-level BPE.

This tokenizer class handles Mistral's Tekken (tiktoken-style byte-level BPE) vocabulary, used by presets such as Magistral. It is based on [`keras_hub.tokenizers.BytePairTokenizer`](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer#bytepairtokenizer-class)
, but uses the Tekken pre-tokenization regex instead of the GPT-2/Llama3 pattern hardcoded in the base class, and checks for the special tokens needed by Mistral models.

The `vocabulary` and `merges` are usually produced from a `tekken.json` file by the Hugging Face conversion path; see `keras_hub.src.utils.transformers.convert_mistral`.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **vocabulary**: A dict mapping token strings to integer ids, or a path to a vocabulary JSON file.
*   **merges**: A list of BPE merge rules, or a path to a merges file.
*   **split\_pattern**: str. The Tekken pre-tokenization regex.

**Examples**

Copied!

`tokenizer = keras_hub.models.MistralTekkenTokenizer.from_preset(     "hf://mistralai/Magistral-Small-2506", ) tokenizer("The quick brown fox jumped.") tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`MistralTekkenTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [mistral\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_7b_en/8) | 7.24B | Mistral 7B base model |
| [mistral\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_instruct_7b_en/8) | 7.24B | Mistral 7B instruct model |
| [mistral\_0.2\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.2_instruct_7b_en/3) | 7.24B | Mistral 7B instruct version 0.2 model |
| [mistral\_0.3\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.3_7b_en/1) | 7.25B | Mistral 7B base version 0.3 model |
| [mistral\_0.3\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.3_instruct_7b_en/1) | 7.25B | Mistral 7B instruct version 0.3 model |
| [magistral\_small\_2506\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2506_en/1) | 23.57B | Magistral Small 2506 model |
| [magistral\_small\_2507\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2507_en/1) | 23.57B | Magistral Small 2507 model |

* * *

[MistralTekkenTokenizer](https://keras.io/keras_hub/api/models/mistral/mistral_tekken_tokenizer/#mistraltekkentokenizer)

[`MistralTekkenTokenizer` class](https://keras.io/keras_hub/api/models/mistral/mistral_tekken_tokenizer/#mistraltekkentokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mistral/mistral_tekken_tokenizer/#frompreset-method)