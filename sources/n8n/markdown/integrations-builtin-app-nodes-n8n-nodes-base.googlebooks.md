For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md)
.

Use the Google Books node to automate work in Google Books, and integrate Google Books with other applications. n8n has built-in support for a wide range of Google Books features, including retrieving a specific bookshelf resource for the specified user, adding volume to a bookshelf, and getting volume.

On this page, you'll find a list of operations the Google Books node supports and links to more resources.

**Credentials**

Refer to [Google credentials](https://docs.n8n.io/integrations/builtin/credentials/google)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks#operations)

-------------------------------------------------------------------------------------------------------

*   Bookshelf
    
    *   Retrieve a specific bookshelf resource for the specified user
        
    *   Get all public bookshelf resource for the specified user
        
    
*   Bookshelf Volume
    
    *   Add a volume to a bookshelf
        
    *   Clears all volumes from a bookshelf
        
    *   Get all volumes in a specific bookshelf for the specified user
        
    *   Moves a volume within a bookshelf
        
    *   Removes a volume from a bookshelf
        
    
*   Volume
    
    *   Get a volume resource based on ID
        
    *   Get all volumes filtered by query
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------

[Browse Google Books node documentation integration templates](https://n8n.io/integrations/google-books)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousGoogle BigQuery](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery)
[NextGoogle Business Profile](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile)

Last updated 10 days ago

Was this helpful?