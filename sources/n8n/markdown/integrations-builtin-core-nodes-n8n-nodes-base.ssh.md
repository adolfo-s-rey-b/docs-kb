For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh.md)
.

The SSH node is useful for executing commands using the Secure Shell Protocol.

**Credentials**

Refer to the [SSH credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/ssh)
 for authentication information for this node.

Operations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#operations)

------------------------------------------------------------------------------------------------

*   [**Execute** a command](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#execute-command)
    
*   [**Download** a file](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#download-file)
    
*   [**Upload** a file](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#upload-file)
    

**Uploading files**

To attach a file for upload, you will need to use an extra node such as the [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile)
 node or the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 node to pass the file as a data property.

### Execute Command[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#execute-command)

Configure this operation with these parameters:

*   **Credential to connect with**: Select an existing or create a new [SSH credential](https://docs.n8n.io/integrations/builtin/credentials/ssh)
     to connect with.
    
*   **Command**: Enter the command to execute on the remote device.
    
*   **Working Directory**: Enter the directory where n8n should execute the command.
    

### Download File[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#download-file)

*   **Credential to connect with**: Select an existing or create a new [SSH credential](https://docs.n8n.io/integrations/builtin/credentials/ssh)
     to connect with.
    
*   **Path**: Enter the path for the file you want to download. This path must include the file name. The downloaded file will use this file name. To use a different name, use the **File Name** option. Refer to [Download File options](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#download-file-options)
     for more information.
    
*   **File Property**: Enter the name of the object property that holds the binary data you want to download.
    

#### Download File options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#download-file-options)

You can further configure this operation with the **File Name** option. Use this option to override the binary data file name to a name of your choice.

### Upload File[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#upload-file)

*   **Credential to connect with**: Select an existing or create a new [SSH credential](https://docs.n8n.io/integrations/builtin/credentials/ssh)
     to connect with.
    
*   **Input Binary Field**: Enter the name of the input binary field that contains the file you want to upload.
    
*   **Target Directory**: The directory to upload the file to. The name of the file is taken from the binary data file name. To enter a different name, use the **File Name** option. Refer to [Upload File options](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#upload-file-options)
     for more information.
    

#### Upload File options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#upload-file-options)

You can further configure this operation with the **File Name** option. Use this option to override the binary data file name to a name of your choice.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------

[Browse SSH integration templates](https://n8n.io/integrations/ssh)
 or [search all templates](https://n8n.io/workflows/)

[PreviousSSE Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssetrigger)
[NextStop And Error](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror)

Last updated 10 days ago

Was this helpful?