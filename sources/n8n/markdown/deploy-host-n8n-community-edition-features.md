For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/community-edition-features.md)
.

Every self-hosted installation runs on the same underlying product. You can stick with the free Community edition indefinitely, register for free to unlock extra features, or subscribe to a paid plan for a license key that unlocks that plan's features.

*   **Community edition**: the free edition. This is what n8n runs without a license key.
    
*   **Registered Community edition**: the free Community edition with extra features unlocked by registering your email. Still free.
    
*   **Business** and **Enterprise** plans: paid plans. Subscribing gives you a license key that unlocks the features for that plan.
    

**Plan, edition, or license?**

An **edition** is the variant of the self-hosted software you run: Community, Registered Community, Business, or Enterprise. A **plan** is the paid subscription tier you buy, for self-hosted or [n8n Cloud](https://docs.n8n.io/deploy/use-n8n-cloud/start-your-free-trial)
. When you subscribe to a paid plan, you get a **license** key that unlocks the features for that plan. Registering a free Community edition also uses a license key. See the [glossary](https://docs.n8n.io/key-concept-glossary#edition-n8n)
 for definitions.

**The pricing page is the source of truth**

Exact features per plan and edition can change. For the current breakdown, see the [pricing page](https://n8n.io/pricing/)
. This page explains what the plans and editions are and the main differences between them, not the full feature list.

Community edition[](https://docs.n8n.io/deploy/host-n8n/community-edition-features#community-edition)

------------------------------------------------------------------------------------------------------

The Community edition includes almost the complete feature set of n8n. It doesn't include these features:

*   [Custom variables](https://docs.n8n.io/build/code-in-n8n/define-custom-variables)
    
*   [Environments](https://docs.n8n.io/administer/use-source-control-and-environments)
    
*   [External secrets](https://docs.n8n.io/administer/manage-credentials/use-external-secret-stores)
    
*   [External storage for binary data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
    
*   [Log streaming](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems)
     ([Logging](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/set-up-logging)
     _is_ included)
    
*   [Multi-main mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#multi-main-setup)
     ([Queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
     _is_ included)
    
*   [Projects](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects)
    
*   SSO ([SAML](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso)
    , [LDAP](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/connect-ldap)
    )
    
*   Sharing ([workflows](https://docs.n8n.io/build/manage-workflows/share-with-others)
    , [credentials](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely)
    ) (Only the instance owner and the user who creates them can access workflows and credentials)
    
*   [Version control using Git](https://docs.n8n.io/administer/use-source-control-and-environments)
    

These features are available on self-hosted Business and Enterprise plans. Some are also available on n8n Cloud. See [pricing](https://n8n.io/pricing/)
 for the current breakdown.

Registered Community edition[](https://docs.n8n.io/deploy/host-n8n/community-edition-features#registered-community-edition)

----------------------------------------------------------------------------------------------------------------------------

Register your Community edition with your email to receive a free license key. It unlocks these features for the Community edition:

*   Folders: Organize your workflows into tidy folders
    
*   [Debug in editor](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
    : Copy and pin execution data when working on a workflow
    
*   [Custom execution data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    : Save, find, and annotate execution metadata
    

To register a new Community edition instance, select the option during your initial account creation.

To register an existing Community edition instance:

1.  Select the **three dots icon** ![three dots icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2773773108-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fjm0ZYRpZIPWge2ZSiDYO%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=02f47b9009a4c346ccb34c5c13c66476&sv=3) in the lower-left corner.
    
2.  Select **Settings** and then **Usage and plan**.
    
3.  Select **Unlock** to enter your email and then select **Send me a free license key**.
    
4.  Check your email for the account you entered.
    

Once you have a license key, activate it by selecting the button in the license email, or by going to **Options > Settings > Usage and plan** and selecting **Enter activation key**.

Business and Enterprise plans[](https://docs.n8n.io/deploy/host-n8n/community-edition-features#business-and-enterprise-editions)

---------------------------------------------------------------------------------------------------------------------------------

The Business and Enterprise plans unlock the paid features that the Community edition doesn't include, such as SSO, environments, external secrets, and log streaming. The Enterprise plan adds the most advanced features for security, scaling, and governance.

When you subscribe to a paid plan, you get a license key that unlocks the features for that plan. Add the key to your instance to activate it. For how to get and activate a key, see [Manage your license](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-your-license)
. For the features included in each plan, see the [pricing page](https://n8n.io/pricing/)
.

Which plan or edition is right for you[](https://docs.n8n.io/deploy/host-n8n/community-edition-features#which-edition-is-right-for-you)

----------------------------------------------------------------------------------------------------------------------------------------

*   Use the **Community edition** to self-host n8n for free with almost the complete feature set.
    
*   **Register** your Community edition (free) to also get folders, debug in editor, and custom execution data.
    
*   Subscribe to a **Business** or **Enterprise** plan when you need paid features like SSO, environments, projects, or external secrets. If you'd rather not manage infrastructure at all, consider [n8n Cloud](https://docs.n8n.io/deploy/use-n8n-cloud/start-your-free-trial)
     instead.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/community-edition-features#related-resources)

------------------------------------------------------------------------------------------------------

*   [Host n8n](https://docs.n8n.io/deploy/host-n8n)
    
*   [Install options](https://docs.n8n.io/deploy/host-n8n/install-options)
    
*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    
*   [Keep n8n running](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running)
    
*   [Understand the architecture](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture)
    
*   [Deploy as an OEM integration](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration)
    
*   [Deploy with the AI starter kit](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit)
    

[PreviousDeploy with the AI starter kit](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit)

Last updated 10 days ago

Was this helpful?