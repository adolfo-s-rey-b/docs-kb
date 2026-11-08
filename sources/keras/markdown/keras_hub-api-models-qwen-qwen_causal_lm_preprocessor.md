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
 / QwenCausalLMPreprocessor layer

QwenCausalLMPreprocessor layer
==============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen/qwen_causal_lm_preprocessor.py#L7)

### `QwenCausalLMPreprocessor` class

Copied!

`keras_hub.models.QwenCausalLMPreprocessor()`

Qwen Causal LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.QwenCausalLM`](https://keras.io/keras_hub/api/models/qwen/qwen_causal_lm#qwencausallm-class)
. By default, it will take in batches of strings, and return outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.QwenCausalLM`](https://keras.io/keras_hub/api/models/qwen/qwen_causal_lm#qwencausallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.QwenTokenizer` instance.
*   **sequence\_length**: The length of the packed inputs.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence. Default is `True`.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence. Default is `False`.

**Call arguments**

*   **x**: A string, [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or list of python strings.
*   **y**: Label data. Should always be `None` as the layer generates labels.
*   **sample\_weight**: Label weights. Should always be `None` as the layer generates label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.

**Examples**

Copied!

`# Load the preprocessor from a preset. preprocessor = keras_hub.models.QwenCausalLMPreprocessor.from_preset(     "qwen2.5_0.5b_en" )  # Tokenize and pack a single sentence. sentence = tf.constant("League of legends") preprocessor(sentence) # Same output. preprocessor("League of legends")  # Tokenize a batch of sentences. sentences = tf.constant(["Taco tuesday", "Fish taco please!"]) preprocessor(sentences) # Same output. preprocessor(["Taco tuesday", "Fish taco please!"])  # Map a dataset to preprocess a single sentence. features = tf.constant(     [         "Avatar 2 is amazing!",         "Well, I am not sure.",     ] ) labels = tf.constant([1, 0]) ds = tf.data.Dataset.from_tensor_slices((features, labels)) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Map a dataset to preprocess unlabled sentences. ds = tf.data.Dataset.from_tensor_slices(features) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`QwenCausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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

### `tokenizer` property

Copied!

`keras_hub.models.QwenCausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[QwenCausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/qwen/qwen_causal_lm_preprocessor/#qwencausallmpreprocessor-layer)

[`QwenCausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/qwen/qwen_causal_lm_preprocessor/#qwencausallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen/qwen_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/qwen/qwen_causal_lm_preprocessor/#tokenizer-property)