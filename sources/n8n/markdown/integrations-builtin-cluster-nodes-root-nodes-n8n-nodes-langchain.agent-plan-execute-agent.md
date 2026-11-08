For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent.md)
.

**Feature availability**

The Plan and Execute Agent is deprecated from n8n 1.82.0. New or updated AI Agent nodes use the [Tools Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)
 instead. Only workflows still using node version 1 of the AI Agent node can select the Plan and Execute Agent.

Node version 1 of the AI Agent node is removed from n8n 3.0, so the Plan and Execute Agent stops working for all workflows. See [n8n 3.0 breaking changes](https://docs.n8n.io/changelog/v30-breaking-changes)
 for details.

The Plan and Execute Agent is like the [ReAct agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent)
 but with a focus on planning. It first creates a high-level plan to solve the given task and then executes the plan step by step. This agent is most useful for tasks that require a structured approach and careful planning.

Refer to [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 for more information on the AI Agent node itself.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent#node-parameters)

--------------------------------------------------------------------------------------------------------------------------------------------------

Configure the Plan and Execute Agent using the following parameters.

### Prompt[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent#prompt)

Select how you want the node to construct the prompt (also known as the user's query or input from the chat).

Choose from:

*   **Take from previous node automatically**: If you select this option, the node expects an input from a previous node called `chatInput`.
    
*   **Define below**: If you select this option, provide either static text or an expression for dynamic content to serve as the prompt in the **Prompt (User Message)** field.
    

### Require Specific Output Format[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent#require-specific-output-format)

This parameter controls whether you want the node to require a specific output format. When turned on, n8n prompts you to connect one of these output parsers to the node:

*   [Auto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing)
    
*   [Item List Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist)
    
*   [Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent#node-options)

--------------------------------------------------------------------------------------------------------------------------------------------

Refine the Plan and Execute Agent node's behavior using these options:

### Human Message Template[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent#human-message-template)

Enter a message that n8n will send to the agent during each step execution.

Available LangChain expressions:

*   `{previous_steps}`: Contains information about the previous steps the agent's already completed.
    
*   `{current_step}`: Contains information about the current step.
    
*   `{agent_scratchpad}`: Information to remember for the next iteration.
    

### Tracing Metadata[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent#tracing-metadata)

Add custom key-value metadata to tracing events for this agent. This is useful for filtering and debugging runs in tracing tools like [LangSmith](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n#use-langsmith-with-a-self-hosted-n8n-instance)
.

Entries with empty keys or values are ignored.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Refer to the main AI Agent node's [Templates and examples](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent#templates-and-examples)
 section.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent#common-issues)

----------------------------------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues)
.

[PreviousOpenAI Functions Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent)
[NextReAct Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent)

Last updated 10 days ago

Was this helpful?