[Skip to main content](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-performance.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Performance[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-performance.html#performance "Link to this heading")

=============================================================================================================================================

Conda's performance can be affected by a variety of things. Unlike many package managers, Anaconda’s repositories generally don’t filter or remove old packages from the index. This allows old environments to be easily recreated. However, it does mean that the index metadata is always growing, and thus conda becomes slower as the number of packages increases.

How a package is installed[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-performance.html#how-a-package-is-installed "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While you are waiting, conda is doing a lot of work installing the packages. At any point along these steps, performance issues may arise.

Conda follows these steps when installing a package:

1.  Downloading and processing index metadata.
    
2.  Reducing the index.
    
3.  Expressing the package data and constraints as a SAT problem.
    
4.  Running the solver.
    
5.  Downloading and extracting packages.
    
6.  Verifying package contents.
    
7.  Linking packages from package cache into environments.
    

Therefore, if you're experiencing a slowdown, evaluate the following questions to identify potential causes:

*   Are you creating a new environment or installing into an existing one?
    
*   Does your environment have pip-installed dependencies in it?
    
*   What channels are you using?
    
*   What packages are you installing?
    
*   Is the channel metadata sane?
    
*   Are channels interacting in bad ways?
    

Improving conda performance[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-performance.html#improving-conda-performance "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section goes over some of the best practices we recommend for addressing performance challenges.

1.  **Make your package specifications more narrow.**
    
    For example, instead of `numpy`, we recommend `numpy=1.15` or, even better, `numpy=1.15.4`.
    
2.  **Use the rattler solver plugin.** The plugin is the default solver starting with conda 26.10.0 and improves performance for large environments. If you previously selected another solver, that setting is preserved when you upgrade conda.
    
    Note
    
    The classic solver, now named pycosat (classic remains a supported alias), is provided by the standalone [conda-pycosat-solver](https://github.com/conda/conda-pycosat-solver)
     plugin rather than being registered by conda itself.
    
    To check which solver you have, run the following command:
    
    conda config \--show solver
    
    Copy to clipboard
    
    If rattler is set as your solver, you will see the following:
    
    solver: rattler
    
    Copy to clipboard
    
    If you don't have rattler set as your solver, follow these steps to enable it:
    
    1.  Make sure `conda-rattler-solver` is installed in your base environment:
        
        conda install \--name base conda-rattler-solver
        
        Copy to clipboard
        
    2.  Set rattler as your solver:
        
        conda config \--set solver rattler
        
        Copy to clipboard
        
    
    Tip
    
    You can also use the rattler solver temporarily when installing a package:
    
    conda install \--solver\=rattler package\_name
    
    Copy to clipboard
    
    For more information on conda's solver options, see [Solvers](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/solvers.html)
    .
    

3.  **Configure channels to minimize conflicts.**
    
    Channel configuration has a significant impact on solver performance and environment reproducibility. We recommend using a single channel as your default, such as `conda-forge` or `defaults`, but not both. Mixing channels in your global configuration increases solver search space and the risk of incompatible packages.
    
    For more information on channel configuration, see [Channel configuration best practices](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-channels.html#channel-best-practices)
    .
    
    If you must use both `defaults` and `conda-forge` in your channel list, setting strict channel priority reduces solver search space and helps prevent mixed-channel environments:
    
    conda config \--set channel\_priority strict
    
    Copy to clipboard
    
    Warning
    
    Strict channel priority can make some environments unsatisfiable and blocks fallback to lower-priority channels when a package with the same name exists in a higher-priority channel. To learn more about strict channel priority and channel configuration, see [channel configuration best practices](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-channels.html#strict)
    .
    
    [![../../_images/strict-disabled.png](https://docs.conda.io/projects/conda/en/stable/_images/strict-disabled.png)](https://docs.conda.io/projects/conda/en/stable/_images/strict-disabled.png)
    
    [![../../_images/strict-enabled.png](https://docs.conda.io/projects/conda/en/stable/_images/strict-enabled.png)](https://docs.conda.io/projects/conda/en/stable/_images/strict-enabled.png)
    
4.  **Use sharded repodata.** This splits your repodata into multiple small files and fetches only what is needed, which dramatically speeds up environment creation and updates. Learn more in [CEP 16](https://conda.org/learn/ceps/cep-0016)
    .
    
    Note
    
    This option is currently available for conda-forge and prefix.dev for all channels as of March 2026.
    
    With the rattler and libmamba solvers, sharded repodata is enabled by default through conda's `repodata_use_shards` setting. Channels that do not publish sharded repodata are fetched normally.
    
    To disable sharded repodata, run:
    
    conda config \--set repodata\_use\_shards false
    
    Copy to clipboard
    

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/user-guide/concepts/conda-performance.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/user-guide/concepts/conda-performance.rst.txt)