For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger.md)
.

[Gmail](https://www.gmail.com/)
 is an email service developed by Google. The Gmail Trigger node can start a workflow based on events in Gmail.

**Credentials**

Refer to the [Google credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/google)
 for authentication information for this node.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Gmail Trigger integrations](https://n8n.io/integrations/gmail-trigger/)
 page.

Events[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger#events)

----------------------------------------------------------------------------------------------------

*   **Message Received**: The node triggers for new messages at the selected **Poll Time**.
    

Node parameters[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger#node-parameters)

----------------------------------------------------------------------------------------------------------------------

Configure the node with these parameters:

*   **Credential to connect with**: Select or create a new Google credential to use for the trigger. Refer to [Google credentials](https://docs.n8n.io/integrations/builtin/credentials/google)
     for more information on setting up a new credential.
    
*   **Poll Times**: Select a poll **Mode** to set how often to trigger the poll. Your **Mode** selection will add or remove relevant fields. Refer to [Poll Mode options](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/poll-mode-options)
     to configure the parameters for each mode type.
    
*   **Simplify**: Choose whether to return a simplified version of the response (turned on, default) or the raw data (turned off).
    
    *   The simplified version returns email message IDs, labels, and email headers, including: From, To, CC, BCC, and Subject.
        
    
*   **Max Emails per Poll**: Enter the maximum number of emails the node fetches per poll cycle. The default is 10, with a maximum of 50. If there are more unread emails than the limit, the node queues the remaining emails and fetches them in the next poll cycle.
    

Node filters[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger#node-filters)

----------------------------------------------------------------------------------------------------------------

Use these filters to further refine the node's behavior:

*   **Include Spam and Trash**: Select whether the node should trigger on new messages in the Spam and Trash folders (turned on) or not (turned off).
    
*   **Label Names or IDs**: Only trigger on messages with the selected labels added to them. Select the Label names you want to apply or enter an expression to specify IDs. The dropdown populates based on the **Credential** you selected.
    
*   **Search**: Enter Gmail search refine filters, like `from:`, to trigger the node on the filtered conditions only. Refer to [Refine searches in Gmail](https://support.google.com/mail/answer/7190?hl=en)
     for more information.
    
*   **Read Status**: Choose whether to receive **Unread and read emails**, **Unread emails only** (default), or **Read emails only**.
    
*   **Sender**: Enter an email or a part of a sender name to trigger only on messages from that sender.
    

Related resources[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger#related-resources)

--------------------------------------------------------------------------------------------------------------------------

n8n provides an app node for Gmail. Refer to the [Gmail node documentation](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail)
 for more information.

View [example workflows and related content](https://n8n.io/integrations/gmail-trigger/)
 on n8n's website.

Refer to [Google's Gmail API documentation](https://developers.google.com/gmail/api/guides)
 for details about their API.

Common issues[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger#common-issues)

------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/common-issues)
.

[PreviousGitLab Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger)
[NextPoll mode options](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/poll-mode-options)

Last updated 10 days ago

Was this helpful?