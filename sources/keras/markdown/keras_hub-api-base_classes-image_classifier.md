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
 / ImageClassifier

ImageClassifier
===============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/image_classifier.py#L7)

### `ImageClassifier` class

Copied!

`keras_hub.models.ImageClassifier(     backbone,     num_classes,     preprocessor=None,     pooling="avg",     activation=None,     dropout=0.0,     head_dtype=None,     **kwargs )`

Base class for all image classification tasks.

`ImageClassifier` tasks wrap a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be used for image classification. `ImageClassifier` tasks take an additional `num_classes` argument, controlling the number of predicted output classes.

To fine-tune with `fit()`, pass a dataset containing tuples of `(x, y)` labels where `x` is a string and `y` is an integer from `[0, num_classes)`. All `ImageClassifier` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and weights.\
\
**Arguments**\
\
*   **backbone**: A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)\
     instance or a [`keras.Model`](https://keras.io/api/models/model#model-class)\
    .\
*   **num\_classes**: int. The number of classes to predict.\
*   **preprocessor**: `None`, a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
     instance, a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)\
     instance, or a callable. If `None` no preprocessing will be applied to the inputs.\
*   **pooling**: `"avg"` or `"max"`. The type of pooling to apply on backbone output. Defaults to average pooling.\
*   **activation**: `None`, str, or callable. The activation function to use on the `Dense` layer. Set `activation=None` to return the output logits. Defaults to `"softmax"`.\
*   **head\_dtype**: `None`, str, or `keras.mixed_precision.DTypePolicy`. The dtype to use for the classification head's computations and weights.\
\
**Examples**\
\
Call `predict()` to run inference.\
\
Copied!\
\
`# Load preset and train images = np.random.randint(0, 256, size=(2, 224, 224, 3)) classifier = keras_hub.models.ImageClassifier.from_preset(     "resnet_50_imagenet" ) classifier.predict(images)`\
\
Call `fit()` on a single batch.\
\
Copied!\
\
`# Load preset and train images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] classifier = keras_hub.models.ImageClassifier.from_preset(     "resnet_50_imagenet" ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
Call `fit()` with custom loss, optimizer and backbone.\
\
Copied!\
\
`classifier = keras_hub.models.ImageClassifier.from_preset(     "resnet_50_imagenet" ) classifier.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5), ) classifier.backbone.trainable = False classifier.fit(x=images, y=labels, batch_size=2)`\
\
Custom backbone.\
\
Copied!\
\
`images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] backbone = keras_hub.models.ResNetBackbone(     stackwise_num_filters=[64, 64, 64],     stackwise_num_blocks=[2, 2, 2],     stackwise_num_strides=[1, 2, 2],     block_type="basic_block",     use_pre_activation=True,     pooling="avg", ) classifier = keras_hub.models.ImageClassifier(     backbone=backbone,     num_classes=4, ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)\
\
### `from_preset` method\
\
Copied!\
\
`ImageClassifier.from_preset(preset, load_weights=True, **kwargs)`\
\
Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)\
 from a model preset.\
\
A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:\
\
1.  a built-in preset identifier like `'bert_base_en'`\
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`\
3.  a Hugging Face handle like `'hf://user/bert_base_en'`\
4.  a path to a local preset directory like `'./bert_base_en'`\
\
For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.\
\
This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.\
\
**Arguments**\
\
*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.\
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.\
\
**Examples**\
\
Copied!\
\
`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`\
\
| Preset | Parameters | Description |\
| --- | --- | --- |\
| [csp\_resnext\_50\_ra\_imagenet](https://www.kaggle.com/models/keras/cspdarknet/keras/csp_resnext_50_ra_imagenet/1) | 20.57M | A CSP-ResNeXt (Cross-Stage-Partial) image classification model pre-trained on the Randomly Augmented ImageNet 1k dataset at a 256x256 resolution. |\
| [csp\_resnet\_50\_ra\_imagenet](https://www.kaggle.com/models/keras/cspdarknet/keras/csp_resnet_50_ra_imagenet/1) | 21.62M | A CSP-ResNet (Cross-Stage-Partial) image classification model pre-trained on the Randomly Augmented ImageNet 1k dataset at a 256x256 resolution. |\
| [csp\_darknet\_53\_ra\_imagenet](https://www.kaggle.com/models/keras/cspdarknet/keras/csp_darknet_53_ra_imagenet/2) | 27.64M | A CSP-DarkNet (Cross-Stage-Partial) image classification model pre-trained on the Randomly Augmented ImageNet 1k dataset at a 256x256 resolution. |\
| [darknet\_53\_imagenet](https://www.kaggle.com/models/keras/cspdarknet/keras/darknet_53_imagenet/1) | 41.61M | A DarkNet image classification model pre-trained on theImageNet 1k dataset at a 256x256 resolution. |\
| [deit\_tiny\_distilled\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/deit/keras/deit_tiny_distilled_patch16_224_imagenet/1) | 5.52M | DeiT-T16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |\
| [deit\_small\_distilled\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/deit/keras/deit_small_distilled_patch16_224_imagenet/1) | 21.67M | DeiT-S16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |\
| [deit\_base\_distilled\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/deit/keras/deit_base_distilled_patch16_224_imagenet/1) | 85.80M | DeiT-B16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |\
| [deit\_base\_distilled\_patch16\_384\_imagenet](https://www.kaggle.com/models/keras/deit/keras/deit_base_distilled_patch16_384_imagenet/1) | 86.09M | DeiT-B16 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [densenet\_121\_imagenet](https://www.kaggle.com/models/keras/densenet/keras/densenet_121_imagenet/3) | 7.04M | 121-layer DenseNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [densenet\_169\_imagenet](https://www.kaggle.com/models/keras/densenet/keras/densenet_169_imagenet/3) | 12.64M | 169-layer DenseNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [densenet\_201\_imagenet](https://www.kaggle.com/models/keras/densenet/keras/densenet_201_imagenet/3) | 18.32M | 201-layer DenseNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [efficientnet\_lite0\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_lite0_ra_imagenet/2) | 4.65M | EfficientNet-Lite model fine-trained on the ImageNet 1k dataset with RandAugment recipe. |\
| [efficientnet\_b0\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b0_ra_imagenet/2) | 5.29M | EfficientNet B0 model pre-trained on the ImageNet 1k dataset with RandAugment recipe. |\
| [efficientnet\_b0\_ra4\_e3600\_r224\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b0_ra4_e3600_r224_imagenet/2) | 5.29M | EfficientNet B0 model pre-trained on the ImageNet 1k dataset by Ross Wightman. Trained with timm scripts using hyper-parameters inspired by the MobileNet-V4 small, mixed with go-to hparams from timm and 'ResNet Strikes Back'. |\
| [efficientnet\_es\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ft_imagenet/5) | 5.44M | EfficientNet-EdgeTPU Small model trained on the ImageNet 1k dataset with RandAugment recipe. |\
| [efficientnet\_em\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ft_imagenet/5) | 6.90M | EfficientNet-EdgeTPU Medium model trained on the ImageNet 1k dataset with RandAugment2 recipe. |\
| [efficientnet\_b1\_ft\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ft_imagenet/5) | 7.79M | EfficientNet B1 model fine-tuned on the ImageNet 1k dataset. |\
| [efficientnet\_b1\_ra4\_e3600\_r240\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ra4_e3600_r240_imagenet/2) | 7.79M | EfficientNet B1 model pre-trained on the ImageNet 1k dataset by Ross Wightman. Trained with timm scripts using hyper-parameters inspired by the MobileNet-V4 small, mixed with go-to hparams from timm and 'ResNet Strikes Back'. |\
| [efficientnet\_b2\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b2_ra_imagenet/2) | 9.11M | EfficientNet B2 model pre-trained on the ImageNet 1k dataset with RandAugment recipe. |\
| [efficientnet\_el\_ra\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b1_ft_imagenet/5) | 10.59M | EfficientNet-EdgeTPU Large model trained on the ImageNet 1k dataset with RandAugment recipe. |\
| [efficientnet\_b3\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b3_ra2_imagenet/2) | 12.23M | EfficientNet B3 model pre-trained on the ImageNet 1k dataset with RandAugment2 recipe. |\
| [efficientnet2\_rw\_t\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet2_rw_t_ra2_imagenet/2) | 13.65M | EfficientNet-v2 Tiny model trained on the ImageNet 1k dataset with RandAugment2 recipe. |\
| [efficientnet\_b4\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b4_ra2_imagenet/2) | 19.34M | EfficientNet B4 model pre-trained on the ImageNet 1k dataset with RandAugment2 recipe. |\
| [efficientnet2\_rw\_s\_ra2\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet2_rw_s_ra2_imagenet/2) | 23.94M | EfficientNet-v2 Small model trained on the ImageNet 1k dataset with RandAugment2 recipe. |\
| [efficientnet\_b5\_sw\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b5_sw_imagenet/2) | 30.39M | EfficientNet B5 model pre-trained on the ImageNet 12k dataset by Ross Wightman. Based on Swin Transformer train / pretrain recipe with modifications (related to both DeiT and ConvNeXt recipes). |\
| [efficientnet\_b5\_sw\_ft\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet_b5_sw_ft_imagenet/2) | 30.39M | EfficientNet B5 model pre-trained on the ImageNet 12k dataset and fine-tuned on ImageNet-1k by Ross Wightman. Based on Swin Transformer train / pretrain recipe with modifications (related to both DeiT and ConvNeXt recipes). |\
| [efficientnet2\_rw\_m\_agc\_imagenet](https://www.kaggle.com/models/keras/efficientnet/keras/efficientnet2_rw_m_agc_imagenet/2) | 53.24M | EfficientNet-v2 Medium model trained on the ImageNet 1k dataset with adaptive gradient clipping. |\
| [hgnetv2\_b4\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b4_ssld_stage2_ft_in1k/1) | 13.60M | HGNetV2 B4 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |\
| [hgnetv2\_b5\_ssld\_stage1\_in22k\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b5_ssld_stage1_in22k_in1k/1) | 33.42M | HGNetV2 B5 model with 1-stage SSLD training, pre-trained on ImageNet-22K and fine-tuned on ImageNet-1K. |\
| [hgnetv2\_b5\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b5_ssld_stage2_ft_in1k/1) | 33.42M | HGNetV2 B5 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |\
| [hgnetv2\_b6\_ssld\_stage1\_in22k\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b6_ssld_stage1_in22k_in1k/1) | 69.18M | HGNetV2 B6 model with 1-stage SSLD training, pre-trained on ImageNet-22K and fine-tuned on ImageNet-1K. |\
| [hgnetv2\_b6\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b6_ssld_stage2_ft_in1k/1) | 69.18M | HGNetV2 B6 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |\
| [mit\_b0\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b0_ade20k_512/4) | 3.32M | MiT (MixTransformer) model with 8 transformer blocks. |\
| [mit\_b0\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b0_cityscapes_1024/3) | 3.32M | MiT (MixTransformer) model with 8 transformer blocks. |\
| [mit\_b1\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b1_ade20k_512/4) | 13.16M | MiT (MixTransformer) model with 8 transformer blocks. |\
| [mit\_b1\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b1_cityscapes_1024/3) | 13.16M | MiT (MixTransformer) model with 8 transformer blocks. |\
| [mit\_b2\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b2_ade20k_512/4) | 24.20M | MiT (MixTransformer) model with 16 transformer blocks. |\
| [mit\_b2\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b2_cityscapes_1024/3) | 24.20M | MiT (MixTransformer) model with 16 transformer blocks. |\
| [mit\_b3\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b3_ade20k_512/3) | 44.08M | MiT (MixTransformer) model with 28 transformer blocks. |\
| [mit\_b3\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b3_cityscapes_1024/3) | 44.08M | MiT (MixTransformer) model with 28 transformer blocks. |\
| [mit\_b4\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b4_ade20k_512/3) | 60.85M | MiT (MixTransformer) model with 41 transformer blocks. |\
| [mit\_b4\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b4_cityscapes_1024/3) | 60.85M | MiT (MixTransformer) model with 41 transformer blocks. |\
| [mit\_b5\_ade20k\_640](https://www.kaggle.com/models/keras/mit/keras/mit_b5_ade20k_640/3) | 81.45M | MiT (MixTransformer) model with 52 transformer blocks. |\
| [mit\_b5\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b5_cityscapes_1024/3) | 81.45M | MiT (MixTransformer) model with 52 transformer blocks. |\
| [mobilenet\_v3\_small\_050\_imagenet](https://www.kaggle.com/models/keras/mobilenetv3/keras/mobilenet_v3_small_050_imagenet/1) | 278.78K | Small Mobilenet V3 model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. Has half channel multiplier. |\
| [mobilenet\_v3\_small\_100\_imagenet](https://www.kaggle.com/models/keras/mobilenetv3/keras/mobilenet_v3_small_100_imagenet/1) | 939.12K | Small Mobilenet V3 model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. Has baseline channel multiplier. |\
| [mobilenet\_v3\_large\_100\_imagenet](https://www.kaggle.com/models/keras/mobilenetv3/keras/mobilenet_v3_large_100_imagenet/1) | 3.00M | Large Mobilenet V3 model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. Has baseline channel multiplier. |\
| [mobilenet\_v3\_large\_100\_imagenet\_21k](https://www.kaggle.com/models/keras/mobilenetv3/keras/mobilenet_v3_large_100_imagenet_21k/1) | 3.00M | Large Mobilenet V3 model pre-trained on the ImageNet 21k dataset at a 224x224 resolution. Has baseline channel multiplier. |\
| [mobilenetv5\_300m\_enc\_gemma3n](https://www.kaggle.com/models/keras/mobilenetv5/keras/mobilenetv5_300m_enc_gemma3n/1) | 294.28M | Lightweight 300M-parameter convolutional vision encoder used as the image backbone for Gemma 3n |\
| [resnet\_18\_imagenet](https://www.kaggle.com/models/keras/resnetv1/keras/resnet_18_imagenet/3) | 11.19M | 18-layer ResNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_vd\_18\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_18_imagenet/2) | 11.72M | 18-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_vd\_34\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_34_imagenet/2) | 21.84M | 34-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_50\_imagenet](https://www.kaggle.com/models/keras/resnetv1/keras/resnet_50_imagenet/3) | 23.56M | 50-layer ResNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_v2\_50\_imagenet](https://www.kaggle.com/models/keras/resnetv2/keras/resnet_v2_50_imagenet/3) | 23.56M | 50-layer ResNetV2 model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_vd\_50\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_50_imagenet/2) | 25.63M | 50-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_vd\_50\_ssld\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_50_ssld_imagenet/2) | 25.63M | 50-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution with knowledge distillation. |\
| [resnet\_vd\_50\_ssld\_v2\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_50_ssld_v2_imagenet/2) | 25.63M | 50-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution with knowledge distillation and AutoAugment. |\
| [resnet\_vd\_50\_ssld\_v2\_fix\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_50_ssld_v2_fix_imagenet/2) | 25.63M | 50-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution with knowledge distillation, AutoAugment and additional fine-tuning of the classification head. |\
| [resnet\_101\_imagenet](https://www.kaggle.com/models/keras/resnetv1/keras/resnet_101_imagenet/3) | 42.61M | 101-layer ResNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_v2\_101\_imagenet](https://www.kaggle.com/models/keras/resnetv2/keras/resnet_v2_101_imagenet/3) | 42.61M | 101-layer ResNetV2 model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_vd\_101\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_101_imagenet/2) | 44.67M | 101-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_vd\_101\_ssld\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_101_ssld_imagenet/2) | 44.67M | 101-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution with knowledge distillation. |\
| [resnet\_152\_imagenet](https://www.kaggle.com/models/keras/resnetv1/keras/resnet_152_imagenet/3) | 58.30M | 152-layer ResNet model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_vd\_152\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_152_imagenet/2) | 60.36M | 152-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [resnet\_vd\_200\_imagenet](https://www.kaggle.com/models/keras/resnet_vd/keras/resnet_vd_200_imagenet/2) | 74.93M | 200-layer ResNetVD (ResNet with bag of tricks) model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [swin\_tiny\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_tiny_patch4_window7_224/1) | 27.52M | Swin-Tiny model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |\
| [swin\_small\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_small_patch4_window7_224/1) | 48.84M | Swin-Small model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |\
| [swin\_base\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_base_patch4_window7_224/1) | 86.74M | Swin-Base model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |\
| [swin\_base\_patch4\_window12\_384](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_base_patch4_window12_384/1) | 86.88M | Swin-Base model pre-trained on the ImageNet 1k dataset with image resolution of 384x384. |\
| [swin\_large\_patch4\_window7\_224](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_large_patch4_window7_224/1) | 195.00M | Swin-Large model pre-trained on the ImageNet 1k dataset with image resolution of 224x224. |\
| [swin\_large\_patch4\_window12\_384](https://www.kaggle.com/models/keras/swin-transformer/keras/swin_large_patch4_window12_384/1) | 195.20M | Swin-Large model pre-trained on the ImageNet 1k dataset with image resolution of 384x384. |\
| [vgg\_11\_imagenet](https://www.kaggle.com/models/keras/vgg/keras/vgg_11_imagenet/3) | 9.22M | 11-layer vgg model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [vgg\_13\_imagenet](https://www.kaggle.com/models/keras/vgg/keras/vgg_13_imagenet/3) | 9.40M | 13-layer vgg model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [vgg\_16\_imagenet](https://www.kaggle.com/models/keras/vgg/keras/vgg_16_imagenet/3) | 14.71M | 16-layer vgg model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [vgg\_19\_imagenet](https://www.kaggle.com/models/keras/vgg/keras/vgg_19_imagenet/3) | 20.02M | 19-layer vgg model pre-trained on the ImageNet 1k dataset at a 224x224 resolution. |\
| [vit\_base\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch16_224_imagenet/4) | 85.80M | ViT-B16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |\
| [vit\_base\_patch16\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch16_224_imagenet21k/3) | 85.80M | ViT-B16 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [vit\_base\_patch16\_384\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch16_384_imagenet/4) | 86.09M | ViT-B16 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [vit\_base\_patch32\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch32_224_imagenet21k/3) | 87.46M | ViT-B32 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [vit\_base\_patch32\_384\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_base_patch32_384_imagenet/3) | 87.53M | ViT-B32 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [vit\_large\_patch16\_224\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch16_224_imagenet/4) | 303.30M | ViT-L16 model pre-trained on the ImageNet 1k dataset with image resolution of 224x224 |\
| [vit\_large\_patch16\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch16_224_imagenet21k/3) | 303.30M | ViT-L16 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [vit\_large\_patch16\_384\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch16_384_imagenet/4) | 303.69M | ViT-L16 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [vit\_large\_patch32\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch32_224_imagenet21k/3) | 305.51M | ViT-L32 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [vit\_large\_patch32\_384\_imagenet](https://www.kaggle.com/models/keras/vit/keras/vit_large_patch32_384_imagenet/3) | 305.61M | ViT-L32 model pre-trained on the ImageNet 1k dataset with image resolution of 384x384 |\
| [vit\_huge\_patch14\_224\_imagenet21k](https://www.kaggle.com/models/keras/vit/keras/vit_huge_patch14_224_imagenet21k/3) | 630.76M | ViT-H14 backbone pre-trained on the ImageNet 21k dataset with image resolution of 224x224 |\
| [xception\_41\_imagenet](https://www.kaggle.com/models/keras/xception/keras/xception_41_imagenet/2) | 20.86M | 41-layer Xception model pre-trained on ImageNet 1k. |\
\
**Guides and examples using `from_preset`**\
\
*   [Image Classification](https://keras.io/keras_hub/guides/classification_with_keras_hub/)\
    \
*   [RAG Pipeline with KerasHub](https://keras.io/keras_hub/guides/rag_pipeline_with_keras_hub/)\
    \
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/image_classifier.py#L168)\
\
### `compile` method\
\
Copied!\
\
`ImageClassifier.compile(optimizer="auto", loss="auto", metrics="auto", **kwargs)`\
\
Configures the `ImageClassifier` task for training.\
\
The `ImageClassifier` task extends the default compilation signature of [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)\
 with defaults for `optimizer`, `loss`, and `metrics`. To override these defaults, pass any value to these arguments during compilation.\
\
**Arguments**\
\
*   **optimizer**: `"auto"`, an optimizer name, or a `keras.Optimizer` instance. Defaults to `"auto"`, which uses the default optimizer for the given model and task. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)\
     and `keras.optimizers` for more info on possible `optimizer` values.\
*   **loss**: `"auto"`, a loss name, or a [`keras.losses.Loss`](https://keras.io/api/losses#loss-class)\
     instance. Defaults to `"auto"`, where a [`keras.losses.SparseCategoricalCrossentropy`](https://keras.io/api/losses/probabilistic_losses#sparsecategoricalcrossentropy-class)\
     loss will be applied for the classification task. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)\
     and `keras.losses` for more info on possible `loss` values.\
*   **metrics**: `"auto"`, or a list of metrics to be evaluated by the model during training and testing. Defaults to `"auto"`, where a [`keras.metrics.SparseCategoricalAccuracy`](https://keras.io/api/metrics/accuracy_metrics#sparsecategoricalaccuracy-class)\
     will be applied to track the accuracy of the model during training. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)\
     and `keras.metrics` for more info on possible `metrics` values.\
*   **\*\*kwargs**: See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)\
     for a full list of arguments supported by the compile method.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L271)\
\
### `save_to_preset` method\
\
Copied!\
\
`ImageClassifier.save_to_preset(preset_dir, max_shard_size=10)`\
\
Save task to a preset directory.\
\
**Arguments**\
\
*   **preset\_dir**: The path to the local model preset directory.\
*   **max\_shard\_size**: `int` or `float`. Maximum size in GB for each sharded file. If `None`, no sharding will be done. Defaults to `10`.\
\
* * *\
\
### `preprocessor` property\
\
Copied!\
\
`keras_hub.models.ImageClassifier.preprocessor`\
\
A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
 layer used to preprocess input.\
\
* * *\
\
### `backbone` property\
\
Copied!\
\
`keras_hub.models.ImageClassifier.backbone`\
\
A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)\
 model with the core architecture.\
\
* * *\
\
[ImageClassifier](https://keras.io/keras_hub/api/base_classes/image_classifier/#imageclassifier)\
\
[`ImageClassifier` class](https://keras.io/keras_hub/api/base_classes/image_classifier/#imageclassifier-class)\
\
[`from_preset` method](https://keras.io/keras_hub/api/base_classes/image_classifier/#frompreset-method)\
\
[`compile` method](https://keras.io/keras_hub/api/base_classes/image_classifier/#compile-method)\
\
[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/image_classifier/#savetopreset-method)\
\
[`preprocessor` property](https://keras.io/keras_hub/api/base_classes/image_classifier/#preprocessor-property)\
\
[`backbone` property](https://keras.io/keras_hub/api/base_classes/image_classifier/#backbone-property)