Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/onnx_export.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/onnx_export.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/onnx_export.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/onnx_export.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/onnx_export.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/onnx_export.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/onnx_export.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/onnx_export.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/onnx_export.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/onnx_export.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/onnx_export.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/onnx_export.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/onnx_export.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/onnx_export.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/onnx_export.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/onnx_export.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/onnx_export.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/onnx_export.html)
[v1.13](https://docs.pytorch.org/docs/1.13/onnx_export.html)
[v1.12](https://docs.pytorch.org/docs/1.12/onnx_export.html)
[v1.11](https://docs.pytorch.org/docs/1.11/onnx_export.html)
[v1.10](https://docs.pytorch.org/docs/1.10/onnx_export.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/onnx_export.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/onnx_export.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/onnx_export.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/onnx_export.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/onnx_export.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/onnx_export.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/onnx_export.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/onnx_export.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/onnx_export.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/onnx_export.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/onnx_export.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/onnx_export.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/onnx_export.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/onnx_export.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/onnx_export.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/onnx_export.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/onnx_export.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/onnx_export.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/onnx_export.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/onnx_export.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/onnx_export.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/onnx_export.html)

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

torch.export-based ONNX Exporter[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch-export-based-onnx-exporter "Link to this heading")

=================================================================================================================================================

Created On: Jun 10, 2025 | Last Updated On: Jan 30, 2026

[Overview](https://docs.pytorch.org/docs/2.15/onnx_export.html#id1)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#overview "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

[torch.export](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#torch-export)
 engine is leveraged to produce a traced graph representing only the Tensor computation of the function in an Ahead-of-Time (AOT) fashion. The resulting traced graph (1) produces normalized operators in the functional ATen operator set (as well as any user-specified custom operators), (2) has eliminated all Python control flow and data structures (with certain exceptions), and (3) records the set of shape constraints needed to show that this normalization and control-flow elimination is sound for future inputs, before it is finally translated into an ONNX graph.

In addition, during the export process, memory usage is significantly reduced.

[Dependencies](https://docs.pytorch.org/docs/2.15/onnx_export.html#id2)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#dependencies "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The ONNX exporter depends on extra Python packages:

*   [ONNX](https://onnx.ai/)
    
*   [ONNX Script](https://microsoft.github.io/onnxscript)
    

They can be installed through [pip](https://pypi.org/project/pip/)
:

  pip install \--upgrade onnx onnxscript

Copy to clipboard

[onnxruntime](https://onnxruntime.ai/)
 can then be used to execute the model on a large variety of processors.

[A simple example](https://docs.pytorch.org/docs/2.15/onnx_export.html#id3)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#a-simple-example "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See below a demonstration of exporter API in action with a simple Multilayer Perceptron (MLP) as example:

import torch
import torch.nn as nn

class MLPModel(nn.Module):
  def \_\_init\_\_(self):
      super().\_\_init\_\_()
      self.fc0 \= nn.Linear(8, 8, bias\=True)
      self.fc1 \= nn.Linear(8, 4, bias\=True)
      self.fc2 \= nn.Linear(4, 2, bias\=True)
      self.fc3 \= nn.Linear(2, 2, bias\=True)
      self.fc\_combined \= nn.Linear(8 + 8 + 8, 8, bias\=True)  \# Combine all inputs

  def forward(self, tensor\_x: torch.Tensor, input\_dict: dict, input\_list: list):
      """
      Forward method that requires all inputs:
      - tensor\_x: A direct tensor input.
      - input\_dict: A dictionary containing the tensor under the key 'tensor\_x'.
      - input\_list: A list where the first element is the tensor.
      """
      \# Extract tensors from inputs
      dict\_tensor \= input\_dict\['tensor\_x'\]
      list\_tensor \= input\_list\[0\]

      \# Combine all inputs into a single tensor
      combined\_tensor \= torch.cat(\[tensor\_x, dict\_tensor, list\_tensor\], dim\=1)

      \# Process the combined tensor through the layers
      combined\_tensor \= self.fc\_combined(combined\_tensor)
      combined\_tensor \= torch.sigmoid(combined\_tensor)
      combined\_tensor \= self.fc0(combined\_tensor)
      combined\_tensor \= torch.sigmoid(combined\_tensor)
      combined\_tensor \= self.fc1(combined\_tensor)
      combined\_tensor \= torch.sigmoid(combined\_tensor)
      combined\_tensor \= self.fc2(combined\_tensor)
      combined\_tensor \= torch.sigmoid(combined\_tensor)
      output \= self.fc3(combined\_tensor)
      return output

model \= MLPModel()

\# Example inputs
tensor\_input \= torch.rand((97, 8), dtype\=torch.float32)
dict\_input \= {'tensor\_x': torch.rand((97, 8), dtype\=torch.float32)}
list\_input \= \[torch.rand((97, 8), dtype\=torch.float32)\]

\# The input\_names and output\_names are used to identify the inputs and outputs of the ONNX model
input\_names \= \['tensor\_input', 'tensor\_x', 'list\_input\_index\_0'\]
output\_names \= \['output'\]

\# Exporting the model with all required inputs
onnx\_program \= torch.onnx.export(model,(tensor\_input, dict\_input, list\_input), dynamic\_shapes\=({0: "batch\_size"},{"tensor\_x": {0: "batch\_size"}},\[{0: "batch\_size"}\]), input\_names\=input\_names, output\_names\=output\_names, dynamo\=True,)

\# Check the exported ONNX model is dynamic
assert onnx\_program.model.graph.inputs\[0\].shape \== ("batch\_size", 8)
assert onnx\_program.model.graph.inputs\[1\].shape \== ("batch\_size", 8)
assert onnx\_program.model.graph.inputs\[2\].shape \== ("batch\_size", 8)

Copy to clipboard

As the code above shows, all you need is to provide [`torch.onnx.export()`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.export "torch.onnx.export")
 with an instance of the model and its input. The exporter will then return an instance of [`torch.onnx.ONNXProgram`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "torch.onnx.ONNXProgram")
 that contains the exported ONNX graph along with extra information.

The in-memory model available through `onnx_program.model_proto` is an `onnx.ModelProto` object in compliance with the [ONNX IR spec](https://github.com/onnx/onnx/blob/main/docs/IR.md)
. The ONNX model may then be serialized into a [Protobuf file](https://protobuf.dev/)
 using the [`torch.onnx.ONNXProgram.save()`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.save "torch.onnx.ONNXProgram.save")
 API.

  onnx\_program.save("mlp.onnx")

Copy to clipboard

[Inspecting the ONNX model using GUI](https://docs.pytorch.org/docs/2.15/onnx_export.html#id4)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#inspecting-the-onnx-model-using-gui "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can view the exported model using [Netron](https://netron.app/)
.

[![MLP model as viewed using Netron](https://docs.pytorch.org/docs/2.15/_images/onnx_dynamo_mlp_model.png)](https://docs.pytorch.org/docs/2.15/_images/onnx_dynamo_mlp_model.png)

[When the conversion fails](https://docs.pytorch.org/docs/2.15/onnx_export.html#id5)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#when-the-conversion-fails "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Function [`torch.onnx.export()`](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.export "torch.onnx.export")
 should be called a second time with parameter `report=True`. A markdown report is generated to help the user to resolve the issue.

[Metadata](https://docs.pytorch.org/docs/2.15/onnx_export.html#id6)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#metadata "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

During ONNX export, each ONNX node is annotated with metadata that helps trace its origin and context from the original PyTorch model. This metadata is useful for debugging, model inspection, and understanding the mapping between PyTorch and ONNX graphs.

The following metadata fields are added to each ONNX node:

*   **namespace**
    
    A string representing the hierarchical namespace of the node, consisting of a stack trace of modules/methods.
    
    _Example:_ `__main__.SimpleAddModel/add: aten.add.Tensor`
    
*   **pkg.torch.onnx.class\_hierarchy**
    
    A list of class names representing the hierarchy of modules leading to this node.
    
    _Example:_ `['__main__.SimpleAddModel', 'aten.add.Tensor']`
    
*   **pkg.torch.onnx.fx\_node**
    
    The string representation of the original FX node, including its name, number of consumers, the targeted torch op, arguments, and keyword arguments.
    
    _Example:_ `%cat : [num_users=1] = call_function[target=torch.ops.aten.cat.default](args = ([%tensor_x, %input_dict_tensor_x, %input_list_0], 1), kwargs = {})`
    
*   **pkg.torch.onnx.name\_scopes**
    
    A list of name scopes (methods) representing the path to this node in the PyTorch model.
    
    _Example:_ `['', 'add']`
    
*   **pkg.torch.onnx.stack\_trace**
    
    The stack trace from the original code where this node was created, if available.
    
    _Example:_
    
    File "simpleadd.py", line 7, in forward
        return torch.add(x, y)
    
    Copy to clipboard
    

These metadata fields are stored in the metadata\_props attribute of each ONNX node and can be inspected using Netron or programmatically.

The overall ONNX graph has the following `metadata_props`:

*   **pkg.torch.export.ExportedProgram.graph\_signature**
    
    This property contains a string representation of the graph\_signature from the original PyTorch ExportedProgram. The graph signature describes the structure of the model’s inputs and outputs and how they map to the ONNX graph. The inputs are defined as `InputSpec` objects, which include the kind of input (e.g., `InputKind.PARAMETER` for parameters, `InputKind.USER_INPUT` for user-defined inputs), the argument name, the target (which can be a specific node in the model), and whether the input is persistent. The outputs are defined as `OutputSpec` objects, which specify the kind of output (e.g., `OutputKind.USER_OUTPUT`) and the argument name.
    
    To read more about the graph signature, please see the [torch.export](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html)
     for more information.
    
*   **pkg.torch.export.ExportedProgram.range\_constraints**
    
    This property contains a string representation of any range constraints that were present in the original PyTorch ExportedProgram. Range constraints specify valid ranges for symbolic shapes or values in the model, which can be important for models that use dynamic shapes or symbolic dimensions.
    
    _Example:_ `s0: VR[2, int_oo]`, which indicates that the size of the input tensor must be at least 2.
    
    To read more about range constraints, please see the [torch.export](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html)
     for more information.
    

Each input value in the ONNX graph may have the following metadata property:

*   **pkg.torch.export.graph\_signature.InputSpec.kind**
    
    The kind of input, as defined by PyTorch’s InputKind enum.
    
    _Example values:_
    
    *   “USER\_INPUT”: A user-provided input to the model.
        
    *   “PARAMETER”: A model parameter (e.g., weight).
        
    *   “BUFFER”: A model buffer (e.g., running mean in BatchNorm).
        
    *   “CONSTANT\_TENSOR”: A constant tensor argument.
        
    *   “CUSTOM\_OBJ”: A custom object input.
        
    *   “TOKEN”: A token input.
        
*   **pkg.torch.export.graph\_signature.InputSpec.persistent**
    
    Indicates whether the input is persistent (i.e., should be saved as part of the model’s state).
    
    _Example values:_
    
    *   “True”
        
    *   “False”
        

Each output value in the ONNX graph may have the following metadata property:

*   **pkg.torch.export.graph\_signature.OutputSpec.kind**
    
    The kind of input, as defined by PyTorch’s OutputKind enum.
    
    _Example values:_
    
    *   “USER\_OUTPUT”: A user-visible output.
        
    *   “LOSS\_OUTPUT”: A loss value output.
        
    *   “BUFFER\_MUTATION”: Indicates a buffer was mutated.
        
    *   “GRADIENT\_TO\_PARAMETER”: Gradient output for a parameter.
        
    *   “GRADIENT\_TO\_USER\_INPUT”: Gradient output for a user input.
        
    *   “USER\_INPUT\_MUTATION”: Indicates a user input was mutated.
        
    *   “TOKEN”: A token output.
        

Each initialized value, input, output has the following metadata:

*   **pkg.torch.onnx.original\_node\_name**
    
    The original name of the node in the PyTorch FX graph that produced this value in the case where the value was renamed. This helps trace initializers back to their source in the original model.
    
    _Example:_ `fc1.weight`
    

[API Reference](https://docs.pytorch.org/docs/2.15/onnx_export.html#id7)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#api-reference "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

torch.onnx.export(_model_, _args=()_, _f=None_, _\*_, _kwargs=None_, _verbose=None_, _input\_names=None_, _output\_names=None_, _opset\_version=None_, _dynamo=True_, _external\_data=True_, _dynamic\_shapes=None_, _custom\_translation\_table=None_, _report=False_, _optimize=True_, _verify=False_, _profile=False_, _dump\_exported\_program=False_, _artifacts\_dir='.'_, _export\_params=True_, _keep\_initializers\_as\_inputs=False_, _dynamic\_axes=None_, _training=<TrainingMode.EVAL: 0>_, _operator\_export\_type=<OperatorExportTypes.ONNX: 0>_, _do\_constant\_folding=True_, _custom\_opsets=None_, _export\_modules\_as\_functions=False_, _autograd\_inlining=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/__init__.py#L65)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.export "Link to this definition")

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

_class_ torch.onnx.ONNXProgram(_model_, _exported\_program_)[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "Link to this definition")

A class to represent an ONNX program that is callable with torch tensors.

Variables:

*   **model** – The ONNX model as an ONNX IR model object.
    
*   **exported\_program** – The exported program that produced the ONNX model.
    

apply\_weights(_state\_dict_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_onnx_program.py#L391)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.apply_weights "Link to this definition")

Apply the weights from the specified state dict to the ONNX model.

Use this method to replace FakeTensors or other weights.

Parameters:

**state\_dict** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
_\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_\]_) – The state dict containing the weights to apply to the ONNX model.

call\_reference(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_onnx_program.py#L263)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.call_reference "Link to this definition")

Run the ONNX model using the reference backend.

Return type:

[_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

compute\_values(_value\_names_, _args\=()_, _kwargs\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_onnx_program.py#L279)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.compute_values "Link to this definition")

Compute the values of the specified names in the ONNX model.

This method is used to compute the values of the specified names in the ONNX model. The values are returned as a dictionary mapping names to tensors.

Parameters:

**value\_names** ([_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
_\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_\]_) – The names of the values to compute.

Returns:

A dictionary mapping names to tensors.

Return type:

[_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

initialize\_inference\_session(_initializer=<function \_ort\_session\_initializer>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_onnx_program.py#L413)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.initialize_inference_session "Link to this definition")

Initialize the ONNX Runtime inference session.

Parameters:

**initializer** (_Callable__\[__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 _|_ [_bytes_](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
_\]__,_ _ort.InferenceSession__\]_) – The function to initialize the ONNX Runtime inference session with the specified model. By default, it uses the `_ort_session_initializer()` function.

_property_ model\_proto_: ModelProto_[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.model_proto "Link to this definition")

Return the ONNX `ModelProto` object.

optimize()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_onnx_program.py#L316)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.optimize "Link to this definition")

Optimize the ONNX model.

This method optimizes the ONNX model by performing constant folding and eliminating redundancies in the graph. The optimization is done in-place.

release()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_onnx_program.py#L443)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.release "Link to this definition")

Release the inference session.

You may call this method to release the resources used by the inference session.

rename\_axes(_rename\_mapping_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_onnx_program.py#L456)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.rename_axes "Link to this definition")

Rename axes in a model according to the specified rename mapping.

Example:

batch \= onnx\_program.model.graph.inputs\[0\].shape\[0\]
seq\_len \= onnx\_program.model.graph.inputs\[0\].shape\[2\]
rename\_mapping \= {
    batch: "batch",
    seq\_len: "seq\_len",
}
onnx\_program.rename\_axes(rename\_mapping)

Copy to clipboard

Parameters:

**rename\_mapping** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
_\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 _|_ _SymbolicDim__,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_\]_) –

A dictionary mapping old axes to new axis names. Keys can be either:

*   String axis names (e.g., “s1”, “s2”)
    
*   SymbolicDim objects obtained from the model (e.g., onnx\_program.model.graph.inputs\[0\].shape\[0\])
    

Values must be strings representing the new axis names.

save(_destination_, _\*_, _include\_initializers\=True_, _keep\_initializers\_as\_inputs\=False_, _external\_data\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_onnx_program.py#L324)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram.save "Link to this definition")

Save the ONNX model to the specified destination.

When `external_data` is `True` or the model is larger than 2GB, the weights are saved as external data in a separate file.

Initializer (model weights) serialization behaviors:

*   `include_initializers=True`, `keep_initializers_as_inputs=False` (default): The initializers are included in the saved model.
    
*   `include_initializers=True`, `keep_initializers_as_inputs=True`: The initializers are included in the saved model and kept as model inputs. Choose this option if you want the ability to override the model weights during inference.
    
*   `include_initializers=False`, `keep_initializers_as_inputs=False`: The initializers are not included in the saved model and are not listed as model inputs. Choose this option if you want to attach the initializers to the ONNX model in a separate, post-processing, step.
    
*   `include_initializers=False`, `keep_initializers_as_inputs=True`: The initializers are not included in the saved model but are listed as model inputs. Choose this option if you want to supply the initializers during inference and want to minimize the size of the saved model.
    

Parameters:

*   **destination** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    ) – The path to save the ONNX model to.
    
*   **include\_initializers** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to include the initializers in the saved model.
    
*   **keep\_initializers\_as\_inputs** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to keep the initializers as inputs in the saved model. If True, the initializers are added as inputs to the model which means they can be overwritten. by providing the initializers as model inputs.
    
*   **external\_data** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _None_) – Whether to save the weights as external data in a separate file.
    

Raises:

[**TypeError**](https://docs.python.org/3/builtins/exceptions.html#TypeError "(in Python v3.15)")
 – If `external_data` is `True` and `destination` is not a file path.

_class_ torch.onnx.ExportableModule(_\*args_, _\*\*kwargs_)[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ExportableModule "Link to this definition")

Abstract interface for ONNX exportable modules.

Inherit from this class and implement the defined abstract methods to create a module that can be exported to ONNX format.

Example:

class Model(torch.nn.Module):
    def forward(self, x):
        return x \* 2

class MyExportableModule(torch.onnx.ExportableModule):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.model \= Model()

    def forward(self, x):
        return self.model(x)

    def example\_arguments(self):
        return (torch.randn(2, 3, 224, 224),), None

    def input\_names(self):
        return ("input",)

    def output\_names(self):
        return ("output",)

    def dynamic\_shapes(self):
        return ({0: "batch\_size"},)

exportable\_module \= MyExportableModule()
onnx\_program \= exportable\_module.to\_onnx()
\# The model can also be supplied directly to torch.onnx.export
onnx\_program \= torch.onnx.export(exportable\_module)

Copy to clipboard

dynamic\_shapes()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_exportable_module.py#L85)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ExportableModule.dynamic_shapes "Link to this definition")

Return dynamic shape specifications for the model’s inputs.

Override this method to specify which dimensions of the input tensors should be treated as dynamic during ONNX export. This allows the exported model to accept inputs with varying sizes along the specified dimensions.

Example:

def dynamic\_shapes(self):
    \# Specify batch dimension as dynamic for input named 'x'
    return {"x": {0: "batch\_size"}}

def dynamic\_shapes(self):
    \# Multiple dynamic dimensions
    return {
        "input": {0: "batch\_size", 2: "height", 3: "width"},
        "mask": {0: "batch\_size"},
    }

Copy to clipboard

Note

The default implementation returns None, indicating all dimensions are static.

Returns:

Dynamic shape specification compatible with `torch.export.export`. Return None if all input dimensions should be static. The format can be:

*   A dictionary mapping input names to dimension specifications
    
*   A tuple/list of dimension specifications corresponding to inputs
    
*   Any format accepted by the `dynamic_shapes` parameter of `torch.export.export`
    

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

_abstract_ example\_arguments()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_exportable_module.py#L55)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ExportableModule.example_arguments "Link to this definition")

Return example arguments for the model’s forward method.

This method must be implemented by subclasses to provide sample inputs that can be used for tracing, testing, and ONNX export. The returned arguments should be representative of the expected input shapes and types during inference.

Example:

def example\_arguments(self):
    \# For a model expecting a single tensor input
    return (torch.randn(1, 3, 224, 224),), None

def example\_arguments(self):
    \# For a model with multiple inputs and keyword arguments
    return (torch.randn(1, 3, 224, 224), torch.randn(1, 512)), {
        "temperature": 1.0
    }

Copy to clipboard

Returns:

*   A tuple of positional arguments to pass to the forward method
    
*   A dictionary of keyword arguments (or None if no kwargs are needed)
    

Return type:

A tuple containing

input\_names()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_exportable_module.py#L119)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ExportableModule.input_names "Link to this definition")

Return names for the model’s input tensors.

Override this method to provide custom names for the input tensors in the exported ONNX model. These names will be used as identifiers in the ONNX graph and can be useful for debugging and model inspection.

Example:

def input\_names(self):
    return \["image", "mask"\]

def input\_names(self):
    \# For a single input
    return \["input\_tensor"\]

Copy to clipboard

Note

The default implementation returns None, which results in auto-generated names.

Returns:

A sequence of strings representing input names, or None to use default names. The number of names should match the number of positional arguments in the forward method.

Return type:

Sequence\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\] | None

output\_names()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_exportable_module.py#L146)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ExportableModule.output_names "Link to this definition")

Return names for the model’s output tensors.

Override this method to provide custom names for the output tensors in the exported ONNX model. These names will be used as identifiers in the ONNX graph and can be useful for debugging and model inspection.

Example:

def output\_names(self):
    return \["logits", "probabilities"\]

def output\_names(self):
    \# For a single output
    return \["prediction"\]

Copy to clipboard

Note

The default implementation returns None, which results in auto-generated names.

Returns:

A sequence of strings representing output names, or None to use default names. The number of names should match the number of outputs from the forward method. For models returning multiple outputs, provide a name for each output.

Return type:

Sequence\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\] | None

to\_onnx(_\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_exportable_module.py#L173)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ExportableModule.to_onnx "Link to this definition")

Export the module to ONNX format.

This method provides a convenient wrapper around `torch.onnx.export` that automatically uses the example arguments, dynamic shapes, and input/output names defined by the module. Additional export options can be specified via keyword arguments.

See Also: `torch.onnx.export` for complete documentation of export options.

Parameters:

**\*\*kwargs** ([_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
) –

Additional keyword arguments to pass to `torch.onnx.export`. Common options include:

*   `opset_version` (int): The ONNX opset version to target
    
*   `optimize` (bool): Whether to apply optimizations to the exported model
    

Returns:

An ONNXProgram object containing the exported model and metadata.

Return type:

[_ONNXProgram_](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "torch.onnx.ONNXProgram")

torch.onnx.is\_in\_onnx\_export()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/__init__.py#L359)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.is_in_onnx_export "Link to this definition")

Returns whether it is in the middle of ONNX export.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

_class_ torch.onnx.OnnxExporterError[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.OnnxExporterError "Link to this definition")

Errors raised by the ONNX exporter. This is the base class for all exporter errors.

_class_ torch.onnx.InputObserver(_value\_if\_missing\=None_)[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.InputObserver "Link to this definition")

Steals forward method to collect inputs and outputs. This information is used to infer dynamic shapes and export arguments.

Parameters:

**value\_if\_missing** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
_\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 _|_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
_,_ _Any__\]_ _|_ _None_) – If an argument is missing, a default value will be taken in this dictionary, this is used when after the prefill step, an argument disappears (such as pixel\_values) and another one is added (such as past\_key\_values). The values are only to infer dynamic shapes and arguments, not to run the model.

Examples

\>>> input\_observer \= InputObserver()
\>>> with input\_observer(model):
\>>>     model(x1, y1)
\>>>     model(x2, y2)
\>>> ep \= torch.export.export(  \# or torch.onnx.export
\>>>     model,
\>>>     input\_observer.infer\_arguments(),
\>>>     dynamic\_shapes.input\_observer.infer\_dynamic\_shapes(),
\>>> )

Copy to clipboard

With LLM:

\>>> input\_observer \= InputObserver()
\>>> with input\_observer(model):
\>>>     model.generate(input\_ids)
\>>> ep \= torch.export.export(  \# or torch.onnx.export
\>>>     model,
\>>>     (),
\>>>     kwargs\=input\_observer.infer\_arguments(),
\>>>     dynamic\_shapes.input\_observer.infer\_dynamic\_shapes(),
\>>> )

Copy to clipboard

The last example considers an LLM taking images and text as inputs. The first call to the forward method which we try to export has pixel\_values but no past\_key\_values. The next calls do not have pixel\_values but past\_key\_values. The observer understands pixel\_values and past\_key\_values are needed but they may not be both specified at the same time. Since pixel\_values only appears in the first call, the observer cannot tell how to infer an empty tensor for this argument. That’s what the argument value\_if\_missing is for. The following example is more than a dummy example but shows how to use it with `transformers`.

from transformers import pipeline

model\_id \= "tiny-random/gemma-3"
pipe \= pipeline(
    "image-text-to-text",
    model\=model\_id,
    device\="cpu",
    trust\_remote\_code\=True,
    max\_new\_tokens\=3,
    dtype\=torch.float16,
)
messages \= \[\
    {\
        "role": "system",\
        "content": \[{"type": "text", "text": "You are a helpful assistant."}\],\
    },\
    {\
        "role": "user",\
        "content": \[\
            {\
                "type": "image",\
                "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG",\
            },\
            {"type": "text", "text": "What animal is on the candy?"},\
        \],\
    },\
\]
observer \= InputObserver(
    value\_if\_missing\=dict(
        pixel\_values\=torch.empty((0, 3, 896, 896), dtype\=torch.float16)
    )
)
with observer(pipe.model):
    pipe(text\=messages, max\_new\_tokens\=4)

Copy to clipboard

New in version 2.11.0.

check\_discrepancies(_onnx\_program_, _atol=0.0001_, _rtol=0.1_, _progress\_bar=False_, _initializer=<function \_ort\_session\_initializer>_, _skip\_none=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_input_observer.py#L1114)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.InputObserver.check_discrepancies "Link to this definition")

Computes the discrepancies between the saved inputs and outputs with the saved onnx model.

Parameters:

*   **onnx\_program** ([_torch.onnx.ONNXProgram_](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.ONNXProgram "torch.onnx.ONNXProgram")
    ) – Exported Model to verify.
    
*   **atol** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Absolute tolerance, recommended values, 1e-4 for float, 1e-2 for float16.
    
*   **rtol** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Relative tolerance.
    
*   **progress\_bar** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Shows a progress bar (requires tqdm).
    
*   **initializer** (_Callable__\[__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
     _|_ [_bytes_](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
    _\]__,_ _ort.InferenceSession__\]_) – The function called to initialize the ONNX Runtime inference session with the specified model. By default, it uses the \_ort\_session\_initializer function.
    
*   **skip\_none** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Does not check discrepancies when an output is None.
    

Returns:

A list of dictionaries, ready to be consumed by a dataframe.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\]\]

The function catches exceptions, it shows the error in the returned summary.

infer\_arguments(_index\_or\_args\_or\_kwargs\=None_, _flat\=False_, _as\_args\_kwargs\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_input_observer.py#L1035)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.InputObserver.infer_arguments "Link to this definition")

Infers arguments based on the collected tensors.

Parameters:

*   **index\_or\_args\_or\_kwargs** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_ _|_ [_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_ _|_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – If missing, the method selects one set of inputs among the available ones, usually the set of inputs containing with the highest number of tensors. It then replaces None values and missing tensors with empty tensors. If not missing, it can be an integer to fetch one of the stored set or some inputs.
    
*   **flat** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If True, it returns a flattened list of tensors, if False, it returns a tuple or a dictionary preserving the nested structures. The flat version is used internally. It produces a single list of tensors easier to process or modify rather than a nested structure holding the same tensors. The original structure can be restored with `torch.utils._pytree.tree_unflatten(flat_list, self.aligned_spec)`. This mechanism is used to replace None values by empty tensors.
    
*   **as\_args\_kwargs** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If True, the method always returns (args, kwargs), otherwise, it returns either a tuple (only args) or a dictionary (only kwargs) or raises an exception if it cannot do so.
    

Returns:

Inferred arguments, every optional tensor is replaced by an empty tensor.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | None\] | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, …\] | [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\] | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\] | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, …\], [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]\]

infer\_dynamic\_shapes(_set\_batch\_dimension\_for\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_input_observer.py#L1011)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.InputObserver.infer_dynamic_shapes "Link to this definition")

Infers dynamic shapes. Most of the time, models do support a batch dimension but this batch dimension has the same value for every input sample. Instead of running inference on new samples, argument set\_batch\_dimension\_for can be used to tell the first dimension is a dynamic dimension for a particular set of inputs referenced by their name (str) or their position (int).

Parameters:

**set\_batch\_dimension\_for** ([_set_](https://docs.python.org/3/builtins/stdtypes.html#set "(in Python v3.15)")
_\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_\]_ _|_ [_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 _|_ _None_) – A set of input identifiers (by position as `int` or by name as `str`) for which the first dimension should be treated as a dynamic batch dimension. If `None`, no dimensions are explicitly marked as dynamic.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\] | None, …\] | [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\] | None\]

num\_obs()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/_internal/exporter/_input_observer.py#L936)
[#](https://docs.pytorch.org/docs/2.15/onnx_export.html#torch.onnx.InputObserver.num_obs "Link to this definition")

Returns the number of stored set of inputs.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/onnx_export.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/onnx_export.md.txt)

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