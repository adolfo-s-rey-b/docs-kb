For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai.md)
.

Use the Mistral AI node to automate work in Mistral AI and integrate Mistral AI with other applications. n8n has built-in support for extracting text with various models, file types, and input methods.

On this page, you'll find a list of operations the Mistral AI node supports, and links to more resources.

**Credentials**

Refer to the [Mistral Cloud credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/mistral)
 for authentication information for this node.

Node parameters[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai#node-parameters)

---------------------------------------------------------------------------------------------------------------

*   **Resource**: The resource that Mistral AI should operate on. The current implementation supports the "Document" resource.
    
*   **Operation**: The operation to perform:
    
    *   **Extract Text**: Extracts text from a document or image using optical character recognition (OCR).
        
    
*   **Model**: The model to use for the given operation. The current version requires the `mistral-ocr-latest` model.
    
*   **Document Type**: The document format to process. Can be "Document" or "Image".
    
*   **Input Type**: How to input the document:
    
    *   **Binary Data**: Pass the document to this node as a binary field.
        
    *   **URL**: Fetch the document from a given URL.
        
    
*   **Input Binary Field**: When using the "Binary Data" input type, defines the name of the input binary field containing the file.
    
*   **URL**: When using the "URL" input type, the URL of the document or image to process.
    

Node options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai#node-options)

---------------------------------------------------------------------------------------------------------

*   **Enable Batch Processing**: Whether to process multiple documents in the same API call. This may reduce your costs by bundling requests.
    
*   **Batch Size**: When using "Enable Batch Processing", sets the maximum number of documents to process per batch.
    
*   **Delete Files After Processing**: When using "Enable Batch Processing", whether to delete the files from Mistral Cloud after processing.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------

[Browse MistralAI node documentation integration templates](https://n8n.io/integrations/mistral-ai)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai#related-resources)

-------------------------------------------------------------------------------------------------------------------

Refer to [Mistral AI's documentation](https://docs.mistral.ai/api/)
 for more information about the service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousMISP](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp)
[NextMiniMax](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.minimax)

Last updated 10 days ago

Was this helpful?