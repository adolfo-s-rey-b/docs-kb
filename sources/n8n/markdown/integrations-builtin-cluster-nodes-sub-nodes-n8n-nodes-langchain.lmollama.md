For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama.md)
.

The Ollama Model node allows you use local Llama 2 models.

On this page, you'll find the node parameters for the Ollama Model node, and links to more resources.

This node lacks tools support, so it won't work with the [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 node. Instead, connect it with the [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)
 node.

**Credentials**

Refer to the [Ollama credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/ollama)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model that generates the completion. Choose from:
    
    *   **Llama2**
        
    *   **Llama2 13B**
        
    *   **Llama2 70B**
        
    *   **Llama2 Uncensored**
        
    

Refer to the Ollama [Models Library documentation](https://ollama.com/library)
 for more information about available models.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama#node-options)

---------------------------------------------------------------------------------------------------------------------------

*   **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
    
*   **Top K**: Enter the number of token choices the model uses to generate the next token.
    
*   **Top P**: Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-langchain.lmollama integration templates](https://n8n.io/integrations/ollama-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Ollama documentation](https://docs.langchain.com/oss/javascript/integrations/llms/ollama)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama#common-issues)

-----------------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/common-issues)
.

### Self-hosted AI Starter Kit[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama#self-hosted-ai-starter-kit)

New to working with AI and using self-hosted n8n? Try n8n's [self-hosted AI Starter Kit](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit)
 to get started with a proof-of-concept or demo playground using Ollama, Qdrant, and PostgreSQL.

[PreviousLemonade Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/common-issues)

Last updated 10 days ago

Was this helpful?