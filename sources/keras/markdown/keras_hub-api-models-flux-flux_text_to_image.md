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
 / [Flux](https://keras.io/keras_hub/api/models/flux/)
 / FluxTextToImage model

FluxTextToImage model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/flux/flux_text_to_image.py#L11)

### `FluxTextToImage` class

Copied!

`keras_hub.models.FluxTextToImage(backbone, preprocessor, **kwargs)`

An end-to-end Flux model for text-to-image generation.

This model has a `generate()` method, which generates image based on a prompt.

**Arguments**

*   **backbone**: A [`keras_hub.models.FluxBackbone`](https://keras.io/keras_hub/api/models/flux/flux_model#fluxbackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.FluxTextToImagePreprocessor`](https://keras.io/keras_hub/api/models/flux/flux_text_to_image_preprocessor#fluxtexttoimagepreprocessor-class)
     instance.

**Examples**

Use `generate()` to do image generation.

Copied!

``prompt = (     "Astronaut in a jungle, cold color palette, muted colors, "     "detailed, 8k" ) text_to_image = keras_hub.models.FluxTextToImage.from_preset(     "TBA", height=512, width=512 ) text_to_image.generate(     prompt )  # Generate with batched prompts. text_to_image.generate(     ["cute wallpaper art of a cat", "cute wallpaper art of a dog"] )  # Generate with different `num_steps` and `guidance_scale`. text_to_image.generate(     prompt,     num_steps=50,     guidance_scale=5.0, )  # Generate with `negative_prompts`. text_to_image.generate(     {         "prompts": prompt,         "negative_prompts": "green color",     } )``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`FluxTextToImage.from_preset(preset, load_weights=True, **kwargs)`

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

* * *

### `backbone` property

Copied!

`keras_hub.models.FluxTextToImage.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/flux/flux_text_to_image.py#L134)

### `generate` method

Copied!

`FluxTextToImage.generate(inputs, num_steps=28, guidance_scale=7.0, seed=None)`

Generate image based on the provided `inputs`.

Typically, `inputs` contains a text description (known as a prompt) used to guide the image generation.

Some models support a `negative_prompts` key, which helps steer the model away from generating certain styles and elements. To enable this, pass `prompts` and `negative_prompts` as a dict:

Copied!

`prompt = (     "Astronaut in a jungle, cold color palette, muted colors, "     "detailed, 8k" ) text_to_image.generate(     {         "prompts": prompt,         "negative_prompts": "green color",     } )`

If `inputs` are a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, outputs will be generated "batch-by-batch" and concatenated. Otherwise, all inputs will be processed as batches.

**Arguments**

*   **inputs**: python data, tensor data, or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    . The format must be one of the following:
    *   A single string
    *   A list of strings
    *   A dict with "prompts" and/or "negative\_prompts" keys
    *   A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
         with "prompts" and/or "negative\_prompts" keys
*   **num\_steps**: int. The number of diffusion steps to take.
*   **guidance\_scale**: Optional float. The classifier free guidance scale defined in [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598)
    . A higher scale encourages generating images more closely related to the prompts, typically at the cost of lower image quality. Note that some models don't utilize classifier-free guidance.
*   **seed**: optional int. Used as a random seed.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.FluxTextToImage.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[FluxTextToImage model](https://keras.io/keras_hub/api/models/flux/flux_text_to_image/#fluxtexttoimage-model)

[`FluxTextToImage` class](https://keras.io/keras_hub/api/models/flux/flux_text_to_image/#fluxtexttoimage-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/flux/flux_text_to_image/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/flux/flux_text_to_image/#backbone-property)

[`generate` method](https://keras.io/keras_hub/api/models/flux/flux_text_to_image/#generate-method)

[`preprocessor` property](https://keras.io/keras_hub/api/models/flux/flux_text_to_image/#preprocessor-property)