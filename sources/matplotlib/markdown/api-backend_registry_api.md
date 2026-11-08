[Skip to main content](https://matplotlib.org/stable/api/backend_registry_api.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

`matplotlib.backends.registry`[#](https://matplotlib.org/stable/api/backend_registry_api.html#module-matplotlib.backends.registry "Link to this heading")

==========================================================================================================================================================

class matplotlib.backends.registry.BackendFilter(_\*values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L5-L12)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendFilter "Link to this definition")

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)")

Filter used with [`list_builtin()`](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.list_builtin "matplotlib.backends.registry.BackendRegistry.list_builtin")

Added in version 3.9.

INTERACTIVE \= 0[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendFilter.INTERACTIVE "Link to this definition")

NON\_INTERACTIVE \= 1[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendFilter.NON_INTERACTIVE "Link to this definition")

class matplotlib.backends.registry.BackendRegistry[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L15-L410)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Registry of backends available within Matplotlib.

This is the single source of truth for available backends.

All use of `BackendRegistry` should be via the singleton instance `backend_registry` which can be imported from `matplotlib.backends`.

Each backend has a name, a module name containing the backend code, and an optional GUI framework that must be running if the backend is interactive. There are three sources of backends: built-in (source code is within the Matplotlib repository), explicit `module://some.backend` syntax (backend is obtained by loading the module), or via an entry point (self-registering backend in an external package).

Added in version 3.9.

backend\_for\_gui\_framework(_framework_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L186-L200)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.backend_for_gui_framework "Link to this definition")

Return the name of the backend corresponding to the specified GUI framework.

Parameters:

**framework**str

GUI framework such as "qt".

Returns:

str or None

Backend name or None if GUI framework not recognised.

is\_valid\_backend(_backend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L202-L248)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.is_valid_backend "Link to this definition")

Return True if the backend name is valid, False otherwise.

A backend name is valid if it is one of the built-in backends or has been dynamically added via an entry point. Those beginning with `module://` are always considered valid and are added to the current list of all backends within this function.

Even if a name is valid, it may not be importable or usable. This can only be determined by loading and using the backend module.

Parameters:

**backend**str

Name of backend.

Returns:

bool

True if backend is valid, False otherwise.

list\_all()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L250-L265)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.list_all "Link to this definition")

Return list of all known backends.

These include built-in backends and those obtained at runtime either from entry points or explicit `module://some.backend` syntax.

Entry points will be loaded if they haven't been already.

Returns:

list of str

Backend names.

list\_builtin(_filter\_\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L267-L289)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.list_builtin "Link to this definition")

Return list of backends that are built into Matplotlib.

Parameters:

**filter\_**[`BackendFilter`](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendFilter "matplotlib.backends.registry.BackendFilter")
, optional

Filter to apply to returned backends. For example, to return only non-interactive backends use [`BackendFilter.NON_INTERACTIVE`](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendFilter.NON_INTERACTIVE "matplotlib.backends.registry.BackendFilter.NON_INTERACTIVE")
.

Returns:

list of str

Backend names.

list\_gui\_frameworks()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L291-L300)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.list_gui_frameworks "Link to this definition")

Return list of GUI frameworks used by Matplotlib backends.

Returns:

list of str

GUI framework names.

load\_backend\_module(_backend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L302-L317)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.load_backend_module "Link to this definition")

Load and return the module containing the specified backend.

Parameters:

**backend**str

Name of backend to load.

Returns:

Module

Module containing backend.

resolve\_backend(_backend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L319-L371)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.resolve_backend "Link to this definition")

Return the backend and GUI framework for the specified backend name.

If the GUI framework is not yet known then it will be determined by loading the backend module and checking the `FigureCanvas.required_interactive_framework` attribute.

This function only loads entry points if they have not already been loaded and the backend is not built-in and not of `module://some.backend` format.

Parameters:

**backend**str or None

Name of backend, or None to use the default backend.

Returns:

**backend**str

The backend name.

**framework**str or None

The GUI framework, which will be None for a backend that is non-interactive.

resolve\_gui\_or\_backend(_gui\_or\_backend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/registry.py#L373-L410)
[#](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.resolve_gui_or_backend "Link to this definition")

Return the backend and GUI framework for the specified string that may be either a GUI framework or a backend name, tested in that order.

This is for use with the IPython %matplotlib magic command which may be a GUI framework such as `%matplotlib qt` or a backend name such as `%matplotlib qtagg`.

This function only loads entry points if they have not already been loaded and the backend is not built-in and not of `module://some.backend` format.

Parameters:

**gui\_or\_backend**str or None

Name of GUI framework or backend, or None to use the default backend.

Returns:

**backend**str

The backend name.

**framework**str or None

The GUI framework, which will be None for a backend that is non-interactive.

On this page