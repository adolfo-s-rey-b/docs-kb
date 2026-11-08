[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/export_base/get_timestamped_export_dir#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.export\_base.get\_timestamped\_export\_dir Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/export_base.py#L152-L182)

Builds a path to a new subdirectory within the base directory.

tfm.core.export_base.get_timestamped_export_dir(
        export_dir_base
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `export_dir_base` | A string containing a directory to write the exported graph and checkpoints. |

|     |
| --- |
| Returns<br>------- |     |
| The full path of the new subdirectory (which is not actually created yet). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | if repeated attempts fail to obtain a unique timestamped directory name. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.