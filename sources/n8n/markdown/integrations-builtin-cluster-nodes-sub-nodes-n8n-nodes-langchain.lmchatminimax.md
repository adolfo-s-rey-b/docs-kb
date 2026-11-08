For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax.md)
.

On n8n Cloud, you can use the MiniMax Chat Model node with [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 instead of your own MiniMax API key. Select **Use Gateway credits** in the node's credential field to run the node without a MiniMax account.

Use the MiniMax Chat Model node to use MiniMax's chat models with conversational agents.

On this page, you'll find the node parameters for the MiniMax Chat Model node, and links to more resources.

**Credentials**

Refer to the [MiniMax credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/minimax)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax#node-parameters)

--------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model that generates the completion. Refer to [MiniMax's model documentation](https://platform.minimax.io/docs/guides/models-intro)
     for the available models.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax#node-options)

--------------------------------------------------------------------------------------------------------------------------------

*   **Hide Thinking**: When turned on (default), the node strips `<think>` tags from the model's response. Turn this off to include the model's reasoning in the output.
    
*   **Maximum Number of Tokens**: Enter the maximum number of tokens used, which sets the completion length.
    
*   **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
    
*   **Timeout**: Enter the maximum request time in milliseconds.
    
*   **Max Retries**: Enter the maximum number of times to retry a request.
    
*   **Top P**: Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------------------------

[Browse MiniMax Chat Model node documentation integration templates](https://n8n.io/integrations/minimax-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------

Refer to [MiniMax's documentation](https://platform.minimax.io/docs/guides/models-intro)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousLemonade Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade)
[NextMistral Cloud Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud)

Last updated 10 days ago

Was this helpful?