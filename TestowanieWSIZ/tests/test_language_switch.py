# tests/test_language_switch.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def _go_to_language(driver, option_value_part: str, expected_url_part: str):
    """
    Z poziomu strony PL:
    - czeka 5 sekund,
    - wybiera język z selecta #dynamic_select,
    - czeka aż przełączy się na EN/UA/RU,
    - czeka kolejne 5 sekund na wersji językowej.
    """

    # chwila „oglądania” wersji PL
    time.sleep(5)

    lang_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dynamic_select"))
    )

    select = Select(lang_select)

    found = False
    for option in select.options:
        value = option.get_attribute("value") or ""
        if option_value_part in value:
            select.select_by_value(value)
            found = True
            break

    assert found, f"Nie znaleziono opcji językowej z value zawierającym: {option_value_part}"

    # czekamy aż przełączy się domena (EN/UA/RU)
    WebDriverWait(driver, 15).until(
        lambda d: expected_url_part in d.current_url
    )

    # chwila na wersję językową
    time.sleep(5)


def _click_pl_flag_and_wait(driver):
    """
    Kliknięcie polskiej flagi na EN/UA/RU i powrót na wsiz.edu.pl
    + 5 sekund pauzy na PL.
    """
    pl_flag = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//img[contains(@src, 'flaga_polska')]")
        )
    )
    pl_flag.click()

    WebDriverWait(driver, 15).until(
        lambda d: "wsiz.edu.pl" in d.current_url
    )

    time.sleep(5)


def test_language_switch_pl_en_pl(wsiz_home):
    driver = wsiz_home
    _go_to_language(driver, "en.uitm.edu.eu", "en.uitm.edu.eu")
    assert "en.uitm.edu.eu" in driver.current_url

    _click_pl_flag_and_wait(driver)
    assert "wsiz.edu.pl" in driver.current_url


def test_language_switch_pl_ua_pl(wsiz_home):
    driver = wsiz_home
    _go_to_language(driver, "ua.uitm.edu.eu", "ua.uitm.edu.eu")
    assert "ua.uitm.edu.eu" in driver.current_url

    _click_pl_flag_and_wait(driver)
    assert "wsiz.edu.pl" in driver.current_url


def test_language_switch_pl_ru_pl(wsiz_home):
    driver = wsiz_home
    _go_to_language(driver, "ru.uitm.edu.eu", "ru.uitm.edu.eu")
    assert "ru.uitm.edu.eu" in driver.current_url

    _click_pl_flag_and_wait(driver)
    assert "wsiz.edu.pl" in driver.current_url
