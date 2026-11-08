For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram.md)
.

Use this object to receive updates when someone comments on the Media objects of your app users; @mentions your app users; or when Stories of your app users expire. Refer to [Facebook Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger)
 for more information on the trigger itself.

**Credentials**

Refer to the [Facebook App credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
 for authentication information for this node.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/)
 page.

Trigger configuration[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram#trigger-configuration)

-----------------------------------------------------------------------------------------------------------------------------------------------

To configure the trigger with this Object:

1.  Select the **Credential to connect with**. Select an existing or create a new [Facebook App credential](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
    .
    
2.  Enter the **APP ID** of the app connected to your credential. Refer to the [Facebook App credential](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
     documentation for more information.
    
3.  Select **Instagram** as the **Object**.
    
4.  **Field Names or IDs**: By default, the node will trigger on all the available events using the `*` wildcard filter. If you'd like to limit the events, use the `X` to remove the star and use the dropdown or an expression to select the updates you're interested in. Options include:
    
    *   **Comments**: Notifies you when anyone comments on an IG Media owned by your app's Instagram user.
        
    *   **Messaging Handover**
        
    *   **Mentions**: Notifies you whenever an Instagram user @mentions an Instagram Business or Creator Account in a comment or caption.
        
    *   **Messages**: Notifies you when anyone messages your app's Instagram user.
        
    *   **Messaging Seen**: Notifies you when someone sees a message sent by your app's Instagram user.
        
    *   **Standby**
        
    *   **Story Insights**: Notifies you one hour after a story expires with metrics describing interactions on a story.
        
    
5.  In **Options**, turn on the toggle to **Include Values**. This Object type fails without the option enabled.
    

Related resources[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------

Refer to [Webhooks for Instagram](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-instagram)
 and Meta's [Instagram](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/)
 Graph API reference for more information.

[PreviousGroup](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/group)
[NextLink](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link)

Last updated 10 days ago

Was this helpful?