For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap.md)
.

Use the IMAP Email node to receive emails using an IMAP email server. This node is a trigger node.

**Credential**

Refer to the [IMAP credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/imap)
 for authentication information for this node.

Operations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#operations)

------------------------------------------------------------------------------------------------------

*   Receive an email
    

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#node-parameters)

----------------------------------------------------------------------------------------------------------------

Configure the node using the following parameters.

### Credential to connect with[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#credential-to-connect-with)

Select or create an [IMAP credential](https://docs.n8n.io/integrations/builtin/credentials/imap)
 to connect to the server with.

### Mailbox Name[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#mailbox-name)

Enter the mailbox from which you want to receive emails.

### Action[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#action)

Choose whether you want an email marked as read when n8n receives it. **None** will leave it marked unread. **Mark as Read** will mark it as read.

### Download Attachments[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#download-attachments)

This toggle controls whether to download email attachments (turned on) or not (turned off). Only set this if necessary, since it increases processing.

### Format[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#format)

Choose the format to return the message in from these options:

*   **RAW**: This format returns the full email message data with body content in the raw field as a base64url encoded string. It doesn't use the payload field.
    
*   **Resolved**: This format returns the full email with all data resolved and attachments saved as binary data.
    
*   **Simple**: This format returns the full email. Don't use it if you want to gather inline attachments.
    

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#node-options)

----------------------------------------------------------------------------------------------------------

You can further configure the node using these **Options**.

### Custom Email Rules[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#custom-email-rules)

Enter custom email fetching rules to determine which emails the node fetches.

Refer to [node-imap's search function criteria](https://github.com/mscdex/node-imap)
 for more information.

### Force Reconnect Every Minutes[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#force-reconnect-every-minutes)

Set an interval in minutes to force reconnection.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------

[Browse Email Trigger (IMAP) node documentation integration templates](https://n8n.io/integrations/email-trigger-imap)
 or [search all templates](https://n8n.io/workflows/)

[PreviousEdit Image](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage)
[NextError Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger)

Last updated 10 days ago

Was this helpful?