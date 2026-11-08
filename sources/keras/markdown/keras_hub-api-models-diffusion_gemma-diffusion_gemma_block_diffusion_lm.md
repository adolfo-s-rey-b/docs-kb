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
 / [DiffusionGemma](https://keras.io/keras_hub/api/models/diffusion_gemma/)
 / DiffusionGemmaBlockDiffusionLM model

DiffusionGemmaBlockDiffusionLM model
====================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm.py#L17)

### `DiffusionGemmaBlockDiffusionLM` class

Copied!

`keras_hub.models.DiffusionGemmaBlockDiffusionLM(     preprocessor,     backbone,     canvas_length=256,     max_denoising_steps=48,     t_min=0.4,     t_max=0.8,     sampler="entropy_bound",     stop_token_ids=None,     pad_token_id=None,     **kwargs )`

DiffusionGemma discrete block-diffusion language model.

Wraps a `DiffusionGemmaBackbone` with the block-diffusion generation loop from `BlockDiffusionLM`. The backbone is called twice per generation iteration: once as a causal encoder to freeze prompt KV caches, and up to `max_denoising_steps` times as a bidirectional decoder over a fixed-length canvas of tokens.

Supports both text-only and multimodal (image) prompts. Vision embeddings are pre-scaled by `1/sqrt(hidden_dim)` before interleaving so that the global `embed_scale` factor does not distort them.

**Arguments**

*   **preprocessor**: A [`keras_hub.models.DiffusionGemmaBlockDiffusionLMPreprocessor`](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm_preprocessor#diffusiongemmablockdiffusionlmpreprocessor-class)
     or `None`.
*   **backbone**: A [`keras_hub.models.DiffusionGemmaBackbone`](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_backbone#diffusiongemmabackbone-class)
     instance.
*   **canvas\_length**: int. Number of tokens in the denoising canvas. Defaults to `256`.
*   **max\_denoising\_steps**: int. Maximum number of denoising iterations per canvas block. Defaults to `48`.
*   **t\_min**: float. Minimum sampling temperature applied at the last denoising step. Defaults to `0.4`.
*   **t\_max**: float. Maximum sampling temperature applied at the first denoising step. Defaults to `0.8`.
*   **sampler**: `"entropy_bound"` or a compatible diffusion sampler. Defaults to `"entropy_bound"`.
*   **stop\_token\_ids**: Optional tuple of token IDs that finish generation. Defaults to `None`.
*   **pad\_token\_id**: Optional int token ID used after the first stop token. Defaults to `None`.
*   **\*\*kwargs**: Additional keyword arguments passed to the parent class.

**Examples**

Text generation from a text prompt.

Copied!

`model = keras_hub.models.DiffusionGemmaBlockDiffusionLM.from_preset(     "diffusion_gemma_26b_a4b_it", ) model.generate("The quick brown fox")`

Image + text generation.

Copied!

`model = keras_hub.models.DiffusionGemmaBlockDiffusionLM.from_preset(     "diffusion_gemma_26b_a4b_it", ) model.generate({     "prompts": "Describe this image: <|image|>",     "images": image_array,  # np.ndarray of shape (H, W, 3) })`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`DiffusionGemmaBlockDiffusionLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [diffusion\_gemma\_26b\_a4b\_it](https://www.kaggle.com/models/keras/diffusion-gemma/keras/diffusion_gemma_26b_a4b_it/1) | 25.82B | DiffusionGemma 26B MoE instruction-tuned model. 25.8B total parameters (3.8B active), 30 layers, 128 experts. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm.py#L77)

### `generate` method

Copied!

`DiffusionGemmaBlockDiffusionLM.generate(     inputs,     max_length=None,     stop_token_ids="auto",     sequence_length=None,     t_min=None,     t_max=None,     pad_token_id="auto", )`

Generate a denoised canvas given prompt inputs.

**Arguments**

*   **inputs**: python data, tensor data, or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    . If a `preprocessor` is attached to the model, `inputs` should match the structure expected by the `preprocessor` layer. If a `preprocessor` is not attached, `inputs` should match the structure expected by the `backbone` model.
*   **max\_length**: Optional int. Maximum length of the generated sequence. Defaults to the model's configured canvas length.
*   **stop\_token\_ids**: Optional. `None`, `"auto"`, or tuple of token IDs. Defaults to `"auto"`, which uses stop IDs configured on the model, or the preprocessor tokenizer's end token plus `<turn|>` (DiffusionGemma's end-of-turn token). `None` generates until `max_length`.
*   **sequence\_length**: Optional int. Overrides the preprocessor's prompt packing length. Raises `ValueError` if the prompt does not fit. Defaults to `None`.
*   **t\_min**: Optional float. Sampling temperature minimum. Defaults to `self.t_min`.
*   **t\_max**: Optional float. Sampling temperature maximum. Defaults to `self.t_max`.
*   **pad\_token\_id**: Optional int. Overrides the model's configured padding token. `None` disables padding. Defaults to `"auto"`, which uses `self.pad_token_id`.

**Returns**

Decoded string(s) or integer token arrays, depending on whether a `preprocessor` is attached.

* * *

### `backbone` property

Copied!

`keras_hub.models.DiffusionGemmaBlockDiffusionLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.DiffusionGemmaBlockDiffusionLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[DiffusionGemmaBlockDiffusionLM model](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm/#diffusiongemmablockdiffusionlm-model)

[`DiffusionGemmaBlockDiffusionLM` class](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm/#diffusiongemmablockdiffusionlm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_block_diffusion_lm/#preprocessor-property)