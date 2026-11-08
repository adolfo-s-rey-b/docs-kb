For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/environments/git-based-promotion.md)
.

With Git-based promotion, changes travel between n8n instances through a Git repository. Each environment is a repository and branch.

**Preview status**

Environments are in Preview and may change in future releases. Try them on test instances before you set them up for your production instances.

What n8n writes to the repository[](https://docs.n8n.io/administer/environments/git-based-promotion#what-n8n-writes-to-the-repository)

---------------------------------------------------------------------------------------------------------------------------------------

n8n stores promoted content in an `n8n/` folder at the root of the repository. The folder holds an [n8n package](https://docs.n8n.io/build/manage-workflows/n8n-packages)
. n8n exports it when you promote and imports it when you apply. n8n doesn't change anything outside that folder, so the repository can hold other files, such as CI configuration.

Direct commits and feature branches[](https://docs.n8n.io/administer/environments/git-based-promotion#direct-commits-and-feature-branches)

-------------------------------------------------------------------------------------------------------------------------------------------

Depending on its settings, the environment an instance promotes changes to either:

*   Commits directly to its branch.
    
*   Pushes each promote to a feature branch named `n8n-promotion/<timestamp>`, based on its branch. n8n never force-pushes. For feature branches, the environment's branch must already exist on the Git host.
    

Instances that apply from the environment read its branch, so they see changes from a feature branch only after someone merges it.

Providers[](https://docs.n8n.io/administer/environments/git-based-promotion#providers)

---------------------------------------------------------------------------------------

A provider holds the details n8n uses to connect and authenticate to your Git host. Several environments on an instance can use the same provider. The provider type decides which features you get:

Feature

Generic Git

GitLab

Authentication

SSH key, or username and access token

Access token

Pick repositories and branches from a list

No

Yes

Promotion reviews

No

Yes: GitLab merge requests synced to n8n, with a visual diff of the changes in **Reviews**

GitHub, Bitbucket, and other Git hosts work through Generic Git, without repository lists or promotion reviews.

Self-hosted n8n[](https://docs.n8n.io/administer/environments/git-based-promotion#self-hosted-n8n)

---------------------------------------------------------------------------------------------------

*   If your GitLab instance is on an internal network, allow it for GitLab API calls in [SSRF protection](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection)
     with `N8N_SSRF_ALLOWED_HOSTNAMES` or `N8N_SSRF_ALLOWED_IP_RANGES`.
    
*   If your Git host uses a certificate from a private certificate authority, set `GIT_SSL_CAINFO` or `GIT_SSL_CAPATH` for Git, and [configure custom certificate authorities](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities)
     for API calls.
    
*   To get detailed logs, set `N8N_LOG_SCOPES=promotions`.
    

Troubleshooting[](https://docs.n8n.io/administer/environments/git-based-promotion#troubleshooting)

---------------------------------------------------------------------------------------------------

### Could not complete the Git operation[](https://docs.n8n.io/administer/environments/git-based-promotion#could-not-complete-the-git-operation)

Check:

*   The authentication details in the provider are correct and haven't expired.
    
*   For SSH, the deploy key has write access.
    
*   The branch exists on the Git host.
    
*   The repository URL has the right format for the authentication type. See [Generic Git](https://docs.n8n.io/administer/environments/git-based-promotion/generic-git)
    .
    

In this section[](https://docs.n8n.io/administer/environments/git-based-promotion#in-this-section)

---------------------------------------------------------------------------------------------------

*   [Generic Git](https://docs.n8n.io/administer/environments/git-based-promotion/generic-git)
    : connect any Git repository over SSH or HTTPS.
    
*   [GitLab](https://docs.n8n.io/administer/environments/git-based-promotion/gitlab)
    : connect GitLab with an access token, and review promotions as merge requests.
    

Related resources[](https://docs.n8n.io/administer/environments/git-based-promotion#related-resources)

-------------------------------------------------------------------------------------------------------

*   [Environments](https://docs.n8n.io/administer/environments)
    
*   [Plan your environments](https://docs.n8n.io/administer/environments/plan-your-environments)
    
*   [Your first promotion](https://docs.n8n.io/administer/environments/first-promotion)
    
*   [Promote changes](https://docs.n8n.io/administer/environments/promote-changes)
    
*   [Apply changes](https://docs.n8n.io/administer/environments/apply-changes)
    
*   [Promotion reviews](https://docs.n8n.io/administer/environments/promotion-reviews)
    
*   [Known limitations](https://docs.n8n.io/administer/environments/known-limitations)
    
*   [Upgrade from Environments (Classic)](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic)
    

[PreviousPromotion reviews](https://docs.n8n.io/administer/environments/promotion-reviews)
[NextGeneric Git](https://docs.n8n.io/administer/environments/git-based-promotion/generic-git)

Last updated 5 days ago

Was this helpful?