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
 / EfficientNetBackbone model

EfficientNetBackbone model
==========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/efficientnet/efficientnet_backbone.py#L12)

### `EfficientNetBackbone` class

Copied!

`keras_hub.models.EfficientNetBackbone(     stackwise_width_coefficients=None,     stackwise_depth_coefficients=None,     stackwise_kernel_sizes,     stackwise_num_repeats,     stackwise_input_filters,     stackwise_output_filters,     stackwise_expansion_ratios,     stackwise_squeeze_and_excite_ratios,     stackwise_strides,     stackwise_block_types,     stackwise_force_input_filters=[0, 0, 0, 0, 0, 0, 0],     stackwise_nores_option=[False, False, False, False, False, False, False],     dropout=0.2,     depth_divisor=8,     min_depth=8,     input_shape=(None, None, 3),     data_format="channels_last",     activation="swish",     include_stem_padding=True,     use_depth_divisor_as_min_depth=False,     cap_round_filter_decrease=False,     stem_conv_padding="valid",     batch_norm_momentum=0.9,     batch_norm_epsilon=1e-05,     projection_activation=None,     num_features=1280,     **kwargs )`

An EfficientNet backbone model.

This class encapsulates the architectures for both EfficientNetV1 and EfficientNetV2. EfficientNetV2 uses Fused-MBConv Blocks and Neural Architecture Search (NAS) to make models sizes much smaller while still improving overall model quality.

**References**

*   \[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks\] (https://arxiv.org/abs/1905.11946) (ICML 2019)
*   \[Based on the original keras.applications EfficientNet\] (https://github.com/keras-team/keras/blob/master/keras/applications/efficientnet.py)
*   \[EfficientNetV2: Smaller Models and Faster Training\] (https://arxiv.org/abs/2104.00298) (ICML 2021)

**Arguments**

*   **stackwise\_width\_coefficients**: list\[float\], scaling coefficient for network width. If single float, it is assumed that this value applies to all stacks.
*   **stackwise\_depth\_coefficients**: list\[float\], scaling coefficient for network depth. If single float, it is assumed that this value applies to all stacks.
*   **stackwise\_kernel\_sizes**: list of ints, the kernel sizes used for each conv block.
*   **stackwise\_num\_repeats**: list of ints, number of times to repeat each conv block.
*   **stackwise\_input\_filters**: list of ints, number of input filters for each conv block.
*   **stackwise\_output\_filters**: list of ints, number of output filters for each stack in the conv blocks model.
*   **stackwise\_expansion\_ratios**: list of floats, expand ratio passed to the squeeze and excitation blocks.
*   **stackwise\_strides**: list of ints, stackwise\_strides for each conv block.
*   **stackwise\_squeeze\_and\_excite\_ratios**: list of ints, the squeeze and excite ratios passed to the squeeze and excitation blocks.
*   **stackwise\_block\_types**: list of strings. Each value is either 'v1', 'unfused' or 'fused' depending on the desired blocks. 'v1' uses the original efficientnet block. FusedMBConvBlock is similar to MBConvBlock, but instead of using a depthwise convolution and a 1x1 output convolution blocks fused blocks use a single 3x3 convolution block.
*   **stackwise\_force\_input\_filters**: list of ints, overrides stackwise\_input\_filters if > 0. Primarily used to parameterize stem filters (usually stackwise\_input\_filters\[0\]) differently than stack input filters.
*   **stackwise\_nores\_option**: list of bools, toggles if residual connection is not used. If False (default), the stack will use residual connections, otherwise not.
*   **dropout**: float, dropout rate at skip connections. The default value is set to 0.2.
*   **depth\_divisor**: integer, a unit of network width. The default value is set to 8.
*   **min\_depth**: integer, minimum number of filters. Can be None and ignored if use\_depth\_divisor\_as\_min\_depth is set to True.
*   **activation**: activation function to use between each convolutional layer.
*   **input\_shape**: optional shape tuple, it should have exactly 3 input channels.
*   **data\_format**: str, the data format of the input images. Only "channels\_last" is supported.
*   **include\_stem\_padding**: bool, whether to include initial zero padding (as per v1).
*   **use\_depth\_divisor\_as\_min\_depth**: bool, whether to use depth\_divisor as the minimum depth instead of min\_depth (as per v1).
*   **cap\_round\_filter\_decrease**: bool, whether to cap the max decrease in the number of filters the rounding process potentially produces (as per v1).
*   **stem\_conv\_padding**: str, can be 'same' or 'valid'. Padding for the stem.
*   **batch\_norm\_momentum**: float, momentum for the moving average calculation in the batch normalization layers.
*   **batch\_norm\_epsilon**: float, epsilon for batch norm calculations. Used in denominator for calculations to prevent divide by 0 errors.
*   **projection\_activation**: optional activation function to use after the output projection convolution of the 'v1' and 'fused' blocks. If None (default), no activation is applied.
*   **num\_features**: int, number of filters of the top convolution before they are scaled by the last width coefficient and rounded. This sets the number of output channels. Defaults to 1280.

**Example**

Copied!

`# You can customize the EfficientNet architecture: model = EfficientNetBackbone(     stackwise_kernel_sizes=[3, 3, 3, 3, 3, 3],     stackwise_num_repeats=[2, 4, 4, 6, 9, 15],     stackwise_input_filters=[24, 24, 48, 64, 128, 160],     stackwise_output_filters=[24, 48, 64, 128, 160, 256],     stackwise_expansion_ratios=[1, 4, 4, 4, 6, 6],     stackwise_squeeze_and_excite_ratios=[0.0, 0.0, 0, 0.25, 0.25, 0.25],     stackwise_strides=[1, 2, 2, 2, 1, 2],     stackwise_block_types=[["fused"] * 3 + ["unfused"] * 3],     width_coefficient=1.0,     depth_coefficient=1.0, ) images = np.ones((1, 256, 256, 3)) outputs = efficientnet.predict(images)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`EfficientNetBackbone.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as a one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a ModelScope handle like `'modelscope://user/bert_base_en'`
5.  a path to a local preset directory like `'./bert_base_en'`

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Backbone.from_preset()`, or from a model class like `keras_hub.models.GemmaBackbone.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

For any `Backbone` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma backbone with pre-trained weights. model = keras_hub.models.Backbone.from_preset(     "gemma_2b_en", )  # Load a Bert backbone with a pre-trained config and random weights. model = keras_hub.models.Backbone.from_preset(     "bert_base_en",     load_weights=False, )`

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

[EfficientNetBackbone model](https://keras.io/keras_hub/api/models/efficientnet/efficientnet_backbone/#efficientnetbackbone-model)

[`EfficientNetBackbone` class](https://keras.io/keras_hub/api/models/efficientnet/efficientnet_backbone/#efficientnetbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/efficientnet/efficientnet_backbone/#frompreset-method)