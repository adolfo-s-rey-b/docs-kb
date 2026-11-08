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
 / [Bloom](https://keras.io/keras_hub/api/models/bloom/)
 / BloomCausalLM model

BloomCausalLM model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/bloom/bloom_causal_lm.py#L12)

### `BloomCausalLM` class

Copied!

`keras_hub.models.BloomCausalLM(backbone, preprocessor=None, **kwargs)`

An end-to-end BLOOM model for causal language modeling.

A causal language model (LM) predicts the next token based on previous tokens. This task setup can be used to train the model unsupervised on plain text input, or to autoregressively generate plain text similar to the data used for training. This task can be used for pre-training or fine-tuning a BLOOM model, simply by calling `fit()`.

This model has a `generate()` method, which generates text based on a prompt. The generation strategy used is controlled by an additional `sampler` argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"greedy"` sampling will be used.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to string inputs during `fit()`, `predict()`, `evaluate()` and `generate()`. This is done by default when creating the model with `from_preset()`.

**Arguments**

*   **backbone**: A [`keras_hub.models.BloomBackbone`](https://keras.io/keras_hub/api/models/bloom/bloom_backbone#bloombackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.BloomCausalLMPreprocessor`](https://keras.io/keras_hub/api/models/bloom/bloom_causal_lm_preprocessor#bloomcausallmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

**Examples**

Use `generate()` to do text generation.

Copied!

`bloom_lm = keras_hub.models.BloomCausalLM.from_preset("bloom_560m_multi") bloom_lm.generate("I want to say", max_length=30)  # Generate with batched prompts. bloom_lm.generate(["This is a", "Where are you"], max_length=30)`

Compile the `generate()` function with a custom sampler.

Copied!

`bloom_lm = keras_hub.models.BloomCausalLM.from_preset("bloom_560m_multi") bloom_lm.compile(sampler="top_k") bloom_lm.generate("I want to say", max_length=30)  bloom_lm.compile(sampler=keras_hub.samplers.BeamSampler(num_beams=2)) bloom_lm.generate("I want to say", max_length=30)`

Use `generate()` without preprocessing.

Copied!

``prompt = {     # Token ids for "<s> Keras is".     "token_ids": np.array([[1, 46, 15762, 632, 3, 3, 3, 3, 3]] * 2),     # Use `"padding_mask"` to indicate values that should not be overridden.     "padding_mask": np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0]] * 2), }  bloom_lm = keras_hub.models.BloomCausalLM.from_preset(     "bloom_560m_multi",     preprocessor=None, ) bloom_lm.generate(prompt)``

Call `fit()` on a single batch.

Copied!

`features = ["The quick brown fox jumped.", "I forgot my homework."] bloom_lm = keras_hub.models.BloomCausalLM.from_preset("bloom_560m_multi") bloom_lm.fit(x=features, batch_size=2)`

Call `fit()` without preprocessing.

Copied!

`x = {     # Token ids for "<bos> Keras is deep learning library<eos>"     "token_ids": np.array([[2, 214064, 603, 5271, 6044, 9581, 1, 0]] * 2),     "padding_mask": np.array([[1, 1, 1, 1, 1, 1, 1, 0]] * 2), } y = np.array([[214064, 603, 5271, 6044, 9581, 3, 0, 0]] * 2) sw = np.array([[1, 1, 1, 1, 1, 1, 0, 0]] * 2)  bloom_lm = keras_hub.models.BloomCausalLM.from_preset(     "bloom_560m_multi",     preprocessor=None, ) bloom_lm.fit(x=x, y=y, sample_weight=sw, batch_size=2)`

Custom backbone and vocabulary.

Copied!

`features = [     " airplane at airport",     " airplane airport", ] vocab = ["<unk>", "<s>", "</s>", "<pad>"] vocab += ["!", "air", "Ġair", "plane", "Ġat", "port"] vocab = dict([(token, i) for i, token in enumerate(vocab)]) merges = ["Ġ a", "Ġ t", "Ġ i", "Ġ b", "a i", "p l", "n e"] merges += ["Ġa t", "p o", "r t", "Ġt h", "ai r", "pl a", "po rt"] merges += ["Ġai r", "Ġa i", "pla ne"] tokenizer = keras_hub.models.BloomTokenizer(vocabulary=vocab, merges=merges) preprocessor = keras_hub.models.BloomCausalLMPreprocessor(     tokenizer=tokenizer,     sequence_length=128, ) backbone = keras_hub.models.BloomBackbone(     vocabulary_size=tokenizer.vocabulary_size(),     num_layers=4,     num_heads=4,     hidden_dim=32,     intermediate_dim=128, ) bloom_lm = keras_hub.models.BloomCausalLM(     backbone=backbone,     preprocessor=preprocessor, ) bloom_lm.fit(x=features, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`BloomCausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [bloom\_560m\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_560m_multi/4) | 559.21M | 24-layer Bloom model with hidden dimension of 1024. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_560m\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_560m_multi/2) | 559.21M | 24-layer Bloom model with hidden dimension of 1024. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_1.1b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_1.1b_multi/2) | 1.07B | 24-layer Bloom model with hidden dimension of 1536. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_1.1b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_1.1b_multi/2) | 1.07B | 24-layer Bloom model with hidden dimension of 1536. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_1.7b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_1.7b_multi/2) | 1.72B | 24-layer Bloom model with hidden dimension of 2048. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_1.7b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_1.7b_multi/2) | 1.72B | 24-layer Bloom model with hidden dimension of 2048. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_3b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_3b_multi/2) | 3.00B | 30-layer Bloom model with hidden dimension of 2560. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_3b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_3b_multi/2) | 3.00B | 30-layer Bloom model with hidden dimension of 2560. finetuned on crosslingual task mixture (xP3) dataset. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`BloomCausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.BloomCausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.BloomCausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[BloomCausalLM model](https://keras.io/keras_hub/api/models/bloom/bloom_causal_lm/#bloomcausallm-model)

[`BloomCausalLM` class](https://keras.io/keras_hub/api/models/bloom/bloom_causal_lm/#bloomcausallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/bloom/bloom_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/bloom/bloom_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/bloom/bloom_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/bloom/bloom_causal_lm/#preprocessor-property)