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
 / [Qwen3Moe](https://keras.io/keras_hub/api/models/qwen3_moe/)
 / Qwen3MoeTokenizer

Qwen3MoeTokenizer
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3_moe/qwen3_moe_tokenizer.py#L6)

### `Qwen3MoeTokenizer` class

Copied!

`keras_hub.tokenizers.Qwen3MoeTokenizer(vocabulary=None, merges=None, **kwargs)`

Tokenizer for Qwen Moe model.

This tokenizer implements byte-pair encoding (BPE) for Qwen models, handling special tokens like BOS (beginning of sequence) and EOS (end of sequence).

**Arguments**

*   **vocabulary**: Dictionary mapping tokens to token IDs, or path to vocabulary file.
*   **merges**: List of BPE merges, or path to merges file.
*   **bos\_token**: Beginning of sequence token. Defaults to None.
*   **eos\_token**: End of sequence token. Defaults to "<|endoftext|>".
*   **misc\_special\_tokens**: Set of additional special tokens. Defaults to empty set.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`Qwen3MoeTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [qwen3\_moe\_30b\_a3b\_en](https://www.kaggle.com/models/keras/qwen-3-moe/keras/qwen3_moe_30b_a3b_en/2) | 30.53B | Mixture-of-Experts (MoE) model has 30.5 billion total parameters with 3.3 billion activated, built on 48 layers and utilizes 32 query and 4 key/value attention heads with 128 experts (8 active). |
| [qwen3\_coder\_instruct\_30b\_a3b\_en](https://www.kaggle.com/models/keras/qwen3-coder/keras/qwen3_coder_instruct_30b_a3b_en/1) | 30.53B | A Code-Specific Model,Mixture-of-Experts (MoE) model has 30.5 billion total parameters with 3.3 billion activated, built on 48 layers and utilizes 32 query and 4 key/value attention heads with 128 experts (8 active). |
| [qwen3\_moe\_235b\_a22b\_en](https://www.kaggle.com/models/keras/qwen-3-moe/keras/qwen3_moe_235b_a22b_en/1) | 235.09B | Mixture-of-Experts (MoE) model has 235 billion total parameters with 22 billion activated, built on 94 layers and utilizes 64 query and 4 key/value attention heads with 128 experts (8 active). |

* * *

[Qwen3MoeTokenizer](https://keras.io/keras_hub/api/models/qwen3_moe/qwen3_moe_tokenizer/#qwen3moetokenizer)

[`Qwen3MoeTokenizer` class](https://keras.io/keras_hub/api/models/qwen3_moe/qwen3_moe_tokenizer/#qwen3moetokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3_moe/qwen3_moe_tokenizer/#frompreset-method)