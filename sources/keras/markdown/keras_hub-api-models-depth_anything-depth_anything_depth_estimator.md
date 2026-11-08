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
 / [DepthAnything](https://keras.io/keras_hub/api/models/depth_anything/)
 / DepthAnythingDepthEstimator model

DepthAnythingDepthEstimator model
=================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/depth_anything/depth_anything_depth_estimator.py#L16)

### `DepthAnythingDepthEstimator` class

Copied!

`keras_hub.models.DepthAnythingDepthEstimator(     backbone,     depth_estimation_type,     min_depth=1e-07,     max_depth=None,     preprocessor=None,     **kwargs )`

Base class for all depth estimation tasks.

`DepthEstimator` tasks wrap a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be used for depth estimation.

To fine-tune with `fit()`, pass a dataset containing tuples of `(x, y)` labels where `x` is a RGB image and `y` is a depth map. All `DepthEstimator` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and weights.

**Arguments**

*   **backbone**: A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
     instance or a [`keras.Model`](https://keras.io/api/models/model#model-class)
    .
*   **preprocessor**: `None`, a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
     instance, a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)
     instance, or a callable. If `None` no preprocessing will be applied to the inputs.
*   **depth\_estimation\_type**: `"relative"` or `"metric"`. The type of depth map to use. `"relative"` depth maps are up-to-scale, while `"metric"` depth maps have metric meaning (e.g. in meters). Defaults to `"relative"`.
*   **min\_depth**: An float representing the minimum depth value. This value can be used to filter out invalid depth values during training. Defaults to `keras.config.epsilon()`.
*   **max\_depth**: An optional float representing the maximum depth value. This value can be used to filter out invalid depth values during training. When `depth_estimation_type="metric"`, the model's output will be scaled to the range `[0, max_depth]`.

**Examples**

Call `predict()` to run inference.

Copied!

`# Load preset and train images = np.random.randint(0, 256, size=(2, 224, 224, 3)) depth_estimator = keras_hub.models.DepthEstimator.from_preset(     "depth_anything_v2_small" ) depth_estimator.predict(images)`

Call `fit()` on a single batch.

Copied!

`# Load preset and train images = np.random.randint(0, 256, size=(2, 224, 224, 3)) depths = np.random.uniform(0, 10, size=(2, 224, 224)) depth_estimator = keras_hub.models.DepthEstimator.from_preset(     "depth_anything_v2_small",     depth_estimation_type="metric",     max_depth=10.0, ) depth_estimator.fit(x=images, y=depths, batch_size=2)`

Call `fit()` with custom loss, optimizer and backbone.

Copied!

`depth_estimator = keras_hub.models.DepthEstimator.from_preset(     "depth_anything_v2_small",     depth_estimation_type="metric",     max_depth=10.0, ) depth_estimator.compile(     loss=keras.losses.MeanSquaredError(),     optimizer=keras.optimizers.Adam(5e-5), ) depth_estimator.backbone.trainable = False depth_estimator.fit(x=images, y=depths, batch_size=2)`

Custom backbone.

Copied!

`images = np.random.randint(0, 256, size=(2, 224, 224, 3)) depths = np.random.uniform(0, 10, size=(2, 224, 224)) image_encoder = keras_hub.models.DINOV2Backbone.from_preset("dinov2_small") backbone = keras_hub.models.DepthAnythingBackbone(     image_encoder=image_encoder,     patch_size=image_encoder.patch_size,     backbone_hidden_dim=image_encoder.hidden_dim,     reassemble_factors=[4, 2, 1, 0.5],     neck_hidden_dims=[48, 96, 192, 384],     fusion_hidden_dim=64,     head_hidden_dim=32,     head_in_index=-1, ) depth_estimator = keras_hub.models.DepthEstimator(     backbone=backbone,     depth_estimation_type="metric",     max_depth=10.0, ) depth_estimator.fit(x=images, y=depths, batch_size=2)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`DepthAnythingDepthEstimator.from_preset(preset, load_weights=True, **kwargs)`

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
| [depth\_anything\_v2\_small](https://www.kaggle.com/models/keras/depth-anything/keras/depth_anything_v2_small/1) | 25.31M | Small variant of Depth Anything V2 monocular depth estimation (MDE) model trained on synthetic labeled images and real unlabeled images. |
| [depth\_anything\_v2\_base](https://www.kaggle.com/models/keras/depth-anything/keras/depth_anything_v2_base/1) | 98.52M | Base variant of Depth Anything V2 monocular depth estimation (MDE) model trained on synthetic labeled images and real unlabeled images. |
| [depth\_anything\_v2\_large](https://www.kaggle.com/models/keras/depth-anything/keras/depth_anything_v2_large/1) | 336.72M | Large variant of Depth Anything V2 monocular depth estimation (MDE) model trained on synthetic labeled images and real unlabeled images. |

* * *

### `backbone` property

Copied!

`keras_hub.models.DepthAnythingDepthEstimator.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

[DepthAnythingDepthEstimator model](https://keras.io/keras_hub/api/models/depth_anything/depth_anything_depth_estimator/#depthanythingdepthestimator-model)

[`DepthAnythingDepthEstimator` class](https://keras.io/keras_hub/api/models/depth_anything/depth_anything_depth_estimator/#depthanythingdepthestimator-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/depth_anything/depth_anything_depth_estimator/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/depth_anything/depth_anything_depth_estimator/#backbone-property)