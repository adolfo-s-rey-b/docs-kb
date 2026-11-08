[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/train#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/train#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/train#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.train Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/train#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/train#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/train#functions)
    

Public API for tf.\_api.v2.train namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/train/experimental)
 module: Public API for tf.\_api.v2.train.experimental namespace

Classes
-------

[`class BytesList`](https://www.tensorflow.org/api_docs/python/tf/train/BytesList)
: Used in [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 protos. Holds a list of byte-strings.

[`class Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
: Manages saving/restoring trackable values to disk.

[`class CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
: Manages multiple checkpoints by keeping some and deleting unneeded ones.

[`class CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)
: Options for constructing a Checkpoint.

[`class CheckpointView`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointView)
: Gathers and serializes a checkpoint view.

[`class ClusterDef`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterDef)
: A ProtocolMessage

[`class ClusterSpec`](https://www.tensorflow.org/api_docs/python/tf/train/ClusterSpec)
: Represents a cluster as a set of "tasks", organized into "jobs".

[`class Coordinator`](https://www.tensorflow.org/api_docs/python/tf/train/Coordinator)
: A coordinator for threads.

[`class Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
: An `Example` is a standard proto storing data for training and inference.

[`class ExponentialMovingAverage`](https://www.tensorflow.org/api_docs/python/tf/train/ExponentialMovingAverage)
: Maintains moving averages of variables by employing an exponential decay.

[`class Feature`](https://www.tensorflow.org/api_docs/python/tf/train/Feature)
: Used in [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 protos. Contains a list of values.

[`class FeatureList`](https://www.tensorflow.org/api_docs/python/tf/train/FeatureList)
: Mainly used as part of a [`tf.train.SequenceExample`](https://www.tensorflow.org/api_docs/python/tf/train/SequenceExample)
.

[`class FeatureLists`](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists)
: Mainly used as part of a [`tf.train.SequenceExample`](https://www.tensorflow.org/api_docs/python/tf/train/SequenceExample)
.

[`class Features`](https://www.tensorflow.org/api_docs/python/tf/train/Features)
: Used in [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 protos. Contains the mapping from keys to `Feature`.

[`class FloatList`](https://www.tensorflow.org/api_docs/python/tf/train/FloatList)
: Used in [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 protos. Holds a list of floats.

[`class Int64List`](https://www.tensorflow.org/api_docs/python/tf/train/Int64List)
: Used in [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example)
 protos. Holds a list of Int64s.

[`class JobDef`](https://www.tensorflow.org/api_docs/python/tf/train/JobDef)
: A ProtocolMessage

[`class SequenceExample`](https://www.tensorflow.org/api_docs/python/tf/train/SequenceExample)
: A `SequenceExample` represents a sequence of features and some context.

[`class ServerDef`](https://www.tensorflow.org/api_docs/python/tf/train/ServerDef)
: A ProtocolMessage

[`class TrackableView`](https://www.tensorflow.org/api_docs/python/tf/train/TrackableView)
: Gathers and serializes a trackable view.

Functions
---------

[`checkpoints_iterator(...)`](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator)
: Continuously yield new checkpoint files as they appear.

[`get_checkpoint_state(...)`](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state)
: Returns CheckpointState proto from the "checkpoint" file.

[`latest_checkpoint(...)`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)
: Finds the filename of latest saved checkpoint file.

[`list_variables(...)`](https://www.tensorflow.org/api_docs/python/tf/train/list_variables)
: Lists the checkpoint keys and shapes of variables in a checkpoint.

[`load_checkpoint(...)`](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint)
: Returns `CheckpointReader` for checkpoint found in `ckpt_dir_or_file`.

[`load_variable(...)`](https://www.tensorflow.org/api_docs/python/tf/train/load_variable)
: Returns the tensor value of the given variable in the checkpoint.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.