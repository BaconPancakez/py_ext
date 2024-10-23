from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import email, key


def automation():
    # Initialize the Chrome driver
    browser = webdriver.Chrome()

    # Open GitHub
    browser.get('https://github.com')

    # Wait for the "Sign in" link and click it
    try:
        signIn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Sign in'))
        )
        signIn.click()

        # Wait for the username field to appear
        username = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'login_field'))
        )
        # Enter username and password
        username.send_keys(email)

        password = browser.find_element(By.ID, 'password')
        password.send_keys(key)

        # Submit the form
        password.submit()

        # Wait for the page to load and check for the presence of the user profile
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'PoodsJeff'))
        )

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Keep the browser open for inspection
        input('Press Enter to close the browser...')

        # Close the browser
        browser.quit()
