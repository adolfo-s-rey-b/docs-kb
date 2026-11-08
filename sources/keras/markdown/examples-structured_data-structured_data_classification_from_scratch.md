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
 / Structured data classification from scratch

Structured data classification from scratch
===========================================

**Author:** [fchollet](https://twitter.com/fchollet)
  
**Date created:** 2020/06/09  
**Last modified:** 2020/06/09  
**Description:** Binary classification of structured data including numerical and categorical features.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/structured_data/ipynb/structured_data_classification_from_scratch.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/structured_data/structured_data_classification_from_scratch.py)

* * *

Introduction
------------

This example demonstrates how to do structured data classification, starting from a raw CSV file. Our data includes both numerical and categorical features. We will use Keras preprocessing layers to normalize the numerical features and vectorize the categorical ones.

Note that this example should be run with TensorFlow 2.5 or higher.

### The dataset

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

`import os  os.environ["KERAS_BACKEND"] = "torch"  # or torch, or tensorflow  import pandas as pd import keras from keras import layers`

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

Below, we define 2 utility functions to do the operations:

*   `encode_numerical_feature` to apply featurewise normalization to numerical features.
*   `process` to one-hot encode string or integer categorical features.

Copied!

`# Tensorflow required for tf.data.Dataset import tensorflow as tf  # We process our datasets elements here (categorical) and convert them to indices to avoid this step # during model training since only tensorflow support strings. def encode_categorical(features, target):     for feature_name in features:         if feature_name in CATEGORICAL_FEATURES_WITH_VOCABULARY:             lookup_class = (                 layers.StringLookup                 if features[feature_name].dtype == "string"                 else layers.IntegerLookup             )             vocabulary = CATEGORICAL_FEATURES_WITH_VOCABULARY[feature_name]             # Create a lookup to convert a string values to an integer indices.             # Since we are not using a mask token nor expecting any out of vocabulary             # (oov) token, we set mask_token to None and  num_oov_indices to 0.             index = lookup_class(                 vocabulary=vocabulary,                 mask_token=None,                 num_oov_indices=0,                 output_mode="binary",             )             # Convert the string input values into integer indices.             value_index = index(features[feature_name])             features[feature_name] = value_index          else:             pass      # Change features from OrderedDict to Dict to match Inputs as they are Dict.     return dict(features), target  def encode_numerical_feature(feature, name, dataset):     # Create a Normalization layer for our feature     normalizer = layers.Normalization()     # Prepare a Dataset that only yields our feature     feature_ds = dataset.map(lambda x, y: x[name])     feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))     # Learn the statistics of the data     normalizer.adapt(feature_ds)     # Normalize the input feature     encoded_feature = normalizer(feature)     return encoded_feature`

Let's generate [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 objects for each dataframe:

Copied!

`def dataframe_to_dataset(dataframe):     dataframe = dataframe.copy()     labels = dataframe.pop("target")     ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels)).map(         encode_categorical     )     ds = ds.shuffle(buffer_size=len(dataframe))     return ds  train_ds = dataframe_to_dataset(train_dataframe) val_ds = dataframe_to_dataset(val_dataframe)`

Each `Dataset` yields a tuple `(input, target)` where `input` is a dictionary of features and `target` is the value `0` or `1`:

Copied!

`for x, y in train_ds.take(1):     print("Input:", x)     print("Target:", y)`

`Input: {'age': <tf.Tensor: shape=(), dtype=int64, numpy=45>, 'sex': <tf.Tensor: shape=(2,), dtype=int64, numpy=array([0, 1])>, 'cp': <tf.Tensor: shape=(5,), dtype=int64, numpy=array([0, 0, 0, 0, 1])>, 'trestbps': <tf.Tensor: shape=(), dtype=int64, numpy=142>, 'chol': <tf.Tensor: shape=(), dtype=int64, numpy=309>, 'fbs': <tf.Tensor: shape=(2,), dtype=int64, numpy=array([1, 0])>, 'restecg': <tf.Tensor: shape=(3,), dtype=int64, numpy=array([0, 0, 1])>, 'thalach': <tf.Tensor: shape=(), dtype=int64, numpy=147>, 'exang': <tf.Tensor: shape=(2,), dtype=int64, numpy=array([0, 1])>, 'oldpeak': <tf.Tensor: shape=(), dtype=float64, numpy=0.0>, 'slope': <tf.Tensor: shape=(), dtype=int64, numpy=2>, 'ca': <tf.Tensor: shape=(4,), dtype=int64, numpy=array([0, 0, 0, 1])>, 'thal': <tf.Tensor: shape=(5,), dtype=int64, numpy=array([0, 0, 0, 0, 1])>} Target: tf.Tensor(1, shape=(), dtype=int64)`

Let's batch the datasets:

Copied!

`train_ds = train_ds.batch(32) val_ds = val_ds.batch(32)`

* * *

Build a model
-------------

With this done, we can create our end-to-end model:

Copied!

`# Categorical features have different shapes after the encoding, dependent on the # vocabulary or unique values of each feature. We create them accordinly to match the # input data elements generated by tf.data.Dataset after pre-processing them def create_model_inputs():     inputs = {}      # This a helper function for creating categorical features     def create_input_helper(feature_name):         num_categories = len(CATEGORICAL_FEATURES_WITH_VOCABULARY[feature_name])         inputs[feature_name] = layers.Input(             name=feature_name, shape=(num_categories,), dtype="int64"         )         return inputs      for feature_name in FEATURE_NAMES:         if feature_name in CATEGORICAL_FEATURES_WITH_VOCABULARY:             # Categorical features             create_input_helper(feature_name)         else:             # Make them float32, they are Real numbers             feature_input = layers.Input(name=feature_name, shape=(1,), dtype="float32")             # Process the Inputs here             inputs[feature_name] = encode_numerical_feature(                 feature_input, feature_name, train_ds             )     return inputs  # This Layer defines the logic of the Model to perform the classification class Classifier(keras.layers.Layer):      def __init__(self, **kwargs):         super().__init__(**kwargs)         self.dense_1 = layers.Dense(32, activation="relu")         self.dropout = layers.Dropout(0.5)         self.dense_2 = layers.Dense(1, activation="sigmoid")      def call(self, inputs):         all_features = layers.concatenate(list(inputs.values()))         x = self.dense_1(all_features)         x = self.dropout(x)         output = self.dense_2(x)         return output      # Surpress build warnings     def build(self, input_shape):         self.built = True  # Create the Classifier model def create_model():     all_inputs = create_model_inputs()     output = Classifier()(all_inputs)     model = keras.Model(all_inputs, output)     return model  model = create_model() model.compile("adam", "binary_crossentropy", metrics=["accuracy"])`

``/home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/models/functional.py:106: UserWarning: When providing `inputs` as a dict, all keys in the dict must match the names of the corresponding tensors. Received key 'age' mapping to value <KerasTensor shape=(None, 1), dtype=float32, sparse=False, name=keras_tensor> which has name 'keras_tensor'. Change the tensor name to 'age' (via `Input(..., name='age')`)   warnings.warn( /home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/models/functional.py:106: UserWarning: When providing `inputs` as a dict, all keys in the dict must match the names of the corresponding tensors. Received key 'trestbps' mapping to value <KerasTensor shape=(None, 1), dtype=float32, sparse=False, name=keras_tensor_1> which has name 'keras_tensor_1'. Change the tensor name to 'trestbps' (via `Input(..., name='trestbps')`)   warnings.warn( /home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/models/functional.py:106: UserWarning: When providing `inputs` as a dict, all keys in the dict must match the names of the corresponding tensors. Received key 'thalach' mapping to value <KerasTensor shape=(None, 1), dtype=float32, sparse=False, name=keras_tensor_2> which has name 'keras_tensor_2'. Change the tensor name to 'thalach' (via `Input(..., name='thalach')`)   warnings.warn( /home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/models/functional.py:106: UserWarning: When providing `inputs` as a dict, all keys in the dict must match the names of the corresponding tensors. Received key 'oldpeak' mapping to value <KerasTensor shape=(None, 1), dtype=float32, sparse=False, name=keras_tensor_3> which has name 'keras_tensor_3'. Change the tensor name to 'oldpeak' (via `Input(..., name='oldpeak')`)   warnings.warn( /home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/models/functional.py:106: UserWarning: When providing `inputs` as a dict, all keys in the dict must match the names of the corresponding tensors. Received key 'slope' mapping to value <KerasTensor shape=(None, 1), dtype=float32, sparse=False, name=keras_tensor_4> which has name 'keras_tensor_4'. Change the tensor name to 'slope' (via `Input(..., name='slope')`)   warnings.warn( /home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/models/functional.py:106: UserWarning: When providing `inputs` as a dict, all keys in the dict must match the names of the corresponding tensors. Received key 'chol' mapping to value <KerasTensor shape=(None, 1), dtype=float32, sparse=False, name=keras_tensor_5> which has name 'keras_tensor_5'. Change the tensor name to 'chol' (via `Input(..., name='chol')`)   warnings.warn(``

Let's visualize our connectivity graph:

Copied!

``# `rankdir='LR'` is to make the graph horizontal. keras.utils.plot_model(model, show_shapes=True, rankdir="LR")``

![png](https://keras.io/img/examples/structured_data/structured_data_classification_from_scratch/structured_data_classification_from_scratch_25_0.png)

* * *

Train the model
---------------

Copied!

`model.fit(train_ds, epochs=50, validation_data=val_ds)`

`Epoch 1/50`

1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 102ms/step - accuracy: 0.4688 - loss: 8.0563\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 8ms/step - accuracy: 0.4732 - loss: 7.9796\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.4725 - loss: 7.9848 - val\_accuracy: 0.2295 - val\_loss: 12.0816\
\
`Epoch 2/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 105ms/step - accuracy: 0.5000 - loss: 6.6368\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 8ms/step - accuracy: 0.4532 - loss: 7.8320\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 18ms/step - accuracy: 0.4547 - loss: 7.8310 - val\_accuracy: 0.2459 - val\_loss: 6.2543\
\
`Epoch 3/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 91ms/step - accuracy: 0.5000 - loss: 7.6558\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.5041 - loss: 7.3378\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 19ms/step - accuracy: 0.5087 - loss: 7.2802 - val\_accuracy: 0.6885 - val\_loss: 2.1633\
\
`Epoch 4/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 93ms/step - accuracy: 0.4375 - loss: 8.9030\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 8ms/step - accuracy: 0.4815 - loss: 8.0109\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 19ms/step - accuracy: 0.4858 - loss: 7.9351 - val\_accuracy: 0.7705 - val\_loss: 3.3916\
\
`Epoch 5/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 88ms/step - accuracy: 0.4688 - loss: 8.1279\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.5049 - loss: 7.4815\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.5117 - loss: 7.4054 - val\_accuracy: 0.7705 - val\_loss: 3.6911\
\
`Epoch 6/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 107ms/step - accuracy: 0.4688 - loss: 7.8832\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.4940 - loss: 7.4615\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.5121 - loss: 7.1851 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 7/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 101ms/step - accuracy: 0.5312 - loss: 6.9446\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 12ms/step - accuracy: 0.5357 - loss: 6.5511\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.5497 - loss: 6.3711 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 8/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 110ms/step - accuracy: 0.5938 - loss: 6.3905\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.6192 - loss: 5.9601\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6101 - loss: 6.0728 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 9/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 108ms/step - accuracy: 0.5938 - loss: 6.5442\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.6006 - loss: 6.3309\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step - accuracy: 0.5949 - loss: 6.3647 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 10/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 113ms/step - accuracy: 0.5625 - loss: 6.8250\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 10ms/step - accuracy: 0.5675 - loss: 6.5020\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.5764 - loss: 6.3308 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 11/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 116ms/step - accuracy: 0.6250 - loss: 4.3582\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.6053 - loss: 5.4824\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6076 - loss: 5.4500 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 12/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 118ms/step - accuracy: 0.5625 - loss: 7.0064\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.5740 - loss: 6.4431\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step - accuracy: 0.5787 - loss: 6.3510 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 13/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 115ms/step - accuracy: 0.7500 - loss: 3.7382\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 10ms/step - accuracy: 0.6812 - loss: 4.7893\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step - accuracy: 0.6712 - loss: 4.9453 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 14/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 114ms/step - accuracy: 0.6562 - loss: 5.5498\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.6580 - loss: 5.4636\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - accuracy: 0.6578 - loss: 5.4379 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 15/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 113ms/step - accuracy: 0.5938 - loss: 5.8118\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 8ms/step - accuracy: 0.5978 - loss: 5.9295\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step - accuracy: 0.6045 - loss: 5.8426 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 16/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 115ms/step - accuracy: 0.6562 - loss: 4.4893\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.5763 - loss: 5.9135\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.5814 - loss: 5.8590 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 17/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 127ms/step - accuracy: 0.5625 - loss: 7.0281\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.6071 - loss: 6.0424\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 24ms/step - accuracy: 0.6179 - loss: 5.8262 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 18/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 130ms/step - accuracy: 0.6562 - loss: 5.3547\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.6701 - loss: 5.0648\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - accuracy: 0.6713 - loss: 5.0607 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 19/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 121ms/step - accuracy: 0.7500 - loss: 4.0295\
\
``\
\
5/8 ━━━━━━━━━━━━\[37m━━━━━━━━ 0s 13ms/step - accuracy: 0.7157 - loss: 4.3995\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - accuracy: 0.7077 - loss: 4.4886 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 20/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 129ms/step - accuracy: 0.6250 - loss: 6.0278\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.6479 - loss: 5.4982\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 24ms/step - accuracy: 0.6461 - loss: 5.4898 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 21/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 134ms/step - accuracy: 0.5938 - loss: 5.8592\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.6782 - loss: 4.7529\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step - accuracy: 0.6627 - loss: 5.0219 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 22/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 127ms/step - accuracy: 0.6875 - loss: 5.0149\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.6342 - loss: 5.5898\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - accuracy: 0.6290 - loss: 5.6701 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 23/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 121ms/step - accuracy: 0.5938 - loss: 6.0783\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.6259 - loss: 5.6908\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 24ms/step - accuracy: 0.6352 - loss: 5.5719 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 24/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 112ms/step - accuracy: 0.7812 - loss: 3.1021\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 12ms/step - accuracy: 0.7353 - loss: 3.8725\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step - accuracy: 0.7163 - loss: 4.1637 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 25/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 112ms/step - accuracy: 0.5625 - loss: 6.9224\
\
``\
\
5/8 ━━━━━━━━━━━━\[37m━━━━━━━━ 0s 13ms/step - accuracy: 0.6331 - loss: 5.5663\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step - accuracy: 0.6416 - loss: 5.4024 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 26/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 117ms/step - accuracy: 0.6875 - loss: 4.4043\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.6668 - loss: 5.0742\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6743 - loss: 4.9986 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 27/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 104ms/step - accuracy: 0.6562 - loss: 5.3405\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 8ms/step - accuracy: 0.6868 - loss: 4.7990\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - accuracy: 0.6838 - loss: 4.8458 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 28/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 116ms/step - accuracy: 0.6562 - loss: 4.8092\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.7061 - loss: 4.3996\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - accuracy: 0.7053 - loss: 4.4297 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 29/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 114ms/step - accuracy: 0.6250 - loss: 5.6655\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 10ms/step - accuracy: 0.6536 - loss: 5.3912\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step - accuracy: 0.6589 - loss: 5.3014 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 30/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 116ms/step - accuracy: 0.7812 - loss: 3.5258\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.6900 - loss: 4.7711\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - accuracy: 0.6882 - loss: 4.8074 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 31/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 123ms/step - accuracy: 0.5938 - loss: 6.5425\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 10ms/step - accuracy: 0.6346 - loss: 5.6779\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6423 - loss: 5.5672 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 32/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 120ms/step - accuracy: 0.6250 - loss: 5.6215\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.6451 - loss: 5.2140\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step - accuracy: 0.6556 - loss: 5.0993 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 33/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 115ms/step - accuracy: 0.7188 - loss: 4.2096\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.7218 - loss: 4.3075\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step - accuracy: 0.7143 - loss: 4.4143 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 34/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 114ms/step - accuracy: 0.5625 - loss: 7.0242\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.6608 - loss: 5.3428\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 24ms/step - accuracy: 0.6675 - loss: 5.2031 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 35/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 105ms/step - accuracy: 0.6875 - loss: 5.0369\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.6601 - loss: 5.2386\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 24ms/step - accuracy: 0.6675 - loss: 5.0972 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 36/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 114ms/step - accuracy: 0.6562 - loss: 4.8957\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.7086 - loss: 4.4144\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step - accuracy: 0.6980 - loss: 4.5912 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 37/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 115ms/step - accuracy: 0.6250 - loss: 6.0333\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.6438 - loss: 5.6852\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step - accuracy: 0.6551 - loss: 5.4504 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 38/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 119ms/step - accuracy: 0.5938 - loss: 6.4043\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.6659 - loss: 5.2220\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6751 - loss: 5.0637 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 39/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 122ms/step - accuracy: 0.5625 - loss: 7.0517\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 10ms/step - accuracy: 0.6782 - loss: 5.0396\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6854 - loss: 4.9129 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 40/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 121ms/step - accuracy: 0.6562 - loss: 5.4278\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.6575 - loss: 5.2183\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6676 - loss: 5.0430 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 41/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 120ms/step - accuracy: 0.7500 - loss: 3.9611\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 10ms/step - accuracy: 0.7322 - loss: 4.2233\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 24ms/step - accuracy: 0.7325 - loss: 4.2274 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 42/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 127ms/step - accuracy: 0.8438 - loss: 2.5075\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.7483 - loss: 3.8605\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - accuracy: 0.7305 - loss: 4.1423 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 43/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 132ms/step - accuracy: 0.7188 - loss: 4.5277\
\
``\
\
5/8 ━━━━━━━━━━━━\[37m━━━━━━━━ 0s 15ms/step - accuracy: 0.6698 - loss: 5.2541\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - accuracy: 0.6831 - loss: 4.9995 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 44/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 1s 149ms/step - accuracy: 0.7188 - loss: 4.3368\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 12ms/step - accuracy: 0.6884 - loss: 4.8941\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - accuracy: 0.6877 - loss: 4.9237 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 45/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 113ms/step - accuracy: 0.7188 - loss: 3.6048\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.6953 - loss: 4.5189\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 24ms/step - accuracy: 0.6914 - loss: 4.6078 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 46/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 120ms/step - accuracy: 0.7188 - loss: 4.5277\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.7298 - loss: 4.2710\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - accuracy: 0.7214 - loss: 4.4175 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 47/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 117ms/step - accuracy: 0.7500 - loss: 4.0295\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.6962 - loss: 4.8892\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - accuracy: 0.6981 - loss: 4.8478 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 48/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 122ms/step - accuracy: 0.7812 - loss: 3.4540\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 9ms/step - accuracy: 0.7095 - loss: 4.5553\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step - accuracy: 0.7080 - loss: 4.5585 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 49/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 117ms/step - accuracy: 0.6875 - loss: 4.5707\
\
``\
\
7/8 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 10ms/step - accuracy: 0.6914 - loss: 4.7756\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6939 - loss: 4.7445 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`Epoch 50/50`\
\
1/8 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 124ms/step - accuracy: 0.7188 - loss: 4.0735\
\
``\
\
6/8 ━━━━━━━━━━━━━━━\[37m━━━━━ 0s 11ms/step - accuracy: 0.7049 - loss: 4.3802\
\
``\
\
8/8 ━━━━━━━━━━━━━━━━━━━━ 0s 22ms/step - accuracy: 0.6987 - loss: 4.5132 - val\_accuracy: 0.7705 - val\_loss: 3.6992\
\
`<keras.src.callbacks.history.History at 0x747bef08e590>`\
\
We quickly get to 80% validation accuracy.\
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
`sample = {     "age": 60,     "sex": 1,     "cp": 1,     "trestbps": 145,     "chol": 233,     "fbs": 1,     "restecg": 2,     "thalach": 150,     "exang": 0,     "oldpeak": 2.3,     "slope": 3,     "ca": 0,     "thal": "fixed", }  # Given the category (in the sample above - key) and the category value (in the sample above - value), # we return its one-hot encoding def get_cat_encoding(cat, cat_value):     # Create a list of zeros with the same length as categories     encoding = [0] * len(cat)     # Find the index of category_value in categories and set the corresponding position to 1     if cat_value in cat:         encoding[cat.index(cat_value)] = 1     return encoding  for name, value in sample.items():     if name in CATEGORICAL_FEATURES_WITH_VOCABULARY:         sample.update(             {                 name: get_cat_encoding(                     CATEGORICAL_FEATURES_WITH_VOCABULARY[name], sample[name]                 )             }         ) # Convert inputs to tensors input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()} predictions = model.predict(input_dict)  print(     f"This particular patient had a {100 * predictions[0][0]:.1f} "     "percent probability of having a heart disease, "     "as evaluated by our model." )`\
\
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 77ms/step\
\
``\
\
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 79ms/step\
\
`This particular patient had a 0.0 percent probability of having a heart disease, as evaluated by our model.`\
\
* * *\
\
Conclusions\
-----------\
\
*   The orignal model (the one that runs only on tensorflow) converges quickly to around 80% and remains there for extended periods and at times hits 85%\
*   The updated model (the backed-agnostic) model may fluctuate between 78% and 83% and at times hitting 86% validation accuracy and converges around 80% also.\
\
[Structured data classification from scratch](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#structured-data-classification-from-scratch)\
\
[Introduction](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#introduction)\
\
[The dataset](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#the-dataset)\
\
[Setup](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#setup)\
\
[Preparing the data](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#preparing-the-data)\
\
[Define dataset metadata](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#define-dataset-metadata)\
\
[Feature preprocessing with Keras layers](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#feature-preprocessing-with-keras-layers)\
\
[Build a model](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#build-a-model)\
\
[Train the model](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#train-the-model)\
\
[Inference on new data](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#inference-on-new-data)\
\
[Conclusions](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/#conclusions)