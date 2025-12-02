# aws-webapp-app
Part of my aws onboarding project. ([aws-webapp-app](https://github.com/Q29vbA/aws-webapp-app/) (this repo), [aws-webapp-manifests](https://github.com/Q29vbA/aws-webapp-manifests/), [aws-webapp-infra](https://github.com/Q29vbA/aws-webapp-infra/))

This repo contains the python flask app code, dependencies, and the Dockerfile

Using github actions pipeline, code goes through pylint, built and pushed to Amazon ECR

Resulting image is referenced in the Helm chart located in the manifests repo and deployed to a k3s cluster managed by ArgoCD

## Usage

To build and run locally:

```bash
docker build -t aws-webapp-app:latest .
docker run -p 8080:8080 aws-webapp-app:latest
