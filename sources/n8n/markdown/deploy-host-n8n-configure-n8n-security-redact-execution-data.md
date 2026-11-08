For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data.md)
.

**Feature availability**

Data redaction is available on:

*   **n8n Cloud:** Enterprise
    
*   **Self-hosted:** Enterprise
    

Per-workflow execution data redaction is available from n8n 2.16.0. Instance-level enforcement of execution data redaction is available from n8n 2.26.0.

Execution data redaction lets you hide the input and output data of workflow executions. This helps protect sensitive information like personal data, authentication tokens, and financial records from users who can view the workflow but don't need to see the underlying data.

When you enable redaction, execution metadata (status, timing, node names) remains visible, but n8n replaces the actual data payload processed by each node with a redacted indicator.

You can configure redaction per workflow, or [enforce it instance-wide](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#instance-level-enforcement)
 so that every workflow redacts execution data.

Why use execution data redaction[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#why-use-execution-data-redaction)

------------------------------------------------------------------------------------------------------------------------------------------------------

Workflows often process data that the workflow builder or viewers shouldn't have access to outside of n8n. Common scenarios include:

*   **PII and compliance**: Workflows handling customer personal data (emails, addresses, financial records) need to meet GDPR, SOC 2, or internal security standards.
    
*   **Cross-department workflows**: A workflow built by one team processes sensitive data from another team that the builder wouldn't have access to otherwise.
    
*   **Least privilege principle**: Limiting data visibility to only those who need it, rather than everyone with workflow view access.
    

Before execution data redaction, the only option was to disable execution history entirely at the workflow level, which removed all visibility into workflow success or failure status. Execution data redaction preserves execution monitoring while hiding the sensitive data payload.

Configure redaction settings[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#configure-redaction-settings)

----------------------------------------------------------------------------------------------------------------------------------------------

You configure redaction per workflow in the workflow settings. You need the `workflow:enableRedaction` or `workflow:disableRedaction` scope (or both) to change these settings.

To configure redaction:

1.  Open your workflow.
    
2.  Select the **Workflow menu** ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2773773108-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fjm0ZYRpZIPWge2ZSiDYO%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=02f47b9009a4c346ccb34c5c13c66476&sv=3) in the upper-right corner.
    
3.  Select **Settings**.
    
4.  Find the **Redact production execution data** and **Redact manual execution data** settings.
    
5.  For each setting, choose either **Default - Do not redact** or **Redact**.
    
6.  Select **Save**.
    

**Settings locked by instance enforcement**

When [instance-level enforcement](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#instance-level-enforcement)
 is active, n8n locks the settings covered by the enforced scope to **Redact**. You can't turn them off at the workflow level.

### Redaction settings explained[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#redaction-settings-explained)

There are two independent toggles that control redaction:

Setting

What it controls

**Redact production execution data**

Controls whether n8n redacts data from production (non-manually triggered) executions. Production executions include those triggered by webhooks, schedules, or other triggers when the workflow stays active.

**Redact manual execution data**

Controls whether n8n redacts data from manually triggered executions. Manual executions include those you start by selecting **Execute Workflow** in the editor.

Instance-level enforcement[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#instance-level-enforcement)

------------------------------------------------------------------------------------------------------------------------------------------

Instance owners and admins can enforce redaction for all workflows on the instance instead of relying on each workflow's individual settings. Enforcement sets a minimum redaction policy (a "floor") that applies everywhere.

To enable enforcement, navigate to **Settings** > **Security** and configure the **Data redaction** section. Refer to [Security settings](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/manage-security-policies#enforce-execution-data-redaction)
 for the step-by-step instructions.

### Enforcement scope[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#enforcement-scope)

The enforcement scope controls which executions n8n redacts across the instance:

Scope

What it enforces

**Production executions**

n8n redacts data from production executions in every workflow. Manual executions follow each workflow's own settings. This is the recommended setting: it protects live data while keeping manual test runs visible for debugging.

**Manual and production executions**

n8n redacts data from all executions in every workflow. Use this when even test data is sensitive.

### How enforcement interacts with workflow settings[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#how-enforcement-interacts-with-workflow-settings)

*   **Enforcement applies when execution data is read.** n8n redacts data covered by the enforcement scope whenever anyone views an execution, including executions from workflows that don't have redaction enabled in their own settings.
    
*   **Workflow settings can't be weaker than the enforced scope.** The workflow settings UI locks the affected redaction toggles, and the [public API](https://docs.n8n.io/connect/n8n-api)
     rejects attempts to create or update a workflow with a redaction policy below the floor. Workflows can still opt into stricter redaction than the floor.
    
*   **New workflows start at the floor.** When you create a workflow while enforcement is active, its redaction policy defaults to the enforced scope. If you create a workflow through the public API without specifying a redaction policy, n8n sets it to the floor.
    
*   **Existing workflow settings stay as they are.** Enabling enforcement doesn't change the stored settings of existing workflows. Their execution data is still redacted at the enforced scope, and if you later disable enforcement, each workflow returns to its own settings.
    

What gets redacted[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#what-gets-redacted)

--------------------------------------------------------------------------------------------------------------------------

When n8n redacts an execution, it redacts:

*   **Item JSON data**: n8n replaces all input and output data (`item.json`) for each node with an empty object.
    
*   **Binary data**: n8n removes binary data (`item.binary`) such as files and images.
    
*   **Declared sensitive fields**: n8n always redacts fields that node authors mark as sensitive (using `sensitiveOutputFields`) and prevents revealing them, even for users with reveal access.
    
*   **Error metadata**: n8n redacts error messages, preserving only the error type and HTTP status code (for API errors) to aid in troubleshooting.
    

In the redacted execution:

*   The execution viewer displays a **"Data redacted"** indicator with a shredder icon instead of the usual data tables.
    
*   Execution metadata remains visible: node names, execution status (success/failure), timing information, and the workflow structure.
    

**Error information**

When n8n redacts execution data, it also redacts error details to prevent sensitive information from leaking through error messages. Only the error type (for example, `NodeApiError`) and HTTP status code remain. This provides enough information to identify the category of failure without exposing data.

Reveal redacted data[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#reveal-redacted-data)

------------------------------------------------------------------------------------------------------------------------------

Users with the **Reveal execution data** (`execution:reveal`) scope can temporarily view redacted execution data for a specific execution. Instance owners and admins have this scope by default.

To reveal data:

1.  Open the execution in the execution viewer.
    
2.  Select the **Reveal data** button displayed in the redacted data area.
    
3.  Review the confirmation dialog. It explains that:
    
    *   The system logs the action in the audit trail.
        
    *   You should only reveal data if you have a legitimate reason.
        
    *   Unnecessary access may violate your organization's policy.
        
    
4.  Select **Reveal data** to confirm.
    

The execution data becomes visible for that execution in the current session.

**Executions using dynamic credentials**

n8n denies reveal requests for executions that used dynamic credentials, regardless of the user's permissions or the redaction policy in effect. This prevents exposing credentials that the execution resolved at runtime.

Audit logging[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#audit-logging)

----------------------------------------------------------------------------------------------------------------

[Log streaming](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems)
 tracks reveal actions and enforcement policy changes. The following audit events are available:

Event

Description

`n8n.audit.execution.data.revealed`

n8n emits this event when a user reveals redacted execution data. Includes the user, execution ID, workflow ID, timestamp, IP address, and the redaction policy in effect.

`n8n.audit.execution.data.reveal_failure`

n8n emits this event when it denies a reveal attempt (for example, due to insufficient permissions). Includes the same fields plus the rejection reason.

`n8n.audit.redaction-enforcement.updated`

n8n emits this event when a user changes the instance-level enforcement policy. Includes the user and the policy values before and after the change.

These events integrate with your existing log streaming destinations (syslog, webhooks, Sentry) and support compliance reporting and access auditing.

Permission scopes[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#permission-scopes)

------------------------------------------------------------------------------------------------------------------------

Execution data redaction introduces the following permission scopes that you can assign through [custom project roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles)
:

Scope

Purpose

`workflow:enableRedaction`

Allows turning redaction on in workflow settings. Displayed as **Enable data redaction** in the role configuration UI.

`workflow:disableRedaction`

Allows turning redaction off in workflow settings. Displayed as **Disable data redaction** in the role configuration UI.

By default, instance owners, admins, and project admins have the permissions to enable or disable redaction and to reveal redacted data. You can create custom roles to give more users, such as workflow builders, one or both scopes independently.

What redaction doesn't cover[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#what-redaction-doesnt-cover)

---------------------------------------------------------------------------------------------------------------------------------------------

Redaction controls the visibility of execution data when users view executions. It's not a backend access control, and some data paths fall outside its scope. Keep these limitations in mind when evaluating redaction for compliance:

*   **Code node** `**console.log**` **output**: data that a Code node logs with `console.log` isn't redacted. In manual executions, the output appears in the editor's Logs panel. In production executions, the output goes to the server's standard output (stdout) and any logging infrastructure attached to it.
    
*   **Data flowing between nodes**: redaction doesn't restrict what downstream nodes receive. During an execution, data flows between nodes without restriction, so any node in the workflow can send execution data to external systems. Redaction controls what users see in the execution viewer, not what the workflow itself does with the data.
    
*   **Webhook responses**: the response body that a workflow returns to a caller (for example, through the Respond to Webhook node or a node's respond option) is the raw data, not a redacted version.
    
*   **Authentication headers in outbound requests**: redaction doesn't alter the requests workflows make to external services, including any authentication headers they contain.
    
*   **No field-level redaction**: redaction applies to a node's entire data payload. You can't configure redaction for individual fields within the data. The exception is fields that node authors declare as sensitive, which n8n always redacts.
    
*   **Stored data stays as it is**: redaction doesn't encrypt or change execution data in the database. n8n applies redaction when serving the data through the API. Anyone with direct database access can read the underlying data.
    
*   **Enforcement doesn't propagate through source control**: instance-level enforcement is an instance policy and isn't included when you push workflows with [source control](https://docs.n8n.io/administer/use-source-control-and-environments)
    . A workflow pushed from an enforced instance to a non-enforced instance isn't redacted on the target instance. This matches the behavior of other instance-level policies, such as two-factor authentication enforcement.
    

Best practices[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#best-practices)

------------------------------------------------------------------------------------------------------------------

### Choosing the right redaction policy[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#choosing-the-right-redaction-policy)

Scenario

Recommended setting

Workflows processing PII, financial data, or authentication tokens in production

Redact production execution data

Workflows where even test data is sensitive (for example, using copies of production data)

Redact both production and manual execution data

Workflows processing non-sensitive data, or during initial development

No redaction

### General recommendations[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#general-recommendations)

*   **Start with production redaction**: For most workflows handling sensitive data, redacting production executions while keeping manual executions visible provides a good balance between security and ease of debugging.
    
*   **Redact manual data when needed**: If your test environment uses real or production-like data, enable manual execution redaction as well.
    
*   **Use log streaming**: Enable [log streaming](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems)
     to capture reveal audit events. This provides an audit trail for compliance and allows you to monitor who accesses sensitive execution data.
    
*   **Review redaction settings during workflow reviews**: Include redaction policy as part of your workflow review or approval process, particularly for workflows that handle cross-department or customer-facing data.
    

Security considerations[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#security-considerations)

------------------------------------------------------------------------------------------------------------------------------------

*   n8n applies redaction at the API level and never sends redacted data to the browser.
    
*   When you [create custom nodes](https://docs.n8n.io/connect/create-nodes/overview)
    , you can declare specific output fields as sensitive (using `sensitiveOutputFields` in the node type definition). n8n always redacts these fields and prevents revealing them, even for users with reveal access.
    
*   If the redaction service can't resolve a node's type definition (for example, after uninstalling a community node), n8n fully redacts all output data for that node. This fail-closed approach prevents unknown nodes from leaking sensitive fields.
    
*   When redaction is enabled, execution data is also automatically redacted from [log streaming](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems)
     and logging output.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data#related-resources)

------------------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    

[PreviousDecrypt OAuth 2.0 tokens with JWE](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/decrypt-oauth-20-tokens-with-jwe)
[NextScaling](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling)

Last updated 10 days ago

Was this helpful?