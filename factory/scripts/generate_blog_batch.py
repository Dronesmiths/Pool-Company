
import os

blog_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AV Pool Bros News</title>
    <meta name="description" content="{description}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://avpoolbros.com/blog/{slug}/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="/images/av-pool-bros-logo.png">

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
            <a href="/" class="logo">AV <span>Pool Bros</span></a>
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
                <a href="tel:6614984444" class="phone-link mobile-hide"><i class="fas fa-phone"></i> (661) 498-4444</a>
                <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
                <button class="mobile-menu-btn" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background-image: linear-gradient(rgba(0, 119, 190, 0.9), rgba(0, 119, 190, 0.8)), url('/images/pool-blue-hero.png'); padding: 80px 0; background-size: cover; background-position: center;">
        <div class="container" style="text-align: center;">
            <span style="color: #b0e0e6; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">{category}</span>
            <h1 style="color: white; font-size: 3rem; margin-top: 10px; max-width: 900px; margin-left: auto; margin-right: auto;">{title}</h1>
            <p style="color: rgba(255,255,255,0.9); margin-top: 15px;">Published by AV Pool Bros</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 60px 0; background: #fff;">
        <div class="container" style="max-width: 800px;">
            <div class="blog-content" style="line-height: 1.8; color: #444; font-size: 1.1rem;">
                <p class="lead" style="font-size: 1.3rem; color: #0077be; font-weight: 600; margin-bottom: 30px;">
                    {lead_text}
                </p>
                
                {content_body}

                <div style="background: #f0faff; padding: 30px; border-left: 5px solid #0077be; margin: 40px 0; border-radius: 4px;">
                    <h3 style="margin-top: 0; color: #0077be;">Ready for Crystal Clear Water?</h3>
                    <p style="margin-bottom: 15px;">We serve the entire Antelope Valley with professional pool cleaning and maintenance.</p>
                    <a href="tel:6614984444" class="btn btn-primary">Call (661) 498-4444</a>
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
    <section class="av-cta-section" style="padding: 80px 0; text-align: center; background: linear-gradient(rgba(0, 119, 190, 0.95), rgba(0, 119, 190, 0.95)), url('/images/pool-blue-hero.png'); background-size: cover; background-position: center; color: white;">
        <div class="container">
            <h2 style="font-size: 2.5rem; margin-bottom: 20px; color: white;">Need a Professional Pool Tech?</h2>
            <p style="font-size: 1.2rem; margin-bottom: 30px; opacity: 0.9;">
                Get your free estimate today. Weekly service available in Palmdale & Lancaster.
            </p>
            <a href="tel:6614984444" class="btn btn-secondary" style="font-size: 1.3rem; padding: 18px 50px; background: white; color: #0077be; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">
                Call (661) 498-4444
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="aw-footer">
        <div class="container aw-footer-inner">
                <div class="aw-footer-brand" style="margin-bottom: 30px;">
                    <img src="/images/av-pool-bros-logo.png" alt="AV Pool Bros - Professional Pool Cleaning & Maintenance" style="max-width: 200px; margin-bottom: 20px;">
                    <p style="opacity: 0.8; line-height: 1.6;">Your trusted pool cleaning and maintenance provider in the Antelope Valley. Quality craftsmanship, reliable service.</p>
                </div>
            <div class="aw-footer-contact">
                <h4 style="color: white; margin-bottom: 15px; font-size: 1.1rem;">Contact Us</h4>
                <p class="aw-footer-phone"><a href="tel:6614984444">(661) 498-4444</a></p>
                <p class="aw-footer-email">Palmdale & Lancaster</p>
            </div>
            <div class="aw-footer-services">
                <h4>Our Services</h4>
                <ul>
                    <li><a href="/services/pool-cleaning/">Pool Cleaning</a></li>
                    <li><a href="/services/chemical-balancing/">Chemical Balancing</a></li>
                    <li><a href="/services/filter-equipment-repair/">Equipment Repair</a></li>
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
            <p>© <span id="year"></span> AV Pool Bros. All rights reserved. | <a href="/privacy/">Privacy Policy</a> | <a href="/terms/">Terms of Service</a></p>
        </div>
    </footer>
    <script src="/js/script.js"></script>
</body>
</html>
"""

articles = [
    {
        "slug": "ultimate-pool-maintenance-guide-antelope-valley",
        "title": "The Ultimate Guide to Pool Maintenance in the Antelope Valley",
        "category": "Maintenance Guide",
        "description": "Expert pool care tips for the High Desert climate. Learn how to keep your pool crystal clear in Palmdale and Lancaster's unique environment.",
        "lead_text": "Maintaining a pool in the Antelope Valley comes with unique challenges, from extreme summer heat to high winds and dust. This guide covers the essentials of keeping your water sparkling year-round.",
        "tags": "Pool care, Antelope Valley, Maintenance, High Desert",
        "content_body": '''
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">The High Desert Challenge</h2>
            <p>Antelope Valley pool owners face intensified evaporation and rapid chemical depletion due to our dry air and high UV index. Without a consistent maintenance plan, a clear pool can turn green in just a few days during a heatwave.</p>
            
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Top Maintenance Pillars</h2>
            <ul style="margin-bottom: 30px; list-style-type: none; padding-left: 0;">
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: #0077be; position: absolute; left: 0; top: 5px;"></i> <strong>Filtration:</strong> Run your pump 8-10 hours a day in summer to ensure proper turnover.</li>
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: #0077be; position: absolute; left: 0; top: 5px;"></i> <strong>Chemical Balance:</strong> Test PH and Chlorine at least twice a week.</li>
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: #0077be; position: absolute; left: 0; top: 5px;"></i> <strong>Circulation:</strong> Ensure all jets are angled correctly to avoid 'dead spots' where algae grows.</li>
            </ul>

            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Dealing with Wind and Dust</h2>
            <p>Our valley's famous wind storms dump massive amounts of organic debris and fine dust into pools. Regular basket emptying and filter cleaning are mandatory to prevent equipment strain.</p>
            
            <p>Need professional help? <a href="/services/pool-cleaning/" style="color: #0077be; font-weight: 600;">Explore our weekly cleaning services</a> to take the stress off your hands.</p>
        '''
    },
    {
        "slug": "why-av-pool-bros-top-rated-palmdale",
        "title": "Why AV Pool Bros is Palmdale's Top Rated Pool Service",
        "category": "Company News",
        "description": "Discover what sets AV Pool Bros apart from other pool companies in Lancaster and Palmdale. Reliability, expertise, and community trust.",
        "lead_text": "In a market full of unreliable 'pool guys,' AV Pool Bros has built a reputation on professional standards and crystal clear results.",
        "tags": "Palmdale, Reliability, Pool Service, Customer Success",
        "content_body": '''
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Consistency is Key</h2>
            <p>The number one complaint homeowners have about pool services is lack of consistency. We pride ourselves on showing up on your scheduled day, every single week. Our technicians are local, trained, and committed to your pool's health.</p>
            
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Expert Diagnostics</h2>
            <p>We don't just 'scoop and go.' We monitor your equipment performance, checking for leaks, unusual pump noises, and filter efficiency. Catching a small leak today saves you thousands in repairs tomorrow.</p>

            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Antelope Valley Roots</h2>
            <p>As a local company, we know exactly what the Palmdale wind does to your phosphate levels. We aren't a national franchise; we are your neighbors who happen to be experts in pool science.</p>
        '''
    },
    {
        "slug": "chemical-balancing-science-clear-water",
        "title": "Chemical Balancing: The Science of Crystal Clear Water",
        "category": "Expert Tips",
        "description": "Understanding the chemistry behind a healthy pool. Learn how to manage PH, Chlorine, and Alkalinity for a safe swimming environment.",
        "lead_text": "Clear water doesn't always mean healthy water. Achieving the perfect balance is a science that keeps your swimmers safe and your equipment long-lasting.",
        "tags": "Water Chemistry, PH balance, Chlorine, Pool Safety",
        "content_body": '''
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">The PH Scale and Your Pool</h2>
            <p>PH is the most important factor in pool chemistry. If it's too high, your chlorine becomes ineffective. If it's too low, the water becomes acidic and eats away at your pool heater and liner. We aim for a perfect 7.4 to 7.6 range.</p>
            
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Chlorine Myths</h2>
            <p>That 'pool smell' isn't actually chlorine—it's chloramines (combined chlorine) indicating that your pool actually needs MORE sanitizer to break down organic matter. Proper balancing ensures your water smells fresh and stays sanitized.</p>
            
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Phosphates: The Algae Food</h2>
            <p>Dust storms in Lancaster bring in high phosphate levels. Think of phosphates as fertilizer for algae. Even with high chlorine, if your phosphates are high, you will struggle with green water. We test and treat for phosphates as part of our core service.</p>

            <p>Stop the guessing game with your chemicals. <a href="/services/chemical-balancing/" style="color: #0077be; font-weight: 600;">Learn about our Chemical Balancing service</a>.</p>
        '''
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
