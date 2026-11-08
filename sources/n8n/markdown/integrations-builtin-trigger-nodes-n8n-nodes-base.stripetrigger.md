For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger.md)
.

[Stripe](https://stripe.com/)
 is a suite of payment APIs that powers commerce for online businesses.

**Credentials**

Refer to the [Stripe credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/stripe)
 for authentication information for this node.

Webhook authentication[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger#webhook-authentication)

-------------------------------------------------------------------------------------------------------------------------------------

**Feature availability**

Verification of incoming requests is available from n8n 2.25.7 and n8n 2.26.2.

The Stripe Trigger node can verify that incoming webhook requests genuinely come from Stripe.

When you set a **Signature Secret** on your [Stripe credential](https://docs.n8n.io/integrations/builtin/credentials/stripe)
, the node checks the `Stripe-Signature` header on each request and rejects any request that's unsigned, forged, or more than five minutes old with a `401 Unauthorized` response. n8n doesn't run your workflow for rejected requests.

Without a **Signature Secret**, the node doesn't verify incoming requests, so anyone who knows your webhook URL could send forged events. n8n strongly recommends setting one. For setup steps, refer to [Verify incoming requests](https://docs.n8n.io/integrations/builtin/credentials/stripe#verify-incoming-requests)
.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Stripe Trigger integrations](https://n8n.io/integrations/stripe-trigger/)
 page.

[PreviousStrava Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.stravatrigger)
[NextSurveyMonkey Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.surveymonkeytrigger)

Last updated 10 days ago

Was this helpful?