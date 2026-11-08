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
 / [GPT-OSS](https://keras.io/keras_hub/api/models/gpt_oss/)
 / GptOssCausalLM model

GptOssCausalLM model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gpt_oss/gpt_oss_causal_lm.py#L13)

### `GptOssCausalLM` class

Copied!

`keras_hub.models.GptOssCausalLM(backbone, preprocessor=None, **kwargs)`

An end-to-end GptOss model for causal language modeling.

A causal language model (LM) predicts the next token based on previous tokens. This task setup can be used to train the model unsupervised on plain text input, or to autoregressively generate plain text similar to the data used for training. This task can be used for pre-training or fine-tuning a GptOss model, simply by calling `fit()`.

This model has a `generate()` method, which generates text based on a prompt. The generation strategy used is controlled by an additional `sampler` argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"top_k"` sampling will be used.

**Arguments**

*   **backbone**: A [`keras_hub.models.GptOssBackbone`](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_backbone#gptossbackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.GptOssCausalLMPreprocessor`](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm_preprocessor#gptosscausallmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`GptOssCausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [gpt\_oss\_20b\_en](https://www.kaggle.com/models/keras/gpt-oss/keras/gpt_oss_20b_en/1) | 20.91B | This preset has 21 billion total parameters, with 3.6 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [gpt\_oss\_safeguard\_20b\_en](https://www.kaggle.com/models/keras/gpt-oss-safeguard/keras/gpt_oss_safeguard_20b_en/1) | 20.91B | Open-weight safety reasoning model with 21 billion total parameters,with 3.6 billion active parameters, a context length of over 128k, and is de-quantized from MXFP4. |
| [gpt\_oss\_120b\_en](https://www.kaggle.com/models/keras/gpt-oss/keras/gpt_oss_120b_en/1) | 116.83B | This preset has 117 billion total parameters, with 5.1 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [gpt\_oss\_safeguard\_120b\_en](https://www.kaggle.com/models/keras/gpt-oss-safeguard/keras/gpt_oss_safeguard_120b_en/1) | 116.83B | Open-weight safety reasoning model with 117 billion total parameters,with 5.1 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`GptOssCausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.GptOssCausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.GptOssCausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[GptOssCausalLM model](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm/#gptosscausallm-model)

[`GptOssCausalLM` class](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm/#gptosscausallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/gpt_oss/gpt_oss_causal_lm/#preprocessor-property)