
import os

blog_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | All Clean Junk Removal Blog</title>
    <meta name="description" content="{description}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.allcleanjunkremoval.com/blog/{slug}/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="/images/all-clean-logo-footer.webp">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <link rel="stylesheet" href="/css/styles.css?v=2.1">
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
</head>

<body>

    <!-- Header -->
    <header>
        <div class="container">
            <a href="/" class="logo">All Clean <span>Junk Removal</span></a>
            <nav class="nav-menu">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/services/">Services</a></li>
                    <li><a href="/about/">About Us</a></li>
                    <li><a href="/blog/" class="active">Blog</a></li>
                    <li><a href="/contact/">Contact</a></li>
                </ul>
            </nav>
            <div class="header-actions">
                <a href="tel:6613824566" class="phone-link mobile-hide"><i class="fas fa-phone"></i> 661-382-4566</a>
                <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
                <button class="mobile-menu-btn" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background-image: linear-gradient(rgba(27, 77, 46, 0.9), rgba(27, 77, 46, 0.8)), url('/images/landscape-hero-v2.png'); padding: 80px 0;">
        <div class="container" style="text-align: center;">
            <span style="color: var(--primary-apple); font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">{category}</span>
            <h1 style="color: white; font-size: 3rem; margin-top: 10px; max-width: 900px; margin-left: auto; margin-right: auto;">{title}</h1>
            <p style="color: rgba(255,255,255,0.9); margin-top: 15px;">Published by All Clean Junk Removal</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 60px 0; background: #fff;">
        <div class="container" style="max-width: 800px;">
            <div class="blog-content" style="line-height: 1.8; color: #444; font-size: 1.1rem;">
                <p class="lead" style="font-size: 1.3rem; color: var(--primary-navy); font-weight: 600; margin-bottom: 30px;">
                    {lead_text}
                </p>
                
                {content_body}

                <div style="background: #f0f8ec; padding: 30px; border-left: 5px solid var(--primary-green); margin: 40px 0; border-radius: 4px;">
                    <h3 style="margin-top: 0; color: var(--primary-green);">Need Help Reclaiming Your Space?</h3>
                    <p style="margin-bottom: 15px;">We serve the entire Antelope Valley with fast, professional junk removal.</p>
                    <a href="tel:6613824566" class="btn btn-primary">Call 661-382-4566</a>
                </div>

                <hr style="margin: 50px 0; border: 0; border-top: 1px solid #eee;">
                
                <div style="font-size: 0.9rem; color: #666;">
                    <p><strong>Tags:</strong> {tags}</p>
                    <p><a href="/blog/">&larr; Back to All Articles</a></p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="av-cta-section" style="padding: 80px 0; text-align: center; background: linear-gradient(rgba(27, 77, 46, 0.95), rgba(27, 77, 46, 0.95)), url('/images/landscape-hero-v2.png'); background-size: cover; background-position: center; color: white;">
        <div class="container">
            <h2 style="font-size: 2.5rem; margin-bottom: 20px; color: white;">Ready to Clear the Clutter?</h2>
            <p style="font-size: 1.2rem; margin-bottom: 30px; opacity: 0.9;">
                Get your free estimate today. Same-day service available in Palmdale & Lancaster.
            </p>
            <a href="tel:6613824566" class="btn btn-secondary" style="font-size: 1.3rem; padding: 18px 50px; background: white; color: var(--primary-green); font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">
                Call 661-382-4566
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="aw-footer">
        <div class="container aw-footer-inner">
            <div class="aw-footer-brand">
                <img src="/images/all-clean-logo-footer.webp" alt="All Clean Junk Removal Logo" style="max-width: 250px; margin-bottom: 15px;">
                <p>Your trusted hauling services provider in the Antelope Valley.</p>
            </div>
            <div class="aw-footer-contact">
                <h4 style="color: white; margin-bottom: 15px; font-size: 1.1rem;">Contact Us</h4>
                <p class="aw-footer-phone"><a href="tel:6613824566">661-382-4566</a></p>
                <p class="aw-footer-email">Palmdale & Lancaster</p>
            </div>
            <div class="aw-footer-services">
                <h4>Our Services</h4>
                <ul>
                    <li><a href="/services/furniture-removal/">Furniture Removal</a></li>
                    <li><a href="/services/appliance-hauling/">Appliance Hauling</a></li>
                    <li><a href="/services/property-cleanouts/">Property Cleanouts</a></li>
                </ul>
            </div>
            <div class="aw-footer-locations">
                <h4>Service Areas</h4>
                <ul>
                    <li><a href="/locations/palmdale/">Palmdale, CA</a></li>
                    <li><a href="/locations/lancaster/">Lancaster, CA</a></li>
                    <li><a href="/locations/quartz-hill/">Quartz Hill</a></li>
                </ul>
            </div>
        </div>
        <div class="aw-footer-bottom">
            <p>© <span id="year"></span> All Clean Junk Removal. All rights reserved. | <a href="/privacy/">Privacy Policy</a> | <a href="/terms/">Terms of Service</a></p>
        </div>
    </footer>
    <script src="/js/script.js"></script>
</body>
</html>
"""

articles = [
    {
        "slug": "garage-cleanout-west-lancaster",
        "title": "Massive Garage Cleanout in West Lancaster: A Before & After",
        "category": "Project Spotlight",
        "description": "See how we transformed a cluttered 2-car garage in West Lancaster into a usable workspace in just 3 hours.",
        "lead_text": "We recently helped a West Lancaster homeowner who hadn't seen their garage floor in five years. The goal? reclaim the space for a new workshop. The result? Total transformation.",
        "tags": "Garage Cleanout, Lancaster, Project Spotlight, Before and After",
        "content_body": """
            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">The Problem: 5 Years of Accumulation</h2>
            <p>Life happens. Boxes from moving, old holiday decorations, and broken appliances can stack up quickly. This client in West Lancaster needed a fresh start but was overwhelmed by the sheer volume of stuff.</p>
            
            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">The Solution: All Hands on Deck</h2>
            <p>Our team arrived at 8:00 AM. By 11:00 AM, the garage was empty and swept clean. We sorted items into three categories:</p>
            <ul style="margin-bottom: 30px; list-style-type: none; padding-left: 0;">
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: var(--primary-green); position: absolute; left: 0; top: 5px;"></i> <strong>Donation:</strong> Usable tools and decor went to local charities.</li>
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: var(--primary-green); position: absolute; left: 0; top: 5px;"></i> <strong>Recycling:</strong> Cardboard and scrap metal were processed at the recycling center.</li>
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: var(--primary-green); position: absolute; left: 0; top: 5px;"></i> <strong>Disposal:</strong> Real trash was hauled to the landfill responsibly.</li>
            </ul>

            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">Client Reaction</h2>
            <p><em>"I can't believe how fast you guys worked. I finally have my garage back!"</em> — Start your own transformation today with our <a href="/services/property-cleanouts/" style="color: var(--primary-green); font-weight: 600;">Property Cleanout services</a>.</p>
        """
    },
    {
        "slug": "cost-of-junk-removal-palmdale",
        "title": "How Much Does a Full Truckload of Junk Removal Cost in Palmdale?",
        "category": "Pricing & FAQ",
        "description": "Understanding junk removal pricing in the Antelope Valley. What factors into the cost and how to get the best value.",
        "lead_text": "One of the most common questions we get is, 'How much will this cost?' Transparency is key to our business, so let's break down how junk removal pricing works in Palmdale and Lancaster.",
        "tags": "Pricing, Cost, Palmdale, FAQ",
        "content_body": """
            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">Volume-Based Pricing</h2>
            <p>Most professional junk removal companies, including All Clean, charge based on how much space your items take up in the truck. You don't pay for the time it takes us to load (usually) or the weight (unless it's dense material like concrete).</p>
            
            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">Key Pricing Factors</h2>
            <ul style="margin-bottom: 30px; list-style-type: none; padding-left: 0;">
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-dollar-sign" style="color: var(--primary-green); position: absolute; left: 0; top: 5px;"></i> <strong>Volume:</strong> Is it a 1/4 truck, 1/2 truck, or full load?</li>
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-dollar-sign" style="color: var(--primary-green); position: absolute; left: 0; top: 5px;"></i> <strong>Access:</strong> Are the items in a driveway or a 3rd-floor apartment?</li>
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-dollar-sign" style="color: var(--primary-green); position: absolute; left: 0; top: 5px;"></i> <strong>Material:</strong> Hazardous materials or extremely heavy items may incur surcharges.</li>
            </ul>

            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">Get a Firm Quote</h2>
            <p>We believe in no surprises. That's why we offer free, no-obligation estimates. Send us a photo or <a href="/contact/" style="color: var(--primary-green); font-weight: 600;">contact us</a> to schedule an in-person quote today.</p>
        """
    },
    {
        "slug": "appliance-hauling-guide",
        "title": "Appliance Hauling: Responsible Disposal of Refrigerators and Washers",
        "category": "Service Deep Dive",
        "description": "Old appliances are heavy and can be hazardous to the environment. Learn how we safely haul and recycle refrigerators, washers, and dryers.",
        "lead_text": "Upgrading your kitchen or laundry room? Dealing with the old appliances is the hardest part. Here is why you should leave appliance hauling to the professionals.",
        "tags": "Appliance Removal, Recycling, Safety, Guide",
        "content_body": """
            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">The Hazards of Old Appliances</h2>
            <p>Refrigerators and freezers contain refrigerants (freon) that must be captured and disposed of by certified facilities. Simply leaving them on the curb can result in fines and environmental damage. Washers and dryers are heavy, awkward, and can easily scratch floors or damage walls during removal.</p>
            
            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">Our Safe Removal Process</h2>
            <ol style="margin-bottom: 30px; padding-left: 20px;">
                <li style="margin-bottom: 15px;"><strong>Disconnect:</strong> We ensure units are safely unplugged and disconnected (for simple connections).</li>
                <li style="margin-bottom: 15px;"><strong>Protect:</strong> We use dollies, straps, and floor protection to keep your home safe.</li>
                <li style="margin-bottom: 15px;"><strong>recycle:</strong> We transport units to certified metal recyclers who handle hazardous components properly.</li>
            </ol>

            <h2 style="color: var(--primary-navy); margin-top: 40px; margin-bottom: 20px;">Schedule Your Pickup</h2>
            <p>Don't risk your back or your floors. Let us handle the heavy lifting. Learn more about our <a href="/services/appliance-hauling/" style="color: var(--primary-green); font-weight: 600;">Appliance Hauling services</a>.</p>
        """
    }
]

def generate_articles():
    base_dir = "blog"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for article in articles:
        # Create directory
        article_dir = os.path.join(base_dir, article['slug'])
        if not os.path.exists(article_dir):
            os.makedirs(article_dir)
            
        # Create HTML
        html_content = blog_template.format(
            title=article['title'],
            description=article['description'],
            slug=article['slug'],
            category=article['category'],
            lead_text=article['lead_text'],
            content_body=article['content_body'],
            tags=article['tags']
        )
        
        # Write file
        file_path = os.path.join(article_dir, "index.html")
        with open(file_path, "w") as f:
            f.write(html_content)
        
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    generate_articles()
