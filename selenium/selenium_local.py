import config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_click_without_log(url: str):
    """
    Тест, при клике на кнопку login без заполнения полей
    username, password - всплывает сообщение об ошибке.
    Epic sadface: Username is required
    """
    service = Service(executable_path="./chromedriver")
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service,
                              options=options)
    try:
        driver.get(url=url)
        driver.implicitly_wait(5)

        login_buton = driver.find_element(By.NAME, 'login-button')
        login_buton.click()
        error = driver.find_element(By.XPATH, config.XPATH_USER_ERROR)
        if error:
            print('Test is OK - ', error.text)
        else:
            print('Test is Failed')
    except Exception as e:
        print(e)
    finally:
        driver.quit()


def test_user_login_and_screenshot(
        url: str,
        user_name: str,
        user_password: str
):
    """
    Тест, при вводе всех данных и нажатии на кнопку login
    происходит переход на страницу товаров,
    сохраняется screenshot страницы сайта.
    """
    service = Service(executable_path="./chromedriver")
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service,
                              options=options)
    try:
        driver.get(url)
        driver.implicitly_wait(3)

        user = driver.find_element(By.XPATH, config.XPATH_USER_NAME)
        user.send_keys(user_name)
        password = driver.find_element(By.XPATH, config.XPATH_USER_PASSWORD)
        password.send_keys(user_password)

        login_buton = driver.find_element(By.NAME, 'login-button')
        login_buton.click()

        height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, height)
        driver.save_screenshot(f"{config.SCREENSHOTS}{config.FILE_NAME}")
    except Exception:
        pass
    finally:
        driver.quit()


if __name__ == "__main__":
    test_click_without_log(config.URL)
    test_user_login_and_screenshot(config.URL, config.USER, config.PASSWORD)
    print('DONE!')
