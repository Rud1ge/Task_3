from selenium import webdriver


class DriverFactory:
    @staticmethod
    def getWebdriver(browserName):
        # На Ubuntu snap /usr/bin/firefox и /snap/bin/chromium — shell-обёртки.
        # Selenium ждёт реальный executable (options.binary_location).
        if browserName == "chrome":
            options = webdriver.ChromeOptions()
            options.binary_location = "/snap/chromium/current/usr/lib/chromium-browser/chrome"
            return webdriver.Chrome(options=options)
        elif browserName == "firefox":
            options = webdriver.FirefoxOptions()
            options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
            return webdriver.Firefox(options=options)
