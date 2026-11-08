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
 / CausalLMPreprocessor

CausalLMPreprocessor
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm_preprocessor.py#L11)

### `CausalLMPreprocessor` class

Copied!

`keras_hub.models.CausalLMPreprocessor(     tokenizer, sequence_length=1024, add_start_token=True, add_end_token=True, **kwargs )`

Base class for causal language modeling preprocessing layers.

`CausalLMPreprocessor` tasks wrap a `keras_hub.tokenizer.Tokenizer` to create a preprocessing layer for causal language modeling tasks. It is intended to be paired with a `keras.models.CausalLM` task.

All `CausalLMPreprocessor` take inputs a single input. This can be a single string or a batch of strings. See examples below. These inputs will be tokenized and padded/truncated to a fixed sequence length.

This layer will always output a `(x, y, sample_weight)` tuple, where `x` is a dictionary with the tokenized inputs, `y` contains the tokens from `x` offset by 1, and `sample_weight` marks where `y` contains padded values. The exact contents of `x` will vary depending on the model being used.

a `CausalLMPreprocessor` contains two extra methods, `generate_preprocess` and `generate_postprocess` for use with generation. See examples below.

All `CausalLMPreprocessor` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and vocabularies. You can call the `from_preset()` constructor directly on this base class, in which case the correct class for you model will be automatically instantiated.

Examples.

Copied!

``preprocessor = keras_hub.models.CausalLMPreprocessor.from_preset(     "bert_base_en_uncased",     sequence_length=256, # Optional. )  # Tokenize, mask and pack a single sentence. x = "The quick brown fox jumped." x, y, sample_weight = preprocessor(x)  # Tokenize and pad/truncate a batch of labeled sentences. x = ["The quick brown fox jumped.", "Call me Ishmael."] x, y, sample_weight = preprocessor(x)  # With a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). ds = tf.data.Dataset.from_tensor_slices(x) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)  # Generate preprocess and postprocess. x = preprocessor.generate_preprocess(x)  # Tokenized numeric inputs. x = preprocessor.generate_postprocess(x)  # Detokenized string outputs.``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`CausalLMPreprocessor.from_preset(preset, config_file="preprocessor.json", **kwargs)`

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
| [blip2\_opt\_2.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_2.7b/1) | 3.74B | BLIP-2 model using OPT-2.7B as the frozen language model. |
| [blip2\_flan\_t5\_xl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xl/1) | 3.94B | BLIP-2 model using Flan-T5-XL (~3B) as the frozen language model. |
| [blip2\_opt\_6.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_6.7b/1) | 7.75B | BLIP-2 model using OPT-6.7B as the frozen language model. |
| [blip2\_flan\_t5\_xxl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xxl/1) | 12.23B | BLIP-2 model using Flan-T5-XXL (~11B) as the frozen language model. |
| [bloom\_560m\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_560m_multi/4) | 559.21M | 24-layer Bloom model with hidden dimension of 1024. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_560m\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_560m_multi/2) | 559.21M | 24-layer Bloom model with hidden dimension of 1024. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_1.1b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_1.1b_multi/2) | 1.07B | 24-layer Bloom model with hidden dimension of 1536. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_1.1b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_1.1b_multi/2) | 1.07B | 24-layer Bloom model with hidden dimension of 1536. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_1.7b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_1.7b_multi/2) | 1.72B | 24-layer Bloom model with hidden dimension of 2048. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_1.7b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_1.7b_multi/2) | 1.72B | 24-layer Bloom model with hidden dimension of 2048. finetuned on crosslingual task mixture (xP3) dataset. |
| [bloom\_3b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloom_3b_multi/2) | 3.00B | 30-layer Bloom model with hidden dimension of 2560. trained on 45 natural languages and 12 programming languages. |
| [bloomz\_3b\_multi](https://www.kaggle.com/models/keras/bloom/keras/bloomz_3b_multi/2) | 3.00B | 30-layer Bloom model with hidden dimension of 2560. finetuned on crosslingual task mixture (xP3) dataset. |
| [clip\_vit\_base\_patch16](https://www.kaggle.com/models/keras/clip/keras/clip_vit_base_patch16/3) | 149.62M | 150 million parameter, 12-layer for vision and 12-layer for text, patch size of 16, CLIP model. |
| [clip\_vit\_base\_patch32](https://www.kaggle.com/models/keras/clip/keras/clip_vit_base_patch32/3) | 151.28M | 151 million parameter, 12-layer for vision and 12-layer for text, patch size of 32, CLIP model. |
| [clip\_vit\_b\_32\_laion2b\_s34b\_b79k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_b_32_laion2b_s34b_b79k/3) | 151.28M | 151 million parameter, 12-layer for vision and 12-layer for text, patch size of 32, Open CLIP model. |
| [clip\_vit\_large\_patch14](https://www.kaggle.com/models/keras/clip/keras/clip_vit_large_patch14/3) | 427.62M | 428 million parameter, 24-layer for vision and 12-layer for text, patch size of 14, CLIP model. |
| [clip\_vit\_large\_patch14\_336](https://www.kaggle.com/models/keras/clip/keras/clip_vit_large_patch14_336/3) | 427.94M | 428 million parameter, 24-layer for vision and 12-layer for text, patch size of 14, image size of 336, CLIP model. |
| [clip\_vit\_h\_14\_laion2b\_s32b\_b79k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_h_14_laion2b_s32b_b79k/3) | 986.11M | 986 million parameter, 32-layer for vision and 24-layer for text, patch size of 14, Open CLIP model. |
| [clip\_vit\_g\_14\_laion2b\_s12b\_b42k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_g_14_laion2b_s12b_b42k/3) | 1.37B | 1.4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, Open CLIP model. |
| [clip\_vit\_bigg\_14\_laion2b\_39b\_b160k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_bigg_14_laion2b_39b_b160k/3) | 2.54B | 2.5 billion parameter, 48-layer for vision and 32-layer for text, patch size of 14, Open CLIP model. |
| [falcon\_refinedweb\_1b\_en](https://www.kaggle.com/models/keras/falcon/keras/falcon_refinedweb_1b_en/2) | 1.31B | 24-layer Falcon model (Falcon with 1B parameters), trained on 350B tokens of RefinedWeb dataset. |
| [vault\_gemma\_1b\_en](https://www.kaggle.com/models/keras/vaultgemma/keras/vault_gemma_1b_en/2) | 1.04B | 1 billion parameter, 26-layer, VaultGemma model. |
| [gemma\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_2b_en/3) | 2.51B | 2 billion parameter, 18-layer, base Gemma model. |
| [gemma\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_instruct_2b_en/3) | 2.51B | 2 billion parameter, 18-layer, instruction tuned Gemma model. |
| [gemma\_1.1\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_1.1_instruct_2b_en/4) | 2.51B | 2 billion parameter, 18-layer, instruction tuned Gemma model. The 1.1 update improves model quality. |
| [code\_gemma\_1.1\_2b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_1.1_2b_en/2) | 2.51B | 2 billion parameter, 18-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. The 1.1 update improves model quality. |
| [code\_gemma\_2b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_2b_en/2) | 2.51B | 2 billion parameter, 18-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. |
| [gemma2\_2b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, base Gemma model. |
| [gemma2\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, instruction tuned Gemma model. |
| [shieldgemma\_2b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, ShieldGemma model. |
| [c2s\_scale\_gemma\_2\_2b\_en](https://www.kaggle.com/models/keras/cell2sentence/keras/c2s_scale_gemma_2_2b_en/1) | 2.61B | A 2 billion parameter, single-cell biology-aware model built on the Gemma-2 architecture. |
| [gemma\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_7b_en/4) | 8.54B | 7 billion parameter, 28-layer, base Gemma model. |
| [gemma\_instruct\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_instruct_7b_en/4) | 8.54B | 7 billion parameter, 28-layer, instruction tuned Gemma model. |
| [gemma\_1.1\_instruct\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_1.1_instruct_7b_en/5) | 8.54B | 7 billion parameter, 28-layer, instruction tuned Gemma model. The 1.1 update improves model quality. |
| [code\_gemma\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. |
| [code\_gemma\_instruct\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_instruct_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, instruction tuned CodeGemma model. This model has been trained for chat use cases related to code. |
| [code\_gemma\_1.1\_instruct\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_1.1_instruct_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, instruction tuned CodeGemma model. This model has been trained for chat use cases related to code. The 1.1 update improves model quality. |
| [gemma2\_9b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_9b_en/4) | 9.24B | 9 billion parameter, 42-layer, base Gemma model. |
| [gemma2\_instruct\_9b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_9b_en/4) | 9.24B | 9 billion parameter, 42-layer, instruction tuned Gemma model. |
| [shieldgemma\_9b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_9b_en/2) | 9.24B | 9 billion parameter, 42-layer, ShieldGemma model. |
| [gemma2\_27b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_27b_en/3) | 27.23B | 27 billion parameter, 42-layer, base Gemma model. |
| [gemma2\_instruct\_27b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_27b_en/3) | 27.23B | 27 billion parameter, 42-layer, instruction tuned Gemma model. |
| [shieldgemma\_27b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_27b_en/2) | 27.23B | 27 billion parameter, 42-layer, ShieldGemma model. |
| [c2s\_scale\_gemma\_2\_27b\_en](https://www.kaggle.com/models/keras/cell2sentence/keras/c2s_scale_gemma_2_27b_en/1) | 27.23B | A 27 billion parameter, single-cell biology-aware model built on the Gemma-2 architecture. |
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
| [gpt2\_base\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_base_en/3) | 124.44M | 12-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_base\_en\_cnn\_dailymail](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_base_en_cnn_dailymail/3) | 124.44M | 12-layer GPT-2 model where case is maintained. Finetuned on the CNN/DailyMail summarization dataset. |
| [gpt2\_medium\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_medium_en/3) | 354.82M | 24-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_large\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_large_en/3) | 774.03M | 36-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt2\_extra\_large\_en](https://www.kaggle.com/models/keras/gpt2/keras/gpt2_extra_large_en/3) | 1.56B | 48-layer GPT-2 model where case is maintained. Trained on WebText. |
| [gpt\_oss\_20b\_en](https://www.kaggle.com/models/keras/gpt-oss/keras/gpt_oss_20b_en/1) | 20.91B | This preset has 21 billion total parameters, with 3.6 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [gpt\_oss\_safeguard\_20b\_en](https://www.kaggle.com/models/keras/gpt-oss-safeguard/keras/gpt_oss_safeguard_20b_en/1) | 20.91B | Open-weight safety reasoning model with 21 billion total parameters,with 3.6 billion active parameters, a context length of over 128k, and is de-quantized from MXFP4. |
| [gpt\_oss\_120b\_en](https://www.kaggle.com/models/keras/gpt-oss/keras/gpt_oss_120b_en/1) | 116.83B | This preset has 117 billion total parameters, with 5.1 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [gpt\_oss\_safeguard\_120b\_en](https://www.kaggle.com/models/keras/gpt-oss-safeguard/keras/gpt_oss_safeguard_120b_en/1) | 116.83B | Open-weight safety reasoning model with 117 billion total parameters,with 5.1 billion active parameters, a 128k context length, and is de-quantized from MXFP4. |
| [llama2\_7b\_en](https://www.kaggle.com/models/keras/llama2/keras/llama2_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, base LLaMA 2 model. |
| [llama2\_instruct\_7b\_en](https://www.kaggle.com/models/keras/llama2/keras/llama2_instruct_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, instruction tuned LLaMA 2 model. |
| [vicuna\_1.5\_7b\_en](https://www.kaggle.com/models/keras/vicuna/keras/vicuna_1.5_7b_en/3) | 6.74B | 7 billion parameter, 32-layer, instruction tuned Vicuna v1.5 model. |
| [llama2\_7b\_en\_int8](https://www.kaggle.com/models/keras/llama2/keras/llama2_7b_en_int8/2) | 6.74B | 7 billion parameter, 32-layer, base LLaMA 2 model with activation and weights quantized to int8. |
| [llama2\_instruct\_7b\_en\_int8](https://www.kaggle.com/models/keras/llama2/keras/llama2_instruct_7b_en_int8/2) | 6.74B | 7 billion parameter, 32-layer, instruction tuned LLaMA 2 model with activation and weights quantized to int8. |
| [llama3.2\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_1b/1) | 1.50B | 1 billion parameter, 16-layer, based LLaMA 3.2 model. |
| [llama3.2\_instruct\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_instruct_1b/1) | 1.50B | 1 billion parameter, 16-layer, instruction tuned LLaMA 3.2. |
| [llama3.2\_guard\_1b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_guard_1b/1) | 1.50B | 1 billion parameter, 16-layer, based LLaMA 3.2 model fine-tuned for consent safety classification. |
| [llama3.2\_3b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_3b/1) | 3.61B | 3 billion parameter, 26-layer, based LLaMA 3.2 model. |
| [llama3.2\_instruct\_3b](https://www.kaggle.com/models/keras/llama3/keras/llama3.2_instruct_3b/1) | 3.61B | 3 billion parameter, 28-layer, instruction tuned LLaMA 3.2. |
| [llama3\_8b\_en](https://www.kaggle.com/models/keras/llama3/keras/llama3_8b_en/5) | 8.03B | 8 billion parameter, 32-layer, base LLaMA 3 model. |
| [llama3\_instruct\_8b\_en](https://www.kaggle.com/models/keras/llama3/keras/llama3_instruct_8b_en/5) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3 model. |
| [llama3.1\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_8b/2) | 8.03B | 8 billion parameter, 32-layer, based LLaMA 3.1 model. |
| [llama3.1\_instruct\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_instruct_8b/2) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3.1. |
| [llama3.1\_guard\_8b](https://www.kaggle.com/models/keras/llama3/keras/llama3.1_guard_8b/2) | 8.03B | 8 billion parameter, 32-layer, LLaMA 3.1 fine-tuned for consent safety classification. |
| [llama3\_8b\_en\_int8](https://www.kaggle.com/models/keras/llama3/keras/llama3_8b_en_int8/2) | 8.03B | 8 billion parameter, 32-layer, base LLaMA 3 model with activation and weights quantized to int8. |
| [llama3\_instruct\_8b\_en\_int8](https://www.kaggle.com/models/keras/llama3/keras/llama3_instruct_8b_en_int8/2) | 8.03B | 8 billion parameter, 32-layer, instruction tuned LLaMA 3 model with activation and weights quantized to int8. |
| [metaclip\_2\_vit\_huge\_patch14\_224](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_huge_patch14_224/1) | 1.86B | 2 billion parameter, 32-layer for vision and 24-layer for text, patch size of 14, image resolution 224x224. MetaCLIP 2 worldwide huge model (ViT-H-14-quickgelu-worldwide) trained on 29B seen pairs with QuickGELU activation. |
| [metaclip\_2\_vit\_huge\_patch14\_378](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_huge_patch14_378/1) | 1.86B | 2 billion parameter, 32-layer for vision and 24-layer for text, patch size of 14, image resolution 378x378. MetaCLIP 2 worldwide huge model (ViT-H-14-378-worldwide) trained on 29B seen pairs. |
| [metaclip\_2\_vit\_giant\_patch14\_224](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_giant_patch14_224/1) | 3.63B | 4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, image resolution 224x224. MetaCLIP 2 worldwide giant model (ViT-bigG-14-worldwide) trained on 29B seen pairs. |
| [metaclip\_2\_vit\_giant\_patch14\_378](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_giant_patch14_378/1) | 3.63B | 4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, image resolution 378x378. MetaCLIP 2 worldwide giant model (ViT-bigG-14-378-worldwide) trained on 29B seen pairs. |
| [mistral\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_7b_en/8) | 7.24B | Mistral 7B base model |
| [mistral\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_instruct_7b_en/8) | 7.24B | Mistral 7B instruct model |
| [mistral\_0.2\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.2_instruct_7b_en/3) | 7.24B | Mistral 7B instruct version 0.2 model |
| [mistral\_0.3\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.3_7b_en/1) | 7.25B | Mistral 7B base version 0.3 model |
| [mistral\_0.3\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mistral/keras/mistral_0.3_instruct_7b_en/1) | 7.25B | Mistral 7B instruct version 0.3 model |
| [magistral\_small\_2506\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2506_en/1) | 23.57B | Magistral Small 2506 model |
| [magistral\_small\_2507\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2507_en/1) | 23.57B | Magistral Small 2507 model |
| [ministral\_3\_3b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_base_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_instruct_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_reasoning_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [shieldstral\_1.0\_3b\_en](https://www.kaggle.com/models/keras/shieldstral/keras/shieldstral_1.0_3b_en/1) | 3.85B | 3 billion parameter, 26-layer Shieldstral model with a Pixtral vision encoder. The model checks text and image content against a safety policy written in natural language. The model returns one safety score for each input. |
| [ministral\_3\_8b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_base_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_instruct_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_reasoning_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_base_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_instruct_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_reasoning_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_base\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_base_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, pretrained Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_instruct\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_instruct_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.2\_24b\_instruct\_2506\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.2_24b_instruct_2506_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. An updated version of mistral\_small\_3.1\_24b\_instruct\_2503\_en with improved instruction-following and reduced repetition. |
| [devstral\_small\_2\_24b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/devstral2/keras/devstral_small_2_24b_instruct_2512_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Devstral Small 2 model for agentic software engineering, with a Pixtral vision encoder for image input. |
| [magistral\_small\_2509\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2509_en/1) | 24.01B | 24 billion parameter, 40-layer, reasoning-tuned Magistral Small model with a Pixtral vision encoder for image input. |
| [mixtral\_8\_7b\_en](https://www.kaggle.com/models/keras/mixtral/keras/mixtral_8_7b_en/4) | 46.70B | 32-layer Mixtral MoE model with 7 billionactive parameters and 8 experts per MoE layer. |
| [mixtral\_8\_instruct\_7b\_en](https://www.kaggle.com/models/keras/mixtral/keras/mixtral_8_instruct_7b_en/4) | 46.70B | Instruction fine-tuned 32-layer Mixtral MoE modelwith 7 billion active parameters and 8 experts per MoE layer. |
| [muse\_glimmer\_30b\_assistant](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b_assistant/1) | 2.56B | MuseGlimmer 30B DFlash Assistant model: 5-layer speculative-decoding drafter for the 30B model. Drafts a 16-token block-diffusion denoised block per forward pass, conditioned on the target model's hidden states. This model must NOT be used standalone. It is designed exclusively as a draft model used from the target model's generation loop. |
| [muse\_glimmer\_30b](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b/1) | 29.78B | 30B-parameter dense causal decoder with an attached windowed-attention perception encoder, distilled from Muse Spark for local agentic use. |
| [opt\_125m\_en](https://www.kaggle.com/models/keras/opt/keras/opt_125m_en/3) | 125.24M | 12-layer OPT model where case in maintained. Trained on BookCorpus, CommonCrawl, Pile, and PushShift.io corpora. |
| [opt\_1.3b\_en](https://www.kaggle.com/models/keras/opt/keras/opt_1.3b_en/3) | 1.32B | 24-layer OPT model where case in maintained. Trained on BookCorpus, CommonCrawl, Pile, and PushShift.io corpora. |
| [opt\_2.7b\_en](https://www.kaggle.com/models/keras/opt/keras/opt_2.7b_en/3) | 2.70B | 32-layer OPT model where case in maintained. Trained on BookCorpus, CommonCrawl, Pile, and PushShift.io corpora. |
| [opt\_6.7b\_en](https://www.kaggle.com/models/keras/opt/keras/opt_6.7b_en/3) | 6.70B | 32-layer OPT model where case in maintained. Trained on BookCorpus, CommonCrawl, Pile, and PushShift.io corpora. |
| [pali\_gemma\_3b\_mix\_224](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_mix_224/4) | 2.92B | image size 224, mix fine tuned, text sequence length is 256 |
| [pali\_gemma\_3b\_224](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_224/4) | 2.92B | image size 224, pre trained, text sequence length is 128 |
| [pali\_gemma\_3b\_mix\_448](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_mix_448/4) | 2.92B | image size 448, mix fine tuned, text sequence length is 512 |
| [pali\_gemma\_3b\_448](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_448/4) | 2.92B | image size 448, pre trained, text sequence length is 512 |
| [pali\_gemma\_3b\_896](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_896/4) | 2.93B | image size 896, pre trained, text sequence length is 512 |
| [pali\_gemma2\_mix\_3b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_3b_224/2) | 3.03B | 3 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_3b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_224/2) | 3.03B | 3 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma\_2\_ft\_docci\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma_2_ft_docci_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on the DOCCI dataset for improved descriptions with fine-grained details. |
| [pali\_gemma2\_mix\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_3b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_896/2) | 3.04B | 3 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_mix\_10b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_10b_224/3) | 9.66B | 10 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_10b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_224/3) | 9.66B | 10 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_ft\_docci\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_ft_docci_10b_448/3) | 9.66B | 10 billion parameter, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on the DOCCI dataset for improved descriptions with fine-grained details. |
| [pali\_gemma2\_mix\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_10b_448/3) | 9.66B | 10 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_448/3) | 9.66B | 10 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_10b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_896/3) | 9.67B | 10 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_mix\_28b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_28b_mix_224/3) | 27.65B | 28 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_mix\_28b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_28b_mix_448/3) | 27.65B | 28 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_28b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_224/4) | 27.65B | 28 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_28b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_448/3) | 27.65B | 28 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_28b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_896/3) | 27.65B | 28 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [parseq](https://www.kaggle.com/models/keras/parseq/keras/parseq/1) | 23.83M | Permuted autoregressive sequence (PARSeq) base model for scene text recognition |
| [phi3\_mini\_4k\_instruct\_en](https://www.kaggle.com/models/keras/phi3/keras/phi3_mini_4k_instruct_en/2) | 3.82B | 3.8 billion parameters, 32 layers, 4k context length, Phi-3 model. The model was trained using the Phi-3 datasets. This dataset includes both synthetic data and filtered publicly available website data, with an emphasis on high-quality and reasoning-dense properties. |
| [phi3\_mini\_128k\_instruct\_en](https://www.kaggle.com/models/keras/phi3/keras/phi3_mini_128k_instruct_en/2) | 3.82B | 3.8 billion parameters, 32 layers, 128k context length, Phi-3 model. The model was trained using the Phi-3 datasets. This dataset includes both synthetic data and filtered publicly available website data, with an emphasis on high-quality and reasoning-dense properties. |
| [qwen2.5\_0.5b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_0.5b_en/1) | 494.03M | 24-layer Qwen model with 0.5 billion parameters. |
| [qwen2.5\_instruct\_0.5b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_0.5b_en/1) | 494.03M | Instruction fine-tuned 24-layer Qwen model with 0.5 billion parameters. |
| [qwen2.5\_coder\_0.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_0.5b/1) | 494.03M | Code-focused fine-tuned Qwen-2.5 model with 0.5 billion parameters. |
| [qwen2.5\_coder\_instruct\_0.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_0.5b/1) | 494.03M | Instruction-tuned code-focused Qwen-2.5 model with 0.5 billion parameters. |
| [qwen2.5\_coder\_1.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_1.5b/1) | 1.54B | Code-focused fine-tuned 28-layer Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_coder\_instruct\_1.5b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_1.5b/1) | 1.54B | Instruction-tuned code-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_math\_1.5b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_1.5b_en/1) | 1.54B | Math-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_math\_instruct\_1.5b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_instruct_1.5b_en/1) | 1.54B | Instruction-tuned math-focused Qwen-2.5 model with 1.5 billion parameters. |
| [qwen2.5\_3b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_3b_en/1) | 3.09B | 36-layer Qwen model with 3.1 billion parameters. |
| [qwen2.5\_coder\_3b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_3b/1) | 3.09B | Code-focused fine-tuned Qwen-2.5 model with 3 billion parameters. |
| [qwen2.5\_coder\_instruct\_3b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_3b/1) | 3.09B | Instruction-tuned code-focused Qwen-2.5 model with 3 billion parameters. |
| [qwen2.5\_7b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_7b_en/3) | 6.99B | 48-layer Qwen model with 7 billion parameters. |
| [qwen2.5\_coder\_7b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_7b/1) | 6.99B | Code-focused fine-tuned Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_coder\_instruct\_7b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_7b/1) | 6.99B | Instruction-tuned code-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_math\_7b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_7b_en/1) | 7.62B | Math-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_math\_instruct\_7b\_en](https://www.kaggle.com/models/keras/qwen2-5-math/keras/qwen2.5_math_instruct_7b_en/1) | 7.62B | Instruction-tuned math-focused Qwen-2.5 model with 7 billion parameters. |
| [qwen2.5\_coder\_14b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_14b/1) | 14.00B | Code-focused fine-tuned Qwen-2.5 model with 14 billion parameters. |
| [qwen2.5\_coder\_instruct\_14b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_14b/1) | 14.00B | Instruction-tuned code-focused Qwen-2.5 model with 14 billion parameters. |
| [qwen2.5\_instruct\_32b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_32b_en/2) | 32.76B | Instruction fine-tuned 64-layer Qwen model with 32 billion parameters. |
| [qwen2.5\_coder\_32b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_32b/1) | 32.76B | Code-focused fine-tuned Qwen-2.5 model with 32 billion parameters. |
| [qwen2.5\_coder\_instruct\_32b](https://www.kaggle.com/models/keras/qwen2-5-coder/keras/qwen2.5_coder_instruct_32b/1) | 32.76B | Instruction-tuned code-focused Qwen-2.5 model with 32 billion parameters. |
| [qwen2.5\_instruct\_72b\_en](https://www.kaggle.com/models/keras/qwen/keras/qwen2.5_instruct_72b_en/2) | 72.71B | Instruction fine-tuned 80-layer Qwen model with 72 billion parameters. |
| [qwen3\_embedding\_0.6b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_0.6b_en/1) | 595.78M | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 1024. |
| [qwen3\_0.6b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_0.6b_en/1) | 596.05M | 28-layer Qwen3 model with 596M parameters, optimized for efficiency and fast inference on resource-constrained devices. |
| [harrier\_embedding\_oss\_0.6b](https://www.kaggle.com/models/keras/harrier/keras/harrier_embedding_oss_0.6b/1) | 596.05M | Microsoft harrier-oss-v1 0.6B multilingual text embedding model based on the Qwen3-0.6B architecture, fine-tuned for dense retrieval and semantic similarity across 94+ languages. Achieves 69.0 on Multilingual MTEB v2. |
| [qwen3\_1.7b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_1.7b_en/1) | 1.72B | 28-layer Qwen3 model with 1.72B parameters, offering a good balance between performance and resource usage. |
| [qwen3\_embedding\_4b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_4b_en/1) | 4.02B | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 2560. |
| [qwen3\_4b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_4b_en/1) | 4.02B | 36-layer Qwen3 model with 4.02B parameters, offering improved reasoning capabilities and better performance than smaller variants. |
| [qwen3\_embedding\_8b\_en](https://www.kaggle.com/models/keras/qwen-3-embedding/keras/qwen3_embedding_8b_en/1) | 8.19B | This text embedding model features a 32k context length and offers flexible, user-defined embedding dimensions that can range from 32 to 4096. |
| [qwen3\_8b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_8b_en/1) | 8.19B | 36-layer Qwen3 model with 8.19B parameters, featuring enhanced reasoning, coding, and instruction-following capabilities. |
| [qwen3\_14b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_14b_en/1) | 14.77B | 40-layer Qwen3 model with 14.77B parameters, featuring advanced reasoning, coding, and multilingual capabilities. |
| [qwen3\_32b\_en](https://www.kaggle.com/models/keras/qwen-3/keras/qwen3_32b_en/1) | 32.76B | 64-layer Qwen3 model with 32.76B parameters, featuring state-of-the-art performance across reasoning, coding, and general language tasks. |
| [qwen3\_5\_0.8b\_base](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_0.8b_base/1) | 852.99M | Ultra-lightweight foundation model. Ideal for edge devices and efficient, task-specific fine-tuning. Supports Text, Multimodal, video processing tasks. |
| [qwen3\_5\_0.8b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_0.8b/1) | 852.99M | Instruction-tuned ultra-lightweight model. Best for simple chat and basic NLP tasks on resource-constrained devices. Supports Text, Multimodal, video processing tasks. |
| [qwen3\_5\_2b\_base](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_2b_base/1) | 2.21B | Lightweight foundation model. Balances speed and capability; great for mobile deployment and domain-specific fine-tuning. Supports Text, Multimodal, video processing tasks. |
| [qwen3\_5\_2b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_2b/1) | 2.21B | Instruction-tuned lightweight model. Optimized for fast chat applications and general assistance on consumer hardware. Supports Text, Multimodal, video processing tasks. |
| [qwen3\_5\_4b\_base](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_4b_base/1) | 4.54B | Mid-small foundation model. Offers improved reasoning and context understanding for custom fine-tuning tasks. |
| [qwen3\_5\_4b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_4b/1) | 4.54B | Instruction-tuned mid-small model. A capable assistant for general text generation and conversational tasks on standard GPUs. Supports Multimodal, video processing tasks. |
| [qwen3\_5\_9b\_base](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_9b_base/1) | 9.41B | Mid-sized foundation model. Delivers strong reasoning, coding, and math baseline capabilities for advanced fine-tuning. Supports Multimodal, video processing tasks. |
| [qwen3\_5\_9b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_9b/1) | 9.41B | Instruction-tuned mid-sized model. Highly capable chatbot offering strong logic, coding assistance, and multi-lingual support. Supports Multimodal, video processing tasks. |
| [qwen3\_5\_27b](https://www.kaggle.com/models/keras/qwen3-5/keras/qwen3_5_27b/1) | 27.36B | Instruction-tuned large model. Delivers high-tier performance for complex reasoning, coding, and extensive contextual tasks. Supports Multimodal, video processing tasks. |
| [qwen3\_6\_27b](https://www.kaggle.com/models/keras/qwen3-6/keras/qwen3_6_27b/1) | 27.36B | Instruction-tuned 27B model. Delivers highly efficient, top-tier performance for complex reasoning, advanced coding, and extensive multilingual tasks. Optimized for fast inference and extended context lengths. |
| [qwen3\_8\_27b](https://www.kaggle.com/models/keras/qwen3-8/keras/qwen3_8_27b/1) | 27.36B | Qwen3.8-27B — instruction-tuned 27B dense vision-language model. Built on the Qwen3.5 foundation with substantial gains in coding, professional and research tasks, and long-horizon agentic workflows. Native image and video understanding. |
| [qwen\_agent\_world\_35b\_a3b](https://www.kaggle.com/models/keras/qwen-agentworld/keras/qwen_agent_world_35b_a3b/1) | 34.66B | 35 billion total parameter Qwen AgentWorld model with ~3 billion active parameters per token. Optimized for agentic applications and tool use. |
| [qwen3\_5\_moe\_35b\_a3b\_base](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b_base/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE base model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward for highly efficient inference. Supports text and multimodal inputs. |
| [qwen3\_5\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-5-moe/keras/qwen3_5_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.5 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for chat, reasoning, coding, and multimodal tasks. |
| [qwen3\_6\_moe\_35b\_a3b](https://www.kaggle.com/models/keras/qwen3-6-moe/keras/qwen3_6_moe_35b_a3b/1) | 35.11B | 35 billion total parameter Qwen3.6 MoE instruction-tuned model with ~3 billion active parameters per token. Features a 3:1 hybrid attention stack (GatedDeltaNet linear attention and full attention) with sparse Mixture-of-Experts feedforward. Optimized for fast inference and extended context lengths. |
| [qwen3\_moe\_30b\_a3b\_en](https://www.kaggle.com/models/keras/qwen-3-moe/keras/qwen3_moe_30b_a3b_en/2) | 30.53B | Mixture-of-Experts (MoE) model has 30.5 billion total parameters with 3.3 billion activated, built on 48 layers and utilizes 32 query and 4 key/value attention heads with 128 experts (8 active). |
| [qwen3\_coder\_instruct\_30b\_a3b\_en](https://www.kaggle.com/models/keras/qwen3-coder/keras/qwen3_coder_instruct_30b_a3b_en/1) | 30.53B | A Code-Specific Model,Mixture-of-Experts (MoE) model has 30.5 billion total parameters with 3.3 billion activated, built on 48 layers and utilizes 32 query and 4 key/value attention heads with 128 experts (8 active). |
| [qwen3\_moe\_235b\_a22b\_en](https://www.kaggle.com/models/keras/qwen-3-moe/keras/qwen3_moe_235b_a22b_en/1) | 235.09B | Mixture-of-Experts (MoE) model has 235 billion total parameters with 22 billion activated, built on 94 layers and utilizes 64 query and 4 key/value attention heads with 128 experts (8 active). |
| [qwen1.5\_moe\_2.7b\_en](https://www.kaggle.com/models/keras/qwen-1.5-moe/Keras/qwen1.5_moe_2.7b_en/4) | 14.32B | 24-layer Qwen MoE model with 2.7 billion active parameters and 8 experts per MoE layer. |
| [rwkv7\_g1a\_0.1b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.1b/1) | 150.00M | 150 million parameter RWKV7 model. Optimized for edge devices and mobile deployment. |
| [rwkv7\_g1a\_0.3b\_en](https://www.kaggle.com/models/keras/rwkv7/keras/rwkv7_g1a_0.3b/1) | 400.00M | 400 million parameter RWKV7 model. Small variant balancing speed and instruction following. |
| [siglip\_base\_patch16\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_224/1) | 203.16M | 200 million parameter, image size 224, pre-trained on WebLi. |
| [siglip\_base\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_256/1) | 203.20M | 200 million parameter, image size 256, pre-trained on WebLi. |
| [siglip\_base\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_384/1) | 203.45M | 200 million parameter, image size 384, pre-trained on WebLi. |
| [siglip\_base\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_512/1) | 203.79M | 200 million parameter, image size 512, pre-trained on WebLi. |
| [siglip\_base\_patch16\_256\_multilingual](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_256_multilingual/1) | 370.63M | 370 million parameter, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_224/1) | 375.19M | 375 million parameter, patch size 16, image size 224, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_256/1) | 375.23M | 375 million parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch32\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch32_256/1) | 376.86M | 376 million parameter, patch size 32, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_384/1) | 376.86M | 376 million parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [siglip\_large\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip_large_patch16_256/1) | 652.15M | 652 million parameter, image size 256, pre-trained on WebLi. |
| [siglip\_large\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_large_patch16_384/1) | 652.48M | 652 million parameter, image size 384, pre-trained on WebLi. |
| [siglip\_so400m\_patch14\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch14_224/1) | 877.36M | 877 million parameter, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip\_so400m\_patch14\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch14_384/1) | 877.96M | 877 million parameter, image size 384, shape-optimized version, pre-trained on WebLi. |
| [medsiglip\_900m\_448](https://www.kaggle.com/models/keras/medsiglip/keras/medsiglip_900m_448/1) | 878.30M | A 900 million parameter variant of SigLIP trained to encode medical images and text into a common embedding space. MedSigLIP contains a vision encoder and a text encoder, and supports 448x448 image resolution with up to 64 text tokens. |
| [siglip2\_large\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_256/1) | 881.53M | 881 million parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_large\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_384/1) | 881.86M | 881 million parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [siglip2\_large\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_512/1) | 882.31M | 882 million parameter, patch size 16, image size 512, pre-trained on WebLi. |
| [siglip\_so400m\_patch16\_256\_i18n](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch16_256_i18n/1) | 1.13B | 1.1 billion parameter, image size 256, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch14\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch14_224/1) | 1.14B | 1.1 billion parameter, patch size 14, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_256/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 256, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch14\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch14_384/1) | 1.14B | 1.1 billion parameter, patch size 14, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_384/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 384, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_512/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 512, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_giant\_opt\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_giant_opt_patch16_256/2) | 1.87B | 1.8 billion parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_giant\_opt\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_giant_opt_patch16_384/1) | 1.87B | 1.8 billion parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [smollm3\_3b\_en](https://www.kaggle.com/models/keras/smollm3/keras/smollm3_3b_en/1) | 3.08B | Dense decoder-only model has 3 billion total parameters, built on 36 layers and utilizes 16 query and 4 key/value attention heads. |
| [smolvlm2\_256m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_256m_video_instruct/1) | 256.48M | 256 million parameter SmolVLM2 vision-language model with a 30-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_500m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_500m_video_instruct/1) | 507.48M | 500 million parameter SmolVLM2 vision-language model with a 32-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_2.2b\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_2.2b_instruct/1) | 2.25B | 2.2 billion parameter SmolVLM2 vision-language model with a 24-layer SmolLM2 text decoder and a 27-layer SigLIP vision encoder (384x384 images). Instruction-tuned for image and video understanding. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L254)

### `save_to_preset` method

Copied!

`CausalLMPreprocessor.save_to_preset(preset_dir)`

Save preprocessor to a preset directory.

**Arguments**

*   **preset\_dir**: The path to the local model preset directory.

* * *

### `tokenizer` property

Copied!

`keras_hub.models.CausalLMPreprocessor.tokenizer`

The tokenizer used to tokenize strings.

* * *

[CausalLMPreprocessor](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#causallmpreprocessor)

[`CausalLMPreprocessor` class](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#frompreset-method)

[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#savetopreset-method)

[`tokenizer` property](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#tokenizer-property)