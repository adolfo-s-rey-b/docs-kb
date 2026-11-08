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
 / [PaliGemma](https://keras.io/keras_hub/api/models/pali_gemma/)
 / PaliGemmaCausalLMPreprocessor layer

PaliGemmaCausalLMPreprocessor layer
===================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/pali_gemma/pali_gemma_causal_lm_preprocessor.py#L20)

### `PaliGemmaCausalLMPreprocessor` class

Copied!

`keras_hub.models.PaliGemmaCausalLMPreprocessor(     tokenizer,     image_converter=None,     sequence_length=1024,     add_start_token=True,     add_end_token=True,     **kwargs )`

Base class for causal language modeling preprocessing layers.

`CausalLMPreprocessor` tasks wrap a `keras_hub.tokenizer.Tokenizer` to create a preprocessing layer for causal language modeling tasks. It is intended to be paired with a `keras.models.CausalLM` task.

All `CausalLMPreprocessor` take inputs a single input. This can be a single string or a batch of strings. See examples below. These inputs will be tokenized and padded/truncated to a fixed sequence length.

This layer will always output a `(x, y, sample_weight)` tuple, where `x` is a dictionary with the tokenized inputs, `y` contains the tokens from `x` offset by 1, and `sample_weight` marks where `y` contains padded values. The exact contents of `x` will vary depending on the model being used.

a `CausalLMPreprocessor` contains two extra methods, `generate_preprocess` and `generate_postprocess` for use with generation. See examples below.

All `CausalLMPreprocessor` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and vocabularies. You can call the `from_preset()` constructor directly on this base class, in which case the correct class for you model will be automatically instantiated.

Examples.

Copied!

``preprocessor = keras_hub.models.CausalLMPreprocessor.from_preset(     "bert_base_en_uncased",     sequence_length=256, # Optional. )  # Tokenize, mask and pack a single sentence. x = "The quick brown fox jumped." x, y, sample_weight = preprocessor(x)  # Tokenize and pad/truncate a batch of labeled sentences. x = ["The quick brown fox jumped.", "Call me Ishmael."] x, y, sample_weight = preprocessor(x)  # With a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). ds = tf.data.Dataset.from_tensor_slices(x) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Generate preprocess and postprocess. x = preprocessor.generate_preprocess(x)  # Tokenized numeric inputs. x = preprocessor.generate_postprocess(x)  # Detokenized string outputs.``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`PaliGemmaCausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [pali\_gemma\_3b\_mix\_224](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_mix_224/4) | 2.92B | image size 224, mix fine tuned, text sequence length is 256 |
| [pali\_gemma\_3b\_224](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_224/4) | 2.92B | image size 224, pre trained, text sequence length is 128 |
| [pali\_gemma\_3b\_mix\_448](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_mix_448/4) | 2.92B | image size 448, mix fine tuned, text sequence length is 512 |
| [pali\_gemma\_3b\_448](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_448/4) | 2.92B | image size 448, pre trained, text sequence length is 512 |
| [pali\_gemma\_3b\_896](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_896/4) | 2.93B | image size 896, pre trained, text sequence length is 512 |
| [pali\_gemma2\_mix\_3b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_3b_224/2) | 3.03B | 3 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_3b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_224/2) | 3.03B | 3 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma\_2\_ft\_docci\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma_2_ft_docci_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on the DOCCI dataset for improved descriptions with fine-grained details. |
| [pali\_gemma2\_mix\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_3b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_896/2) | 3.04B | 3 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_mix\_10b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_10b_224/3) | 9.66B | 10 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_10b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_224/3) | 9.66B | 10 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_ft\_docci\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_ft_docci_10b_448/3) | 9.66B | 10 billion parameter, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on the DOCCI dataset for improved descriptions with fine-grained details. |
| [pali\_gemma2\_mix\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_10b_448/3) | 9.66B | 10 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_448/3) | 9.66B | 10 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_10b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_896/3) | 9.67B | 10 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_mix\_28b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_28b_mix_224/3) | 27.65B | 28 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_mix\_28b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_28b_mix_448/3) | 27.65B | 28 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_28b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_224/4) | 27.65B | 28 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_28b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_448/3) | 27.65B | 28 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_28b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_896/3) | 27.65B | 28 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |

* * *

### `tokenizer` property

Copied!

`keras_hub.models.PaliGemmaCausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[PaliGemmaCausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_causal_lm_preprocessor/#paligemmacausallmpreprocessor-layer)

[`PaliGemmaCausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_causal_lm_preprocessor/#paligemmacausallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/pali_gemma/pali_gemma_causal_lm_preprocessor/#tokenizer-property)