For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jinaai.md)
.

Use the Jina AI node to automate work in Jina AI and integrate Jina AI with other applications. n8n has built-in support for a wide range of Jina AI features.

On this page, you'll find a list of operations the Jina AI node supports, and links to more resources.

**Credentials**

Refer to the [Jina AI credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/jinaai)
 for authentication information for this node.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jinaai#operations)

--------------------------------------------------------------------------------------------------

*   **Reader**:
    
    *   **Read**: Fetches content from a URL and converts it to clean, LLM-friendly formats.
        
    *   **Search**: Performs a web search using Jina AI and returns the top results as clean, LLM-friendly formats.
        
    
*   **Research**:
    
    *   **Deep Research**: Research a topic and generate a structured research report.
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jinaai#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

[Browse Jina AI node documentation integration templates](https://n8n.io/integrations/jina-ai)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jinaai#related-resources)

----------------------------------------------------------------------------------------------------------------

Refer to [Jina AI's reader API documentation](https://r.jina.ai/docs)
 and [Jina AI's search API documentation](https://s.jina.ai/docs)
 for more information about the service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jinaai#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousJenkins](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jenkins)
[NextJira Software](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira)

Last updated 10 days ago

Was this helpful?