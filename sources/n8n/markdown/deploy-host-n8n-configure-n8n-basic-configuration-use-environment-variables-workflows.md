For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows.md)
.

**File-based configuration**

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#keeping-sensitive-data-in-separate-files)
 for more details.

Variable

Type

Default

Description

`N8N_ONBOARDING_FLOW_DISABLED`

Boolean

`false`

Whether to disable onboarding tips when creating a new workflow (true) or not (false).

`N8N_WORKFLOW_ACTIVATION_BATCH_SIZE`

Number

`1`

How many workflows to publish simultaneously during startup.

`N8N_WORKFLOW_CALLER_POLICY_DEFAULT_OPTION`

String

`workflowsFromSameOwner`

Which workflows can call a workflow. Options are: `any`, `none`, `workflowsFromAList`, `workflowsFromSameOwner`. This feature requires [Workflow sharing](https://docs.n8n.io/build/manage-workflows/share-with-others)
.

`N8N_WORKFLOW_TAGS_DISABLED`

Boolean

`false`

Whether to disable workflow tags (true) or enable tags (false).

`WORKFLOWS_DEFAULT_NAME`

String

`My workflow`

The default name used for new workflows.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

*   [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
    

[PreviousUser management and 2FA](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa)
[NextWorkflow history](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history)

Last updated 10 days ago

Was this helpful?