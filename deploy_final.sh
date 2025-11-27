#!/bin/bash

echo "🚀 Deploying Flight Price Predictor to Cloud Run..."

# Deploy with optimized settings
gcloud run deploy flight-price \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --timeout 300 \
  --cpu 1 \
  --concurrency 10 \
  --max-instances 5 \
  --set-env-vars PYTHONUNBUFFERED=1

echo "✅ Deployment complete!"
echo "🌐 Your app: https://flight-price-o63biaxwoa-el.a.run.app"