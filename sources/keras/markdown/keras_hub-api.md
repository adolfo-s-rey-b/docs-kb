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
 / KerasHub API documentation

KerasHub API documentation
==========================

KerasHub is a toolbox of modular building blocks ranging from pretrained state-of-the-art models, to low-level Transformer Encoder layers.

*   **Modeling API**: Base classes that can be used for most high-level tasks using pretrained models. Note that you can use the `from_preset()` constructor on a base class to instantiate a model of the correct subclass.
*   **Model Architectures**: Implementations of all pretrained model architectures shipped with KerasHub.
*   **Tokenizers**: Layer implementations of tokenization routines for text-based models.
*   **Preprocessing Layers**: Layers for building preprocessing pipelines that handle audio, text, and image input.
*   **Modeling Layers**: Common modeling layers used by pretrained model architectures.
*   **Samplers**: An API for controlling generative text sampling.
*   **Metrics**: Metrics useful for audio, text, and image workflows.

### [Modeling API](https://keras.io/keras_hub/api/base_classes/)

*   [Backbone](https://keras.io/keras_hub/api/base_classes/backbone)
    
*   [CausalLM](https://keras.io/keras_hub/api/base_classes/causal_lm)
    
*   [CausalLMPreprocessor](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor)
    
*   [ImageClassifier](https://keras.io/keras_hub/api/base_classes/image_classifier)
    
*   [ImageClassifierPreprocessor](https://keras.io/keras_hub/api/base_classes/image_classifier_preprocessor)
    
*   [ImageToImage](https://keras.io/keras_hub/api/base_classes/image_to_image)
    
*   [ImageSegmenter](https://keras.io/keras_hub/api/base_classes/image_segmenter)
    
*   [Inpaint](https://keras.io/keras_hub/api/base_classes/inpaint)
    
*   [MaskedLM](https://keras.io/keras_hub/api/base_classes/masked_lm)
    
*   [MaskedLMPreprocessor](https://keras.io/keras_hub/api/base_classes/masked_lm_preprocessor)
    
*   [Preprocessor](https://keras.io/keras_hub/api/base_classes/preprocessor)
    
*   [Seq2SeqLM](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm)
    
*   [Seq2SeqLMPreprocessor](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor)
    
*   [Task](https://keras.io/keras_hub/api/base_classes/task)
    
*   [TextClassifier](https://keras.io/keras_hub/api/base_classes/text_classifier)
    
*   [TextClassifierPreprocessor](https://keras.io/keras_hub/api/base_classes/text_classifier_preprocessor)
    
*   [TextEmbedder](https://keras.io/keras_hub/api/base_classes/text_embedder)
    
*   [TextEmbedderPreprocessor](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor)
    
*   [TextToImage](https://keras.io/keras_hub/api/base_classes/text_to_image)
    
*   [upload\_preset](https://keras.io/keras_hub/api/base_classes/upload_preset)
    

### [Model Architectures](https://keras.io/keras_hub/api/models/)

*   [Albert](https://keras.io/keras_hub/api/models/albert/)
    
*   [Bart](https://keras.io/keras_hub/api/models/bart/)
    
*   [BASNet](https://keras.io/keras_hub/api/models/basnet/)
    
*   [Bert](https://keras.io/keras_hub/api/models/bert/)
    
*   [Blip2](https://keras.io/keras_hub/api/models/blip2/)
    
*   [Bloom](https://keras.io/keras_hub/api/models/bloom/)
    
*   [CLIP](https://keras.io/keras_hub/api/models/clip/)
    
*   [CSPNet](https://keras.io/keras_hub/api/models/cspnet/)
    
*   [D-FINE](https://keras.io/keras_hub/api/models/d_fine/)
    
*   [DebertaV3](https://keras.io/keras_hub/api/models/deberta_v3/)
    
*   [DeepLabV3](https://keras.io/keras_hub/api/models/deeplab_v3/)
    
*   [DeiT](https://keras.io/keras_hub/api/models/deit/)
    
*   [DenseNet](https://keras.io/keras_hub/api/models/densenet/)
    
*   [DepthAnything](https://keras.io/keras_hub/api/models/depth_anything/)
    
*   [DiffusionGemma](https://keras.io/keras_hub/api/models/diffusion_gemma/)
    
*   [DINOV2](https://keras.io/keras_hub/api/models/dinov2/)
    
*   [DINOV3](https://keras.io/keras_hub/api/models/dinov3/)
    
*   [DistilBert](https://keras.io/keras_hub/api/models/distil_bert/)
    
*   [EfficientNet](https://keras.io/keras_hub/api/models/efficientnet/)
    
*   [Electra](https://keras.io/keras_hub/api/models/electra/)
    
*   [EmbeddingGemma2](https://keras.io/keras_hub/api/models/embedding_gemma2/)
    
*   [ESM](https://keras.io/keras_hub/api/models/esm/)
    
*   [Falcon](https://keras.io/keras_hub/api/models/falcon/)
    
*   [Flux](https://keras.io/keras_hub/api/models/flux/)
    
*   [FNet](https://keras.io/keras_hub/api/models/f_net/)
    
*   [Gemma](https://keras.io/keras_hub/api/models/gemma/)
    
*   [Gemma3](https://keras.io/keras_hub/api/models/gemma3/)
    
*   [Gemma3n](https://keras.io/keras_hub/api/models/gemma3n/)
    
*   [Gemma4](https://keras.io/keras_hub/api/models/gemma4/)
    
*   [GPT2](https://keras.io/keras_hub/api/models/gpt2/)
    
*   [GPT-NeoX](https://keras.io/keras_hub/api/models/gpt_neo_x/)
    
*   [GPT-OSS](https://keras.io/keras_hub/api/models/gpt_oss/)
    
*   [HGNetV2](https://keras.io/keras_hub/api/models/hgnetv2/)
    
*   [Llama](https://keras.io/keras_hub/api/models/llama/)
    
*   [Llama3](https://keras.io/keras_hub/api/models/llama3/)
    
*   [MetaCLIP 2](https://keras.io/keras_hub/api/models/metaclip_2/)
    
*   [Mistral](https://keras.io/keras_hub/api/models/mistral/)
    
*   [Mistral3](https://keras.io/keras_hub/api/models/mistral3/)
    
*   [MiT](https://keras.io/keras_hub/api/models/mit/)
    
*   [Mixtral](https://keras.io/keras_hub/api/models/mixtral/)
    
*   [MobileNet](https://keras.io/keras_hub/api/models/mobilenet/)
    
*   [MobileNetV5](https://keras.io/keras_hub/api/models/mobilenetv5/)
    
*   [ModernBERT](https://keras.io/keras_hub/api/models/modern_bert/)
    
*   [Moonshine](https://keras.io/keras_hub/api/models/moonshine/)
    
*   [MPNet](https://keras.io/keras_hub/api/models/mpnet/)
    
*   [MuseGlimmer](https://keras.io/keras_hub/api/models/muse_glimmer/)
    
*   [OPT](https://keras.io/keras_hub/api/models/opt/)
    
*   [PaliGemma](https://keras.io/keras_hub/api/models/pali_gemma/)
    
*   [PARSeq](https://keras.io/keras_hub/api/models/parseq/)
    
*   [Phi3](https://keras.io/keras_hub/api/models/phi3/)
    
*   [Qwen](https://keras.io/keras_hub/api/models/qwen/)
    
*   [Qwen3](https://keras.io/keras_hub/api/models/qwen3/)
    
*   [Qwen3.5](https://keras.io/keras_hub/api/models/qwen3_5/)
    
*   [Qwen3.5 MoE](https://keras.io/keras_hub/api/models/qwen3_5_moe/)
    
*   [Qwen3Moe](https://keras.io/keras_hub/api/models/qwen3_moe/)
    
*   [QwenMoe](https://keras.io/keras_hub/api/models/qwen_moe/)
    
*   [ResNet](https://keras.io/keras_hub/api/models/resnet/)
    
*   [RetinaNet](https://keras.io/keras_hub/api/models/retinanet/)
    
*   [Roberta](https://keras.io/keras_hub/api/models/roberta/)
    
*   [RWKV7](https://keras.io/keras_hub/api/models/rwkv7/)
    
*   [SegFormer](https://keras.io/keras_hub/api/models/segformer/)
    
*   [Segment Anything Model](https://keras.io/keras_hub/api/models/sam/)
    
*   [Segment Anything Model 3](https://keras.io/keras_hub/api/models/sam3/)
    
*   [SigLIP](https://keras.io/keras_hub/api/models/siglip/)
    
*   [SmolLM3](https://keras.io/keras_hub/api/models/smollm3/)
    
*   [SmolVLM2](https://keras.io/keras_hub/api/models/smolvlm2/)
    
*   [Stable Diffusion 3](https://keras.io/keras_hub/api/models/stable_diffusion_3/)
    
*   [Swin Transformer](https://keras.io/keras_hub/api/models/swin_transformer/)
    
*   [T5](https://keras.io/keras_hub/api/models/t5/)
    
*   [T5Gemma](https://keras.io/keras_hub/api/models/t5gemma/)
    
*   [T5Gemma2](https://keras.io/keras_hub/api/models/t5gemma2/)
    
*   [VGG](https://keras.io/keras_hub/api/models/vgg/)
    
*   [VideoPrism](https://keras.io/keras_hub/api/models/video_prism/)
    
*   [ViT](https://keras.io/keras_hub/api/models/vit/)
    
*   [ViTDet](https://keras.io/keras_hub/api/models/vit_det/)
    
*   [Whisper](https://keras.io/keras_hub/api/models/whisper/)
    
*   [Xception](https://keras.io/keras_hub/api/models/xception/)
    
*   [XLNet](https://keras.io/keras_hub/api/models/xlnet/)
    
*   [XLMRoberta](https://keras.io/keras_hub/api/models/xlm_roberta/)
    

### [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)

*   [Tokenizer](https://keras.io/keras_hub/api/tokenizers/tokenizer)
    
*   [WordPieceTokenizer](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer)
    
*   [SentencePieceTokenizer](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer)
    
*   [BytePairTokenizer](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer)
    
*   [ByteTokenizer](https://keras.io/keras_hub/api/tokenizers/byte_tokenizer)
    
*   [UnicodeCodepointTokenizer](https://keras.io/keras_hub/api/tokenizers/unicode_codepoint_tokenizer)
    
*   [compute\_word\_piece\_vocabulary function](https://keras.io/keras_hub/api/tokenizers/compute_word_piece_vocabulary)
    
*   [compute\_sentence\_piece\_proto function](https://keras.io/keras_hub/api/tokenizers/compute_sentence_piece_proto)
    

### [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)

*   [AudioConverter layer](https://keras.io/keras_hub/api/preprocessing_layers/audio_converter)
    
*   [ImageConverter layer](https://keras.io/keras_hub/api/preprocessing_layers/image_converter)
    
*   [StartEndPacker layer](https://keras.io/keras_hub/api/preprocessing_layers/start_end_packer)
    
*   [MultiSegmentPacker layer](https://keras.io/keras_hub/api/preprocessing_layers/multi_segment_packer)
    
*   [RandomSwap layer](https://keras.io/keras_hub/api/preprocessing_layers/random_swap)
    
*   [RandomDeletion layer](https://keras.io/keras_hub/api/preprocessing_layers/random_deletion)
    
*   [MaskedLMMaskGenerator layer](https://keras.io/keras_hub/api/preprocessing_layers/masked_lm_mask_generator)
    

### [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)

*   [TransformerEncoder layer](https://keras.io/keras_hub/api/modeling_layers/transformer_encoder)
    
*   [TransformerDecoder layer](https://keras.io/keras_hub/api/modeling_layers/transformer_decoder)
    
*   [FNetEncoder layer](https://keras.io/keras_hub/api/modeling_layers/fnet_encoder)
    
*   [PositionEmbedding layer](https://keras.io/keras_hub/api/modeling_layers/position_embedding)
    
*   [RotaryEmbedding layer](https://keras.io/keras_hub/api/modeling_layers/rotary_embedding)
    
*   [SinePositionEncoding layer](https://keras.io/keras_hub/api/modeling_layers/sine_position_encoding)
    
*   [ReversibleEmbedding layer](https://keras.io/keras_hub/api/modeling_layers/reversible_embedding)
    
*   [TokenAndPositionEmbedding layer](https://keras.io/keras_hub/api/modeling_layers/token_and_position_embedding)
    
*   [AlibiBias layer](https://keras.io/keras_hub/api/modeling_layers/alibi_bias)
    
*   [MaskedLMHead layer](https://keras.io/keras_hub/api/modeling_layers/masked_lm_head)
    
*   [CachedMultiHeadAttention layer](https://keras.io/keras_hub/api/modeling_layers/cached_multi_head_attention)
    

### [Samplers](https://keras.io/keras_hub/api/samplers/)

*   [Sampler base class](https://keras.io/keras_hub/api/samplers/samplers)
    
*   [BeamSampler](https://keras.io/keras_hub/api/samplers/beam_sampler)
    
*   [ContrastiveSampler](https://keras.io/keras_hub/api/samplers/contrastive_sampler)
    
*   [GreedySampler](https://keras.io/keras_hub/api/samplers/greedy_sampler)
    
*   [RandomSampler](https://keras.io/keras_hub/api/samplers/random_sampler)
    
*   [TopKSampler](https://keras.io/keras_hub/api/samplers/top_k_sampler)
    
*   [TopPSampler](https://keras.io/keras_hub/api/samplers/top_p_sampler)
    

### [Metrics](https://keras.io/keras_hub/api/metrics/)

*   [Perplexity metric](https://keras.io/keras_hub/api/metrics/perplexity)
    

[KerasHub API documentation](https://keras.io/keras_hub/api/#kerashub-api-documentation)

[Modeling API](https://keras.io/keras_hub/api/#modeling-api)

[Model Architectures](https://keras.io/keras_hub/api/#model-architectures)

[Tokenizers](https://keras.io/keras_hub/api/#tokenizers)

[Preprocessing Layers](https://keras.io/keras_hub/api/#preprocessing-layers)

[Modeling Layers](https://keras.io/keras_hub/api/#modeling-layers)

[Samplers](https://keras.io/keras_hub/api/#samplers)

[Metrics](https://keras.io/keras_hub/api/#metrics)