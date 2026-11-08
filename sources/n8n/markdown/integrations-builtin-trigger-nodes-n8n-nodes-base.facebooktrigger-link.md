For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link.md)
.

Use this object to receive updates about links for rich previews by an external provider. Refer to [Facebook Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger)
 for more information on the trigger itself.

**Credentials**

Refer to the [Facebook App credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
 for authentication information for this node.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/)
 page.

Trigger configuration[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link#trigger-configuration)

------------------------------------------------------------------------------------------------------------------------------------------

To configure the trigger with this Object:

1.  Select the **Credential to connect with**. Select an existing or create a new [Facebook App credential](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
    .
    
2.  Enter the **APP ID** of the app connected to your credential. Refer to the [Facebook App credential](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
     documentation for more information.
    
3.  Select **Link** as the **Object**.
    
4.  **Field Names or IDs**: By default, the node will trigger on all the available events using the `*` wildcard filter. If you'd like to limit the events, use the `X` to remove the star and use the dropdown or an expression to select the updates you're interested in.
    
5.  In **Options**, turn on the toggle to **Include Values**. This Object type fails without the option enabled.
    

Related resources[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link#related-resources)

----------------------------------------------------------------------------------------------------------------------------------

Refer to Meta's [Links](https://developers.facebook.com/docs/workplace/reference/webhooks/#links)
 Workplace API reference for more information.

[PreviousInstagram](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram)
[NextPage](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page)

Last updated 10 days ago

Was this helpful?