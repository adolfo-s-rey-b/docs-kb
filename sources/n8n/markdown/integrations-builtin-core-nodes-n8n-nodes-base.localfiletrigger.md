For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger.md)
.

The Local File Trigger node starts a workflow when it detects changes on the file system. These changes involve a file or folder getting added, changed, or deleted.

**Security considerations**

The Local File Trigger node can introduce significant security risks in environments that operate with untrusted users. Because of this, the node is [disabled](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes#exclude-nodes)
 by default from n8n 2.0.

**Self-hosted n8n only**

This node isn't available on n8n Cloud.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger#node-parameters)

-----------------------------------------------------------------------------------------------------------------------

You can choose what event to watch for using the **Trigger On** parameter.

Changes to a Specific File[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger#changes-to-a-specific-file)

---------------------------------------------------------------------------------------------------------------------------------------------

The node triggers when the specified file changes.

Enter the path for the file to watch in **File to Watch**.

Changes Involving a Specific Folder[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger#changes-involving-a-specific-folder)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The node triggers when a change occurs in the selected folder.

Configure these parameters:

*   **Folder to Watch**: Enter the path of the folder to watch.
    
*   **Watch for**: Select the type of change to watch for.
    

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger#node-options)

-----------------------------------------------------------------------------------------------------------------

Use the node **Options** to include or exclude files and folders.

*   **Include Linked Files/Folders**: also watch for changes to linked files or folders.
    
*   **Ignore**: files or paths to ignore. n8n tests the whole path, not just the filename. Supports the [Anymatch](https://github.com/micromatch/anymatch)
     syntax.
    
*   **Max Folder Depth**: how deep into the folder structure to watch for changes.
    

### Examples for Ignore[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger#examples-for-ignore)

Ignore a single file:

Copy

    **/<fileName>.<suffix>
    # For example, **/myfile.txt <a href="#for-example-myfiletxt" id="for-example-myfiletxt"></a>

Ignore a sub-directory of a directory you're watching:

Copy

    **/<directoryName>/**
    # For example, **/myDirectory/** <a href="#for-example-mydirectory" id="for-example-mydirectory"></a>

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------

[Browse Local File Trigger node documentation integration templates](https://n8n.io/integrations/local-file-trigger)
 or [search all templates](https://n8n.io/workflows/)

[PreviousLimit](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit)
[NextLoop Over Items (Split in Batches)](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches)

Last updated 10 days ago

Was this helpful?