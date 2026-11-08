[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#methods)
    *   [export\_best\_eval\_metric](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#export_best_eval_metric)
        
    *   [maybe\_export\_checkpoint](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#maybe_export_checkpoint)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.train\_utils.BestCheckpointExporter Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#methods)
    *   [export\_best\_eval\_metric](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#export_best_eval_metric)
        
    *   [maybe\_export\_checkpoint](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter#maybe_export_checkpoint)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L133-L241)

Keeps track of the best result, and saves its checkpoint.

tfm.core.train_utils.BestCheckpointExporter(
        export_dir: str, metric_name: str, metric_comp: str
    )

Orbit will support an API for checkpoint exporter. This class will be used together with orbit once this functionality is ready.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `export_dir` | The directory that will contain exported checkpoints. |
| `metric_name` | Indicates which metric to look at, when determining which result is better. If eval\_logs being passed to maybe\_export\_checkpoint is a nested dictionary, use `\|` as a seperator for different layers. |
| `metric_comp` | Indicates how to compare results. Either `lower` or `higher`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `best_ckpt_logs` |     |
| `best_ckpt_logs_path` |     |
| `best_ckpt_path` | Returns the best ckpt path or None if there is no ckpt yet. |

Methods
-------

### `export_best_eval_metric`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L216-L228)

export_best_eval_metric(
        eval_logs, global_step
    )

Export evaluation results of the best checkpoint into a json file.

### `maybe_export_checkpoint`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L173-L185)

maybe_export_checkpoint(
        checkpoint, eval_logs, global_step, write_logs=True
    ) -> bool

Compare eval\_logs with past eval\_logs and export checkpoint if better.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.