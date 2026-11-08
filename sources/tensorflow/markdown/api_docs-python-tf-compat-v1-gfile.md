[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.gfile Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile#functions)
    

Public API for tf.\_api.v2.gfile namespace

Classes
-------

[`class FastGFile`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/FastGFile)
: File I/O wrappers without thread locking.

[`class GFile`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile)
: File I/O wrappers without thread locking.

[`class Open`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile)
: File I/O wrappers without thread locking.

Functions
---------

[`Copy(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Copy)
: Copies data from `src` to `dst`.

[`DeleteRecursively(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/DeleteRecursively)
: Deletes everything under dirname recursively.

[`Exists(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Exists)
: Determines whether a path exists or not.

[`Glob(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Glob)
: Returns a list of files that match the given pattern(s).

[`IsDirectory(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/IsDirectory)
: Returns whether the path is a directory or not.

[`ListDirectory(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/ListDirectory)
: Returns a list of entries contained within a directory.

[`MakeDirs(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/MakeDirs)
: Creates a directory and all parent/intermediate directories.

[`MkDir(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/MkDir)
: Creates a directory with the name `dirname`.

[`Remove(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Remove)
: Deletes the file located at 'filename'.

[`Rename(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Rename)
: Rename or move a file / directory.

[`Stat(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Stat)
: Returns file statistics for a given path.

[`Walk(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/gfile/Walk)
: Recursive directory tree generator for directories.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.