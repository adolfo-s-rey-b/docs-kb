For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md)
.

Use the Mistral Cloud Chat Model node to combine Mistral Cloud's chat models with conversational agents.

On this page, you'll find the node parameters for the Mistral Cloud Chat Model node, and links to more resources.

**Credentials**

Refer to the [Mistral Cloud credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/mistral)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model to use to generate the completion. n8n dynamically loads models from Mistral Cloud and you'll only see the models available to your account.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud#node-options)

-------------------------------------------------------------------------------------------------------------------------------------

*   **Maximum Number of Tokens**: Enter the maximum number of tokens used, which sets the completion length.
    
*   **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
    
*   **Timeout**: Enter the maximum request time in milliseconds.
    
*   **Max Retries**: Enter the maximum number of times to retry a request.
    
*   **Top P**: Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.
    
*   **Enable Safe Mode**: Enable safe mode by injecting a safety prompt at the beginning of the completion. This helps prevent the model from generating offensive content.
    
*   **Random Seed**: Enter a seed to use for random sampling. If set, different calls will generate deterministic results.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Mistral Cloud Chat Model node documentation integration templates](https://n8n.io/integrations/mistral-cloud-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Mistral documentation](https://docs.langchain.com/oss/javascript/integrations/chat/mistral)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousMiniMax Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax)
[NextMoonshot Kimi Chat Model node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot)

Last updated 10 days ago

Was this helpful?