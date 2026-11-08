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
 / [XLMRoberta](https://keras.io/keras_hub/api/models/xlm_roberta/)
 / XLMRobertaMaskedLMPreprocessor layer

XLMRobertaMaskedLMPreprocessor layer
====================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/xlm_roberta/xlm_roberta_masked_lm_preprocessor.py#L16)

### `XLMRobertaMaskedLMPreprocessor` class

Copied!

`keras_hub.models.XLMRobertaMaskedLMPreprocessor(     tokenizer,     sequence_length=512,     truncate="round_robin",     mask_selection_rate=0.15,     mask_selection_length=96,     mask_token_rate=0.8,     random_token_rate=0.1,     **kwargs )`

XLM-RoBERTa preprocessing for the masked language modeling task.

This preprocessing layer will prepare inputs for a masked language modeling task. It is primarily intended for use with the [`keras_hub.models.XLMRobertaMaskedLM`](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm#xlmrobertamaskedlm-class)
 task model. Preprocessing will occur in multiple steps.

1.  Tokenize any number of input segments using the `tokenizer`.
2.  Pack the inputs together with the appropriate `"<s>"`, `"</s>"` and `"<pad>"` tokens, i.e., adding a single `"<s>"` at the start of the entire sequence, `"</s></s>"` between each segment, and a `"</s>"` at the end of the entire sequence.
3.  Randomly select non-special tokens to mask, controlled by `mask_selection_rate`.
4.  Construct a `(x, y, sample_weight)` tuple suitable for training with a [`keras_hub.models.XLMRobertaMaskedLM`](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm#xlmrobertamaskedlm-class)
     task model.

**Arguments**

*   **tokenizer**: A `keras_hub.models.XLMRobertaTokenizer` instance.
*   **sequence\_length**: int. The length of the packed inputs.
*   **truncate**: string. The algorithm to truncate a list of batched segments to fit within `sequence_length`. The value can be either `round_robin` or `waterfall`: - `"round_robin"`: Available space is assigned one token at a time in a round-robin fashion to the inputs that still need some, until the limit is reached. - `"waterfall"`: The allocation of the budget is done using a "waterfall" algorithm that allocates quota in a left-to-right manner and fills up the buckets until we run out of budget. It supports an arbitrary number of segments.
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

`# Load the preprocessor from a preset. preprocessor = keras_hub.models.XLMRobertaMaskedLMPreprocessor.from_preset(     "xlm_roberta_base_multi" )  # Tokenize and mask a single sentence. preprocessor("The quick brown fox jumped.") # Tokenize and mask a batch of single sentences. preprocessor(["The quick brown fox jumped.", "Call me Ishmael."]) # Tokenize and mask sentence pairs. # In this case, always convert input to tensors before calling the layer. first = tf.constant(["The quick brown fox jumped.", "Call me Ishmael."]) second = tf.constant(["The fox tripped.", "Oh look, a whale."]) preprocessor((first, second))`

Mapping with [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

Copied!

``preprocessor = keras_hub.models.XLMRobertaMaskedLMPreprocessor.from_preset(     "xlm_roberta_base_multi" ) first = tf.constant(["The quick brown fox jumped.", "Call me Ishmael."]) second = tf.constant(["The fox tripped.", "Oh look, a whale."])  # Map single sentences. ds = tf.data.Dataset.from_tensor_slices(first) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Map sentence pairs. ds = tf.data.Dataset.from_tensor_slices((first, second)) # Watch out for tf.data's default unpacking of tuples here! # Best to invoke the `preprocessor` directly in this case. ds = ds.map(     lambda first, second: preprocessor(x=(first, second)),     num_parallel_calls=tf.data.AUTOTUNE, )``

Copied!

``----  <span style="float:right;">[[source]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)</span>  ### `from_preset` method   ```python XLMRobertaMaskedLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )``

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
| [xlm\_roberta\_base\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_base_multi/3) | 277.45M | 12-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_base](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_base/1) | 277.45M | 12-layer multilingual E5 embedding model with 768-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [xlm\_roberta\_large\_multi](https://www.kaggle.com/models/keras/xlm_roberta/keras/xlm_roberta_large_multi/3) | 558.84M | 24-layer XLM-RoBERTa model where case is maintained. Trained on CommonCrawl in 100 languages. |
| [multilingual\_e5\_large](https://www.kaggle.com/models/keras/multilingual-e5/keras/multilingual_e5_large/1) | 558.84M | 24-layer multilingual E5 embedding model with 1024-dimensional vectors. Fine-tuned for dense retrieval across 100+ languages using weakly-supervised contrastive pre-training. Prefix inputs with 'query: ' for queries and 'passage: ' for documents. |
| [bge\_m3](https://www.kaggle.com/models/keras/bge/keras/bge_m3/1) | 566.70M | 568M-parameter multilingual text embedding model supporting 100+ languages with sequences up to 8192 tokens. Uses CLS token pooling with L2 normalization. Supports dense, sparse, and multi-vector (ColBERT-style) retrieval. From BAAI. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.XLMRobertaMaskedLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[XLMRobertaMaskedLMPreprocessor layer](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm_preprocessor/#xlmrobertamaskedlmpreprocessor-layer)

[`XLMRobertaMaskedLMPreprocessor` class](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm_preprocessor/#xlmrobertamaskedlmpreprocessor-class)

[Load a preprocessor for Gemma generation.](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm_preprocessor/#load-a-preprocessor-for-gemma-generation)

[Load a preprocessor for Bert classification.](https://keras.io/keras_hub/api/models/xlm_roberta/xlm_roberta_masked_lm_preprocessor/#load-a-preprocessor-for-bert-classification)