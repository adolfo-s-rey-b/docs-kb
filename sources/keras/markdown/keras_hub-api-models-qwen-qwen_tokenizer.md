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
 / [Qwen](https://keras.io/keras_hub/api/models/qwen/)
 / QwenTokenizer

QwenTokenizer
=============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen/qwen_tokenizer.py#L6)

### `QwenTokenizer` class

Copied!

`keras_hub.tokenizers.QwenTokenizer(vocabulary=None, merges=None, **kwargs)`

Tokenizer for Qwen models.

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

`QwenTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [qwen2.5\_0.5b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_0.5b_en/1) | 494.03M | 24-layer Qwen model with 0.5 billion parameters. |
| [qwen2.5\_instruct\_0.5b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_0.5b_en/1) | 494.03M | Instruction fine-tuned 24-layer Qwen model with 0.5 billion parameters. |
| [qwen2.5\_coder\_0.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_0.5b/1) | 494.03M | Code-focused fine-tuned Qwen-2.5 model with 0.5 billion parameters. |
| [qwen2.5\_coder\_instruct\_0.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_0.5b/1) | 494.03M | Instruction-tuned code-focused Qwen-2.5 model with 0.5 billion parameters. |
| [qwen2.5\_coder\_1.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_1.5b/1) | 1.54B | Code-focused fine-tuned 28-layer Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_coder\_instruct\_1.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_1.5b/1) | 1.54B | Instruction-tuned code-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_math\_1.5b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_1.5b_en/1) | 1.54B | Math-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_math\_instruct\_1.5b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_instruct_1.5b_en/1) | 1.54B | Instruction-tuned math-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_3b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_3b_en/1) | 3.09B | 36-layer Qwen model with 3.1 billion parameters. |
| [qwen2.5\_coder\_3b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_3b/1) | 3.09B | Code-focused fine-tuned Qwen-2.5 model with 3 billion parameters. |
| [qwen2.5\_coder\_instruct\_3b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_3b/1) | 3.09B | Instruction-tuned code-focused Qwen-2.5 model with 3 billion parameters. |
| [qwen2.5\_7b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_7b_en/3) | 6.99B | 48-layer Qwen model with 7 billion parameters. |
| [qwen2.5\_coder\_7b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_7b/1) | 6.99B | Code-focused fine-tuned Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_coder\_instruct\_7b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_7b/1) | 6.99B | Instruction-tuned code-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_math\_7b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_7b_en/1) | 7.62B | Math-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_math\_instruct\_7b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_instruct_7b_en/1) | 7.62B | Instruction-tuned math-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_coder\_14b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_14b/1) | 14.00B | Code-focused fine-tuned Qwen-2.5 model with 14 billion parameters. |
| [qwen2.5\_coder\_instruct\_14b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_14b/1) | 14.00B | Instruction-tuned code-focused Qwen-2.5 model with 14 billion parameters. |
| [qwen2.5\_instruct\_32b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_32b_en/2) | 32.76B | Instruction fine-tuned 64-layer Qwen model with 32 billion parameters. |
| [qwen2.5\_coder\_32b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_32b/1) | 32.76B | Code-focused fine-tuned Qwen-2.5 model with 32 billion parameters. |
| [qwen2.5\_coder\_instruct\_32b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_32b/1) | 32.76B | Instruction-tuned code-focused Qwen-2.5 model with 32 billion parameters. |
| [qwen2.5\_instruct\_72b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_72b_en/2) | 72.71B | Instruction fine-tuned 80-layer Qwen model with 72 billion parameters. |

* * *

[QwenTokenizer](https://keras.io/keras_hub/api/models/qwen/qwen_tokenizer/#qwentokenizer)

[`QwenTokenizer` class](https://keras.io/keras_hub/api/models/qwen/qwen_tokenizer/#qwentokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen/qwen_tokenizer/#frompreset-method)