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
 / DFineObjectDetector model

DFineObjectDetector model
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/d_fine/d_fine_object_detector.py#L18)

### `DFineObjectDetector` class

Copied!

`keras_hub.models.DFineObjectDetector(     backbone,     num_classes,     bounding_box_format="yxyx",     preprocessor=None,     matcher_class_cost=2.0,     matcher_bbox_cost=5.0,     matcher_ciou_cost=2.0,     use_focal_loss=True,     matcher_alpha=0.25,     matcher_gamma=2.0,     weight_loss_vfl=1.0,     weight_loss_bbox=5.0,     weight_loss_ciou=2.0,     weight_loss_fgl=0.15,     weight_loss_ddf=1.5,     ddf_temperature=5.0,     prediction_decoder=None,     activation=None,     **kwargs )`

D-FINE Object Detector model.

This class wraps the `DFineBackbone` and adds the final prediction and loss computation logic for end-to-end object detection. It is responsible for: 1. Defining the functional model that connects the `DFineBackbone` to the input layers. 2. Implementing the `compute_loss` method, which uses a Hungarian matcher to assign predictions to ground truth targets and calculates a weighted sum of multiple loss components (classification, bounding box, etc.). 3. Post-processing the raw outputs from the backbone into final, decoded predictions (boxes, labels, confidence scores) during inference.

**Arguments**

*   **backbone**: A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
     instance, specifically a `DFineBackbone`, serving as the feature extractor for the object detector.
*   **num\_classes**: An integer representing the number of object classes to detect.
*   **bounding\_box\_format**: A string specifying the format of the bounding boxes. Defaults to `"yxyx"`. Must be a supported format (e.g., `"yxyx"`, `"xyxy"`).
*   **preprocessor**: Optional. An instance of `DFineObjectDetectorPreprocessor` for input data preprocessing.
*   **matcher\_class\_cost**: A float representing the cost for class mismatch in the Hungarian matcher. Defaults to `2.0`.
*   **matcher\_bbox\_cost**: A float representing the cost for bounding box mismatch in the Hungarian matcher. Defaults to `5.0`.
*   **matcher\_ciou\_cost**: A float representing the cost for complete IoU mismatch in the Hungarian matcher. Defaults to `2.0`.
*   **use\_focal\_loss**: A boolean indicating whether to use focal loss for classification. Defaults to `True`.
*   **matcher\_alpha**: A float parameter for the focal loss alpha. Defaults to `0.25`.
*   **matcher\_gamma**: A float parameter for the focal loss gamma. Defaults to `2.0`.
*   **weight\_loss\_vfl**: Weight for the classification loss. Defaults to `1.0`.
*   **weight\_loss\_bbox**: Weight for the bounding box regression loss. Default is `5.0`.
*   **weight\_loss\_ciou**: Weight for the complete IoU loss. Defaults to `2.0`.
*   **weight\_loss\_fgl**: Weight for the focal grid loss. Defaults to `0.15`.
*   **weight\_loss\_ddf**: Weight for the DDF loss. Defaults to `1.5`.
*   **ddf\_temperature**: A float temperature scaling factor for the DDF loss. Defaults to `5.0`.
*   **prediction\_decoder**: Optional. A `keras.layers.Layer` instance that decodes raw predictions. If not provided, a `NonMaxSuppression` layer is used.
*   **activation**: Optional. The activation function to apply to the logits before decoding. Defaults to `None`.

**Examples**

**Creating a DFineObjectDetector without labels:**

Copied!

`import numpy as np from keras_hub.src.models.d_fine.d_fine_object_detector import (     DFineObjectDetector ) from keras_hub.src.models.d_fine.d_fine_backbone import DFineBackbone from keras_hub.src.models.hgnetv2.hgnetv2_backbone import HGNetV2Backbone  # Initialize the backbone without labels. hgnetv2_backbone = HGNetV2Backbone(     stem_channels=[3, 16, 16],     stackwise_stage_filters=[         [16, 16, 64, 1, 3, 3],         [64, 32, 256, 1, 3, 3],         [256, 64, 512, 2, 3, 5],         [512, 128, 1024, 1, 3, 5],     ],     apply_downsample=[False, True, True, True],     use_lightweight_conv_block=[False, False, True, True],     depths=[1, 1, 2, 1],     hidden_sizes=[64, 256, 512, 1024],     embedding_size=16,     use_learnable_affine_block=True,     hidden_act="relu",     image_shape=(256, 256, 3),     out_features=["stage3", "stage4"], )  # Initialize the backbone without labels. backbone = DFineBackbone(     backbone=hgnetv2_backbone,     decoder_in_channels=[128, 128],     encoder_hidden_dim=128,     num_denoising=100,     num_labels=80,     hidden_dim=128,     learn_initial_query=False,     num_queries=300,     anchor_image_size=(256, 256),     feat_strides=[16, 32],     num_feature_levels=2,     encoder_in_channels=[512, 1024],     encode_proj_layers=[1],     num_attention_heads=8,     encoder_ffn_dim=512,     num_encoder_layers=1,     hidden_expansion=0.34,     depth_multiplier=0.5,     eval_idx=-1,     num_decoder_layers=3,     decoder_attention_heads=8,     decoder_ffn_dim=512,     decoder_n_points=[6, 6],     lqe_hidden_dim=64,     num_lqe_layers=2,     out_features=["stage3", "stage4"],     image_shape=(256, 256, 3), )  # Create the detector. detector = DFineObjectDetector(     backbone=backbone,     num_classes=80,     bounding_box_format="yxyx", )`

**Creating a DFineObjectDetector with labels for the backbone:**

Copied!

`import numpy as np from keras_hub.src.models.d_fine.d_fine_object_detector import (     DFineObjectDetector ) from keras_hub.src.models.d_fine.d_fine_backbone import DFineBackbone from keras_hub.src.models.hgnetv2.hgnetv2_backbone import HGNetV2Backbone  # Define labels for the backbone. labels = [     {         "boxes": np.array([[0.5, 0.5, 0.2, 0.2], [0.4, 0.4, 0.1, 0.1]]),         "labels": np.array([1, 10])     },     {"boxes": np.array([[0.6, 0.6, 0.3, 0.3]]), "labels": np.array([20])}, ]  hgnetv2_backbone = HGNetV2Backbone(     stem_channels=[3, 16, 16],     stackwise_stage_filters=[         [16, 16, 64, 1, 3, 3],         [64, 32, 256, 1, 3, 3],         [256, 64, 512, 2, 3, 5],         [512, 128, 1024, 1, 3, 5],     ],     apply_downsample=[False, True, True, True],     use_lightweight_conv_block=[False, False, True, True],     depths=[1, 1, 2, 1],     hidden_sizes=[64, 256, 512, 1024],     embedding_size=16,     use_learnable_affine_block=True,     hidden_act="relu",     image_shape=(256, 256, 3),     out_features=["stage3", "stage4"], )  # Backbone is initialized with labels. backbone = DFineBackbone(     backbone=hgnetv2_backbone,     decoder_in_channels=[128, 128],     encoder_hidden_dim=128,     num_denoising=100,     num_labels=80,     hidden_dim=128,     learn_initial_query=False,     num_queries=300,     anchor_image_size=(256, 256),     feat_strides=[16, 32],     num_feature_levels=2,     encoder_in_channels=[512, 1024],     encode_proj_layers=[1],     num_attention_heads=8,     encoder_ffn_dim=512,     num_encoder_layers=1,     hidden_expansion=0.34,     depth_multiplier=0.5,     eval_idx=-1,     num_decoder_layers=3,     decoder_attention_heads=8,     decoder_ffn_dim=512,     decoder_n_points=[6, 6],     lqe_hidden_dim=64,     num_lqe_layers=2,     out_features=["stage3", "stage4"],     image_shape=(256, 256, 3),     labels=labels,     box_noise_scale=1.0,     label_noise_ratio=0.5, )  # Create the detector. detector = DFineObjectDetector(     backbone=backbone,     num_classes=80,     bounding_box_format="yxyx", )`

**Using the detector for training:**

Copied!

`import numpy as np from keras_hub.src.models.d_fine.d_fine_object_detector import (     DFineObjectDetector ) from keras_hub.src.models.d_fine.d_fine_backbone import DFineBackbone from keras_hub.src.models.hgnetv2.hgnetv2_backbone import HGNetV2Backbone  # Initialize backbone and detector. hgnetv2_backbone = HGNetV2Backbone(     stem_channels=[3, 16, 16],     stackwise_stage_filters=[         [16, 16, 64, 1, 3, 3],         [64, 32, 256, 1, 3, 3],         [256, 64, 512, 2, 3, 5],         [512, 128, 1024, 1, 3, 5],     ],     apply_downsample=[False, True, True, True],     use_lightweight_conv_block=[False, False, True, True],     depths=[1, 1, 2, 1],     hidden_sizes=[64, 256, 512, 1024],     embedding_size=16,     use_learnable_affine_block=True,     hidden_act="relu",     image_shape=(256, 256, 3),     out_features=["stage3", "stage4"], ) backbone = DFineBackbone(     backbone=hgnetv2_backbone,     decoder_in_channels=[128, 128],     encoder_hidden_dim=128,     num_denoising=100,     num_labels=80,     hidden_dim=128,     learn_initial_query=False,     num_queries=300,     anchor_image_size=(256, 256),     feat_strides=[16, 32],     num_feature_levels=2,     encoder_in_channels=[512, 1024],     encode_proj_layers=[1],     num_attention_heads=8,     encoder_ffn_dim=512,     num_encoder_layers=1,     hidden_expansion=0.34,     depth_multiplier=0.5,     eval_idx=-1,     num_decoder_layers=3,     decoder_attention_heads=8,     decoder_ffn_dim=512,     decoder_n_points=[6, 6],     lqe_hidden_dim=64,     num_lqe_layers=2,     out_features=["stage3", "stage4"],     image_shape=(256, 256, 3), ) detector = DFineObjectDetector(     backbone=backbone,     num_classes=80,     bounding_box_format="yxyx", )  # Sample training data. images = np.random.uniform(     low=0, high=255, size=(2, 256, 256, 3) ).astype("float32") bounding_boxes = {     "boxes": [         np.array([[10.0, 20.0, 20.0, 30.0], [20.0, 30.0, 30.0, 40.0]]),         np.array([[15.0, 25.0, 25.0, 35.0]]),     ],     "labels": [         np.array([0, 2]), np.array([1])     ], }  # Compile the model. detector.compile(     optimizer="adam",     loss=detector.compute_loss, )  # Train the model. detector.fit(x=images, y=bounding_boxes, epochs=1, batch_size=1)`

**Making predictions:**

Copied!

`import numpy as np from keras_hub.src.models.d_fine.d_fine_object_detector import (     DFineObjectDetector ) from keras_hub.src.models.d_fine.d_fine_backbone import DFineBackbone from keras_hub.src.models.hgnetv2.hgnetv2_backbone import HGNetV2Backbone  # Initialize backbone and detector. hgnetv2_backbone = HGNetV2Backbone(     stem_channels=[3, 16, 16],     stackwise_stage_filters=[         [16, 16, 64, 1, 3, 3],         [64, 32, 256, 1, 3, 3],         [256, 64, 512, 2, 3, 5],         [512, 128, 1024, 1, 3, 5],     ],     apply_downsample=[False, True, True, True],     use_lightweight_conv_block=[False, False, True, True],     depths=[1, 1, 2, 1],     hidden_sizes=[64, 256, 512, 1024],     embedding_size=16,     use_learnable_affine_block=True,     hidden_act="relu",     image_shape=(256, 256, 3),     out_features=["stage3", "stage4"], ) backbone = DFineBackbone(     backbone=hgnetv2_backbone,     decoder_in_channels=[128, 128],     encoder_hidden_dim=128,     num_denoising=100,     num_labels=80,     hidden_dim=128,     learn_initial_query=False,     num_queries=300,     anchor_image_size=(256, 256),     feat_strides=[16, 32],     num_feature_levels=2,     encoder_in_channels=[512, 1024],     encode_proj_layers=[1],     num_attention_heads=8,     encoder_ffn_dim=512,     num_encoder_layers=1,     hidden_expansion=0.34,     depth_multiplier=0.5,     eval_idx=-1,     num_decoder_layers=3,     decoder_attention_heads=8,     decoder_ffn_dim=512,     decoder_n_points=[6, 6],     lqe_hidden_dim=64,     num_lqe_layers=2,     out_features=["stage3", "stage4"],     image_shape=(256, 256, 3), ) detector = DFineObjectDetector(     backbone=backbone,     num_classes=80,     bounding_box_format="yxyx", )  # Sample test image. test_image = np.random.uniform(     low=0, high=255, size=(1, 256, 256, 3) ).astype("float32")  # Make predictions. predictions = detector.predict(test_image)  # Access predictions. boxes = predictions["boxes"]                    # Shape: (1, 100, 4) labels = predictions["labels"]                  # Shape: (1, 100) confidence = predictions["confidence"]          # Shape: (1, 100) num_detections = predictions["num_detections"]  # Shape: (1,)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`DFineObjectDetector.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`

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

### `backbone` property

Copied!

`keras_hub.models.DFineObjectDetector.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.DFineObjectDetector.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[DFineObjectDetector model](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector/#dfineobjectdetector-model)

[`DFineObjectDetector` class](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector/#dfineobjectdetector-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/d_fine/d_fine_object_detector/#preprocessor-property)