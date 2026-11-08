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
 / StableDiffusion3Backbone model

StableDiffusion3Backbone model
==============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/stable_diffusion_3/stable_diffusion_3_backbone.py#L170)

### `StableDiffusion3Backbone` class

Copied!

`keras_hub.models.StableDiffusion3Backbone(     mmdit_patch_size,     mmdit_hidden_dim,     mmdit_num_layers,     mmdit_num_heads,     mmdit_position_size,     mmdit_qk_norm,     mmdit_dual_attention_indices,     vae,     clip_l,     clip_g,     t5=None,     latent_channels=16,     output_channels=3,     num_train_timesteps=1000,     shift=3.0,     image_shape=(1024, 1024, 3),     data_format=None,     dtype=None,     **kwargs )`

Stable Diffusion 3 core network with hyperparameters.

This backbone imports CLIP and T5 models as text encoders and implements the base MMDiT and VAE networks for the Stable Diffusion 3 model.

The default constructor gives a fully customizable, randomly initialized MMDiT and VAE models with any hyperparameters. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **mmdit\_patch\_size**: int. The size of each square patch in the input image in MMDiT.
*   **mmdit\_hidden\_dim**: int. The size of the transformer hidden state at the end of each transformer layer in MMDiT.
*   **mmdit\_num\_layers**: int. The number of transformer layers in MMDiT.
*   **mmdit\_num\_heads**: int. The number of attention heads for each transformer in MMDiT.
*   **mmdit\_position\_size**: int. The size of the height and width for the position embedding in MMDiT.
*   **mmdit\_qk\_norm**: Optional str. Whether to normalize the query and key tensors for each transformer in MMDiT. Available options are `None` and `"rms_norm"`. Typically, this is set to `None` for 3.0 version and to `"rms_norm"` for 3.5 version.
*   **mmdit\_dual\_attention\_indices**: Optional tuple. Specifies the indices of the blocks that serve as dual attention blocks. Typically, this is for 3.5 version. Defaults to `None`.
*   **vae**: The VAE used for transformations between pixel space and latent space.
*   **clip\_l**: The CLIP text encoder for encoding the inputs.
*   **clip\_g**: The CLIP text encoder for encoding the inputs.
*   **t5**: optional The T5 text encoder for encoding the inputs.
*   **latent\_channels**: int. The number of channels in the latent. Defaults to `16`.
*   **output\_channels**: int. The number of channels in the output. Defaults to `3`.
*   **num\_train\_timesteps**: int. The number of diffusion steps to train the model. Defaults to `1000`.
*   **shift**: float. The shift value for the timestep schedule. Defaults to `3.0`.
*   **image\_shape**: tuple. The input shape without the batch size. Defaults to `(1024, 1024, 3)`.
*   **data\_format**: `None` or str. If specified, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch_size, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch_size, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done a float32 precision regardless of dtype.

**Example**

Copied!

`# Pretrained Stable Diffusion 3 model. model = keras_hub.models.StableDiffusion3Backbone.from_preset(     "stable_diffusion_3_medium" )  # Randomly initialized Stable Diffusion 3 model with custom config. vae = keras_hub.models.VAEBackbone(...) clip_l = keras_hub.models.CLIPTextEncoder(...) clip_g = keras_hub.models.CLIPTextEncoder(...) model = keras_hub.models.StableDiffusion3Backbone(     mmdit_patch_size=2,     mmdit_num_heads=4,     mmdit_hidden_dim=256,     mmdit_depth=4,     mmdit_position_size=192,     mmdit_qk_norm=None,     mmdit_dual_attention_indices=None,     vae=vae,     clip_l=clip_l,     clip_g=clip_g, )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`StableDiffusion3Backbone.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as a one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a ModelScope handle like `'modelscope://user/bert_base_en'`
5.  a path to a local preset directory like `'./bert_base_en'`

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Backbone.from_preset()`, or from a model class like `keras_hub.models.GemmaBackbone.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

For any `Backbone` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma backbone with pre-trained weights. model = keras_hub.models.Backbone.from_preset(     "gemma_2b_en", )  # Load a Bert backbone with a pre-trained config and random weights. model = keras_hub.models.Backbone.from_preset(     "bert_base_en",     load_weights=False, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [stable\_diffusion\_3\_medium](https://www.kaggle.com/models/keras/stablediffusion3/keras/stable_diffusion_3_medium/5) | 2.99B | 3 billion parameter, including CLIP L and CLIP G text encoders, MMDiT generative model, and VAE autoencoder. Developed by Stability AI. |
| [stable\_diffusion\_3.5\_medium](https://www.kaggle.com/models/keras/stablediffusion-3.5/keras/stable_diffusion_3.5_medium/1) | 3.37B | 3 billion parameter, including CLIP L and CLIP G text encoders, MMDiT-X generative model, and VAE autoencoder. Developed by Stability AI. |
| [stable\_diffusion\_3.5\_large](https://www.kaggle.com/models/keras/stablediffusion-3.5/keras/stable_diffusion_3.5_large/3) | 9.05B | 9 billion parameter, including CLIP L and CLIP G text encoders, MMDiT generative model, and VAE autoencoder. Developed by Stability AI. |
| [stable\_diffusion\_3.5\_large\_turbo](https://www.kaggle.com/models/keras/stablediffusion-3.5/keras/stable_diffusion_3.5_large_turbo/3) | 9.05B | 9 billion parameter, including CLIP L and CLIP G text encoders, MMDiT generative model, and VAE autoencoder. A timestep-distilled version that eliminates classifier-free guidance and uses fewer steps for generation. Developed by Stability AI. |

**Guides and examples using `from_preset`**

*   [Stable Diffusion 3](https://keras.io/keras_hub/guides/stable_diffusion_3_in_keras_hub/)
    
*   [A walk through latent space with Stable Diffusion 3](https://keras.io/examples/generative/random_walks_with_stable_diffusion_3/)
    
*   [DreamBooth](https://keras.io/examples/generative/dreambooth/)
    

* * *

[StableDiffusion3Backbone model](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_backbone/#stablediffusion3backbone-model)

[`StableDiffusion3Backbone` class](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_backbone/#stablediffusion3backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/stable_diffusion_3/stable_diffusion_3_backbone/#frompreset-method)