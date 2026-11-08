For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md)
.

The [Webhook node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook)
 works a bit differently from other core nodes. n8n recommends following these processes for building, testing, and using your Webhook node in production.

n8n generates two **Webhook URLs** for each Webhook node: a **Test URL** and a **Production URL**.

Build and test workflows[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development#build-and-test-workflows)

-----------------------------------------------------------------------------------------------------------------------------------------------------

While building or testing a workflow, use the **Test** webhook URL.

Using a test webhook ensures that you can view the incoming data in the editor UI, which is useful for debugging. Select **Listen for test event** to register the webhook before sending the data to the test webhook. The test webhook stays active for 120 seconds.

When using the Webhook node on localhost on a [self-hosted](https://docs.n8n.io/deploy/host-n8n)
 n8n instance, run n8n in tunnel mode:

*   [npm with tunnel](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#n8n-with-tunnel)
    
*   [Docker with tunnel](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker#n8n-with-tunnel)
    

Production workflows[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development#production-workflows)

---------------------------------------------------------------------------------------------------------------------------------------------

When your workflow is ready, switch to using the **Production** webhook URL. You can then publish your workflow, and n8n runs it automatically when an external service calls the webhook URL.

When working with a Production webhook, ensure that you have saved and published the workflow. Data flowing through the webhook isn't visible in the editor UI with the production webhook.

Refer to [Create a workflow](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows)
 for more information on publishing workflows.

[PreviousWebhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues)

Last updated 10 days ago

Was this helpful?