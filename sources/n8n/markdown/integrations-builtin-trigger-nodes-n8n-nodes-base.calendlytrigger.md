For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger.md)
.

[Calendly](https://calendly.com/)
 is an automated scheduling software that's designed to help find meeting times.

**Credentials**

Refer to the [Calendly credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/calendly)
 for authentication information for this node.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Calendly Trigger integrations](https://n8n.io/integrations/calendly-trigger/)
 page.

Events[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger#events)

-------------------------------------------------------------------------------------------------------

*   Event created
    
*   Event canceled
    

Common issues[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger#common-issues)

---------------------------------------------------------------------------------------------------------------------

Here are some common errors and issues with the Calendly Trigger node and steps to resolve or troubleshoot them.

### Node only triggers for Calendly-managed bookings[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger#node-only-triggers-for-calendly-managed-bookings)

Calendly webhooks only fire for bookings and cancellations managed by Calendly. Creating or editing an event directly in a connected calendar, such as Google Calendar, won't trigger the Calendly Trigger node.

### Webhook callback URL must be public HTTPS[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger#webhook-callback-url-must-be-public-https)

The Calendly Trigger node uses Calendly webhooks, and Calendly requires webhook callback URLs to be public HTTPS URLs. For local testing, use a tunnel such as [ngrok](https://ngrok.com/)
 or [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/)
 and configure n8n to use that public HTTPS URL for webhooks. Refer to [Configuration > Webhook URL](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy)
 for setup details.

[PreviousBrevo Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.brevotrigger)
[NextCal Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger)

Last updated 10 days ago

Was this helpful?