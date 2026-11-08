For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows.md)
.

This is a workflow that tries to answer user queries using the standard GPT-4 model. If it can't answer, it sends a message to Slack to ask for human help. It prompts the user to supply an email address.

This workflow uses the [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
 to provide the chat interface, and the [Call n8n Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow)
 to call a second workflow that handles checking for email addresses and sending the Slack message.

Key features[](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows#key-features)

----------------------------------------------------------------------------------------------------------------------

This workflow uses:

*   [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
    : start your workflow and respond to user chat interactions. The node provides a customizable chat interface.
    
*   [Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
    : the key piece of the AI workflow. The Agent interacts with other components of the workflow and makes decisions about what tools to use.
    
*   [Call n8n Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow)
    : plug in n8n workflows as custom tools. In AI, a tool is an interface the AI can use to interact with the world (in this case, the data provided by your workflow). It allows the AI model to access information beyond its built-in dataset.
    

Using the example[](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows#using-the-example)

--------------------------------------------------------------------------------------------------------------------------------

To load the template into your n8n instance:

1.  Download the workflow JSON file.
    
2.  Open a new workflow in your n8n instance.
    
3.  Copy in the JSON, or select **Workflow menu** ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=0d48cb7a502e001d3f9694f0a8b239bf&sv=3) > **Import from file...**.
    

The example workflows use Sticky Notes to guide you:

*   Yellow: notes and information.
    
*   Green: instructions to run the workflow.
    
*   Orange: you need to change something to make the workflow work.
    
*   Blue: draws attention to a key feature of the example.
    

Related resources[](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows#related-resources)

--------------------------------------------------------------------------------------------------------------------------------

*   [AI examples](https://docs.n8n.io/build/integrate-ai/ai-examples)
    
*   [Use Google Sheets as a data source](https://docs.n8n.io/build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source)
    
*   [Call APIs](https://docs.n8n.io/build/integrate-ai/ai-examples/call-apis)
    
*   [Use website content](https://docs.n8n.io/build/integrate-ai/ai-examples/use-website-content)
    
*   [Human-in-the-loop for tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools)
    
*   [Use AI for parameters](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
    

[PreviousHuman-in-the-loop for tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools)
[NextUse AI for parameters](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)

Last updated 10 days ago

Was this helpful?