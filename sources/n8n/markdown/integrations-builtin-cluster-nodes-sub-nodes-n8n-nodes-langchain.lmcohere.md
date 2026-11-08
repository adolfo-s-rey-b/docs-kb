For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md)
.

Use the Cohere Model node to use Cohere's models.

On this page, you'll find the node parameters for the Cohere Model node, and links to more resources.

This node lacks tools support, so it won't work with the [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 node. Instead, connect it with the [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)
 node.

**Credentials**

Refer to the [Cohere credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/cohere)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node Options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere#node-options)

---------------------------------------------------------------------------------------------------------------------------

*   **Maximum Number of Tokens**: Enter the maximum number of tokens used, which sets the completion length.
    
*   **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------

[Browse Cohere Model node documentation integration templates](https://n8n.io/integrations/cohere-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Cohere documentation](https://docs.langchain.com/oss/javascript/integrations/llms/cohere)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousxAI Grok Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok)
[NextLemonade Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade)

Last updated 10 days ago

Was this helpful?