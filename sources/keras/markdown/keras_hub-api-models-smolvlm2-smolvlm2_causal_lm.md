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
 / [SmolVLM2](https://keras.io/keras_hub/api/models/smolvlm2/)
 / SmolVLM2CausalLM model

SmolVLM2CausalLM model
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/smolvlm2/smolvlm2_causal_lm.py#L15)

### `SmolVLM2CausalLM` class

Copied!

`keras_hub.models.SmolVLM2CausalLM(backbone, preprocessor=None, **kwargs)`

SmolVLM2 causal language model for multimodal text generation.

Copied!

``A causal language model (LM) that predicts the next token based on previous tokens and optional image inputs. This model can be used for image captioning, visual question answering, video understanding, and general text generation.  This model has a `generate()` method, which generates text based on a prompt (with optional images). The generation strategy is controlled by an additional `sampler` argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"greedy"` sampling is used.  This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to string inputs during `fit()`, `predict()`, `evaluate()` and `generate()`.  # Arguments     backbone: A [`keras_hub.models.SmolVLM2Backbone`](/keras_hub/api/models/smolvlm2/smolvlm2_backbone#smolvlm2backbone-class) instance.     preprocessor: A [`keras_hub.models.SmolVLM2CausalLMPreprocessor`](/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm_preprocessor#smolvlm2causallmpreprocessor-class)         or `None`.  # Examples   Use `generate()` for text generation. ```python smolvlm2_lm = keras_hub.models.SmolVLM2CausalLM.from_preset(     "smolvlm2_2.2b_instruct" ) smolvlm2_lm.generate("Hello, world!") ```  Use `generate()` with an image. The prompt must contain one `<image>` placeholder per image, which the preprocessor expands into the full sub-image token sequence. ```python smolvlm2_lm = keras_hub.models.SmolVLM2CausalLM.from_preset(     "smolvlm2_2.2b_instruct" ) image = np.random.randint(0, 256, (512, 512, 3)).astype("uint8") smolvlm2_lm.generate(     {         "prompts": (             "<|im_start|>User:<image>What is in this image?"             "<end_of_utterance>``

Assistant:" ), "images": image, }, max\_length=512, ) \`\`\`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`SmolVLM2CausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [smolvlm2\_256m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_256m_video_instruct/1) | 256.48M | 256 million parameter SmolVLM2 vision-language model with a 30-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_500m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_500m_video_instruct/1) | 507.48M | 500 million parameter SmolVLM2 vision-language model with a 32-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_2.2b\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_2.2b_instruct/1) | 2.25B | 2.2 billion parameter SmolVLM2 vision-language model with a 24-layer SmolLM2 text decoder and a 27-layer SigLIP vision encoder (384x384 images). Instruction-tuned for image and video understanding. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`SmolVLM2CausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.SmolVLM2CausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.SmolVLM2CausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[SmolVLM2CausalLM model](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm/#smolvlm2causallm-model)

[`SmolVLM2CausalLM` class](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm/#smolvlm2causallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_causal_lm/#preprocessor-property)