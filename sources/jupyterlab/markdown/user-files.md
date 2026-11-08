[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/user/files.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

[![Sponsored: Promoted](https://media.ethicalads.io/images/2026/09/Ethical_1_240x180_wcQNrBm.jpg)](https://server.ethicalads.io/proxy/click/10877/01a1b9a4-dadc-74a3-9ae1-e9bd2b9a236a/)

[See why Rails or Phoenix is slow, down to the line: queries, GC, memory, BEAM metrics.](https://server.ethicalads.io/proxy/click/10877/01a1b9a4-dadc-74a3-9ae1-e9bd2b9a236a/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)
_   ·   [ℹ️](https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads)

Working with Files[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#working-with-files "Link to this heading")

=============================================================================================================================

Opening Files[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#opening-files "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

The file browser and File menu enable you to work with files and folders on your system. This includes opening, creating, deleting, renaming, downloading, copying, and sharing files and folders.

The file browser is in the left sidebar Files tab:

![Arrow pointing to the file browser in the upper left sidebar.](https://jupyterlab.readthedocs.io/en/stable/_images/files-menu-left.png)

Many actions on files can also be carried out in the File menu:

![The File menu open including options like "New", "Save All."](https://jupyterlab.readthedocs.io/en/stable/_images/files-menu-top.png)

To open any file, double-click on its name in the file browser:

You can also drag a file into the main work area to create a new tab:

Many files types have [multiple viewers/editors](https://jupyterlab.readthedocs.io/en/stable/user/file_formats.html#file-and-output-formats)
. For example, you can open a Markdown file in a [text editor](https://jupyterlab.readthedocs.io/en/stable/user/file_editor.html#file-editor)
 or as rendered HTML. A JupyterLab extension can also add new viewers/editors for files. To open a file in a non-default viewer/editor, right-click on its name in the file browser and use the “Open With…” submenu to select the viewer/editor:

A single file can be open simultaneously in multiple viewer/editors and they will remain in sync:

The file system can be navigated by double-clicking on folders in the listing or clicking on the folders at the top of the folder listing:

Right-click on a file or folder and select “Copy Shareable Link” to copy a URL that can be used to open JupyterLab with that file or folder open.

![The Copy Shareable Link option in the context menu of a file. Copy Shareable Link is the last entry on the list.](https://jupyterlab.readthedocs.io/en/stable/_images/files-shareable-link.png)

Right-click on a file or folder and select “Copy Path” to copy the filesystem relative path. This can be used for passing arguments to open files in functions called in various kernels. If you want to copy the filesystem absolute path, you must add the jupyterlab server config `LabServerApp.copy_absolute_path=True` and `ServerApp.root_dir = 'xxx'`.

Creating Files and Activities[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#creating-files-and-activities "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Create new files or activities by clicking the `+` button at the top of the file browser. This will open a new Launcher tab in the main work area, which enables you to pick an activity and kernel:

You can also create new documents or activities using the File menu:

![The context menu entry for creating a new file.](https://jupyterlab.readthedocs.io/en/stable/_images/files-create-text-file.png)

The current working folder of a new activity or document will be the folder listed in the file browser (except for a terminal, which always starts in the root directory of the file browser):

A new file is created with a default name. Rename a file by right-clicking on its name in the file browser and selecting “Rename” from the context menu:

Autosave[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#autosave "Link to this heading")

---------------------------------------------------------------------------------------------------------

JupyterLab automatically saves your files and notebooks every 1 minute (60 seconds) by default.

You can configure this behavior in the **Settings Editor**:

1.  Go to **Settings** → **Settings Editor**.
    
2.  Select **Document Manager** in the left sidebar.
    
3.  Adjust the following settings:
    
    *   **Autosave Documents**: Toggle this checkbox to enable or disable the feature.
        
    *   **Autosave Interval**: Change the frequency by entering a value in **seconds**. (Set to 60 for 1 minute).
        

![The Snapshot of the autosave settings.](https://jupyterlab.readthedocs.io/en/stable/_images/autosave-settings.png)

Uploading and Downloading[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#uploading-and-downloading "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Files can be uploaded to the current folder of the file browser by dragging and dropping files onto the file browser, or by clicking the “Upload Files” button at the top of the file browser:

Any file in JupyterLab can be downloaded by right-clicking its name in the file browser and selecting “Download” from the context menu:

Disabling File Uploads[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#disabling-file-uploads "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

You can disable file uploads in JupyterLab through multiple mechanisms:

**Using the File Browser Settings**

The file browser includes an “Allow file uploads” setting that can be configured in the Settings Editor (Settings → Settings Editor → File Browser), or by adding the following configuration to your settings (Settings → Advanced Settings Editor → File Browser):

{
  "@jupyterlab/filebrowser-extension:browser": {
    "allowFileUploads": false
  }
}

Copy to clipboard

When this setting is disabled, users will not be able to upload files either by clicking the “Upload Files” button or by dragging and dropping files into the file browser.

**Removing the Upload Button via Settings**

You can also remove the upload button entirely in the file browser toolbar by adding the following configuration to your settings (Settings → Advanced Settings Editor → File Browser):

{
  "@jupyterlab/filebrowser-extension:widget": {
    "toolbar": \[\
      {\
        "name": "uploader",\
        "disabled": true\
      }\
    \]
  }
}

Copy to clipboard

This will hide the “Upload” button from the file browser toolbar, but will not prevent drag-and-drop uploads unless the “Allow file uploads” setting is also disabled.

**Combining Both Approaches**

For complete UI-level upload restriction, it is recommended to:

1.  Disable the “Allow file uploads” setting (`allowFileUploads: false`) to prevent both button-based and drag-and-drop uploads in the file browser UI
    
2.  Optionally disable the upload button in the toolbar using the configuration above to remove the UI element entirely
    

Important

**UI-Only Restriction**

These settings only disable the file upload functionality in the JupyterLab user interface. They do not prevent file uploads at the server level. If the Jupyter server allows file uploads through its API, users can still upload files programmatically (e.g., using the Contents API directly, through custom code, or via other clients).

For true upload restriction, you must configure server-side permissions and access controls in addition to these UI settings. Consult the [Jupyter Server documentation](https://jupyter-server.readthedocs.io/)
 for information on server-side security configurations.

Displaying Hidden files[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#displaying-hidden-files "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Hidden files and folders can be displayed in JupyterLab by combining two parameters:

1.  First the server should be allowed to serve hidden files by setting `ContentsManager.allow_hidden = True`; see [server documentation](https://jupyter-server.readthedocs.io/en/latest/users/configuration.html)
    .
    
2.  Then you will be able to display or hide the hidden files through the menu `View` -> `Show Hidden Files`.
    

Single-Click Navigation[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#single-click-navigation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Single-click navigation for files and folders can be enabled via the settings editor under the `File Browser` option: `Navigate files and directories with single click`

Editable Breadcrumbs[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#editable-breadcrumbs "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

You can click on the empty space to the right of the breadcrumb path to enter edit mode. This opens a text input pre-filled with the current path and a completion dropdown that suggests matching subdirectories as you type, allowing you to quickly navigate to any folder.

File name sort order[#](https://jupyterlab.readthedocs.io/en/stable/user/files.html#file-name-sort-order "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

You can choose how file names are ordered when sorting by name in the file browser:

*   **Sort file names naturally** (default, when enabled): Names are ordered in natural order, e.g. `file1.txt`, `file2.txt`, `file10.txt`.
    
*   When disabled: Names are ordered lexicographically, e.g. `file1.txt`, `file10.txt`, `file2.txt`.
    

Change this in **Settings → Settings Editor → File Browser** via the “Sort file names naturally” checkbox, or in **Settings → Advanced Settings Editor → File Browser**:

{
  "@jupyterlab/filebrowser-extension:browser": {
    "sortFileNamesNaturally": true
  }
}

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/user/files.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/user/files.md.txt)