Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/export.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/user_guide/torch_compiler/export.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/user_guide/torch_compiler/export.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/user_guide/torch_compiler/export.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/user_guide/torch_compiler/export.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/user_guide/torch_compiler/export.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/user_guide/torch_compiler/export.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/user_guide/torch_compiler/export.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/user_guide/torch_compiler/export.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/user_guide/torch_compiler/export.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/user_guide/torch_compiler/export.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/user_guide/torch_compiler/export.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/user_guide/torch_compiler/export.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/user_guide/torch_compiler/export.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/user_guide/torch_compiler/export.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/user_guide/torch_compiler/export.html)
[v1.13](https://docs.pytorch.org/docs/1.13/user_guide/torch_compiler/export.html)
[v1.12](https://docs.pytorch.org/docs/1.12/user_guide/torch_compiler/export.html)
[v1.11](https://docs.pytorch.org/docs/1.11/user_guide/torch_compiler/export.html)
[v1.10](https://docs.pytorch.org/docs/1.10/user_guide/torch_compiler/export.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/user_guide/torch_compiler/export.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/user_guide/torch_compiler/export.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/user_guide/torch_compiler/export.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/user_guide/torch_compiler/export.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/user_guide/torch_compiler/export.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/user_guide/torch_compiler/export.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/user_guide/torch_compiler/export.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/user_guide/torch_compiler/export.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/user_guide/torch_compiler/export.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/user_guide/torch_compiler/export.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/user_guide/torch_compiler/export.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/user_guide/torch_compiler/export.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/user_guide/torch_compiler/export.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/user_guide/torch_compiler/export.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/user_guide/torch_compiler/export.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/user_guide/torch_compiler/export.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/user_guide/torch_compiler/export.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/user_guide/torch_compiler/export.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/user_guide/torch_compiler/export.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/user_guide/torch_compiler/export.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/user_guide/torch_compiler/export.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/user_guide/torch_compiler/export.html)

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

torch.export[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#torch-export "Link to this heading")

==============================================================================================================================

Created On: Jun 12, 2025 | Last Updated On: Feb 14, 2026

Overview[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#overview "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

[`torch.export.export()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.export "torch.export.export")
 takes a [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 and produces a traced graph representing only the Tensor computation of the function in an Ahead-of-Time (AOT) fashion, which can subsequently be executed with different inputs or serialized.

import torch
from torch.export import export, ExportedProgram

class Mod(torch.nn.Module):
    def forward(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        a = torch.sin(x)
        b = torch.cos(y)
        return a + b

example\_args = (torch.randn(10, 10), torch.randn(10, 10))

exported\_program: ExportedProgram = export(Mod(), args=example\_args)
print(exported\_program)

Copy to clipboard

`torch.export` produces a clean intermediate representation (IR) with the following invariants. More specifications about the IR can be found [here](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/ir_spec.html#export-ir-spec)
.

*   **Soundness**: It is guaranteed to be a sound representation of the original program, and maintains the same calling conventions of the original program.
    
*   **Normalized**: There are no Python semantics within the graph. Submodules from the original programs are inlined to form one fully flattened computational graph.
    
*   **Graph properties**: By default, the graph may contain both functional and non-functional operators (including mutations). To obtain a purely functional graph, use `run_decompositions()` which removes mutations and aliasing.
    
*   **Metadata**: The graph contains metadata captured during tracing, such as a stacktrace from user’s code.
    

Under the hood, `torch.export` leverages the following latest technologies:

*   **TorchDynamo (torch.\_dynamo)** is an internal API that uses a CPython feature called the Frame Evaluation API to safely trace PyTorch graphs. This provides a massively improved graph capturing experience, with much fewer rewrites needed in order to fully trace the PyTorch code.
    
*   **AOT Autograd** ensures the graph is decomposed/lowered to the ATen operator set. When using `run_decompositions()`, it can also provide functionalization.
    
*   **Torch FX (torch.fx)** is the underlying representation of the graph, allowing flexible Python-based transformations.
    

### Existing frameworks[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#existing-frameworks "Link to this heading")

[`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
 also utilizes the same PT2 stack as `torch.export`, but is slightly different:

*   **JIT vs. AOT**: [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
     is a JIT compiler whereas which is not intended to be used to produce compiled artifacts outside of deployment.
    
*   **Partial vs. Full Graph Capture**: When [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
     runs into an untraceable part of a model, it will “graph break” and fall back to running the program in the eager Python runtime. In comparison, `torch.export` aims to get a full graph representation of a PyTorch model, so it will error out when something untraceable is reached. Since `torch.export` produces a full graph disjoint from any Python features or runtime, this graph can then be saved, loaded, and run in different environments and languages.
    
*   **Usability tradeoff**: Since [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
     is able to fallback to the Python runtime whenever it reaches something untraceable, it is a lot more flexible. `torch.export` will instead require users to provide more information or rewrite their code to make it traceable.
    

Compared to [`torch.fx.symbolic_trace()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.symbolic_trace "torch.fx.symbolic_trace")
, `torch.export` traces using TorchDynamo which operates at the Python bytecode level, giving it the ability to trace arbitrary Python constructs not limited by what Python operator overloading supports. Additionally, `torch.export` keeps fine-grained track of tensor metadata, so that conditionals on things like tensor shapes do not fail tracing. In general, `torch.export` is expected to work on more user programs, and produce lower-level graphs (at the `torch.ops.aten` operator level). Note that users can still use [`torch.fx.symbolic_trace()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.symbolic_trace "torch.fx.symbolic_trace")
 as a preprocessing step before `torch.export`.

Compared to `torch.jit.script()`, `torch.export` does not capture Python control flow or data structures, unless using explicit [control flow operators](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html#higher-order-ops)
, but it supports more Python language features due to its comprehensive coverage over Python bytecodes. The resulting graphs are simpler and only have straight line control flow, except for explicit control flow operators.

Compared to `torch.jit.trace()`, `torch.export` is sound: it can trace code that performs integer computation on sizes and records all of the side-conditions necessary to ensure that a particular trace is valid for other inputs.

Exporting a PyTorch Model[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#exporting-a-pytorch-model "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

The main entrypoint is through [`torch.export.export()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.export "torch.export.export")
, which takes a [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 and sample inputs, and captures the computation graph into an [`torch.export.ExportedProgram`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.ExportedProgram "torch.export.ExportedProgram")
. An example:

import torch
from torch.export import export, ExportedProgram

# Simple module for demonstration
class M(torch.nn.Module):
    def \_\_init\_\_(self) -> None:
        super().\_\_init\_\_()
        self.conv = torch.nn.Conv2d(
            in\_channels=3, out\_channels=16, kernel\_size=3, padding=1
        )
        self.relu = torch.nn.ReLU()
        self.maxpool = torch.nn.MaxPool2d(kernel\_size=3)

    def forward(self, x: torch.Tensor, \*, constant=None) -> torch.Tensor:
        a = self.conv(x)
        a.add\_(constant)
        return self.maxpool(self.relu(a))

example\_args = (torch.randn(1, 3, 256, 256),)
example\_kwargs = {"constant": torch.ones(1, 16, 256, 256)}

exported\_program: ExportedProgram = export(
    M(), args=example\_args, kwargs=example\_kwargs
)
print(exported\_program)

# To run the exported program, we can use the \`module()\` method
print(exported\_program.module()(torch.randn(1, 3, 256, 256), constant=torch.ones(1, 16, 256, 256)))

Copy to clipboard

Inspecting the `ExportedProgram`, we can note the following:

*   The [`torch.fx.Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
     contains the computation graph of the original program, along with records of the original code for easy debugging.
    
*   The graph contains only `torch.ops.aten` operators found [here](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/native/native_functions.yaml)
     and custom operators.
    
*   The parameters (weight and bias to conv) are lifted as inputs to the graph, resulting in no `get_attr` nodes in the graph, which previously existed in the result of [`torch.fx.symbolic_trace()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.symbolic_trace "torch.fx.symbolic_trace")
    .
    
*   The `torch.export.ExportGraphSignature` models the input and output signature, along with specifying which inputs are parameters.
    
*   The resulting shape and dtype of tensors produced by each node in the graph is noted. For example, the `conv2d` node will result in a tensor of dtype `torch.float32` and shape (1, 16, 256, 256).
    

Expressing Dynamism[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#expressing-dynamism "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

By default `torch.export` will trace the program assuming all input shapes are **static**, and specializing the exported program to those dimensions. One consequence of this is that at runtime, the program won’t work on inputs with different shapes, even if they’re valid in eager mode.

An example:

import torch
import traceback as tb

class M(torch.nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()

        self.branch1 = torch.nn.Sequential(
            torch.nn.Linear(64, 32), torch.nn.ReLU()
        )
        self.branch2 = torch.nn.Sequential(
            torch.nn.Linear(128, 64), torch.nn.ReLU()
        )
        self.buffer = torch.ones(32)

    def forward(self, x1, x2):
        out1 = self.branch1(x1)
        out2 = self.branch2(x2)
        return (out1 + self.buffer, out2)

example\_args = (torch.randn(32, 64), torch.randn(32, 128))

ep = torch.export.export(M(), example\_args)
print(ep)

example\_args2 = (torch.randn(64, 64), torch.randn(64, 128))
try:
    ep.module()(\*example\_args2)  # fails
except Exception:
    tb.print\_exc()

Copy to clipboard

However, some dimensions, such as a batch dimension, can be dynamic and vary from run to run. Such dimensions must be specified by using the `torch.export.Dim()` API to create them and by passing them into [`torch.export.export()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.export "torch.export.export")
 through the `dynamic_shapes` argument.

import torch

class M(torch.nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()

        self.branch1 = torch.nn.Sequential(
            torch.nn.Linear(64, 32), torch.nn.ReLU()
        )
        self.branch2 = torch.nn.Sequential(
            torch.nn.Linear(128, 64), torch.nn.ReLU()
        )
        self.buffer = torch.ones(32)

    def forward(self, x1, x2):
        out1 = self.branch1(x1)
        out2 = self.branch2(x2)
        return (out1 + self.buffer, out2)

example\_args = (torch.randn(32, 64), torch.randn(32, 128))

# Create a dynamic batch size
batch = torch.export.Dim("batch")
# Specify that the first dimension of each input is that batch size
dynamic\_shapes = {"x1": {0: batch}, "x2": {0: batch}}

ep = torch.export.export(
    M(), args=example\_args, dynamic\_shapes=dynamic\_shapes
)
print(ep)

example\_args2 = (torch.randn(64, 64), torch.randn(64, 128))
ep.module()(\*example\_args2)  # success

Copy to clipboard

Some additional things to note:

*   Through the `torch.export.Dim()` API and the `dynamic_shapes` argument, we specified the first dimension of each input to be dynamic. Looking at the inputs `x1` and `x2`, they have a symbolic shape of `(s0, 64)` and `(s0, 128)`, instead of the `(32, 64)` and `(32, 128)` shaped tensors that we passed in as example inputs. `s0` is a symbol representing that this dimension can be a range of values.
    
*   `exported_program.range_constraints` describes the ranges of each symbol appearing in the graph. In this case, we see that `s0` has the range \[0, int\_oo\]. For technical reasons that are difficult to explain here, they are assumed to be not 0 or 1. This is not a bug, and does not necessarily mean that the exported program will not work for dimensions 0 or 1. See [The 0/1 Specialization Problem](https://docs.google.com/document/d/16VPOa3d-Liikf48teAOmxLc92rgvJdfosIy-yoT38Io/edit?fbclid=IwAR3HNwmmexcitV0pbZm_x1a4ykdXZ9th_eJWK-3hBtVgKnrkmemz6Pm5jRQ#heading=h.ez923tomjvyk)
     for an in-depth discussion of this topic.
    

In the example, we used `Dim("batch")` to create a dynamic dimension. This is the most explicit way to specify dynamism. We can also use `Dim.DYNAMIC` and `Dim.AUTO` to specify dynamism. We will go over both methods in the next section.

### Named Dims[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#named-dims "Link to this heading")

For every dimension specified with `Dim("name")`, we will allocate a symbolic shape. Specifying a `Dim` with the same name will result in the same symbol to be generated. This allows users to specify what symbols are allocated for each input dimension.

batch \= Dim("batch")
dynamic\_shapes \= {"x1": {0: dim}, "x2": {0: batch}}

Copy to clipboard

For each `Dim`, we can specify minimum and maximum values. We also allow specifying relations between `Dim`s in univariate linear expressions: `A * dim + B`. This allows users to specify more complex constraints like integer divisibility for dynamic dimensions. These features allow for users to place explicit restrictions on the dynamic behavior of the `ExportedProgram` produced.

dx \= Dim("dx", min\=4, max\=256)
dh \= Dim("dh", max\=512)
dynamic\_shapes \= {
    "x": (dx, None),
    "y": (2 \* dx, dh),
}

Copy to clipboard

However, `ConstraintViolationErrors` will be raised if the while tracing, we emit guards that conflict with the relations or static/dynamic specifications given. For example, in the above specification, the following is asserted:

*   `x.shape[0]` is to have range `[4, 256]`, and related to `y.shape[0]` by `y.shape[0] == 2 * x.shape[0]`.
    
*   `x.shape[1]` is static.
    
*   `y.shape[1]` has range `[0, 512]`, and is unrelated to any other dimension.
    

If any of these assertions are found to be incorrect while tracing (ex. `x.shape[0]` is static, or `y.shape[1]` has a smaller range, or `y.shape[0] != 2 * x.shape[0]`), then a `ConstraintViolationError` will be raised, and the user will need to change their `dynamic_shapes` specification.

### Dim Hints[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#dim-hints "Link to this heading")

Instead of explicitly specifying dynamism using `Dim("name")`, we can let `torch.export` infer the ranges and relationships of the dynamic values using `Dim.DYNAMIC`. This is also a more convenient way to specify dynamism when you don’t know specifically _how_ dynamic your dynamic values are.

dynamic\_shapes \= {
    "x": (Dim.DYNAMIC, None),
    "y": (Dim.DYNAMIC, Dim.DYNAMIC),
}

Copy to clipboard

We can also specify min/max values for `Dim.DYNAMIC`, which will serve as hints to export. But if while tracing export found the range to be different, it will automatically update the range without raising an error. We also cannot specify relationships between dynamic values. Instead, this will be inferred by export, and exposed to users through an inspection of assertions within the graph. In this method of specifying dynamism, `ConstraintViolationErrors` will **only** be raised if the specified value is inferred to be **static**.

An even more convenient way to specify dynamism is to use `Dim.AUTO`, which will behave like `Dim.DYNAMIC`, but will **not** raise an error if the dimension is inferred to be static. This is useful for when you have no idea what the dynamic values are, and want to export the program with a “best effort” dynamic approach.

### ShapesCollection[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#shapescollection "Link to this heading")

When specifying which inputs are dynamic via `dynamic_shapes`, we must specify the dynamism of every input. For example, given the following inputs:

args \= {"x": tensor\_x, "others": \[tensor\_y, tensor\_z\]}

Copy to clipboard

we would need to specify the dynamism of `tensor_x`, `tensor_y`, and `tensor_z` along with the dynamic shapes:

\# With named-Dims
dim \= torch.export.Dim(...)
dynamic\_shapes \= {"x": {0: dim, 1: dim + 1}, "others": \[{0: dim \* 2}, None\]}

torch.export(..., args, dynamic\_shapes\=dynamic\_shapes)

Copy to clipboard

However, this is particularly complicated as we need to specify the `dynamic_shapes` specification in the same nested input structure as the input arguments. Instead, an easier way to specify dynamic shapes is with the helper utility `torch.export.ShapesCollection`, where instead of specifying the dynamism of every single input, we can just assign directly which input dimensions are dynamic.

import torch

class M(torch.nn.Module):
    def forward(self, inp):
        x = inp\["x"\] \* 1
        y = inp\["others"\]\[0\] \* 2
        z = inp\["others"\]\[1\] \* 3
        return x, y, z

tensor\_x = torch.randn(3, 4, 8)
tensor\_y = torch.randn(6)
tensor\_z = torch.randn(6)
args = {"x": tensor\_x, "others": \[tensor\_y, tensor\_z\]}

dim = torch.export.Dim("dim")
sc = torch.export.ShapesCollection()
sc\[tensor\_x\] = (dim, dim + 1, 8)
sc\[tensor\_y\] = {0: dim \* 2}

print(sc.dynamic\_shapes(M(), (args,)))
ep = torch.export.export(M(), (args,), dynamic\_shapes=sc)
print(ep)

Copy to clipboard

### AdditionalInputs[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#additionalinputs "Link to this heading")

In the case where you don’t know how dynamic your inputs are, but you have an ample set of testing or profiling data that can provide a fair sense of representative inputs for a model, you can use `torch.export.AdditionalInputs` in place of `dynamic_shapes`. You can specify all the possible inputs used to trace the program, and `AdditionalInputs` will infer which inputs are dynamic based on which input shapes are changing.

Example:

import dataclasses
import torch
import torch.utils.\_pytree as pytree

@dataclasses.dataclass
class D:
    b: bool
    i: int
    f: float
    t: torch.Tensor

pytree.register\_dataclass(D)

class M(torch.nn.Module):
    def forward(self, d: D):
        return d.i + d.f + d.t

input1 = (D(True, 3, 3.0, torch.ones(3)),)
input2 = (D(True, 4, 3.0, torch.ones(4)),)
ai = torch.export.AdditionalInputs()
ai.add(input1)
ai.add(input2)

print(ai.dynamic\_shapes(M(), input1))
ep = torch.export.export(M(), input1, dynamic\_shapes=ai)
print(ep)

Copy to clipboard

Serialization[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#serialization "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

To save the `ExportedProgram`, users can use the [`torch.export.save()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.save "torch.export.save")
 and [`torch.export.load()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.load "torch.export.load")
 APIs. The resulting file is a zipfile with a specific structure. The details of the structure are defined in the [PT2 Archive Spec](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/pt2_archive.html#export-pt2-archive)
.

An example:

import torch

class MyModule(torch.nn.Module):
    def forward(self, x):
        return x + 10

exported\_program \= torch.export.export(MyModule(), (torch.randn(5),))

torch.export.save(exported\_program, 'exported\_program.pt2')
saved\_exported\_program \= torch.export.load('exported\_program.pt2')

Copy to clipboard

Export IR: Training vs Inference[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#export-ir-training-vs-inference "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The graph produced by `torch.export` returns a graph containing only [ATen operators](https://pytorch.org/cppdocs/#aten)
, which are the basic unit of computation in PyTorch. Export provides different IR levels based on your use case:

| IR Type | How to Obtain | Properties | Operator Count | Use Case |
| --- | --- | --- | --- | --- |
| Training IR | `torch.export.export()` (default) | May contain mutations | ~3000 | Training with autograd |
| Inference IR | `ep.run_decompositions(decomp_table={})` | Purely functional | ~2000 | Inference deployment |
| Core ATen IR | `ep.run_decompositions(decomp_table=None)` | Purely functional, highly decomposed | ~180 | Minimal backend support |

### Training IR (Default)[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#training-ir-default "Link to this heading")

By default, export produces a **Training IR** which contains all ATen operators, including both functional and non-functional (mutating) operators. A functional operator is one that does not contain any mutations or aliasing of the inputs, while non-functional operators may modify their inputs in-place. You can find a list of all ATen operators [here](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/native/native_functions.yaml)
 and you can inspect if an operator is functional by checking `op._schema.is_mutable`.

This Training IR, which may contain mutations, is designed for training use cases and can be used with eager PyTorch Autograd.

import torch

class M(torch.nn.Module):
    def \_\_init\_\_(self) -> None:
        super().\_\_init\_\_()
        self.conv = torch.nn.Conv2d(1, 3, 1, 1)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return (x,)

ep\_for\_training = torch.export.export(M(), (torch.randn(1, 1, 3, 3),))
print(ep\_for\_training.graph\_module.print\_readable(print\_output=False))

Copy to clipboard

### Inference IR (via run\_decompositions)[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#inference-ir-via-run-decompositions "Link to this heading")

To obtain an **Inference IR** suitable for deployment, use the `ExportedProgram.run_decompositions()` API. This method automatically:

1.  Functionalizes the graph (removes all mutations and converts them to functional equivalents)
    
2.  Optionally decomposes ATen operators based on the provided decomposition table
    

This produces a purely functional graph ideal for inference scenarios.

By specifying an empty decomposition table (`decomp_table={}`), you get just the functionalization without additional decompositions. This produces an Inference IR with ~2000 functional operators (compared to 3000+ in Training IR).

import torch

class M(torch.nn.Module):
    def \_\_init\_\_(self) -> None:
        super().\_\_init\_\_()
        self.conv = torch.nn.Conv2d(1, 3, 1, 1)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return (x,)

ep\_for\_training = torch.export.export(M(), (torch.randn(1, 1, 3, 3),))
with torch.no\_grad():
    ep\_for\_inference = ep\_for\_training.run\_decompositions(decomp\_table={})
print(ep\_for\_inference.graph\_module.print\_readable(print\_output=False))

Copy to clipboard

As we can see, the previously in-place operator, `torch.ops.aten.add_.default` has now been replaced with `torch.ops.aten.add.default`, a functional operator.

### Core ATen IR[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#core-aten-ir "Link to this heading")

We can further lower the Inference IR to the `Core ATen Operator Set <https://docs.pytorch.org/docs/main/user_guide/torch_compiler/torch.compiler_ir.html#core-aten-ir>`\_\_, which contains only ~180 operators. This is achieved by passing `decomp_table=None` (which uses the default decomposition table) to `run_decompositions()`. This IR is optimal for backends who want to minimize the number of operators they need to implement.

import torch

class M(torch.nn.Module):
    def \_\_init\_\_(self) -> None:
        super().\_\_init\_\_()
        self.conv = torch.nn.Conv2d(1, 3, 1, 1)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return (x,)

ep\_for\_training = torch.export.export(M(), (torch.randn(1, 1, 3, 3),))
with torch.no\_grad():
    core\_aten\_ir = ep\_for\_training.run\_decompositions(decomp\_table=None)
print(core\_aten\_ir.graph\_module.print\_readable(print\_output=False))

Copy to clipboard

We now see that `torch.ops.aten.conv2d.default` has been decomposed into `torch.ops.aten.convolution.default`. This is because `convolution` is a more “core” operator, as operations like `conv1d` and `conv2d` can be implemented using the same op.

We can also specify our own decomposition behaviors:

class M(torch.nn.Module):
    def \_\_init\_\_(self) -> None:
        super().\_\_init\_\_()
        self.conv = torch.nn.Conv2d(1, 3, 1, 1)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return (x,)

ep\_for\_training = torch.export.export(M(), (torch.randn(1, 1, 3, 3),))

my\_decomp\_table = torch.export.default\_decompositions()

def my\_awesome\_custom\_conv2d\_function(x, weight, bias, stride=\[1, 1\], padding=\[0, 0\], dilation=\[1, 1\], groups=1):
    return 2 \* torch.ops.aten.convolution(x, weight, bias, stride, padding, dilation, False, \[0, 0\], groups)

my\_decomp\_table\[torch.ops.aten.conv2d.default\] = my\_awesome\_custom\_conv2d\_function
my\_ep = ep\_for\_training.run\_decompositions(my\_decomp\_table)
print(my\_ep.graph\_module.print\_readable(print\_output=False))

Copy to clipboard

Notice that instead of `torch.ops.aten.conv2d.default` being decomposed into `torch.ops.aten.convolution.default`, it is now decomposed into `torch.ops.aten.convolution.default` and `torch.ops.aten.mul.Tensor`, which matches our custom decomposition rule.

Limitations of torch.export[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#limitations-of-torch-export "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

As `torch.export` is a one-shot process for capturing a computation graph from a PyTorch program, it might ultimately run into untraceable parts of programs as it is nearly impossible to support tracing all PyTorch and Python features. In the case of `torch.compile`, an unsupported operation will cause a “graph break” and the unsupported operation will be run with default Python evaluation. In contrast, `torch.export` will require users to provide additional information or rewrite parts of their code to make it traceable.

[Draft-export](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/draft_export.html#export-draft-export)
 is a great resource for listing out graphs breaks that will be encountered when tracing the program, along with additional debug information to solve those errors.

[ExportDB](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#torch-export-db)
 is also great resource for learning about the kinds of programs that are supported and unsupported, along with ways to rewrite programs to make them traceable.

### TorchDynamo unsupported[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#torchdynamo-unsupported "Link to this heading")

When using `torch.export` with `strict=True`, this will use TorchDynamo to evaluate the program at the Python bytecode level to trace the program into a graph. Compared to previous tracing frameworks, there will be significantly fewer rewrites required to make a program traceable, but there will still be some Python features that are unsupported. An option to get past dealing with this graph breaks is by using [non-strict export](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/programming_model.html#non-strict-export)
 through changing the `strict` flag to `strict=False`.

### Data/Shape-Dependent Control Flow[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#data-shape-dependent-control-flow "Link to this heading")

Graph breaks can also be encountered on data-dependent control flow (`if x.shape[0] > 2`) when shapes are not being specialized, as a tracing compiler cannot possibly deal with without generating code for a combinatorially exploding number of paths. In such cases, users will need to rewrite their code using special control flow operators. Currently, we support [higher order operators](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html#higher-order-ops)
 to express control flow patterns like conditionals, mapping, scanning, and looping.

You can also refer to this [tutorial](https://docs.pytorch.org/tutorials/intermediate/torch_export_tutorial.html#data-dependent-errors)
 for more ways of addressing data-dependent errors.

### Missing Fake/Meta Kernels for Operators[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#missing-fake-meta-kernels-for-operators "Link to this heading")

When tracing, a FakeTensor kernel (aka meta kernel) is required for all operators. This is used to reason about the input/output shapes for this operator.

Please see this [tutorial](https://docs.pytorch.org/tutorials/advanced/custom_ops_landing_page.html)
 for more details.

In the unfortunate case where your model uses an ATen operator that is does not have a FakeTensor kernel implementation yet, please file an issue.

Read More[#](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export.html#read-more "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Additional Links for Export Users

*   [torch.export API Reference](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html)
    
*   [torch.export Programming Model](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/programming_model.html)
    
*   [torch.export IR Specification](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/ir_spec.html)
    
*   [PT2 Archive Spec](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/pt2_archive.html)
    
*   [Draft Export](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/draft_export.html)
    
*   [Joint with descriptors](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/joint_with_descriptors.html)
    
*   [Control Flow Operators](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html)
    
*   [ExportDB](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html)
    
*   [AOTInductor: Ahead-Of-Time Compilation for Torch.Export-ed Models](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_aot_inductor.html)
    
*   [IRs](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_ir.html)
    

Deep Dive for PyTorch Developers

*   [Dynamic Shapes](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_dynamic_shapes.html)
    
*   [Fake tensor](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_fake_tensor.html)
    
*   [Writing Graph Transformations on ATen IR](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler_transformations.html)
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/user_guide/torch_compiler/export.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/user_guide/torch_compiler/export.md.txt)

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