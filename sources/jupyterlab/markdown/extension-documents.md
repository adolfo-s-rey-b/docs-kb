[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Documents[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#documents "Link to this heading")

====================================================================================================================

JupyterLab can be extended in several ways:

*   **Extensions (top level)**: Application extensions extend the functionality of JupyterLab itself, and we cover them in the [Develop Extensions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html#developer-extensions)
    .
    
*   **Document widget extensions (lower level):** Document widget extensions extend the functionality of document widgets added to the application, and we cover them in this section.
    

For this section, the term ‘document’ refers to any visual thing that is backed by a file stored on disk (i.e. uses Contents API).

Overview of document architecture[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#overview-of-document-architecture "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

A ‘document’ in JupyterLab is represented by a model instance implementing the [`IModel`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/docregistry.DocumentRegistry.IModel.html)
 interface. The model interface is intentionally fairly small, and concentrates on representing the data in the document and signaling changes to that data. Each model has an associated [`IContext`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/docregistry.DocumentRegistry.IContext.html)
 instance as well. The context for a model is the bridge between the internal data of the document, stored in the model, and the file metadata and operations possible on the file, such as save and revert. Since many objects will need both the context and the model, the context contains a reference to the model as its `.model` attribute.

A single file path can have multiple different models (and hence different contexts) representing the file. For example, a notebook can be opened with a notebook model and with a text model. Different models for the same file path do not directly communicate with each other.

Models contain an instance of [ISharedDocument](https://jupyter-ydoc.readthedocs.io/en/latest/api/interfaces/ISharedDocument.html)
 that acts as data storage for the model’s content. As of JupyterLab 4, the default data storage implementation is a [YDocument](https://jupyter-ydoc.readthedocs.io/en/latest/api/classes/YDocument.html)
 based on [Yjs](https://docs.yjs.dev/)
, a high-performance CRDT for building collaborative applications. Both the interface and the implementation are provided by the package [@jupyter/ydoc](https://github.com/jupyter-server/jupyter_ydoc)
.

[`DocumentWidget`](https://jupyterlab.readthedocs.io/en/stable/api/classes/docregistry.DocumentWidget-1.html)
 represent a view of a document model. There can be multiple document widgets associated with a single document model, and they naturally stay in sync with each other since they are views on the same underlying data model.

The [`DocumentRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/classes/docregistry.DocumentRegistry-1.html)
 is where document types and factories are registered. Plugins can require a document registry instance and register their content types and providers.

The [`DocumentManager`](https://jupyterlab.readthedocs.io/en/stable/api/classes/docmanager.DocumentManager-1.html)
 uses the Document Registry to create models and widgets for documents. The Document Manager handles the lifecycle of documents for the application.

Document Registry[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#document-registry "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

_Document widget extensions_ in the JupyterLab application can register:

*   file types
    
*   model factories for specific file types
    
*   widget factories for specific model factories
    
*   widget extension factories
    

Note

We recommend you to look at the [document example](https://github.com/jupyterlab/extension-examples/tree/main/documents)
 to help understanding a practical case.

### Widget Factories[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#widget-factories "Link to this heading")

Widget Factories (see [`DocumentRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/classes/docregistry.DocumentRegistry-1.html)
 `addWidgetFactory` method) create a widget for a given file.

If multiple widget factories are associated with the same file type, the user will be able to choose one of them using “Open with” list in the context menu of the file browser.

Added in version 4.4: Widget factories now can accept a `contentProviderId` parameter allowing the widgets to modify the way the content is provisioned. For example, using a custom provider enables fetching the document content in chunks rather than all at once.

_Example_

*   The notebook widget factory that creates NotebookPanel widgets.
    

### Model Factories[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#model-factories "Link to this heading")

Model Factories (see [`DocumentRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/classes/docregistry.DocumentRegistry-1.html)
 `addModelFactory` method) create a model for a given file.

Models are generally differentiated by the contents options used to fetch the model (e.g. text, base64, notebook).

### Widget Extension Factories[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#widget-extension-factories "Link to this heading")

Widget Extension Factories (see [`DocumentRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/classes/docregistry.DocumentRegistry-1.html)
 `addWidgetExtension` method) add additional functionality to a widget type. An extension instance is created for each widget instance, enabling the extension to add functionality to each widget or observe the widget and/or its context.

_Examples_

*   The ipywidgets extension that is created for NotebookPanel widgets.
    
*   Adding a button to the toolbar of each NotebookPanel widget.
    

### File Types[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#file-types "Link to this heading")

File Types (see [`DocumentRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/classes/docregistry.DocumentRegistry-1.html)
 `addFileType` method) add a new file type to be understood through a mimetype and file extensions within JupyterLab.

### Document Models[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#document-models "Link to this heading")

[`IModel`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/docregistry.DocumentRegistry.IModel.html)
 instances are created by the model factories and passed to widget factories and widget extension factories. Models are the way in which we interact with the data of a document. For a simple text file, we typically only use the `to/fromString()` methods. A more complex document like a Notebook contains more points of interaction like the Notebook metadata.

### Document Contexts[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#document-contexts "Link to this heading")

[`IContext`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/docregistry.DocumentRegistry.IContext.html)
 instances are created by the Document Manager and passed to widget factories and widget extensions. The context contains the model as one of its properties so that we can pass a single object around.

They are used to provide an abstracted interface to the session and Contents API from `@jupyterlab/services` for the given model. They can be shared between widgets.

The reason for a separate context and model is so that it is easy to create model factories and the heavy lifting of the context is left to the Document Manager. Contexts are not meant to be subclassed or re-implemented. Instead, the contexts are intended to be the glue between the document model and the wider application.

Shared Models[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#shared-models "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

The `@jupyter/ydoc` package contains an [ISharedNotebook](https://jupyter-ydoc.readthedocs.io/en/latest/api/modules/ISharedNotebook.html)
 and an [ISharedFile](https://jupyter-ydoc.readthedocs.io/en/latest/api/interfaces/ISharedFile.html)
 which are the abstract interfaces to work against if you want to manipulate a notebook or a text file.

These models wrap a [Yjs document (Y.Doc)](https://docs.yjs.dev/api/y.doc)
 which represents a shared document between clients and hold multiple shared objects. They enable you to share different [data types like text, Array, Map or set](https://docs.yjs.dev/getting-started/working-with-shared-types)
, to make different types of collaborative applications.

In addition, a shared model has an [Awareness](https://docs.yjs.dev/getting-started/adding-awareness)
 attribute. This attribute is linked to the _Y.Doc_ which means there is one _Awareness_ object per document and is used for sharing cursor locations and presence information. The `Awareness` is an implementation detail of Yjs and is not part of the `ISharedDocument` interface.

Please, check out the [@jupyter/ydoc documentation](https://jupyter-ydoc.readthedocs.io/en/latest)
 to know more about this package.

Document Manager[#](https://jupyterlab.readthedocs.io/en/stable/extension/documents.html#document-manager "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The _Document Manager_ handles:

*   document models
    
*   document contexts
    

The _File Browser_ uses the _Document Manager_ to open documents and manage them.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/documents.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/documents.md.txt)