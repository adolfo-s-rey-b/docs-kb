Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/onnx.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/onnx.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/onnx.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/onnx.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/onnx.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/onnx.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/onnx.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/onnx.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/onnx.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/onnx.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/onnx.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/onnx.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/onnx.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/onnx.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/onnx.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/onnx.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/onnx.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/onnx.html)
[v1.13](https://docs.pytorch.org/docs/1.13/onnx.html)
[v1.12](https://docs.pytorch.org/docs/1.12/onnx.html)
[v1.11](https://docs.pytorch.org/docs/1.11/onnx.html)
[v1.10](https://docs.pytorch.org/docs/1.10/onnx.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/onnx.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/onnx.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/onnx.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/onnx.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/onnx.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/onnx.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/onnx.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/onnx.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/onnx.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/onnx.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/onnx.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/onnx.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/onnx.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/onnx.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/onnx.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/onnx.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/onnx.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/onnx.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/onnx.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/onnx.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/onnx.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/onnx.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

torch.onnx[#](https://docs.pytorch.org/docs/2.15/onnx.html#torch-onnx "Link to this heading")

==============================================================================================

Created On: Jun 10, 2025 | Last Updated On: Sep 10, 2025

Overview[#](https://docs.pytorch.org/docs/2.15/onnx.html#overview "Link to this heading")

------------------------------------------------------------------------------------------

[Open Neural Network eXchange (ONNX)](https://onnx.ai/)
 is an open standard format for representing machine learning models. The `torch.onnx` module captures the computation graph from a native PyTorch [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 model and converts it into an [ONNX graph](https://github.com/onnx/onnx/blob/main/docs/IR.md)
.

The exported model can be consumed by any of the many [runtimes that support ONNX](https://onnx.ai/supported-tools.html#deployModel)
, including Microsoft’s [ONNX Runtime](https://www.onnxruntime.ai/)
.

Next example shows how to export a simple model.

import torch

class MyModel(torch.nn.Module):
    def \_\_init\_\_(self):
        super(MyModel, self).\_\_init\_\_()
        self.conv1 \= torch.nn.Conv2d(1, 128, 5)

    def forward(self, x):
        return torch.relu(self.conv1(x))

input\_tensor \= torch.rand((1, 1, 128, 128), dtype\=torch.float32)

model \= MyModel()

torch.onnx.export(
    model,                  \# model to export
    (input\_tensor,),        \# inputs of the model,
    "my\_model.onnx",        \# filename of the ONNX model
    input\_names\=\["input"\],  \# Rename inputs for the ONNX model
    dynamo\=True             \# True or False to select the exporter to use
)

Copy to clipboard

torch.export-based ONNX Exporter[#](https://docs.pytorch.org/docs/2.15/onnx.html#torch-export-based-onnx-exporter "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

_The torch.export-based ONNX exporter is the newest exporter for PyTorch 2.6 and newer_

[torch.export](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#torch-export)
 engine is leveraged to produce a traced graph representing only the Tensor computation of the function in an Ahead-of-Time (AOT) fashion. The resulting traced graph (1) produces normalized operators in the functional ATen operator set (as well as any user-specified custom operators), (2) has eliminated all Python control flow and data structures (with certain exceptions), and (3) records the set of shape constraints needed to show that this normalization and control-flow elimination is sound for future inputs, before it is finally translated into an ONNX graph.

[Learn more about the torch.export-based ONNX Exporter](https://docs.pytorch.org/docs/2.15/onnx_export.html)

Frequently Asked Questions[#](https://docs.pytorch.org/docs/2.15/onnx.html#frequently-asked-questions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

Q: I have exported my LLM model, but its input size seems to be fixed?

The tracer records the shapes of the example inputs. If the model should accept inputs of dynamic shapes, set `dynamic_shapes` when calling [`torch.onnx.export()`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.export "torch.onnx.export")
.

Q: How to export models containing loops?

See [torch.cond](https://docs.pytorch.org/docs/2.15/higher_order_ops/cond.html#cond)
.

Contributing / Developing[#](https://docs.pytorch.org/docs/2.15/onnx.html#contributing-developing "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The ONNX exporter is a community project and we welcome contributions. We follow the [PyTorch guidelines for contributions](https://github.com/pytorch/pytorch/blob/main/CONTRIBUTING.md)
, but you might also be interested in reading our [development wiki](https://github.com/pytorch/pytorch/wiki/PyTorch-ONNX-exporter)
.

torch.onnx APIs[#](https://docs.pytorch.org/docs/2.15/onnx.html#module-torch.onnx "Link to this heading")

----------------------------------------------------------------------------------------------------------

### Functions[#](https://docs.pytorch.org/docs/2.15/onnx.html#functions "Link to this heading")

torch.onnx.export(_model_, _args=()_, _f=None_, _\*_, _kwargs=None_, _verbose=None_, _input\_names=None_, _output\_names=None_, _opset\_version=None_, _dynamo=True_, _external\_data=True_, _dynamic\_shapes=None_, _custom\_translation\_table=None_, _report=False_, _optimize=True_, _verify=False_, _profile=False_, _dump\_exported\_program=False_, _artifacts\_dir='.'_, _export\_params=True_, _keep\_initializers\_as\_inputs=False_, _dynamic\_axes=None_, _training=<TrainingMode.EVAL: 0>_, _operator\_export\_type=<OperatorExportTypes.ONNX: 0>_, _do\_constant\_folding=True_, _custom\_opsets=None_, _export\_modules\_as\_functions=False_, _autograd\_inlining=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/__init__.py#L65)

Exports a model into ONNX format.

Setting `dynamo=True` enables the new ONNX export logic which is based on [`torch.export.ExportedProgram`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.ExportedProgram "torch.export.ExportedProgram")
 and a more modern set of translation logic. This is the recommended and default way to export models to ONNX.

When `dynamo=True`:

The exporter tries the following strategies to get an ExportedProgram for conversion to ONNX.

1.  If the model is already an ExportedProgram, it will be used as-is.
    
2.  Use [`torch.export.export()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.export "torch.export.export")
     and set `strict=False`.
    
3.  Use [`torch.export.export()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.export "torch.export.export")
     and set `strict=True`.
    

Parameters:

*   **model** ([_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
     _|_ [_torch.export.ExportedProgram_](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.ExportedProgram "torch.export.ExportedProgram")
     _|_ _torch.jit.ScriptModule_ _|_ _torch.jit.ScriptFunction_) – The model to be exported.
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[__Any__,_ _...__\]_) – Example positional inputs. Any non-Tensor arguments will be hard-coded into the exported model; any Tensor arguments will become inputs of the exported model, in the order they occur in the tuple.
    
*   **f** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_os.PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
     _|_ _None_) – Path to the output ONNX model file. E.g. “model.onnx”. This argument is kept for backward compatibility. It is recommended to leave unspecified (None) and use the returned [`torch.onnx.ONNXProgram`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "torch.onnx.ONNXProgram")
     to serialize the model to a file instead.
    
*   **kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]_ _|_ _None_) – Optional example keyword inputs.
    
*   **verbose** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _None_) – Whether to enable verbose logging.
    
*   **input\_names** (_Sequence__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – names to assign to the input nodes of the graph, in order.
    
*   **output\_names** (_Sequence__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – names to assign to the output nodes of the graph, in order. These are labels only and do not affect the order of outputs. If the model returns a dictionary, outputs are flattened in the dictionary’s iteration order regardless of the names specified here.
    
*   **opset\_version** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – The version of the [default (ai.onnx) opset](https://github.com/onnx/onnx/blob/master/docs/Operators.md)
     to target. You should set `opset_version` according to the supported opset versions of the runtime backend or compiler you want to run the exported model with. Leave as default (`None`) to use the recommended version, or refer to the ONNX operators documentation for more information.
    
*   **dynamo** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to export the model with `torch.export` ExportedProgram instead of TorchScript.
    
*   **external\_data** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to save the model weights as an external data file. This is required for models with large weights that exceed the ONNX file size limit (2GB). When False, the weights are saved in the ONNX file with the model architecture.
    
*   **dynamic\_shapes** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]_ _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[__Any__,_ _...__\]_ _|_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[__Any__\]_ _|_ _None_) – A dictionary or a tuple of dynamic shapes for the model inputs. Refer to [`torch.export.export()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.export "torch.export.export")
     for more details. This is only used (and preferred) when dynamo is True. Note that dynamic\_shapes is designed to be used when the model is exported with dynamo=True, while dynamic\_axes is used when dynamo=False.
    
*   **custom\_translation\_table** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[__Callable__,_ _Callable__\]_ _|_ _None_) – A dictionary of custom decompositions for operators in the model. The dictionary should have the callable target in the fx Node as the key (e.g. `torch.ops.aten.stft.default`), and the value should be a function that builds that graph using ONNX Script. This option is only valid when dynamo is True.
    
*   **report** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to generate a markdown report for the export process. This option is only valid when dynamo is True.
    
*   **optimize** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to optimize the exported model. This option is only valid when dynamo is True. Default is True.
    
*   **verify** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to verify the exported model using ONNX Runtime. This option is only valid when dynamo is True.
    
*   **profile** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to profile the export process. This option is only valid when dynamo is True.
    
*   **dump\_exported\_program** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to dump the [`torch.export.ExportedProgram`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.ExportedProgram "torch.export.ExportedProgram")
     to a file. This is useful for debugging the exporter. This option is only valid when dynamo is True.
    
*   **artifacts\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_os.PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    ) – The directory to save the debugging artifacts like the report and the serialized exported program. This option is only valid when dynamo is True.
    
*   **export\_params** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) –
    
    **When \`\`f\`\` is specified**: If false, parameters (weights) will not be exported.
    
    You can also leave it unspecified and use the returned [`torch.onnx.ONNXProgram`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "torch.onnx.ONNXProgram")
     to control how initializers are treated when serializing the model.
    
*   **keep\_initializers\_as\_inputs** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) –
    
    **When \`\`f\`\` is specified**: If True, all the initializers (typically corresponding to model weights) in the exported graph will also be added as inputs to the graph. If False, then initializers are not added as inputs to the graph, and only the user inputs are added as inputs.
    
    Set this to True if you intend to supply model weights at runtime. Set it to False if the weights are static to allow for better optimizations (e.g. constant folding) by backends/runtimes.
    
    You can also leave it unspecified and use the returned [`torch.onnx.ONNXProgram`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "torch.onnx.ONNXProgram")
     to control how initializers are treated when serializing the model.
    
*   **dynamic\_axes** (_Mapping__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Mapping__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__\]_ _|_ _Mapping__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Sequence__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__\]_ _|_ _None_) –
    
    Deprecated: Prefer specifying `dynamic_shapes` when `dynamo=True`.
    
    By default the exported model will have the shapes of all input and output tensors set to exactly match those given in `args`. To specify axes of tensors as dynamic (i.e. known only at run-time), set `dynamic_axes` to a dict with schema:
    
    *   KEY (str): an input or output name. Each name must also be provided in `input_names` or
        
        `output_names`.
        
    *   VALUE (dict or list): If a dict, keys are axis indices and values are axis names. If a
        
        list, each element is an axis index.
        
    
    For example:
    
    class SumModule(torch.nn.Module):
        def forward(self, x):
            return torch.sum(x, dim\=1)
    
    torch.onnx.export(
        SumModule(),
        (torch.ones(2, 2),),
        "onnx.pb",
        input\_names\=\["x"\],
        output\_names\=\["sum"\],
    )
    
    Copy to clipboard
    
    Produces:
    
    input {
      name: "x"
      ...
          shape {
            dim {
              dim\_value: 2  \# axis 0
            }
            dim {
              dim\_value: 2  \# axis 1
    ...
    output {
      name: "sum"
      ...
          shape {
            dim {
              dim\_value: 2  \# axis 0
    ...
    
    Copy to clipboard
    
    While:
    
    torch.onnx.export(
        SumModule(),
        (torch.ones(2, 2),),
        "onnx.pb",
        input\_names\=\["x"\],
        output\_names\=\["sum"\],
        dynamic\_axes\={
            \# dict value: manually named axes
            "x": {0: "my\_custom\_axis\_name"},
            \# list value: automatic names
            "sum": \[0\],
        },
    )
    
    Copy to clipboard
    
    Produces:
    
    input {
      name: "x"
      ...
          shape {
            dim {
              dim\_param: "my\_custom\_axis\_name"  \# axis 0
            }
            dim {
              dim\_value: 2  \# axis 1
    ...
    output {
      name: "sum"
      ...
          shape {
            dim {
              dim\_param: "sum\_dynamic\_axes\_1"  \# axis 0
    ...
    
    Copy to clipboard
    
*   **training** (_\_C\_onnx.TrainingMode_) – Deprecated option. Instead, set the training mode of the model before exporting.
    
*   **operator\_export\_type** (_\_C\_onnx.OperatorExportTypes_) – Deprecated option. Only ONNX is supported.
    
*   **do\_constant\_folding** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Deprecated option.
    
*   **custom\_opsets** (_Mapping__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_ _|_ _None_) – Deprecated option.
    
*   **export\_modules\_as\_functions** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _Collection__\[_[_type_](https://docs.python.org/3/builtins/functions.html#type "(in Python v3.15)")\
    _\[_[_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")\
    _\]__\]_) – Deprecated option.
    
*   **autograd\_inlining** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Deprecated option.
    

Returns:

[`torch.onnx.ONNXProgram`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "torch.onnx.ONNXProgram")
 if dynamo is True, otherwise None.

Return type:

[ONNXProgram](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "torch.onnx.ONNXProgram")
 | None

Changed in version 2.6: `training` is now deprecated. Instead, set the training mode of the model before exporting. `operator_export_type` is now deprecated. Only ONNX is supported. `do_constant_folding` is now deprecated. It is always enabled. `export_modules_as_functions` is now deprecated. `autograd_inlining` is now deprecated.

Changed in version 2.7: `optimize` is now True by default.

Changed in version 2.9: `dynamo` is now True by default.

Changed in version 2.11: `fallback` option has been removed.

torch.onnx.is\_in\_onnx\_export()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/__init__.py#L359)

Returns whether it is in the middle of ONNX export.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

### Classes[#](https://docs.pytorch.org/docs/2.15/onnx.html#classes "Link to this heading")

_class_ torch.onnx.ONNXProgram(_model_, _exported\_program_)

A class to represent an ONNX program that is callable with torch tensors.

Variables:

*   **model** – The ONNX model as an ONNX IR model object.
    
*   **exported\_program** – The exported program that produced the ONNX model.
    

_class_ torch.onnx.OnnxExporterError

Errors raised by the ONNX exporter. This is the base class for all exporter errors.

### Deprecated APIs[#](https://docs.pytorch.org/docs/2.15/onnx.html#deprecated-apis "Link to this heading")

Deprecated since version 2.6: These functions are deprecated and will be removed in a future version.

torch.onnx.register\_custom\_op\_symbolic(_symbolic\_name_, _symbolic\_fn_, _opset\_version_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/torchscript_exporter/utils.py#L1842)
[#](https://docs.pytorch.org/docs/2.15/onnx.html#torch.onnx.register_custom_op_symbolic "Link to this definition")

Registers a symbolic function for a custom operator.

When the user registers symbolic for custom/contrib ops, it is highly recommended to add shape inference for that operator via setType API, otherwise the exported graph may have incorrect shape inference in some extreme cases. An example of setType is test\_aten\_embedding\_2 in test\_operators.py.

See “Custom Operators” in the module documentation for an example usage.

Parameters:

*   **symbolic\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of the custom operator in “<domain>::<op>” format.
    
*   **symbolic\_fn** (_Callable_) – A function that takes in the ONNX graph and the input arguments to the current operator, and returns new operator nodes to add to the graph.
    
*   **opset\_version** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The ONNX opset version in which to register.
    

torch.onnx.unregister\_custom\_op\_symbolic(_symbolic\_name_, _opset\_version_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/torchscript_exporter/utils.py#L1872)
[#](https://docs.pytorch.org/docs/2.15/onnx.html#torch.onnx.unregister_custom_op_symbolic "Link to this definition")

Unregisters `symbolic_name`.

See “Custom Operators” in the module documentation for an example usage.

Parameters:

*   **symbolic\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of the custom operator in “<domain>::<op>” format.
    
*   **opset\_version** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The ONNX opset version in which to unregister.
    

torch.onnx.select\_model\_mode\_for\_export(_model_, _mode_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/torchscript_exporter/utils.py#L91)
[#](https://docs.pytorch.org/docs/2.15/onnx.html#torch.onnx.select_model_mode_for_export "Link to this definition")

A context manager to temporarily set the training mode of `model` to `mode`, resetting it when we exit the with-block.

Deprecated since version 2.7: Please set training mode before exporting the model.

Parameters:

*   **model** – Same type and meaning as `model` arg to [`export()`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.export "torch.onnx.export")
    .
    
*   **mode** (_TrainingMode_) – Same type and meaning as `training` arg to [`export()`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.export "torch.onnx.export")
    .
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/onnx.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/onnx.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |