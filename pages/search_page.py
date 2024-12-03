from .base_page import BasePage

class LinkedInSearchPage(BasePage):
    def search_keyword(self, keyword):
        search_url = f"https://www.linkedin.com/search/results/content/?keywords={keyword}"
        self.page.goto(search_url)
        self.page.wait_for_selector("div.search-results-container")

    def scrape_user_profiles(self, max_posts=50):
        """
        Scrape user profiles for posts matching the search criteria, handling endless scrolling.

        :param max_posts: Maximum number of posts to collect.
        :return: List of user profile URLs.
        """
        profiles = set()
        scroll_count = 0
        max_scroll_attempts = 10  # Max scroll attempts before stopping
        previous_height = None

        while len(profiles) < max_posts and scroll_count < max_scroll_attempts:
            # Extract user profile links in the current viewport
            self.page.wait_for_timeout(2000)  # Small delay to allow content to load
            current_profiles = self.page.locator("a[href*='/in/']").evaluate_all(
                "elements => elements.map(e => e.href)"
            )

            # Add new profiles to the set
            profiles.update(current_profiles)

            # Scroll down
            self.page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            self.page.wait_for_timeout(2000)  # Small delay after scrolling

            # Check if scrolling has reached the end
            current_height = self.page.evaluate("document.body.scrollHeight")
            if previous_height == current_height:  # No change in height
                scroll_count += 1
            else:
                scroll_count = 0  # Reset counter if new content is loaded

            previous_height = current_height

        # Return only the required number of profiles
        return list(profiles)[:max_posts]
