# AI Pilots: Content & Newsletter Queue

Use this checklist to track the rollout of the 50 high-authority content pieces. Mark as `[x]` only after the page is live and CloudFront cache is invalidated.

## Phase 1: The Authority Foundation (1-10)
- [ ] **01: Cornerstone Guide** - The Ultimate Guide to Eco-Friendly Junk Removal in the Antelope Valley
- [ ] **02: Locality Anchor** - Why All Clean Junk Removal is Palmdale's Fastest Hauling Service
- [ ] **03: Service Deep Dive** - Furniture Removal: How to Safely Clear Out Your Home
- [ ] **04: Project Spotlight** - Massive Garage Cleanout in West Lancaster: A Before & After
- [ ] **05: PAA Capture** - How much does a full truckload of junk removal cost in Palmdale?
- [ ] **06: Service Deep Dive** - Appliance Hauling: Responsible Disposal of Refrigerators and Washers
- [ ] **07: Pro Tip** - 5 Things to Do Before Your Junk Removal Crew Arrives
- [ ] **08: Project Spotlight** - Post-Construction Debris Removal for Antelope Valley Renovations
- [ ] **09: PAA Capture** - Do junk removal companies take old tires or hazardous waste?
- [ ] **10: Locality Anchor** - Santa Clarita Hauling: Extending Service to the Santa Clarita Valley

## Phase 2: Strategic Expansion (11-30)
- [ ] **11: Locality Anchor** - Clearing Out in Rosamond: Efficient Hauling for Local Residents
- [ ] **12: PAA Capture** - What is the difference between hoarding cleanup and standard junk removal?
- [ ] **13: Service Deep Dive** - Commercial Junk Removal: Keeping Antelope Valley Businesses Clean
- [ ] **14: Project Spotlight** - Estate Cleanout Success Story: Compassionate and Rapid Service
- [ ] **15: Cornerstone Pillar** - The 2026 Homeowner's Guide to Property Decluttering
- [ ] **16-30:** ...

## Phase 3: Domain Dominance (31-50)
- [ ] **31:** ...
- [ ] **50:** ...

> [!IMPORTANT]
> **Deployment Rule**: Every time a checkbox is marked `[x]`, you must:
> 1. Sync the repo: `git add . && git commit -m "feat: deploy content piece #[XX]" && git push`
> 2. Sync S3: `aws s3 sync . s3://[BUCKET] --profile mediusa`
> 3. Invalidate: `aws cloudfront create-invalidation --distribution-id [ID] --paths "/news/*" "/blog/*"`
