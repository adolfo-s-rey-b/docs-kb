For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management.md)
.

User management in n8n allows you to invite people to work in your n8n instance.

This document describes how to configure your n8n instance to support user management, and the steps to start inviting users.

Refer to the main [User management](https://docs.n8n.io/administer/manage-users-and-access)
 guide for more information about usage, including:

*   [Managing users](https://docs.n8n.io/administer/manage-users-and-access/add-and-remove-users)
    
*   [Instance roles](https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles)
    
*   [Best practices](https://docs.n8n.io/administer/manage-users-and-access/follow-best-practices)
    

For LDAP setup information, refer to [LDAP](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/connect-ldap)
.

For SAML setup information, refer to [SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml)
.

**Feature availability**

Support for basic auth and JWT authentication was removed from n8n 1.0.

The `N8N_USER_MANAGEMENT_DISABLED` environment variable was also removed from n8n 1.0. No supported way to disable the login screen exists in recent versions of n8n, including for local or development use. If you need to simplify login for local development, consider using a password manager, setting a simple local password, or scripting the standard login flow.

Setup[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management#setup)

---------------------------------------------------------------------------------

There are three stages to set up user management in n8n:

1.  Configure your n8n instance to use your SMTP server.
    
2.  Start n8n and follow the setup steps in the app.
    
3.  Invite users.
    

### Step one: SMTP[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management#step-one-smtp)

n8n recommends setting up an SMTP server, for user invites and password resets.

**Feature availability**

Setting up SMTP is optional from n8n 0.210.1. You can choose to manually copy and send invite links instead of setting up SMTP. Note that if you skip this step, users can't reset passwords.

Get the following information from your SMTP provider:

*   Server name
    
*   SMTP username
    
*   SMTP password
    
*   SMTP sender name
    

To set up SMTP with n8n, configure the SMTP environment variables for your n8n instance. For information on how to set environment variables, refer to [Configuration](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)

Variable

Type

Description

Required?

`N8N_EMAIL_MODE`

string

`smtp`

Required

`N8N_SMTP_HOST`

string

_your\_SMTP\_server\_name_

Required

`N8N_SMTP_PORT`

number

_your\_SMTP\_server\_port_ Default is `465`.

Optional

`N8N_SMTP_USER`

string

_your\_SMTP\_username_

Optional

`N8N_SMTP_PASS`

string

_your\_SMTP\_password_

Optional

`N8N_SMTP_OAUTH_SERVICE_CLIENT`

string

_your\_OAuth\_service\_client_

Optional

`N8N_SMTP_OAUTH_PRIVATE_KEY`

string

_your\_OAuth\_private\_key_

Optional

`N8N_SMTP_SENDER`

string

Sender email address. You can optionally include the sender name. Example with name: _n8n_ `_<contact@n8n.com>_`

Required

`N8N_SMTP_SSL`

boolean

Whether to use SSL for SMTP (true) or not (false). Defaults to `true`.

Optional

`N8N_UM_EMAIL_TEMPLATES_INVITE`

string

Full path to your HTML email template. This overrides the default template for invite emails.

Optional

`N8N_UM_EMAIL_TEMPLATES_PWRESET`

string

Full path to your HTML email template. This overrides the default template for password reset emails.

Optional

`N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED`

String

Overrides the default HTML template for notifying users that a credential was shared. Provide the full path to the template.

Optional

`N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED`

String

Overrides the default HTML template for notifying users that a credential was shared. Provide the full path to the template.

Optional

`N8N_UM_EMAIL_TEMPLATES_PROJECT_SHARED`

String

Overrides the default HTML template for notifying users that a project was shared. Provide the full path to the template.

Optional

If your n8n instance is already running, you need to restart it to enable the new SMTP settings.

**More configuration options**

There are more configuration options available as environment variables. Refer to [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
 for a list. These include options to disable tags, workflow templates, and the personalization survey, if you don't want your users to see them.

**New to SMTP?**

If you're not familiar with SMTP, this [blog post by SendGrid](https://sendgrid.com/blog/what-is-an-smtp-server/)
 offers a short introduction, while [Wikipedia's Simple Mail Transfer Protocol article](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
 provides more detailed technical background.

### Step two: In-app setup[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management#step-two-in-app-setup)

When you set up user management for the first time, you create an owner account.

1.  Open n8n. The app displays a signup screen.
    
2.  Enter your details. Your password must be at least eight characters, including at least one number and one capital letter.
    
3.  Click **Next**. n8n logs you in with your new owner account.
    

#### Pre-provision the instance owner from environment variables[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management#pre-provision-the-instance-owner-from-environment-variables)

**Feature availability**

Pre-provisioning the instance owner from environment variables is available from n8n 2.17.0.

You can pre-provision the instance owner from environment variables instead of going through the in-app setup. Set `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` to `true` and provide the owner details. See [Manage instance settings using environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables)
 for how the activation pattern works.

To change the owner email after setup, see [Change the instance owner email for self-hosted n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email)
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

### Step three: Invite users[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management#step-three-invite-users)

You can now invite other people to your n8n instance.

1.  Sign in to your n8n instance with your owner account. On n8n Cloud, if you're in the n8n Cloud console, select **Open instance** on the **Overview** page.
    
2.  Click the three dots next to your user icon at the bottom left and click **Settings**. n8n opens your **Personal settings** page.
    
3.  Click **Users** to go to the **Users** page.
    
4.  Click **Invite**.
    
5.  Enter the new user's email address.
    
6.  Click **Invite user**. n8n sends an email with a link for the new user to join.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management#related-resources)

---------------------------------------------------------------------------------------------------------

*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    

[PreviousUse the command line](https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line)
[NextChange instance owner email](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email)

Last updated 10 days ago

Was this helpful?