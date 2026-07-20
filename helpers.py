import random
import string

import requests

from urls import INGREDIENTS_ENDPOINT, ORDERS_ENDPOINT, REGISTER_ENDPOINT, USER_ENDPOINT


def random_string(length=8):
    return "".join(random.choices(string.ascii_lowercase, k=length))


def register_user():
    email = f"{random_string()}@example.com"
    password = random_string()
    name = random_string()
    body = requests.post(
        REGISTER_ENDPOINT,
        json={"email": email, "password": password, "name": name},
    ).json()
    return {
        "email": email,
        "password": password,
        "name": name,
        "accessToken": body["accessToken"],
    }


def delete_user(access_token):
    requests.delete(USER_ENDPOINT, headers={"Authorization": access_token})


def get_ingredients():
    items = requests.get(INGREDIENTS_ENDPOINT).json()["data"]
    bun = None
    sauce = None
    for item in items:
        if bun is None and item["type"] == "bun":
            bun = item
        if sauce is None and item["type"] == "sauce":
            sauce = item
    return {
        "bun_name": bun["name"],
        "sauce_name": sauce["name"],
        "bun_id": bun["_id"],
        "sauce_id": sauce["_id"],
    }


def create_order(user, ingredients):
    return requests.post(
        ORDERS_ENDPOINT,
        json={
            "ingredients": [
                ingredients["bun_id"],
                ingredients["sauce_id"],
                ingredients["bun_id"],
            ]
        },
        headers={"Authorization": user["accessToken"]},
    ).json()


def clear_browser_session(driver):
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
