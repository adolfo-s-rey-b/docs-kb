For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere.md)
.

Use the Cohere Chat Model node to access Cohere's large language models for conversational AI and text generation tasks.

On this page, you'll find the node parameters for the Cohere Chat Model node, and links to more resources.

**Credentials**

Refer to the [Cohere credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/cohere)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model which will generate the completion. n8n dynamically loads available models from the Cohere API. Learn more in the [Cohere model documentation](https://docs.cohere.com/v2/docs/models#command)
    .
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere#node-options)

-------------------------------------------------------------------------------------------------------------------------------

*   **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
    
*   **Max Retries**: Enter the maximum number of times to retry a request.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Cohere Chat Model node documentation integration templates](https://n8n.io/integrations/cohere-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------

Refer to [Cohere's API documentation](https://docs.cohere.com/v2/reference/about)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousMicrosoft Foundry Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai)
[NextDatabricks Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdatabricks)

Last updated 10 days ago

Was this helpful?