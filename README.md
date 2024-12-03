# **LinkedIn Scraper with Playwright**

This project is a LinkedIn scraper built using [Playwright](https://playwright.dev/python/). The scraper automates the process of searching for posts containing specific keywords and extracting user profile links. The tool can run inside a Docker container, with options for local browser debugging.

---

## **Features**
- Search LinkedIn posts for specific keywords.
- Extract user profile links from posts.
- Supports headless and non-headless browser modes.

---

## **Requirements**
- Python 3.8 or higher
- Docker (optional)
- LinkedIn account for logging in

---

## **Setup**

### **Clone the Repository**
```bash
git clone https://github.com/yourusername/linkedin-scraper.git
cd linkedin-scraper

### **Install Dependencies**
pip install -r requirements.txt

### **Playwright Setup**
playwright install

### **Usage**
export LINKEDIN_PASSWORD=<password>
export LINKEDIN_EMAIL=<email>
python main.py

