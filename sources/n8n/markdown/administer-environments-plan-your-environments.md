For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/environments/plan-your-environments.md)
.

Decide which instances promote changes, which instances apply them, and which repository and branch stand for each environment before you set anything up.

**Preview status**

Environments are in Preview and may change in future releases. Try them on test instances before you set them up for your production instances.

How instances and environments relate[](https://docs.n8n.io/administer/environments/plan-your-environments#how-instances-and-environments-relate)

--------------------------------------------------------------------------------------------------------------------------------------------------

Each instance belongs to one environment and promotes to the next. You configure this on each instance separately in **Settings** > **Environments**, with up to two environment configurations:

*   **Apply:** the environment the instance belongs to. The instance applies changes from it.
    
*   **Promote:** the next environment. The instance promotes changes to it.
    

With [Git-based promotion](https://docs.n8n.io/administer/environments/git-based-promotion)
, each environment configuration uses a provider, repository, and branch. They don't have to match across directions or instances, and several configurations can share a provider. An instance can apply from one repository and promote to another, or use different branches of the same repository. Changes reach the next instance once they're on the branch it applies from, whether n8n commits them there directly or someone merges them in. To approve changes before they reach the branch, use [promotion reviews](https://docs.n8n.io/administer/environments/promotion-reviews)
 with GitLab.

Name each environment after its step in your release process, such as Staging or Production. The patterns below are common setups, not the only ones.

Development and production[](https://docs.n8n.io/administer/environments/plan-your-environments#development-and-production)

----------------------------------------------------------------------------------------------------------------------------

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-7379b9ce30b1c9c9cc2d7479b1952295f451a03d%252Fenvironments-dev-prod.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9fc29aac748356656d56695226ad1747&sv=3)

The development instance promotes to the Production environment, and the production instance applies from it

Use this pattern when one team builds on one instance and runs workflows on another.

Instance

Promote changes to

Apply changes from

Development

Production: repository `acme/n8n`, branch `main`

None

Production

None

Production: repository `acme/n8n`, branch `main`

On the development instance, add a Production promote environment configuration. On the production instance, add a Production apply environment configuration, pointing to the same repository and branch.

Development, staging, and production[](https://docs.n8n.io/administer/environments/plan-your-environments#development-staging-and-production)

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-0b86e3e7988667320a38114bb4e49a396840b2e8%252Fenvironments-dev-staging-prod.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=225ea291a4c71e6eef565684802f3437&sv=3)

The staging instance applies from the Staging environment and promotes to the Production environment

Use this pattern when you test changes on a staging instance before they reach production. The staging instance has two environments: it applies changes from Staging and promotes changes to Production.

Instance

Promote changes to

Apply changes from

Development

Staging: branch `staging`

None

Staging

Production: branch `main`

Staging: branch `staging`

Production

None

Production: branch `main`

On the development instance, add a Staging promote environment configuration. On the staging instance, add a Staging apply and a Production promote environment configuration. On the production instance, add a Production apply environment configuration. The configurations for the same environment point to the same repository and branch.

Staging and Production can be two branches in one repository, as in the table, or branches in two repositories. Use two repositories if different teams own staging and production, or if they need different access rules on your Git host.

Set up a new target instance[](https://docs.n8n.io/administer/environments/plan-your-environments#set-up-a-new-target-instance)

--------------------------------------------------------------------------------------------------------------------------------

To bring your work to a new target instance for the first time, follow [Your first promotion](https://docs.n8n.io/administer/environments/first-promotion)
. If your instances use Environments (Classic), follow [Migrate from Environments (Classic)](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic#migrate-from-environments-classic)
.

Protect the instances that only apply[](https://docs.n8n.io/administer/environments/plan-your-environments#protect-the-instances-that-only-apply)

--------------------------------------------------------------------------------------------------------------------------------------------------

Turn on **Protected instance** on instances that only apply changes, such as production. See [Protect a production instance](https://docs.n8n.io/administer/environments/protect-a-production-instance)
.

Related resources[](https://docs.n8n.io/administer/environments/plan-your-environments#related-resources)

----------------------------------------------------------------------------------------------------------

*   [Environments](https://docs.n8n.io/administer/environments)
    
*   [Your first promotion](https://docs.n8n.io/administer/environments/first-promotion)
    
*   [Protect a production instance](https://docs.n8n.io/administer/environments/protect-a-production-instance)
    
*   [Promote changes](https://docs.n8n.io/administer/environments/promote-changes)
    
*   [Apply changes](https://docs.n8n.io/administer/environments/apply-changes)
    
*   [Promotion reviews](https://docs.n8n.io/administer/environments/promotion-reviews)
    
*   [Git-based promotion](https://docs.n8n.io/administer/environments/git-based-promotion)
    
*   [Known limitations](https://docs.n8n.io/administer/environments/known-limitations)
    
*   [Upgrade from Environments (Classic)](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic)
    

[PreviousEnvironments](https://docs.n8n.io/administer/environments)
[NextYour first promotion](https://docs.n8n.io/administer/environments/first-promotion)

Last updated 5 days ago

Was this helpful?