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
 / [Segment Anything Model 3](https://keras.io/keras_hub/api/models/sam3/)
 / SAM3PromptableConceptImageSegmenter model

SAM3PromptableConceptImageSegmenter model
=========================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/sam3/sam3_pc_image_segmenter.py#L13)

### `SAM3PromptableConceptImageSegmenter` class

Copied!

`keras_hub.models.SAM3PromptableConceptImageSegmenter(     backbone, preprocessor=None, **kwargs )`

The Segment Anything 3 (SAM3) promptable concept image segmenter Model.

SAM3 promptable concept segmentation (PCS) segments objects in images based on concept prompts, which could be short noun phrases (e.g., “yellow school bus”), image exemplars, or a combination of both. SAM3 PCS takes such prompts and returns segmentation masks and unique identities for all matching object instances.

There are two ways to prompt: 1. Text prompt: A short noun phrase describing the concept to segment. 2. Box prompt: A box tells the model which part/crop of the image to segment.

These prompts can be used individually or together, but at least one of the prompts must be present. To turn off a particular prompt, simply exclude it from the inputs to the model.

**Arguments**

*   **backbone**: A [`keras_hub.models.SAM3PromptableConceptBackbone`](https://keras.io/keras_hub/api/models/sam3/sam3_pc_backbone#sam3promptableconceptbackbone-class)
     instance.
*   **preprocessor**: Optional. An instance of `SAM3PromptableConceptImageSegmenterPreprocessor` for input data preprocessing.

**Example**

Load pretrained model using `from_preset`.

Copied!

`image_size = 128 batch_size = 2 input_data = {     "images": np.ones(         (batch_size, image_size, image_size, 3), dtype="float32",     ),     "prompts": ["ear", "head"],     "boxes": np.ones((batch_size, 1, 4), dtype="float32"),  # XYXY format.     "box_labels": np.ones((batch_size, 1), dtype="float32"), } sam3_pcs = keras_hub.models.SAM3PromptableConceptImageSegmenter.from_preset(     "sam3_pcs" ) outputs = sam3_pcs.predict(input_data) scores = outputs["scores"]  # [B, num_queries] boxes = outputs["boxes"]  # [B, num_queries, 4] masks = outputs["masks"]  # [B, num_queries, H, W]`

Load pretrained model with custom image shape.

Copied!

`input_image_size = 128 batch_size = 1 model_image_size = 336 input_data = {     "images": np.ones(         (batch_size, input_image_size, input_image_size, 3),         dtype="float32",     ),     "prompts": ["ear", "head"],     "boxes": np.ones((batch_size, 1, 4), dtype="float32"),  # XYXY format.     "box_labels": np.ones((batch_size, 1), dtype="float32"), } sam3_backbone = keras_hub.models.SAM3PromptableConceptBackbone.from_preset(     "sam3_pcs", image_shape=(model_image_size, model_image_size, 3) ) sam3_preprocessor = keras_hub.models.SAM3PromptableConceptImageSegmenterPreprocessor.from_preset(     "sam3_pcs" ) sam3_preprocessor.image_size = (model_image_size, model_image_size) sam3_pcs = keras_hub.models.SAM3PromptableConceptImageSegmenter(     backbone=sam3_backbone, preprocessor=sam3_preprocessor ) outputs = sam3_pcs.predict(input_data) scores = outputs["scores"]  # [B, num_queries] boxes = outputs["boxes"]  # [B, num_queries, 4] masks = outputs["masks"]  # [B, num_queries, H, W]`

Load SAM3PromptableConceptImageSegmenter with custom backbone

Copied!

`vision_encoder = keras_hub.layers.SAM3VisionEncoder(     image_shape=(224, 224, 3),     patch_size=14,     num_layers=2,     hidden_dim=32,     intermediate_dim=128,     num_heads=2,     fpn_hidden_dim=32,     fpn_scale_factors=[4.0, 2.0, 1.0, 0.5],     pretrain_image_shape=(112, 112, 3),     window_size=2,     global_attn_indexes=[1, 2], ) text_encoder = keras_hub.layers.SAM3TextEncoder(     vocabulary_size=1024,     embedding_dim=32,     hidden_dim=32,     num_layers=2,     num_heads=2,     intermediate_dim=128, ) geometry_encoder = keras_hub.layers.SAM3GeometryEncoder(     num_layers=3,     hidden_dim=32,     intermediate_dim=128,     num_heads=2,     roi_size=7, ) detr_encoder = keras_hub.layers.SAM3DetrEncoder(     num_layers=3,     hidden_dim=32,     intermediate_dim=128,     num_heads=2, ) detr_decoder = keras_hub.layers.SAM3DetrDecoder(     image_shape=(224, 224, 3),     patch_size=14,     num_layers=2,     hidden_dim=32,     intermediate_dim=128,     num_heads=2,     num_queries=100, ) mask_decoder = keras_hub.layers.SAM3MaskDecoder(     num_upsampling_stages=3,     hidden_dim=32,     num_heads=2, ) backbone = keras_hub.models.SAM3PromptableConceptBackbone(     vision_encoder=vision_encoder,     text_encoder=text_encoder,     geometry_encoder=geometry_encoder,     detr_encoder=detr_encoder,     detr_decoder=detr_decoder,     mask_decoder=mask_decoder, ) preprocessor = keras_hub.models.SAM3PromptableConceptImageSegmenterPreprocessor.from_preset(     "sam3_pcs" ) sam3_pcs = keras_hub.models.SAM3PromptableConceptImageSegmenter(     backbone=backbone, preprocessor=preprocessor )`

For example, to pass in all the prompts, do:

Copied!

`image_size = 128 batch_size = 2 images = np.ones(     (batch_size, image_size, image_size, 3), dtype="float32", ) prompts = ["ear", "head"] # Box prompt in XYXY format boxes = np.array(     [[[100.0, 100.0, 150.0, 150.0]], [[50.0, 50.0, 80.0, 80.0]]],     dtype="float32", ) # Box labels: 1 means positive box, 0 means negative box, -10 is for # padding boxes. box_labels = np.array([[1], [1]], dtype="int32") # Prepare an input dictionary: inputs = {     "images": images,     "prompts": prompts,     "boxes": boxes,     "box_labels": box_labels, } outputs = sam3_pcs.predict(inputs) scores = outputs["scores"]  # [B, num_queries] boxes = outputs["boxes"]  # [B, num_queries, 4] masks = outputs["masks"]  # [B, num_queries, H, W]`

Now, in case of only text prompts, simply exclude the box prompts:

Copied!

`inputs = {     "images": images,     "prompts": prompts, } outputs = sam3_pcs.predict(inputs) scores = outputs["scores"]  # [B, num_queries] boxes = outputs["boxes"]  # [B, num_queries, 4] masks = outputs["masks"]  # [B, num_queries, H, W]`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`SAM3PromptableConceptImageSegmenter.from_preset(preset, load_weights=True, **kwargs)`

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
| [sam3\_pcs](https://www.kaggle.com/models/keras/sam3/keras/sam3_pcs/1) | 30.00M | 30 million parameter Promptable Concept Segmentation (PCS) SAM model. |

* * *

### `backbone` property

Copied!

`keras_hub.models.SAM3PromptableConceptImageSegmenter.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.SAM3PromptableConceptImageSegmenter.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[SAM3PromptableConceptImageSegmenter model](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter/#sam3promptableconceptimagesegmenter-model)

[`SAM3PromptableConceptImageSegmenter` class](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter/#sam3promptableconceptimagesegmenter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/sam3/sam3_pc_image_segmenter/#preprocessor-property)