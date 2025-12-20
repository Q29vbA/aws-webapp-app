# aws-webapp-app
Part of my small aws base project. ([aws-webapp-app](https://github.com/Q29vbA/aws-webapp-app/) (this repo), [aws-webapp-manifests](https://github.com/Q29vbA/aws-webapp-manifests/), [aws-webapp-infra](https://github.com/Q29vbA/aws-webapp-infra/))

This repo contains the python flask app code, dependencies, and the Dockerfile

Using github actions pipeline, code goes through pylint, built and pushed to dockerhub.

Resulting image tag is updated in the helm chart located in the manifests repo

## Usage

To build and run locally:

```bash
docker build -t aws-webapp-app:latest .
docker run -p 8080:8080 aws-webapp-app:latest
```