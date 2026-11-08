[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/gfile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/gfile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/gfile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/gfile#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/gfile#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.io.gfile Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/gfile#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/io/gfile#functions)
    

Public API for tf.\_api.v2.io.gfile namespace

Classes
-------

[`class GFile`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/GFile)
: File I/O wrappers without thread locking.

Functions
---------

[`copy(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/copy)
: Copies data from `src` to `dst`.

[`exists(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/exists)
: Determines whether a path exists or not.

[`get_registered_schemes(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/get_registered_schemes)
: Returns the currently registered filesystem schemes.

[`glob(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/glob)
: Returns a list of files that match the given pattern(s).

[`isdir(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/isdir)
: Returns whether the path is a directory or not.

[`join(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/join)
: Join one or more path components intelligently.

[`listdir(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir)
: Returns a list of entries contained within a directory.

[`makedirs(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/makedirs)
: Creates a directory and all parent/intermediate directories.

[`mkdir(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/mkdir)
: Creates a directory with the name given by `path`.

[`remove(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/remove)
: Deletes the path located at 'path'.

[`rename(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/rename)
: Rename or move a file / directory.

[`rmtree(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/rmtree)
: Deletes everything under path recursively.

[`stat(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/stat)
: Returns file statistics for a given path.

[`walk(...)`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/walk)
: Recursive directory tree generator for directories.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.