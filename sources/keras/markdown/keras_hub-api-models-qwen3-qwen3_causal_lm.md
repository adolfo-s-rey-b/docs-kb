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
 / [Qwen3](https://keras.io/keras_hub/api/models/qwen3/)
 / Qwen3CausalLM model

Qwen3CausalLM model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/qwen3/qwen3_causal_lm.py#L13)

### `Qwen3CausalLM` class

Copied!

`keras_hub.models.Qwen3CausalLM(backbone, preprocessor=None, **kwargs)`

An end-to-end Qwen3 model for causal language modeling.

A causal language model (LM) predicts the next token based on previous tokens. This task setup can be used to train the model unsupervised on plain text input, or to autoregressively generate plain text similar to the data used for training. This task can be used for pre-training or fine-tuning a Qwen3 model, simply by calling `fit()`.

This model has a `generate()` method, which generates text based on a prompt. The generation strategy used is controlled by an additional `sampler` argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"greedy"` sampling will be used.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to string inputs during `fit()`, `predict()`, `evaluate()`, and `generate()`. This is done by default when creating the model with `from_preset()`.

**Arguments**

*   **backbone**: A [`keras_hub.models.Qwen3Backbone`](https://keras.io/keras_hub/api/models/qwen3/qwen3_backbone#qwen3backbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.Qwen3CausalLMPreprocessor`](https://keras.io/keras_hub/api/models/qwen3/qwen3_causal_lm_preprocessor#qwen3causallmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

**Examples**

Use `generate()` to do text generation.

Copied!

`qwen3_lm = keras_hub.models.Qwen3CausalLM.from_preset("qwen3_0.6b_en") qwen3_lm.generate("I want to say", max_length=30)  # Generate with batched prompts. qwen3_lm.generate(["This is a", "Where are you"], max_length=30)`

Compile the `generate()` function with a custom sampler.

Copied!

`qwen3_lm = keras_hub.models.Qwen3MoeCausalLM.from_preset("qwen3_0.6b_en") qwen3_lm.compile(sampler="top_k") qwen3_lm.generate("I want to say", max_length=30)  qwen3_lm.compile(sampler=keras_hub.samplers.BeamSampler(num_beams=2)) qwen3_lm.generate("I want to say", max_length=30)`

Use `generate()` without preprocessing.

Copied!

``prompt = {     # Token ids for "<bos> Qwen3 is".     "token_ids": np.array([[2, 12345, 678, 0, 0, 0, 0]] * 2),     # Use `"padding_mask"` to indicate values that should not be overridden.     "padding_mask": np.array([[1, 1, 1, 0, 0, 0, 0]] * 2), }  qwen3_lm = keras_hub.models.Qwen3MoeCausalLM.from_preset(     "qwen3_0.6b_en",     preprocessor=None, ) qwen3_lm.generate(prompt)``

Call `fit()` on a single batch.

Copied!

`features = ["The quick brown fox jumped.", "I forgot my homework."] qwen3_lm = keras_hub.models.Qwen3MoeCausalLM.from_preset("qwen3_0.6b_en") qwen3_lm.fit(x=features, batch_size=2)`

Call `fit()` with LoRA fine-tuning enabled.

Copied!

`features = ["The quick brown fox jumped.", "I forgot my homework."] qwen3_lm = keras_hub.models.Qwen3MoeCausalLM.from_preset(     'qwen3_0.6b_en' ) qwen3_lm.backbone.enable_lora(rank=4) qwen3_lm.fit(x=features, batch_size=2)`

Call `fit()` without preprocessing.

Copied!

`x = {     # Token ids for "<bos> Qwen3 is a language model<eos>"     "token_ids": np.array([[2, 12345, 678, 543, 9876, 1, 0, 0]] * 2),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 0, 0]] * 2), } y = np.array([[12345, 678, 543, 9876, 1, 0, 0, 0]] * 2) sw = np.array([[1, 1, 1, 1, 1, 0, 0, 0]] * 2)  qwen3_lm = keras_hub.models.Qwen3MoeCausalLM.from_preset(     "qwen3_0.6b_en",     preprocessor=None, ) qwen3_lm.fit(x=x, y=y, sample_weight=sw, batch_size=2)`

Custom backbone and vocabulary.

Copied!

`tokenizer = keras_hub.models.Qwen3MoeTokenizer(     proto="qwen3_moe_vocab.spm", ) preprocessor = keras_hub.models.Qwen3MoeCausalLMPreprocessor(     tokenizer=tokenizer,     sequence_length=128, ) backbone = keras_hub.models.Qwen3MoeBackbone(     vocabulary_size=151936,     num_layers=28,     num_query_heads=16,     num_key_value_heads=8,     hidden_dim=2048,     intermediate_dim=4096,     moe_intermediate_dim=128,     shared_expert_intermediate_dim=4096,     num_experts=60,     top_k=4,     max_sequence_length=4096, ) qwen3_lm = keras_hub.models.Qwen3MoeCausalLM(     backbone=backbone,     preprocessor=preprocessor, ) qwen3_lm.fit(x=features, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`Qwen3CausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [qwen3\_embedding\_0.6b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_0.6b_en/1) | 595.78M | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 1024. |
| [qwen3\_0.6b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_0.6b_en/1) | 596.05M | 28-layer Qwen3 model with 596M parameters, optimized for efficiency and fast inference on resource-constrained devices. |
| [harrier\_embedding\_oss\_0.6b](https://www.kaggle.com/models/keras/harrier/keras/harrier_embedding_oss_0.6b/1) | 596.05M | Microsoft harrier-oss-v1 0.6B multilingual text embedding model based on the Qwen3-0.6B architecture, fine-tuned for dense retrieval and semantic similarity across 94+ languages. Achieves 69.0 on Multilingual MTEB v2. |
| [qwen3\_1.7b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_1.7b_en/1) | 1.72B | 28-layer Qwen3 model with 1.72B parameters, offering a good balance between performance and resource usage. |
| [qwen3\_embedding\_4b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_4b_en/1) | 4.02B | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 2560. |
| [qwen3\_4b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_4b_en/1) | 4.02B | 36-layer Qwen3 model with 4.02B parameters, offering improved reasoning capabilities and better performance than smaller variants. |
| [qwen3\_embedding\_8b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_8b_en/1) | 8.19B | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 4096. |
| [qwen3\_8b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_8b_en/1) | 8.19B | 36-layer Qwen3 model with 8.19B parameters, featuring enhanced reasoning, coding, and instruction-following capabilities. |
| [qwen3\_14b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_14b_en/1) | 14.77B | 40-layer Qwen3 model with 14.77B parameters, featuring advanced reasoning, coding, and multilingual capabilities. |
| [qwen3\_32b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_32b_en/1) | 32.76B | 64-layer Qwen3 model with 32.76B parameters, featuring state-of-the-art performance across reasoning, coding, and general language tasks. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`Qwen3CausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.Qwen3CausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.Qwen3CausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[Qwen3CausalLM model](https://keras.io/keras_hub/api/models/qwen3/qwen3_causal_lm/#qwen3causallm-model)

[`Qwen3CausalLM` class](https://keras.io/keras_hub/api/models/qwen3/qwen3_causal_lm/#qwen3causallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/qwen3/qwen3_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/qwen3/qwen3_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/qwen3/qwen3_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/qwen3/qwen3_causal_lm/#preprocessor-property)