# aws-webapp-app
Part of my small aws base project. ([aws-webapp-app](https://github.com/Q29vbA/aws-webapp-app/) (this repo), [aws-webapp-manifests](https://github.com/Q29vbA/aws-webapp-manifests/), [aws-webapp-infra](https://github.com/Q29vbA/aws-webapp-infra/))

simple python flask app + dockerfile. ci uses github actions: pylint first, then buildx builds and pushes to the registry, then opens a PR to bump the tag in the manifests repo.

## ci secrets (set in repo settings → actions secrets):
- `REGISTRY_USERNAME` / `REGISTRY_PASSWORD` for docker login
- `MANIFESTS_REPO_TOKEN` to push a branch + open a PR in the manifests repo

note: demo repo, so after all worked - i removed the secrets (and access tokens revoked), so the actions pipeline won’t work until you add them back.

## usage

local quick run:

```bash
docker build -t aws-webapp-app:latest .
docker run -p 8080:8080 aws-webapp-app:latest
```

## future tweaks (maybe)
- add a tiny test (pytest) so pylint isn’t the only gate
- multi-arch image? not sure i need it
- add a health endpoint instead of only “/”
