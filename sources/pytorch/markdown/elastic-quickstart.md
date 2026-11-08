Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/quickstart.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/quickstart.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/quickstart.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/quickstart.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/quickstart.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/quickstart.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/quickstart.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/quickstart.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/quickstart.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/quickstart.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/quickstart.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/quickstart.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/quickstart.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/quickstart.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/quickstart.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/quickstart.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/quickstart.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/quickstart.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/quickstart.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/quickstart.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/quickstart.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/quickstart.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/quickstart.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/quickstart.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/quickstart.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/quickstart.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/quickstart.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/quickstart.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/quickstart.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/quickstart.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/quickstart.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/quickstart.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/quickstart.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/quickstart.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/quickstart.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/quickstart.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/quickstart.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/quickstart.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/quickstart.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/quickstart.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/quickstart.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/quickstart.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/quickstart.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/quickstart.html)

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

Quickstart[#](https://docs.pytorch.org/docs/2.15/elastic/quickstart.html#quickstart "Link to this heading")

============================================================================================================

Created On: May 06, 2026 | Last Updated On: May 06, 2026

To launch a **fault-tolerant** job, run the following on all nodes.

torchrun
   \--nnodes\=NUM\_NODES
   \--nproc-per-node\=TRAINERS\_PER\_NODE
   \--max-restarts\=NUM\_ALLOWED\_FAILURES
   \--rdzv-id\=JOB\_ID
   \--rdzv-backend\=c10d
   \--rdzv-endpoint\=HOST\_NODE\_ADDR
   YOUR\_TRAINING\_SCRIPT.py (\--arg1 ... train script args...)

Copy to clipboard

To launch an **elastic** job, run the following on at least `MIN_SIZE` nodes and at most `MAX_SIZE` nodes.

torchrun
    \--nnodes\=MIN\_SIZE:MAX\_SIZE
    \--nproc-per-node\=TRAINERS\_PER\_NODE
    \--max-restarts\=NUM\_ALLOWED\_FAILURES\_OR\_MEMBERSHIP\_CHANGES
    \--rdzv-id\=JOB\_ID
    \--rdzv-backend\=c10d
    \--rdzv-endpoint\=HOST\_NODE\_ADDR
    YOUR\_TRAINING\_SCRIPT.py (\--arg1 ... train script args...)

Copy to clipboard

Note

TorchElastic models failures as membership changes. When a node fails, this is treated as a “scale down” event. When the failed node is replaced by the scheduler, it is a “scale up” event. Hence for both fault tolerant and elastic jobs, `--max-restarts` is used to control the total number of restarts before giving up, regardless of whether the restart was caused due to a failure or a scaling event.

`HOST_NODE_ADDR`, in form <host>\[:<port>\] (e.g. node1.example.com:29400), specifies the node and the port on which the C10d rendezvous backend should be instantiated and hosted. It can be any node in your training cluster, but ideally you should pick a node that has a high bandwidth.

Note

If no port number is specified `HOST_NODE_ADDR` defaults to 29400.

Note

The `--standalone` option can be passed to launch a single node job with a sidecar rendezvous backend. You don’t have to pass `--rdzv-id`, `--rdzv-endpoint`, and `--rdzv-backend` when the `--standalone` option is used.

Note

Learn more about writing your distributed training script [here](https://docs.pytorch.org/docs/2.15/elastic/train_script.html)
.

If `torchrun` does not meet your requirements you may use our APIs directly for more powerful customization. Start by taking a look at the [elastic agent](https://docs.pytorch.org/docs/2.15/elastic/agent.html)
 API.

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/quickstart.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/quickstart.md.txt)

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