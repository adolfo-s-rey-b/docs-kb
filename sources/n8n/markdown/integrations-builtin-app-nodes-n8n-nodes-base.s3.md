For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3.md)
.

Use the S3 node to automate work in non-AWS S3 storage and integrate S3 with other applications. n8n has built-in support for a wide range of S3 features, including creating, deleting, and getting buckets, files, and folders. For AWS S3, use [AWS S3](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3)
.

Use the S3 node for non-AWS S3 solutions like:

*   [MinIO](https://min.io/)
    
*   [Wasabi](https://wasabi.com/)
    
*   [Digital Ocean spaces](https://www.digitalocean.com/products/spaces)
    

On this page, you'll find a list of operations the S3 node supports and links to more resources.

**Credentials**

Refer to [S3 credentials](https://docs.n8n.io/integrations/builtin/credentials/s3)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3#operations)

----------------------------------------------------------------------------------------------

*   Bucket
    
    *   Create a bucket
        
    *   Delete a bucket
        
    *   Get all buckets
        
    *   Search within a bucket
        
    
*   File
    
    *   Copy a file
        
    *   Delete a file
        
    *   Download a file
        
    *   Get all files
        
    *   Upload a file
        
    
    **Attach file for upload**
    
    To attach a file for upload, use another node to pass the file as a data property. Nodes like the [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile)
     node or the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
     work well.
    
*   Folder
    
    *   Create a folder
        
    *   Delete a folder
        
    *   Get all folders
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------

[Browse S3 node documentation integration templates](https://n8n.io/integrations/s3)
 or [search all templates](https://n8n.io/workflows/)

Node reference[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3#node-reference)

------------------------------------------------------------------------------------------------------

### Setting file permissions in Wasabi[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3#setting-file-permissions-in-wasabi)

When uploading files to [Wasabi](https://wasabi.com/)
, you must set permissions for the files using the **ACL** dropdown and not the toggles.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-8ff470fdadd5e040061cb2bea4f23d741e1bcfa0%252Facl_dropdown.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b005488840128f0e40f05e0b88767070&sv=3)

File permissions when using the S3 node with Wasabi

[PreviousRundeck](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.rundeck)
[NextSalesforce](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce)

Last updated 10 days ago

Was this helpful?