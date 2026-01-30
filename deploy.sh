#!/bin/bash

# Configuration
BUCKET_NAME="av-pool-cleaning-com"
DISTRIBUTION_ID="E23QUUF716MFDQ"
PROFILE="mediusa"

echo "🚀 Starting Deployment for AV Pool Cleaners..."

# 1. Sync files to S3
echo "📦 Syncing files to S3 bucket: $BUCKET_NAME..."
aws s3 sync . s3://$BUCKET_NAME \
    --profile $PROFILE \
    --exclude ".git/*" \
    --exclude "infra/*" \
    --exclude ".DS_Store" \
    --exclude "deploy.sh" \
    --delete

# 2. Force Content-Types for critical files (metadata-directive REPLACE)
echo "🛠️ Hardening MIME types..."
aws s3 cp s3://$BUCKET_NAME/ s3://$BUCKET_NAME/ --recursive --exclude "*" --include "*.html" --content-type "text/html; charset=utf-8" --metadata-directive REPLACE --profile $PROFILE
aws s3 cp s3://$BUCKET_NAME/ s3://$BUCKET_NAME/ --recursive --exclude "*" --include "*.css" --content-type "text/css" --metadata-directive REPLACE --profile $PROFILE
aws s3 cp s3://$BUCKET_NAME/ s3://$BUCKET_NAME/ --recursive --exclude "*" --include "*.js" --content-type "application/javascript" --metadata-directive REPLACE --profile $PROFILE

# 3. Invalidate CloudFront Cache
echo "🧹 Invalidating CloudFront cache: $DISTRIBUTION_ID..."
aws cloudfront create-invalidation \
    --profile $PROFILE \
    --distribution-id $DISTRIBUTION_ID \
    --paths "/*"

echo "✅ Deployment Complete! Changes should be live on avpoolcleaning.com shortly."
