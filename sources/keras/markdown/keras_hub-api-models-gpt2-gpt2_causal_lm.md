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
 / [GPT2](https://keras.io/keras_hub/api/models/gpt2/)
 / GPT2CausalLM model

GPT2CausalLM model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gpt2/gpt2_causal_lm.py#L13)

### `GPT2CausalLM` class

Copied!

`keras_hub.models.GPT2CausalLM(backbone, preprocessor=None, **kwargs)`

An end-to-end GPT2 model for causal language modeling.

A causal language model (LM) predicts the next token based on previous tokens. This task setup can be used to train the model unsupervised on plain text input, or to autoregressively generate plain text similar to the data used for training. This task can be used for pre-training or fine-tuning a GPT-2 model, simply by calling `fit()`.

This model has a `generate()` method, which generates text based on a prompt. The generation strategy used is controlled by an additional `sampler` argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"top_k"` sampling will be used.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to string inputs during `fit()`, `predict()`, `evaluate()` and `generate()`. This is done by default when creating the model with `from_preset()`.

Disclaimer: Pre-trained models are provided on an "as is" basis, without warranties or conditions of any kind. The underlying model is provided by a third party and subject to a separate license, available [here](https://github.com/openai/gpt-2)
.

**Arguments**

*   **backbone**: A [`keras_hub.models.GPT2Backbone`](https://keras.io/keras_hub/api/models/gpt2/gpt2_backbone#gpt2backbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.GPT2CausalLMPreprocessor`](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm_preprocessor#gpt2causallmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

**Examples**

Use `generate()` to do text generation.

Copied!

`gpt2_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en") gpt2_lm.generate("I want to say", max_length=30)  # Generate with batched prompts. gpt2_lm.generate(["This is a", "Where are you"], max_length=30)`

Compile the `generate()` function with a custom sampler.

Copied!

`gpt2_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en") gpt2_lm.compile(sampler="greedy") gpt2_lm.generate("I want to say", max_length=30)  gpt2_lm.compile(sampler=keras_hub.samplers.BeamSampler(num_beams=2)) gpt2_lm.generate("I want to say", max_length=30)`

Use `generate()` without preprocessing.

Copied!

``# Prompt the model with `5338, 318` (the token ids for `"Who is"`). # Use `"padding_mask"` to indicate values that should not be overridden. prompt = {     "token_ids": np.array([[5338, 318, 0, 0, 0]] * 2),     "padding_mask": np.array([[1, 1, 0, 0, 0]] * 2), }  gpt2_lm = keras_hub.models.GPT2CausalLM.from_preset(     "gpt2_base_en",     preprocessor=None, ) gpt2_lm.generate(prompt)``

Call `fit()` on a single batch.

Copied!

`features = ["The quick brown fox jumped.", "I forgot my homework."] gpt2_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en") gpt2_lm.fit(x=features, batch_size=2)`

Call `fit()` without preprocessing.

Copied!

`x = {     "token_ids": np.array([[50256, 1, 2, 3, 4]] * 2),     "padding_mask": np.array([[1, 1, 1, 1, 1]] * 2), } y = np.array([[1, 2, 3, 4, 50256]] * 2) sw = np.array([[1, 1, 1, 1, 1]] * 2)  gpt2_lm = keras_hub.models.GPT2CausalLM.from_preset(     "gpt2_base_en",     preprocessor=None, ) gpt2_lm.fit(x=x, y=y, sample_weight=sw, batch_size=2)`

Custom backbone and vocabulary.

Copied!

`features = ["a quick fox.", "a fox quick."] vocab = {"<|endoftext|>": 0, "a": 4, "Ġquick": 5, "Ġfox": 6} merges = ["Ġ q", "u i", "c k", "ui ck", "Ġq uick"] merges += ["Ġ f", "o x", "Ġf ox"]  tokenizer = keras_hub.models.GPT2Tokenizer(     vocabulary=vocab,     merges=merges, ) preprocessor = keras_hub.models.GPT2CausalLMPreprocessor(     tokenizer=tokenizer,     sequence_length=128, ) backbone = keras_hub.models.GPT2Backbone(     vocabulary_size=30552,     num_layers=4,     num_heads=4,     hidden_dim=256,     intermediate_dim=512,     max_sequence_length=128, ) gpt2_lm = keras_hub.models.GPT2CausalLM(     backbone=backbone,     preprocessor=preprocessor, ) gpt2_lm.fit(x=features, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`GPT2CausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [gpt2\_base\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_base_en/3) | 124.44M | 12-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_base\_en\_cnn\_dailymail](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_base_en_cnn_dailymail/3) | 124.44M | 12-layer GPT-2 model where case is maintained. Finetuned on the CNN/DailyMail summarization dataset. |
| [gpt2\_medium\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_medium_en/3) | 354.82M | 24-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_large\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_large_en/3) | 774.03M | 36-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_extra\_large\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_extra_large_en/3) | 1.56B | 48-layer GPT-2 model where case is maintained. Trained on WebText. |

**Guides and examples using `from_preset`**

*   [Parameter-efficient fine-tuning of GPT-2 with LoRA](https://keras.io/examples/nlp/parameter_efficient_finetuning_of_gpt2_with_lora/)
    
*   [GPT2 Text Generation with KerasHub](https://keras.io/examples/generative/gpt2_text_generation_with_keras_hub/)
    

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`GPT2CausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.GPT2CausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.GPT2CausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[GPT2CausalLM model](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm/#gpt2causallm-model)

[`GPT2CausalLM` class](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm/#gpt2causallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/gpt2/gpt2_causal_lm/#preprocessor-property)