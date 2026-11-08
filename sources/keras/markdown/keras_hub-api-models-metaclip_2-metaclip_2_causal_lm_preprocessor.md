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
 / [MetaCLIP 2](https://keras.io/keras_hub/api/models/metaclip_2/)
 / MetaCLIP2CausalLMPreprocessor

MetaCLIP2CausalLMPreprocessor
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/metaclip_2/metaclip_2_causal_lm_preprocessor.py#L24)

### `MetaCLIP2CausalLMPreprocessor` class

Copied!

`keras_hub.models.MetaCLIP2CausalLMPreprocessor(     tokenizer,     image_converter=None,     sequence_length=77,     add_start_token=True,     add_end_token=True,     to_lower=True,     **kwargs )`

MetaCLIP 2 preprocessor.

This preprocessing layer handles both text and image preprocessing for MetaCLIP 2 models. It tokenizes text inputs and resizes/normalizes images to match the model's expected input format.

**Arguments**

*   **tokenizer**: A `keras_hub.models.MetaCLIP2Tokenizer` instance.
*   **image\_converter**: A `keras_hub.models.MetaCLIP2ImageConverter` instance.
*   **sequence\_length**: The length of the packed inputs. Defaults to 77.
*   **add\_start\_token**: If `True`, the preprocessor will prepend the tokenizer start token to each input sequence.
*   **add\_end\_token**: If `True`, the preprocessor will append the tokenizer end token to each input sequence.
*   **to\_lower**: bool. Whether to lowercase the inputs.

**Call arguments**

*   **x**: A dict with `"prompts"` and `"images"` keys, where `"prompts"` is [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     or list of python strings and `"images"` are the image tensors.
*   **y**: Label data. Should always be `None` since MetaCLIP 2 doesn't need labels to calculate the loss.
*   **sample\_weight**: Label weights.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.

**Examples**

Copied!

`# Load the preprocessor from a preset. preprocessor = keras_hub.models.MetaCLIP2CausalLMPreprocessor.from_preset(     "metaclip_2_vit_huge_patch14_224" )  # Tokenize the sentence and preprocess the image. preprocessor(     {         "prompts": "The quick brown fox jumped.",         "images": np.ones(shape=(224, 224, 3)),     } )  # Tokenize a batch of sentences and preprocess a batch of images. preprocessor(     {         "prompts": ["The quick brown fox jumped.", "The fox slept."],         "images": np.ones(shape=(2, 224, 224, 3)),     } )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`MetaCLIP2CausalLMPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [metaclip\_2\_vit\_huge\_patch14\_224](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_huge_patch14_224/1) | 1.86B | 2 billion parameter, 32-layer for vision and 24-layer for text, patch size of 14, image resolution 224x224. MetaCLIP 2 worldwide huge model (ViT-H-14-quickgelu-worldwide) trained on 29B seen pairs with QuickGELU activation. |
| [metaclip\_2\_vit\_huge\_patch14\_378](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_huge_patch14_378/1) | 1.86B | 2 billion parameter, 32-layer for vision and 24-layer for text, patch size of 14, image resolution 378x378. MetaCLIP 2 worldwide huge model (ViT-H-14-378-worldwide) trained on 29B seen pairs. |
| [metaclip\_2\_vit\_giant\_patch14\_224](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_giant_patch14_224/1) | 3.63B | 4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, image resolution 224x224. MetaCLIP 2 worldwide giant model (ViT-bigG-14-worldwide) trained on 29B seen pairs. |
| [metaclip\_2\_vit\_giant\_patch14\_378](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_giant_patch14_378/1) | 3.63B | 4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, image resolution 378x378. MetaCLIP 2 worldwide giant model (ViT-bigG-14-378-worldwide) trained on 29B seen pairs. |

* * *

[MetaCLIP2CausalLMPreprocessor](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_causal_lm_preprocessor/#metaclip2causallmpreprocessor)

[`MetaCLIP2CausalLMPreprocessor` class](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_causal_lm_preprocessor/#metaclip2causallmpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_causal_lm_preprocessor/#frompreset-method)