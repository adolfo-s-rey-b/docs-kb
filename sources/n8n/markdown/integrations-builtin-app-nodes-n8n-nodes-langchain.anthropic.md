For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic.md)
.

On n8n Cloud, you can use the Anthropic node with [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 instead of your own Anthropic API key. Select **Use Gateway credits** in the node's credential field to run the node without an Anthropic account.

Use the Anthropic node to automate work in Anthropic and integrate Anthropic with other applications. n8n has built-in support for a wide range of Anthropic features, including analyzing, uploading, getting, and deleting documents, files, and images, and generating, improving, or templatizing prompts.

On this page, you'll find a list of operations the Anthropic node supports, and links to more resources.

**Credentials**

Refer to the [Anthropic credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/anthropic)
 for authentication information for this node.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic#operations)

----------------------------------------------------------------------------------------------------------

*   Document:
    
    *   Analyze Document: Take in documents and answer questions about them.
        
    
*   File:
    
    *   Upload File: Upload a file to the Anthropic API for later user.
        
    *   Get File Metadata: Get metadata for a file from the Anthropic API.
        
    *   List Files: List files from the Anthropic API.
        
    *   Delete File: Delete a file from the Anthropic API.
        
    
*   Image:
    
    *   Analyze Image: Take in images and answer questions about them.
        
    
*   Prompt:
    
    *   Generate Prompt: Generate a prompt for a model.
        
    *   Improve Prompt: Improve a prompt for a model.
        
    *   Templatize Prompt: Templatize a prompt for a model.
        
    
*   Text:
    
    *   Message a Model: Create a completion with an Anthropic model.
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------

[Browse Anthropic node documentation integration templates](https://n8n.io/integrations/anthropic)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic#related-resources)

------------------------------------------------------------------------------------------------------------------------

Refer to [Anthropic's documentation](https://docs.anthropic.com/en/api/overview)
 for more information about the service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousAMQP Sender](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.amqp)
[NextAPITemplate.io](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.apitemplateio)

Last updated 10 days ago

Was this helpful?