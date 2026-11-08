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
 / [ModernBERT](https://keras.io/keras_hub/api/models/modern_bert/)
 / ModernBertMaskedLMPreprocessor layer

ModernBertMaskedLMPreprocessor layer
====================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/modern_bert/modern_bert_masked_lm_preprocessor.py#L13)

### `ModernBertMaskedLMPreprocessor` class

Copied!

`keras_hub.models.ModernBertMaskedLMPreprocessor(     tokenizer,     sequence_length=512,     truncate="round_robin",     mask_selection_rate=0.15,     mask_selection_length=96,     mask_token_rate=0.8,     random_token_rate=0.1,     **kwargs )`

ModernBERT Masked LM preprocessor.

This preprocessor tokenizes and prepares inputs for masked language modeling with ModernBERT. The masking, packing, and serialization logic is inherited from `MaskedLMPreprocessor`.

**Arguments**

*   **tokenizer**: A `keras_hub.models.ModernBertTokenizer` instance.
*   **sequence\_length**: int. The length of the packed sequence.
*   **mask\_selection\_rate**: float. The probability of masking a token.
*   **mask\_selection\_length**: int. The maximum number of tokens to mask per sequence.
*   **mask\_token\_rate**: float. The fraction of selected tokens replaced with the mask token.
*   **random\_token\_rate**: float. The fraction of selected tokens replaced with a randomly selected token.
*   **\*\*kwargs**: Additional keyword arguments passed to `MaskedLMPreprocessor`.

**Examples**

Copied!

``import keras_hub  preprocessor = keras_hub.models.ModernBertMaskedLMPreprocessor.from_preset(     "modern_bert_base_en" )  # Tokenize and mask a single sentence. preprocessor("The quick brown fox jumped.")  # Tokenize and mask a batch of sentences. preprocessor(["The quick brown fox jumped.", "Call me Ishmael."])  # Use in a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). import tensorflow as tf  features = ["The quick brown fox jumped.", "Call me Ishmael."] ds = tf.data.Dataset.from_tensor_slices(features) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`ModernBertMaskedLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [modern\_bert\_base\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_base_en/1) | 149.01M | 22-layer ModernBERT Base encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |
| [modern\_bert\_embed\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/modern_bert_embed_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Nomic AI (nomic-ai/modernbert-embed-base). Produces 768-dimensional, L2-normalized, mean-pooled embeddings for inputs of up to 8192 tokens. Prefix queries with 'search\_query: ' and documents with 'search\_document: '. |
| [gte\_modern\_bert\_base](https://www.kaggle.com/models/keras/modernbert-embedding/keras/gte_modern_bert_base/1) | 149.01M | 22-layer ModernBERT Base sentence embedding model from Alibaba-NLP (Alibaba-NLP/gte-modernbert-base). Produces 768-dimensional \[CLS\]-pooled embeddings that are not normalized, so compare them with cosine similarity. The model supports inputs of up to 8192 tokens. |
| [modern\_bert\_large\_en](https://www.kaggle.com/models/keras/modernbert/keras/modern_bert_large_en/1) | 394.78M | 28-layer ModernBERT Large encoder model pretrained on English for masked language modeling. Uses Rotary Position Embeddings (RoPE), alternating local and global attention, and GeGLU feedforward layers. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.ModernBertMaskedLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[ModernBertMaskedLMPreprocessor layer](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm_preprocessor/#modernbertmaskedlmpreprocessor-layer)

[`ModernBertMaskedLMPreprocessor` class](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm_preprocessor/#modernbertmaskedlmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/modern_bert/modern_bert_masked_lm_preprocessor/#tokenizer-property)