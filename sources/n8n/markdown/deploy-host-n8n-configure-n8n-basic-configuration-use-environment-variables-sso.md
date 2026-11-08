For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso.md)
.

**File-based configuration**

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#keeping-sensitive-data-in-separate-files)
 for more details.

**Feature availability**

Single sign-on is available on:

*   **Self-hosted:** Business, Enterprise
    

n8n Cloud Enterprise also supports single sign-on, but not through the environment variables on this page.

Refer to [Set up SSO](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso)
 for in-app setup steps and identity provider guides. See [Manage instance settings using environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables)
 for how the activation pattern works.

Activation and shared settings[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso#activation-and-shared-settings)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

OIDC[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso#oidc)

-----------------------------------------------------------------------------------------------------------------

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

SAML[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso#saml)

-----------------------------------------------------------------------------------------------------------------

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

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------

*   [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
    

[PreviousSource control](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control)
[NextSSRF protection](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection)

Last updated 10 days ago

Was this helpful?