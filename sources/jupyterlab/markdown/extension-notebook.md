[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Promoted](https://media.ethicalads.io/images/2026/09/Ethical_2_240x180.jpg)](https://server.ethicalads.io/proxy/click/10878/01a1b9a4-0a6d-7d52-877c-066650131d5b/)

[AppSignal feeds Claude or Cursor the error, trace, deploy and code. **No more vibe-debugging.**](https://server.ethicalads.io/proxy/click/10878/01a1b9a4-0a6d-7d52-877c-066650131d5b/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

![](https://server.ethicalads.io/proxy/view/10878/01a1b9a4-0a6d-7d52-877c-066650131d5b/)

Notebook[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#notebook "Link to this heading")

=================================================================================================================

Background[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#background "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

A JupyterLab architecture walkthrough from June 16, 2016, provides an overview of the notebook architecture.

The most complicated plugin included in the **JupyterLab application** is the **Notebook plugin**.

The [`NotebookWidgetFactory`](https://jupyterlab.readthedocs.io/en/stable/api/classes/notebook.NotebookWidgetFactory-1.html)
 constructs a new [`NotebookPanel`](https://jupyterlab.readthedocs.io/en/stable/api/classes/notebook.NotebookPanel-1.html)
 from a model and populates the toolbar with default widgets.

Structure of the Notebook plugin[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#structure-of-the-notebook-plugin "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The Notebook plugin provides a model and widgets for dealing with notebook files.

### Model[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#model "Link to this heading")

The [`NotebookModel`](https://jupyterlab.readthedocs.io/en/stable/api/classes/notebook.NotebookModel-1.html)
 contains an observable list of cells.

A [`CellModel`](https://jupyterlab.readthedocs.io/en/stable/api/classes/cells.CellModel-1.html)
 can be:

*   a code cell
    
*   a markdown cell
    
*   raw cell
    

A code cell contains a list of **output models**. The list of cells and the list of outputs can be observed for changes.

#### Cell operations[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#cell-operations "Link to this heading")

The NotebookModel cell list supports single-step operations such as moving, adding, or deleting cells. Compound cell list operations, such as undo/redo, are also supported by the NotebookModel. Right now, undo/redo is only supported on cells and is not supported on notebook attributes, such as notebook metadata. Currently, undo/redo for individual cell input content is supported by the CodeMirror editor’s undo feature. (Note: CodeMirror editor’s undo does not cover cell metadata changes.)

#### Metadata[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#metadata "Link to this heading")

The notebook model and the cell model (i.e. notebook cells) support getting and setting metadata through method `getMetadata`, `setMetadata` and `deleteMetadata` (see [`NotebookModel`](https://jupyterlab.readthedocs.io/en/stable/api/classes/notebook.NotebookModel-1.html)
 and [`CellModel`](https://jupyterlab.readthedocs.io/en/stable/api/classes/cells.CellModel-1.html)
). You can listen for changes in the metadata through the `sharedModel.metadataChanged` attribute (see [cell shared model](https://jupyter-ydoc.readthedocs.io/en/latest/api/interfaces/ISharedBaseCell.html#metadataChanged)
 and [notebook shared model](https://jupyter-ydoc.readthedocs.io/en/latest/api/interfaces/ISharedNotebook.html#metadataChanged)
).

### Notebook widget[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#notebook-widget "Link to this heading")

After the NotebookModel is created, the NotebookWidgetFactory constructs a new NotebookPanel from the model. The NotebookPanel widget is added to the DockPanel. The **NotebookPanel** contains:

*   a [`Toolbar`](https://jupyterlab.readthedocs.io/en/stable/api/classes/ui-components.Toolbar-1.html)
    
*   a [`Notebook`](https://jupyterlab.readthedocs.io/en/stable/api/classes/notebook.Notebook-1.html)
     widget.
    

The NotebookPanel also adds completion logic.

The **Notebook toolbar** maintains a list of widgets to add to the toolbar. The **Notebook widget** contains the rendering of the notebook and handles most of the interaction logic with the notebook itself (such as keeping track of interactions such as selected and active cells and also the current edit/command mode).

The NotebookModel cell list provides ways to do fine-grained changes to the cell list.

#### Higher level actions using NotebookActions[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#higher-level-actions-using-notebookactions "Link to this heading")

Higher-level actions are contained in the [`NotebookActions`](https://jupyterlab.readthedocs.io/en/stable/api/modules/notebook.NotebookActions.html)
 namespace, which has functions, when given a notebook widget, to run a cell and select the next cell, merge or split cells at the cursor, delete selected cells, etc.

#### Widget hierarchy[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#widget-hierarchy "Link to this heading")

A Notebook widget contains a list of [`Cell`](https://jupyterlab.readthedocs.io/en/stable/api/classes/cells.Cell-1.html)
 widgets, corresponding to the cell models in its cell list.

*   Each cell widget contains an [`InputArea`](https://jupyterlab.readthedocs.io/en/stable/api/classes/cells.InputArea-1.html)
    ,
    
    *   which contains a [`CodeEditorWrapper`](https://jupyterlab.readthedocs.io/en/stable/api/classes/codeeditor.CodeEditorWrapper-1.html)
        ,
        
        *   which contains a JavaScript CodeMirror instance.
            

A [`CodeCell`](https://jupyterlab.readthedocs.io/en/stable/api/classes/cells.CodeCell-1.html)
 also contains an [`OutputArea`](https://jupyterlab.readthedocs.io/en/stable/api/classes/outputarea.OutputArea-1.html)
. An OutputArea is responsible for rendering the outputs in the [`OutputAreaModel`](https://jupyterlab.readthedocs.io/en/stable/api/classes/outputarea.OutputAreaModel-1.html)
 list. An OutputArea uses a notebook-specific [`RenderMimeRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/classes/rendermime.RenderMimeRegistry-1.html)
 object to render `display_data` output messages.

The Notebook widget is represented in the DOM with a `<div>` element with CSS classes `jp-Notebook` and `jp-NotebookPanel-notebook`. It contains a sequence of cells widgets.

> *   Code cells have the following DOM structure:
>     
>     ![../_images/code-cell-dom.svg](https://jupyterlab.readthedocs.io/en/stable/_images/code-cell-dom.svg)
> *   Rendered markdown cells have the following DOM structure:
>     
>     ![../_images/rendered-markdown-cell-dom.svg](https://jupyterlab.readthedocs.io/en/stable/_images/rendered-markdown-cell-dom.svg)
> *   Active markdown cells have the following DOM structure:
>     
>     ![../_images/active-markdown-cell-dom.svg](https://jupyterlab.readthedocs.io/en/stable/_images/active-markdown-cell-dom.svg)

Note

The default nbconvert template for the HTML exporter produces the same DOM as the JupyterLab notebook, allowing for the JupyterLab CSS to be used directly. In JupyterLab, input areas are rendered with the CodeMirror, with a custom theme making use of the CSS variables of JupyterLab. In the case of nbconvert, code cells are rendered using the Pygments Python library, which produces static HTML with syntax highlighting. The [jupyterlab\_pygments](https://github.com/jupyterlab/jupyterlab_pygments.git)
 Pygments theme mimics the default CodeMirror theme of JupyterLab.

Note

The SVG figures presenting the DOM structures of the different cell types were produced with Draw.io, and contain the metadata allowing them to be directly opened and edited with Draw.io.

#### Rendering output messages[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#rendering-output-messages "Link to this heading")

A **Rendermime plugin** provides a pluggable system for rendering output messages. Default renderers are provided for markdown, html, images, text, etc. Extensions can register renderers to be used across the entire application by registering a handler and mimetype in the rendermime registry. When a notebook is created, it copies the global Rendermime singleton so that notebook-specific renderers can be added. The ipywidgets widget manager is an example of an extension that adds a notebook-specific renderer, since rendering a widget depends on notebook-specific widget state.

#### Keyboard interaction model[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#keyboard-interaction-model "Link to this heading")

Multiple elements can receive focus in the Notebook: - the main toolbar, - cells, - cell components (editor, toolbar, outputs).

When the focus is outside of the cell input editor, the Notebook switches to so-called “command” mode. In the command mode additional keyboard shortcuts are accessible to the user, enabling quick access to cell- and notebook-specific actions. These shortcuts are only active when the notebook is in command mode and the active element is non-editable, as signalled by absence of `.jp-mod-readWrite` class on the notebook node. This class is set if the active element is editable as ascertained by matching to the `:read-write` pseudo-selector, and accounts for any elements nested in the open shadow DOM, but not for the closed shadow DOM nor non-editable elements with custom key event handlers (such as `<div contenteditable="false" onkeydown="alert()" tabindex="0"></div>`). If your output widget (for example created with `IPython.display.HTML`, or created by your MIME renderer on cell output in a notebook or console) uses closed shadow DOM or non-editable elements with custom key event handlers, you may wish to set `lm-suppress-shortcuts` data attribute on the host element to prevent side-effects from the command-mode actions, e.g:

<div
  contenteditable\="false"
  onkeydown\="alert()"
  tabindex\="1"
  data-lm-suppress-shortcuts\="true"
\>
  Click on me and press "A" with and without "lm-suppress-shortcuts"
</div\>

Copy to clipboard

How to extend the Notebook plugin[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#how-to-extend-the-notebook-plugin "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

We’ll walk through two notebook extensions:

*   adding a button to the toolbar
    
*   adding a widget to the notebook header
    
*   adding an ipywidgets extension
    

### Adding a button to the toolbar[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#adding-a-button-to-the-toolbar "Link to this heading")

Since JupyterLab 3.2, adding toolbar item can be done using a [Toolbar Registry](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html#toolbar-registry)
 and settings. In particular for the notebook, if the button is linked to a new command, you can add a button in the toolbar using the following JSON snippet in your extension settings file:

"jupyter.lab.toolbars": {
  "Notebook": \[ // Widget factory name for which you want to add a toolbar item.\
    // Item with default button widget triggering a command\
    { "name": "run", "command": "runmenu:run" }\
  \]
}

Copy to clipboard

You may add a `rank` attribute to modify the item position (the default value is 50).

### Adding a widget to the notebook header[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#adding-a-widget-to-the-notebook-header "Link to this heading")

Start from the extension template.

pip install "copier~=9" jinja2-time
mkdir myextension
cd myextension
copier copy \--trust https://github.com/jupyterlab/extension-template .

Copy to clipboard

Install the dependencies. Note that extensions are built against the released npm packages, not the development versions.

jlpm add \-D @jupyterlab/notebook @jupyterlab/application @jupyterlab/ui-components @jupyterlab/docregistry @lumino/disposable @lumino/widgets

Copy to clipboard

Copy the following to `src/index.ts`:

import { IDisposable, DisposableDelegate } from '@lumino/disposable';

import { Widget } from '@lumino/widgets';

import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { DocumentRegistry } from '@jupyterlab/docregistry';

import { NotebookPanel, INotebookModel } from '@jupyterlab/notebook';

/\*\*
 \* The plugin registration information.
 \*/
const plugin: JupyterFrontEndPlugin<void\> \= {
  activate,
  id: 'my-extension-name:widgetPlugin',
  description: 'Add a widget to the notebook header.',
  autoStart: true
};

/\*\*
 \* A notebook widget extension that adds a widget in the notebook header (widget below the toolbar).
 \*/
export class WidgetExtension implements DocumentRegistry.IWidgetExtension<
  NotebookPanel,
  INotebookModel
\> {
  /\*\*
   \* Create a new extension object.
   \*/
  createNew(
    panel: NotebookPanel,
    context: DocumentRegistry.IContext<INotebookModel\>
  ): IDisposable {
    const widget \= new Widget({ node: Private.createNode() });
    widget.addClass('jp-myextension-myheader');

    panel.contentHeader.insertWidget(0, widget);
    return new DisposableDelegate(() \=> {
      widget.dispose();
    });
  }
}

/\*\*
 \* Activate the extension.
 \*/
function activate(app: JupyterFrontEnd): void {
  app.docRegistry.addWidgetExtension('Notebook', new WidgetExtension());
}

/\*\*
 \* Export the plugin as default.
 \*/
export default plugin;

/\*\*
 \* Private helpers
 \*/
namespace Private {
  /\*\*
   \* Generate the widget node
   \*/
  export function createNode(): HTMLElement {
    const span \= document.createElement('span');
    span.textContent \= 'My custom header';
    return span;
  }
}

Copy to clipboard

And the following to `style/base.css`:

.jp-myextension-myheader {
  min-height: 20px;
  background-color: lightsalmon;
}

Copy to clipboard

Run the following commands:

pip install \-e .
jupyter-builder develop . \--overwrite
jupyter lab

Copy to clipboard

Open a notebook and observe the new “Header” widget.

### The _ipywidgets_ third party-extension[#](https://jupyterlab.readthedocs.io/en/stable/extension/notebook.html#the-ipywidgets-third-party-extension "Link to this heading")

This discussion will be a bit confusing since we’ve been using the term _widget_ to refer to _lumino widgets_. In the discussion below, _Jupyter interactive widgets_ will be referred to as _ipywidgets_. There is no intrinsic relation between _lumino widgets_ and _Jupyter interactive widgets_.

The _ipywidgets_ extension registers a factory for a notebook _widget_ extension using the [`DocumentRegistry`](https://jupyterlab.readthedocs.io/en/stable/api/classes/docregistry.DocumentRegistry-1.html)
. The `createNew()` function is called with a [`NotebookPanel`](https://jupyterlab.readthedocs.io/en/stable/api/classes/notebook.NotebookPanel-1.html)
 and [`IContext`](https://jupyterlab.readthedocs.io/en/stable/api/interfaces/docregistry.DocumentRegistry.IContext.html)
. The plugin then creates a ipywidget manager (which uses the context to interact the kernel and kernel’s comm manager). The plugin then registers an ipywidget renderer with the notebook instance’s rendermime (which is specific to that particular notebook).

When an ipywidget model is created in the kernel, a comm message is sent to the browser and handled by the ipywidget manager to create a browser-side ipywidget model. When the model is displayed in the kernel, a `display_data` output is sent to the browser with the ipywidget model id. The renderer registered in that notebook’s rendermime is asked to render the output. The renderer asks the ipywidget manager instance to render the corresponding model, which returns a JavaScript promise. The renderer creates a container _lumino widget_ which it hands back synchronously to the OutputArea, and then fills the container with the rendered _ipywidget_ when the promise resolves.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/notebook.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/notebook.md.txt)