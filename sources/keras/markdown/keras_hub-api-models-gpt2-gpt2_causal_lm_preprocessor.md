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
 / [GPT2](https://keras.io/keras_hub/api/models/gpt2/)
 / GPT2CausalLMPreprocessor layer

GPT2CausalLMPreprocessor layer
==============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gpt2/gpt2_causal_lm_preprocessor.py#L7)

### `GPT2CausalLMPreprocessor` class

Copied!

`keras_hub.models.GPT2CausalLMPreprocessor(     tokenizer, sequence_length=1024, add_start_token=True, add_end_token=True, **kwargs )`

GPT2 Causal LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.GPT2CausalLM`](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm#gpt2causallm-class)
. By default, it will take in batches of strings, and return outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.GPT2CausalLM`](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm#gpt2causallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.GPT2Tokenizer` instance.
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

`# Load the preprocessor from a preset. preprocessor = keras_hub.models.GPT2CausalLMPreprocessor.from_preset(     "gpt2_base_en" )  # Tokenize and pack a single sentence. sentence = tf.constant("League of legends") preprocessor(sentence) # Same output. preprocessor("League of legends")  # Tokenize a batch of sentences. sentences = tf.constant(["Taco tuesday", "Fish taco please!"]) preprocessor(sentences) # Same output. preprocessor(["Taco tuesday", "Fish taco please!"])  # Map a dataset to preprocess a single sentence. features = tf.constant(     [         "Avatar 2 is amazing!",         "Well, I am not sure.",     ] ) labels = tf.constant([1, 0]) ds = tf.data.Dataset.from_tensor_slices((features, labels)) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Map a dataset to preprocess unlabled sentences. ds = tf.data.Dataset.from_tensor_slices(features) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`GPT2CausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [gpt2\_base\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_base_en/3) | 124.44M | 12-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_base\_en\_cnn\_dailymail](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_base_en_cnn_dailymail/3) | 124.44M | 12-layer GPT-2 model where case is maintained. Finetuned on the CNN/DailyMail summarization dataset. |
| [gpt2\_medium\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_medium_en/3) | 354.82M | 24-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_large\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_large_en/3) | 774.03M | 36-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_extra\_large\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_extra_large_en/3) | 1.56B | 48-layer GPT-2 model where case is maintained. Trained on WebText. |

**Guides and examples using `from_preset`**

*   [Parameter-efficient fine-tuning of GPT-2 with LoRA](https://keras.io/examples/nlp/parameter_efficient_finetuning_of_gpt2_with_lora/)
    
*   [GPT2 Text Generation with KerasHub](https://keras.io/examples/generative/gpt2_text_generation_with_keras_hub/)
    

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm_preprocessor.py#L152)

### `generate_preprocess` method

Copied!

`GPT2CausalLMPreprocessor.generate_preprocess(x, sequence_length=None)`

Convert strings to integer token input for generation.

Similar to calling the layer for training, this method takes in strings or tensor strings, tokenizes and packs the input, and computes a padding mask masking all inputs not filled in with a padded value.

Unlike calling the layer for training, this method does not compute labels and will never append a `tokenizer.end_token_id` to the end of the sequence (as generation is expected to continue at the end of the inputted prompt).

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm_preprocessor.py#L195)

### `generate_postprocess` method

Copied!

`GPT2CausalLMPreprocessor.generate_postprocess(x)`

Convert integer token output to strings for generation.

This method reverses `generate_preprocess()`, by first removing all padding and start/end tokens, and then converting the integer sequence back to a string.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.GPT2CausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[GPT2CausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm_preprocessor/#gpt2causallmpreprocessor-layer)

[`GPT2CausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm_preprocessor/#gpt2causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm_preprocessor/#frompreset-method)

[`generate_preprocess` method](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm_preprocessor/#generatepreprocess-method)

[`generate_postprocess` method](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm_preprocessor/#generatepostprocess-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm_preprocessor/#tokenizer-property)