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
 / [OPT](https://keras.io/keras_hub/api/models/opt/)
 / OPTCausalLMPreprocessor layer

OPTCausalLMPreprocessor layer
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/opt/opt_causal_lm_preprocessor.py#L7)

### `OPTCausalLMPreprocessor` class

Copied!

`keras_hub.models.OPTCausalLMPreprocessor(     tokenizer, sequence_length=1024, add_start_token=True, add_end_token=True, **kwargs )`

OPT Causal LM preprocessor.

This preprocessing layer is primarily meant to be used with [`keras_hub.models.OPTCausalLM`](https://keras.io/keras_hub/api/models/opt/opt_causal_lm#optcausallm-class)
. By default, it will take in batches of strings, and return outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence. For use with generation, pass `return_labels=False` in which case the output will simply be the encoded string features.

**Arguments**

*   **tokenizer**: A `keras_hub.models.OPTTokenizer` instance.
*   **sequence\_length**: The length of the packed inputs.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence.

**Call arguments**

*   **x**: A string, [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or list of python strings.
*   **y**: Label data. Should always be `None` as the layer generates labels.
*   **sample\_weight**: Label weights. Should always be `None` as the layer generates label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.
*   **add\_start\_token**: Pass to override the configured value of `add_start_token` on the layer.
*   **add\_end\_token**: Pass to override the configured value of `add_end_token` on the layer.
*   **return\_labels**: If `True`, the output `"token_ids"` will be offset by one and returned as labels. If `False` only features will be returned.

**Examples**

Copied!

`# Load the preprocessor from a preset. preprocessor = keras_hub.models.OPTCausalLMPreprocessor.from_preset(     "opt_125m_en" )  # Tokenize and pack a single sentence. sentence = tf.constant("League of legends") preprocessor(sentence) # Same output. preprocessor("League of legends")  # Tokenize a batch of sentences. sentences = tf.constant(["Taco tuesday", "Fish taco please!"]) preprocessor(sentences) # Same output. preprocessor(["Taco tuesday", "Fish taco please!"])  # Map a dataset to preprocess a single sentence. features = tf.constant(     [         "Avatar 2 is amazing!",         "Well, I am not sure.",     ] ) labels = tf.constant([1, 0]) ds = tf.data.Dataset.from_tensor_slices((features, labels)) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Map a dataset to preprocess unlabled sentences. ds = tf.data.Dataset.from_tensor_slices(features) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`OPTCausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [opt\_125m\_en](https://www.kaggle.com/models/keras/opt/keras/opt_125m_en/3) | 125.24M | 12-layer OPT model where case in maintained. Trained on BookCorpus, CommonCrawl, Pile, and PushShift.io corpora. |
| [opt\_1.3b\_en](https://www.kaggle.com/models/keras/opt/keras/opt_1.3b_en/3) | 1.32B | 24-layer OPT model where case in maintained. Trained on BookCorpus, CommonCrawl, Pile, and PushShift.io corpora. |
| [opt\_2.7b\_en](https://www.kaggle.com/models/keras/opt/keras/opt_2.7b_en/3) | 2.70B | 32-layer OPT model where case in maintained. Trained on BookCorpus, CommonCrawl, Pile, and PushShift.io corpora. |
| [opt\_6.7b\_en](https://www.kaggle.com/models/keras/opt/keras/opt_6.7b_en/3) | 6.70B | 32-layer OPT model where case in maintained. Trained on BookCorpus, CommonCrawl, Pile, and PushShift.io corpora. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.OPTCausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[OPTCausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/opt/opt_causal_lm_preprocessor/#optcausallmpreprocessor-layer)

[`OPTCausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/opt/opt_causal_lm_preprocessor/#optcausallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/opt/opt_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/opt/opt_causal_lm_preprocessor/#tokenizer-property)