# aws-webapp-app
Part of my small aws base project. ([aws-webapp-app](https://github.com/Q29vbA/aws-webapp-app/) (this repo), [aws-webapp-manifests](https://github.com/Q29vbA/aws-webapp-manifests/), [aws-webapp-infra](https://github.com/Q29vbA/aws-webapp-infra/))


built this project mainly to experiment hands-on a bit with aws + terraform (instead of keep reading about it), intentionally simple setup

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

## future tweaks
- add a tiny test (pytest) so pylint isn’t the only gate
- multi-arch image? not sure i need it
- add a health endpoint instead of only “/”
