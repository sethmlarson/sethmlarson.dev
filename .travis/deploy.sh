#!/bin/bash

set -exo pipefail

mkdir -p public/
gcloud builds submit --tag gcr.io/sethmlarson-dev/website
gcloud beta run deploy website --image gcr.io/sethmlarson-dev/website --platform managed --region us-central1
firebase deploy
