[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/export_base#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/export_base)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/export_base?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/core/export_base#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/core/export_base#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/core/export_base#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.core.export\_base Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/core/export_base#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/core/export_base#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/core/export_base#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/export_base.py)

Base class for model export.

Classes
-------

[`class ExportModule`](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/ExportModule)
: Base Export Module.

Functions
---------

[`export(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/export)
: Exports to SavedModel format.

[`get_timestamped_export_dir(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/get_timestamped_export_dir)
: Builds a path to a new subdirectory within the base directory.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| MAX\_DIRECTORY\_CREATION\_ATTEMPTS | `10` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.