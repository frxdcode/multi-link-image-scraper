import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from urllib.parse import urljoin
from tqdm import tqdm

def scrape_images_with_selenium(url, output_dir):
    # Create the output directory
    os.makedirs(output_dir, exist_ok=True)

    print(f"Setting up Selenium WebDriver for: {url}")
    # Setup Selenium WebDriver with Firefox
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Firefox(service=service, options=options)

    try:
        print(f"Opening the webpage: {url}")
        driver.get(url)

        # Wait for the page to load
        print("Loading webpage content...")
        driver.implicitly_wait(10)

        # Find all image elements
        print("Finding image tags on the webpage...")
        img_elements = driver.find_elements(By.TAG_NAME, "img")
        img_urls = [img.get_attribute("src") for img in img_elements if img.get_attribute("src")]

        print(f"Found {len(img_urls)} images. Preparing to download...")

    finally:
        # Always close the driver
        driver.quit()

    # Headers mimicking the latest Firefox on Windows 11
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": url,
        "DNT": "1",  # Do Not Track request
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }

    # Download images with progress bar
    for idx, img_url in enumerate(tqdm(img_urls, desc="Downloading images"), start=1):
        if not img_url:
            continue

        # Resolve the full URL
        img_url = urljoin(url, img_url)

        # Generate image file name
        img_name = f"image_{idx}.jpg"
        img_path = os.path.join(output_dir, img_name)

        try:
            img_data = requests.get(img_url, headers=headers, stream=True)
            img_data.raise_for_status()
            total_size = int(img_data.headers.get("content-length", 0))

            with open(img_path, "wb") as img_file:
                with tqdm(
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    desc=f"Saving {img_name}",
                    leave=False,
                ) as progress:
                    for chunk in img_data.iter_content(1024):
                        img_file.write(chunk)
                        progress.update(len(chunk))

            print(f"Saved: {img_path}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {img_url}: {e}")

def main():
    print("Enter URLs and folder names. Type 'done' when finished.")
    tasks = []

    while True:
        url = input("Enter the URL to scrape images from (or 'done' to finish): ").strip()
        if url.lower() == "done":
            break

        folder_name = input("Enter the folder name for this URL: ").strip()
        if not folder_name:
            print("Folder name cannot be empty.")
            continue

        tasks.append((url, folder_name))

    if not tasks:
        print("No tasks entered. Exiting...")
        return

    for url, folder_name in tasks:
        print(f"\nProcessing URL: {url} -> Folder: {folder_name}")
        scrape_images_with_selenium(url, folder_name)

if __name__ == "__main__":
    main()
