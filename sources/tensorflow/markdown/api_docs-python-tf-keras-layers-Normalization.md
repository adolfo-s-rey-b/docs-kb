[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#methods)
    *   [adapt](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#adapt)
        
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#convert_weight)
        
    *   [finalize\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#finalize_state)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Normalization Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#methods)
    *   [adapt](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#adapt)
        
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#convert_weight)
        
    *   [finalize\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#finalize_state)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Normalization#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/normalization.py#L21-L471)

A preprocessing layer that normalizes continuous features.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Normalization(
        axis=-1, mean=None, variance=None, invert=False, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers) | *   [Load a pandas DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)<br>    <br>*   [Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression)<br>    <br>*   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)<br>    <br>*   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Classify structured data using Keras preprocessing layers](https://www.tensorflow.org/tutorials/structured_data/preprocessing_layers) |

This layer will shift and scale inputs into a distribution centered around 0 with standard deviation 1. It accomplishes this by precomputing the mean and variance of the data, and calling `(input - mean) / sqrt(var)` at runtime.

The mean and variance values for the layer must be either supplied on construction or learned via `adapt()`. `adapt()` will compute the mean and variance of the data and store them as the layer's weights. `adapt()` should be called before `fit()`, `evaluate()`, or `predict()`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `axis` | Integer, tuple of integers, or None. The axis or axes that should have a separate mean and variance for each index in the shape. For example, if shape is `(None, 5)` and `axis=1`, the layer will track 5 separate mean and variance values for the last axis. If `axis` is set to `None`, the layer will normalize all elements in the input by a scalar mean and variance. When `-1`, the last axis of the input is assumed to be a feature dimension and is normalized per index. Note that in the specific case of batched scalar inputs where the only axis is the batch axis, the default will normalize each index in the batch separately. In this case, consider passing `axis=None`. Defaults to `-1`. |
| `mean` | The mean value(s) to use during normalization. The passed value(s) will be broadcast to the shape of the kept axes above; if the value(s) cannot be broadcast, an error will be raised when this layer's `build()` method is called. `mean` and `variance` must be specified together. |
| `variance` | The variance value(s) to use during normalization. The passed value(s) will be broadcast to the shape of the kept axes above; if the value(s) cannot be broadcast, an error will be raised when this layer's `build()` method is called. `mean` and `variance` must be specified together. |
| `invert` | If `True`, this layer will apply the inverse transformation to its inputs: it would turn a normalized input back into its original form. |

#### Examples:

Calculate a global mean and variance by analyzing the dataset in `adapt()`.

    adapt_data = np.array([1., 2., 3., 4., 5.], dtype='float32')

Calculate a mean and variance for each index on the last axis.

    adapt_data = np.array([[0., 7., 4.],\
\
Pass the mean and variance directly.\
\
    input_data = np.array([[1.], [2.], [3.]], dtype='float32')\
\
Use the layer to de-normalize inputs (after adapting the layer).\
\
    adapt_data = np.array([[0., 7., 4.],\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
\
Methods\
-------\
\
### `adapt`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/normalization.py#L251-L397)\
\
adapt(\
        data\
    )\
\
Computes the mean and variance of values in a dataset.\
\
Calling `adapt()` on a `Normalization` layer is an alternative to passing in `mean` and `variance` arguments during layer construction. A `Normalization` layer should always either be adapted over a dataset or passed `mean` and `variance`.\
\
During `adapt()`, the layer will compute a `mean` and `variance` separately for each position in each axis specified by the `axis` argument. To calculate a single `mean` and `variance` over the input data, simply pass `axis=None` to the layer.\
\
|     |     |\
| --- | --- |\
| Arg |     |\
| `data` | The data to train on. It can be passed as a NumPy array, a backend-native eager tensor, a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, or an iterable of batches (e.g. a list of arrays or a generator yielding batches). If a dataset or iterable, _it must be batched_. Keras will assume that each element is a batch, and if that assumption doesn't hold, the mean and variance may be incorrectly computed. |\
\
### `convert_weight`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/data_layer.py#L153-L159)\
\
convert_weight(\
        weight\
    )\
\
Convert the weight if it is from the a different backend.\
\
### `finalize_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/normalization.py#L399-L408)\
\
finalize_state()\
\
### `from_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)\
\
@classmethod\
\
Creates an operation from its config.\
\
This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.\
\
if "dtype" in config and isinstance(config["dtype"], dict):\
        policy = dtype_policies.deserialize(config["dtype"])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `config` | A Python dictionary, typically the output of `get_config`. |\
\
|     |\
| --- |\
| Returns |     |\
| An operation instance. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.