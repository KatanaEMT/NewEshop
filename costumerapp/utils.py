from selenium import webdriver


def get_driver():
    path = r"C:\Users\katan\OneDrive\桌面\M1\return\chromedriver-win64\chromedriver.exe"
    cService = webdriver.ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=cService)
    driver.maximize_window()
    return driver