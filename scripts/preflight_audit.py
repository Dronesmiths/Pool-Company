import os
import re
import sys

# Configuration - Future agents should update these based on CLIENT_INTAKE.md
CLIENT_NAME = "Diaz Landscaping"
OLD_BRAND = "Reed and Sons"
FORBIDDEN_WORDS = ["Handyman", "Handy", "Home Service"] # Words from legacy templates to avoid
PHONE = "(661) 583-6000"
EMAIL = "brian@dronesmiths.com"
PRIMARY_DOMAIN = "d1sxjpzrvgytjj.cloudfront.net"

def print_banner(text):
    print("\n" + "="*60)
    print(f" {text}")
    print("="*60)

def audit_files(directory):
    errors = 0
    warnings = 0
    
    html_files = []
    for root, dirs, files in os.walk(directory):
        if any(d in root for d in [".git", ".gemini", "node_modules"]):
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    print(f"Auditing {len(html_files)} HTML files for brand integrity...")

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, directory)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        file_issues = []

        # 1. Leakage Check
        if OLD_BRAND.lower() in content.lower():
            file_issues.append(f"CRITICAL: Found legacy branding '{OLD_BRAND}'")
            errors += 1
            
        for word in FORBIDDEN_WORDS:
            if word.lower() in content.lower():
                file_issues.append(f"WARNING: Found legacy service term '{word}'")
                warnings += 1

        # 2. Identity Sync
        if PHONE not in content and "tel:" in content:
            # Check if there's a different phone number
            found_phones = re.findall(r'tel:(\d{10})', content)
            if found_phones and found_phones[0] != PHONE.replace("(", "").replace(")", "").replace(" ", "").replace("-", ""):
                 file_issues.append(f"WARNING: Phone number mismatch. Found {found_phones[0]}, expected {PHONE}")
                 warnings += 1

        # 3. Broken Links / Placeholders
        if 'href="#"' in content:
            file_issues.append("WARNING: Found placeholder link href='#'")
            warnings += 1
            
        # 4. Meta Quality
        if "<title>" not in content or "</title>" not in content:
            file_issues.append("ERROR: Missing <title> tag")
            errors += 1
        
        if 'name="description"' not in content:
            file_issues.append("WARNING: Missing meta description")
            warnings += 1

        # 5. Favicon Check
        if 'rel="icon"' not in content and 'rel="shortcut icon"' not in content:
            file_issues.append("WARNING: Missing favicon link")
            warnings += 1

        if file_issues:
            print(f"\n[!] {rel_path}:")
            for issue in file_issues:
                print(f"  - {issue}")

    return errors, warnings

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    print_banner(f"PRE-FLIGHT AUDIT: {CLIENT_NAME}")
    
    err, warn = audit_files(project_root)
    
    print_banner("AUDIT SUMMARY")
    print(f"Total Errors: {err}")
    print(f"Total Warnings: {warn}")
    
    if err > 0:
        print("\n[RESULT] FAIL: Critical errors found. Do not deploy.")
        sys.exit(1)
    elif warn > 0:
        print("\n[RESULT] PASS WITH WARNINGS: Review warnings before deployment.")
        sys.exit(0)
    else:
        print("\n[RESULT] PERFECT PASS: System is clean. Ready for deployment.")
        sys.exit(0)
