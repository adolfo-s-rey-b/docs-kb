For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md)
.

The Call n8n Workflow Tool node is a tool that allows an agent to run another n8n workflow and fetch its output data.

On this page, you'll find the node parameters for the Call n8n Workflow Tool node, and links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------

### Description[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow#description)

Enter a custom code a description. This tells the agent when to use this tool. For example:

> Call this tool to get a random color. The input should be a string with comma separated names of colors to exclude.

### Source[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow#source)

Tell n8n which workflow to call. You can choose either:

*   **Database** to select the workflow from a list or enter a workflow ID.
    
*   **Define Below** and copy in a complete [workflow JSON](https://docs.n8n.io/build/manage-workflows/export-and-import)
    .
    

When using **Database** as the workflow source and running the agent in production (not the manual/chat test panel), the sub-workflow must be published. If it isn't, the tool call fails with the error `Workflow is not active and cannot be executed`. The error text is returned to the agent as the tool result. This can be easy to miss inside a longer agent response. If the agent reports it couldn't retrieve data, check that the sub-workflow has been published and that its execution list shows a run.

### Workflow Inputs[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow#workflow-inputs)

When using **Database** as workflow source, once you choose a sub-workflow (and define the **Workflow Input Schema** in the sub-workflow), you can define the **Workflow Inputs**.

Select the **Refresh** button to pull in the input fields from the sub-workflow.

You can define the workflow input values using any combination of the following options:

*   providing fixed values
    
*   using expressions to reference data from the current workflow
    
*   [letting the AI model specify the parameter](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
     by selecting the button AI button on the right side of the field
    
*   using the [`$fromAI()` function](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters#use-the-fromai-function)
     in expressions to control the way the model fills in data and to mix AI generated input with other custom input
    

To reference data from the current workflow, drag fields from the input panel to the field with the Expressions mode selected.

To get started with the `$fromAI()` function, select the "Let the model define this parameter" button on the right side of the field and then use the **X** on the box to revert to user-defined values. The field will change to an expression field pre-populated with the `$fromAI()` expression. From here, you can customize the expression to add other static or dynamic content, or tweak the `$fromAI()` function parameters.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Call n8n Workflow Tool node documentation integration templates](https://n8n.io/integrations/workflow-tool)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's documentation on tools](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
 for more information about tools in LangChain.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousWolfram|Alpha tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha)
[NextReranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)

Last updated 10 days ago

Was this helpful?