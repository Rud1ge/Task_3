import random
import string

import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from urls import (
    INGREDIENTS_ENDPOINT,
    ORDERS_ENDPOINT,
    REGISTER_ENDPOINT,
    USER_ENDPOINT,
)

FIREFOX_BINARY = "/snap/firefox/current/usr/lib/firefox/firefox"


def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def build_random_user_payload():
    return {
        "email": f"{generate_random_string(10)}@example.com",
        "password": generate_random_string(10),
        "name": generate_random_string(10),
    }


def register_new_user_and_return_data():
    payload = build_random_user_payload()
    response = requests.post(REGISTER_ENDPOINT, json=payload)
    body = response.json()
    return {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "accessToken": body["accessToken"],
        "refreshToken": body["refreshToken"],
    }


@allure.step("Удаляем пользователя")
def delete_user(access_token):
    return requests.delete(USER_ENDPOINT, headers={"Authorization": access_token})


def get_ingredient_ids():
    response = requests.get(INGREDIENTS_ENDPOINT)
    ingredients = response.json()["data"]
    bun_id = next(item["_id"] for item in ingredients if item["type"] == "bun")
    filling_id = next(item["_id"] for item in ingredients if item["type"] != "bun")
    return bun_id, filling_id


@allure.step("Создаём заказ через API")
def create_order_via_api(access_token, ingredients=None):
    if ingredients is None:
        bun_id, filling_id = get_ingredient_ids()
        ingredients = [bun_id, filling_id, bun_id]
    response = requests.post(
        ORDERS_ENDPOINT,
        json={"ingredients": ingredients},
        headers={"Authorization": access_token},
    )
    return response.json()


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            options = ChromeOptions()
            options.page_load_strategy = "eager"
            return webdriver.Chrome(options=options)
        if browser_name == "firefox":
            options = FirefoxOptions()
            options.binary_location = FIREFOX_BINARY
            return webdriver.Firefox(options=options)
        raise ValueError(f"Браузер {browser_name} не поддерживается")
