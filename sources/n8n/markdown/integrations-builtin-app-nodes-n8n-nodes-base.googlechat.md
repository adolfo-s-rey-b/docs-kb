For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md)
.

Use the Google Chat node to automate work in Google Chat, and integrate Google Chat with other applications. n8n has built-in support for a wide range of Google Chat features, including getting membership and spaces, as well as creating and deleting messages.

On this page, you'll find a list of operations the Google Chat node supports and links to more resources.

**Credentials**

Refer to [Google credentials](https://docs.n8n.io/integrations/builtin/credentials/google)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

**Human-in-the-loop for AI tool calls**

This node can be used as a human review step for AI Agent tool calls. When configured this way, the AI Agent will pause and request human approval through this service before executing tools that require oversight. Learn more in [Human-in-the-loop for AI tool calls](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat#operations)

------------------------------------------------------------------------------------------------------

*   Member
    
    *   Get a membership
        
    *   Get all memberships in a space
        
    
*   Message
    
    *   Create a message
        
    *   Delete a message
        
    *   Get a message
        
    *   Send and Wait for Response
        
    *   Update a message
        
    
*   Space
    
    *   Get a space
        
    *   Get all spaces the caller is a member of
        
    

### Waiting for a response[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat#waiting-for-a-response)

By choosing the **Send and Wait for a Response** operation, you can send a message and pause the workflow execution until a person confirms the action or provides more information.

#### Response Type[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat#response-type)

You can choose between the following types of waiting and approval actions:

*   **Approval**: Users can approve or disapprove from within the message.
    
*   **Free Text**: Users can submit a response with a form.
    
*   **Custom Form**: Users can submit a response with a custom form.
    

You can customize the waiting and response behavior depending on which response type you choose. You can configure these options in any of the above response types:

*   **Limit Wait Time**: Whether the workflow will automatically resume execution after a specified time limit. This can be an interval or a specific wall time.
    
*   **Append n8n Attribution**: Whether to mention in the message that it was sent automatically with n8n (turned on) or not (turned off).
    

#### Approval response customization[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat#approval-response-customization)

When using the Approval response type, you can choose whether to present only an approval button or both approval _and_ disapproval buttons.

You can also customize the button labels for the buttons you include.

#### Free Text response customization[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat#free-text-response-customization)

When using the Free Text response type, you can customize the message button label, the form title and description, and the response button label.

#### Custom Form response customization[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat#custom-form-response-customization)

When using the Custom Form response type, you build a form using the fields and options you want.

You can customize each form element with the settings outlined in the [n8n Form trigger's form elements](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger#form-elements)
. To add more fields, select the **Add Form Element** button.

You'll also be able to customize the message button label, the form title and description, and the response button label.

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------

[Browse Google Chat node documentation integration templates](https://n8n.io/integrations/google-chat)
 or [search all templates](https://n8n.io/workflows/)

[PreviousEvent operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations)
[NextGoogle Cloud Firestore](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudfirestore)

Last updated 10 days ago

Was this helpful?