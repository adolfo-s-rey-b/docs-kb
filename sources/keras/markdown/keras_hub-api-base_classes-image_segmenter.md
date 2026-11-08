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
 / ImageSegmenter

ImageSegmenter
==============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/image_segmenter.py#L7)

### `ImageSegmenter` class

Copied!

`keras_hub.models.ImageSegmenter(*args, compile=True, **kwargs)`

Base class for all image segmentation tasks.

`ImageSegmenter` tasks wrap a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be used for image segmentation.

All `ImageSegmenter` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and weights.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`ImageSegmenter.from_preset(preset, load_weights=True, **kwargs)`

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
| [basnet\_duts](https://www.kaggle.com/models/keras/basnet/keras/basnet_duts) | 108.89M | BASNet model with a 34-layer ResNet backbone, pre-trained on the DUTS image dataset at a 288x288 resolution. Model training was performed by Hamid Ali (https://github.com/hamidriasat/BASNet). |
| [deeplab\_v3\_plus\_resnet50\_pascalvoc](https://www.kaggle.com/models/keras/deeplabv3plus/keras/deeplab_v3_plus_resnet50_pascalvoc/4) | 39.19M | DeepLabV3+ model with ResNet50 as image encoder and trained on augmented Pascal VOC dataset by Semantic Boundaries Dataset(SBD) which is having categorical accuracy of 90.01 and 0.63 Mean IoU. |
| [sam\_base\_sa1b](https://www.kaggle.com/models/keras/sam/keras/sam_base_sa1b/5) | 93.74M | The base SAM model trained on the SA1B dataset. |
| [sam\_huge\_sa1b](https://www.kaggle.com/models/keras/sam/keras/sam_huge_sa1b/5) | 312.34M | The huge SAM model trained on the SA1B dataset. |
| [sam\_large\_sa1b](https://www.kaggle.com/models/keras/sam/keras/sam_large_sa1b/5) | 641.09M | The large SAM model trained on the SA1B dataset. |
| [sam3\_pcs](https://www.kaggle.com/models/keras/sam3/keras/sam3_pcs/1) | 30.00M | 30 million parameter Promptable Concept Segmentation (PCS) SAM model. |
| [segformer\_b0\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b0_ade20k_512/3) | 3.72M | SegFormer model with MiTB0 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b0\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b0_cityscapes_1024/3) | 3.72M | SegFormer model with MiTB0 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b1\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b1_ade20k_512/5) | 13.68M | SegFormer model with MiTB1 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b1\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b1_ade20k_512/1) | 13.68M | SegFormer model with MiTB1 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b2\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b2_ade20k_512/3) | 24.73M | SegFormer model with MiTB2 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b2\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b2_cityscapes_1024/3) | 24.73M | SegFormer model with MiTB2 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b3\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b3_ade20k_512/3) | 44.60M | SegFormer model with MiTB3 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b3\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b3_cityscapes_1024/3) | 44.60M | SegFormer model with MiTB3 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b4\_ade20k\_512](https://www.kaggle.com/models/keras/segformer/keras/segformer_b4_ade20k_512/3) | 61.37M | SegFormer model with MiTB4 backbone fine-tuned on ADE20k in 512x512 resolution. |
| [segformer\_b4\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b4_cityscapes_1024/3) | 61.37M | SegFormer model with MiTB4 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |
| [segformer\_b5\_ade20k\_640](https://www.kaggle.com/models/keras/segformer/keras/segformer_b5_ade20k_640/3) | 81.97M | SegFormer model with MiTB5 backbone fine-tuned on ADE20k in 640x640 resolution. |
| [segformer\_b5\_cityscapes\_1024](https://www.kaggle.com/models/keras/segformer/keras/segformer_b5_cityscapes_1024/3) | 81.97M | SegFormer model with MiTB5 backbone fine-tuned on Cityscapes in 1024x1024 resolution. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/image_segmenter.py#L19)

### `compile` method

Copied!

`ImageSegmenter.compile(optimizer="auto", loss="auto", metrics="auto", **kwargs)`

Configures the `ImageSegmenter` task for training.

The `ImageSegmenter` task extends the default compilation signature of [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
 with defaults for `optimizer`, `loss`, and `metrics`. To override these defaults, pass any value to these arguments during compilation.

**Arguments**

*   **optimizer**: `"auto"`, an optimizer name, or a `keras.Optimizer` instance. Defaults to `"auto"`, which uses the default optimizer for the given model and task. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
     and `keras.optimizers` for more info on possible `optimizer` values.
*   **loss**: `"auto"`, a loss name, or a [`keras.losses.Loss`](https://keras.io/api/losses#loss-class)
     instance. Defaults to `"auto"`, where a [`keras.losses.SparseCategoricalCrossentropy`](https://keras.io/api/losses/probabilistic_losses#sparsecategoricalcrossentropy-class)
     loss will be applied for the classification task. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
     and `keras.losses` for more info on possible `loss` values.
*   **metrics**: `"auto"`, or a list of metrics to be evaluated by the model during training and testing. Defaults to `"auto"`, where a [`keras.metrics.SparseCategoricalAccuracy`](https://keras.io/api/metrics/accuracy_metrics#sparsecategoricalaccuracy-class)
     will be applied to track the accuracy of the model during training. See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
     and `keras.metrics` for more info on possible `metrics` values.
*   **\*\*kwargs**: See [`keras.Model.compile`](https://keras.io/api/models/model_training_apis#compile-method)
     for a full list of arguments supported by the compile method.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L271)

### `save_to_preset` method

Copied!

`ImageSegmenter.save_to_preset(preset_dir, max_shard_size=10)`

Save task to a preset directory.

**Arguments**

*   **preset\_dir**: The path to the local model preset directory.
*   **max\_shard\_size**: `int` or `float`. Maximum size in GB for each sharded file. If `None`, no sharding will be done. Defaults to `10`.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.ImageSegmenter.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

### `backbone` property

Copied!

`keras_hub.models.ImageSegmenter.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

[ImageSegmenter](https://keras.io/keras_hub/api/base_classes/image_segmenter/#imagesegmenter)

[`ImageSegmenter` class](https://keras.io/keras_hub/api/base_classes/image_segmenter/#imagesegmenter-class)

[`from_preset` method](https://keras.io/keras_hub/api/base_classes/image_segmenter/#frompreset-method)

[`compile` method](https://keras.io/keras_hub/api/base_classes/image_segmenter/#compile-method)

[`save_to_preset` method](https://keras.io/keras_hub/api/base_classes/image_segmenter/#savetopreset-method)

[`preprocessor` property](https://keras.io/keras_hub/api/base_classes/image_segmenter/#preprocessor-property)

[`backbone` property](https://keras.io/keras_hub/api/base_classes/image_segmenter/#backbone-property)