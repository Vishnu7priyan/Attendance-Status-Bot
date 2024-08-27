# Attendance Status Bot

This Python script automates the process of logging into the Hindustan University student portal, capturing a screenshot of your attendance status, and sending it to a specified Telegram chat using a bot.

## Features

- **Automated Login**: Logs into the student portal with your credentials.
- **Screenshot Capture**: Captures a screenshot of the attendance status page.
- **Telegram Integration**: Sends the screenshot to a specified Telegram chat.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Google Chrome browser
- ChromeDriver (Make sure it's compatible with your Chrome version)
- Selenium
- Requests

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/attendance-status-bot.git
    cd attendance-status-bot
    ```

2. **Install Required Python Packages**
    ```bash
    pip install selenium requests
    ```

3. **Set Up ChromeDriver**
    - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's added to your PATH.

## Usage

1. **Configure Telegram Bot**
    - Create a Telegram bot by talking to [@BotFather](https://t.me/BotFather) and obtain your bot token.
    - Replace `_TOKEN = "Bot Token HERE"` in the script with your actual bot token.

2. **Run the Script**
    - Execute the script using Python:
    ```bash
    python sel.py
    ```

3. **Input Your Credentials**
    - You will be prompted to enter your university username and password.

4. **Receive Attendance Status**
    - The script will log in, capture the attendance status screenshot, and send it to the specified Telegram chat.

## Example

```bash
Enter your Username: vishnu
Enter your password: **********
