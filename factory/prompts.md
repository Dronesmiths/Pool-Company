# Workflow-Factory V3: Rebranding Prompts & Logic

Use these prompts to ensure high-fidelity rebranding when transitioning a project from the Gold Master template to a new niche.

## 1. Aesthetic Palette Synchronization
> [!IMPORTANT]
> Always check for secondary CSS definitions that might override root variables.

**Prompt**: "Review `styles.css` for any hardcoded gradients or color hex codes that override the `:root` variables. Specifically, look for components like `.stats-bar`, `.page-hero`, or any 'New Section' blocks that might have been added in post-production. Synchronize all backgrounds to `var(--primary-blue)` or the specific brand primary."

## 2. Hero Eyebrow Readability
**Prompt**: "When updating page heroes, ensure the 'Eyebrow' text (e.g., 'Maintenance Guide') has a subtle text-shadow or high-contrast color (white on dark blue) to ensure readability against dynamic background images. Use `text-shadow: 0 2px 4px rgba(0,0,0,0.5);` as a baseline."

## 3. Mobile Typography Scaling
**Prompt**: "Audit the mobile media queries (max-width: 768px). Update `h1` and `h2` font sizes to be responsive (e.g., 2.2rem for h1). Ensure `.blog-content` or similar main containers have at least `20px` horizontal padding to prevent 'edge-bleed' where text touches the device border."

## 4. Logo & Identity Verification
**Prompt**: "Verify that the social metadata (`og:image`) and the footer logo are synchronized to the authoritative asset in `factory/brand_assets/`. Eliminate placeholders and ensure the filename `av-pool-bros-logo.png` (or the niche equivalent) is consistent across all pages."
