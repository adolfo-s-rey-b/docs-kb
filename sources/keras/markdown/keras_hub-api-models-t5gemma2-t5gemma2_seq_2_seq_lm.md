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
 / [T5Gemma2](https://keras.io/keras_hub/api/models/t5gemma2/)
 / T5Gemma2Seq2SeqLM model

T5Gemma2Seq2SeqLM model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/t5gemma2/t5gemma2_seq_2_seq_lm.py#L12)

### `T5Gemma2Seq2SeqLM` class

Copied!

`keras_hub.models.T5Gemma2Seq2SeqLM(backbone, preprocessor=None, **kwargs)`

An end-to-end T5Gemma2 model for seq2seq language modeling.

A seq2seq language model (LM) is an encoder-decoder model which is used for conditional text generation. The encoder is given a "context" text (fed to the encoder), and the decoder predicts the next token based on both the encoder inputs and the previous tokens.

T5Gemma2 extends T5Gemma by using Gemma3-based components, with merged self+cross attention in the decoder, Gemma3-style Q/K normalization, and per-layer-type RoPE.

This model has a `generate()` method, which generates text based on a prompt. The generation strategy used is controlled by an additional `sampler` argument on `compile()`.

**Arguments**

*   **backbone**: A [`keras_hub.models.T5Gemma2Backbone`](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_backbone#t5gemma2backbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.T5Gemma2Seq2SeqLMPreprocessor`](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm_preprocessor#t5gemma2seq2seqlmpreprocessor-class)
     or `None`. Defaults to `None`.

**Examples**

Use `generate()` to do text generation.

Copied!

`t5gemma2_lm = keras_hub.models.T5Gemma2Seq2SeqLM.from_preset(     "t5gemma2_270m_270m" ) t5gemma2_lm.generate(     "The quick brown fox jumped.", max_length=30 )`

Custom backbone and vocabulary.

Copied!

`tokenizer = keras_hub.models.T5Gemma2Tokenizer(     proto="proto.spm", ) preprocessor = keras_hub.models.T5Gemma2Seq2SeqLMPreprocessor(     tokenizer=tokenizer,     encoder_sequence_length=128,     decoder_sequence_length=128, ) backbone = keras_hub.models.T5Gemma2Backbone(     vocabulary_size=32000,     encoder_hidden_dim=256,     encoder_intermediate_dim=512,     encoder_num_layers=4,     encoder_num_attention_heads=4,     encoder_num_key_value_heads=2,     encoder_head_dim=64,     encoder_layer_types=["full_attention"] * 4,     decoder_hidden_dim=256,     decoder_intermediate_dim=512,     decoder_num_layers=4,     decoder_num_attention_heads=4,     decoder_num_key_value_heads=2,     decoder_head_dim=64,     decoder_layer_types=["full_attention"] * 4,     dropout_rate=0.1,     rms_norm_eps=1e-6,     query_pre_attn_scalar=1.0,     attention_bias=False,     hidden_activation="gelu_approximate", ) t5gemma2_lm = keras_hub.models.T5Gemma2Seq2SeqLM(     backbone=backbone,     preprocessor=preprocessor, )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`T5Gemma2Seq2SeqLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [t5gemma2\_270m\_270m](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_270m_270m/2) | 953.80M | Encoder–decoder (T5-style) based out of Gemma3 model with 270M encoder + 270M decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_1b\_1b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_1b_1b/2) | 2.42B | Encoder–decoder (T5-style) based out of Gemma3 model with 1B encoder + 1B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |
| [t5gemma2\_4b\_4b](https://www.kaggle.com/models/keras/t5gemma-2/keras/t5gemma2_4b_4b/2) | 8.18B | Encoder–decoder (T5-style) based out of Gemma3 model with 4B encoder + 4B decoder parameters, supporting text generation, multilingual tasks and long-context inputs. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`T5Gemma2Seq2SeqLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.T5Gemma2Seq2SeqLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.T5Gemma2Seq2SeqLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[T5Gemma2Seq2SeqLM model](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm/#t5gemma2seq2seqlm-model)

[`T5Gemma2Seq2SeqLM` class](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm/#t5gemma2seq2seqlm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/t5gemma2/t5gemma2_seq_2_seq_lm/#preprocessor-property)