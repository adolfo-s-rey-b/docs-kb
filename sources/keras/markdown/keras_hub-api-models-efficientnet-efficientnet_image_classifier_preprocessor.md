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
 / [EfficientNet](https://keras.io/keras_hub/api/models/efficientnet/)
 / EfficientNetImageClassifierPreprocessor layer

EfficientNetImageClassifierPreprocessor layer
=============================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/efficientnet/efficientnet_image_classifier_preprocessor.py#L13)

### `EfficientNetImageClassifierPreprocessor` class

Copied!

`keras_hub.models.EfficientNetImageClassifierPreprocessor(     image_converter=None, **kwargs )`

Base class for image classification preprocessing layers.

`ImageClassifierPreprocessor` tasks wraps a [`keras_hub.layers.ImageConverter`](https://keras.io/keras_hub/api/preprocessing_layers/image_converter#imageconverter-class)
 to create a preprocessing layer for image classification tasks. It is intended to be paired with a [`keras_hub.models.ImageClassifier`](https://keras.io/keras_hub/api/base_classes/image_classifier#imageclassifier-class)
 task.

All `ImageClassifierPreprocessor` take inputs three inputs, `x`, `y`, and `sample_weight`. `x`, the first input, should always be included. It can be an image or batch of images. See examples below. `y` and `sample_weight` are optional inputs that will be passed through unaltered. Usually, `y` will be the classification label, and `sample_weight` will not be provided.

The layer will output either `x`, an `(x, y)` tuple if labels were provided, or an `(x, y, sample_weight)` tuple if labels and sample weight were provided. `x` will be the input images after all model preprocessing has been applied.

All `ImageClassifierPreprocessor` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and vocabularies. You can call the `from_preset()` constructor directly on this base class, in which case the correct class for your model will be automatically instantiated.

Examples.

Copied!

``preprocessor = keras_hub.models.ImageClassifierPreprocessor.from_preset(     "resnet_50", )  # Resize a single image for resnet 50. x = np.random.randint(0, 256, (512, 512, 3)) x = preprocessor(x)  # Resize a labeled image. x, y = np.random.randint(0, 256, (512, 512, 3)), 1 x, y = preprocessor(x, y)  # Resize a batch of labeled images. x, y = [     np.random.randint(0, 256, (512, 512, 3)),     np.zeros((512, 512, 3)) ], [1, 0] x, y = preprocessor(x, y)  # Use a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). ds = tf.data.Dataset.from_tensor_slices((x, y)).batch(2) ds = ds.map(preprocessor, num_parallel_calls=tf.data.AUTOTUNE)``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/preprocessor.py#L158)

### `from_preset` method

Copied!

`EfficientNetImageClassifierPreprocessor.from_preset(     preset, config_file="preprocessor.json", **kwargs )`

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
| [efficientnet\_lite0\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_lite0_ra_imagenet/2) | 4.65M | EfficientNet-Lite model fine-trained on the ImageNet 1k dataset with RandAugment recipe. |
| [efficientnet\_b0\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b0_ra_imagenet/2) | 5.29M | EfficientNet B0 model pre-trained on the ImageNet 1k dataset with RandAugment recipe. |
| [efficientnet\_b0\_ra4\_e3600\_r224\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b0_ra4_e3600_r224_imagenet/2) | 5.29M | EfficientNet B0 model pre-trained on the ImageNet 1k dataset by Ross Wightman. Trained with timm scripts using hyper-parameters inspired by the MobileNet-V4 small, mixed with go-to hparams from timm and 'ResNet Strikes Back'. |
| [efficientnet\_es\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ft_imagenet/5) | 5.44M | EfficientNet-EdgeTPU Small model trained on the ImageNet 1k dataset with RandAugment recipe. |
| [efficientnet\_em\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ft_imagenet/5) | 6.90M | EfficientNet-EdgeTPU Medium model trained on the ImageNet 1k dataset with RandAugment2 recipe. |
| [efficientnet\_b1\_ft\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ft_imagenet/5) | 7.79M | EfficientNet B1 model fine-tuned on the ImageNet 1k dataset. |
| [efficientnet\_b1\_ra4\_e3600\_r240\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ra4_e3600_r240_imagenet/2) | 7.79M | EfficientNet B1 model pre-trained on the ImageNet 1k dataset by Ross Wightman. Trained with timm scripts using hyper-parameters inspired by the MobileNet-V4 small, mixed with go-to hparams from timm and 'ResNet Strikes Back'. |
| [efficientnet\_b2\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b2_ra_imagenet/2) | 9.11M | EfficientNet B2 model pre-trained on the ImageNet 1k dataset with RandAugment recipe. |
| [efficientnet\_el\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ft_imagenet/5) | 10.59M | EfficientNet-EdgeTPU Large model trained on the ImageNet 1k dataset with RandAugment recipe. |
| [efficientnet\_b3\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b3_ra2_imagenet/2) | 12.23M | EfficientNet B3 model pre-trained on the ImageNet 1k dataset with RandAugment2 recipe. |
| [efficientnet2\_rw\_t\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet2_rw_t_ra2_imagenet/2) | 13.65M | EfficientNet-v2 Tiny model trained on the ImageNet 1k dataset with RandAugment2 recipe. |
| [efficientnet\_b4\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b4_ra2_imagenet/2) | 19.34M | EfficientNet B4 model pre-trained on the ImageNet 1k dataset with RandAugment2 recipe. |
| [efficientnet2\_rw\_s\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet2_rw_s_ra2_imagenet/2) | 23.94M | EfficientNet-v2 Small model trained on the ImageNet 1k dataset with RandAugment2 recipe. |
| [efficientnet\_b5\_sw\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b5_sw_imagenet/2) | 30.39M | EfficientNet B5 model pre-trained on the ImageNet 12k dataset by Ross Wightman. Based on Swin Transformer train / pretrain recipe with modifications (related to both DeiT and ConvNeXt recipes). |
| [efficientnet\_b5\_sw\_ft\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b5_sw_ft_imagenet/2) | 30.39M | EfficientNet B5 model pre-trained on the ImageNet 12k dataset and fine-tuned on ImageNet-1k by Ross Wightman. Based on Swin Transformer train / pretrain recipe with modifications (related to both DeiT and ConvNeXt recipes). |
| [efficientnet2\_rw\_m\_agc\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet2_rw_m_agc_imagenet/2) | 53.24M | EfficientNet-v2 Medium model trained on the ImageNet 1k dataset with adaptive gradient clipping. |

* * *

### `image_converter` property

Copied!

`keras_hub.models.EfficientNetImageClassifierPreprocessor.image_converter`

The image converter used to preprocess image data.

* * *

[EfficientNetImageClassifierPreprocessor layer](https://keras.io/keras_hub/api/models/efficientnet/efficientnet_image_classifier_preprocessor/#efficientnetimageclassifierpreprocessor-layer)

[`EfficientNetImageClassifierPreprocessor` class](https://keras.io/keras_hub/api/models/efficientnet/efficientnet_image_classifier_preprocessor/#efficientnetimageclassifierpreprocessor-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/efficientnet/efficientnet_image_classifier_preprocessor/#frompreset-method)

[`image_converter` property](https://keras.io/keras_hub/api/models/efficientnet/efficientnet_image_classifier_preprocessor/#imageconverter-property)