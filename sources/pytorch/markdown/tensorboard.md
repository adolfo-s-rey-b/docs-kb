Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/tensorboard.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/tensorboard.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/tensorboard.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/tensorboard.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/tensorboard.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/tensorboard.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/tensorboard.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/tensorboard.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/tensorboard.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/tensorboard.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/tensorboard.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/tensorboard.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/tensorboard.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/tensorboard.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/tensorboard.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/tensorboard.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/tensorboard.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/tensorboard.html)
[v1.13](https://docs.pytorch.org/docs/1.13/tensorboard.html)
[v1.12](https://docs.pytorch.org/docs/1.12/tensorboard.html)
[v1.11](https://docs.pytorch.org/docs/1.11/tensorboard.html)
[v1.10](https://docs.pytorch.org/docs/1.10/tensorboard.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/tensorboard.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/tensorboard.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/tensorboard.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/tensorboard.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/tensorboard.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/tensorboard.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/tensorboard.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/tensorboard.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/tensorboard.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/tensorboard.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/tensorboard.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/tensorboard.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/tensorboard.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/tensorboard.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/tensorboard.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/tensorboard.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/tensorboard.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/tensorboard.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/tensorboard.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/tensorboard.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/tensorboard.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/tensorboard.html)

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

torch.utils.tensorboard[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#module-torch.utils.tensorboard "Link to this heading")

======================================================================================================================================

Created On: Apr 25, 2019 | Last Updated On: Jul 20, 2026

Before going further, more details on TensorBoard can be found at [https://www.tensorflow.org/tensorboard/](https://www.tensorflow.org/tensorboard/)

Once you’ve installed TensorBoard, these utilities let you log PyTorch models and metrics into a directory for visualization within the TensorBoard UI. Scalars, images, histograms, graphs, and embedding visualizations are all supported for PyTorch models and tensors.

The SummaryWriter class is your main entry to log data for consumption and visualization by TensorBoard. For example:

import torch
import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms

\# Writer will output to ./runs/ directory by default
writer \= SummaryWriter()

transform \= transforms.Compose(\[transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))\])
trainset \= datasets.MNIST('mnist\_train', train\=True, download\=True, transform\=transform)
trainloader \= torch.utils.data.DataLoader(trainset, batch\_size\=64, shuffle\=True)
model \= torchvision.models.resnet50(False)
\# Have ResNet model take in grayscale rather than RGB
model.conv1 \= torch.nn.Conv2d(1, 64, kernel\_size\=7, stride\=2, padding\=3, bias\=False)
images, labels \= next(iter(trainloader))

grid \= torchvision.utils.make\_grid(images)
writer.add\_image('images', grid, 0)
writer.add\_graph(model, images)
writer.close()

Copy to clipboard

This can then be visualized with TensorBoard, which should be installable and runnable with:

pip install tensorboard
tensorboard \--logdir\=runs

Copy to clipboard

Lots of information can be logged for one experiment. To avoid cluttering the UI and have better result clustering, we can group plots by naming them hierarchically. For example, “Loss/train” and “Loss/test” will be grouped together, while “Accuracy/train” and “Accuracy/test” will be grouped separately in the TensorBoard interface.

from torch.utils.tensorboard import SummaryWriter
import numpy as np

writer \= SummaryWriter()

for n\_iter in range(100):
    writer.add\_scalar('Loss/train', np.random.random(), n\_iter)
    writer.add\_scalar('Loss/test', np.random.random(), n\_iter)
    writer.add\_scalar('Accuracy/train', np.random.random(), n\_iter)
    writer.add\_scalar('Accuracy/test', np.random.random(), n\_iter)

Copy to clipboard

Expected result:

[![_images/hier_tags.png](https://docs.pytorch.org/docs/2.15/_images/hier_tags.png)](https://docs.pytorch.org/docs/2.15/_images/hier_tags.png)

  
  

_class_ torch.utils.tensorboard.writer.SummaryWriter(_log\_dir\=None_, _comment\=''_, _purge\_step\=None_, _max\_queue\=10_, _flush\_secs\=120_, _filename\_suffix\=''_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L173)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter "Link to this definition")

Writes entries directly to event files in the log\_dir to be consumed by TensorBoard.

The SummaryWriter class provides a high-level API to create an event file in a given directory and add summaries and events to it. The class updates the file contents asynchronously. This allows a training program to call methods to add data to the file directly from the training loop, without slowing down training.

\_\_init\_\_(_log\_dir\=None_, _comment\=''_, _purge\_step\=None_, _max\_queue\=10_, _flush\_secs\=120_, _filename\_suffix\=''_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L183)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.__init__ "Link to this definition")

Create a SummaryWriter that will write out events and summaries to the event file.

Parameters:

*   **log\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Save directory location. Default is runs/**CURRENT\_DATETIME\_HOSTNAME**, which changes after each run. Use hierarchical folder structure to compare between runs easily. e.g. pass in ‘runs/exp1’, ‘runs/exp2’, etc. for each new experiment to compare across them.
    
*   **comment** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Comment log\_dir suffix appended to the default `log_dir`. If `log_dir` is assigned, this argument has no effect.
    
*   **purge\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – When logging crashes at step T+XT+XT+X and restarts at step TTT, any events whose global\_step larger or equal to TTT will be purged and hidden from TensorBoard. Note that crashed and resumed experiments should have the same `log_dir`.
    
*   **max\_queue** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Size of the queue for pending events and summaries before one of the ‘add’ calls forces a flush to disk. Default is ten items.
    
*   **flush\_secs** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – How often, in seconds, to flush the pending events and summaries to disk. Default is every two minutes.
    
*   **filename\_suffix** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Suffix added to all event filenames in the log\_dir directory. More details on filename construction in tensorboard.summary.writer.event\_file\_writer.EventFileWriter.
    

Examples:

from torch.utils.tensorboard import SummaryWriter

\# create a summary writer with automatically generated folder name.
writer \= SummaryWriter()
\# folder location: runs/May04\_22-14-54\_s-MacBook-Pro.local/

\# create a summary writer using the specified folder name.
writer \= SummaryWriter("my\_experiment")
\# folder location: my\_experiment

\# create a summary writer with comment appended.
writer \= SummaryWriter(comment\="LR\_0.1\_BATCH\_16")
\# folder location: runs/May04\_22-14-54\_s-MacBook-Pro.localLR\_0.1\_BATCH\_16/

Copy to clipboard

add\_scalar(_tag_, _scalar\_value_, _global\_step\=None_, _walltime\=None_, _new\_style\=False_, _double\_precision\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L347)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_scalar "Link to this definition")

Add scalar data to summary.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **scalar\_value** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ _string/blobname_) – Value to save
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) with seconds after epoch of event
    
*   **new\_style** (_boolean_) – Whether to use new style (tensor field) or old style (simple\_value field). New style could lead to faster data loading.
    

Examples:

from torch.utils.tensorboard import SummaryWriter
writer \= SummaryWriter()
x \= range(100)
for i in x:
    writer.add\_scalar('y=2x', i \* 2, i)
writer.close()

Copy to clipboard

Expected result:

[![_images/add_scalar.png](https://docs.pytorch.org/docs/2.15/_images/add_scalar.png)](https://docs.pytorch.org/docs/2.15/_images/add_scalar.png)

add\_scalars(_main\_tag_, _tag\_scalar\_dict_, _global\_step\=None_, _walltime\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L388)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_scalars "Link to this definition")

Add many scalar data to summary.

Parameters:

*   **main\_tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The parent name for the tags
    
*   **tag\_scalar\_dict** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    ) – Key-value pair storing the tag and corresponding values
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    

Examples:

from torch.utils.tensorboard import SummaryWriter
writer \= SummaryWriter()
r \= 5
for i in range(100):
    writer.add\_scalars('run\_14h', {'xsinx':i\*np.sin(i/r),
                                    'xcosx':i\*np.cos(i/r),
                                    'tanx': np.tan(i/r)}, i)
writer.close()
\# This call adds three values to the same scalar plot with the tag
\# 'run\_14h' in TensorBoard's scalar section.

Copy to clipboard

Expected result:

[![_images/add_scalars.png](https://docs.pytorch.org/docs/2.15/_images/add_scalars.png)](https://docs.pytorch.org/docs/2.15/_images/add_scalars.png)

add\_histogram(_tag_, _values_, _global\_step\=None_, _bins\='tensorflow'_, _walltime\=None_, _max\_bins\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L465)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_histogram "Link to this definition")

Add histogram to summary.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **values** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ [_numpy.ndarray_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
    _, or_ _string/blobname_) – Values to build histogram
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **bins** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – One of {‘tensorflow’,’auto’, ‘fd’, …}. This determines how the bins are made. You can find other options in: [https://numpy.org/doc/stable/reference/generated/numpy.histogram.html](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html)
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    

Examples:

from torch.utils.tensorboard import SummaryWriter
import numpy as np
writer \= SummaryWriter()
for i in range(10):
    x \= np.random.random(1000)
    writer.add\_histogram('distribution centers', x + i, i)
writer.close()

Copy to clipboard

Expected result:

[![_images/add_histogram.png](https://docs.pytorch.org/docs/2.15/_images/add_histogram.png)](https://docs.pytorch.org/docs/2.15/_images/add_histogram.png)

add\_image(_tag_, _img\_tensor_, _global\_step\=None_, _walltime\=None_, _dataformats\='CHW'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L583)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_image "Link to this definition")

Add image data to summary.

Note that this requires the `pillow` package.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **img\_tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ [_numpy.ndarray_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
    _, or_ _string/blobname_) – Image data
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    
*   **dataformats** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Image data format specification of the form CHW, HWC, HW, WH, etc.
    

Shape:

img\_tensor: Default is (3,H,W)(3, H, W)(3,H,W). You can use `torchvision.utils.make_grid()` to convert a batch of tensor into 3xHxW format or call `add_images` and let us do the job. Tensor with (1,H,W)(1, H, W)(1,H,W), (H,W)(H, W)(H,W), (H,W,3)(H, W, 3)(H,W,3) is also suitable as long as corresponding `dataformats` argument is passed, e.g. `CHW`, `HWC`, `HW`.

Examples:

from torch.utils.tensorboard import SummaryWriter
import numpy as np
img \= np.zeros((3, 100, 100))
img\[0\] \= np.arange(0, 10000).reshape(100, 100) / 10000
img\[1\] \= 1 \- np.arange(0, 10000).reshape(100, 100) / 10000

img\_HWC \= np.zeros((100, 100, 3))
img\_HWC\[:, :, 0\] \= np.arange(0, 10000).reshape(100, 100) / 10000
img\_HWC\[:, :, 1\] \= 1 \- np.arange(0, 10000).reshape(100, 100) / 10000

writer \= SummaryWriter()
writer.add\_image('my\_image', img, 0)

\# If you have non-default dimension setting, set the dataformats argument.
writer.add\_image('my\_image\_HWC', img\_HWC, 0, dataformats\='HWC')
writer.close()

Copy to clipboard

Expected result:

[![_images/add_image.png](https://docs.pytorch.org/docs/2.15/_images/add_image.png)](https://docs.pytorch.org/docs/2.15/_images/add_image.png)

add\_images(_tag_, _img\_tensor_, _global\_step\=None_, _walltime\=None_, _dataformats\='NCHW'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L634)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_images "Link to this definition")

Add batched image data to summary.

Note that this requires the `pillow` package.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **img\_tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ [_numpy.ndarray_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
    _, or_ _string/blobname_) – Image data
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    
*   **dataformats** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Image data format specification of the form NCHW, NHWC, CHW, HWC, HW, WH, etc.
    

Shape:

img\_tensor: Default is (N,3,H,W)(N, 3, H, W)(N,3,H,W). If `dataformats` is specified, other shape will be accepted. e.g. NCHW or NHWC.

Examples:

from torch.utils.tensorboard import SummaryWriter
import numpy as np

img\_batch \= np.zeros((16, 3, 100, 100))
for i in range(16):
    img\_batch\[i, 0\] \= np.arange(0, 10000).reshape(100, 100) / 10000 / 16 \* i
    img\_batch\[i, 1\] \= (1 \- np.arange(0, 10000).reshape(100, 100) / 10000) / 16 \* i

writer \= SummaryWriter()
writer.add\_images('my\_image\_batch', img\_batch, 0)
writer.close()

Copy to clipboard

Expected result:

[![_images/add_images.png](https://docs.pytorch.org/docs/2.15/_images/add_images.png)](https://docs.pytorch.org/docs/2.15/_images/add_images.png)

add\_figure(_tag_, _figure_, _global\_step\=None_, _close\=True_, _walltime\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L729)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_figure "Link to this definition")

Render matplotlib figure into an image and add it to summary.

Note that this requires the `matplotlib` package.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **figure** (_Figure_ _|_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[__Figure__\]_) – Figure or a list of figures
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – Global step value to record
    
*   **close** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Flag to automatically close the figure
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ _None_) – Optional override default walltime (time.time()) seconds after epoch of event
    

add\_video(_tag_, _vid\_tensor_, _global\_step\=None_, _fps\=4_, _walltime\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L767)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_video "Link to this definition")

Add video data to summary.

Note that this requires the `moviepy` package.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **vid\_tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Video data
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **fps** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Frames per second
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    

Shape:

vid\_tensor: (N,T,C,H,W)(N, T, C, H, W)(N,T,C,H,W). The values should lie in \[0, 255\] for type uint8 or \[0, 1\] for type float.

add\_audio(_tag_, _snd\_tensor_, _global\_step\=None_, _sample\_rate\=44100_, _walltime\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L787)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_audio "Link to this definition")

Add audio data to summary.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **snd\_tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Sound data
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **sample\_rate** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – sample rate in Hz
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    

Shape:

snd\_tensor: (1,L)(1, L)(1,L). The values should lie between \[-1, 1\].

add\_text(_tag_, _text\_string_, _global\_step\=None_, _walltime\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L807)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_text "Link to this definition")

Add text data to summary.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **text\_string** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – String to save
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    

Examples:

writer.add\_text('lstm', 'This is an lstm', 0)
writer.add\_text('rnn', 'This is an rnn', 10)

Copy to clipboard

add\_graph(_model_, _input\_to\_model\=None_, _verbose\=False_, _use\_strict\_trace\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L830)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_graph "Link to this definition")

Add graph data to summary.

Parameters:

*   **model** ([_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – Model to draw.
    
*   **input\_to\_model** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
     _of_ [_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – A variable or a tuple of variables to be fed.
    
*   **verbose** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to print graph structure in console.
    
*   **use\_strict\_trace** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to pass keyword argument strict to torch.jit.trace. Pass False when you want the tracer to record your mutable container types (list, dict)
    

add\_embedding(_mat_, _metadata\=None_, _label\_img\=None_, _global\_step\=None_, _tag\='default'_, _metadata\_header\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L859)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_embedding "Link to this definition")

Add embedding projector data to summary.

Parameters:

*   **mat** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ [_numpy.ndarray_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
    ) – A matrix which each row is the feature vector of the data point
    
*   **metadata** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    ) – A list of labels, each element will be converted to string
    
*   **label\_img** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Images correspond to each data point
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name for the embedding
    
*   **metadata\_header** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    ) – A list of headers for multi-column metadata. If given, each metadata must be a list with values corresponding to headers.
    

Shape:

mat: (N,D)(N, D)(N,D), where N is number of data and D is feature dimension

label\_img: (N,C,H,W)(N, C, H, W)(N,C,H,W)

Examples:

import keyword
import torch
meta \= \[\]
while len(meta)<100:
    meta \= meta+keyword.kwlist \# get some strings
meta \= meta\[:100\]

for i, v in enumerate(meta):
    meta\[i\] \= v+str(i)

label\_img \= torch.rand(100, 3, 10, 32)
for i in range(100):
    label\_img\[i\]\*=i/100.0

writer.add\_embedding(torch.randn(100, 5), metadata\=meta, label\_img\=label\_img)
writer.add\_embedding(torch.randn(100, 5), label\_img\=label\_img)
writer.add\_embedding(torch.randn(100, 5), metadata\=meta)

Copy to clipboard

Note

Categorical (i.e. non-numeric) metadata cannot have more than 50 unique values if they are to be used for coloring in the embedding projector.

add\_pr\_curve(_tag_, _labels_, _predictions_, _global\_step\=None_, _num\_thresholds\=127_, _weights\=None_, _walltime\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L964)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_pr_curve "Link to this definition")

Add precision recall curve.

Plotting a precision-recall curve lets you understand your model’s performance under different threshold settings. With this function, you provide the ground truth labeling (T/F) and prediction confidence (usually the output of your model) for each target. The TensorBoard UI will let you choose the threshold interactively.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **labels** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ [_numpy.ndarray_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
    _, or_ _string/blobname_) – Ground truth data. Binary label for each element.
    
*   **predictions** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ [_numpy.ndarray_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
    _, or_ _string/blobname_) – The probability that an element be classified as true. Value should be in \[0, 1\]
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **num\_thresholds** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of thresholds used to draw the curve.
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    

Examples:

from torch.utils.tensorboard import SummaryWriter
import numpy as np
labels \= np.random.randint(2, size\=100)  \# binary label
predictions \= np.random.rand(100)
writer \= SummaryWriter()
writer.add\_pr\_curve('pr\_curve', labels, predictions, 0)
writer.close()

Copy to clipboard

add\_custom\_scalars(_layout_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L1101)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_custom_scalars "Link to this definition")

Create special chart by collecting charts tags in ‘scalars’.

NOTE: This function can only be called once for each SummaryWriter() object.

Because it only provides metadata to tensorboard, the function can be called before or after the training loop.

Parameters:

**layout** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
) – {categoryName: _charts_}, where _charts_ is also a dictionary {chartName: _ListOfProperties_}. The first element in _ListOfProperties_ is the chart’s type (one of **Multiline** or **Margin**) and the second element should be a list containing the tags you have used in add\_scalar function, which will be collected into the new chart.

Examples:

layout \= {'Taiwan':{'twse':\['Multiline',\['twse/0050', 'twse/2330'\]\]},
             'USA':{ 'dow':\['Margin',   \['dow/aaa', 'dow/bbb', 'dow/ccc'\]\],
                  'nasdaq':\['Margin',   \['nasdaq/aaa', 'nasdaq/bbb', 'nasdaq/ccc'\]\]}}

writer.add\_custom\_scalars(layout)

Copy to clipboard

add\_mesh(_tag_, _vertices_, _colors\=None_, _faces\=None_, _config\_dict\=None_, _global\_step\=None_, _walltime\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L1125)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_mesh "Link to this definition")

Add meshes or 3D point clouds to TensorBoard.

The visualization is based on Three.js, so it allows users to interact with the rendered object. Besides the basic definitions such as vertices, faces, users can further provide camera parameter, lighting condition, etc. Please check [https://threejs.org/docs/index.html#manual/en/introduction/Creating-a-scene](https://threejs.org/docs/index.html#manual/en/introduction/Creating-a-scene)
 for advanced usage.

Parameters:

*   **tag** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Data identifier
    
*   **vertices** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – List of the 3D coordinates of vertices.
    
*   **colors** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Colors for each vertex
    
*   **faces** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Indices of vertices within each triangle. (Optional)
    
*   **config\_dict** – Dictionary with ThreeJS classes names and configuration.
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    
*   **walltime** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional override default walltime (time.time()) seconds after epoch of event
    

Shape:

vertices: (B,N,3)(B, N, 3)(B,N,3). (batch, number\_of\_vertices, channels)

colors: (B,N,3)(B, N, 3)(B,N,3). The values should lie in \[0, 255\] for type uint8 or \[0, 1\] for type float.

faces: (B,N,3)(B, N, 3)(B,N,3). The values should lie in \[0, number\_of\_vertices\] for type uint8.

Examples:

from torch.utils.tensorboard import SummaryWriter
vertices\_tensor \= torch.as\_tensor(\[\
    \[1, 1, 1\],\
    \[\-1, \-1, 1\],\
    \[1, \-1, \-1\],\
    \[\-1, 1, \-1\],\
\], dtype\=torch.float).unsqueeze(0)
colors\_tensor \= torch.as\_tensor(\[\
    \[255, 0, 0\],\
    \[0, 255, 0\],\
    \[0, 0, 255\],\
    \[255, 0, 255\],\
\], dtype\=torch.int).unsqueeze(0)
faces\_tensor \= torch.as\_tensor(\[\
    \[0, 2, 3\],\
    \[0, 3, 1\],\
    \[0, 1, 2\],\
    \[1, 3, 2\],\
\], dtype\=torch.int).unsqueeze(0)

writer \= SummaryWriter()
writer.add\_mesh('my\_mesh', vertices\=vertices\_tensor, colors\=colors\_tensor, faces\=faces\_tensor)

writer.close()

Copy to clipboard

add\_hparams(_hparam\_dict_, _metric\_dict_, _hparam\_domain\_discrete\=None_, _run\_name\=None_, _global\_step\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L292)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.add_hparams "Link to this definition")

Add a set of hyperparameters to be compared in TensorBoard.

Parameters:

*   **hparam\_dict** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    ) – Each key-value pair in the dictionary is the name of the hyper parameter and its corresponding value. The type of the value can be one of bool, string, float, int, or None.
    
*   **metric\_dict** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    ) – Each key-value pair in the dictionary is the name of the metric and its corresponding value. Note that the key used here should be unique in the tensorboard record. Otherwise the value you added by `add_scalar` will be displayed in hparam plugin. In most cases, this is unwanted.
    
*   **hparam\_domain\_discrete** – (Optional\[Dict\[str, List\[Any\]\]\]) A dictionary that contains names of the hyperparameters and all discrete values they can hold
    
*   **run\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the run, to be included as part of the logdir. If unspecified, will use current timestamp.
    
*   **global\_step** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global step value to record
    

Examples:

from torch.utils.tensorboard import SummaryWriter
with SummaryWriter() as w:
    for i in range(5):
        w.add\_hparams({'lr': 0.1\*i, 'bsize': i},
                      {'hparam/accuracy': 10\*i, 'hparam/loss': 10\*i})

Copy to clipboard

Expected result:

[![_images/add_hparam.png](https://docs.pytorch.org/docs/2.15/_images/add_hparam.png)](https://docs.pytorch.org/docs/2.15/_images/add_hparam.png)

flush()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L1192)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.flush "Link to this definition")

Flushes the event file to disk.

Call this method to make sure that all pending events have been written to disk.

close()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/tensorboard/writer.py#L1203)
[#](https://docs.pytorch.org/docs/2.15/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter.close "Link to this definition")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/tensorboard.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/tensorboard.md.txt)

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