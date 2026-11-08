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
 / [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 / Seq2SeqLMPreprocessor

Seq2SeqLMPreprocessor
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/seq_2_seq_lm_preprocessor.py#L11)

### `Seq2SeqLMPreprocessor` class

Copied!

`keras_hub.models.Seq2SeqLMPreprocessor(     tokenizer, encoder_sequence_length=1024, decoder_sequence_length=1024, **kwargs )`

Base class for seq2seq language modeling preprocessing layers.

`Seq2SeqLMPreprocessor` tasks wrap a `keras_hub.tokenizer.Tokenizer` to create a preprocessing layer for seq2seq language modeling tasks. It is intended to be paired with a `keras.models.Seq2SeqLM` task.

All `Seq2SeqLMPreprocessor` layers take inputs a dictionary input with keys `"encoder_text"` and `"decoder_text"`.

This layer will always output a `(x, y, sample_weight)` tuple, where `x` is a dictionary with the tokenized inputs, `y` contains the tokens from `x` offset by 1, and `sample_weight` marks where `y` contains padded values. The exact contents of `x` will vary depending on the model being used.

a `Seq2SeqLMPreprocessor` contains two extra methods, `generate_preprocess` and `generate_postprocess` for use with generation. See examples below.

All `Seq2SeqLMPreprocessor` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and vocabularies. You can call the `from_preset()` constructor directly on this base class, in which case the correct class for you model will be automatically instantiated.

Examples.

Copied!

``preprocessor = keras_hub.models.Seq2SeqLMPreprocessor.from_preset(     "bart_base_en",     encoder_sequence_length=256,     decoder_sequence_length=256, )  # Tokenize, mask and pack a single sentence. x = {     "encoder_text": "The fox was sleeping.",     "decoder_text": "The fox was awake.", } x, y, sample_weight = preprocessor(x)  # Tokenize and pad/truncate a batch of labeled sentences. x = {     "encoder_text": ["The fox was sleeping."],     "decoder_text": ["The fox was awake."], x, y, sample_weight = preprocessor(x)  # With a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). ds = tf.data.Dataset.from_tensor_slices(x) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Generate preprocess and postprocess. x = preprocessor.generate_preprocess(x)  # Tokenized numeric inputs. x = preprocessor.generate_postprocess(x)  # Detokenized string outputs.``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`Seq2SeqLMPreprocessor.from_preset(preset, config_file="preprocessor.json", **kwargs)`

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
| [bart\_base\_en](https://www.kaggle.com/models/keras/bart/keras/bart_base_en/3) | 139.42M | 6-layer BART model where case is maintained. Trained on BookCorpus, English Wikipedia and CommonCrawl. |
| [bart\_large\_en](https://www.kaggle.com/models/keras/bart/keras/bart_large_en/3) | 406.29M | 12-layer BART model where case is maintained. Trained on BookCorpus, English Wikipedia and CommonCrawl. |
| [bart\_large\_en\_cnn](https://www.kaggle.com/models/keras/bart/keras/bart_large_en_cnn/3) | 406.29M | The `bart_large_en` backbone model fine-tuned on the CNN+DM summarization dataset. |
| [blip2\_opt\_2.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_2.7b/1) | 3.74B | BLIP-2 model using OPT-2.7B as the frozen language model. |
| [blip2\_flan\_t5\_xl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xl/1) | 3.94B | BLIP-2 model using Flan-T5-XL (~3B) as the frozen language model. |
| [blip2\_opt\_6.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_6.7b/1) | 7.75B | BLIP-2 model using OPT-6.7B as the frozen language model. |
| [blip2\_flan\_t5\_xxl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xxl/1) | 12.23B | BLIP-2 model using Flan-T5-XXL (~11B) as the frozen language model. |
| [moonshine\_tiny\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_tiny_en/1) | 27.09M | Moonshine tiny model for English speech recognition. Developed by Useful Sensors for real-time transcription. |
| [moonshine\_base\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_base_en/1) | 61.51M | Moonshine base model for English speech recognition. Developed by Useful Sensors for real-time transcription. |
| [t5\_small\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_small_multi/3) | 60.51M | 6-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_small](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_small/2) | 60.51M |     |
| [flan\_small\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_small_multi/3) | 76.96M | 8-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_base\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_base_multi/3) | 222.90M | 12-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_base](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_base/2) | 247.58M |     |
| [flan\_base\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_base_multi/3) | 247.58M | 12-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_large\_multi](https://www.kaggle.com/models/keras/t5/keras/t5_large_multi/3) | 737.67M | 24-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_large](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_large/2) | 750.25M |     |
| [flan\_large\_multi](https://www.kaggle.com/models/keras/t5/keras/flan_large_multi/3) | 783.15M | 24-layer T5 model. Trained on the Colossal Clean Crawled Corpus (C4). |
| [t5\_1.1\_xl](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_xl/2) | 2.85B |     |
| [t5\_1.1\_xxl](https://www.kaggle.com/models/keras/t5/keras/t5_1.1_xxl/2) | 11.14B |     |
| [t5gemma\_s\_s\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_ul2/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a UL2 model. |
| [t5gemma\_s\_s\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_prefixlm/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a prefix language model. |
| [t5gemma\_s\_s\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_ul2_it/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_s\_s\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_s_s_prefixlm_it/1) | 312.52M | T5Gemma S/S model with a small encoder and small decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_b\_b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_ul2/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a UL2 model. |
| [t5gemma\_b\_b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_prefixlm/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a prefix language model. |
| [t5gemma\_b\_b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_ul2_it/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_b\_b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_b_b_prefixlm_it/1) | 591.49M | T5Gemma B/B model with a base encoder and base decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_l\_l\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_ul2/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a UL2 model. |
| [t5gemma\_l\_l\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_prefixlm/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a prefix language model. |
| [t5gemma\_l\_l\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_ul2_it/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_l\_l\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_l_l_prefixlm_it/1) | 1.24B | T5Gemma L/L model with a large encoder and large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_ml\_ml\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_ul2/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a UL2 model. |
| [t5gemma\_ml\_ml\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_prefixlm/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a prefix language model. |
| [t5gemma\_ml\_ml\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_ul2_it/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_ml\_ml\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_ml_ml_prefixlm_it/1) | 2.20B | T5Gemma ML/ML model with a medium-large encoder and medium-large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_xl\_xl\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_ul2/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a UL2 model. |
| [t5gemma\_xl\_xl\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_prefixlm/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a prefix language model. |
| [t5gemma\_xl\_xl\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_ul2_it/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_xl\_xl\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_xl_xl_prefixlm_it/1) | 3.77B | T5Gemma XL/XL model with an extra-large encoder and extra-large decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_2b\_2b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_ul2/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_2b\_2b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_prefixlm/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_2b\_2b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_ul2_it/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_2b\_2b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_2b_2b_prefixlm_it/1) | 5.60B | T5Gemma 2B/2B model with a 2-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_9b\_2b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_ul2/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_9b\_2b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_prefixlm/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_9b\_2b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_ul2_it/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_9b\_2b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_2b_prefixlm_it/1) | 12.29B | T5Gemma 9B/2B model with a 9-billion-parameter encoder and 2-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma\_9b\_9b\_ul2](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_ul2/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a UL2 model. |
| [t5gemma\_9b\_9b\_prefixlm](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_prefixlm/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a prefix language model. |
| [t5gemma\_9b\_9b\_ul2\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_ul2_it/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a UL2 model and fine-tuned for instruction following. |
| [t5gemma\_9b\_9b\_prefixlm\_it](https://www.kaggle.com/models/keras/t5-gemma/keras/t5gemma_9b_9b_prefixlm_it/1) | 20.33B | T5Gemma 9B/9B model with a 9-billion-parameter encoder and 9-billion-parameter decoder, adapted as a prefix language model and fine-tuned for instruction following. |
| [t5gemma2\_270m\_270m](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_270m_270m/2) | 953.80M | Encoder–decoder (T5-style) based out of Gemma3 model with 270M encoder + 270M decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_1b\_1b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_1b_1b/2) | 2.42B | Encoder–decoder (T5-style) based out of Gemma3 model with 1B encoder + 1B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_4b\_4b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_4b_4b/2) | 8.18B | Encoder–decoder (T5-style) based out of Gemma3 model with 4B encoder + 4B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L254)

### `save_to_preset` method

Copied!

`Seq2SeqLMPreprocessor.save_to_preset(preset_dir)`

Save preprocessor to a preset directory.

**Arguments**

*   **preset\_dir**: The path to the local model preset directory.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.Seq2SeqLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[Seq2SeqLMPreprocessor](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#seq2seqlmpreprocessor)

[`Seq2SeqLMPreprocessor` class](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#seq2seqlmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#frompreset-method)

[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#savetopreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#tokenizer-property)