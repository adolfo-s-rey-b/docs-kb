For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables.md)
.

You can manage a subset of instance settings from environment variables, instead of configuring them through the UI. This is useful when you provision n8n instances automatically, such as through an internal deployment pipeline.

Each supported area has a dedicated environment variable named `<AREA>_MANAGED_BY_ENV`. Set this variable to `true` to activate environment variable management for that area. n8n then applies the related environment variables and locks the matching UI controls.

How it works[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#how-it-works)

---------------------------------------------------------------------------------------------------------------------------

When you set `<AREA>_MANAGED_BY_ENV` to `true`:

*   n8n reapplies the settings from environment variables **on every startup**.
    
*   The matching UI controls become **read-only**.
    

When `<AREA>_MANAGED_BY_ENV` is `false` (the default), n8n ignores the related environment variables, even if you set them.

**Values persist when you turn off** `***_MANAGED_BY_ENV**`

Setting `*_MANAGED_BY_ENV` back to `false` restores UI write access but keeps the values that were last applied. Edit them through the UI afterward if you want to change them.

**Unexpected read-only UI controls**

If a setting appears as read-only and you didn't expect it, check whether the matching `*_MANAGED_BY_ENV` variable is `true` in your environment.

The supported areas and their activating variables:

*   Instance owner: `N8N_INSTANCE_OWNER_MANAGED_BY_ENV`
    
*   SSO: `N8N_SSO_MANAGED_BY_ENV`
    
*   Security policy: `N8N_SECURITY_POLICY_MANAGED_BY_ENV`
    
*   Log streaming: `N8N_LOG_STREAMING_MANAGED_BY_ENV`
    
*   MCP: `N8N_MCP_MANAGED_BY_ENV`
    
*   Community packages: `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV`
    

**Set** `**<AREA>_MANAGED_BY_ENV**` **to activate the group**

The other environment variables for an area have no effect unless `<AREA>_MANAGED_BY_ENV` is `true`. Set it to `true` to activate the group.

Instance owner[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#instance-owner)

-------------------------------------------------------------------------------------------------------------------------------

**Feature availability**

Instance owner management through environment variables is available from n8n 2.17.0.

Pre-provision the [instance owner](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management)
 from environment variables instead of going through the in-app setup. To change the owner email after setup, see [Change the instance owner email for self-hosted n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email)
.

`**N8N_INSTANCE_OWNER_PASSWORD_HASH**` **must be a bcrypt hash**

This variable expects a pre-hashed bcrypt value. Setting a plaintext password breaks login.

Variable

Type

Default

Description

`N8N_INSTANCE_OWNER_MANAGED_BY_ENV`

Boolean

`false`

Set to `true` to manage the instance owner from environment variables. When `true`, n8n overwrites the instance owner details below on every startup, locks the UI control for that user, and rejects API writes.

`N8N_INSTANCE_OWNER_EMAIL`

String

\-

Email address for the instance owner.

`N8N_INSTANCE_OWNER_FIRST_NAME`

String

\-

First name for the instance owner.

`N8N_INSTANCE_OWNER_LAST_NAME`

String

\-

Last name for the instance owner.

`N8N_INSTANCE_OWNER_PASSWORD_HASH`

String

\-

Bcrypt hash of the instance owner's password. Setting a plaintext password breaks login.

**Owner email must be unique**

`N8N_INSTANCE_OWNER_EMAIL` must not already belong to another user on the instance. This setting updates the existing instance owner account; it doesn't transfer ownership to another existing user or merge user accounts. To use an email address that already belongs to another user, change or delete that user first so the email becomes available.

SSO[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#sso)

---------------------------------------------------------------------------------------------------------

**Feature availability**

Single sign-on is available on:

*   **Self-hosted:** Business, Enterprise
    

n8n Cloud Enterprise also supports single sign-on, but not through the environment variables on this page.

Managing SSO from environment variables is available from n8n 2.18.0.

Configure [single sign-on](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso)
 from environment variables.

### Activation and shared settings[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#activation-and-shared-settings)

Variable

Type

Default

Description

`N8N_SSO_MANAGED_BY_ENV`

Boolean

`false`

Set to `true` to manage SSO from environment variables. When `true`, n8n applies the SSO variables on every startup and locks the matching UI controls.

`N8N_SSO_USER_ROLE_PROVISIONING`

Enum string: `disabled`, `instance_role`, `instance_and_project_roles`

`disabled`

How n8n provisions roles for users who sign in through SSO. `disabled` doesn't provision any roles. `instance_role` provisions the instance-level role only. `instance_and_project_roles` provisions both instance and project roles.

### OIDC[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#oidc)

Variable

Type

Default

Description

`N8N_SSO_OIDC_LOGIN_ENABLED`

Boolean

`false`

Whether to enable OIDC login.

`N8N_SSO_OIDC_CLIENT_ID`

String

\-

OIDC client ID issued by your identity provider.

`N8N_SSO_OIDC_CLIENT_SECRET`

String

\-

OIDC client secret issued by your identity provider.

`N8N_SSO_OIDC_DISCOVERY_ENDPOINT`

String

\-

OIDC discovery endpoint URL (the `.well-known/openid-configuration` URL for your identity provider).

`N8N_SSO_OIDC_PROMPT`

String

\-

Optional OIDC `prompt` parameter to send with the authorization request, for example `login` or `consent`.

`N8N_SSO_OIDC_ACR_VALUES`

String

\-

Optional OIDC `acr_values` parameter. Use this to request a specific authentication context, for example a step-up MFA flow.

### SAML[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#saml)

**SAML metadata variables are mutually exclusive**

Set either `N8N_SSO_SAML_METADATA` (inline XML) or `N8N_SSO_SAML_METADATA_URL` (URL), not both.

Variable

Type

Default

Description

`N8N_SSO_SAML_LOGIN_ENABLED`

Boolean

`false`

Whether to enable SAML login.

`N8N_SSO_SAML_METADATA`

String

\-

SAML identity provider metadata as an XML string. Mutually exclusive with `N8N_SSO_SAML_METADATA_URL`; don't set both.

`N8N_SSO_SAML_METADATA_URL`

String

\-

URL to fetch SAML identity provider metadata from. Mutually exclusive with `N8N_SSO_SAML_METADATA`; don't set both.

Security policy[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#security-policy)

---------------------------------------------------------------------------------------------------------------------------------

**Feature availability**

Managing the security policy from environment variables is available from n8n 2.18.0.

Manage the instance security policy from environment variables, including MFA enforcement and personal space restrictions.

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

Log streaming[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#log-streaming)

-----------------------------------------------------------------------------------------------------------------------------

**Feature availability**

Managing log streaming from environment variables is available from n8n 2.19.0.

Manage [log streaming](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems)
 destinations from environment variables. See [Configure using environment variables](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems#configure-using-environment-variables)
 for the per-destination JSON shape.

Variable

Type

Default

Description

`N8N_LOG_STREAMING_MANAGED_BY_ENV`

Boolean

`false`

Set to `true` to manage log streaming from environment variables. When `true`, n8n applies the log streaming variables on every startup and locks the matching UI controls.

`N8N_LOG_STREAMING_DESTINATIONS`

JSON string

\-

JSON array of log streaming destinations. Each destination is an object with a `type` of `webhook`, `syslog`, or `sentry`, plus the configuration for that type.

MCP[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#mcp)

---------------------------------------------------------------------------------------------------------

**Feature availability**

Managing instance-level MCP access from environment variables is available from n8n 2.20.0.

Manage [instance-level MCP access](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
 from environment variables.

Variable

Type

Default

Description

`N8N_MCP_MANAGED_BY_ENV`

Boolean

`false`

Set to `true` to manage MCP settings from environment variables. When `true`, n8n applies the MCP variables on every startup and locks the matching UI controls.

`N8N_MCP_ACCESS_ENABLED`

Boolean

`false`

Whether to enable instance-level MCP access (`true`) or not (`false`).

Community packages[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#community-packages)

---------------------------------------------------------------------------------------------------------------------------------------

**Feature availability**

Managing installed community packages from environment variables is available from n8n 2.21.0.

Manage the set of installed [community packages](https://docs.n8n.io/integrations/community-nodes/installation-and-management)
 from environment variables. n8n reconciles the installed packages against the list on every startup. Managed packages can't be uninstalled or updated through the UI.

`N8N_COMMUNITY_PACKAGES_ENABLED` must also be set to `true` (the default). When community packages are disabled, n8n ignores `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV` and logs a warning.

Variable

Type

Default

Description

`N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV`

Boolean

`false`

Set to `true` to manage installed community packages from environment variables. When `true`, n8n reconciles the installed packages against `N8N_COMMUNITY_PACKAGES` on every startup, installing missing packages, correcting versions, and **uninstalling any currently-installed packages that aren't in the list**. The **Community nodes** settings page becomes read-only: you can't install, update, or uninstall packages from the UI while this is enabled.

`N8N_COMMUNITY_PACKAGES`

JSON string

\-

JSON array of community packages to install. Each entry is an object with a `name` (required) and optional `version` and `checksum` fields. You can also embed the version in the name as `<package-name>@<version>`. See [environment variable installation](https://docs.n8n.io/integrations/community-nodes/installation-and-management/environment-variable-installation)
 for the full per-field reference.

Combined example[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#combined-example)

-----------------------------------------------------------------------------------------------------------------------------------

The following example configures an instance with all six areas managed by environment variables. It creates the instance owner, configures OIDC SSO, enforces MFA, registers a webhook log streaming destination, enables MCP access, and manages a community package.

Copy

    # Instance owner <a href="#instance-owner" id="instance-owner"></a>
    export N8N_INSTANCE_OWNER_MANAGED_BY_ENV=true
    export N8N_INSTANCE_OWNER_EMAIL=<owner-email>
    export N8N_INSTANCE_OWNER_FIRST_NAME=<first-name>
    export N8N_INSTANCE_OWNER_LAST_NAME=<last-name>
    export N8N_INSTANCE_OWNER_PASSWORD_HASH=<bcrypt-hash>
    
    # SSO using OIDC <a href="#sso-using-oidc" id="sso-using-oidc"></a>
    export N8N_SSO_MANAGED_BY_ENV=true
    export N8N_SSO_USER_ROLE_PROVISIONING=instance_role
    export N8N_SSO_OIDC_LOGIN_ENABLED=true
    export N8N_SSO_OIDC_CLIENT_ID=<client-id>
    export N8N_SSO_OIDC_CLIENT_SECRET=<client-secret>
    export N8N_SSO_OIDC_DISCOVERY_ENDPOINT=<discovery-url>
    
    # Security policy <a href="#security-policy" id="security-policy"></a>
    export N8N_SECURITY_POLICY_MANAGED_BY_ENV=true
    export N8N_MFA_ENFORCED_ENABLED=true
    export N8N_PERSONAL_SPACE_PUBLISHING_ENABLED=false
    export N8N_PERSONAL_SPACE_SHARING_ENABLED=false
    
    # Log streaming <a href="#log-streaming" id="log-streaming"></a>
    export N8N_LOG_STREAMING_MANAGED_BY_ENV=true
    export N8N_LOG_STREAMING_DESTINATIONS='[{"type":"webhook","url":"https://logs.example.com/n8n"}]'
    
    # MCP <a href="#mcp" id="mcp"></a>
    export N8N_MCP_MANAGED_BY_ENV=true
    export N8N_MCP_ACCESS_ENABLED=true
    
    # Community packages <a href="#community-packages" id="community-packages"></a>
    export N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV=true
    export N8N_COMMUNITY_PACKAGES='[{"name":"n8n-nodes-foo","version":"1.2.3"}]'

Set environment variables[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#set-environment-variables)

-----------------------------------------------------------------------------------------------------------------------------------------------------

For the supported ways to set environment variables, see [Configuration methods](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------

*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    

[PreviousChange instance owner email](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email)
[NextSet up task runners](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-task-runners)

Last updated 10 days ago

Was this helpful?