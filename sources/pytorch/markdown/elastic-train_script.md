Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/train_script.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/train_script.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/train_script.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/train_script.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/train_script.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/train_script.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/train_script.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/train_script.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/train_script.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/train_script.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/train_script.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/train_script.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/train_script.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/train_script.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/train_script.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/train_script.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/train_script.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/train_script.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/train_script.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/train_script.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/train_script.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/train_script.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/train_script.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/train_script.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/train_script.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/train_script.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/train_script.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/train_script.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/train_script.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/train_script.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/train_script.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/train_script.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/train_script.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/train_script.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/train_script.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/train_script.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/train_script.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/train_script.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/train_script.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/train_script.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/train_script.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/train_script.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/train_script.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/train_script.html)

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

Train script[#](https://docs.pytorch.org/docs/2.15/elastic/train_script.html#train-script "Link to this heading")

==================================================================================================================

Created On: May 06, 2026 | Last Updated On: May 06, 2026

If your train script works with `torch.distributed.launch` it will continue working with `torchrun` with these differences:

1.  No need to manually pass `RANK`, `WORLD_SIZE`, `MASTER_ADDR`, and `MASTER_PORT`.
    
2.  `rdzv_backend` and `rdzv_endpoint` can be provided. For most users this will be set to `c10d` (see [Rendezvous](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html)
    ). The default `rdzv_backend` creates a non-elastic rendezvous where `rdzv_endpoint` holds the master address.
    
3.  Make sure you have a `load_checkpoint(path)` and `save_checkpoint(path)` logic in your script. When any number of workers fail we restart all the workers with the same program arguments so you will lose progress up to the most recent checkpoint (see [elastic launch](https://docs.pytorch.org/docs/2.15/elastic/run.html)
    ).
    
4.  `use_env` flag has been removed. If you were parsing local rank by parsing the `--local-rank` option, you need to get the local rank from the environment variable `LOCAL_RANK` (e.g. `int(os.environ["LOCAL_RANK"])`).
    

Below is an expository example of a training script that checkpoints on each epoch, hence the worst-case progress lost on failure is one full epoch worth of training.

  def main():
       args \= parse\_args(sys.argv\[1:\])
       state \= load\_checkpoint(args.checkpoint\_path)
       initialize(state)

       \# torch.distributed.run ensures that this will work
       \# by exporting all the env vars needed to initialize the process group
       torch.distributed.init\_process\_group(backend\=args.backend)

       for i in range(state.epoch, state.total\_num\_epochs)
            for batch in iter(state.dataset)
                train(batch, state.model)

            state.epoch += 1
            save\_checkpoint(state)

Copy to clipboard

For concrete examples of torchelastic-compliant train scripts, visit our [examples](https://docs.pytorch.org/docs/2.15/elastic/examples.html)
 page.

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/train_script.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/train_script.md.txt)

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