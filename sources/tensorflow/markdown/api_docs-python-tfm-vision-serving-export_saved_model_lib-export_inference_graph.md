[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/serving/export_saved_model_lib/export_inference_graph#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/serving/export_saved_model_lib/export_inference_graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/serving/export_saved_model_lib/export_inference_graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/serving/export_saved_model_lib/export_inference_graph#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.serving.export\_saved\_model\_lib.export\_inference\_graph Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/serving/export_saved_model_lib/export_inference_graph#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/serving/export_saved_model_lib.py#L33-L216)

Exports inference graph for the model specified in the exp config.

tfm.vision.serving.export_saved_model_lib.export_inference_graph(
        input_type: str,
        batch_size: Optional[int],
        input_image_size: List[int],
        params: tfm.core.base_trainer.ExperimentConfig,
        checkpoint_path: (str | None),
        export_dir: str,
        num_channels: Optional[int] = 3,
        export_module: Optional[tfm.core.export_base.ExportModule] = None,
        export_checkpoint_subdir: Optional[str] = None,
        export_saved_model_subdir: Optional[str] = None,
        save_options: Optional[tf.saved_model.SaveOptions] = None,
        log_model_flops_and_params: bool = False,
        checkpoint: Optional[tf.train.Checkpoint] = None,
        input_name: Optional[str] = None,
        function_keys: Optional[Union[List[str], Dict[str, str]]] = None,
        add_tpu_function_alias: Optional[bool] = False
    )

Saved model is stored at export\_dir/saved\_model, checkpoint is saved at export\_dir/checkpoint, and params is saved at export\_dir/params.yaml.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_type` | One of `image_tensor`, `image_bytes`, `tf_example` or `tflite`. |
| `batch_size` | 'int', or None. |
| `input_image_size` | List or Tuple of height and width. |
| `params` | Experiment params. |
| `checkpoint_path` | Trained checkpoint path or directory. |
| `export_dir` | Export directory path. |
| `num_channels` | The number of input image channels. |
| `export_module` | Optional export module to be used instead of using params to create one. If None, the params will be used to create an export module. |
| `export_checkpoint_subdir` | Optional subdirectory under export\_dir to store checkpoint. |
| `export_saved_model_subdir` | Optional subdirectory under export\_dir to store saved model. |
| `save_options` | `SaveOptions` for [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)<br>. |
| `log_model_flops_and_params` | If True, writes model FLOPs to model\_flops.txt and model parameters to model\_params.txt. |
| `checkpoint` | An optional tf.train.Checkpoint. If provided, the export module will use it to read the weights. |
| `input_name` | The input tensor name, default at `None` which produces input tensor name `inputs`. |
| `function_keys` | a list of string keys to retrieve pre-defined serving signatures. The signaute keys will be set with defaults. If a dictionary is provided, the values will be used as signature keys. |
| `add_tpu_function_alias` | Whether to add TPU function alias so that it can be converted to a TPU compatible saved model later. Default is False. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.