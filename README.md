# Multi-Link Image Scraper with Progress Bars

A Python script to scrape images from multiple URLs, with support for queuing multiple links and assigning custom folder names for each. The script uses Selenium, `requests`, and `tqdm` to provide a user-friendly scraping experience with real-time progress updates.

## Features

- Scrape images from multiple URLs.
- Assign custom folder names for each URL.
- Dynamic folder creation.
- Real-time progress bars for downloading images and saving files.
- Mimics a real browser to bypass simple restrictions.

## Prerequisites

1. Python 3.7 or higher.
2. [GeckoDriver](https://github.com/mozilla/geckodriver) (automatically managed by `webdriver-manager`).
3. A modern operating system (Windows, macOS, or Linux).

## Installation

### Option 1: Clone the Repository (Recommended)

1. Clone this repository using Git:
    ```bash
    git clone https://github.com/yourusername/multi-link-image-scraper.git
    cd multi-link-image-scraper
    ```

2. Install the required Python packages:
    ```bash
    pip install selenium requests tqdm webdriver-manager
    ```

### Option 2: Download the Repository as a ZIP File

1. Go to the [GitHub repository](https://github.com/frxdcode/multi-link-image-scraper/tree/main).
2. Click the green **Code** button and select **Download ZIP**.
3. Extract the ZIP file to your desired location.
4. Open a terminal or command prompt and navigate to the extracted folder:
    ```bash
    cd path/to/multi-link-image-scraper
    ```

5. Install the required Python packages:
    ```bash
    pip install selenium requests tqdm webdriver-manager
    ```

## Usage

Run the script to start scraping:

```bash
python scraper.py
```

### Sample Interaction

1. **Start the script**:
   ```plaintext
   Enter the URL to scrape images from (or 'done' to finish): https://example.com/gallery1
   Enter the folder name for this URL: Gallery1
   Enter the URL to scrape images from (or 'done' to finish): https://example.com/gallery2
   Enter the folder name for this URL: Gallery2
   Enter the URL to scrape images from (or 'done' to finish): done
   ```

2. **Result**:
   - Images from `https://example.com/gallery1` will be saved in `Gallery1/`.
   - Images from `https://example.com/gallery2` will be saved in `Gallery2/`.

### Script Output

During execution, the script provides:
- Real-time updates for loading webpages.
- Progress bars for downloading and saving images.

Example:
```plaintext
Processing URL: https://example.com/gallery1 -> Folder: Gallery1
Downloading images: 100%|████████████████████████████████| 10/10 [00:10<00:00,  1.00s/it]
Saving image_1.jpg: 100%|███████████████████████████████| 500k/500k [00:01<00:00, 500kB/s]
Saved: Gallery1/image_1.jpg
```

## Notes

- The script uses Firefox in **headless mode** for scraping.
- If a URL doesn't have valid images, the folder will still be created, but it will be empty.
- Ensure you comply with the website’s terms of service before scraping.

## Troubleshooting

- **403 Forbidden Errors**:
  - Ensure the script mimics a modern browser using the provided headers.
  - Some websites may still block automated scraping. For complex sites, additional configuration or CAPTCHA handling may be required.
  
- **Missing GeckoDriver**:
  - This script automatically installs `GeckoDriver` using `webdriver-manager`. If this fails, install `GeckoDriver` manually from [here](https://github.com/mozilla/geckodriver).

## License

MIT License

---

Enjoy using `multi-link-image-scraper`! 🚀
