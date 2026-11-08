For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md)
.

Use the Facebook Lead Ads Trigger node to respond to events in [Facebook Lead Ads](https://www.facebook.com/business/ads/lead-ads/)
 and integrate Facebook Lead Ads with other applications. n8n has built-in support for responding to new leads.

On this page, you'll find a list of events the Facebook Lead Ads Trigger node can respond to, and links to more resources.

**Credentials**

Refer to the [Facebook Lead Ads credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/facebookleadads)
 for authentication information for this node.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Facebook Lead Ads Trigger integrations](https://n8n.io/integrations/facebook-lead-ads-trigger/)
 page.

Events[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger#events)

--------------------------------------------------------------------------------------------------------------

*   New lead
    

Related resources[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger#related-resources)

------------------------------------------------------------------------------------------------------------------------------------

View [example workflows and related content](https://n8n.io/integrations/facebook-lead-ads-trigger/)
 on n8n's website.

Refer to [Facebook Lead Ads' documentation](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/)
 for details about their API.

Common issues[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger#common-issues)

----------------------------------------------------------------------------------------------------------------------------

Here are some common errors and issues with the Facebook Lead Ads Trigger node and steps to resolve or troubleshoot them.

### Workflow only works in testing or production[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger#workflow-only-works-in-testing-or-production)

Facebook Lead Ads only allows you to register a single webhook per app. This means that every time you switch from using the testing URL to the production URL (and vice versa), Facebook Lead Ads overwrites the registered webhook URL.

You may have trouble with this if you try to test a workflow that's also published. Facebook Lead Ads will only send events to one of the two webhook URLs, so the other will never receive event notifications.

To work around this, you can disable your workflow when testing:

**Halts production traffic**

This workaround temporarily disables your production workflow for testing. Your workflow will no longer receive production traffic while it's unpublished.

1.  Go to your workflow page.
    
2.  From the workflow settings dropdown, click **Unpublish** to disable the workflow temporarily.
    
3.  Test your workflow using the test webhook URL.
    
4.  When you finish testing, click **Publish**. The production webhook URL should resume working.
    

[PreviousEventbrite Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.eventbritetrigger)
[NextFacebook Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger)

Last updated 10 days ago

Was this helpful?