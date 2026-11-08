For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues.md)
.

Here are some common errors and issues with the [Structured Output Parser node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)
 and steps to resolve or troubleshoot them.

Processing parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues#processing-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Structured Output Parser node is a sub-node. Sub-nodes behave differently than other nodes when processing multiple items using expressions.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five name values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five name values, the expression `{{ $json.name }}` always resolves to the first name.

Adding the structured output parser node to AI nodes[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues#adding-the-structured-output-parser-node-to-ai-nodes)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can attach output parser nodes to select [AI root nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes)
.

To add the Structured Output Parser to a node, enable the **Require Specific Output Format** option in the AI root node you wish to format. Once the option is enabled, a new **output parser** attachment point is displayed. Click the **output parser** attachment point to add the Structured Output Parser node to the node.

Using the structured output parser to format intermediary steps[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues#using-the-structured-output-parser-to-format-intermediary-steps)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Structured Output Parser node structures the final output from AI agents. It's not intended to structure intermediary output to pass to other AI tools or stages.

To request a specific format for intermediary output, include the response structure in the **System Message** for the **AI Agent**. The message can include either a schema or example response for the agent to use as a template for its results.

Structuring output from agents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues#structuring-output-from-agents)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Structured output parsing is often not reliable when working with [agents](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
.

If your workflow uses agents, n8n recommends using a separate [LLM-chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)
 to receive the data from the agent and parse it. This leads to better, more consistent results than parsing directly in the agent workflow.

[PreviousStructured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)
[NextContextual Compression Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression)

Last updated 10 days ago

Was this helpful?