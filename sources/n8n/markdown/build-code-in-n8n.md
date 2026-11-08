For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n.md)
.

n8n is a low-code tool. This means you can do a lot without code, then add code when needed.

In this section[](https://docs.n8n.io/build/code-in-n8n#in-this-section)

-------------------------------------------------------------------------

*   [Using the Code node](https://docs.n8n.io/build/code-in-n8n/using-the-code-node)
    : add JavaScript or Python code to your workflow.
    
*   [Get coding help from AI](https://docs.n8n.io/build/code-in-n8n/get-coding-help-from-ai)
    : use GPT to generate code in the Code node.
    
*   [Use built-in shortcuts](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts)
    : reference for n8n's built-in methods and variables for use in expressions and code.
    
*   [Define custom variables](https://docs.n8n.io/build/code-in-n8n/define-custom-variables)
    : store and reuse values across your workflows.
    
*   [Cookbook](https://docs.n8n.io/build/code-in-n8n/cookbook)
    : examples and recipes for common coding tasks.
    

Code in your workflows[](https://docs.n8n.io/build/code-in-n8n#code-in-your-workflows)

---------------------------------------------------------------------------------------

There are two places in your workflows where you can use code:

*   **Expressions**
    
    Use expressions to transform [data](https://docs.n8n.io/build/work-with-data)
     in your nodes. You can use JavaScript in expressions, as well as n8n's [Built-in methods and variables](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts)
    .
    
    [→ Expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    
*   **Code node**
    
    Use the Code node to add JavaScript or Python to your workflow.
    
    [→ Code node](https://docs.n8n.io/build/code-in-n8n/using-the-code-node)
    

Other technical resources[](https://docs.n8n.io/build/code-in-n8n#other-technical-resources)

---------------------------------------------------------------------------------------------

These are features that are relevant to technical users.

### Technical nodes[](https://docs.n8n.io/build/code-in-n8n#technical-nodes)

n8n provides core nodes, which simplify adding key functionality such as API requests, webhooks, scheduling, and file handling.

*   **Write a backend**
    
    The [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
    , [Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook)
    , and [Code](https://docs.n8n.io/build/code-in-n8n/using-the-code-node)
     nodes help you make API calls, respond to webhooks, and write any JavaScript in your workflow.
    
    Use this do things like [Create an API endpoint](https://n8n.io/workflows/1750-creating-an-api-endpoint/)
    .
    
    [→ Core nodes](https://docs.n8n.io/integrations/builtin/core-nodes)
    
*   **Represent complex logic**
    
    You can build complex flows, using nodes like [If](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if)
    , [Switch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch)
    , and [Merge](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge)
     nodes.
    
    [→ Flow logic](https://docs.n8n.io/build/flow-logic)
    

### Other developer resources[](https://docs.n8n.io/build/code-in-n8n#other-developer-resources)

*   **The n8n API**
    
    n8n provides an API, where you can programmatically perform many of the same tasks as you can in the GUI. There's an [n8n API node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n)
     to access the API in your workflows.
    
    [→ API](https://docs.n8n.io/connect/n8n-api)
    
*   **Self-host**
    
    You can self-host n8n. This keeps your data on your own infrastructure.
    
    [→ Hosting](https://docs.n8n.io/deploy/host-n8n)
    
*   **Build your own nodes**
    
    You can build custom nodes, install them on your n8n instance, and publish them to [npm](https://www.npmjs.com/)
    .
    
    [→ Creating nodes](https://docs.n8n.io/connect/create-nodes/overview)
    

Related resources[](https://docs.n8n.io/build/code-in-n8n#related-resources)

-----------------------------------------------------------------------------

*   [Build](https://docs.n8n.io/build)
    
*   [Understand workflows](https://docs.n8n.io/build/understand-workflows)
    
*   [Build and manage agents](https://docs.n8n.io/build/build-and-manage-agents)
    
*   [Ways of building workflows](https://docs.n8n.io/build/ways-of-building-workflows)
    
*   [Manage workflows](https://docs.n8n.io/build/manage-workflows)
    
*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Work with data](https://docs.n8n.io/build/work-with-data)
    
*   [Integrate AI](https://docs.n8n.io/build/integrate-ai)
    
*   [Keyboard shortcuts](https://docs.n8n.io/build/keyboard-shortcuts)
    

[PreviousData tables](https://docs.n8n.io/build/work-with-data/data-tables)
[NextUsing the Code node](https://docs.n8n.io/build/code-in-n8n/using-the-code-node)

Last updated 10 days ago

Was this helpful?