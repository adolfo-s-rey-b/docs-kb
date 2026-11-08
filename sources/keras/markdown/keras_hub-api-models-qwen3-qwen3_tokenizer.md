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
 / [Qwen3](https://keras.io/keras_hub/api/models/qwen3/)
 / Qwen3Tokenizer

Qwen3Tokenizer
==============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3/qwen3_tokenizer.py#L6)

### `Qwen3Tokenizer` class

Copied!

`keras_hub.models.Qwen3Tokenizer(vocabulary=None, merges=None, **kwargs)`

Tokenizer for Qwen3 models.

This tokenizer implements byte-pair encoding (BPE) for Qwen3 models, handling special tokens like BOS (beginning of sequence) and EOS (end of sequence).

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

`Qwen3Tokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [qwen3\_embedding\_0.6b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_0.6b_en/1) | 595.78M | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 1024. |
| [qwen3\_0.6b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_0.6b_en/1) | 596.05M | 28-layer Qwen3 model with 596M parameters, optimized for efficiency and fast inference on resource-constrained devices. |
| [harrier\_embedding\_oss\_0.6b](https://www.kaggle.com/models/keras/harrier/keras/harrier_embedding_oss_0.6b/1) | 596.05M | Microsoft harrier-oss-v1 0.6B multilingual text embedding model based on the Qwen3-0.6B architecture, fine-tuned for dense retrieval and semantic similarity across 94+ languages. Achieves 69.0 on Multilingual MTEB v2. |
| [qwen3\_1.7b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_1.7b_en/1) | 1.72B | 28-layer Qwen3 model with 1.72B parameters, offering a good balance between performance and resource usage. |
| [qwen3\_embedding\_4b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_4b_en/1) | 4.02B | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 2560. |
| [qwen3\_4b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_4b_en/1) | 4.02B | 36-layer Qwen3 model with 4.02B parameters, offering improved reasoning capabilities and better performance than smaller variants. |
| [qwen3\_embedding\_8b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_8b_en/1) | 8.19B | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 4096. |
| [qwen3\_8b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_8b_en/1) | 8.19B | 36-layer Qwen3 model with 8.19B parameters, featuring enhanced reasoning, coding, and instruction-following capabilities. |
| [qwen3\_14b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_14b_en/1) | 14.77B | 40-layer Qwen3 model with 14.77B parameters, featuring advanced reasoning, coding, and multilingual capabilities. |
| [qwen3\_32b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_32b_en/1) | 32.76B | 64-layer Qwen3 model with 32.76B parameters, featuring state-of-the-art performance across reasoning, coding, and general language tasks. |

* * *

[Qwen3Tokenizer](https://keras.io/keras_hub/api/models/qwen3/qwen3_tokenizer/#qwen3tokenizer)

[`Qwen3Tokenizer` class](https://keras.io/keras_hub/api/models/qwen3/qwen3_tokenizer/#qwen3tokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3/qwen3_tokenizer/#frompreset-method)