# Python Projects: Automation, API Integration, Web Scraping, and Data Processing with Popular Libraries

This repository is a collection of various Python scripts where I experiment with different functionalities, including automation, web scraping, API integration, and data processing using common libraries.

- Sample files are provided to demonstrate the functionality of each script.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Features](#features)
5. [Sample Files](#sample-files)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

### Prerequisites

- Python 3.x
- [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)
- ChromeDriver (for Selenium to control Chrome)
- Yelp API Key (for querying Yelp businesses)
- Pipenv (optional, for virtual environment management)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BaconPancakez/py_ext
   cd py_ext
   ```

2. **Install required dependencies:**

   Create and activate a virtual environment (optional but recommended):

   ```bash
   pipenv install
   pipenv shell
   ```

   If not using `pipenv`, install dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download and install ChromeDriver:**

   Ensure that the version of ChromeDriver matches the version of your installed Chrome browser. You can download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

4. **Configure your API keys:**

   Create a `config.py` file in the root directory of the project with the following content:

   ```python
   # config.py
   api_key = 'YOUR_YELP_API_KEY'
   email = 'YOUR_EMAIL'
   key = 'YOUR_PASSWORD'
   ```

   Replace `'YOUR_YELP_API_KEY'`, `'YOUR_EMAIL'`, and `'YOUR_PASSWORD'` with your actual Yelp API key and GitHub login credentials.

## Configuration

- The `config.py` file contains sensitive data (Yelp API key, email, and password). Make sure you include this file in your `.gitignore` to prevent it from being uploaded to version control.

## Usage

You can run the individual scripts for different tasks as shown below:

- **Automation (automation.py)**: Logs into GitHub using Selenium and automates some tasks.
- **Yelp API (pyvelp.py)**: Queries the Yelp API for businesses in NYC and filters results based on ratings.
- **PDF Processing (pypdf.py)**: Rotates a page in a PDF and merges multiple PDFs.
- **Excel Processing (pyExcel.py)**: Reads and formats data from an Excel sheet using `openpyxl`.
- **Array Calculations (pyNumbers.py)**: Performs array operations and calculations using NumPy.
- **Web Scraping (scraping.py)**: Scrapes the latest questions from Stack Overflow and displays the question titles and vote counts.

### Running the Individual Scripts:

To run any of the individual scripts, simply run them using Python:

```bash
python3 <script_name.py>
```

For example, to run the **automation.py** script, use the following command:

```bash
python3 automation.py
```

### Example Output:

For **Automation (automation.py)**:

```bash
running automation....
```

For **Yelp API (pyvelp.py)**:

```bash
Barber Shop XYZ
[‘High Rated Barber Shop 1’, ‘High Rated Barber Shop 2’]
```

## Features

- **Automation**: Uses Selenium to automate login to GitHub.
- **Yelp Business Search (Pyvelp)**: Queries the Yelp API to retrieve a list of businesses and filters those with ratings higher than 4.5.
- **PDF Processing**: Rotates and merges PDF files using PyPDF2.
- **Excel Processing**: Formats and prints rows from an Excel sheet.
- **Array Calculations**: Demonstrates basic array operations using NumPy.
- **Web Scraping**: Scrapes the latest questions from Stack Overflow and prints the questions and vote counts.

## Sample Files

This repository includes sample files to demonstrate the functionality of the scripts:

- `transactions.xlsx` for the Excel processing script.
- `first.pdf` and `second.pdf` for PDF rotation and merging examples.
- These files can be found in the `samples` directory within the project.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## License

This project is licensed under the MIT License.
