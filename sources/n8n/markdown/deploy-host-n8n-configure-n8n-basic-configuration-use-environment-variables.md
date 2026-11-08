For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables.md)
.

This section lists the environment variables that you can use to change n8n's configuration settings when self-hosting n8n.

**File-based configuration**

You can provide a [configuration file](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
 for n8n. You can also append `_FILE` to certain variables to provide their configuration in a separate file.

In this section[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables#in-this-section)

-----------------------------------------------------------------------------------------------------------------------------------

*   [Ask n8n AI](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant)
    : variables for n8n's built-in AI help assistant.
    
*   [Binary data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data)
    : variables for storing and handling binary data.
    
*   [Credentials](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials)
    : variables for credential overwrites and encryption.
    
*   [Database](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database)
    : variables for database connection and configuration.
    
*   [Deployment](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
    : variables for instance identity, encryption, and the public API.
    
*   [Endpoints](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints)
    : variables for customizing n8n's REST and webhook endpoint paths.
    
*   [Executions](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions)
    : variables for execution timeouts, data pruning, and process modes.
    
*   [Expression engine](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/expression-engine)
    : variables for controlling expression evaluation.
    
*   [External data storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage)
    : variables for storing data outside the n8n database.
    
*   [External hooks](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks)
    : variables for the external hooks file location.
    
*   [External secrets](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets)
    : variables for external secrets vaults.
    
*   [Insights](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights)
    : variables for the Insights usage tracking feature.
    
*   [Logs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs)
    : variables for logging level, format, and destinations.
    
*   [License](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/license)
    : variables for activating and managing your n8n license.
    
*   [Nodes](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes)
    : variables for excluding or including specific nodes.
    
*   [OpenTelemetry](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/opentelemetry)
    : variables for exporting execution traces.
    
*   [Queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/queue-mode)
    : variables for running n8n across multiple worker processes.
    
*   [Scheduler](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/scheduler)
    : variables for the durable scheduler.
    
*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security)
    : variables for hardening a self-hosted instance.
    
*   [Source control](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control)
    : variables for Git-based source control.
    
*   [SSO](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso)
    : variables for single sign-on.
    
*   [SSRF protection](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection)
    : variables for restricting outbound requests from workflow nodes.
    
*   [Task runners](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners)
    : variables for configuring external Code node execution.
    
*   [Timezone and localization](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization)
    : variables for setting your instance's timezone and locale.
    
*   [User management and 2FA](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa)
    : variables for user management and two-factor authentication.
    
*   [Workflows](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows)
    : variables for workflow defaults and templates.
    
*   [Workflow history](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history)
    : variables for workflow version history.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------

*   [Basic configuration](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
    
*   [Configuration examples](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples)
    

[PreviousBasic configuration](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
[NextAsk n8n AI](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant)

Last updated 10 days ago

Was this helpful?