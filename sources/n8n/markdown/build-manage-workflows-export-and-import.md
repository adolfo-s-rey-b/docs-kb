For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/manage-workflows/export-and-import.md)
.

n8n saves workflows in JSON format. You can export your workflows as JSON files or import JSON files into your n8n library. You can export and import workflows in several ways.

**Sharing credentials**

Exported workflow JSON files include [credential](https://docs.n8n.io/key-concept-glossary#credential-n8n)
 names and IDs. While IDs aren't sensitive, the names could be, depending on how you name your credentials. HTTP Request nodes may contain authentication headers when imported from cURL. Remove or anonymize this information from the JSON file before sharing to protect your credentials.

Copy-Paste[](https://docs.n8n.io/build/manage-workflows/export-and-import#copy-paste)

--------------------------------------------------------------------------------------

You can copy and paste a workflow or parts of it by selecting the nodes you want to copy to the clipboard (`Ctrl + c` or `cmd +c`) and pasting it (`Ctrl + v` or `cmd + v`) into the Editor UI.

To select all nodes or a group of nodes, click and drag: ![Select a group of nodes](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-bf41e4ac7244ff99bb3af3bd248b44fe161dd771%252Fselectingnodes.gif%3Falt%3Dmedia&width=300&dpr=3&quality=100&sign=0ada394ad6ee0f554e71d3af3baa41aa&sv=3)

From the Editor UI menu[](https://docs.n8n.io/build/manage-workflows/export-and-import#from-the-editor-ui-menu)

----------------------------------------------------------------------------------------------------------------

From the Canvas header, select the Workflow menu ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=054f3c717b7b07b59bb2cd5fd69cc732&sv=3) to see the following options:

*   **Download**: Downloads your current workflow as a JSON file to your computer.
    
*   **Import from URL**: Imports workflow JSON from a URL, for example, [this workflow JSON file on GitHub](https://raw.githubusercontent.com/n8n-io/self-hosted-ai-starter-kit/refs/heads/main/n8n/demo-data/workflows/srOnR8PAY3u4RSwb.json)
    .
    
*   **Import from File**: Imports a workflow as a JSON file from your computer.
    

From the command line[](https://docs.n8n.io/build/manage-workflows/export-and-import#from-the-command-line)

------------------------------------------------------------------------------------------------------------

### Using the n8n CLI[](https://docs.n8n.io/build/manage-workflows/export-and-import#using-the-n8n-cli)

The `n8n-cli package` commands bundle workflows into a portable `.n8np` file you can import into another instance. See [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
, and [Export a package](https://docs.n8n.io/build/manage-workflows/n8n-packages/export-a-package)
 for the available options. n8n packages are in Preview and may change in future releases.

The n8n CLI is the method n8n recommends for moving workflows between instances from the command line. It runs from any machine with network access, carries the folders, projects, and references a workflow needs, and checks an import before writing anything.

### Using the Server CLI[](https://docs.n8n.io/build/manage-workflows/export-and-import#using-the-server-cli)

*   Export: See the [export commands](https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line#export-entities)
     for exporting workflows or credentials.
    
*   Import: See the [import commands](https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line#import-entities)
     for importing workflows or credentials.
    

n8n recommends the [n8n CLI](https://docs.n8n.io/build/manage-workflows/export-and-import#using-the-n8n-cli)
 over the Server CLI export and import commands for new work. We plan to deprecated Server CLI export and import commands, though this is not yet scheduled.

From the n8n API[](https://docs.n8n.io/build/manage-workflows/export-and-import#from-the-n8n-api)

--------------------------------------------------------------------------------------------------

The n8n API can export and import [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
, which carry workflows along with the folders, projects, and references they need. n8n packages are in Preview and may change in future releases.

To move a single workflow as JSON instead, use the workflow endpoints in the [n8n API](https://docs.n8n.io/connect/n8n-api)
.

Related resources[](https://docs.n8n.io/build/manage-workflows/export-and-import#related-resources)

----------------------------------------------------------------------------------------------------

*   [Manage workflows](https://docs.n8n.io/build/manage-workflows)
    
*   [Configure workflow settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
    
*   [Tag workflows](https://docs.n8n.io/build/manage-workflows/tag-workflows)
    
*   [Favorite items](https://docs.n8n.io/build/manage-workflows/favorite-items)
    
*   [View change history](https://docs.n8n.io/build/manage-workflows/view-change-history)
    
*   [Review workflows](https://docs.n8n.io/build/manage-workflows/workflow-reviews)
    
*   [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
    
*   [Share with others](https://docs.n8n.io/build/manage-workflows/share-with-others)
    

[PreviousReview workflows](https://docs.n8n.io/build/manage-workflows/workflow-reviews)
[Nextn8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)

Last updated 10 days ago

Was this helpful?