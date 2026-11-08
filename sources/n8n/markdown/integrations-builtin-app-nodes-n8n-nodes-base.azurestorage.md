For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage.md)
.

The Azure Storage node has built-in support for a wide range of features, which includes creating, getting, and deleting blobs and containers. Use this node to automate work within the Azure Storage service or integrate it with other services in your workflow.

On this page, you'll find a list of operations the Azure Storage node supports, and links to more resources.

**Credentials**

Refer to the [Azure Storage credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/azurestorage)
 for authentication information for this node.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage#operations)

--------------------------------------------------------------------------------------------------------

*   **Blob**
    
    *   **Create blob**: Create a new blob or replace an existing one.
        
    *   **Delete blob**: Delete an existing blob.
        
    *   **Get blob**: Retrieve data for a specific blob.
        
    *   **Get many blobs**: Retrieve a list of blobs.
        
    
*   **Container**
    
    *   **Create container**: Create a new container.
        
    *   **Delete container**: Delete an existing container.
        
    *   **Get container**: Retrieve data for a specific container.
        
    *   **Get many containers**: Retrieve a list of containers.
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------------

[Browse Azure Storage node documentation integration templates](https://n8n.io/integrations/azure-storage)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage#related-resources)

----------------------------------------------------------------------------------------------------------------------

Refer to [Microsoft's Azure Storage documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/)
 for more information about the service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousAzure Cosmos DB](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb)
[NextBambooHR](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.bamboohr)

Last updated 10 days ago

Was this helpful?