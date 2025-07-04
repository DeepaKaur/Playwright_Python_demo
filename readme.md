# Playwright Python Demo

This project demonstrates basic browser automation using [Playwright](https://playwright.dev/python/) with Python. It includes simple scripts and tests that open a browser, navigate to [google.com](https://www.google.com), and verify the page title.

## Requirements

- Python 3.7+
- [Playwright for Python](https://playwright.dev/python/)
- [pytest](https://docs.pytest.org/en/stable/) (for running tests)
- pip install -r requirements.txt

## Setup

1. Install dependencies:
    ```
    pip install pytest-playwright
    playwright install
    pip install python-dotenv
    ```
2. Activate python environment
    ```
     .\venv1\Scripts\activate 
     ```
3. Run a script directly:
    ```
    python first_test.py
    ```

3. Run tests with pytest:
    ```
    pytest tests\test_google.py --headed
    pytest tests\test_google.py --browser=chromium --headed --screenshot=on --video=on
    pytest .\tests\test_rec_ampcharge.py
    pytest
    ```

## Files

- `first_test.py`: Basic script to open Google and print the page title.
- `test_google_title.py`: Pytest test to open Google and verify search
- `test_rec_ampcharge.py`: Pytest test to open ampcharge and verify search location 