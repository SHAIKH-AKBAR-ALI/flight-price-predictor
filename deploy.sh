#!/bin/bash

# Cloud Run deployment script
echo "Deploying Flight Price Predictor to Cloud Run..."

# Build and deploy
gcloud run deploy flight-price \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 1 \
  --timeout 300 \
  --concurrency 10 \
  --max-instances 5 \
  --set-env-vars PYTHONUNBUFFERED=1 \
  --platform managed

echo "Deployment complete!"
echo "Your app is available at: https://flight-price-o63biaxwoa-el.a.run.app"