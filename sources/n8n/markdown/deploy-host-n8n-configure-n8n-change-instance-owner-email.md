For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email.md)
.

You can change the instance owner email from the UI, or from environment variables if you manage the instance owner that way.

**Owner email must be unique**

The owner email must not already belong to another user on the instance. If the email you want is already used by another user, change or delete that user first so the email becomes available.

Changing the owner email updates the existing instance owner account. It doesn't transfer ownership to another existing user or merge user accounts.

Change the owner email in the UI[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email#change-the-owner-email-in-the-ui)

---------------------------------------------------------------------------------------------------------------------------------------------------

1.  Log in as the instance owner.
    
2.  Go to **Settings** > **Personal**.
    
3.  Update the **Email** field.
    
4.  Select **Save**.
    

Change the owner email using environment variables[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email#change-the-owner-email-using-environment-variables)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you manage the instance owner using environment variables:

1.  Set `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` to `true`.
    
2.  Set `N8N_INSTANCE_OWNER_EMAIL` to the new owner email.
    
3.  Keep `N8N_INSTANCE_OWNER_FIRST_NAME`, `N8N_INSTANCE_OWNER_LAST_NAME`, and `N8N_INSTANCE_OWNER_PASSWORD_HASH` set.
    
4.  Restart n8n.
    

When `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` is `true`, n8n reapplies the owner details on every startup. The matching UI controls become read-only.

`**N8N_INSTANCE_OWNER_PASSWORD_HASH**` **must be a bcrypt hash**

This variable expects a pre-hashed bcrypt value. Setting a plaintext password breaks login.

For more information, see [Manage instance settings using environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#instance-owner)
.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email#related-resources)

---------------------------------------------------------------------------------------------------------------------

*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    

[PreviousUser management](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management)
[NextManage settings using environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables)

Last updated 10 days ago

Was this helpful?