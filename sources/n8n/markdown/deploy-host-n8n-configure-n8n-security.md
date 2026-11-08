For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security.md)
.

You can secure a self-hosted n8n instance to protect credentials and workflow data: run a security audit, set up SSL and SSO, restrict nodes and the public API, and redact execution data.

Securing your n8n instance can take several forms.

In this section[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security#in-this-section)

----------------------------------------------------------------------------------------------

*   [Manage security policies](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/manage-security-policies)
    : manage instance-wide security policies including MFA enforcement and personal space controls.
    
*   [Run security audits](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits)
    : run a security audit to identify security risks.
    
*   [Set up SSL](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/set-up-ssl)
    : enforce secure connections.
    
*   [Configure SSO](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso)
    : set up SAML or OIDC Single Sign-On.
    
*   [Rotate encryption keys](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/rotate-encryption-keys)
    : periodically replace the key that encrypts credentials and other sensitive data.
    
*   [Decrypt OAuth 2.0 tokens with JWE](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/decrypt-oauth-20-tokens-with-jwe)
    : let your identity provider encrypt access and ID tokens that only your instance can decrypt.
    
*   [Harden task runners](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners)
    : better isolation for Code node executions.
    
*   [Redact execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data)
    : hide input and output data from workflow executions.
    
*   [Disable the public API](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api)
    : prevent others from using the n8n public REST API.
    
*   [Control telemetry](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry)
    : opt out of the anonymous data n8n collects automatically.
    
*   [Block specific nodes](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes)
    : prevent your n8n users from accessing specific nodes.
    
*   [Enable SSRF protection](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection)
    : control which hosts and IP ranges workflow nodes can connect to.
    
*   [Verify user emails](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails)
    : restrict account registration to email-verified users.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security#related-resources)

--------------------------------------------------------------------------------------------------

*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    
*   [Set up token exchange](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration/set-up-token-exchange)
    : authenticate users from your own identity provider when embedding n8n.
    
*   [Require two-factor auth](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth)
    : enable 2FA for your users.
    

[PreviousManage your license](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-your-license)
[NextManage security policies](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/manage-security-policies)

Last updated 10 days ago

Was this helpful?