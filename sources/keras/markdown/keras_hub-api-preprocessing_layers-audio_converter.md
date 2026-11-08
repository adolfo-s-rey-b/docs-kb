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
 / [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 / AudioConverter layer

AudioConverter layer
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/audio_converter.py#L12)

### `AudioConverter` class

Copied!

`keras_hub.layers.AudioConverter(**kwargs)`

Convert raw audio for models that support audio input.

This class converts from raw audio tensors of any length, to preprocessed audio for pretrained model inputs. It is meant to be a convenient way to write custom preprocessing code that is not model specific. This layer should be instantiated via the `from_preset()` constructor, which will create the correct subclass of this layer for the model preset.

The layer will take as input a raw audio tensor with shape `(batch_size, num_samples)`, and output a preprocessed audio input for modeling. The exact structure of the preprocessed input will vary per model. Preprocessing will often include computing a spectogram of the raw audio signal.

**Examples**

Copied!

`# Load an audio converter from a preset. converter = keras_hub.layers.AudioConverter.from_preset("whisper_base_en") # Convert some raw audio input. converter(np.ones(2, 1_000))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/audio_converter.py#L47)

### `from_preset` method

Copied!

`AudioConverter.from_preset(preset, **kwargs)`

Instantiate a [`keras_hub.layers.AudioConverter`](https://keras.io/keras_hub/api/preprocessing_layers/audio_converter#audioconverter-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'whisper_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/whisper/keras/whisper_base_en'`
3.  a Hugging Face handle like `'hf://user/whisper_base_en'`
4.  a path to a local preset directory like `'./whisper_base_en'`

You can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.AudioConverter.from_preset()`, or from a model class like `keras_hub.models.WhisperAudioConverter.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load an audio converter from a preset. converter = keras_hub.layers.AudioConverter.from_preset(     "whisper_base_en" ) # Convert some raw mono channel audio input. converter(np.ones(2, 1_000))`

| Preset | Parameters | Description |
| --- | --- | --- |
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |
| [gemma3n\_e2b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b/1) | 5.44B | Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e2b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e2b_it/1) | 5.44B | Instruction-tuned Gemma 3n E2B multimodal model (~5B total, ~2B effective parameters) supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b/1) | 7.85B | Gemma 3n E4B multimodal with ( ~8B total ~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |
| [gemma3n\_e4b\_it](https://www.kaggle.com/models/keras/gemma-3n/keras/gemma3n_e4b_it/1) | 7.85B | Instruction-tuned Gemma 3n E4B multimodal with ~8B total (~4B effective parameters ), supporting multimodal inputs and optimized for on-device deployment. |
| [gemma4\_instruct\_2b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_2b_assistant/1) | 77.73M | Gemma 4 E2B MTP Assistant model: 4-layer speculative-decoding assistant for the 2B-it model. Uses Multi-Token Prediction to propose candidate tokens and achieve inference speedups. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_4b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_4b_assistant/1) | 77.73M | Gemma 4 E4B MTP Assistant model: 4-layer speculative-decoding assistant for the 4B-it model. Uses Multi-Token Prediction to propose candidate tokens and achieve inference speedups. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_26b\_a4b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_26b_a4b_assistant/1) | 412.76M | Gemma 4 26B A4B MTP Assistant model: 4-layer speculative-decoding assistant for the 26B MoE model. Uses Multi-Token Prediction and a standard logit head to propose candidates. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_31b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_31b_assistant/1) | 454.71M | Gemma 4 31B MTP Assistant model: 4-layer speculative-decoding assistant for the 31B dense model. Uses Multi-Token Prediction and a standard logit head to propose candidates. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_2b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_2b/2) | 5.10B | Gemma 4 E2B base model: 2.3B effective parameters (5.1B total with Per-Layer Embeddings), 35-layer, audio+vision+text pretrained Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_instruct\_2b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_2b/2) | 5.10B | Gemma 4 E2B instruction-tuned model: 2.3B effective parameters (5.1B total with Per-Layer Embeddings), 35-layer, audio+vision+text instruction-tuned Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_4b/2) | 7.90B | Gemma 4 E4B base model: 4.5B effective parameters (7.9B total with Per-Layer Embeddings), 42-layer, audio+vision+text pretrained Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_instruct\_4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_4b/2) | 7.90B | Gemma 4 E4B instruction-tuned model: 4.5B effective parameters (7.9B total with Per-Layer Embeddings), 42-layer, audio+vision+text instruction-tuned Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_26b\_a4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_26b_a4b/2) | 26.00B | Gemma 4 26B A4B base model: Mixture-of-Experts (MoE) model with 26B total parameters and only 4B active parameters per forward pass, 30-layer, vision+text pretrained Gemma4 model. The 'A' denotes active parameters — by activating only a 4B subset during inference, this MoE model runs nearly as fast as a dense 4B model. |
| [gemma4\_instruct\_26b\_a4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_26b_a4b/2) | 26.00B | Gemma 4 26B A4B instruction-tuned model: Mixture-of-Experts (MoE) model with 26B total parameters and only 4B active parameters per forward pass, 30-layer, vision+text instruction-tuned Gemma4 model. The 'A' denotes active parameters — by activating only a 4B subset during inference, this MoE model runs nearly as fast as a dense 4B model. |
| [gemma4\_31b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_31b/2) | 31.00B | Gemma 4 31B base model: 31B parameter, 60-layer, dense vision+text pretrained Gemma4 model. The dense model in the Gemma 4 family, offering maximum quality for deployments where inference speed is less of a constraint. |
| [gemma4\_instruct\_31b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_31b/2) | 31.00B | Gemma 4 31B instruction-tuned model: 31B parameter, 60-layer, dense vision+text instruction-tuned Gemma4 model. The dense model in the Gemma 4 family, offering maximum quality for deployments where inference speed is less of a constraint. |
| [moonshine\_tiny\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_tiny_en/1) | 27.09M | Moonshine tiny model for English speech recognition. Developed by Useful Sensors for real-time transcription. |
| [moonshine\_base\_en](https://www.kaggle.com/models/keras/moonshine/Keras/moonshine_base_en/1) | 61.51M | Moonshine base model for English speech recognition. Developed by Useful Sensors for real-time transcription. |
| [whisper\_tiny\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_tiny_en/4) | 37.18M | 4-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_tiny\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_tiny_multi/4) | 37.76M | 4-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_base\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_base_multi/4) | 72.59M | 6-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_base\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_base_en/4) | 124.44M | 6-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_small\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_small_en/4) | 241.73M | 12-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_small\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_small_multi/4) | 241.73M | 12-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_medium\_en](https://www.kaggle.com/models/keras/whisper/keras/whisper_medium_en/4) | 763.86M | 24-layer Whisper model. Trained on 438,000 hours of labelled English speech data. |
| [whisper\_medium\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_medium_multi/4) | 763.86M | 24-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_large\_multi](https://www.kaggle.com/models/keras/whisper/keras/whisper_large_multi/4) | 1.54B | 32-layer Whisper model. Trained on 680,000 hours of labelled multilingual speech data. |
| [whisper\_large\_multi\_v2](https://www.kaggle.com/models/keras/whisper/keras/whisper_large_multi_v2/4) | 1.54B | 32-layer Whisper model. Trained for 2.5 epochs on 680,000 hours of labelled multilingual speech data. An improved of `whisper_large_multi`. |

* * *

[AudioConverter layer](https://keras.io/keras_hub/api/preprocessing_layers/audio_converter/#audioconverter-layer)

[`AudioConverter` class](https://keras.io/keras_hub/api/preprocessing_layers/audio_converter/#audioconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/preprocessing_layers/audio_converter/#frompreset-method)