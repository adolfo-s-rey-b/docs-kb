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
 / KerasHub Modeling API

KerasHub Modeling API
=====================

The following base classes form the API for working with pretrained models through KerasHub. These base classes can be used with the `from_preset()` constructor to automatically instantiate a subclass with the correct model architecture, e.g. `keras_hub.models.TextClassifier.from_preset("bert_base_en", num_classes=2)`.

For the full list of available pretrained model presets shipped directly by the Keras team, see the [Pretrained Models](https://keras.io/keras_hub/presets/)
 page.

### [Backbone](https://keras.io/keras_hub/api/base_classes/backbone/)

*   [Backbone class](https://keras.io/keras_hub/api/base_classes/backbone/#backbone-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/backbone/#from_preset-method)
    
*   [token\_embedding property](https://keras.io/keras_hub/api/base_classes/backbone/#token_embedding-property)
    
*   [enable\_lora method](https://keras.io/keras_hub/api/base_classes/backbone/#enable_lora-method)
    
*   [save\_lora\_weights method](https://keras.io/keras_hub/api/base_classes/backbone/#save_lora_weights-method)
    
*   [load\_lora\_weights method](https://keras.io/keras_hub/api/base_classes/backbone/#load_lora_weights-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/backbone/#save_to_preset-method)
    

### [CausalLM](https://keras.io/keras_hub/api/base_classes/causal_lm/)

*   [CausalLM class](https://keras.io/keras_hub/api/base_classes/causal_lm/#causallm-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/causal_lm/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/causal_lm/#compile-method)
    
*   [generate method](https://keras.io/keras_hub/api/base_classes/causal_lm/#generate-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/causal_lm/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/causal_lm/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/causal_lm/#backbone-property)
    

### [CausalLMPreprocessor](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/)

*   [CausalLMPreprocessor class](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#causallmpreprocessor-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#save_to_preset-method)
    
*   [tokenizer property](https://keras.io/keras_hub/api/base_classes/causal_lm_preprocessor/#tokenizer-property)
    

### [ImageClassifier](https://keras.io/keras_hub/api/base_classes/image_classifier/)

*   [ImageClassifier class](https://keras.io/keras_hub/api/base_classes/image_classifier/#imageclassifier-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/image_classifier/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/image_classifier/#compile-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/image_classifier/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/image_classifier/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/image_classifier/#backbone-property)
    

### [ImageClassifierPreprocessor](https://keras.io/keras_hub/api/base_classes/image_classifier_preprocessor/)

*   [ImageClassifierPreprocessor class](https://keras.io/keras_hub/api/base_classes/image_classifier_preprocessor/#imageclassifierpreprocessor-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/image_classifier_preprocessor/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/image_classifier_preprocessor/#save_to_preset-method)
    

### [ImageToImage](https://keras.io/keras_hub/api/base_classes/image_to_image/)

*   [ImageToImage class](https://keras.io/keras_hub/api/base_classes/image_to_image/#imagetoimage-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/image_to_image/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/image_to_image/#compile-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/image_to_image/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/image_to_image/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/image_to_image/#backbone-property)
    
*   [generate method](https://keras.io/keras_hub/api/base_classes/image_to_image/#generate-method)
    

### [ImageSegmenter](https://keras.io/keras_hub/api/base_classes/image_segmenter/)

*   [ImageSegmenter class](https://keras.io/keras_hub/api/base_classes/image_segmenter/#imagesegmenter-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/image_segmenter/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/image_segmenter/#compile-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/image_segmenter/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/image_segmenter/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/image_segmenter/#backbone-property)
    

### [Inpaint](https://keras.io/keras_hub/api/base_classes/inpaint/)

*   [Inpaint class](https://keras.io/keras_hub/api/base_classes/inpaint/#inpaint-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/inpaint/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/inpaint/#compile-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/inpaint/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/inpaint/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/inpaint/#backbone-property)
    
*   [generate method](https://keras.io/keras_hub/api/base_classes/inpaint/#generate-method)
    

### [MaskedLM](https://keras.io/keras_hub/api/base_classes/masked_lm/)

*   [MaskedLM class](https://keras.io/keras_hub/api/base_classes/masked_lm/#maskedlm-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/masked_lm/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/masked_lm/#compile-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/masked_lm/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/masked_lm/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/masked_lm/#backbone-property)
    

### [MaskedLMPreprocessor](https://keras.io/keras_hub/api/base_classes/masked_lm_preprocessor/)

*   [MaskedLMPreprocessor class](https://keras.io/keras_hub/api/base_classes/masked_lm_preprocessor/#maskedlmpreprocessor-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/masked_lm_preprocessor/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/masked_lm_preprocessor/#save_to_preset-method)
    
*   [tokenizer property](https://keras.io/keras_hub/api/base_classes/masked_lm_preprocessor/#tokenizer-property)
    

### [Preprocessor](https://keras.io/keras_hub/api/base_classes/preprocessor/)

*   [Preprocessor class](https://keras.io/keras_hub/api/base_classes/preprocessor/#preprocessor-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/preprocessor/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/preprocessor/#save_to_preset-method)
    
*   [tokenizer property](https://keras.io/keras_hub/api/base_classes/preprocessor/#tokenizer-property)
    

### [Seq2SeqLM](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm/)

*   [Seq2SeqLM class](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm/#seq2seqlm-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm/#compile-method)
    
*   [generate method](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm/#generate-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm/#backbone-property)
    

### [Seq2SeqLMPreprocessor](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/)

*   [Seq2SeqLMPreprocessor class](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#seq2seqlmpreprocessor-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#save_to_preset-method)
    
*   [tokenizer property](https://keras.io/keras_hub/api/base_classes/seq_2_seq_lm_preprocessor/#tokenizer-property)
    

### [Task](https://keras.io/keras_hub/api/base_classes/task/)

*   [Task class](https://keras.io/keras_hub/api/base_classes/task/#task-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/task/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/task/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/task/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/task/#backbone-property)
    

### [TextClassifier](https://keras.io/keras_hub/api/base_classes/text_classifier/)

*   [TextClassifier class](https://keras.io/keras_hub/api/base_classes/text_classifier/#textclassifier-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/text_classifier/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/text_classifier/#compile-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/text_classifier/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/text_classifier/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/text_classifier/#backbone-property)
    

### [TextClassifierPreprocessor](https://keras.io/keras_hub/api/base_classes/text_classifier_preprocessor/)

*   [TextClassifierPreprocessor class](https://keras.io/keras_hub/api/base_classes/text_classifier_preprocessor/#textclassifierpreprocessor-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/text_classifier_preprocessor/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/text_classifier_preprocessor/#save_to_preset-method)
    
*   [tokenizer property](https://keras.io/keras_hub/api/base_classes/text_classifier_preprocessor/#tokenizer-property)
    

### [TextEmbedder](https://keras.io/keras_hub/api/base_classes/text_embedder/)

*   [TextEmbedder class](https://keras.io/keras_hub/api/base_classes/text_embedder/#textembedder-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/text_embedder/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/text_embedder/#compile-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/text_embedder/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/text_embedder/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/text_embedder/#backbone-property)
    

### [TextEmbedderPreprocessor](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/)

*   [TextEmbedderPreprocessor class](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#textembedderpreprocessor-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#from_preset-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#save_to_preset-method)
    
*   [tokenizer property](https://keras.io/keras_hub/api/base_classes/text_embedder_preprocessor/#tokenizer-property)
    

### [TextToImage](https://keras.io/keras_hub/api/base_classes/text_to_image/)

*   [TextToImage class](https://keras.io/keras_hub/api/base_classes/text_to_image/#texttoimage-class)
    
*   [from\_preset method](https://keras.io/keras_hub/api/base_classes/text_to_image/#from_preset-method)
    
*   [compile method](https://keras.io/keras_hub/api/base_classes/text_to_image/#compile-method)
    
*   [save\_to\_preset method](https://keras.io/keras_hub/api/base_classes/text_to_image/#save_to_preset-method)
    
*   [preprocessor property](https://keras.io/keras_hub/api/base_classes/text_to_image/#preprocessor-property)
    
*   [backbone property](https://keras.io/keras_hub/api/base_classes/text_to_image/#backbone-property)
    
*   [generate method](https://keras.io/keras_hub/api/base_classes/text_to_image/#generate-method)
    

### [upload\_preset](https://keras.io/keras_hub/api/base_classes/upload_preset/)

*   [upload\_preset function](https://keras.io/keras_hub/api/base_classes/upload_preset/#upload_preset-function)
    

[KerasHub Modeling API](https://keras.io/keras_hub/api/base_classes/#kerashub-modeling-api)

[Backbone](https://keras.io/keras_hub/api/base_classes/#backbone)

[CausalLM](https://keras.io/keras_hub/api/base_classes/#causallm)

[CausalLMPreprocessor](https://keras.io/keras_hub/api/base_classes/#causallmpreprocessor)

[ImageClassifier](https://keras.io/keras_hub/api/base_classes/#imageclassifier)

[ImageClassifierPreprocessor](https://keras.io/keras_hub/api/base_classes/#imageclassifierpreprocessor)

[ImageToImage](https://keras.io/keras_hub/api/base_classes/#imagetoimage)

[ImageSegmenter](https://keras.io/keras_hub/api/base_classes/#imagesegmenter)

[Inpaint](https://keras.io/keras_hub/api/base_classes/#inpaint)

[MaskedLM](https://keras.io/keras_hub/api/base_classes/#maskedlm)

[MaskedLMPreprocessor](https://keras.io/keras_hub/api/base_classes/#maskedlmpreprocessor)

[Preprocessor](https://keras.io/keras_hub/api/base_classes/#preprocessor)

[Seq2SeqLM](https://keras.io/keras_hub/api/base_classes/#seq2seqlm)

[Seq2SeqLMPreprocessor](https://keras.io/keras_hub/api/base_classes/#seq2seqlmpreprocessor)

[Task](https://keras.io/keras_hub/api/base_classes/#task)

[TextClassifier](https://keras.io/keras_hub/api/base_classes/#textclassifier)

[TextClassifierPreprocessor](https://keras.io/keras_hub/api/base_classes/#textclassifierpreprocessor)

[TextEmbedder](https://keras.io/keras_hub/api/base_classes/#textembedder)

[TextEmbedderPreprocessor](https://keras.io/keras_hub/api/base_classes/#textembedderpreprocessor)

[TextToImage](https://keras.io/keras_hub/api/base_classes/#texttoimage)

[upload\_preset](https://keras.io/keras_hub/api/base_classes/#uploadpreset)