None

[Code examples](https://keras.io/examples/)

[Computer Vision](https://keras.io/examples/vision/)
 [Natural Language Processing](https://keras.io/examples/nlp/)
 [Structured Data](https://keras.io/examples/structured_data/)
 [Structured data classification with FeatureSpace](https://keras.io/examples/structured_data/structured_data_classification_with_feature_space/)
 [FeatureSpace advanced use cases](https://keras.io/examples/structured_data/feature_space_advanced/)
 [Imbalanced classification: credit card fraud detection](https://keras.io/examples/structured_data/imbalanced_classification/)
 [Structured data classification from scratch](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/)
 [Structured data learning with Wide, Deep, and Cross networks](https://keras.io/examples/structured_data/wide_deep_cross_networks/)
 [Deep Learning for Customer Lifetime Value](https://keras.io/examples/structured_data/customer_lifetime_value/)
 [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)
 [Classification with TensorFlow Decision Forests](https://keras.io/examples/structured_data/classification_with_tfdf/)
 [Classification with Neural Decision Forests](https://keras.io/examples/structured_data/deep_neural_decision_forests/)
 [Structured data learning with TabTransformer](https://keras.io/examples/structured_data/tabtransformer/)
 [Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/)
 [Collaborative Filtering for Movie Recommendations](https://keras.io/examples/structured_data/collaborative_filtering_movielens/)
 [A Transformer-based recommendation system](https://keras.io/examples/structured_data/movielens_recommendations_transformers/)
 [Timeseries](https://keras.io/examples/timeseries/)
 [Generative Deep Learning](https://keras.io/examples/generative/)
 [Audio Data](https://keras.io/examples/audio/)
 [Reinforcement Learning](https://keras.io/examples/rl/)
 [Graph Data](https://keras.io/examples/graph/)
 [Quick Keras Recipes](https://keras.io/examples/keras_recipes/)

► [Code examples](https://keras.io/examples/)
 / [Structured Data](https://keras.io/examples/structured_data/)
 / Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning

Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning
==============================================================================================

**Author:** [Humbulani Ndou](https://github.com/Humbulani1234)
  
**Date created:** 2025/03/17  
**Last modified:** 2025/03/17  
**Description:** Gated Residual and Variable Selection Networks prediction with HyperParameters tuning.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/structured_data/ipynb/class_with_grn_and_vsn_with_hyperparameters_tuning.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning.py)

* * *

Introduction
------------

The following example extends the script `structured_data/classification_with_grn_and_vsn.py` by incorporating hyperparameters tuning using [Autokeras](https://github.com/keras-team/autokeras)
 and [KerasTuner](https://github.com/keras-team/keras-tuner)
. Specifics regarding which APIs are used from the these two packages will be described in detail in the relevant code sections.

This example demonstrates the use of Gated Residual Networks (GRN) and Variable Selection Networks (VSN), proposed by Bryan Lim et al. in [Temporal Fusion Transformers (TFT) for Interpretable Multi-horizon Time Series Forecasting](https://arxiv.org/abs/1912.09363)
, for structured data classification. GRNs give the flexibility to the model to apply non-linear processing only where needed. VSNs allow the model to softly remove any unnecessary noisy inputs which could negatively impact performance. Together, those techniques help improving the learning capacity of deep neural network models.

Note that this example implements only the GRN and VSN components described in in the paper, rather than the whole TFT model, as GRN and VSN can be useful on their own for structured data learning tasks.

To run the code you need to use TensorFlow 2.3 or higher.

* * *

The dataset
-----------

[Our dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
 is provided by the Cleveland Clinic Foundation for Heart Disease. It's a CSV file with 303 rows. Each row contains information about a patient (a **sample**), and each column describes an attribute of the patient (a **feature**). We use the features to predict whether a patient has a heart disease (**binary classification**).

Here's the description of each feature:

| Column | Description | Feature Type |
| --- | --- | --- |
| Age | Age in years | Numerical |
| Sex | (1 = male; 0 = female) | Categorical |
| CP  | Chest pain type (0, 1, 2, 3, 4) | Categorical |
| Trestbpd | Resting blood pressure (in mm Hg on admission) | Numerical |
| Chol | Serum cholesterol in mg/dl | Numerical |
| FBS | fasting blood sugar in 120 mg/dl (1 = true; 0 = false) | Categorical |
| RestECG | Resting electrocardiogram results (0, 1, 2) | Categorical |
| Thalach | Maximum heart rate achieved | Numerical |
| Exang | Exercise induced angina (1 = yes; 0 = no) | Categorical |
| Oldpeak | ST depression induced by exercise relative to rest | Numerical |
| Slope | Slope of the peak exercise ST segment | Numerical |
| CA  | Number of major vessels (0-3) colored by fluoroscopy | Both numerical & categorical |
| Thal | 3 = normal; 6 = fixed defect; 7 = reversible defect | Categorical |
| Target | Diagnosis of heart disease (1 = true; 0 = false) | Target |

* * *

Setup
-----

Copied!

`import os import subprocess import tarfile import numpy as np import pandas as pd import tree from typing import Optional, Union  os.environ["KERAS_BACKEND"] = "tensorflow"  # or jax, or torch  # Keras imports import keras from keras import layers  # KerasTuner imports import keras_tuner from keras_tuner import HyperParameters  # AutoKeras imports import autokeras as ak from autokeras.utils import utils, types`

* * *

Preparing the data
------------------

Let's download the data and load it into a Pandas dataframe:

Copied!

`file_url = "http://storage.googleapis.com/download.tensorflow.org/data/heart.csv" dataframe = pd.read_csv(file_url)`

The dataset includes 303 samples with 14 columns per sample (13 features, plus the target label):

Copied!

`dataframe.shape`

`(303, 14)`

Here's a preview of a few samples:

Copied!

`dataframe.head()`

|     | age | sex | cp  | trestbps | chol | fbs | restecg | thalach | exang | oldpeak | slope | ca  | thal | target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 63  | 1   | 1   | 145 | 233 | 1   | 2   | 150 | 0   | 2.3 | 3   | 0   | fixed | 0   |
| 1   | 67  | 1   | 4   | 160 | 286 | 0   | 2   | 108 | 1   | 1.5 | 2   | 3   | normal | 1   |
| 2   | 67  | 1   | 4   | 120 | 229 | 0   | 2   | 129 | 1   | 2.6 | 2   | 2   | reversible | 0   |
| 3   | 37  | 1   | 3   | 130 | 250 | 0   | 0   | 187 | 0   | 3.5 | 3   | 0   | normal | 0   |
| 4   | 41  | 0   | 2   | 130 | 204 | 0   | 2   | 172 | 0   | 1.4 | 1   | 0   | normal | 0   |

The last column, "target", indicates whether the patient has a heart disease (1) or not (0).

Let's split the data into a training and validation set:

Copied!

`val_dataframe = dataframe.sample(frac=0.2, random_state=1337) train_dataframe = dataframe.drop(val_dataframe.index)  print(     f"Using {len(train_dataframe)} samples for training "     f"and {len(val_dataframe)} for validation" )`

`Using 242 samples for training and 61 for validation`

* * *

Define dataset metadata
-----------------------

Here, we define the metadata of the dataset that will be useful for reading and parsing the data into input features, and encoding the input features with respect to their types.

Copied!

`COLUMN_NAMES = [     "age",     "sex",     "cp",     "trestbps",     "chol",     "fbs",     "restecg",     "thalach",     "exang",     "oldpeak",     "slope",     "ca",     "thal",     "target", ] # Target feature name. TARGET_FEATURE_NAME = "target" # Numeric feature names. NUMERIC_FEATURE_NAMES = ["age", "trestbps", "thalach", "oldpeak", "slope", "chol"] # Categorical features and their vocabulary lists. # Note that we add 'v=' as a prefix to all categorical feature values to make # sure that they are treated as strings.  CATEGORICAL_FEATURES_WITH_VOCABULARY = {     feature_name: sorted(         [             # Integer categorcal must be int and string must be str             value if dataframe[feature_name].dtype == "int64" else str(value)             for value in list(dataframe[feature_name].unique())         ]     )     for feature_name in COLUMN_NAMES     if feature_name not in list(NUMERIC_FEATURE_NAMES + [TARGET_FEATURE_NAME]) } # All features names. FEATURE_NAMES = NUMERIC_FEATURE_NAMES + list(     CATEGORICAL_FEATURES_WITH_VOCABULARY.keys() )`

* * *

Feature preprocessing with Keras layers
---------------------------------------

The following features are categorical features encoded as integers:

*   `sex`
*   `cp`
*   `fbs`
*   `restecg`
*   `exang`
*   `ca`

We will encode these features using **one-hot encoding**. We have two options here:

*   Use `CategoryEncoding()`, which requires knowing the range of input values and will error on input outside the range.
*   Use `IntegerLookup()` which will build a lookup table for inputs and reserve an output index for unkown input values.

For this example, we want a simple solution that will handle out of range inputs at inference, so we will use `IntegerLookup()`.

We also have a categorical feature encoded as a string: `thal`. We will create an index of all possible features and encode output using the `StringLookup()` layer.

Finally, the following feature are continuous numerical features:

*   `age`
*   `trestbps`
*   `chol`
*   `thalach`
*   `oldpeak`
*   `slope`

For each of these features, we will use a `Normalization()` layer to make sure the mean of each feature is 0 and its standard deviation is 1.

Below, we define a utility function to do the operations:

*   `process` to one-hot encode string or integer categorical features.

Copied!

`# Tensorflow required for tf.data.Dataset import tensorflow as tf  # We process our datasets elements here (categorical) and convert them to indices to avoid this step # during model training since only tensorflow support strings. def encode_categorical(features, target):     for f in features:         if f in CATEGORICAL_FEATURES_WITH_VOCABULARY:             # Create a lookup to convert a string values to an integer indices.             # Since we are not using a mask token nor expecting any out of vocabulary             # (oov) token, we set mask_token to None and  num_oov_indices to 0.             cls = (                 layers.StringLookup                 if features[f].dtype == "string"                 else layers.IntegerLookup             )             features[f] = cls(                 vocabulary=CATEGORICAL_FEATURES_WITH_VOCABULARY[f],                 mask_token=None,                 num_oov_indices=0,                 output_mode="binary",             )(features[f])      # Change features from OrderedDict to Dict to match Inputs as they are Dict.     return dict(features), target`

Let's generate [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 objects for each dataframe:

Copied!

`def dataframe_to_dataset(dataframe):     dataframe = dataframe.copy()     labels = dataframe.pop("target")     ds = (         tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))         .map(encode_categorical)         .shuffle(buffer_size=len(dataframe))     )     return ds  train_ds = dataframe_to_dataset(train_dataframe) val_ds = dataframe_to_dataset(val_dataframe)`

Each `Dataset` yields a tuple `(input, target)` where `input` is a dictionary of features and `target` is the value `0` or `1`:

Copied!

`for x, y in train_ds.take(1):     print("Input:", x)     print("Target:", y)`

`Input: {'age': <tf.Tensor: shape=(), dtype=int64, numpy=37>, 'sex': <tf.Tensor: shape=(2,), dtype=int64, numpy=array([1, 0])>, 'cp': <tf.Tensor: shape=(5,), dtype=int64, numpy=array([0, 0, 0, 1, 0])>, 'trestbps': <tf.Tensor: shape=(), dtype=int64, numpy=120>, 'chol': <tf.Tensor: shape=(), dtype=int64, numpy=215>, 'fbs': <tf.Tensor: shape=(2,), dtype=int64, numpy=array([1, 0])>, 'restecg': <tf.Tensor: shape=(3,), dtype=int64, numpy=array([1, 0, 0])>, 'thalach': <tf.Tensor: shape=(), dtype=int64, numpy=170>, 'exang': <tf.Tensor: shape=(2,), dtype=int64, numpy=array([1, 0])>, 'oldpeak': <tf.Tensor: shape=(), dtype=float64, numpy=0.0>, 'slope': <tf.Tensor: shape=(), dtype=int64, numpy=1>, 'ca': <tf.Tensor: shape=(4,), dtype=int64, numpy=array([1, 0, 0, 0])>, 'thal': <tf.Tensor: shape=(5,), dtype=int64, numpy=array([0, 0, 0, 1, 0])>} Target: tf.Tensor(0, shape=(), dtype=int64)`

Let's batch the datasets:

Copied!

`train_ds = train_ds.batch(32) val_ds = val_ds.batch(32)`

* * *

Subclassing Autokeras Graph
---------------------------

Here we subclass the Autokeras `Graph`

*   `build`: we override this method to be able to handle model `Inputs` passed as dictionaries. In structured data analysis Inputs are normally passed as dictionaries for each feature of interest

Copied!

`class Graph(ak.graph.Graph):      def build(self, hp):         """Build the HyperModel into a Keras Model."""         keras_nodes = {}         keras_input_nodes = []         for node in self.inputs:             node_id = self._node_to_id[node]             input_node = node.build_node(hp)             output_node = node.build(hp, input_node)             keras_input_nodes.append(input_node)             keras_nodes[node_id] = output_node         for block in self.blocks:             temp_inputs = (                 {                     n.name: keras_nodes[self._node_to_id[n]]                     for n in block.inputs                     if isinstance(n, ak.Input)                 }                 if isinstance(block.inputs[0], ak.Input)                 else [keras_nodes[self._node_to_id[n]] for n in block.inputs]             )             outputs = tree.flatten(block.build(hp, inputs=temp_inputs))             for n, o in zip(block.outputs, outputs):                 keras_nodes[self._node_to_id[n]] = o         model = keras.models.Model(             keras_input_nodes,             [                 keras_nodes[self._node_to_id[output_node]]                 for output_node in self.outputs             ],         )         return self._compile_keras_model(hp, model)      def _compile_keras_model(self, hp, model):         # Specify hyperparameters from compile(...)         optimizer_name = hp.Choice(             "optimizer",             ["adam", "sgd"],             default="adam",         )         learning_rate = hp.Choice(             "learning_rate", [1e-1, 1e-2, 1e-3, 1e-4, 2e-5, 1e-5], default=1e-3         )         if optimizer_name == "adam":             optimizer = keras.optimizers.Adam(learning_rate=learning_rate)         elif optimizer_name == "sgd":             optimizer = keras.optimizers.SGD(learning_rate=learning_rate)         model.compile(             optimizer=optimizer,             metrics=self._get_metrics(),             loss=self._get_loss(),         )         return model`

* * *

Subclassing Autokeras `Input`
-----------------------------

Here we subclass the Autokeras Input node object and override the dtype attribute from None to a user supplied value. We also override the `build_node` method to use user supplied name for Inputs layers.

Copied!

`class Input(ak.Input):     def __init__(self, dtype, name=None, **kwargs):         super().__init__(name=name, **kwargs)         # Override dtype to a user dtype value         self.dtype = dtype         self.name = name      def build_node(self, hp):         return keras.Input(name=self.name, shape=self.shape, dtype=self.dtype)`

* * *

Subclassing ClassificationHead
------------------------------

Here we subclass Autokeras ClassificationHead and override the **init** method, and we add the method `get_expected_shape` to infer the labels shape. We remove the preprocessing fuctionality as we prefer to conduct such manually.

Copied!

`class ClassifierHead(ak.ClassificationHead):      def __init__(         self,         num_classes: Optional[int] = None,         multi_label: bool = False,         loss: Optional[types.LossType] = None,         metrics: Optional[types.MetricsType] = None,         dropout: Optional[float] = None,         **kwargs,     ):         self.num_classes = num_classes         self.multi_label = multi_label         self.dropout = dropout         if metrics is None:             metrics = ["accuracy"]         if loss is None:             loss = self.infer_loss()         ak.Head.__init__(self, loss=loss, metrics=metrics, **kwargs)         self.shape = self.get_expected_shape()      def get_expected_shape(self):         # Compute expected shape from num_classes.         if self.num_classes == 2 and not self.multi_label:             return [1]         return [self.num_classes]`

* * *

GatedLinearUnit Layer
---------------------

This is a keras layer defined in the script `structured_data/classification_with_grn_vsn.py` More details about this layer maybe found in the relevant script

Copied!

`class GatedLinearUnit(layers.Layer):     def __init__(self, num_units, activation, **kwargs):         super().__init__(**kwargs)         self.linear = layers.Dense(num_units)         self.sigmoid = layers.Dense(num_units, activation=activation)      def call(self, inputs):         return self.linear(inputs) * self.sigmoid(inputs)      def build(self):         self.built = True`

* * *

GatedResidualNetwork Layer
--------------------------

This is a keras layer defined in the script `structured_data/classification_with_grn_vsn.py` More details about this layer maybe found in the relevant script

Copied!

`class GatedResidualNetwork(layers.Layer):      def __init__(         self, num_units, dropout_rate, activation, use_layernorm=None, **kwargs     ):         super().__init__(**kwargs)         self.num_units = num_units         self.use_layernorm = use_layernorm         self.elu_dense = layers.Dense(num_units, activation=activation)         self.linear_dense = layers.Dense(num_units)         self.dropout = layers.Dropout(dropout_rate)         self.gated_linear_unit = GatedLinearUnit(num_units, activation)         self.layer_norm = layers.LayerNormalization()         self.project = layers.Dense(num_units)      def call(self, inputs, hp):         x = self.elu_dense(inputs)         x = self.linear_dense(x)         x = self.dropout(x)         if inputs.shape[-1] != self.num_units:             inputs = self.project(inputs)         x = inputs + self.gated_linear_unit(x)         use_layernorm = self.use_layernorm         if use_layernorm is None:             use_layernorm = hp.Boolean("use_layernorm", default=True)         if use_layernorm:             x = self.layer_norm(x)         return x      def build(self):         self.built = True`

* * *

Building the Autokeras `VariableSelection Block`
------------------------------------------------

We have converted the following keras layer to an Autokeras Block to include hyperapameters to tune. Refer to Autokeras blocks API for writing custom Blocks.

Copied!

`class VariableSelection(ak.Block):     def __init__(         self,         num_units: Optional[Union[int, HyperParameters.Choice]] = None,         dropout_rate: Optional[Union[float, HyperParameters.Choice]] = None,         activation: Optional[Union[str, HyperParameters.Choice]] = None,         **kwargs,     ):         super().__init__(**kwargs)         self.dropout = utils.get_hyperparameter(             dropout_rate,             HyperParameters().Choice("dropout", [0.0, 0.25, 0.5], default=0.0),             float,         )         self.num_units = utils.get_hyperparameter(             num_units,             HyperParameters().Choice(                 "num_units", [16, 32, 64, 128, 256, 512, 1024], default=16             ),             int,         )         self.activation = utils.get_hyperparameter(             activation,             HyperParameters().Choice(                 "vsn_activation", ["sigmoid", "elu"], default="sigmoid"             ),             str,         )      def build(self, hp, inputs):         num_units = utils.add_to_hp(self.num_units, hp, "num_units")         dropout_rate = utils.add_to_hp(self.dropout, hp, "dropout_rate")         activation = utils.add_to_hp(self.activation, hp, "activation")         concat_inputs = []         # Project the features to 'num_units' dimension         for input_ in inputs:             if input_ in CATEGORICAL_FEATURES_WITH_VOCABULARY:                 concat_inputs.append(                     keras.layers.Dense(units=num_units)(inputs[input_])                 )             else:                 # Create a Normalization layer for our feature                 normalizer = layers.Normalization()                 # Prepare a Dataset that only yields our feature                 feature_ds = train_ds.map(lambda x, y: x[input_]).map(                     lambda x: keras.ops.expand_dims(x, -1)                 )                 # Learn the statistics of the data                 normalizer.adapt(feature_ds)                 # Normalize the input feature                 normal_feature = normalizer(inputs[input_])                 concat_inputs.append(                     keras.layers.Dense(units=num_units)(normal_feature)                 )         v = layers.concatenate(concat_inputs)         v = GatedResidualNetwork(             num_units=num_units, dropout_rate=dropout_rate, activation=activation         )(v, hp=hp)         v = keras.ops.expand_dims(             layers.Dense(units=len(inputs), activation=activation)(v), axis=-1         )         x = []         x += [             GatedResidualNetwork(num_units, dropout_rate, activation)(i, hp=hp)             for i in concat_inputs         ]         x = keras.ops.stack(x, axis=1)         return keras.ops.squeeze(             keras.ops.matmul(keras.ops.transpose(v, axes=[0, 2, 1]), x), axis=1         )`

We create the HyperModel (from KerasTuner) Inputs which will be built into Keras Input objects
==============================================================================================

Copied!

`# Categorical features have different shapes after the encoding, dependent on the # vocabulary or unique values of each feature. We create them accordinly to match the # input data elements generated by tf.data.Dataset after pre-processing them def create_model_inputs():     inputs = {         f: (             Input(                 name=f,                 shape=(len(CATEGORICAL_FEATURES_WITH_VOCABULARY[f]),),                 dtype="int64",             )             if f in CATEGORICAL_FEATURES_WITH_VOCABULARY             else Input(name=f, shape=(1,), dtype="float32")         )         for f in FEATURE_NAMES     }     return inputs`

* * *

KerasTuner `HyperModel`
-----------------------

Here we use the Autokeras `Functional` API to construct a network of BlocksSSS which will be built into a KerasTuner HyperModel and finally to a Keras Model.

Copied!

`class MyHyperModel(keras_tuner.HyperModel):      def build(self, hp):         inputs = create_model_inputs()         features = VariableSelection()(inputs)         outputs = ClassifierHead(num_classes=2, multi_label=False)(features)         model = Graph(inputs=inputs, outputs=outputs)         model = model.build(hp)         return model      def fit(self, hp, model, *args, **kwargs):         return model.fit(             *args,             # Tune whether to shuffle the data in each epoch.             shuffle=hp.Boolean("shuffle"),             **kwargs,         )`

* * *

Using `RandomSearch` Tuner to find best HyperParameters
-------------------------------------------------------

We use the RandomSearch tuner to serach for hyparameters in the search space We also display the search space

Copied!

`print("Start training and searching for the best model...")  tuner = keras_tuner.RandomSearch(     MyHyperModel(),     objective="val_accuracy",     max_trials=3,     overwrite=True,     directory="my_dir",     project_name="tune_hypermodel", )  # Show the search space summary print("Tuner search space summary:\n") tuner.search_space_summary() # Search for best model tuner.search(train_ds, epochs=2, validation_data=val_ds)`

`Trial 3 Complete [00h 00m 16s] val_accuracy: 0.8032786846160889`

`Best val_accuracy So Far: 0.8032786846160889 Total elapsed time: 00h 00m 34s`

* * *

Extracting the best model
-------------------------

Copied!

`# Get the top model. models = tuner.get_best_models(num_models=1) best_model = models[0] best_model.summary()`

`/home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/saving/saving_lib.py:757: UserWarning: Skipping variable loading for optimizer 'adam', because it has 2 variables whereas the saved optimizer has 346 variables.    saveable.load_own_variables(weights_store.get(inner_path))`

Model: "functional"

┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Layer (type)        ┃ Output Shape      ┃    Param # ┃ Connected to      ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ age (InputLayer)    │ (None, 1)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ chol (InputLayer)   │ (None, 1)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ oldpeak             │ (None, 1)         │          0 │ -                 │
│ (InputLayer)        │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ slope (InputLayer)  │ (None, 1)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ thalach             │ (None, 1)         │          0 │ -                 │
│ (InputLayer)        │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ trestbps            │ (None, 1)         │          0 │ -                 │
│ (InputLayer)        │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ cast\_to\_float32     │ (None, 1)         │          0 │ age\[0\]\[0\]         │
│ (CastToFloat32)     │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ ca (InputLayer)     │ (None, 4)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ cast\_to\_float32\_2   │ (None, 1)         │          0 │ chol\[0\]\[0\]        │
│ (CastToFloat32)     │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ cp (InputLayer)     │ (None, 5)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ exang (InputLayer)  │ (None, 2)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ fbs (InputLayer)    │ (None, 2)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ cast\_to\_float32\_6   │ (None, 1)         │          0 │ oldpeak\[0\]\[0\]     │
│ (CastToFloat32)     │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ restecg             │ (None, 3)         │          0 │ -                 │
│ (InputLayer)        │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ sex (InputLayer)    │ (None, 2)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ cast\_to\_float32\_9   │ (None, 1)         │          0 │ slope\[0\]\[0\]       │
│ (CastToFloat32)     │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ thal (InputLayer)   │ (None, 5)         │          0 │ -                 │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ cast\_to\_float32\_11  │ (None, 1)         │          0 │ thalach\[0\]\[0\]     │
│ (CastToFloat32)     │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ cast\_to\_float32\_12  │ (None, 1)         │          0 │ trestbps\[0\]\[0\]    │
│ (CastToFloat32)     │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ normalization       │ (None, 1)         │          3 │ cast\_to\_float32\[… │\
│ (Normalization)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ cast\_to\_float32\_1   │ (None, 4)         │          0 │ ca\[0\]\[0\]          │\
│ (CastToFloat32)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ normalization\_1     │ (None, 1)         │          3 │ cast\_to\_float32\_… │\
│ (Normalization)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ cast\_to\_float32\_3   │ (None, 5)         │          0 │ cp\[0\]\[0\]          │\
│ (CastToFloat32)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ cast\_to\_float32\_4   │ (None, 2)         │          0 │ exang\[0\]\[0\]       │\
│ (CastToFloat32)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ cast\_to\_float32\_5   │ (None, 2)         │          0 │ fbs\[0\]\[0\]         │\
│ (CastToFloat32)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ normalization\_2     │ (None, 1)         │          3 │ cast\_to\_float32\_… │\
│ (Normalization)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ cast\_to\_float32\_7   │ (None, 3)         │          0 │ restecg\[0\]\[0\]     │\
│ (CastToFloat32)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ cast\_to\_float32\_8   │ (None, 2)         │          0 │ sex\[0\]\[0\]         │\
│ (CastToFloat32)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ normalization\_3     │ (None, 1)         │          3 │ cast\_to\_float32\_… │\
│ (Normalization)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ cast\_to\_float32\_10  │ (None, 5)         │          0 │ thal\[0\]\[0\]        │\
│ (CastToFloat32)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ normalization\_4     │ (None, 1)         │          3 │ cast\_to\_float32\_… │\
│ (Normalization)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ normalization\_5     │ (None, 1)         │          3 │ cast\_to\_float32\_… │\
│ (Normalization)     │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense (Dense)       │ (None, 16)        │         32 │ normalization\[0\]… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_1 (Dense)     │ (None, 16)        │         80 │ cast\_to\_float32\_… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_2 (Dense)     │ (None, 16)        │         32 │ normalization\_1\[… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_3 (Dense)     │ (None, 16)        │         96 │ cast\_to\_float32\_… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_4 (Dense)     │ (None, 16)        │         48 │ cast\_to\_float32\_… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_5 (Dense)     │ (None, 16)        │         48 │ cast\_to\_float32\_… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_6 (Dense)     │ (None, 16)        │         32 │ normalization\_2\[… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_7 (Dense)     │ (None, 16)        │         64 │ cast\_to\_float32\_… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_8 (Dense)     │ (None, 16)        │         48 │ cast\_to\_float32\_… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_9 (Dense)     │ (None, 16)        │         32 │ normalization\_3\[… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_10 (Dense)    │ (None, 16)        │         96 │ cast\_to\_float32\_… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_11 (Dense)    │ (None, 16)        │         32 │ normalization\_4\[… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_12 (Dense)    │ (None, 16)        │         32 │ normalization\_5\[… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ concatenate         │ (None, 208)       │          0 │ dense\[0\]\[0\],      │\
│ (Concatenate)       │                   │            │ dense\_1\[0\]\[0\],    │\
│                     │                   │            │ dense\_2\[0\]\[0\],    │\
│                     │                   │            │ dense\_3\[0\]\[0\],    │\
│                     │                   │            │ dense\_4\[0\]\[0\],    │\
│                     │                   │            │ dense\_5\[0\]\[0\],    │\
│                     │                   │            │ dense\_6\[0\]\[0\],    │\
│                     │                   │            │ dense\_7\[0\]\[0\],    │\
│                     │                   │            │ dense\_8\[0\]\[0\],    │\
│                     │                   │            │ dense\_9\[0\]\[0\],    │\
│                     │                   │            │ dense\_10\[0\]\[0\],   │\
│                     │                   │            │ dense\_11\[0\]\[0\],   │\
│                     │                   │            │ dense\_12\[0\]\[0\]    │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      7,536 │ concatenate\[0\]\[0\] │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_18 (Dense)    │ (None, 13)        │        221 │ gated\_residual\_n… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ expand\_dims         │ (None, 13, 1)     │          0 │ dense\_18\[0\]\[0\]    │\
│ (ExpandDims)        │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\[0\]\[0\]       │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_1\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_2\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_3\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_4\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_5\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_6\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_7\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_8\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_9\[0\]\[0\]     │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_10\[0\]\[0\]    │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_11\[0\]\[0\]    │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ gated\_residual\_net… │ (None, 16)        │      1,120 │ dense\_12\[0\]\[0\]    │\
│ (GatedResidualNetw… │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ transpose           │ (None, 1, 13)     │          0 │ expand\_dims\[0\]\[0\] │\
│ (Transpose)         │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ stack (Stack)       │ (None, 13, 16)    │          0 │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
│                     │                   │            │ gated\_residual\_n… │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ matmul (Matmul)     │ (None, 1, 16)     │          0 │ transpose\[0\]\[0\],  │\
│                     │                   │            │ stack\[0\]\[0\]       │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ squeeze (Squeeze)   │ (None, 16)        │          0 │ matmul\[0\]\[0\]      │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dropout\_14          │ (None, 16)        │          0 │ squeeze\[0\]\[0\]     │\
│ (Dropout)           │                   │            │                   │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ dense\_84 (Dense)    │ (None, 1)         │         17 │ dropout\_14\[0\]\[0\]  │\
├─────────────────────┼───────────────────┼────────────┼───────────────────┤\
│ classifier\_head\_1   │ (None, 1)         │          0 │ dense\_84\[0\]\[0\]    │\
│ (Activation)        │                   │            │                   │\
└─────────────────────┴───────────────────┴────────────┴───────────────────┘\
\
 Total params: 23,024 (89.96 KB)\
\
 Trainable params: 23,006 (89.87 KB)\
\
 Non-trainable params: 18 (96.00 B)\
\
* * *\
\
Inference on new data\
---------------------\
\
To get a prediction for a new sample, you can simply call `model.predict()`. There are just two things you need to do:\
\
1.  wrap scalars into a list so as to have a batch dimension (models only process batches of data, not single samples)\
2.  Call `convert_to_tensor` on each feature\
\
Copied!\
\
`sample = {     "age": 60,     "sex": 1,     "cp": 1,     "trestbps": 145,     "chol": 233,     "fbs": 1,     "restecg": 2,     "thalach": 150,     "exang": 0,     "oldpeak": 2.3,     "slope": 3,     "ca": 0,     "thal": "fixed", }  # Given the category (in the sample above - key) and the category value (in the sample above - value), # we return its one-hot encoding def get_cat_encoding(cat, cat_value):     # Create a list of zeros with the same length as categories     encoding = [0] * len(cat)     # Find the index of category_value in categories and set the corresponding position to 1     if cat_value in cat:         encoding[cat.index(cat_value)] = 1     return encoding  for name, value in sample.items():     if name in CATEGORICAL_FEATURES_WITH_VOCABULARY:         sample.update(             {                 name: get_cat_encoding(                     CATEGORICAL_FEATURES_WITH_VOCABULARY[name], sample[name]                 )             }         ) # Convert inputs to tensors input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()} predictions = best_model.predict(input_dict)  print(     f"This particular patient had a {100 * predictions[0][0]:.1f} "     "percent probability of having a heart disease, "     "as evaluated by our model." )`\
\
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 136ms/step\
\
``\
\
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 162ms/step\
\
`This particular patient had a 28.1 percent probability of having a heart disease, as evaluated by our model.`\
\
[Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#classification-with-gated-residual-and-variable-selection-networks-with-hyperparameters-tuning)\
\
[Introduction](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#introduction)\
\
[The dataset](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#the-dataset)\
\
[Setup](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#setup)\
\
[Preparing the data](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#preparing-the-data)\
\
[Define dataset metadata](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#define-dataset-metadata)\
\
[Feature preprocessing with Keras layers](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#feature-preprocessing-with-keras-layers)\
\
[Subclassing Autokeras Graph](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#subclassing-autokeras-graph)\
\
[Subclassing Autokeras `Input`](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#subclassing-autokeras-input)\
\
[Subclassing ClassificationHead](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#subclassing-classificationhead)\
\
[GatedLinearUnit Layer](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#gatedlinearunit-layer)\
\
[GatedResidualNetwork Layer](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#gatedresidualnetwork-layer)\
\
[Building the Autokeras `VariableSelection Block`](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#building-the-autokeras-variableselection-block)\
\
[We create the HyperModel (from KerasTuner) Inputs which will be built into Keras Input objects](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#we-create-the-hypermodel-from-kerastuner-inputs-which-will-be-built-into-keras-input-objects)\
\
[KerasTuner `HyperModel`](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#kerastuner-hypermodel)\
\
[Using `RandomSearch` Tuner to find best HyperParameters](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#-using-randomsearch-tuner-to-find-best-hyperparameters)\
\
[Extracting the best model](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#extracting-the-best-model)\
\
[Inference on new data](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/#inference-on-new-data)