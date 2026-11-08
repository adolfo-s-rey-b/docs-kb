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
 / [Gemma3n](https://keras.io/keras_hub/api/models/gemma3n/)
 / Gemma3nCausalLM model

Gemma3nCausalLM model
=====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma3n/gemma3n_causal_lm.py#L19)

### `Gemma3nCausalLM` class

Copied!

`keras_hub.models.Gemma3nCausalLM(preprocessor, backbone, **kwargs)`

An end-to-end multimodal Gemma3n model for causal language modeling.

A causal language model (LM) predicts the next token based on previous tokens. This task setup can be used to train the model unsupervised on images, audio, and plain text inputs, or to autoregressively generate plain text similar to the data used for training. Note that the model is image-audio-text in, text out.

This model has a `generate()` method, which generates text based on a prompt. The generation strategy used is controlled by an additional `sampler` argument on `compile()`. You can recompile the model with different `keras_hub.samplers` objects to control the generation. By default, `"greedy"` sampling will be used.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to string inputs during `fit()`, `predict()`, `evaluate()` and `generate()`. This is done by default when creating the model with `from_preset()`.

**Arguments**

*   **preprocessor**: A [`keras_hub.models.Gemma3nCausalLMPreprocessor`](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm_preprocessor#gemma3ncausallmpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing, and inputs should be preprocessed before calling the model.
*   **backbone**: A [`keras_hub.models.Gemma3nBackbone`](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_backbone#gemma3nbackbone-class)
     instance.

**Examples**

Copied!

`import numpy as np from keras_hub.models import Gemma3nCausalLM  # === Text-only usage === # Load a text-only Gemma3n model from preset. causal_lm = Gemma3nCausalLM.from_preset("gemma3n_2b_it")  # Generate text. causal_lm.generate("What is the capital of France?", max_length=128)  # === Vision + Text usage === # Load a vision-text Gemma3n model from preset. causal_lm = Gemma3nCausalLM.from_preset("gemma3n_2b_it")  # Generate with image input. image = np.ones((768, 768, 3), dtype="float32") causal_lm.generate({     "prompts": "Describe this image: <start_of_image>",     "images": image })  # === Audio + Text usage === # Load an audio-text Gemma3n model from preset. causal_lm = Gemma3nCausalLM.from_preset("gemma3n_2b_it")  # Generate with audio input. audio = np.ones((16000,), dtype="float32") causal_lm.generate({     "prompts": "Transcribe this audio: <start_of_audio>",     "audios": audio })  # === Vision + Audio + Text usage === # Generate with both image and audio. causal_lm.generate({     "prompts": "Image: <start_of_image>, Audio: <start_of_audio>",     "images": image,     "audios": audio })`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`Gemma3nCausalLM.from_preset(preset, load_weights=True, **kwargs)`

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
| [gemma3n\_e2b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b/1) | 5.44B | Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e2b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b_it/1) | 5.44B | Instruction-tuned Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b/1) | 7.85B | Gemma 3n E4B multimodal with ( ~8B total ~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b_it/1) | 7.85B | Instruction-tuned Gemma 3n E4B multimodal with ~8B total (~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma3n/gemma3n_causal_lm.py#L437)

### `generate` method

Copied!

`Gemma3nCausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.Gemma3nCausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.Gemma3nCausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[Gemma3nCausalLM model](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm/#gemma3ncausallm-model)

[`Gemma3nCausalLM` class](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm/#gemma3ncausallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/gemma3n/gemma3n_causal_lm/#preprocessor-property)