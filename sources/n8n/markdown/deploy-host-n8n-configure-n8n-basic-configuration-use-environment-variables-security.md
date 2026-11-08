For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security.md)
.

**File-based configuration**

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#keeping-sensitive-data-in-separate-files)
 for more details.

Variable

Type

Default

Description

`N8N_BLOCK_ENV_ACCESS_IN_NODE`

Boolean

`false`

Whether to allow users to access environment variables in expressions and the Code node (false) or not (true).

`N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES`

Boolean

`true`

Set to `true` to block access to all files in the `.n8n` directory and user defined configuration files.

`N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS`

Boolean

`false`

Set to `true` to try to set 0600 permissions for the settings file, giving only the owner read and write access.

`N8N_RESTRICT_FILE_ACCESS_TO`

String

Limits access to files in these directories. Provide multiple files as a semicolon-separated list ("`;`").

`N8N_SECURITY_AUDIT_DAYS_ABANDONED_WORKFLOW`

Number

90

Number of days to consider a workflow abandoned if it's not executed.

`N8N_CONTENT_SECURITY_POLICY`

String

`script-src <nonce> 'strict-dynamic' 'unsafe-eval'; object-src 'none'; base-uri 'none'`

The [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
 n8n serves on its own pages. Accepts a policy string, for example `frame-ancestors http://localhost:3000`, or a [helmet.js](https://helmetjs.github.io/#content-security-policy)
 directives object. Write `<nonce>` where n8n inserts the per-request nonce. Set to `default` for n8n's policy, or `{}` for no header.

`N8N_CONTENT_SECURITY_POLICY_REPORT_ONLY`

String

The policy n8n serves as `Content-Security-Policy-Report-Only`, in the same formats as `N8N_CONTENT_SECURITY_POLICY`. The browser reports violations but doesn't block them, so use it to try a policy before enforcing it.

`N8N_SECURE_COOKIE`

Boolean

`true`

Ensures that cookies are only sent over HTTPS, enhancing security.

`N8N_SAMESITE_COOKIE`

Enum string: `strict`, `lax`, `none`

`lax`

Controls cross-site cookie behavior ([learn more](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite)
):

*   `strict`: Sent only for first-party requests.
    
*   `lax` (default): Sent with top-level navigation requests.
    
*   `none`: Sent in all contexts (requires HTTPS).
    

`N8N_GIT_NODE_DISABLE_BARE_REPOS`

Boolean

`false`

Set to `true` to prevent the [Git node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.git)
 from working with bare repositories, enhancing security.

`N8N_GIT_NODE_ENABLE_HOOKS`

Boolean

`false`

Set to `true` to allow the [Git node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.git)
 to execute Git hooks.

`N8N_POSTMESSAGE_ALLOWED_ORIGINS`

String

Origins allowed to exchange `postMessage` commands with the editor when it's embedded in another page. Only relevant when embedding the editor is possible, for example when running with `N8N_PREVIEW_MODE=true`. Provide multiple origins as a comma-separated list, for example `https://n8n.io,https://app.example.com`. When empty (the default), the editor accepts messages from any origin.

Security policy using environment variables[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security#security-policy-using-environment-variables)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Set `N8N_SECURITY_POLICY_MANAGED_BY_ENV` to `true` to manage the security policy from environment variables. See [Manage instance settings using environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables)
 for how the activation pattern works.

Variable

Type

Default

Description

`N8N_SECURITY_POLICY_MANAGED_BY_ENV`

Boolean

`false`

Set to `true` to manage the security policy from environment variables. When `true`, n8n applies the security policy variables on every startup and locks the matching UI controls.

`N8N_MFA_ENFORCED_ENABLED`

Boolean

`false`

Whether to enforce two-factor authentication for all users (`true`) or not (`false`).

`N8N_PERSONAL_SPACE_PUBLISHING_ENABLED`

Boolean

`true`

Whether users can publish from their personal space (`true`) or not (`false`).

`N8N_PERSONAL_SPACE_SHARING_ENABLED`

Boolean

`true`

Whether users can share resources from their personal space (`true`) or not (`false`).

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------------

*   [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
    

[PreviousScheduler](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/scheduler)
[NextSource control](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control)

Last updated 10 days ago

Was this helpful?