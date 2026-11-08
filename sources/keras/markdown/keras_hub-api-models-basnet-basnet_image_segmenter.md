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
 / [BASNet](https://keras.io/keras_hub/api/models/basnet/)
 / BASNetImageSegmenter model

BASNetImageSegmenter model
==========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/basnet/basnet.py#L9)

### `BASNetImageSegmenter` class

Copied!

`keras_hub.models.BASNetImageSegmenter(backbone, preprocessor=None, **kwargs)`

BASNet image segmentation task.

**Arguments**

*   **backbone**: A [`keras_hub.models.BASNetBackbone`](https://keras.io/keras_hub/api/models/basnet/basnet_backbone#basnetbackbone-class)
     instance.
*   **preprocessor**: `None`, a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
     instance, a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)
     instance, or a callable. If `None` no preprocessing will be applied to the inputs.

**Example**

Copied!

`import keras_hub  images = np.ones(shape=(1, 288, 288, 3)) labels = np.zeros(shape=(1, 288, 288, 1))  image_encoder = keras_hub.models.ResNetBackbone.from_preset(     "resnet_18_imagenet",     load_weights=False ) backbone = keras_hub.models.BASNetBackbone(     image_encoder,     num_classes=1,     image_shape=[288, 288, 3] ) model = keras_hub.models.BASNetImageSegmenter(backbone)  # Evaluate the model pred_labels = model(images)  # Train the model model.compile(     optimizer="adam",     loss=keras.losses.BinaryCrossentropy(from_logits=False),     metrics=["accuracy"], ) model.fit(images, labels, epochs=3)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`BASNetImageSegmenter.from_preset(preset, load_weights=True, **kwargs)`

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

* * *

### `backbone` property

Copied!

`keras_hub.models.BASNetImageSegmenter.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.BASNetImageSegmenter.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[BASNetImageSegmenter model](https://keras.io/keras_hub/api/models/basnet/basnet_image_segmenter/#basnetimagesegmenter-model)

[`BASNetImageSegmenter` class](https://keras.io/keras_hub/api/models/basnet/basnet_image_segmenter/#basnetimagesegmenter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/basnet/basnet_image_segmenter/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/basnet/basnet_image_segmenter/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/basnet/basnet_image_segmenter/#preprocessor-property)