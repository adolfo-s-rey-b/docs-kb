For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant.md)
.

Ask n8n AI helps you build, debug, and optimize your workflows. From answering questions about n8n to providing help with coding and expressions, Ask n8n AI supports you as you navigate n8n's capabilities.

Ask n8n AI is n8n's built-in help assistant and is no longer actively developed. To build, edit, and run workflows from a chat, see [Use n8n Assistant](https://docs.n8n.io/build/ways-of-building-workflows/n8n-assistant)
.

Current capabilities[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#current-capabilities)

-----------------------------------------------------------------------------------------------------------------------

Ask n8n AI offers a range of tools to support you:

*   **Debug helper**: Identify and troubleshoot node execution issues in your workflows to keep them running without issues.
    
*   **Answer n8n questions**: Get instant answers to your n8n-related questions, whether they're about specific features or general functionality.
    
*   **Coding support**: Receive guidance on coding, including SQL and JSON, to optimize your nodes and data processing.
    
*   **Expression assistance**: Learn how to create and refine [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
     to get the most out of your workflows.
    
*   **Credential setup tips**: Find out how to set up and manage node [credentials](https://docs.n8n.io/integrations/builtin/credentials)
     securely and efficiently.
    

Tips for getting the most out of the Assistant[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#tips-for-getting-the-most-out-of-the-assistant)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  **Engage in a conversation**: Ask n8n AI can collaborate with you step-by-step. If a suggestion isn't what you need, let it know! The more context you provide, the better the recommendations will be.
    
2.  **Ask specific questions**: For the best results, ask focused questions (for example, "How do I set up credentials for Google Sheets?"). The assistant works best with clear queries.
    
3.  **Iterate on suggestions**: Don't hesitate to build on the assistant's responses. Try different approaches and keep refining based on the assistant's feedback to get closer to your ideal solution.
    
4.  **Things to try out**:
    
    *   Debug any error you're seeing
        
    *   Ask how to setup credentials
        
    *   "Explain what this workflow does."
        
    *   "I need your help to write code: \[Explain your code here\]"
        
    *   "How can I build X in n8n?"
        
    

AI usage settings[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#ai-usage-settings)

-----------------------------------------------------------------------------------------------------------------

**Feature availability**

AI usage settings are available from n8n 2.7.0.

You can manage your AI usage settings by navigating to **Settings** > **AI Usage** in your n8n instance. Here, you can control what data is shared with Ask n8n AI.

These settings are only available to the instance owners and administrators, and will apply to all users on the instance.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-135bf4355bf2b890ed95da70f2c0365608dfbdc7%252Fai_usage_settings.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=791fc10f709612a364b2970bfe1659ec&sv=3)

AI Usage settings page with the Send actual data values checkbox

Choose whether to share actual workflow data (like node names, parameters, and structure) with Ask n8n AI. Disabling this option will limit the assistant's ability to provide context-aware help based on your workflows.

Since access to workflow data is essential for the AI Workflow builder to function, **disabling this option will also disable the AI Workflow builder feature**.

### Disable sending data[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#disable-sending-data)

To stop sending actual data values to Ask n8n AI, turn off the **Send actual data values** checkbox on the **AI Usage** settings page.

FAQs[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#faqs)

---------------------------------------------------------------------------------------

### What context does the Assistant have?[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#what-context-does-the-assistant-have)

Ask n8n AI has access to all elements displayed on your n8n screen, excluding actual input and output data values (like customer information). To learn more about what data n8n shares with Ask n8n AI, refer to [AI in n8n](https://docs.n8n.io/privacy-and-security#ai-in-n8n)
.

### Who can use the Assistant?[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#who-can-use-the-assistant)

The assistant is available on all n8n Cloud plans. It isn't available on self-hosted.

### How does the Assistant work?[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#how-does-the-assistant-work)

The underlying logic of the assistant is build with the advanced AI capabilities of n8n. It uses a combination of different agents, specialized in different areas of n8n, RAG to gather knowledge from the docs and the community forum, and custom prompts, memory and context.

Related resources[](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant#related-resources)

-----------------------------------------------------------------------------------------------------------------

*   [Ways of building workflows](https://docs.n8n.io/build/ways-of-building-workflows)
    
*   [Use n8n Assistant](https://docs.n8n.io/build/ways-of-building-workflows/n8n-assistant)
    
*   [Use n8n MCP server](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server)
    
*   [Use templates](https://docs.n8n.io/build/ways-of-building-workflows/use-templates)
    
*   [Use Chat Hub](https://docs.n8n.io/build/ways-of-building-workflows/chat-hub)
    

[PreviousUse templates](https://docs.n8n.io/build/ways-of-building-workflows/use-templates)
[NextUse Chat Hub](https://docs.n8n.io/build/ways-of-building-workflows/chat-hub)

Last updated 10 days ago

Was this helpful?