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
 / [GPT-OSS](https://keras.io/keras_hub/api/models/gpt_oss/)
 / GptOssCausalLMPreprocessor layer

GptOssCausalLMPreprocessor layer
================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gpt_oss/gpt_oss_causal_lm_preprocessor.py#L7)

### `GptOssCausalLMPreprocessor` class

Copied!

`keras_hub.models.GptOssCausalLMPreprocessor(     tokenizer, sequence_length=1024, add_start_token=True, add_end_token=True, **kwargs )`

GptOss Causal LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.GptOssCausalLM`](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm#gptosscausallm-class)
. By default, it will take in batches of strings, and return outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.GptOssCausalLM`](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm#gptosscausallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.GptOssTokenizer` instance.
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

`import tensorflow as tf import keras_hub  # Load the preprocessor from a preset. preprocessor = keras_hub.models.GptOssCausalLMPreprocessor.from_preset(     "gpt_oss_base_en" )  # Tokenize and pack a single sentence. sentence = tf.constant("League of legends") preprocessor(sentence) # Same output. preprocessor("League of legends")  # Tokenize a batch of sentences. sentences = tf.constant(["Taco tuesday", "Fish taco please!"]) preprocessor(sentences) # Same output. preprocessor(["Taco tuesday", "Fish taco please!"])  # Map a dataset to preprocess a single sentence. features = tf.constant(     [         "Avatar 2 is amazing!",         "Well, I am not sure.",     ] ) labels = tf.constant([1, 0]) ds = tf.data.Dataset.from_tensor_slices((features, labels)) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Map a dataset to preprocess unlabled sentences. ds = tf.data.Dataset.from_tensor_slices(features) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`GptOssCausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [gpt\_oss\_20b\_en](https://www.kaggle.com/models/keras/gpt-oss/keras/gpt_oss_20b_en/1) | 20.91B | This preset has 21 billion total parameters, with 3.6 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [gpt\_oss\_safeguard\_20b\_en](https://www.kaggle.com/models/keras/gpt-oss-safeguard/keras/gpt_oss_safeguard_20b_en/1) | 20.91B | Open-weight safety reasoning model with 21 billion total parameters,with 3.6 billion active parameters, a context length of over 128k, and is de-quantized from MXFP4. |
| [gpt\_oss\_120b\_en](https://www.kaggle.com/models/keras/gpt-oss/keras/gpt_oss_120b_en/1) | 116.83B | This preset has 117 billion total parameters, with 5.1 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [gpt\_oss\_safeguard\_120b\_en](https://www.kaggle.com/models/keras/gpt-oss-safeguard/keras/gpt_oss_safeguard_120b_en/1) | 116.83B | Open-weight safety reasoning model with 117 billion total parameters,with 5.1 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.GptOssCausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[GptOssCausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm_preprocessor/#gptosscausallmpreprocessor-layer)

[`GptOssCausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm_preprocessor/#gptosscausallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm_preprocessor/#tokenizer-property)