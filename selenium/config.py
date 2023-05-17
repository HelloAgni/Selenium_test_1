import pathlib

SCREENSHOTS = ''.join((str(pathlib.Path(__file__).parent), '/screenshots/'))
pathlib.Path(SCREENSHOTS).mkdir(parents=True, exist_ok=True)
URL = "https://www.saucedemo.com/"
FILE_NAME = "swaglabs.png"
XPATH_USER_NAME = '//*[@name="user-name"]'
XPATH_USER_PASSWORD = '//*[@name="password"]'
XPATH_LOGIN = '//*[@name="login-button"]'
XPATH_USER_ERROR = '//div[@class="error-message-container error"]'\
                   '[.="Epic sadface: Username is required"]'
PASSWORD = 'secret_sauce'
USER = 'standard_user'
