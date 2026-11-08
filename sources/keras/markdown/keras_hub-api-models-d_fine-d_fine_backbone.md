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
 / [D-FINE](https://keras.io/keras_hub/api/models/d_fine/)
 / DFineBackbone model

DFineBackbone model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/d_fine/d_fine_backbone.py#L94)

### `DFineBackbone` class

Copied!

`keras_hub.models.DFineBackbone(     backbone,     decoder_in_channels,     encoder_hidden_dim,     num_labels,     num_denoising,     learn_initial_query,     num_queries,     anchor_image_size,     feat_strides,     num_feature_levels,     hidden_dim,     encoder_in_channels,     encode_proj_layers,     num_attention_heads,     encoder_ffn_dim,     num_encoder_layers,     hidden_expansion,     depth_multiplier,     eval_idx,     num_decoder_layers,     decoder_attention_heads,     decoder_ffn_dim,     decoder_n_points,     lqe_hidden_dim,     num_lqe_layers,     decoder_method="default",     label_noise_ratio=0.5,     box_noise_scale=1.0,     labels=None,     seed=None,     image_shape=(None, None, 3),     out_features=None,     data_format=None,     dtype=None,     **kwargs )`

D-FINE Backbone for Object Detection.

This class implements the core D-FINE architecture, which serves as the backbone for `DFineObjectDetector`. It integrates a `HGNetV2Backbone` for initial feature extraction, a `DFineHybridEncoder` for multi-scale feature fusion using FPN/PAN pathways, and a `DFineDecoder` for refining object queries.

The backbone orchestrates the entire forward pass, from processing raw pixels to generating intermediate predictions. Key steps include: 1. Extracting multi-scale feature maps using the HGNetV2 backbone. 2. Fusing these features with the hybrid encoder. 3. Generating anchor proposals and selecting the top-k to initialize decoder queries and reference points. 4. Generating noisy queries for contrastive denoising (if the `labels` argument is provided). 5. Passing the queries and fused features through the transformer decoder to produce iterative predictions for bounding boxes and class logits.

**Arguments**

*   **backbone**: A [`keras.Model`](https://keras.io/api/models/model#model-class)
     instance that serves as the feature extractor. While any [`keras.Model`](https://keras.io/api/models/model#model-class)
     can be used, we highly recommend using a [`keras_hub.models.HGNetV2Backbone`](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_backbone#hgnetv2backbone-class)
     instance, as this architecture is optimized for its outputs. If a custom backbone is provided, it must have a `stage_names` attribute, or the `out_features` argument for this model must be specified. This requirement helps prevent hard-to-debug downstream dimensionality errors.
*   **decoder\_in\_channels**: list, Channel dimensions of the multi-scale features from the hybrid encoder. This should typically be a list of `encoder_hidden_dim` repeated for each feature level.
*   **encoder\_hidden\_dim**: int, Hidden dimension size for the encoder layers.
*   **num\_labels**: int, Number of object classes for detection.
*   **num\_denoising**: int, Number of denoising queries for contrastive denoising training. Set to `0` to disable denoising.
*   **learn\_initial\_query**: bool, Whether to learn initial query embeddings.
*   **num\_queries**: int, Number of object queries for detection.
*   **anchor\_image\_size**: tuple, Size of the anchor image as `(height, width)`.
*   **feat\_strides**: list, List of feature stride values for different pyramid levels.
*   **num\_feature\_levels**: int, Number of feature pyramid levels to use.
*   **hidden\_dim**: int, Hidden dimension size for the model.
*   **encoder\_in\_channels**: list, Channel dimensions of the feature maps from the backbone (`HGNetV2Backbone`) that are fed into the hybrid encoder.
*   **encode\_proj\_layers**: list, List specifying projection layer configurations.
*   **num\_attention\_heads**: int, Number of attention heads in encoder layers.
*   **encoder\_ffn\_dim**: int, Feed-forward network dimension in encoder.
*   **num\_encoder\_layers**: int, Number of encoder layers.
*   **hidden\_expansion**: float, Hidden dimension expansion factor.
*   **depth\_multiplier**: float, Depth multiplier for the backbone.
*   **eval\_idx**: int, Index for evaluation. Defaults to `-1` for the last layer.
*   **num\_decoder\_layers**: int, Number of decoder layers.
*   **decoder\_attention\_heads**: int, Number of attention heads in decoder layers.
*   **decoder\_ffn\_dim**: int, Feed-forward network dimension in decoder.
*   **decoder\_method**: str, Decoder method. Can be either `"default"` or `"discrete"`. Defaults to `"default"`.
*   **decoder\_n\_points**: list, Number of sampling points for deformable attention.
*   **lqe\_hidden\_dim**: int, Hidden dimension for learned query embedding.
*   **num\_lqe\_layers**: int, Number of layers in learned query embedding.
*   **label\_noise\_ratio**: float, Ratio of label noise for denoising training. Defaults to `0.5`.
*   **box\_noise\_scale**: float, Scale factor for box noise in denoising training. Defaults to `1.0`.
*   **labels**: list or None, Ground truth labels for denoising training. This is passed during model initialization to construct the training graph for contrastive denoising. Each element should be a dictionary with `"boxes"` (numpy array of shape `[N, 4]` with normalized coordinates) and `"labels"` (numpy array of shape `[N]` with class indices). Required when `num_denoising > 0`. Defaults to `None`.
*   **seed**: int or None, Random seed for reproducibility. Defaults to `None`.
*   **image\_shape**: tuple, Shape of input images as `(height, width, channels)`. Height and width can be `None` for variable input sizes. Defaults to `(None, None, 3)`.
*   **out\_features**: list or None, List of feature names to output from backbone. If `None`, uses the last `len(decoder_in_channels)` features from the backbone's `stage_names`. Defaults to `None`.
*   **data\_format**: str, The data format of the image channels. Can be either `"channels_first"` or `"channels_last"`. If `None` is specified, it will use the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. Defaults to `None`.
*   **dtype**: `None` or str or `keras.mixed_precision.DTypePolicy`. The dtype to use for the model's computations and weights. Defaults to `None`.
*   **\*\*kwargs**: Additional keyword arguments passed to the base class.

**Example**

Copied!

``import keras import numpy as np from keras_hub.models import DFineBackbone from keras_hub.models import HGNetV2Backbone  # Example 1: Basic usage without denoising. # First, build the `HGNetV2Backbone` instance. hgnetv2 = HGNetV2Backbone(     stem_channels=[3, 16, 16],     stackwise_stage_filters=[         [16, 16, 64, 1, 3, 3],         [64, 32, 256, 1, 3, 3],         [256, 64, 512, 2, 3, 5],         [512, 128, 1024, 1, 3, 5],     ],     apply_downsample=[False, True, True, True],     use_lightweight_conv_block=[False, False, True, True],     depths=[1, 1, 2, 1],     hidden_sizes=[64, 256, 512, 1024],     embedding_size=16,     use_learnable_affine_block=True,     hidden_act="relu",     image_shape=(None, None, 3),     out_features=["stage3", "stage4"],     data_format="channels_last", )  # Then, pass the backbone instance to `DFineBackbone`. backbone = DFineBackbone(     backbone=hgnetv2,     decoder_in_channels=[128, 128],     encoder_hidden_dim=128,     num_denoising=0,  # Disable denoising     num_labels=80,     hidden_dim=128,     learn_initial_query=False,     num_queries=300,     anchor_image_size=(256, 256),     feat_strides=[16, 32],     num_feature_levels=2,     encoder_in_channels=[512, 1024],     encode_proj_layers=[1],     num_attention_heads=8,     encoder_ffn_dim=512,     num_encoder_layers=1,     hidden_expansion=0.34,     depth_multiplier=0.5,     eval_idx=-1,     num_decoder_layers=3,     decoder_attention_heads=8,     decoder_ffn_dim=512,     decoder_n_points=[6, 6],     lqe_hidden_dim=64,     num_lqe_layers=2,     out_features=["stage3", "stage4"],     image_shape=(None, None, 3),     data_format="channels_last",     seed=0, )  # Prepare input data. input_data = keras.random.uniform((2, 256, 256, 3))  # Forward pass. outputs = backbone(input_data)  # Example 2: With contrastive denoising training. labels = [     {         "boxes": np.array([[0.5, 0.5, 0.2, 0.2], [0.4, 0.4, 0.1, 0.1]]),         "labels": np.array([1, 10]),     },     {         "boxes": np.array([[0.6, 0.6, 0.3, 0.3]]),         "labels": np.array([20]),     }, ]  # Pass the `HGNetV2Backbone` instance to `DFineBackbone`. backbone_with_denoising = DFineBackbone(     backbone=hgnetv2,     decoder_in_channels=[128, 128],     encoder_hidden_dim=128,     num_denoising=100,  # Enable denoising     num_labels=80,     hidden_dim=128,     learn_initial_query=False,     num_queries=300,     anchor_image_size=(256, 256),     feat_strides=[16, 32],     num_feature_levels=2,     encoder_in_channels=[512, 1024],     encode_proj_layers=[1],     num_attention_heads=8,     encoder_ffn_dim=512,     num_encoder_layers=1,     hidden_expansion=0.34,     depth_multiplier=0.5,     eval_idx=-1,     num_decoder_layers=3,     decoder_attention_heads=8,     decoder_ffn_dim=512,     decoder_n_points=[6, 6],     lqe_hidden_dim=64,     num_lqe_layers=2,     out_features=["stage3", "stage4"],     image_shape=(None, None, 3),     seed=0,     labels=labels, )  # Forward pass with denoising. outputs_with_denoising = backbone_with_denoising(input_data)``

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`DFineBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [dfine\_nano\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_nano_coco/1) | 3.79M | D-FINE Nano model, the smallest variant in the family, pretrained on the COCO dataset. Ideal for applications where computational resources are limited. |
| [dfine\_small\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_coco/1) | 10.33M | D-FINE Small model pretrained on the COCO dataset. Offers a balance between performance and computational efficiency. |
| [dfine\_small\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_obj2coco/1) | 10.33M | D-FINE Small model first pretrained on Objects365 and then fine-tuned on COCO, combining broad feature learning with benchmark-specific adaptation. |
| [dfine\_small\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_obj365/1) | 10.62M | D-FINE Small model pretrained on the large-scale Objects365 dataset, enhancing its ability to recognize a wider variety of objects. |
| [dfine\_medium\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_coco/1) | 19.62M | D-FINE Medium model pretrained on the COCO dataset. A solid baseline with strong performance for general-purpose object detection. |
| [dfine\_medium\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_obj2coco/1) | 19.62M | D-FINE Medium model using a two-stage training process: pretraining on Objects365 followed by fine-tuning on COCO. |
| [dfine\_medium\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_obj365/1) | 19.99M | D-FINE Medium model pretrained on the Objects365 dataset. Benefits from a larger and more diverse pretraining corpus. |
| [dfine\_large\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_coco/1) | 31.34M | D-FINE Large model pretrained on the COCO dataset. Provides high accuracy and is suitable for more demanding tasks. |
| [dfine\_large\_obj2coco\_e25](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_obj2coco_e25/1) | 31.34M | D-FINE Large model pretrained on Objects365 and then fine-tuned on COCO for 25 epochs. A high-performance model with specialized tuning. |
| [dfine\_large\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_obj365/1) | 31.86M | D-FINE Large model pretrained on the Objects365 dataset for improved generalization and performance on diverse object categories. |
| [dfine\_xlarge\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_coco/1) | 62.83M | D-FINE X-Large model, the largest COCO-pretrained variant, designed for state-of-the-art performance where accuracy is the top priority. |
| [dfine\_xlarge\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_obj2coco/1) | 62.83M | D-FINE X-Large model, pretrained on Objects365 and fine-tuned on COCO, representing the most powerful model in this series for COCO-style tasks. |
| [dfine\_xlarge\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_obj365/1) | 63.35M | D-FINE X-Large model pretrained on the Objects365 dataset, offering maximum performance by leveraging a vast number of object categories during pretraining. |

* * *

[DFineBackbone model](https://keras.io/keras_hub/api/models/d_fine/d_fine_backbone/#dfinebackbone-model)

[`DFineBackbone` class](https://keras.io/keras_hub/api/models/d_fine/d_fine_backbone/#dfinebackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/d_fine/d_fine_backbone/#frompreset-method)