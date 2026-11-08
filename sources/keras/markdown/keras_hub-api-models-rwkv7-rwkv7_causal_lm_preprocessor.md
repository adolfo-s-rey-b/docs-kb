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
 / [RWKV7](https://keras.io/keras_hub/api/models/rwkv7/)
 / RWKV7CausalLMPreprocessor layer

RWKV7CausalLMPreprocessor layer
===============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/rwkv7/rwkv7_causal_lm_preprocessor.py#L14)

### `RWKV7CausalLMPreprocessor` class

Copied!

`keras_hub.models.RWKV7CausalLMPreprocessor(     tokenizer, add_start_token=False, **kwargs )`

RWKV-7 Causal LM preprocessor.

Copied!

``This preprocessing layer is meant for use with [`keras_hub.models.RWKV7CausalLM`](/keras_hub/api/models/rwkv7/rwkv7_causal_lm#rwkv7causallm-class). By default, it will take in batches of strings, and return outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence.  For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.RWKV7CausalLM`](/keras_hub/api/models/rwkv7/rwkv7_causal_lm#rwkv7causallm-class) instance, these methods will be called implicitly in generate(). They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).  # Arguments     tokenizer: A `keras_hub.models.RWKVTokenizer` instance.     sequence_length: The length of the packed inputs.     add_start_token: If `True`, the preprocessor will prepend the tokenizer         start token to each input sequence. Default is `False`.  # Call arguments     x: A string, [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor) or list of python strings.     y: Label data. Should always be `None` as the layer generates labels.     sample_weight: Label weights. Should always be `None` as the layer         generates label weights.     sequence_length: Pass to override the configured sequence_length of         the layer.   # Examples  ```python # Initialize the tokenizer and load assets from a local path. tokenizer = RWKVTokenizer() tokenizer.load_assets(rwkv_path)  # Create a preprocessor with a sequence length of 8. preprocessor = RWKV7CausalLMPreprocessor(tokenizer, sequence_length=8)  # Tokenize and pack a batch of sentences. preprocessor(["Bubble sort``\
\
\`\`\`python", "Hello World\
\
Copied!\
\
``"])      # Preprocess inputs for generation with a maximum generation length of 16.     preprocessor.generate_preprocess(         ["Bubble sort ```python", "Hello World ```python "], 16     )     ```  ----  <span style="float:right;">[[source]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)</span>  ### `from_preset` method  ```python RWKV7CausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )``

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
| [rwkv7\_g1a\_0.1b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.1b/1) | 150.00M | 150 million parameter RWKV7 model. Optimized for edge devices and mobile deployment. |
| [rwkv7\_g1a\_0.3b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.3b/1) | 400.00M | 400 million parameter RWKV7 model. Small variant balancing speed and instruction following. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.RWKV7CausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[RWKV7CausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm_preprocessor/#rwkv7causallmpreprocessor-layer)

[`RWKV7CausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm_preprocessor/#rwkv7causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm_preprocessor/#tokenizer-property)