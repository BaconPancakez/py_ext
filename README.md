# Python Project: Automation, Yelp API, and Web Scraping

This project contains Python scripts that perform various tasks such as web automation using Selenium, querying the Yelp API for business search, and web scraping using BeautifulSoup.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Features](#features)
5. [Contributing](#contributing)
6. [License](#license)

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
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
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

You can run the individual scripts by selecting one of the following options:

- **Automation**: Logs into GitHub using Selenium and automates some tasks.
- **Pyvelp (Yelp API)**: Queries the Yelp API for businesses in NYC and filters results based on ratings.
- **Scraping**: Scrapes the latest questions from Stack Overflow and displays the question titles and vote counts.

### Running the Main Script:

To run the script and select one of the tasks:

```bash
python3 main.py
```

After running the script, you will be prompted to select one of the available tasks:

```
Select an option:
1. Automation
2. Pyvelp
3. Scraping
Which one would you like to select?
```

### Example:

```bash
Select an option:
1. Automation
2. Pyvelp
3. Scraping
Which one would you like to select? 1
running automation....
```

The corresponding task will then be executed.

## Features

- **Automation**: Uses Selenium to automate login to GitHub.
- **Yelp Business Search (Pyvelp)**: Queries the Yelp API to retrieve a list of businesses and filters those with ratings higher than 4.5.
- **Web Scraping**: Scrapes the latest questions from Stack Overflow and prints them along with their vote counts.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## License

This project is licensed under the MIT License.
