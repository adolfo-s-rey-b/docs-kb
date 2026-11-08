For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency.md)
.

Use this object to receive updates about newly issued certificates for any domains that you have subscribed for certificate alerts or phishing alerts. Refer to [Facebook Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger)
 for more information on the trigger itself.

**Credentials**

Refer to the [Facebook App credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
 for authentication information for this node.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/)
 page.

Trigger configuration[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency#trigger-configuration)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

To configure the trigger with this Object:

1.  Select the **Credential to connect with**. Select an existing or create a new [Facebook App credential](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
    .
    
2.  Enter the **APP ID** of the app connected to your credential. Refer to the [Facebook App credential](https://docs.n8n.io/integrations/builtin/credentials/facebookapp)
     documentation for more information.
    
3.  Select **Certificate Transparency** as the **Object**.
    
4.  **Field Names or IDs**: By default, the node will trigger on all the available events using the `*` wildcard filter. If you'd like to limit the events, use the `X` to remove the star and use the dropdown or an expression to select the updates you're interested in. Options include:
    
    *   **Certificate**: Notifies you when someone issues a new certificate for your subscribed domains. You'll need to subscribe your domain for certificate alerts.
        
    *   **Phishing**: Notifies you when someone issues a new certificate that may be phishing one of your legitimate subscribed domains.
        
    
5.  In **Options**, turn on the toggle to **Include Values**. This Object type fails without the option enabled.
    

For these alerts, you'll need to subscribe your domain to the relevant alerts:

*   Refer to [Certificate Alerts](https://developers.facebook.com/docs/certificate-transparency-api#certificate-alerts-subscribing)
     for Certificate Alerts subscriptions.
    
*   Refer to [Phishing Alerts](https://developers.facebook.com/docs/certificate-transparency-api#phishing-alerts-subscribing)
     for Phishing Alerts subscriptions.
    

Related resources[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [Webhooks for Certificate Transparency](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-certificate-transparency)
 and Meta's [Certificate Transparency](https://developers.facebook.com/docs/graph-api/webhooks/reference/certificate-transparency/)
 Graph API reference for more information.

[PreviousApplication](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/application)
[NextGroup](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/group)

Last updated 10 days ago

Was this helpful?