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
 / [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 / TextToImage

TextToImage
===========

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/text_to_image.py#L17)

### `TextToImage` class

Copied!

`keras_hub.models.TextToImage()`

Base class for text-to-image tasks.

`TextToImage` tasks wrap a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be used for generation and generative fine-tuning.

`TextToImage` tasks provide an additional, high-level `generate()` function which can be used to generate image by token with a string in, image out signature.

All `TextToImage` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and weights.

**Example**

Copied!

`# Load a Stable Diffusion 3 backbone with pre-trained weights. text_to_image = keras_hub.models.TextToImage.from_preset(     "stable_diffusion_3_medium", ) text_to_image.generate(     "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k" )  # Load a Stable Diffusion 3 backbone at bfloat16 precision. text_to_image = keras_hub.models.TextToImage.from_preset(     "stable_diffusion_3_medium",     dtype="bfloat16", ) text_to_image.generate(     "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k" )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`TextToImage.from_preset(preset, load_weights=True, **kwargs)`

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
| [stable\_diffusion\_3\_medium](https://www.kaggle.com/models/keras/stablediffusion3/keras/stable_diffusion_3_medium/5) | 2.99B | 3 billion parameter, including CLIP L and CLIP G text encoders, MMDiT generative model, and VAE autoencoder. Developed by Stability AI. |
| [stable\_diffusion\_3.5\_medium](https://www.kaggle.com/models/keras/stablediffusion-3.5/keras/stable_diffusion_3.5_medium/1) | 3.37B | 3 billion parameter, including CLIP L and CLIP G text encoders, MMDiT-X generative model, and VAE autoencoder. Developed by Stability AI. |
| [stable\_diffusion\_3.5\_large](https://www.kaggle.com/models/keras/stablediffusion-3.5/keras/stable_diffusion_3.5_large/3) | 9.05B | 9 billion parameter, including CLIP L and CLIP G text encoders, MMDiT generative model, and VAE autoencoder. Developed by Stability AI. |
| [stable\_diffusion\_3.5\_large\_turbo](https://www.kaggle.com/models/keras/stablediffusion-3.5/keras/stable_diffusion_3.5_large_turbo/3) | 9.05B | 9 billion parameter, including CLIP L and CLIP G text encoders, MMDiT generative model, and VAE autoencoder. A timestep-distilled version that eliminates classifier-free guidance and uses fewer steps for generation. Developed by Stability AI. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/text_to_image.py#L68)

### `compile` method

Copied!

`TextToImage.compile(optimizer="auto", loss="auto", metrics="auto", **kwargs)`

Configures the `TextToImage` task for training.

The `TextToImage` task extends the default compilation signature of [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
 with defaults for `optimizer`, `loss`, and `metrics`. To override these defaults, pass any value to these arguments during compilation.

**Arguments**

*   **optimizer**: `"auto"`, an optimizer name, or a `keras.Optimizer` instance. Defaults to `"auto"`, which uses the default optimizer for the given model and task. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
     and `keras.optimizers` for more info on possible `optimizer` values.
*   **loss**: `"auto"`, a loss name, or a [`keras.losses.Loss`](https://keras.io/api/losses#loss-class)
     instance. Defaults to `"auto"`, where a [`keras.losses.MeanSquaredError`](https://keras.io/api/losses/regression_losses#meansquarederror-class)
     loss will be applied. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
     and `keras.losses` for more info on possible `loss` values.
*   **metrics**: `"auto"`, or a list of metrics to be evaluated by the model during training and testing. Defaults to `"auto"`, where a [`keras.metrics.MeanSquaredError`](https://keras.io/api/metrics/regression_metrics#meansquarederror-class)
     will be applied to track the loss of the model during training. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
     and `keras.metrics` for more info on possible `metrics` values.
*   **\*\*kwargs**: See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
     for a full list of arguments supported by the compile method.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L271)

### `save_to_preset` method

Copied!

`TextToImage.save_to_preset(preset_dir, max_shard_size=10)`

Save task to a preset directory.

**Arguments**

*   **preset\_dir**: The path to the local model preset directory.
*   **max\_shard\_size**: `int` or `float`. Maximum size in GB for each sharded file. If `None`, no sharding will be done. Defaults to `10`.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.TextToImage.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

### `backbone` property

Copied!

`keras_hub.models.TextToImage.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/text_to_image.py#L248)

### `generate` method

Copied!

`TextToImage.generate(inputs, num_steps, guidance_scale=None, seed=None)`

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

[TextToImage](https://keras.io/keras_hub/api/base_classes/text_to_image/#texttoimage)

[`TextToImage` class](https://keras.io/keras_hub/api/base_classes/text_to_image/#texttoimage-class)

[`from_preset` method](https://keras.io/keras_hub/api/base_classes/text_to_image/#frompreset-method)

[`compile` method](https://keras.io/keras_hub/api/base_classes/text_to_image/#compile-method)

[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/text_to_image/#savetopreset-method)

[`preprocessor` property](https://keras.io/keras_hub/api/base_classes/text_to_image/#preprocessor-property)

[`backbone` property](https://keras.io/keras_hub/api/base_classes/text_to_image/#backbone-property)

[`generate` method](https://keras.io/keras_hub/api/base_classes/text_to_image/#generate-method)