#!/bin/bash

set -exo pipefail

gcloud config set project sethmlarson-dev
gcloud builds submit --tag gcr.io/sethmlarson-dev/website
gcloud beta run deploy pkgs-crosstown-dev \
    --image gcr.io/sethmlarson-dev/website \
    --platform=managed \
    --region=us-central1 \
    --timeout=10 \
    --memory=128Mi \
    --allow-unauthenticated
