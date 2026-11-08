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
 / [MPNet](https://keras.io/keras_hub/api/models/mpnet/)
 / MPNetTextEmbedderPreprocessor layer

MPNetTextEmbedderPreprocessor layer
===================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mpnet/mpnet_text_embedder_preprocessor.py#L12)

### `MPNetTextEmbedderPreprocessor` class

Copied!

`keras_hub.models.MPNetTextEmbedderPreprocessor(     tokenizer, sequence_length=256, truncate="round_robin", **kwargs )`

An MPNet preprocessing layer which tokenizes and packs inputs for sentence embedding.

This preprocessing layer will do three things:

1.  Tokenize any number of input segments using the `tokenizer`.
2.  Pack the inputs together using a [`keras_hub.layers.MultiSegmentPacker`](https://keras.io/keras_hub/api/preprocessing_layers/multi_segment_packer#multisegmentpacker-class)
     with the appropriate `"<s>"`, `"</s>"` and `"<pad>"` tokens, i.e., adding a single `"<s>"` at the start of the entire sequence, `"</s></s>"` between segments, and a `"</s>"` at the end of the entire sequence.
3.  Construct a dictionary with keys `"token_ids"` and `"padding_mask"` that can be passed directly to an MPNet model.

This layer can be used directly with [`tf.data.Dataset.map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map)
 to preprocess string data in the `(x, y, sample_weight)` format used by [`keras.Model.fit`](https://keras.io/api/models/model_training_apis#fit-method)
.

**Arguments**

*   **tokenizer**: A `keras_hub.models.MPNetTokenizer` instance.
*   **sequence\_length**: The length of the packed inputs. Defaults to 256. When loading a HuggingFace sentence-transformer preset, this is read from `sentence_bert_config.json` (e.g. 384 for `all-mpnet-base-v2`).
*   **truncate**: string. The algorithm to truncate a list of batched segments to fit within `sequence_length`. The value can be either `round_robin` or `waterfall`:
    *   `"round_robin"`: Available space is assigned one token at a time in a round-robin fashion to the inputs that still need some, until the limit is reached.
    *   `"waterfall"`: The allocation of the budget is done using a "waterfall" algorithm that allocates quota in a left-to-right manner and fills up the buckets until we run out of budget. It supports an arbitrary number of segments.

**Call arguments**

*   **x**: A tensor of single string sequences, or a tuple of multiple tensor sequences to be packed together. Inputs may be batched or unbatched. For single sequences, raw python inputs will be converted to tensors. For multiple sequences, pass tensors directly.
*   **y**: Any label data. Will be passed through unaltered.
*   **sample\_weight**: Any label weight data. Will be passed through unaltered.

**Examples**

Directly calling the layer on data.

Copied!

`preprocessor = keras_hub.models.MPNetTextEmbedderPreprocessor.from_preset(     "all_mpnet_base_v2" )  # Tokenize and pack a single sentence. preprocessor("The quick brown fox jumped.")  # Tokenize a batch of single sentences. preprocessor(["The quick brown fox jumped.", "Call me Ishmael."])`

Mapping with [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
.

Copied!

`preprocessor = keras_hub.models.MPNetTextEmbedderPreprocessor.from_preset(     "all_mpnet_base_v2" )  first = tf.constant(["The quick brown fox jumped.", "Call me Ishmael."])  # Map unlabeled single sentences. ds = tf.data.Dataset.from_tensor_slices(first) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`MPNetTextEmbedderPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [all\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/all_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model. Maps sentences and paragraphs to 768-dimensional normalized vectors. Trained on 1B+ sentence pairs for semantic search, clustering, and similarity. |
| [nli\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/nli_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model trained on natural language inference (NLI) data. Maps sentences to 768-dimensional dense vectors that are not normalized. Inputs are truncated to 75 tokens. |
| [paraphrase\_mpnet\_base\_v2](https://www.kaggle.com/models/keras/mpnet/keras/paraphrase_mpnet_base_v2/1) | 108.89M | 12-layer MPNet sentence embedding model trained on paraphrase data. Maps sentences and paragraphs to 768-dimensional dense vectors that are not normalized, for paraphrase mining, clustering, and semantic search. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.MPNetTextEmbedderPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[MPNetTextEmbedderPreprocessor layer](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder_preprocessor/#mpnettextembedderpreprocessor-layer)

[`MPNetTextEmbedderPreprocessor` class](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder_preprocessor/#mpnettextembedderpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/mpnet/mpnet_text_embedder_preprocessor/#tokenizer-property)