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
 / [RWKV7](https://keras.io/keras_hub/api/models/rwkv7/)
 / RWKV7CausalLM model

RWKV7CausalLM model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/rwkv7/rwkv7_causal_lm.py#L12)

### `RWKV7CausalLM` class

Copied!

`keras_hub.models.RWKV7CausalLM(backbone, preprocessor=None, **kwargs)`

An end-to-end RWKV-7 model for causal language modeling.

Copied!

``A causal language model (LM) predicts the next token based on previous tokens. This task setup can be used to train the model unsupervised on plain text input, or to autoregressively generate plain text similar to the data used for training. This task can be used for pre-training or fine-tuning a RWKV-7 model, simply by calling `fit()`.  This model has a generate() method, which generates text based on a prompt. The generation strategy used is controlled by an additional sampler argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"greedy"` sampling will be used.  # Arguments     backbone: A [`keras_hub.models.RWKV7Backbone`](/keras_hub/api/models/rwkv7/rwkv7_backbone#rwkv7backbone-class) instance.     preprocessor: A [`keras_hub.models.RWKV7CausalLMPreprocessor`](/keras_hub/api/models/rwkv7/rwkv7_causal_lm_preprocessor#rwkv7causallmpreprocessor-class) or `None`.         If `None`, this model will not apply preprocessing, and inputs         should be preprocessed before calling the model.  # Examples  ```python # Initialize the tokenizer and load assets from a local path. tokenizer = RWKVTokenizer() tokenizer.load_assets(rwkv_path)  # Create a preprocessor with a sequence length of 8. preprocessor = RWKV7CausalLMPreprocessor(tokenizer, sequence_length=8)  # Initialize the model with a backbone and preprocessor. causal_lm = RWKV7CausalLM(backbone, preprocessor)  # you also can load model by from_preset rwkv_path = "RWKV7_G1a_0.1B" tokenizer = RWKVTokenizer.from_preset(rwkv_path) causal_lm = RWKV7CausalLM.from_preset(rwkv_path)  prompts = ["Bubble sort``\
\
\`\`\`python", "Hello World\
\
Copied!\
\
``"]      causal_lm.compile(sampler="greedy")      outputs = causal_lm.generate(prompts, max_length=128)     for out in outputs:         print(out)         print("-" * 100)     ```  ----  <span style="float:right;">[[source]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)</span>  ### `from_preset` method  ```python RWKV7CausalLM.from_preset(preset, load_weights=True, **kwargs)``

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
| [rwkv7\_g1a\_0.1b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.1b/1) | 150.00M | 150 million parameter RWKV7 model. Optimized for edge devices and mobile deployment. |
| [rwkv7\_g1a\_0.3b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.3b/1) | 400.00M | 400 million parameter RWKV7 model. Small variant balancing speed and instruction following. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`RWKV7CausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.RWKV7CausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.RWKV7CausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[RWKV7CausalLM model](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm/#rwkv7causallm-model)

[`RWKV7CausalLM` class](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm/#rwkv7causallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/rwkv7/rwkv7_causal_lm/#preprocessor-property)