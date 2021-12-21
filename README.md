# Log request headers

Will log the incoming HTTP request headers for debugging purposes.

## Run

Can be run locally in a [Virtualenv](https://virtualenv.pypa.io/en/latest/) or in a Docker container (below)

```bash
virtualenv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt
python app.py
```

Dockerfile for building Docker image included.

```bash
docker build . --tag log-request-headers:latest
docker run log-request-headers:latest
```

## Deploy

Resource manifest for k8s included.

```bash
kubectl apply -f deployment.yaml
```
