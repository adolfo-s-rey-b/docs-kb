For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp.md)
.

Use the WhatsApp Business Cloud node to automate work in WhatsApp Business, and integrate WhatsApp Business with other applications. n8n has built-in support for a wide range of WhatsApp Business features, including sending messages, and uploading, downloading, and deleting media.

On this page, you'll find a list of operations the WhatsApp Business Cloud node supports and links to more resources.

**Credentials**

Refer to [WhatsApp Business Cloud credentials](https://docs.n8n.io/integrations/builtin/credentials/whatsapp)
 for guidance on setting up authentication.

**Human-in-the-loop for AI tool calls**

This node can be used as a human review step for AI Agent tool calls. When configured this way, the AI Agent will pause and request human approval through this service before executing tools that require oversight. Learn more in [Human-in-the-loop for AI tool calls](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#operations)

----------------------------------------------------------------------------------------------------

*   Message
    
    *   Send
        
    *   Send and Wait for Response
        
    *   Send Template
        
    
*   Media
    
    *   Upload
        
    *   Download
        
    *   Delete
        
    

### Waiting for a response[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#waiting-for-a-response)

By choosing the **Send and Wait for a Response** operation, you can send a message and pause the workflow execution until a person confirms the action or provides more information.

#### Response Type[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#response-type)

You can choose between the following types of waiting and approval actions:

*   **Approval**: Users can approve or disapprove from within the message.
    
*   **Free Text**: Users can submit a response with a form.
    
*   **Custom Form**: Users can submit a response with a custom form.
    

You can customize the waiting and response behavior depending on which response type you choose. You can configure these options in any of the above response types:

*   **Limit Wait Time**: Whether the workflow will automatically resume execution after a specified time limit. This can be an interval or a specific wall time.
    
*   **Append n8n Attribution**: Whether to mention in the message that it was sent automatically with n8n (turned on) or not (turned off).
    

#### Approval response customization[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#approval-response-customization)

When using the Approval response type, you can choose whether to present only an approval button or both approval _and_ disapproval buttons.

You can also customize the button labels for the buttons you include.

#### Free Text response customization[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#free-text-response-customization)

When using the Free Text response type, you can customize the message button label, the form title and description, and the response button label.

#### Custom Form response customization[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#custom-form-response-customization)

When using the Custom Form response type, you build a form using the fields and options you want.

You can customize each form element with the settings outlined in the [n8n Form trigger's form elements](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger#form-elements)
. To add more fields, select the **Add Form Element** button.

You'll also be able to customize the message button label, the form title and description, and the response button label.

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------

[Browse WhatsApp Business Cloud integration templates](https://n8n.io/integrations/whatsapp-business-cloud)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#related-resources)

------------------------------------------------------------------------------------------------------------------

Refer to [WhatsApp Business Platform's Cloud API documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)
 for details about the operations.

Common issues[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#common-issues)

----------------------------------------------------------------------------------------------------------

For common errors or issues and suggested resolution steps, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues)
.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousWekan](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues)

Last updated 10 days ago

Was this helpful?