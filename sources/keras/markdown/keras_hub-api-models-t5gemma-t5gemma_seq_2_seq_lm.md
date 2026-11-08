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
 / [T5Gemma](https://keras.io/keras_hub/api/models/t5gemma/)
 / T5GemmaSeq2SeqLM model

T5GemmaSeq2SeqLM model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma/t5gemma_seq_2_seq_lm.py#L12)

### `T5GemmaSeq2SeqLM` class

Copied!

`keras_hub.models.T5GemmaSeq2SeqLM(backbone, preprocessor=None, **kwargs)`

An end-to-end T5Gemma model for seq2seq language modeling.

A seq2seq language model (LM) is an encoder-decoder model which is used for conditional text generation. The encoder is given a "context" text (fed to the encoder), and the decoder predicts the next token based on both the encoder inputs and the previous tokens. You can finetune `T5GemmaSeq2SeqLM` to generate text for any seq2seq task (e.g., translation or summarization).

This model has a `generate()` method, which generates text based on a prompt. The generation strategy used is controlled by an additional `sampler` argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"greedy"` sampling will be used.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to string inputs during `fit()`, `predict()`, `evaluate()` and `generate()`. This is done by default when creating the model with `from_preset()`.

**Arguments**

*   **backbone**: A [`keras_hub.models.T5GemmaBackbone`](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_backbone#t5gemmabackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.T5GemmaSeq2SeqLMPreprocessor`](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm_preprocessor#t5gemmaseq2seqlmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model. Defaults to `None`.

**Examples**

Use `generate()` to do text generation.

Copied!

`import numpy as np t5gemma_lm = keras_hub.models.T5GemmaSeq2SeqLM.from_preset(     "t5gemma_b_b_prefixlm_it" ) # Generate with encoder-only input. t5gemma_lm.generate("The quick brown fox jumped.", max_length=30)  # Generate with batched encoder-only inputs. t5gemma_lm.generate(     ["The quick brown fox jumped.", "The whale."],     max_length=30 ) # Generate with encoder and decoder inputs. t5gemma_lm.generate(     {         "encoder_text": "The quick brown fox jumped.",         "decoder_text": "A fast fox"     },     max_length=30 )`

Compile the `generate()` function with a custom sampler.

Copied!

`t5gemma_lm = keras_hub.models.T5GemmaSeq2SeqLM.from_preset(     "t5gemma_b_b_prefixlm_it" ) t5gemma_lm.compile(sampler="top_k") t5gemma_lm.generate("I want to say", max_length=30)  t5gemma_lm.compile(sampler=keras_hub.samplers.BeamSampler(num_beams=2)) t5gemma_lm.generate("I want to say", max_length=30)`

Use `generate()` without preprocessing.

Copied!

``# Preprocessed inputs, with encoder inputs corresponding to # "The quick brown fox", and the decoder inputs to "A fast fox". # Use `"padding_mask"` to indicate values that should not be overridden. prompt = {     "encoder_token_ids": np.array([[2, 10, 133, 2119, 6219, 23602, 1, 0]]),     "encoder_padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 0]]),     "decoder_token_ids": np.array([[2, 133, 1769, 1, 0, 0, 0]]),     "decoder_padding_mask": np.array([[1, 1, 1, 1, 0, 0, 0]]) }  t5gemma_lm = keras_hub.models.T5GemmaSeq2SeqLM.from_preset(     "t5gemma_b_b_prefixlm_it",     preprocessor=None, ) t5gemma_lm.generate(prompt)``

Call `fit()` on a single batch.

Copied!

`features = {     "encoder_text": ["The quick fox jumped.", "I forgot my homework."],     "decoder_text": ["The fast hazel fox leapt.", "I forgot my assignment."] } t5gemma_lm = keras_hub.models.T5GemmaSeq2SeqLM.from_preset(     "t5gemma_b_b_prefixlm_it" ) t5gemma_lm.fit(x=features, batch_size=2)`

Call `fit()` without preprocessing.

Copied!

`x = {     "encoder_token_ids": np.array([[2, 133, 2119, 1, 0]] * 2),     "encoder_padding_mask": np.array([[1, 1, 1, 1, 0]] * 2),     "decoder_token_ids": np.array([[2, 133, 1769, 1, 0]] * 2),     "decoder_padding_mask": np.array([[1, 1, 1, 1, 1]] * 2), } y = np.array([[133, 1769, 1, 0, 0]] * 2) sw = np.array([[1, 1, 1, 0, 0]] * 2)  t5gemma_lm = keras_hub.models.T5GemmaSeq2SeqLM.from_preset(     "t5gemma_b_b_prefixlm_it",     preprocessor=None, ) t5gemma_lm.fit(x=x, y=y, sample_weight=sw, batch_size=2)`

Custom backbone and vocabulary.

Copied!

`features = {     "encoder_text": ["The quick fox jumped.", "I forgot my homework."],     "decoder_text": ["The fast hazel fox leapt.", "I forgot my assignment."] } tokenizer = keras_hub.models.T5GemmaTokenizer(     proto="proto.spm", ) preprocessor = keras_hub.models.T5GemmaSeq2SeqLMPreprocessor(     tokenizer=tokenizer,     encoder_sequence_length=128,     decoder_sequence_length=128, ) backbone = keras_hub.models.T5GemmaBackbone(     vocabulary_size=32000,     # Encoder parameters.     encoder_hidden_dim=256,     encoder_intermediate_dim=512,     encoder_num_layers=4,     encoder_num_attention_heads=4,     encoder_num_key_value_heads=2,     encoder_head_dim=64,     encoder_layer_types=["full_attention"] * 4,     # Decoder parameters.     decoder_hidden_dim=256,     decoder_intermediate_dim=512,     decoder_num_layers=4,     decoder_num_attention_heads=4,     decoder_num_key_value_heads=2,     decoder_head_dim=64,     decoder_layer_types=["full_attention"] * 4,     # Common parameters.     dropout_rate=0.1,     rms_norm_eps=1e-6,     query_pre_attn_scalar=1.0,     attention_bias=False,     hidden_activation="gelu_approximate", ) t5gemma_lm = keras_hub.models.T5GemmaSeq2SeqLM(     backbone=backbone,     preprocessor=preprocessor, ) t5gemma_lm.fit(x=features, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`T5GemmaSeq2SeqLM.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`

| Preset | Parameters | Description |
| --- | --- | --- |
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

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`T5GemmaSeq2SeqLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

Generate text given prompt `inputs`.

This method generates text based on given `inputs`. The sampling method used for generation can be set via the `compile()` method.

If `inputs` are a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, outputs will be generated "batch-by-batch" and concatenated. Otherwise, all inputs will be handled as a single batch.

If a `preprocessor` is attached to the model, `inputs` will be preprocessed inside the `generate()` function and should match the structure expected by the `preprocessor` layer (usually raw strings). If a `preprocessor` is not attached, inputs should match the structure expected by the `backbone`. See the example usage above for a demonstration of each.

**Arguments**

*   **inputs**: python data, tensor data, or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    . If a `preprocessor` is attached to the model, `inputs` should match the structure expected by the `preprocessor` layer. If a `preprocessor` is not attached, `inputs` should match the structure expected the `backbone` model.
*   **max\_length**: Optional. int. The max length of the generated sequence. Will default to the max configured `sequence_length` of the `preprocessor`. If `preprocessor` is `None`, `inputs` should be should be padded to the desired maximum length and this argument will be ignored.
*   **stop\_token\_ids**: Optional. `None`, "auto", or tuple of token ids. Defaults to "auto" which uses the `preprocessor.tokenizer.end_token_id`. Not specifying a processor will produce an error. None stops generation after generating `max_length` tokens. You may also specify a list of token id's the model should stop on. Note that sequences of tokens will each be interpreted as a stop token, multi-token stop sequences are not supported.
*   **strip\_prompt**: Optional. By default, generate() returns the full prompt followed by its completion generated by the model. If this option is set to True, only the newly generated text is returned.

* * *

### `backbone` property

Copied!

`keras_hub.models.T5GemmaSeq2SeqLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.T5GemmaSeq2SeqLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[T5GemmaSeq2SeqLM model](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm/#t5gemmaseq2seqlm-model)

[`T5GemmaSeq2SeqLM` class](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm/#t5gemmaseq2seqlm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/t5gemma/t5gemma_seq_2_seq_lm/#preprocessor-property)