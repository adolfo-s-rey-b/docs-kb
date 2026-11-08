For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues.md)
.

Here are some common errors and issues with the [Schedule Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger)
 and steps to resolve or troubleshoot them.

Invalid cron expression[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues#invalid-cron-expression)

----------------------------------------------------------------------------------------------------------------------------------------------------

This error occurs when you set **Trigger Interval** to **Custom (Cron)** and n8n doesn't understand your cron expression. This may mean that there is a mistake in your cron expression or that you're using an incompatible syntax.

To debug, check that the following:

*   That your cron expression follows the syntax used in the [cron examples](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger#custom-cron-interval)
    
*   That your cron expression (after removing the [seconds column](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger#why-there-are-six-asterisks-in-the-cron-expression)
    ) validates on [crontab guru](https://crontab.guru/)
    

Scheduled workflows run at the wrong time[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues#scheduled-workflows-run-at-the-wrong-time)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the Schedule Trigger node runs at the wrong time, it may mean that you need to adjust the time zone n8n uses.

### Adjust the timezone globally[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues#adjust-the-timezone-globally)

If you're using [n8n Cloud](https://docs.n8n.io/deploy/use-n8n-cloud)
, follow the instructions on the [set the Cloud instance timezone](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/set-your-timezone)
 page to ensure that n8n executes in sync with your local time.

If you're [self hosting](https://docs.n8n.io/deploy/host-n8n)
, set your global timezone using the [`GENERIC_TIMEZONE` environment variable](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization)
.

### Adjust the timezone for an individual workflow[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues#adjust-the-timezone-for-an-individual-workflow)

To set the timezone for an individual workflow:

1.  Open the workflow on the canvas.
    
2.  Select the ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=01580b2475489f840a7eea5a18b0040a&sv=3) **Workflow menu** in the upper-right corner.
    
3.  Select **Settings**.
    
4.  Change the **Timezone** setting.
    
5.  Select **Save**.
    

### Variables not working as expected[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues#variables-not-working-as-expected)

While variables can be used in the scheduled trigger, their values only get evaluated when the workflow is published. After publishing the workflow, you can alter a variable's value in the settings but it won't change how often the workflow runs. To work around this, you must stop and then publish a new version of the workflow to apply the updated variable value.

### Changing the trigger interval[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues#changing-the-trigger-interval)

You can update the scheduled trigger interval at any time but it only gets updated when the workflow is published. If you change the trigger interval after the workflow is published, the changes won't take effect until you unpublish the workflow and then publish a new version of the workflow.

Also, the schedule begins from the time when you publish the workflow. For example, if you had originally set a schedule of every 1 hour and it should execute at 12:00, if you changed it to a 2 hour schedule and publish a new version of the workflow at 11:30, the next execution will be at 13:30, 2 hours from when you published it.

[PreviousSchedule Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger)
[NextSend Email](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail)

Last updated 10 days ago

Was this helpful?