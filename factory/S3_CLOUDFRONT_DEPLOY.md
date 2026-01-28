# AWS S3 & CloudFront Deployment Guide: AV Pool Bros

This guide provides the specific steps to deploy the AV Pool Bros website to AWS S3 and CloudFront.

## 1. Prerequisites
- AWS CLI installed and configured.
- AWS Profile `mediusa` with appropriate permissions.
- Remote Git Repository: `https://github.com/Dronesmiths/All-Clean_Junk_Removal.git`

## 2. Infrastructure Details
- **S3 Bucket**: `all-clean-junk-removal`
- **CloudFront Distribution ID**: `E33YEN9BC0LHET`

> [!CAUTION]
> **Check Before Syncing**: Always verify the Bucket Name and Distribution ID in `CLIENT_INTAKE.md` before deploying. Never assume the bucket name from a template is correct for a new client.

## 3. Deployment Workflow

### Step 1: Commit Changes
```bash
git add .
git commit -m "feat: rebrand to AV Pool Bros and update contact info"
git push
```

### Step 2: Pre-Flight Audit (MANDATORY)
Run the automated audit script to verify brand fidelity and link health.
```bash
python3 scripts/preflight_audit.py
```

### Step 3: Sync to S3 (Dry Run First)
Always run with `--dryrun` first to prevent infrastructure collisions.
```bash
aws s3 sync . s3://av-pool-bros --exclude ".git/*" --profile mediusa --dryrun
```

If the dry run is successful:
```bash
aws s3 sync . s3://av-pool-bros \
    --exclude ".git/*" \
    --exclude ".DS_Store" \
    --profile mediusa
```

### Step 4: Invalidate CloudFront Cache
```bash
aws cloudfront create-invalidation \
    --distribution-id ERINMCTBFMBEY \
    --paths "/*" \
    --profile mediusa
```

## 4. Verification
After deployment, verify the changes at the production URL:
- Check for "AV Pool Bros" branding.
- Verify the phone number: **661-382-4566**.
- Confirm the Green and Yellow theme is active.
