For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes.md)
.

One of the most complex parts of setting up API calls is managing authentication. n8n provides [credentials](https://docs.n8n.io/key-concept-glossary#credential-n8n)
 support for operations and services beyond those supported by built-in nodes.

*   Custom operations for existing nodes: n8n supplies hundreds of nodes to create workflows that link multiple products. However, some nodes don't include all the possible operations supported by a product's API. You can work around this by making a custom API call using the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
     node.
    
*   Credential-only nodes: n8n includes credential-only nodes. These are integrations where n8n supports setting up credentials for use in the HTTP Request node, but doesn't provide a standalone node. You can find a credential-only node in the nodes panel, as you would for any other integration.
    

Predefined credential types[](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes#predefined-credential-types)

------------------------------------------------------------------------------------------------------------------------------------------

A predefined credential type is a credential that already exists in n8n. You can use predefined credential types instead of generic credentials in the HTTP Request and GraphQL nodes.

For example: you create an Asana credential, for use with the Asana node. Later, you want to perform an operation that isn't supported by the Asana node, using Asana's API. You can use your existing Asana credential in the HTTP Request node to perform the operation, without additional authentication setup.

### Using predefined credential types[](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes#using-predefined-credential-types)

To use a predefined credential type:

1.  Open your HTTP Request or GraphQL node, or add a new one to your workflow.
    
2.  In **Authentication**, select **Predefined Credential Type**.
    
3.  In **Credential Type**, select the API you want to use.
    
4.  In **Credential for** `**<API name>**`, you can:
    
    1.  Select an existing credential for that platform, if available.
        
    2.  Select **Create New** to create a new credential.
        
    

### Credential scopes[](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes#credential-scopes)

Some existing credential types have specific scopes: the parts of the API they can access. n8n warns you about this when you select the credential type.

For example, follow the steps in [Using predefined credential types](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes#using-predefined-credential-types)
, and select **Google Calendar OAuth2 API** as your **Credential Type**. n8n displays a box listing the two scopes this credential type covers: `calendar` and `calendar.events`.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-f3d16a279c43fed8940226a3e1a32b6e18e1d238%252Fscopes.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9ce44372be3795ce75f2759053b10c5e&sv=3)

Scopes notice for the Google Calendar OAuth2 API credential type

[PreviousZulip credentials](https://docs.n8n.io/integrations/builtin/credentials/zulip)
[NextHandle rate limits](https://docs.n8n.io/integrations/builtin/handle-rate-limits)

Last updated 10 days ago

Was this helpful?