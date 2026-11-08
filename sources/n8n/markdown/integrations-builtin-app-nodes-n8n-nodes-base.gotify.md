For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify.md)
.

Use the Gotify node to automate work in Gotify, and integrate Gotify with other applications. n8n has built-in support for a wide range of Gotify features, including creating, deleting, and getting messages.

On this page, you'll find a list of operations the Gotify node supports and links to more resources.

**Credentials**

Refer to [Gotify credentials](https://docs.n8n.io/integrations/builtin/credentials/gotify)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify#operations)

--------------------------------------------------------------------------------------------------

*   Message
    
    *   Create
        
    *   Delete
        
    *   Get All
        
    

Create message[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify#create-message)

----------------------------------------------------------------------------------------------------------

When creating a message, you can configure the following:

### Additional fields[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify#additional-fields)

*   **Priority**: The priority of the message (default: 1)
    
*   **Title**: The title of the message
    

### Options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify#options)

*   **Content Type**: The message content type. Choose between:
    
    *   **Plain**: The message renders as plain text (default)
        
    *   **Markdown**: The message renders as markdown
        
    
*   **Click URL**: Opens this URL when you click the notification
    
*   **Big Image URL**: Shows a big image in the notification
    
*   **Intent URL**: Opens an intent URL after the notification is delivered (Android only)
    

/// note | Message extras The **Options** fields (**Click URL**, **Big Image URL**, **Intent URL**) use Gotify's message extras feature. These allow you to customize how notifications are displayed and behave in Gotify clients. Refer to [Gotify's message extras documentation](https://gotify.net/docs/msgextras)
{:target="\_blank" .external-link} for more details. ///

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify#templates-and-examples-1)

----------------------------------------------------------------------------------------------------------------------------

[Browse Gotify node documentation integration templates](https://n8n.io/integrations/gotify)
 or [search all templates](https://n8n.io/workflows/)

[PreviousGoogle Workspace Admin](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin)
[NextGoToWebinar](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotowebinar)

Last updated 10 days ago

Was this helpful?