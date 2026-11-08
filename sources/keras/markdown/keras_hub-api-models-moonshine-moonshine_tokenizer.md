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
 / MoonshineTokenizer

MoonshineTokenizer
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/moonshine/moonshine_tokenizer.py#L5)

### `MoonshineTokenizer` class

Copied!

`keras_hub.tokenizers.MoonshineTokenizer(proto, **kwargs)`

Moonshine tokenizer layer based on `keras_hub.models.LlamaTokenizer`.

This tokenizer class is an alias of `LlamaTokenizer` but for the Moonshine model. It uses a SentencePiece vocabulary to handle tokenization.

**Arguments**

*   **proto**: `str` or `bytes`. Either a string path to a SentencePiece proto file or a bytes object containing a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for details on the format.
*   **\*\*kwargs**: Additional keyword arguments passed to the parent `LlamaTokenizer`.

**Examples**

Copied!

`from keras_hub.tokenizers import MoonshineTokenizer  # Initialize tokenizer. tokenizer = MoonshineTokenizer(     "keras_hub/src/tests/test_data/llama_test_vocab.spm" )  # Single input example. single_input = "the quick brown fox" single_tokens = tokenizer(single_input) print("Single input tokenization:") print(f"Input text: {single_input}") print(f"Tokenized: {single_tokens}")  # Batched input example. batch_input = ["the quick brown fox", "the earth is round"] batch_tokens = tokenizer(batch_input) print("Batch input tokenization:") print(f"Input texts: {batch_input}") print(f"Tokenized: {batch_tokens}")  # Detokenization example. encoded = tokenizer(single_input) decoded = tokenizer.detokenize(encoded) print("Detokenization:") print(f"Original text: {single_input}") print(f"Encoded: {encoded}") print(f"Decoded: {decoded}")`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`MoonshineTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [llama2\_7b\_en](https://www.kaggle.com/models/keras/llama2/keras/llama2_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, base LLaMA 2 model. |
| [llama2\_instruct\_7b\_en](https://www.kaggle.com/models/keras/llama2/keras/llama2_instruct_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, instruction tuned LLaMA 2 model. |
| [vicuna\_1.5\_7b\_en](https://www.kaggle.com/models/keras/vicuna/keras/vicuna_1.5_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, instruction tuned Vicuna v1.5 model. |
| [llama2\_7b\_en\_int8](https://www.kaggle.com/models/keras/llama2/keras/llama2_7b_en_int8/2) | 6.74B | 7 billion parameter, 32-layer, base LLaMA 2 model with activation and weights quantized to int8. |
| [llama2\_instruct\_7b\_en\_int8](https://www.kaggle.com/models/keras/llama2/keras/llama2_instruct_7b_en_int8/2) | 6.74B | 7 billion parameter, 32-layer, instruction tuned LLaMA 2 model with activation and weights quantized to int8. |
| [llama3.2\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_1b/1) | 1.50B | 1 billion parameter, 16-layer, based LLaMA 3.2 model. |
| [llama3.2\_instruct\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_instruct_1b/1) | 1.50B | 1 billion parameter, 16-layer, instruction tuned LLaMA 3.2. |
| [llama3.2\_guard\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_guard_1b/1) | 1.50B | 1 billion parameter, 16-layer, based LLaMA 3.2 model fine-tuned for consent safety classification. |
| [llama3.2\_3b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_3b/1) | 3.61B | 3 billion parameter, 26-layer, based LLaMA 3.2 model. |
| [llama3.2\_instruct\_3b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_instruct_3b/1) | 3.61B | 3 billion parameter, 28-layer, instruction tuned LLaMA 3.2. |
| [llama3\_8b\_en](https://www.kaggle.com/models/keras/llama3/keras/llama3_8b_en/5) | 8.03B | 8 billion parameter, 32-layer, base LLaMA 3 model. |
| [llama3\_instruct\_8b\_en](https://www.kaggle.com/models/keras/llama3/keras/llama3_instruct_8b_en/5) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3 model. |
| [llama3.1\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_8b/2) | 8.03B | 8 billion parameter, 32-layer, based LLaMA 3.1 model. |
| [llama3.1\_instruct\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_instruct_8b/2) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3.1. |
| [llama3.1\_guard\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_guard_8b/2) | 8.03B | 8 billion parameter, 32-layer, LLaMA 3.1 fine-tuned for consent safety classification. |
| [llama3\_8b\_en\_int8](https://www.kaggle.com/models/keras/llama3/keras/llama3_8b_en_int8/2) | 8.03B | 8 billion parameter, 32-layer, base LLaMA 3 model with activation and weights quantized to int8. |
| [llama3\_instruct\_8b\_en\_int8](https://www.kaggle.com/models/keras/llama3/keras/llama3_instruct_8b_en_int8/2) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3 model with activation and weights quantized to int8. |

* * *

[MoonshineTokenizer](https://keras.io/keras_hub/api/models/moonshine/moonshine_tokenizer/#moonshinetokenizer)

[`MoonshineTokenizer` class](https://keras.io/keras_hub/api/models/moonshine/moonshine_tokenizer/#moonshinetokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/moonshine/moonshine_tokenizer/#frompreset-method)