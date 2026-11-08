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
 / [Gemma3](https://keras.io/keras_hub/api/models/gemma3/)
 / Gemma3CausalLMPreprocessor layer

Gemma3CausalLMPreprocessor layer
================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma3/gemma3_causal_lm_preprocessor.py#L24)

### `Gemma3CausalLMPreprocessor` class

Copied!

`keras_hub.models.Gemma3CausalLMPreprocessor(     tokenizer,     image_converter=None,     sequence_length=1024,     add_start_token=True,     add_end_token=True,     max_images_per_prompt=2,     num_vision_tokens_per_image=256,     **kwargs )`

Gemma3 Causal LM preprocessor.

This preprocessing layer is meant for use with [`keras_hub.models.Gemma3CausalLM`](https://keras.io/keras_hub/api/models/gemma3/gemma3_causal_lm#gemma3causallm-class)
. It can be configured in two ways: text-only and text + vision, based on whether the passed value of `image_converter` is None. For the former, it takes in batches of strings, whereas for the latter, it takes in batches of images and strings. It returns outputs in a `(x, y, sample_weight)` format, where the `y` label is the next token id in the `x` sequence. `sample_weight` is 0 for "prompt" tokens, and 1 for "response" tokens, so that the loss is computed only on the "response" tokens.

For the text + vision case, this layer replaces instance of `<start_of_image>` token in the prompt with `num_vision_tokens_per_image` placeholder tokens. It also returns indices of where these vision tokens are present so that in the model, image embeddings can be placed in the right position in the sequence of text embeddings. Note that if `max_images_per_prompt` is 2, you can pass either 0, 1, 2 images per sample. The value 0 corresponds to text-only input.

For use with generation, the layer also exposes two methods `generate_preprocess()` and `generate_postprocess()`. When this preprocessor is attached to a [`keras_hub.models.Gemma3CausalLM`](https://keras.io/keras_hub/api/models/gemma3/gemma3_causal_lm#gemma3causallm-class)
 instance, these methods will be called implicitly in `generate()`. They can also be called standalone (e.g. to precompute preprocessing inputs for generation in a separate process).

**Arguments**

*   **tokenizer**: A `keras_hub.models.Gemma3Tokenizer` instance.
*   **image\_converter**: A [`keras_hub.layers.ImageConverter`](https://keras.io/keras_hub/api/preprocessing_layers/image_converter#imageconverter-class)
     instance. Defaults to `None`.
*   **sequence\_length**: The length of the packed inputs. Defaults to 1024.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence. Defaults to `True`.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence. Defaults to `True`.
*   **max\_images\_per\_prompt**: int. Permissible number of images per sample in the batch. Defaults to 2.
*   **num\_vision\_tokens\_per\_image**: int. Number of vision placeholder tokens per image. Defaults to 256.

**Call arguments**

*   **x**: A string, [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or list of python strings.
*   **y**: Label data. Should always be `None` as the layer generates labels.
*   **sample\_weight**: Label weights. Should always be `None` as the layer generates label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.

**Examples**

Copied!

``# === Language Gemma3 model === # Load the preprocessor from a preset. preprocessor = keras_hub.models.Gemma3CausalLMPreprocessor.from_preset(     "gemma3_instruct_1b" )  # Unbatched inputs. preprocessor(     {         "prompts": "What is the capital of India?",         "responses": "New Delhi",     } )  # Batched inputs. preprocessor(     {         "prompts": [             "What is the capital of India?",             "What is the capital of Spain?"         ],         "responses": ["New Delhi", "Madrid"],     } )  # Apply preprocessing to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). features = {     "prompts": [         "What is the capital of India?",         "What is the capital of Spain?"     ],     "responses": ["New Delhi", "Madrid"], }  ds = tf.data.Dataset.from_tensor_slices(features) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Prepare tokens for generation (no end token). preprocessor.generate_preprocess(["The quick brown fox jumped."])  # Map generation outputs back to strings. preprocessor.generate_postprocess({     'token_ids': np.array([[2, 818, 3823, 8864, 37423, 32694, 236761, 0]]),     'padding_mask': np.array([[ 1, 1, 1, 1, 1, 1, 1, 0]]), })  # === Vision and Language Gemma3 model === # Load the preprocessor from a preset. preprocessor = keras_hub.models.Gemma3CausalLMPreprocessor.from_preset(     "gemma3_instruct_4b" )  # text-only inputs (unbatched) preprocessor(     {         "prompts": "What is the capital of India?",         "responses": "New Delhi",     } )  # text-only inputs (batched) preprocessor(     {         "prompts": [             "What is the capital of India?",             "What is the capital of Spain?"         ],         "responses": ["New Delhi", "Madrid"],     } )  # Unbatched inputs, with one image. preprocessor(     {         "prompts": "this is a lily <start_of_image>",         "responses": "pristine!",         "images": np.ones((896, 896, 3), dtype="float32")     } )  # Unbatched inputs, with two images. preprocessor(     {         "prompts": "lily: <start_of_image>, sunflower: <start_of_image>",         "responses": "pristine!",         "images": [             np.ones((896, 896, 3), dtype="float32"),             np.ones((896, 896, 3), dtype="float32")         ],     } )  # Batched inputs, one image per prompt. preprocessor(     {         "prompts": [             "this is a lily: <start_of_image>",             "this is a sunflower: <start_of_image>"         ],         "responses": ["pristine!", "radiant!"],         "images": [             np.ones((896, 896, 3), dtype="float32"),             np.ones((896, 896, 3), dtype="float32")         ]     } )  # Can also be written this way. preprocessor(     {         "prompts": [             "this is a lily: <start_of_image>",             "this is a sunflower: <start_of_image>"         ],         "responses": ["pristine!", "radiant!"],         "images": [             [np.ones((896, 896, 3), dtype="float32")],             [np.ones((896, 896, 3), dtype="float32")]         ]     } )  # Different number of images in every sample. preprocessor(     {         "prompts": [             "Who is this singer: <start_of_image>?",             "Who are these musicians <start_of_image>, <start_of_image>?"         ],         "responses": ["Arijit Singh", "John Lennon, Paul Mccartney"],         "images": [             [                 np.ones((896, 896, 3), dtype="float32"),                 np.ones((896, 896, 3), dtype="float32")             ],             [np.ones((896, 896, 3), dtype="float32")]         ]     } )  # Apply preprocessing to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). inputs = {     "prompts": [         "Who are these two: <start_of_image>, <start_of_image>",         "Who is this: <start_of_image>?",         "What is the capital of India?"     ],     "responses": [         "John Lennon, Paul Mccartney",         "Arijit Singh",         "New Delhi"     ],     "images": (         tf.ragged.constant(             [                 [np.ones((10, 10, 3)), np.ones((10, 10, 3))],                 [np.ones((10, 10, 3))],                 [],             ]         )     ) } ds = tf.data.Dataset.from_tensor_slices(inputs) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`Gemma3CausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

Instantiate a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Preprocessor` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

As there are usually multiple preprocessing classes for a given model, this method should be called on a specific subclass like `keras_hub.models.BertTextClassifierPreprocessor.from_preset()`.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a preprocessor for Gemma generation. preprocessor = keras_hub.models.CausalLMPreprocessor.from_preset(     "gemma_2b_en", )  # Load a preprocessor for Bert classification. preprocessor = keras_hub.models.TextClassifierPreprocessor.from_preset(     "bert_base_en", )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [gemma3\_270m](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_270m/3) | 268.10M | 270-million parameter(170m embedding,100m transformer params) model, 18-layer, text-only designed for hyper-efficient AI, particularly for task-specific fine-tuning. |
| [gemma3\_instruct\_270m](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_270m/4) | 268.10M | 270-million parameter(170m embedding,100m transformer params) model, 18-layer, text-only,instruction-tuned model designed for hyper-efficient AI, particularly for task-specific fine-tuning. |
| [function\_gemma\_instruct\_270m](https://www.kaggle.com/models/keras/function-gemma/keras/function_gemma_instruct_270m/1) | 268.10M | A 270M Million parameter text-only model based on Gemma 3. This model is trained specifically for function calling improvements. |
| [harrier\_embedding\_oss\_270m](https://www.kaggle.com/models/keras/harrier/keras/harrier_embedding_oss_270m/1) | 268.10M | Microsoft harrier-oss-v1 270M multilingual text embedding model based on the Gemma3-270M architecture, fine-tuned for dense retrieval and semantic similarity across 94+ languages. Achieves 66.5 on Multilingual MTEB v2. |
| [embedding\_gemma3\_300m](https://www.kaggle.com/models/keras/embeddinggemma/keras/embedding_gemma3_300m/2) | 307.58M | Embedding-focused Gemma 3 model (300M parameters, 24 layers). |
| [gemma3\_1b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_1b/3) | 999.89M | 1 billion parameter, 26-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_1b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_1b/3) | 999.89M | 1 billion parameter, 26-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_4b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_4b_text/2) | 3.88B | 4 billion parameter, 34-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_4b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_4b_text/3) | 3.88B | 4 billion parameter, 34-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_4b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_4b/1) | 4.30B | 4 billion parameter, 34-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_4b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_4b/1) | 4.30B | 4 billion parameter, 34-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_4b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_4b_it/1) | 4.30B | 4 billion parameter, 34-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [medgemma\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_4b/1) | 4.30B | A 4 billion parameter model based on Gemma 3. This model is pre-trained for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [medgemma\_instruct\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_4b/1) | 4.30B | A 4 billion parameter model based on Gemma 3. This model is instruction-tuned for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [medgemma\_1.5\_instruct\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_1.5_instruct_4b/1) | 4.30B | A 4 billion parameter,Instruct-tuned MedGemma 1.5 4B is an updated version of the Instruction-tuned MedGemma 4B model. |
| [gemma3\_12b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_12b_text/3) | 11.77B | 12 billion parameter, 48-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_12b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_12b_text/3) | 11.77B | 12 billion parameter, 48-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_12b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_12b/2) | 12.19B | 12 billion parameter, 48-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_12b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_12b/2) | 12.19B | 12 billion parameter, 48-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_12b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_12b_it/1) | 12.19B | 12 billion parameter, 48-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [gemma3\_27b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_27b_text/4) | 27.01B | 27 billion parameter, 62-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_27b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_27b_text/3) | 27.01B | 27 billion parameter, 62-layer, text-only instruction-tuned Gemma3 model. |
| [medgemma\_instruct\_27b\_text](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_27b_text/1) | 27.01B | A 27 billion parameter text-only model based on Gemma 3. This model is instruction-tuned (No images) for performance on medical text comprehension and is optimized for medical applications that involve a text generation component. |
| [gemma3\_27b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_27b/2) | 27.43B | 27 billion parameter, 62-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_27b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_27b/2) | 27.43B | 27 billion parameter, 62-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_27b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_27b_it/1) | 27.43B | 27 billion parameter, 62-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [medgemma\_instruct\_27b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_27b/1) | 27.43B | A 27 billion parameter model based on Gemma 3. This model is instruction-tuned for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |

**Guides and examples using `from_preset`**

*   [Exporting Keras models to LiteRT](https://keras.io/guides/litert_export/)
    

* * *

### `tokenizer` property

Copied!

`keras_hub.models.Gemma3CausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[Gemma3CausalLMPreprocessor layer](https://keras.io/keras_hub/api/models/gemma3/gemma3_causal_lm_preprocessor/#gemma3causallmpreprocessor-layer)

[`Gemma3CausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/gemma3/gemma3_causal_lm_preprocessor/#gemma3causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma3/gemma3_causal_lm_preprocessor/#frompreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/models/gemma3/gemma3_causal_lm_preprocessor/#tokenizer-property)