import os
from playwright.sync_api import sync_playwright
from scraper import LinkedInScraper

def main():
    keyword = "Urgent requirement for QA Engineer"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        scraper = LinkedInScraper(browser)
        profiles = scraper.scrape(keyword)
        print(f"Found {len(profiles)} profiles for '{keyword}':")
        for i, profile in enumerate(profiles, 1):
            print(f"{i}: {profile}")

if __name__ == "__main__":
    main()
