import requests
from bs4 import BeautifulSoup
import os


def scraping():
    # Get the terminal size to format the output according to the terminal width
    term_size = os.get_terminal_size()

    # Fetch the latest questions from Stack Overflow via HTTP GET request
    response = requests.get('https://stackoverflow.com/questions')

    # Parse the retrieved HTML content using BeautifulSoup to extract relevant information
    soup = BeautifulSoup(response.text, 'html.parser')

    # Select the question summaries using a specific CSS class
    questions = soup.select('.s-post-summary')

    # Print header for the questions output
    print('Questions from StackOverflow -> Latest to Oldest')
    # Print a line to match terminal width
    print('=' * term_size.columns, end='\n\n')

    # Loop through each question to display the title and vote count
    for question in questions:
        # Extract and print the question title
        print(question.select_one('.s-link').get_text(), ' - ', end='')

        # Extract and print the vote count for each question
        print(question.select_one(
            '.s-post-summary--stats-item-number').get_text(), 'Votes')

        # Print a separator line between questions
        print('-' * term_size.columns, end='\n\n')
