Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/distributed.pipelining.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/distributed.pipelining.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/distributed.pipelining.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/distributed.pipelining.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/distributed.pipelining.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/distributed.pipelining.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/distributed.pipelining.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/distributed.pipelining.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/distributed.pipelining.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/distributed.pipelining.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/distributed.pipelining.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/distributed.pipelining.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/distributed.pipelining.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/distributed.pipelining.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/distributed.pipelining.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/distributed.pipelining.html)
[v1.13](https://docs.pytorch.org/docs/1.13/distributed.pipelining.html)
[v1.12](https://docs.pytorch.org/docs/1.12/distributed.pipelining.html)
[v1.11](https://docs.pytorch.org/docs/1.11/distributed.pipelining.html)
[v1.10](https://docs.pytorch.org/docs/1.10/distributed.pipelining.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/distributed.pipelining.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/distributed.pipelining.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/distributed.pipelining.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/distributed.pipelining.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/distributed.pipelining.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/distributed.pipelining.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/distributed.pipelining.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/distributed.pipelining.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/distributed.pipelining.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/distributed.pipelining.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/distributed.pipelining.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/distributed.pipelining.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/distributed.pipelining.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/distributed.pipelining.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/distributed.pipelining.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/distributed.pipelining.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/distributed.pipelining.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/distributed.pipelining.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/distributed.pipelining.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/distributed.pipelining.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/distributed.pipelining.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/distributed.pipelining.html)

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

Pipeline Parallelism[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#pipeline-parallelism "Link to this heading")

====================================================================================================================================

Created On: Jun 16, 2025 | Last Updated On: Sep 22, 2026

Note

`torch.distributed.pipelining` is currently in alpha state and under development. API changes may be possible. It was migrated from the [PiPPy](https://github.com/pytorch/PiPPy)
 project.

Why Pipeline Parallel?[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#why-pipeline-parallel "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Pipeline Parallelism is one of the primitive forms of parallelism for deep learning. It allows the **execution** of a model to be partitioned such that multiple **micro-batches** can execute different parts of the model code concurrently. Pipeline parallelism can be an effective technique for:

*   large-scale training
    
*   bandwidth-limited clusters
    
*   large model inference
    

The above scenarios share a commonality that the computation per device cannot hide the communication of conventional parallelism, for example, the weight all-gather of FSDP.

What is `torch.distributed.pipelining`?[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#what-is-torch-distributed-pipelining "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

While promising for scaling, pipelining is often difficult to implement because it needs to **partition the execution** of a model in addition to model weights. The partitioning of execution often requires intrusive code changes to your model. Another aspect of complexity comes from **scheduling micro-batches in a distributed environment**, with **data flow dependency** considered.

The `pipelining` package provides a toolkit that does said things **automatically** which allows easy implementation of pipeline parallelism on **general** models.

It consists of two parts: a **splitting frontend** and a **distributed runtime**. The splitting frontend takes your model code as-is, splits it up into “model partitions”, and captures the data-flow relationship. The distributed runtime executes the pipeline stages on different devices in parallel, handling things like micro-batch splitting, scheduling, communication, and gradient propagation, etc.

Overall, the `pipelining` package provides the following features:

*   Splitting of model code based on simple specification.
    
*   Rich support for pipeline schedules, including GPipe, 1F1B, Interleaved 1F1B and Looped BFS, and providing the infrastructure for writing customized schedules.
    
*   First-class support for cross-host pipeline parallelism, as this is where PP is typically used (over slower interconnects).
    
*   Composability with other PyTorch parallel techniques such as data parallel (DDP, FSDP) or tensor parallel. The [TorchTitan](https://github.com/pytorch/torchtitan)
     project demonstrates a “3D parallel” application on the Llama model.
    

Step 1: build `PipelineStage`[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#step-1-build-pipelinestage "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Before we can use a `PipelineSchedule`, we need to create `PipelineStage` objects that wrap the part of the model running in that stage. The `PipelineStage` is responsible for allocating communication buffers and creating send/recv ops to communicate with its peers. It manages intermediate buffers e.g. for the outputs of forward that have not been consumed yet, and it provides a utility for running the backwards for the stage model.

A `PipelineStage` needs to know the input and output shapes for the stage model, so that it can correctly allocate communication buffers. The shapes must be static, e.g. at runtime the shapes can not change from step to step. A class `PipeliningShapeError` will be raised if runtime shapes do not match the expected shapes. When composing with other parallelisms or applying mixed precision, these techniques must be taken into account so the `PipelineStage` knows the correct shape (and dtype) for the output of the stage module at runtime.

Users may construct a `PipelineStage` instance directly, by passing in an `nn.Module` representing the portion of the model that should run on the stage. This may require changes to the original model code. See the example in [Option 1: splitting a model manually](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#option-1-manual)
.

Alternatively, the splitting frontend can use graph partitioning to split your model into a series of `nn.Module` automatically. This technique requires the model is traceable with `torch.Export`. Composability of the resulting `nn.Module` with other parallelism techniques is experimental, and may require some workarounds. Usage of this frontend may be more appealing if the user cannot easily change the model code. See [Option 2: splitting a model automatically](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#option-2-tracer)
 for more information.

Step 2: use `PipelineSchedule` for execution[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#step-2-use-pipelineschedule-for-execution "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can now attach the `PipelineStage` to a pipeline schedule, and run the schedule with input data. Here is a GPipe example:

from torch.distributed.pipelining import ScheduleGPipe

\# Create a schedule
schedule \= ScheduleGPipe(stage, n\_microbatches)

\# Input data (whole batch)
x \= torch.randn(batch\_size, in\_dim, device\=device)

\# Run the pipeline with input \`x\`
\# \`x\` will be divided into microbatches automatically
if rank \== 0:
    schedule.step(x)
else:
    output \= schedule.step()

Copy to clipboard

If your input pipeline already produces microbatches, pass them directly:

arg\_mbs \= \[(x0,), (x1,)\]
kwarg\_mbs \= \[{"mask": mask0}, {"mask": mask1}\]
target\_mbs \= \[target0, target1\]

schedule.step(
    arg\_mbs\=arg\_mbs,
    kwarg\_mbs\=kwarg\_mbs,
    target\_mbs\=target\_mbs,
)

Copy to clipboard

Note that the above code needs to be launched for each worker, thus we use a launcher service to launch multiple processes:

torchrun \--nproc\_per\_node\=2 example.py

Copy to clipboard

Options for Splitting a Model[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#options-for-splitting-a-model "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

### Option 1: splitting a model manually[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#option-1-splitting-a-model-manually "Link to this heading")

To directly construct a `PipelineStage`, the user is responsible for providing a single `nn.Module` instance that owns the relevant `nn.Parameters` and `nn.Buffers`, and defines a `forward()` method that executes the operations relevant for that stage. For example, a condensed version of the Transformer class defined in Torchtitan shows a pattern of building an easily partitionable model.

class Transformer(nn.Module):
    def \_\_init\_\_(self, model\_args: ModelArgs):
        super().\_\_init\_\_()

        self.tok\_embeddings \= nn.Embedding(...)

        \# Using a ModuleDict lets us delete layers without affecting names,
        \# ensuring checkpoints will correctly save and load.
        self.layers \= torch.nn.ModuleDict()
        for layer\_id in range(model\_args.n\_layers):
            self.layers\[str(layer\_id)\] \= TransformerBlock(...)

        self.output \= nn.Linear(...)

    def forward(self, tokens: torch.Tensor):
        \# Handling layers being 'None' at runtime enables easy pipeline splitting
        h \= self.tok\_embeddings(tokens) if self.tok\_embeddings else tokens

        for layer in self.layers.values():
            h \= layer(h, self.freqs\_cis)

        h \= self.norm(h) if self.norm else h
        output \= self.output(h).float() if self.output else h
        return output

Copy to clipboard

A model defined in this manner can be easily configured per stage by first initializing the whole model (using meta-device to avoid OOM errors), deleting undesired layers for that stage, and then creating a PipelineStage that wraps the model. For example:

with torch.device("meta"):
    assert num\_stages \== 2, "This is a simple 2-stage example"

    \# we construct the entire model, then delete the parts we do not need for this stage
    \# in practice, this can be done using a helper function that automatically divides up layers across stages.
    model \= Transformer()

    if stage\_index \== 0:
        \# prepare the first stage model
        del model.layers\["1"\]
        model.norm \= None
        model.output \= None

    elif stage\_index \== 1:
        \# prepare the second stage model
        model.tok\_embeddings \= None
        del model.layers\["0"\]

    from torch.distributed.pipelining import PipelineStage
    stage \= PipelineStage(
        model,
        stage\_index,
        num\_stages,
        device,
    )

Copy to clipboard

When composing with other Data or Model parallelism techniques, `output_args` may also be required, if the output shape/dtype of the model chunk will be affected.

### Option 2: splitting a model automatically[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#option-2-splitting-a-model-automatically "Link to this heading")

If you have a full model and do not want to spend time on modifying it into a sequence of “model partitions”, the `pipeline` API is here to help. Here is a brief example:

class Model(torch.nn.Module):
    def \_\_init\_\_(self) \-> None:
        super().\_\_init\_\_()
        self.emb \= torch.nn.Embedding(10, 3)
        self.layers \= torch.nn.ModuleList(
            Layer() for \_ in range(2)
        )
        self.lm \= LMHead()

    def forward(self, x: torch.Tensor) \-> torch.Tensor:
        x \= self.emb(x)
        for layer in self.layers:
            x \= layer(x)
        x \= self.lm(x)
        return x

Copy to clipboard

If we print the model, we can see multiple hierarchies, which makes it hard to split by hand:

Model(
  (emb): Embedding(10, 3)
  (layers): ModuleList(
    (0\-1): 2 x Layer(
      (lin): Linear(in\_features\=3, out\_features\=3, bias\=True)
    )
  )
  (lm): LMHead(
    (proj): Linear(in\_features\=3, out\_features\=3, bias\=True)
  )
)

Copy to clipboard

Let us see how the `pipeline` API works:

from torch.distributed.pipelining import pipeline, SplitPoint

\# An example micro-batch input
x \= torch.LongTensor(\[1, 2, 4, 5\])

pipe \= pipeline(
    module\=mod,
    mb\_args\=(x,),
    split\_spec\={
        "layers.1": SplitPoint.BEGINNING,
    }
)

Copy to clipboard

The `pipeline` API splits your model given a `split_spec`, where `SplitPoint.BEGINNING` stands for adding a split point _before_ execution of certain submodule in the `forward` function, and similarly, `SplitPoint.END` for split point _after_ such.

If we `print(pipe)`, we can see:

GraphModule(
  (submod\_0): GraphModule(
    (emb): InterpreterModule()
    (layers): Module(
      (0): InterpreterModule(
        (lin): InterpreterModule()
      )
    )
  )
  (submod\_1): GraphModule(
    (layers): Module(
      (1): InterpreterModule(
        (lin): InterpreterModule()
      )
    )
    (lm): InterpreterModule(
      (proj): InterpreterModule()
    )
  )
)

def forward(self, x):
    submod\_0 \= self.submod\_0(x);  x \= None
    submod\_1 \= self.submod\_1(submod\_0);  submod\_0 \= None
    return (submod\_1,)

Copy to clipboard

The “model partitions” are represented by submodules (`submod_0`, `submod_1`), each of which is reconstructed with original model operations, weights and hierarchies. In addition, a “root-level” `forward` function is reconstructed to capture the data flow between those partitions. Such data flow will be replayed by the pipeline runtime later, in a distributed fashion.

The `Pipe` object provides a method for retrieving the “model partitions”:

stage\_mod : nn.Module \= pipe.get\_stage\_module(stage\_idx)

Copy to clipboard

The returned `stage_mod` is a `nn.Module`, with which you can create an optimizer, save or load checkpoints, or apply other parallelisms.

`Pipe` also allows you to create a distributed stage runtime on a device given a `ProcessGroup`:

stage \= pipe.build\_stage(stage\_idx, device, group)

Copy to clipboard

Alternatively, if you would like to build the stage runtime later after some modification to the `stage_mod`, you can use a functional version of the `build_stage` API. For example:

from torch.distributed.pipelining import build\_stage
from torch.nn.parallel import DistributedDataParallel

dp\_mod \= DistributedDataParallel(stage\_mod)
info \= pipe.info()
stage \= build\_stage(dp\_mod, stage\_idx, info, device, group)

Copy to clipboard

Note

The `pipeline` frontend uses a tracer (`torch.export`) to capture your model into a single graph. If your model is not full-graph’able, you can use our manual frontend below.

Hugging Face Examples[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#hugging-face-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

In the [PiPPy](https://github.com/pytorch/PiPPy)
 repo where this package was original created, we kept examples based on unmodified Hugging Face models. See the [examples/huggingface](https://github.com/pytorch/PiPPy/tree/main/examples/huggingface)
 directory.

Examples include:

*   [GPT2](https://github.com/pytorch/PiPPy/tree/main/examples/huggingface/pippy_gpt2.py)
    
*   [Llama](https://github.com/pytorch/PiPPy/tree/main/examples/llama)
    

Technical Deep Dive[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#technical-deep-dive "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

### How does the `pipeline` API split a model?[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#how-does-the-pipeline-api-split-a-model "Link to this heading")

First, the `pipeline` API turns our model into a directed acyclic graph (DAG) by tracing the model. It traces the model using `torch.export` – a PyTorch 2 full-graph capturing tool.

Then, it groups together the **operations and parameters** needed by a stage into a reconstructed submodule: `submod_0`, `submod_1`, …

Different from conventional submodule access methods like `Module.children()`, the `pipeline` API does not only cut the module structure of your model, but also the **forward** function of your model.

This is necessary because model structure like `Module.children()` merely captures information during `Module.__init__()`, and does not capture any information about `Module.forward()`. Said differently, `Module.children()` lacks information about the following aspects key to pipelininig:

*   Execution order of child modules in `forward`
    
*   Activation flows between child modules
    
*   Whether there are any functional operators between child modules (for example, `relu` or `add` operations will not be captured by `Module.children()`).
    

The `pipeline` API, on the contrary, makes sure that the `forward` behavior is truly preserved. It also captures the activation flow between the partitions, helping the distributed runtime to make correct send/receive calls without human intervention.

Another flexibility of the `pipeline` API is that split points can be at arbitrary levels within your model hierarchy. In the split partitions, the original model hierarchy related to that partition will be reconstructed at no cost to you. At a result, fully-qualified names (FQNs) pointing to a submodule or parameter would be still valid, and services that relies on FQNs (such as FSDP, TP or checkpointing) can still run with your partitioned modules with almost zero code change.

Implementing Your Own Schedule[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#implementing-your-own-schedule "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

You can implement your own pipeline schedule by extending one of the following two classes:

*   `PipelineScheduleSingle`
    
*   `PipelineScheduleMulti`
    

`PipelineScheduleSingle` is for schedules that assigns _only one_ stage per rank. `PipelineScheduleMulti` is for schedules that assigns multiple stages per rank. All stages assigned to one rank must execute on one device; adjacent same-rank stages pass activations and gradients directly without device copies.

For example, `ScheduleGPipe` and `Schedule1F1B` are subclasses of `PipelineScheduleSingle`. Whereas, `ScheduleInterleaved1F1B`, `ScheduleLoopedBFS`, `ScheduleInterleavedZeroBubble`, and `ScheduleZBVZeroBubble` are subclasses of `PipelineScheduleMulti`.

### Accessing Stage Forward Information[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#accessing-stage-forward-information "Link to this heading")

A runtime surrounding a pipeline stage may need to select resources by the global logical stage and current microbatch. Physical pipeline rank is not a substitute for logical stage identity because one rank may own several stages in an interleaved schedule.

Register a context factory on the stage without changing the wrapped module’s forward signature:

from contextlib import contextmanager

from torch.distributed.pipelining import PipelineStageInfo

@contextmanager
def stage\_forward\_context(info: PipelineStageInfo):
    planner.enter(
        stage\_index\=info.stage\_index,
        microbatch\_index\=info.microbatch\_index,
        is\_metadata\_inference\=info.is\_metadata\_inference,
    )
    try:
        yield
    finally:
        planner.exit()

handle \= stage.register\_forward\_context(stage\_forward\_context)

Copy to clipboard

The factory is called around each built-in stage forward. Dynamic metadata inference uses microbatch zero and sets `is_metadata_inference=True`, allowing a consumer to distinguish the representative probe from real microbatch-zero execution. Static metadata setup does not execute the module and therefore does not enter the context.

Only one context can be registered on a stage at a time. Remove its handle before registering another context. Register before the first schedule step if the consumer must observe dynamic metadata inference.

The context executes outside a compiled or exported stage module, so it does not add graph inputs or change the module signature. CUDA graph capture runs the Python context while recording the stage computation, but replay does not re-enter Python; consumers must bind replay-stable state during capture. A custom schedule action receives this context only when it delegates execution to `stage.forward_one_chunk()`.

_class_ torch.distributed.pipelining.PipelineStageInfo(_\*_, _stage\_index_, _microbatch\_index_, _is\_metadata\_inference\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/stage.py#L73)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.PipelineStageInfo "Link to this definition")

Identify one pipeline-stage forward invocation.

This immutable value owns no tensors, process groups, schedule state, or storage. Future fields must have defaults so existing keyword-only construction remains source compatible.

Variables:

*   **stage\_index** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global logical pipeline-stage index. A physical pipeline rank may own several logical stages.
    
*   **microbatch\_index** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Microbatch index within the current pipeline step.
    
*   **is\_metadata\_inference** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether this invocation is the representative dynamic metadata-inference probe rather than real execution.
    

PipelineStage.register\_forward\_context(_context\_factory_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/stage.py#L267)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.PipelineStage.register_forward_context "Link to this definition")

Register a context manager around this stage’s forward computation.

The factory receives a [`PipelineStageInfo`](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.PipelineStageInfo "torch.distributed.pipelining.PipelineStageInfo")
 for every built-in runtime forward and dynamic metadata-inference probe. Static metadata setup does not execute the stage module and therefore does not invoke the factory. The returned handle removes the registration.

Only one context may be registered at a time. A custom schedule action receives the context only when it delegates execution to `forward_one_chunk()`. CUDA graph replay does not execute this Python callback; consumers must bind replay-stable state during capture.

Parameters:

**context\_factory** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
_\[__\[_[_PipelineStageInfo_](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.PipelineStageInfo "torch.distributed.pipelining.stage.PipelineStageInfo")\
_\]__,_ [_AbstractContextManager_](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager "(in Python v3.15)")\
_\[__None__\]__\]_) – Callable that returns a fresh context manager for each stage invocation. The context must not suppress exceptions raised by the stage module.

Returns:

A handle whose `remove()` method removes the registration.

Raises:

[**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
 – If a forward context is already registered.

Return type:

_RemovableHandle_

### Controlling FSDP Unshard Lookahead[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#controlling-fsdp-unshard-lookahead "Link to this heading")

Multi-stage runtime schedules lower a compute-only schedule into explicit FSDP `UNSHARD` and `RESHARD` actions. Two parameters control different parts of that lowering:

*   `max_active_stages` is the target parameter-residency window. It determines which stages remain unsharded and where `RESHARD` actions are inserted.
    
*   `unshard_lookahead` is the issue-distance window. It determines how many upcoming distinct logical stages may begin unsharding.
    

Separating these windows allows a schedule to issue fewer all-gathers early without evicting parameters sooner or adding another unshard/reshard cycle. An asynchronous unshard is still real GPU work:

pre-all-gather cast or quantization
  -> copy-in and packing
  -> all-gather
  -> copy-out
  -> post-all-gather quantization or layout preparation
  -> parameter ready

Copy to clipboard

`async_op=True` avoids a host-side wait, but these kernels, copies, collective traffic, allocations, and stream dependencies can still contend with the forward. Issuing the entire residency window at once can therefore put non-critical parameter preparation ahead of useful compute.

The `"auto"` policy estimates how much of this work fits into each rank’s pipeline startup bubble. Let a balanced stage forward take `F`, and let the composite critical-path cost of preparing one stage’s unsharded parameters be `U`. Ignoring pipeline transfer latency, rank `r` waits approximately `U + rF` before its first useful forward. This can complete approximately `floor((U + rF) / U)` unshards; issuing one more allows the next unshard to overlap that first forward. With the simplifying assumption `F = U = T`, the lookahead is `r + 2`, capped by `max_active_stages`.

For PP4 with `max_active_stages=4`, `"auto"` resolves to `(2, 3, 4, 4)`:

interval           | 0..T    | T..2T   | 2T..3T  | 3T..4T  | 4T..5T
-------------------+---------+----------+----------+----------+---------
rank 0 forward     | blocked | F(first) |          |          |
rank 0 preparation | U0      | U1       |          |          |  => 2
-------------------+---------+----------+----------+----------+---------
rank 1 forward     | blocked | blocked  | F(first) |          |
rank 1 preparation | U0      | U1       | U2       |          |  => 3
-------------------+---------+----------+----------+----------+---------
rank 2 forward     | blocked | blocked  | blocked  | F(first) |
rank 2 preparation | U0      | U1       | U2       | U3       |  => 4
-------------------+---------+----------+----------+----------+---------
rank 3 forward     | blocked | blocked  | blocked  | blocked  | F(first)
rank 3 preparation | U0      | U1       | U2       | U3       |  => 4

Copy to clipboard

The diagram is an analytical starting point, not an exact CUDA-stream model. `Uk` denotes preparation of the kth upcoming rank-local stage, not a global stage index. Vertically aligned preparation and forward cells are intended to overlap. Real stages may be unbalanced, unshard phases may overlap only partially, and network or memory-bandwidth contention may change the best distance. Choose a policy accordingly:

| Policy | Per-rank issue distance | Intended use |
| --- | --- | --- |
| `"full"` | `max_active_stages` | Compatibility default matching the original full-window behavior. |
| `"auto"` | `min(pp_rank + 2, max_active_stages)` | Deterministic startup-bubble estimate that avoids recipe-level tuning; not a universal optimum. |
| Tuple | The corresponding positive integer for each PP rank | Expert tuning for measured model, topology, and fabric behavior. |

A custom compute-only schedule may be combined with a tuple before lowering. For exact `UNSHARD` and communication placement, supply an already lowered `compute_comms` schedule; `unshard_lookahead` cannot retune actions that are already present.

An atomic compound action remains indivisible, so it may extend either window by up to the action’s number of stages minus one. Non-full policies can also move absolute P2P action positions because unshards consume lowering rounds. They do not change compute order, `RESHARD` placement, residency episodes, or collective counts. Applications should benchmark an explicit tuple when stage costs differ materially from the balanced model.

Logging[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#logging "Link to this heading")

----------------------------------------------------------------------------------------------------------

You can turn on additional logging using the `TORCH_LOGS` environment variable from [torch.\_logging](https://pytorch.org/docs/main/logging.html#module-torch._logging)
:

*   `TORCH_LOGS=+pp` will display `logging.DEBUG` messages and all levels above it.
    
*   `TORCH_LOGS=pp` will display `logging.INFO` messages and above.
    
*   `TORCH_LOGS=-pp` will display `logging.WARNING` messages and above.
    

API Reference[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#module-torch.distributed.pipelining "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

### Model Split APIs[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#model-split-apis "Link to this heading")

The following set of APIs transform your model into a pipeline representation.

_class_ torch.distributed.pipelining.SplitPoint(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/_IR.py#L1192)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.SplitPoint "Link to this definition")

Enum representing the points at which a split can occur in the execution of a submodule. :ivar BEGINNING: Represents adding a split point _before_ the execution of a certain submodule in the forward function. :ivar END: Represents adding a split point _after_ the execution of a certain submodule in the forward function.

torch.distributed.pipelining.pipeline(_module_, _mb\_args_, _mb\_kwargs\=None_, _split\_spec\=None_, _split\_policy\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/_IR.py#L1247)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.pipeline "Link to this definition")

Split a module based on a specification.

See Pipe for more details.

Parameters:

*   **module** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")
    ) – The module to be split.
    
*   **mb\_args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _,_ _...__\]_) – Example positional inputs, in micro-batch form.
    
*   **mb\_kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_ _|_ _None_) – Example keyword inputs, in micro-batch form. (default: None)
    
*   **split\_spec** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_SplitPoint_](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.SplitPoint "torch.distributed.pipelining._IR.SplitPoint")\
    _\]_ _|_ _None_) – A dictionary using submodule names as split marker. (default: None)
    
*   **split\_policy** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[_[_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
    _\]__,_ [_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
    _\]_ _|_ _None_) – The policy to use for splitting the module. (default: None)
    

Return type:

A pipeline representation of class Pipe.

_class_ torch.distributed.pipelining.Pipe(_split\_gm_, _num\_stages_, _has\_loss\_and\_backward_, _loss\_spec_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/_IR.py#L561)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.Pipe "Link to this definition")

torch.distributed.pipelining.pipe\_split()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/_IR.py#L363)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.pipe_split "Link to this definition")

pipe\_split is a special operator that is used to mark the boundary between stages in a module. It is used to split the module into stages. It is a no-op if your annotated module is run eagerly.

Example

\>>> def forward(self, x):
\>>>     x \= torch.mm(x, self.mm\_param)
\>>>     x \= torch.relu(x)
\>>>     pipe\_split()
\>>>     x \= self.lin(x)
\>>>     return x

Copy to clipboard

The above example will be split into two stages.

### Microbatch Utilities[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#module-torch.distributed.pipelining.microbatch "Link to this heading")

_class_ torch.distributed.pipelining.microbatch.TensorChunkSpec(_split\_dim_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/microbatch.py#L60)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.microbatch.TensorChunkSpec "Link to this definition")

Class used to specify chunking of inputs

torch.distributed.pipelining.microbatch.split\_args\_kwargs\_into\_chunks(_args_, _kwargs_, _chunks_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/microbatch.py#L378)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.microbatch.split_args_kwargs_into_chunks "Link to this definition")

Given a sequence of args and kwargs, split them into a number of chunks according to their respective chunking specs.

Parameters:

*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _,_ _...__\]_) – Tuple of args
    
*   **kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_ _|_ _None_) – Dict of kwargs
    
*   **chunks** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of chunks to split the args and kwargs into
    
*   **args\_chunk\_spec** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_TensorChunkSpec_](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.microbatch.TensorChunkSpec "torch.distributed.pipelining.microbatch.TensorChunkSpec")\
    _,_ _...__\]_ _|_ _None_) – chunking specs for args, in same shape as args
    
*   **kwargs\_chunk\_spec** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_TensorChunkSpec_](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.microbatch.TensorChunkSpec "torch.distributed.pipelining.microbatch.TensorChunkSpec")\
    _\]_ _|_ _None_) – chunking specs for kwargs, in same shape as kwargs
    

Returns:

List of sharded args kwargs\_split: List of sharded kwargs

Return type:

args\_split

torch.distributed.pipelining.microbatch.merge\_chunks(_chunks_, _chunk\_spec_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/microbatch.py#L493)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.microbatch.merge_chunks "Link to this definition")

Given a list of chunks, merge them into a single value according to the chunk spec.

Parameters:

*   **chunks** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_) – list of chunks
    
*   **chunk\_spec** – Chunking spec for the chunks
    

Returns:

Merged value

Return type:

value

### Pipeline Stages[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#module-torch.distributed.pipelining.stage "Link to this heading")

_class_ torch.distributed.pipelining.stage.PipelineStage(_submodule_, _stage\_index_, _num\_stages_, _device_, _input\_args\=None_, _output\_args\=None_, _output\_grads\=None_, _input\_grads\=None_, _group\=None_, _dw\_builder\=None_, _get\_mesh\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/stage.py#L1885)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.stage.PipelineStage "Link to this definition")

A pipeline stage for pipeline parallelism with sequential model partitioning.

Supports both **static** and **dynamic** metadata inference:

Static mode:

All of `input_args`, `output_args` (and `input_grads`/`output_grads` when DTensors are present) are provided at construction time.

Dynamic mode:

Metadata is inferred from the first microbatch at runtime; any statically provided args are used for validation only.

Parameters:

*   **submodule** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")
    ) – The `nn.Module` wrapped by this stage.
    
*   **stage\_index** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Zero-based stage ID.
    
*   **num\_stages** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Total number of stages in the pipeline.
    
*   **device** ([_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    ) – Device this stage runs on.
    
*   **input\_args** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _,_ _...__\]_ _|_ _None_) – Example input tensors (single tensor or tuple). Optional.
    
*   **output\_args** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _,_ _...__\]_ _|_ _None_) – Example output tensors. Optional.
    
*   **output\_grads** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
     _|_ _None__,_ _...__\]_ _|_ _None_) – Example output gradients (received from next stage). Optional.
    
*   **input\_grads** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
     _|_ _None__,_ _...__\]_ _|_ _None_) – Example input gradients (sent to previous stage). Optional.
    
*   **group** (_ProcessGroup_ _|_ _None_) – Process group for P2P communication. Defaults to the world process group.
    
*   **dw\_builder** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[__\]__,_ [_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
    _\[__\[__...__\]__,_ _None__\]__\]_ _|_ _None_) – Builder for deferred weight-update runners used by zero-bubble (F/I/W) schedules.
    
*   **get\_mesh** (_GetMeshCallback_ _|_ _None_) – GetMeshCallback used during dynamic DTensor inference. Ignored in fully static DTensor mode.
    

torch.distributed.pipelining.stage.build\_stage(_stage\_module_, _stage\_index_, _pipe\_info_, _device_, _group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/stage.py#L1855)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.stage.build_stage "Link to this definition")

Create a pipeline stage given a stage\_module to be wrapped by this stage and pipeline information.

Parameters:

*   **stage\_module** ([_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – the module to be wrapped by this stage
    
*   **stage\_index** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the index of this stage in the pipeline
    
*   **pipe\_info** (_PipeInfo_) – information about the pipeline, can be retrieved by pipe.info()
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    ) – the device to be used by this stage
    
*   **group** (_Optional__\[__dist.ProcessGroup__\]_) – the process group to be used by this stage
    

Returns:

a pipeline stage that can run with PipelineSchedules.

Return type:

\_PipelineStage

### Pipeline Schedules[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#pipeline-schedules "Link to this heading")

#### Activation-liveness analysis[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#activation-liveness-analysis "Link to this heading")

Pipeline runtimes and memory planners can use `analyze_pipeline_activation_liveness` to determine how many reusable logical slots are needed for activations retained from forward through backward. The analysis does not allocate tensors. It returns a `PipelineActivationLiveness` plan whose `slot_by_stage_and_microbatch[(stage_index, microbatch_index)]` values are slot IDs that a caller may map to buffers or arena regions.

An activation becomes live at its forward (`F`) action. Full backward (`B`) releases it. For schedules that separate input backward (`I`) from weight backward (`W`), `I` does not release the activation because `W` may still need the saved forward state; `W` releases it. Lifetimes include both endpoint positions, so actions grouped into the same compound schedule position overlap.

For example, consider two stages and two microbatches on one pipeline rank:

position:  0     1     2     3     4     5     6     7
action:   F0,0  F1,0  F0,1  B1,0  B0,0  F1,1  B1,1  B0,1

Copy to clipboard

With `granularity="stage_microbatch"`, the four activation lifetimes are `(0, 4)`, `(1, 3)`, `(2, 7)`, and `(5, 6)`; the final lifetime may reuse the first slot. With `granularity="microbatch"`, the selected stages for each microbatch share one conservative lifetime: `(0, 4)` for microbatch 0 and `(2, 7)` for microbatch 1. The latter mode is useful when a consumer manages all selected stages for one microbatch as one storage unit. Stage indices are global logical indices and commonly identify virtual stages hosted by the same pipeline rank.

torch.distributed.pipelining.schedules.analyze\_pipeline\_activation\_liveness(_schedule_, _\*_, _pp\_rank_, _stage\_indices_, _granularity_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L5027)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.analyze_pipeline_activation_liveness "Link to this definition")

Analyze activation lifetimes and assign reusable pipeline slots.

The analysis follows the finalized action sequence for `pp_rank`. A forward action starts the lifetime of activation state retained for backward. Full backward ends that lifetime; when input and weight backward are split, weight backward ends it. Input backward does not release the activation because weight backward may still consume it. Both interval endpoints are inclusive, including sub-actions in one compound schedule position.

This utility only computes liveness and logical slot IDs. It does not allocate tensors or prescribe a storage layout. Consumers can use the plan to reason about peak activation memory or map slots to stable buffers and arena regions.

Parameters:

*   **schedule** ([_PipelineScheduleMulti_](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineScheduleMulti "torch.distributed.pipelining.schedules.PipelineScheduleMulti")
    ) – Constructed multi-stage schedule whose finalized order will execute the pipeline step.
    
*   **pp\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Rank within the pipeline process group to analyze. This may differ from the rank constructing `schedule` because every rank holds the complete finalized schedule.
    
*   **stage\_indices** ([_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – Global logical stages whose activations should be analyzed. One pipeline rank commonly hosts multiple such virtual stages. Every selected stage must execute once per microbatch on `pp_rank`.
    
*   **granularity** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'microbatch'__,_ _'stage\_microbatch'__\]_) – `"stage_microbatch"` assigns independent lifetimes to every selected `(stage, microbatch)` pair. `"microbatch"` uses one lifetime per microbatch spanning the earliest selected-stage forward through the latest selected-stage release.
    

Returns:

An immutable activation-liveness plan. Its `PipelineActivationLiveness.slot_by_stage_and_microbatch` mapping contains a logical slot ID for every selected stage and microbatch.

Raises:

[**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
 – If the granularity or stage selection is invalid, the rank is absent, or the finalized schedule does not contain one valid forward-to-backward activation lifetime for every selected pair.

Return type:

[_PipelineActivationLiveness_](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineActivationLiveness "torch.distributed.pipelining.schedules.PipelineActivationLiveness")

_class_ torch.distributed.pipelining.schedules.PipelineActivationLiveness(_pp\_rank_, _granularity_, _stage\_indices_, _num\_microbatches_, _slot\_by\_stage\_and\_microbatch_, _num\_slots_, _\_activation\_lifetime\_by\_stage\_and\_microbatch_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L4877)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineActivationLiveness "Link to this definition")

Reusable activation slots derived from a pipeline schedule.

This result describes logical storage slots; it does not allocate or own tensors. Each key in `slot_by_stage_and_microbatch` is a global `(stage_index, microbatch_index)` pair, and each value is the integer ID of the slot assigned to that activation. A caller may map those IDs to its own buffers or arena regions. If activations have different sizes, the caller must size a shared slot for every activation assigned to it or group compatible activations before allocating storage.

An activation becomes live when its forward action executes and remains live through its full-backward or weight-backward action. Input-backward alone does not end the lifetime because a later weight-backward action may still need the forward activation. Schedule positions are inclusive, so two lifetimes that end and begin in the same compound action cannot share a slot.

With `granularity="stage_microbatch"`, each stage and microbatch pair has its own lifetime. With `granularity="microbatch"`, all selected stages for a microbatch share one lifetime from the earliest forward through the latest release, and therefore share one slot ID.

Instances are returned by [`analyze_pipeline_activation_liveness()`](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.analyze_pipeline_activation_liveness "torch.distributed.pipelining.schedules.analyze_pipeline_activation_liveness")
.

Variables:

*   **pp\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Rank in the pipeline process group whose schedule was analyzed. This is not necessarily the global distributed rank.
    
*   **granularity** (_Literal__\[__'microbatch'__,_ _'stage\_microbatch'__\]_) – Whether slots represent individual stage/microbatch pairs or whole microbatches across all selected stages.
    
*   **stage\_indices** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _...__\]_) – Global logical pipeline-stage indices included in the analysis. These commonly identify virtual stages hosted by `pp_rank`.
    
*   **num\_microbatches** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of microbatches in the analyzed schedule.
    
*   **slot\_by\_stage\_and\_microbatch** ([_collections.abc.Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – Immutable mapping from `(stage_index, microbatch_index)` to logical activation-slot ID.
    
*   **num\_slots** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of logical slots required by the assignment.
    

get\_activation\_lifetime(_stage\_index_, _microbatch\_index_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L4951)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineActivationLiveness.get_activation_lifetime "Link to this definition")

Return the inclusive schedule interval for an activation.

The returned `(forward_position, release_position)` indexes the finalized action sequence analyzed for `pp_rank`. Runtime schedules use their compute-and-communication sequence; other multi-stage schedules use their compute sequence.

At `stage_microbatch` granularity, the interval belongs to the exact stage and microbatch pair. At `microbatch` granularity, every selected stage for the microbatch returns the same interval: the convex hull from the earliest selected-stage forward to the latest selected-stage full- or weight-backward action.

Parameters:

*   **stage\_index** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global logical pipeline-stage index.
    
*   **microbatch\_index** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Microbatch index within the pipeline step.
    

Returns:

The inclusive `(forward_position, release_position)` interval.

Raises:

[**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
 – If the pair was not included in the analysis.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]

slot\_for(_stage\_index_, _microbatch\_index_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L4930)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineActivationLiveness.slot_for "Link to this definition")

Return the activation slot for a stage and microbatch.

Parameters:

*   **stage\_index** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global logical pipeline-stage index.
    
*   **microbatch\_index** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Microbatch index within the pipeline step.
    

Returns:

The logical activation-slot ID assigned to the pair.

Raises:

[**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
 – If the pair was not included in the analysis.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

_class_ torch.distributed.pipelining.schedules.ScheduleGPipe(_stage_, _n\_microbatches_, _loss\_fn\=None_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_, _output\_merge\_spec\=None_, _scale\_grads\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L1281)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.ScheduleGPipe "Link to this definition")

The GPipe schedule. Will go through all the microbatches in a fill-drain manner.

_class_ torch.distributed.pipelining.schedules.Schedule1F1B(_stage_, _n\_microbatches_, _loss\_fn\=None_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_, _output\_merge\_spec\=None_, _scale\_grads\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L1415)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.Schedule1F1B "Link to this definition")

The 1F1B schedule. Will perform one forward and one backward on the microbatches in steady state.

_class_ torch.distributed.pipelining.schedules.ScheduleInterleaved1F1B(_stages_, _n\_microbatches_, _loss\_fn\=None_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_, _output\_merge\_spec\=None_, _scale\_grads\=True_, _backward\_requires\_autograd\=True_, _defer\_pp\_recv\=False_, _max\_active\_stages\=3_, _unshard\_lookahead\='full'_, _\*_, _defer\_reduce\_grad\_wait\=False_, _max\_outstanding\_sends\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L4048)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.ScheduleInterleaved1F1B "Link to this definition")

The Interleaved 1F1B schedule. See [https://arxiv.org/pdf/2104.04473](https://arxiv.org/pdf/2104.04473)
 for details. Will perform one forward and one backward on the microbatches in steady state and supports multiple stages per rank. When microbatches are ready for multiple local stages, Interleaved 1F1B prioritizes the earlier microbatch (also called “depth first”).

This schedule is mostly similar to the original paper. It differs by being relaxing the requirement of num\_microbatch % pp\_size == 0. Using the flex\_pp schedule, we will have num\_rounds = max(1, n\_microbatches // pp\_group\_size) and it works as long as n\_microbatches % num\_rounds is 0. As a few examples, support

1.  pp\_group\_size = 4, n\_microbatches = 10. We will have num\_rounds = 2 and n\_microbatches % 2 is 0.
    
2.  pp\_group\_size = 4, n\_microbatches = 3. We will have num\_rounds = 1 and n\_microbatches % 1 is 0.
    

Parameters:

*   **max\_active\_stages** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Positive target number of local FSDP stages whose unsharded parameters may remain resident. An atomic compound action may transiently require up to its size minus one additional stages.
    
*   **unshard\_lookahead** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'full'__,_ _'auto'__\]_ _|_ _tuple__\[__python:int__,_ _...__\]_) – Number of upcoming distinct stages whose asynchronous unshards may be issued. `"full"` matches `max_active_stages`; `"auto"` uses `min(rank + 2, max_active_stages)`; a tuple supplies one positive integer per pipeline rank.
    
*   **defer\_reduce\_grad\_wait** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, delay each FSDP `WAIT_REDUCE_GRAD` until before the next reduction or schedule end. Otherwise, each wait follows its `REDUCE_GRAD`. At most one reduction may be pending per pipeline rank.
    
*   **max\_outstanding\_sends** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – Maximum number of pending forward and backward send batches on each pipeline rank. `None` applies no hard limit. A smaller limit may move a wait before its receive is guaranteed to be posted and may stall. Schedule construction raises `ValueError` when no causally safe wait placement can meet the limit.
    

_class_ torch.distributed.pipelining.schedules.ScheduleLoopedBFS(_stages_, _n\_microbatches_, _loss\_fn\=None_, _output\_merge\_spec\=None_, _scale\_grads\=True_, _backward\_requires\_autograd\=True_, _defer\_pp\_recv\=False_, _max\_active\_stages\=3_, _unshard\_lookahead\='full'_, _\*_, _defer\_reduce\_grad\_wait\=False_, _max\_outstanding\_sends\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L3797)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.ScheduleLoopedBFS "Link to this definition")

Breadth-First Pipeline Parallelism. See [https://arxiv.org/abs/2211.05953](https://arxiv.org/abs/2211.05953)
 for details. Similar to Interleaved 1F1B, Looped BFS supports multiple stages per rank. What is different is that when microbatches are ready for multiple local stages, Loops BFS will prioritizes the earlier stage, running all available microbatches at once.

Parameters:

*   **max\_active\_stages** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Positive target number of local FSDP stages whose unsharded parameters may remain resident. An atomic compound action may transiently require up to its size minus one additional stages.
    
*   **unshard\_lookahead** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'full'__,_ _'auto'__\]_ _|_ _tuple__\[__python:int__,_ _...__\]_) – Number of upcoming distinct stages whose asynchronous unshards may be issued. `"full"` matches `max_active_stages`; `"auto"` uses `min(rank + 2, max_active_stages)`; a tuple supplies one positive integer per pipeline rank.
    
*   **defer\_reduce\_grad\_wait** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, delay each FSDP `WAIT_REDUCE_GRAD` until before the next reduction or schedule end. Otherwise, each wait follows its `REDUCE_GRAD`. At most one reduction may be pending per pipeline rank.
    
*   **max\_outstanding\_sends** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – Maximum number of pending forward and backward send batches on each pipeline rank. `None` applies no hard limit.
    

_class_ torch.distributed.pipelining.schedules.ScheduleInterleavedZeroBubble(_stages_, _n\_microbatches_, _loss\_fn\=None_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_, _output\_merge\_spec\=None_, _scale\_grads\=True_, _backward\_requires\_autograd\=True_, _defer\_pp\_recv\=False_, _max\_active\_stages\=3_, _unshard\_lookahead\='full'_, _\*_, _defer\_reduce\_grad\_wait\=False_, _max\_outstanding\_sends\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L4192)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.ScheduleInterleavedZeroBubble "Link to this definition")

The Interleaved Zero Bubble schedule. See [https://arxiv.org/pdf/2401.10241](https://arxiv.org/pdf/2401.10241)
 for details. Will perform one forward and one backward on inputs for the microbatches in steady state and supports multiple stages per rank. Uses the backward for weights to fill in the pipeline bubble.

In particular this is implementing the ZB1P schedule in the paper.

Parameters:

*   **max\_active\_stages** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Positive target number of local FSDP stages whose unsharded parameters may remain resident. An atomic compound action may transiently require up to its size minus one additional stages.
    
*   **unshard\_lookahead** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'full'__,_ _'auto'__\]_ _|_ _tuple__\[__python:int__,_ _...__\]_) – Number of upcoming distinct stages whose asynchronous unshards may be issued. `"full"` matches `max_active_stages`; `"auto"` uses `min(rank + 2, max_active_stages)`; a tuple supplies one positive integer per pipeline rank.
    
*   **defer\_reduce\_grad\_wait** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, delay each FSDP `WAIT_REDUCE_GRAD` until before the next reduction or schedule end. Otherwise, each wait follows its `REDUCE_GRAD`. At most one reduction may be pending per pipeline rank.
    
*   **max\_outstanding\_sends** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – Maximum number of pending forward and backward send batches on each pipeline rank. `None` applies no hard limit.
    

_class_ torch.distributed.pipelining.schedules.ScheduleZBVZeroBubble(_stages_, _n\_microbatches_, _loss\_fn\=None_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_, _output\_merge\_spec\=None_, _scale\_grads\=True_, _backward\_requires\_autograd\=True_, _defer\_pp\_recv\=False_, _max\_active\_stages\=3_, _unshard\_lookahead\='full'_, _\*_, _defer\_reduce\_grad\_wait\=False_, _max\_outstanding\_sends\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L4408)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.ScheduleZBVZeroBubble "Link to this definition")

The Zero Bubble schedule (ZBV variant). See [https://arxiv.org/pdf/2401.10241](https://arxiv.org/pdf/2401.10241)
 Section 6 for details.

This schedules requires exactly two stages per rank.

This schedule will perform one forward and one backward on inputs for the microbatches in steady state and supports multiple stages per rank. Uses backward with respect to weights to fill in the pipeline bubble.

This ZB-V schedule would have the “zero bubble” property only if time forward == time backward input == time backward weights. In practice, this is not likely true for real models so alternatively a greedy scheduler could be implemented for unequal/unbalanced time.

Parameters:

*   **max\_active\_stages** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Positive target number of local FSDP stages whose unsharded parameters may remain resident. An atomic compound action may transiently require up to its size minus one additional stages.
    
*   **unshard\_lookahead** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'full'__,_ _'auto'__\]_ _|_ _tuple__\[__python:int__,_ _...__\]_) – Number of upcoming distinct stages whose asynchronous unshards may be issued. `"full"` matches `max_active_stages`; `"auto"` uses `min(rank + 2, max_active_stages)`; a tuple supplies one positive integer per pipeline rank.
    
*   **defer\_reduce\_grad\_wait** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, delay each FSDP `WAIT_REDUCE_GRAD` until before the next reduction or schedule end. Otherwise, each wait follows its `REDUCE_GRAD`. At most one reduction may be pending per pipeline rank.
    
*   **max\_outstanding\_sends** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – Maximum number of pending forward and backward send batches on each pipeline rank. `None` applies no hard limit.
    

_class_ torch.distributed.pipelining.schedules.ScheduleDualPipeV(_stages_, _n\_microbatches_, _loss\_fn\=None_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_, _output\_merge\_spec\=None_, _scale\_grads\=True_, _backward\_requires\_autograd\=True_, _defer\_pp\_recv\=False_, _max\_active\_stages\=3_, _unshard\_lookahead\='full'_, _\*_, _defer\_reduce\_grad\_wait\=False_, _max\_outstanding\_sends\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L4626)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.ScheduleDualPipeV "Link to this definition")

The DualPipeV schedule. A more efficient schedule variant based on the DualPipe schedule introduced by DeepSeek in [https://arxiv.org/pdf/2412.19437](https://arxiv.org/pdf/2412.19437)

Based on the open sourced code from [deepseek-ai/DualPipe](https://github.com/deepseek-ai/DualPipe)

Parameters:

*   **max\_active\_stages** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Positive target number of local FSDP stages whose unsharded parameters may remain resident. An atomic compound action may transiently require up to its size minus one additional stages.
    
*   **unshard\_lookahead** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'full'__,_ _'auto'__\]_ _|_ _tuple__\[__python:int__,_ _...__\]_) – Number of upcoming distinct stages whose asynchronous unshards may be issued. `"full"` matches `max_active_stages`; `"auto"` uses `min(rank + 2, max_active_stages)`; a tuple supplies one positive integer per pipeline rank.
    
*   **defer\_reduce\_grad\_wait** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, delay each FSDP `WAIT_REDUCE_GRAD` until before the next reduction or schedule end. Otherwise, each wait follows its `REDUCE_GRAD`. At most one reduction may be pending per pipeline rank.
    
*   **max\_outstanding\_sends** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – Maximum number of pending forward and backward send batches on each pipeline rank. `None` applies no hard limit.
    

_class_ torch.distributed.pipelining.schedules.PipelineScheduleSingle(_stage_, _n\_microbatches_, _loss\_fn\=None_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_, _output\_merge\_spec\=None_, _scale\_grads\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L1036)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineScheduleSingle "Link to this definition")

Base class for single-stage schedules. Implements the step method. Derived classes should implement \_step\_microbatches.

Gradients are scaled by num\_microbatches depending on the scale\_grads argument, defaulting to True. This setting should match the configuration of your loss\_fn, which may either average losses (scale\_grads=True) or sum losses (scale\_grads=False).

step(_\*args_, _target\=None_, _losses\=None_, _return\_outputs\=True_, _loss\_kwargs\=None_, _arg\_mbs\=None_, _kwarg\_mbs\=None_, _target\_mbs\=None_, _finalize\_gradients\=True_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L1090)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineScheduleSingle.step "Link to this definition")

Run one training iteration of a single-stage pipeline schedule.

By default, `args`, `kwargs`, and `target` are full-batch values that the schedule splits into microbatches. When the caller has already split inputs into microbatches, pass them through `arg_mbs`, `kwarg_mbs`, and `target_mbs` instead.

Parameters:

*   **\*args** (_Any_) – Whole-batch positional inputs for the first pipeline stage. Do not pass positional inputs with pre-split inputs.
    
*   **target** (_Any__,_ _optional_) – Whole-batch target for loss computation. When passing pre-split inputs, pass targets through `target_mbs` instead. Default: `None`.
    
*   **losses** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _,_ _optional_) – Mutable list populated with one loss per microbatch when this schedule owns the last stage and a `loss_fn` was configured. Default: `None`.
    
*   **return\_outputs** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to merge and return output chunks on the last stage. Default: `True`.
    
*   **loss\_kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _,_ _optional_) – Extra keyword arguments forwarded to the configured `loss_fn`. Default: `None`.
    
*   **arg\_mbs** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\]__,_ _optional_) – Pre-split positional inputs, one tuple per microbatch. Default: `None`.
    
*   **kwarg\_mbs** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
    _\]__,_ _optional_) – Pre-split keyword inputs, one dict per microbatch. Default: `None`.
    
*   **target\_mbs** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _,_ _optional_) – Pre-split targets, one entry per microbatch. Default: `None`.
    
*   **finalize\_gradients** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to reduce accumulated FSDP gradients and reshard FSDP parameters at the end of this call. If `False`, FSDP parameters stay unsharded, and a later call with `True` is required before reading `.grad`. With `scale_grads=True`, the final call divides by `n_microbatches` only. Divide by the number of accumulated calls separately if needed. This has no effect on non-FSDP stages. Default: `True`.
    
*   **\*\*kwargs** (_Any_) – Whole-batch keyword inputs for the first pipeline stage. Do not pass keyword inputs with pre-split inputs.
    

Returns:

The merged output from the last stage when this rank

owns the last stage and `return_outputs=True`; otherwise `None`.

Return type:

Any or None

Raises:

*   [**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
     – If backward computation is enabled and `step` is called under `torch.no_grad()`. Use `eval()` for forward-only execution.
    
*   [**TypeError**](https://docs.python.org/3/builtins/exceptions.html#TypeError "(in Python v3.15)")
     – If a pre-split microbatch container has the wrong type.
    
*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
     – If whole-batch and pre-split inputs are mixed, or if a pre-split container does not have one entry per microbatch.
    

Examples:

\>>> output \= schedule.step(x, mask\=mask, target\=target)
\>>> arg\_mbs \= \[(x0,), (x1,)\]
\>>> kwarg\_mbs \= \[{"mask": mask0}, {"mask": mask1}\]
\>>> target\_mbs \= \[target0, target1\]
\>>> output \= schedule.step(
...     arg\_mbs\=arg\_mbs,
...     kwarg\_mbs\=kwarg\_mbs,
...     target\_mbs\=target\_mbs,
... )

Copy to clipboard

_class_ torch.distributed.pipelining.schedules.PipelineScheduleMulti(_stages_, _n\_microbatches_, _loss\_fn\=None_, _args\_chunk\_spec\=None_, _kwargs\_chunk\_spec\=None_, _output\_merge\_spec\=None_, _use\_full\_backward\=None_, _scale\_grads\=True_, _backward\_requires\_autograd\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L2636)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineScheduleMulti "Link to this definition")

Base class for multi-stage schedules. Implements the step method.

Gradients are scaled by num\_microbatches depending on the scale\_grads argument, defaulting to True. This setting should match the configuration of your loss\_fn, which may either average losses (scale\_grads=True) or sum losses (scale\_grads=False).

step(_\*args_, _target\=None_, _losses\=None_, _return\_outputs\=True_, _loss\_kwargs\=None_, _arg\_mbs\=None_, _kwarg\_mbs\=None_, _target\_mbs\=None_, _finalize\_gradients\=True_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L2821)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.PipelineScheduleMulti.step "Link to this definition")

Run one training iteration of a multi-stage pipeline schedule.

By default, `args`, `kwargs`, and `target` are full-batch values that the schedule splits into microbatches. When the caller has already split inputs into microbatches, pass them through `arg_mbs`, `kwarg_mbs`, and `target_mbs` instead.

Parameters:

*   **\*args** (_Any_) – Whole-batch positional root inputs when this rank owns the first pipeline stage. Do not pass positional inputs with pre-split inputs.
    
*   **target** (_Any__,_ _optional_) – Whole-batch target for loss computation. When passing pre-split inputs, pass targets through `target_mbs` instead. Default: `None`.
    
*   **losses** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _,_ _optional_) – Mutable list populated with one loss per microbatch when this schedule owns the last stage and a `loss_fn` was configured. Default: `None`.
    
*   **return\_outputs** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to merge and return output chunks on the last stage. Default: `True`.
    
*   **loss\_kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _,_ _optional_) – Extra keyword arguments forwarded to the configured `loss_fn`. Default: `None`.
    
*   **arg\_mbs** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\]__,_ _optional_) – Pre-split positional inputs, one tuple per microbatch. Default: `None`.
    
*   **kwarg\_mbs** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
    _\]__,_ _optional_) – Pre-split keyword inputs, one dict per microbatch. Default: `None`.
    
*   **target\_mbs** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _,_ _optional_) – Pre-split targets, one entry per microbatch. Default: `None`.
    
*   **finalize\_gradients** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to reduce accumulated FSDP gradients and reshard FSDP parameters at the end of this call. If `False`, FSDP parameters stay unsharded, and a later call with `True` is required before reading `.grad`. With `scale_grads=True`, the final call divides by `n_microbatches` only. Divide by the number of accumulated calls separately if needed. This has no effect on non-FSDP stages. Default: `True`.
    
*   **\*\*kwargs** (_Any_) – Whole-batch keyword root inputs when this rank owns the first pipeline stage. Do not pass keyword inputs with pre-split inputs.
    

Returns:

The merged output from the last stage when this rank

owns the last stage and `return_outputs=True`; otherwise `None`.

Return type:

Any or None

Raises:

*   [**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
     – If backward computation is enabled and `step` is called under `torch.no_grad()`. Use `eval()` for forward-only execution.
    
*   [**TypeError**](https://docs.python.org/3/builtins/exceptions.html#TypeError "(in Python v3.15)")
     – If a pre-split microbatch container has the wrong type.
    
*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
     – If whole-batch and pre-split inputs are mixed, or if a pre-split container does not have one entry per microbatch.
    

Examples:

\>>> output \= schedule.step(x, mask\=mask, target\=target)
\>>> arg\_mbs \= \[(x0,), (x1,)\]
\>>> kwarg\_mbs \= \[{"mask": mask0}, {"mask": mask1}\]
\>>> target\_mbs \= \[target0, target1\]
\>>> output \= schedule.step(
...     arg\_mbs\=arg\_mbs,
...     kwarg\_mbs\=kwarg\_mbs,
...     target\_mbs\=target\_mbs,
... )

Copy to clipboard

torch.distributed.pipelining.schedules.get\_schedule\_class(_schedule\_name_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/pipelining/schedules.py#L5220)
[#](https://docs.pytorch.org/docs/2.15/distributed.pipelining.html#torch.distributed.pipelining.schedules.get_schedule_class "Link to this definition")

Maps a schedule name (case insensitive) to its corresponding class object.

Parameters:

**schedule\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – The name of the schedule.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/distributed.pipelining.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/distributed.pipelining.md.txt)

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