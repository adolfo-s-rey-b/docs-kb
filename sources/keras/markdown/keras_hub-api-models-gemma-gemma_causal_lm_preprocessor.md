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
 / [Gemma](https://keras.io/keras_hub/api/models/gemma/)
 / GemmaCausalLMPreprocessor layer

GemmaCausalLMPreprocessor layer
===============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma/gemma_causal_lm_preprocessor.py#L7)

### `GemmaCausalLMPreprocessor` class

Copied!

`keras_hub.models.GemmaCausalLMPreprocessor(     tokenizer, sequence_length=1024, add_start_token=True, add_end_token=True, **kwargs )`

Gemma Causal LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.GemmaCausalLM`](https://keras.io/keras_hub/api/models/gemma/gemma_causal_lm#gemmacausallm-class)
. By default, it will take in batches of strings, and return outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.GemmaCausalLM`](https://keras.io/keras_hub/api/models/gemma/gemma_causal_lm#gemmacausallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.GemmaTokenizer` instance.
*   **sequence\_length**: The length of the packed inputs.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence.

**Call arguments**

*   **x**: A string, [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or list of python strings.
*   **y**: Label data. Should always be `None` as the layer generates labels.
*   **sample\_weight**: Label weights. Should always be `None` as the layer generates label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.

**Examples**

Copied!

``# Load the preprocessor from a preset. preprocessor = keras_hub.models.GemmaCausalLMPreprocessor.from_preset(     "gemma_2b_en" )  # Tokenize and pack a single sentence. preprocessor("The quick brown fox jumped.")  # Tokenize a batch of sentences. preprocessor(["The quick brown fox jumped.", "Call me Ishmael."])  # Apply tokenization to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). features = tf.constant(["The quick brown fox.", "Call me Ishmael."]) ds = tf.data.Dataset.from_tensor_slices(features) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Prepare tokens for generation (no end token). preprocessor.generate_preprocess(["The quick brown fox jumped."])  # Map generation outputs back to strings. preprocessor.generate_postprocess({     'token_ids': np.array([[2, 714, 4320, 8426, 25341, 32292, 235265, 0]]),     'padding_mask': np.array([[ 1,  1,  1,  1,  1,  1,  1, 0]]), })``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`GemmaCausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [vault\_gemma\_1b\_en](https://www.kaggle.com/models/keras/vaultgemma/keras/vault_gemma_1b_en/2) | 1.04B | 1 billion parameter, 26-layer, VaultGemma model. |
| [gemma\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_2b_en/3) | 2.51B | 2 billion parameter, 18-layer, base Gemma model. |
| [gemma\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_instruct_2b_en/3) | 2.51B | 2 billion parameter, 18-layer, instruction tuned Gemma model. |
| [gemma\_1.1\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_1.1_instruct_2b_en/4) | 2.51B | 2 billion parameter, 18-layer, instruction tuned Gemma model. The 1.1 update improves model quality. |
| [code\_gemma\_1.1\_2b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_1.1_2b_en/2) | 2.51B | 2 billion parameter, 18-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. The 1.1 update improves model quality. |
| [code\_gemma\_2b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_2b_en/2) | 2.51B | 2 billion parameter, 18-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. |
| [gemma2\_2b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, base Gemma model. |
| [gemma2\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, instruction tuned Gemma model. |
| [shieldgemma\_2b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, ShieldGemma model. |
| [c2s\_scale\_gemma\_2\_2b\_en](https://www.kaggle.com/models/keras/cell2sentence/keras/c2s_scale_gemma_2_2b_en/1) | 2.61B | A 2 billion parameter, single-cell biology-aware model built on the Gemma-2 architecture. |
| [gemma\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_7b_en/4) | 8.54B | 7 billion parameter, 28-layer, base Gemma model. |
| [gemma\_instruct\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_instruct_7b_en/4) | 8.54B | 7 billion parameter, 28-layer, instruction tuned Gemma model. |
| [gemma\_1.1\_instruct\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_1.1_instruct_7b_en/5) | 8.54B | 7 billion parameter, 28-layer, instruction tuned Gemma model. The 1.1 update improves model quality. |
| [code\_gemma\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. |
| [code\_gemma\_instruct\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_instruct_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, instruction tuned CodeGemma model. This model has been trained for chat use cases related to code. |
| [code\_gemma\_1.1\_instruct\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_1.1_instruct_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, instruction tuned CodeGemma model. This model has been trained for chat use cases related to code. The 1.1 update improves model quality. |
| [gemma2\_9b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_9b_en/4) | 9.24B | 9 billion parameter, 42-layer, base Gemma model. |
| [gemma2\_instruct\_9b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_9b_en/4) | 9.24B | 9 billion parameter, 42-layer, instruction tuned Gemma model. |
| [shieldgemma\_9b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_9b_en/2) | 9.24B | 9 billion parameter, 42-layer, ShieldGemma model. |
| [gemma2\_27b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_27b_en/3) | 27.23B | 27 billion parameter, 42-layer, base Gemma model. |
| [gemma2\_instruct\_27b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_27b_en/3) | 27.23B | 27 billion parameter, 42-layer, instruction tuned Gemma model. |
| [shieldgemma\_27b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_27b_en/2) | 27.23B | 27 billion parameter, 42-layer, ShieldGemma model. |
| [c2s\_scale\_gemma\_2\_27b\_en](https://www.kaggle.com/models/keras/cell2sentence/keras/c2s_scale_gemma_2_27b_en/1) | 27.23B | A 27 billion parameter, single-cell biology-aware model built on the Gemma-2 architecture. |

**Guides and examples using `from_preset`**

*   [Parameter-efficient fine-tuning of Gemma with LoRA and QLoRA](https://keras.io/examples/keras_recipes/parameter_efficient_finetuning_of_gemma_with_lora_and_qlora/)
    

* * *

### `tokenizer` property

Copied!

`keras_hub.models.GemmaCausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[GemmaCausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/gemma/gemma_causal_lm_preprocessor/#gemmacausallmpreprocessor-layer)

[`GemmaCausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/gemma/gemma_causal_lm_preprocessor/#gemmacausallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma/gemma_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/gemma/gemma_causal_lm_preprocessor/#tokenizer-property)