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
 / [ESM](https://keras.io/keras_hub/api/models/esm/)
 / ESMMaskedPLMPreprocessor layer

ESMMaskedPLMPreprocessor layer
==============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/esm/esm_masked_plm_preprocessor.py#L14)

### `ESMMaskedPLMPreprocessor` class

Copied!

`keras_hub.models.ESMMaskedPLMPreprocessor(     tokenizer,     sequence_length=512,     truncate="round_robin",     mask_selection_rate=0.15,     mask_selection_length=96,     mask_token_rate=0.8,     random_token_rate=0.1,     **kwargs )`

ESM preprocessing for the masked language modeling task.

This preprocessing layer will prepare inputs for a masked language modeling task. It is primarily intended for use with the [`keras_hub.models.ESMMaskedPLM`](https://keras.io/keras_hub/api/models/esm/esm_masked_plm#esmmaskedplm-class)
 task model. Preprocessing will occur in multiple steps.

1.  Tokenize any number of input segments using the `tokenizer`.
2.  Pack the inputs together with the appropriate `"[CLS]"`, `"[SEP]"` and `"[PAD]"` tokens.
3.  Randomly select non-special tokens to mask, controlled by `mask_selection_rate`.
4.  Construct a `(x, y, sample_weight)` tuple suitable for training with a [`keras_hub.models.ESMMaskedPLM`](https://keras.io/keras_hub/api/models/esm/esm_masked_plm#esmmaskedplm-class)
     task model.

**Arguments**

*   **tokenizer**: A `keras_hub.models.ESMTokenizer` instance.
*   **sequence\_length**: int. The length of the packed inputs.
*   **truncate**: string. The algorithm to truncate a list of batched segments to fit within `sequence_length`. The value can be either `round_robin` or `waterfall`:
    *   `"round_robin"`: Available space is assigned one token at a time in a round-robin fashion to the inputs that still need some, until the limit is reached.
    *   `"waterfall"`: The allocation of the budget is done using a "waterfall" algorithm that allocates quota in a left-to-right manner and fills up the buckets until we run out of budget. It supports an arbitrary number of segments.
*   **mask\_selection\_rate**: float. The probability an input token will be dynamically masked.
*   **mask\_selection\_length**: int. The maximum number of masked tokens in a given sample.
*   **mask\_token\_rate**: float. The probability the a selected token will be replaced with the mask token.
*   **random\_token\_rate**: float. The probability the a selected token will be replaced with a random token from the vocabulary. A selected token will be left as is with probability `1 - mask_token_rate - random_token_rate`.

**Call arguments**

*   **x**: A tensor of single string sequences, or a tuple of multiple tensor sequences to be packed together. Inputs may be batched or unbatched. For single sequences, raw python inputs will be converted to tensors. For multiple sequences, pass tensors directly.
*   **y**: Label data. Should always be `None` as the layer generates labels.
*   **sample\_weight**: Label weights. Should always be `None` as the layer generates label weights.

**Examples**

Directly calling the layer on data.

Copied!

`preprocessor = keras_hub.models.ESMMaskedPLMPreprocessor.from_preset(     hf://facebook/esm2_t6_8M_UR50D )  # Tokenize and mask a single sentence. preprocessor("The quick brown fox jumped.")  # Tokenize and mask a batch of single sentences. preprocessor(["The quick brown fox jumped.", "Call me Ishmael."])  # Tokenize and mask sentence pairs. # In this case, always convert input to tensors before calling the layer. first = tf.constant(["The quick brown fox jumped.", "Call me Ishmael."]) second = tf.constant(["The fox tripped.", "Oh look, a whale."]) preprocessor((first, second))`

Mapping with [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

Copied!

``preprocessor = keras_hub.models.ESMMaskedPLMPreprocessor.from_preset(     hf://facebook/esm2_t6_8M_UR50D )  first = tf.constant(["The quick brown fox jumped.", "Call me Ishmael."]) second = tf.constant(["The fox tripped.", "Oh look, a whale."])  # Map single sentences. ds = tf.data.Dataset.from_tensor_slices(first) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Map sentence pairs. ds = tf.data.Dataset.from_tensor_slices((first, second)) # Watch out for tf.data's default unpacking of tuples here! # Best to invoke the `preprocessor` directly in this case. ds = ds.map(     lambda first, second: preprocessor(x=(first, second)),     num_parallel_calls=tf.data.AUTOTUNE, )``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`ESMMaskedPLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [esm2\_t6\_8M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t6_8M/1) | 7.41M | 6 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t12\_35M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t12_35M/1) | 33.27M | 12 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t30\_150M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t30_150M/1) | 147.73M | 30 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |
| [esm2\_t33\_650M](https://www.kaggle.com/models/keras/esm-2/keras/esm2_t33_650M/1) | 649.40M | 33 transformer layers version of the ESM-2 protein language model, trained on the UniRef50 clustered protein sequence dataset. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.ESMMaskedPLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[ESMMaskedPLMPreprocessor layer](https://keras.io/keras_hub/api/models/esm/esm_masked_plm_preprocessor/#esmmaskedplmpreprocessor-layer)

[`ESMMaskedPLMPreprocessor` class](https://keras.io/keras_hub/api/models/esm/esm_masked_plm_preprocessor/#esmmaskedplmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/esm/esm_masked_plm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/esm/esm_masked_plm_preprocessor/#tokenizer-property)