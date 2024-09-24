from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_purchase():
    # Драйвер
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    # 1. Авторизация
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID,"login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    time.sleep(2)  # подождем загрузки страницы

    # 2. Выбор товара
    product_link = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    product_link.click()

    add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    add_to_cart_button.click()

    time.sleep(2)  # подождем загрузки страницы

    # 3. Корзина
    cart_link = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_link.click()

    time.sleep(2)  # подождем загрузки страницы

    # 4. Корзина не пустая
    cart_product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    assert cart_product.is_displayed()

    time.sleep(2)  # подождем загрузки страницы

    # 5. Оформляем
    checkout_button = driver.find_element(By.XPATH, "//button[text()='Checkout']")
    checkout_button.click()

    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")

    first_name_input.send_keys("Aleks")
    last_name_input.send_keys("Bebs")
    postal_code_input.send_keys("98765")
    continue_button.click()

    time.sleep(10)  # подождем загрузки страницы

    # 6. Завершаем
    finish_button = driver.find_element(By.XPATH, "//button[text()='Finish']")
    finish_button.click()

    time.sleep(2)  # подождем загрузки страницы

    # 7. Проверяем
    success_message = driver.find_element(By.XPATH, "//h2[contains(text(), 'Thank you for your order')]")
    assert success_message.is_displayed()

    time.sleep(10)  # подождем загрузки страницы

    # Закрыть браузер
    driver.quit()

if __name__ == "__main__":
    test_purchase()
