import os
import pytest

from dotenv import load_dotenv
from pathlib import Path
from pages.login_page import LoginPage


# Load settings from the project's .env file
load_dotenv(Path(__file__).resolve().parent / ".env")


@pytest.fixture
def logged_in_page(page):

    login_page = LoginPage(page)

    login_page.open()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    if not username or not password:
        raise ValueError("USERNAME or PASSWORD is missing from .env")

    login_page.login(username, password)

    return page