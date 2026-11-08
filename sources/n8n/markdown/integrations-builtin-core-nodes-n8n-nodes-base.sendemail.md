For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md)
.

The Send Email node sends emails using an SMTP email server.

**Credential**

Refer to the [Send Email credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/send-email)
 for authentication information for this node.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#node-parameters)

----------------------------------------------------------------------------------------------------------------

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Configure this node using the following parameters.

### Credential to connect with[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#credential-to-connect-with)

Select or create an [SMTP account credential](https://docs.n8n.io/integrations/builtin/credentials/send-email)
 for the node to use.

### Operation[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#operation)

The Send Email node supports the following operations:

*   **Send**: Send an email.
    
*   **Send and Wait for Response**: Send an email and wait for a response from the receiver. This operation pauses the workflow execution until the user submits a response.
    

Choosing **Send and Wait for Response** will activate parameters and options as discussed in [waiting for a response](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#waiting-for-a-response)
.

### From Email[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#from-email)

Enter the email address you want to send the email from. You can also include a name using this format: `Name Name <email@sample.com>`, for example: `Nathan Doe <nate@n8n.io>`.

### To Email[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#to-email)

Enter the email address you want to send the email to. You can also include a name using this format: `Name Name <email@sample.com>`, for example: `Nathan Doe <nate@n8n.io>`. Use a comma to separate multiple email addresses: `first@sample.com, "Name" <second@sample.com>`.

**Email Format**

This email format also applies to the CC and BCC fields.

### Subject[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#subject)

Enter the subject line for the email.

### Email Format[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#email-format)

Select the format to send the email in. This parameter is available when using the **Send** operation. Choose from:

*   **Text**: Send the email in plain-text format.
    
*   **HTML**: Send the email in HTML format.
    
*   **Both**: Send the email in both formats. If you choose this option, the email recipient's client will set which format to display.
    

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#node-options)

----------------------------------------------------------------------------------------------------------

Use these **Options** to further refine the node's behavior.

### Append n8n Attribution[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#append-n8n-attribution)

Set whether to include the phrase `This email was sent automatically with n8n` at the end of the email (turned on) or not (turned off).

### Attachments[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#attachments)

Enter the name of the binary properties that contain data to add as an attachment. Some tips on using this option:

*   Use the [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile)
     node or the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
     node to upload the file to your workflow.
    
*   Add multiple attachments by entering a comma-separated list of binary properties.
    
*   Reference embedded images or other content within the body of an email message, for example `<img src="cid:image_1">`.
    

### CC Email[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#cc-email)

Enter an email address for the `cc:` field.

### BCC Email[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#bcc-email)

Enter an email address for the `bcc:` field.

### Ignore SSL Issues[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#ignore-ssl-issues)

Set whether n8n should ignore failures with TLS/SSL certificate validation (turned on) or enforce them (turned off).

### Reply To[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#reply-to)

Enter an email address for the Reply To field.

Waiting for a response[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#waiting-for-a-response)

------------------------------------------------------------------------------------------------------------------------------

By choosing the **Send and Wait for a Response** operation, you can send an email message and pause the workflow execution until a person confirms the action or provides more information.

### Response Type[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#response-type)

You can choose between the following types of waiting and approval actions:

*   **Approval**: Users can approve or disapprove from within the message.
    
*   **Free Text**: Users can submit a response with a form.
    
*   **Custom Form**: Users can submit a response with a custom form.
    

Different options are available depending on which type you choose.

### Approval parameters and options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#approval-parameters-and-options)

When using the Approval response type, the following options are available:

*   **Type of Approval**: Whether to present only an approval button or both an approval and disapproval buttons.
    
*   **Button Label**: The label for the approval or disapproval button. The default choice is `Approve` and `Decline` for approval and disapproval actions respectively.
    
*   **Button Style**: The style (primary or secondary) for the button.
    

This mode also offers the following options:

*   **Limit Wait Time**: Whether the workflow will automatically resume execution after a specified time limit. This can be an interval or a specific wall time.
    
*   **Append n8n Attribution**: Set whether to include the phrase `This email was sent automatically with n8n` at the end of the email (turned on) or not (turned off).
    

### Free Text parameters and options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#free-text-parameters-and-options)

When using the Free Text response type, the following options are available:

*   **Message Button Label**: The label to use for message button. The default choice is `Respond`.
    
*   **Response Form Title**: The title of the form where users provide their response.
    
*   **Response Form Description**: A description for the form where users provide their response.
    
*   **Response Form Button Label**: The label for the button on the form to submit their response. The default choice is `Submit`.
    
*   **Limit Wait Time**: Whether the workflow will automatically resume execution after a specified time limit. This can be an interval or a specific wall time.
    
*   **Append n8n Attribution**: Set whether to include the phrase `This email was sent automatically with n8n` at the end of the email (turned on) or not (turned off).
    

### Custom Form parameters and options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#custom-form-parameters-and-options)

When using the Custom Form response type, you build a form using the fields and options you want.

You can customize each form element with the settings outlined in the [n8n Form trigger's form elements](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger#form-elements)
. To add more fields, select the **Add Form Element** button.

The following options are also available:

*   **Message Button Label**: The label to use for message button. The default choice is `Respond`.
    
*   **Response Form Title**: The title of the form where users provide their response.
    
*   **Response Form Description**: A description for the form where users provide their response.
    
*   **Response Form Button Label**: The label for the button on the form to submit their response. The default choice is `Submit`.
    
*   **Limit Wait Time**: Whether the workflow will automatically resume execution after a specified time limit. This can be an interval or a specific wall time.
    
*   **Append n8n Attribution**: Set whether to include the phrase `This email was sent automatically with n8n` at the end of the email (turned on) or not (turned off).
    

Limitations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#limitations)

--------------------------------------------------------------------------------------------------------

The Send Email (SMTP) node does not support setting headers like `In-Reply-To` and `References`, which are required for email threading. As a result, each email is treated as a new conversation instead of appearing in the same thread.

*   **Workaround**: Use the Gmail node’s **Reply to a message** operation, or a custom node that supports custom headers.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------

[Browse Send Email integration templates](https://n8n.io/integrations/send-email)
 or [search all templates](https://n8n.io/workflows/)

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues)
[NextSort](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort)

Last updated 10 days ago

Was this helpful?