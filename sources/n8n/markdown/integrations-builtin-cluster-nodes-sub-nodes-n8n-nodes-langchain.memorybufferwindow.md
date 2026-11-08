For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow.md)
.

Use the Simple Memory node to persist chat history in your workflow.

On this page, you'll find a list of operations the Simple Memory node supports, and links to more resources.

**Don't use this node if running n8n in queue mode**

If your n8n instance uses [queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
, this node doesn't work in an active production workflow. This is because n8n can't guarantee that every call to Simple Memory will go to the same worker.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

Configure these parameters to configure the node:

*   **Session Key**: Enter the key to use to store the memory in the workflow data.
    
*   **Context Window Length**: Enter the number of previous interactions to consider for context.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-langchain.memorybufferwindow integration templates](https://n8n.io/integrations/window-buffer-memory)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's short-term memory documentation](https://docs.langchain.com/oss/javascript/langchain/short-term-memory)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow#common-issues)

---------------------------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues)
.

[PreviousChat Memory Manager](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues)

Last updated 10 days ago

Was this helpful?