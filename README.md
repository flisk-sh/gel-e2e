# gel-e2e

Sandbox for the end-to-end check of GEL and Cilytics. Its main branch carries three planted defects on purpose,
so every GEL run on main reports them and https://cilytics.flisk.si shows them for this repo:

- `.github/workflows/planted.yml` uses an action by tag (pinned-actions) and has no `permissions` (workflow-permissions).
- This link points to a file that is not in the repo (dead-links): [missing page](docs/missing.md).

Do not fix them. The check in flisk-sh/cilytics fails when they stop showing up.

## Links
[setup](docs/setup.md) [api](docs/api-guide.md) [faq](docs/faq.md)
[arch](docs/architecture/overview.md) [changelog](CHANGELOG.md) [logo](assets/logo.png)
