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
 / [Llama3](https://keras.io/keras_hub/api/models/llama3/)
 / Llama3Tokenizer

Llama3Tokenizer
===============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/llama3/llama3_tokenizer.py#L6)

### `Llama3Tokenizer` class

Copied!

`keras_hub.tokenizers.Llama3Tokenizer(     vocabulary=None,     merges=None,     bos_token="<|begin_of_text|>",     eos_token="<|end_of_text|>",     misc_special_tokens={"<|start_header_id|>", "<|end_header_id|>"},     **kwargs )`

Bype-pair encoding tokenizer layer.

This BPE tokenizer provides the same functionality as the official GPT-2 tokenizer. Given the same `vocabulary` which maps tokens to ids, and `merges` which describes BPE merge rules, it should provide the same output as OpenAI implementation (https://github.com/openai/gpt-2/blob/master/src/encoder.py). Different from OpenAI, this implementation is graph-compatible, so you can use it within a [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 pipeline.

If input is a batch of strings (rank > 0): By default, the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged. If `sequence_length` is set, the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 where all inputs have been padded or truncated to `sequence_length`. If input is a scalar string (rank == 0): By default, the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`. If `sequence_length` is set, the output will be a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 of shape `[sequence_length]`.

**Arguments**

*   **vocabulary**: string or dict, maps token to integer ids. If it is a string, it should be the file path to a json file.
*   **merges**: string or list, contains the merge rule. If it is a string, it should be the file path to merge rules. The merge rule file should have one merge rule per line.
*   **sequence\_length**: int. If set, the output will be padded or truncated to the `sequence_length`. Defaults to `None`.
*   **add\_prefix\_space**: bool. Whether to add an initial space to the input. This tokenizer is whitespace aware, and will tokenize a word with a leading space differently. Adding a prefix space to the first word will cause it to be tokenized equivalently to all subsequent words in the sequence. Defaults to `False`.
*   **unsplittable\_tokens**: list. A list of strings that will never be split during the word-level splitting applied before the byte-pair encoding. This can be used to ensure special tokens map to unique indices in the vocabulary, even if these special tokens contain splittable characters such as punctuation. Special tokens must still be included in `vocabulary`. Defaults to `None`.

**Examples**

Tokenize

Copied!

`>>> merge = ["b u", "t t", "e r", "bu tt", "butt er", "f l", "fl y"] >>> vocab = [] >>> [vocab.extend([a, b, a + b]) for a, b in [m.split(" ") for m in merge]] >>> vocab = sorted(set(vocab))  # Remove duplicates >>> vocab = dict([(token, i) for i, token in enumerate(vocab)]) >>> tokenizer = keras_hub.tokenizers.BytePairTokenizer(vocab, merge) >>> outputs = tokenizer("butterfly") >>> np.array(outputs) array([3, 8], dtype=int32) >>> seq1, seq2 = tokenizer(["butterfly", "butter"]) >>> np.array(seq1) array([3, 8]) >>> np.array(seq2) array([3]) >>> tokenizer = keras_hub.tokenizers.BytePairTokenizer( ...     vocab, merge, sequence_length=2) >>> seq1, seq2 = tokenizer(["butterfly", "butter"]) >>> np.array(seq1) array([3, 8], dtype=int32) >>> np.array(seq2) array([3, 0], dtype=int32)`

Detokenize

Copied!

`>>> tokenizer = keras_hub.tokenizers.BytePairTokenizer(vocab, merge) >>> tokenizer.detokenize([[3, 8]]) ['butterfly']`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`Llama3Tokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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

[Llama3Tokenizer](https://keras.io/keras_hub/api/models/llama3/llama3_tokenizer/#llama3tokenizer)

[`Llama3Tokenizer` class](https://keras.io/keras_hub/api/models/llama3/llama3_tokenizer/#llama3tokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/llama3/llama3_tokenizer/#frompreset-method)