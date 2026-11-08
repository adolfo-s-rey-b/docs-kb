[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FDiscretization%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#used-in-the-notebooks_1)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#input-shape_1)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#output-shape_1)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#methods_2)
    *   [adapt](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#adapt)
        
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#convert_weight)
        
    *   [finalize\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#finalize_state)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#from_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#reset_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#update_state)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Discretization Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#used-in-the-notebooks_1)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#input-shape_1)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#output-shape_1)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#methods_2)
    *   [adapt](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#adapt)
        
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#convert_weight)
        
    *   [finalize\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#finalize_state)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#from_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#reset_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Discretization?version=stable#update_state)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/discretization.py#L11-L308)

A preprocessing layer which buckets continuous features by ranges.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Discretization(
        bin_boundaries=None,
        num_bins=None,
        epsilon=0.01,
        output_mode='int',
        sparse=False,
        dtype=None,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns) | *   [Using side features: feature preprocessing](https://www.tensorflow.org/recommenders/examples/featurization)<br>    <br>*   [Taking advantage of context features](https://www.tensorflow.org/recommenders/examples/context_features)<br>    <br>*   [Building deep retrieval models](https://www.tensorflow.org/recommenders/examples/deep_recommenders) |

This layer will place each element of its input data into one of several contiguous ranges and output an integer index indicating which range each element was placed in.

|     |
| --- |
| Input shape<br>----------- |     |
| Any array of dimension 2 or higher. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| Same as input shape. |     |

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `bin_boundaries` | A list of bin boundaries. The leftmost and rightmost bins will always extend to `-inf` and `inf`, so `bin_boundaries=[0., 1., 2.]` generates bins `(-inf, 0.)`, `[0., 1.)`, `[1., 2.)`, and `[2., +inf)`. If this option is set, `adapt()` should not be called. |\
| `num_bins` | The integer number of bins to compute. If this option is set, `bin_boundaries` should not be set and `adapt()` should be called to learn the bin boundaries. |\
| `epsilon` | Error tolerance, typically a small fraction close to zero (e.g. 0.01). Higher values of epsilon increase the quantile approximation, and hence result in more unequal buckets, but could improve performance and resource consumption. |\
| `output_mode` | Specification for the output of the layer. Values can be `"int"`, `"one_hot"`, `"multi_hot"`, or `"count"` configuring the layer as follows:<br><br>*   `"int"`: Return the discretized bin indices directly.<br>*   `"one_hot"`: Encodes each individual element in the input into an array the same size as `num_bins`, containing a 1 at the input's bin index. If the last dimension is size 1, will encode on that dimension. If the last dimension is not size 1, will append a new dimension for the encoded output.<br>*   `"multi_hot"`: Encodes each sample in the input into a single array the same size as `num_bins`, containing a 1 for each bin index index present in the sample. Treats the last dimension as the sample dimension, if input shape is `(..., sample_length)`, output shape will be `(..., num_tokens)`.<br>*   `"count"`: As `"multi_hot"`, but the int array contains a count of the number of times the bin index appeared in the sample. Defaults to `"int"`. |\
| `sparse` | Boolean. Only applicable to `"one_hot"`, `"multi_hot"`, and `"count"` output modes. Only supported with TensorFlow backend. If `True`, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`. |\
\
#### Examples:\
\
Discretize float values based on provided buckets.\
\
>>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]])\
    >>> layer = Discretization(bin_boundaries=[0., 1., 2.])\
    >>> layer(input)\
    array([[0, 2, 3, 1],\
           [1, 3, 2, 1]])\
\
Discretize float values based on a number of buckets to compute.\
\
>>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]])\
    >>> layer = Discretization(num_bins=4, epsilon=0.01)\
    >>> layer.adapt(input)\
    >>> layer(input)\
    array([[0, 2, 3, 2],\
           [1, 3, 3, 1]])\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
| `output_dtype` |     |\
\
Methods\
-------\
\
### `adapt`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/discretization.py#L159-L207)\
\
adapt(\
        data, steps=None\
    )\
\
Computes bin boundaries from quantiles in a input dataset.\
\
Calling `adapt()` on a `Discretization` layer is an alternative to passing in a `bin_boundaries` argument during construction. A `Discretization` layer should always be either adapted over a dataset or passed `bin_boundaries`.\
\
During `adapt()`, the layer will estimate the quantile boundaries of the input dataset. The number of quantiles can be controlled via the `num_bins` argument, and the error tolerance for quantile boundaries can be controlled via the `epsilon` argument.\
\
|     |     |\
| --- | --- |\
| Arguments |     |\
| `data` | The data to train on. It can be passed either as a batched [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, a Grain dataset, as a NumPy array, or as any iterable of batches (e.g. a list of arrays or a generator yielding batches). |\
| `steps` | Integer or `None`. Total number of steps (batches of samples) to process. If `data` is a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, and `steps` is `None`, `adapt()` will run until the input dataset is exhausted. When passing an infinitely repeating dataset, you must specify the `steps` argument. This argument is not supported with array inputs or list inputs. |\
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
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/discretization.py#L214-L219)\
\
finalize_state()\
\
### `from_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/discretization.py#L293-L308)\
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
### `reset_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/discretization.py#L221-L224)\
\
reset_state()\
\
### `update_state`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/discretization.py#L209-L212)\
\
update_state(\
        data\
    )\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.