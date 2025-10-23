# -*- coding: utf-8 -*-
"""
Created on Wed Sep  17 13:14:41 2025

@author: DJIMENEZ
"""


# Librerias necesarias
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def driver_configuration(download_save_path:str = None):
    """
    Selenium's driver configuration with automatic file download options and headless mode to enable background execution and Github Actions compatibility.

    Parameters
    ----------
    download_save_path : str, optional
        Route to save downloaded files. The default is None.
    Returns
    -------
    driver : selenium.webdriver.Chrome
        Instance of the configured Chrome driver.

    """
    if download_save_path and not os.path.exists(download_save_path):
        os.makedirs(download_save_path)

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--remote-debugging-port=0")
    chrome_options.add_argument("--log-level=3")

    if download_save_path:
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_save_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options,
    )

    return driver
