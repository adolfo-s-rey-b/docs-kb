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
 / [Moonshine](https://keras.io/keras_hub/api/models/moonshine/)
 / MoonshineAudioToText model

MoonshineAudioToText model
==========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/moonshine/moonshine_audio_to_text.py#L16)

### `MoonshineAudioToText` class

Copied!

`keras_hub.models.MoonshineAudioToText(backbone, preprocessor=None, **kwargs)`

An end-to-end Moonshine model for audio-to-text tasks.

A Seq2Seq LM designed for audio-to-text tasks, such as speech recognition. The encoder processes audio features, and the decoder generates text transcriptions. You can finetune `MoonshineAudioToText` for any audio-to-text task (e.g., live transcription or voice commands).

This model includes a `generate()` method for text generation based on audio inputs and an optional text prompt for the decoder. The generation strategy is controlled by a `sampler` argument passed to `compile()`. By default, `"top_k"` sampling is used.

**Arguments**

*   **backbone**: A [`keras_hub.models.MoonshineBackbone`](https://keras.io/keras_hub/api/models/moonshine/moonshine_backbone#moonshinebackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.MoonshineAudioToTextPreprocessor`](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text_preprocessor#moonshineaudiototextpreprocessor-class)
     or `None`. If `None`, inputs must be preprocessed before calling the model.

**Examples**

Copied!

`# Initialize model from preset. moonshine_lm = keras_hub.models.MoonshineAudioToText.from_preset(     "moonshine_base" )  # Generate with single audio input. audio_tensor = keras.random.normal((1, 16000, 1)) moonshine_lm.generate({"audio": audio_tensor})  # Generate with text prompt. moonshine_lm.generate({"audio": audio_tensor, "text": "quick"})  # Use different sampling strategy. moonshine_lm.compile(sampler="greedy") moonshine_lm.generate({"audio": audio_tensor})`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`MoonshineAudioToText.from_preset(preset, load_weights=True, **kwargs)`

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
| [moonshine\_tiny\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_tiny_en/1) | 27.09M | Moonshine tiny model for English speech recognition. Developed by Useful Sensors for real-time transcription. |
| [moonshine\_base\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_base_en/1) | 61.51M | Moonshine base model for English speech recognition. Developed by Useful Sensors for real-time transcription. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`MoonshineAudioToText.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

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

`keras_hub.models.MoonshineAudioToText.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.MoonshineAudioToText.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[MoonshineAudioToText model](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text/#moonshineaudiototext-model)

[`MoonshineAudioToText` class](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text/#moonshineaudiototext-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/moonshine/moonshine_audio_to_text/#preprocessor-property)