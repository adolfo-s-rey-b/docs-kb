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
 / [Stable Diffusion 3](https://keras.io/keras_hub/api/models/stable_diffusion_3/)
 / StableDiffusion3ImageToImage model

StableDiffusion3ImageToImage model
==================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/stable_diffusion_3/stable_diffusion_3_image_to_image.py#L13)

### `StableDiffusion3ImageToImage` class

Copied!

`keras_hub.models.StableDiffusion3ImageToImage(backbone, preprocessor, **kwargs)`

An end-to-end Stable Diffusion 3 model for image-to-image generation.

This model has a `generate()` method, which generates images based on a combination of a reference image and a text prompt.

**Arguments**

*   **backbone**: A [`keras_hub.models.StableDiffusion3Backbone`](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_backbone#stablediffusion3backbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.StableDiffusion3TextToImagePreprocessor`](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_text_to_image_preprocessor#stablediffusion3texttoimagepreprocessor-class)
     instance.

**Examples**

Use `generate()` to do image generation.

Copied!

``prompt = (     "Astronaut in a jungle, cold color palette, muted colors, "     "detailed, 8k" ) image_to_image = keras_hub.models.StableDiffusion3ImageToImage.from_preset(     "stable_diffusion_3_medium", image_shape=(512, 512, 3) ) image_to_image.generate(     {         "images": np.ones((512, 512, 3), dtype="float32"),         "prompts": prompt,     } )  # Generate with batched prompts. image_to_image.generate(     {         "images": np.ones((2, 512, 512, 3), dtype="float32"),         "prompts": [             "cute wallpaper art of a cat",             "cute wallpaper art of a dog",         ],     } )  # Generate with different `num_steps`, `guidance_scale` and `strength`. image_to_image.generate(     {         "images": np.ones((512, 512, 3), dtype="float32"),         "prompts": prompt,     }     num_steps=50,     guidance_scale=5.0,     strength=0.6, )  # Generate with `negative_prompts`. text_to_image.generate(     {         "images": np.ones((512, 512, 3), dtype="float32"),         "prompts": prompt,         "negative_prompts": "green color",     } )``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`StableDiffusion3ImageToImage.from_preset(preset, load_weights=True, **kwargs)`

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

### `backbone` property

Copied!

`keras_hub.models.StableDiffusion3ImageToImage.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/stable_diffusion_3/stable_diffusion_3_image_to_image.py#L164)

### `generate` method

Copied!

`StableDiffusion3ImageToImage.generate(     inputs, num_steps=50, strength=0.8, guidance_scale=7.0, seed=None )`

Generate image based on the provided `inputs`.

Typically, `inputs` is a dict with `"images"` and `"prompts"` keys. `"images"` are reference images within a value range of `[-1.0, 1.0]`, which will be resized to `self.backbone.height` and `self.backbone.width`, then encoded into latent space by the VAE encoder. `"prompts"` are strings that will be tokenized and encoded by the text encoder.

Some models support a `"negative_prompts"` key, which helps steer the model away from generating certain styles and elements. To enable this, add `"negative_prompts"` to the input dict.

If `inputs` are a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, outputs will be generated "batch-by-batch" and concatenated. Otherwise, all inputs will be processed as batches.

**Arguments**

*   **inputs**: python data, tensor data, or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    . The format must be one of the following:
    *   A dict with `"images"`, `"prompts"` and/or `"negative_prompts"` keys.
    *   A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
         with `"images"`, `"prompts"` and/or `"negative_prompts"` keys.
*   **num\_steps**: int. The number of diffusion steps to take.
*   **strength**: float. Indicates the extent to which the reference `images` are transformed. Must be between `0.0` and `1.0`. When `strength=1.0`, `images` is essentially ignore and added noise is maximum and the denoising process runs for the full number of iterations specified in `num_steps`.
*   **guidance\_scale**: Optional float. The classifier free guidance scale defined in [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598)
    . A higher scale encourages generating images more closely related to the prompts, typically at the cost of lower image quality. Note that some models don't utilize classifier-free guidance.
*   **seed**: optional int. Used as a random seed.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.StableDiffusion3ImageToImage.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[StableDiffusion3ImageToImage model](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_image_to_image/#stablediffusion3imagetoimage-model)

[`StableDiffusion3ImageToImage` class](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_image_to_image/#stablediffusion3imagetoimage-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_image_to_image/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_image_to_image/#backbone-property)

[`generate` method](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_image_to_image/#generate-method)

[`preprocessor` property](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_image_to_image/#preprocessor-property)