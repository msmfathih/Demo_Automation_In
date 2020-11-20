import pytest
import xdist
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if  request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif  request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.close()



def pytest_configure(config):
    config._metadata['Project Name'] = 'Registration Demo'
    config._metadata['Module Name'] = 'User'
    config._metadata['Engineer'] = 'Fathih'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




