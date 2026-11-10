# OrderFlow — Kubernetes Infrastructure Lab

## Overview

OrderFlow is a sample e-commerce order processing
system used to practice production-oriented
DevOps and SRE engineering.

## Architecture

- Orders API — Python / FastAPI
- PostgreSQL — persistent order storage
- Redis — background task queue
- Worker — asynchronous order processing
- Kubernetes — container orchestration
- Prometheus — metrics collection
- Grafana — monitoring and visualization

## Infrastructure

- Kubernetes: Minikube
- Container runtime: Docker
- Local development: Windows + Docker Desktop

## Project goals

- Declarative Kubernetes configuration
- Containerization and image optimization
- Application deployment and scaling
- Health checks and self-healing
- Persistent storage
- CI/CD automation
- Monitoring and troubleshooting
- Kubernetes security

## Current status

- [x] Local Kubernetes cluster
- [x] OrderFlow namespace
- [x] Initial Orders API
- [ ] Docker image
- [ ] Kubernetes Deployment
- [ ] Kubernetes Service
