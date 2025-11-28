# tests/test_homepage_basic.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_homepage_loads(wsiz_home):
    driver = wsiz_home

    # Czekamy aż header się pojawi
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "header"))
    )

    # chwila „na oko”
    time.sleep(5)

    assert "WSIiZ" in driver.title or "Wyższa Szkoła Informatyki" in driver.title


def _open_menu_and_check(driver, menu_text: str, expected_word: str):
    """
    Klikamy pozycję z górnego menu po TEKŚCIE linku
    i sprawdzamy, czy na nowej stronie pojawia się oczekiwane słowo.
    """
    base_url = driver.current_url

    # Klikamy element z górnego menu po tekście
    link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, menu_text))
    )
    link.click()

    # Czekamy aż zmieni się URL (inna podstrona)
    WebDriverWait(driver, 15).until(lambda d: d.current_url != base_url)

    # 5 sekund na podstronie
    time.sleep(5)

    # Sprawdzamy, czy w treści jest oczekiwane słowo
    page_text = driver.page_source.lower()
    assert expected_word.lower() in page_text, (
        f"Po kliknięciu '{menu_text}' nie znaleziono słowa '{expected_word}'. "
        f"Adres: {driver.current_url}"
    )


def test_nawigacja_uczelnia(wsiz_home):
    _open_menu_and_check(wsiz_home, "Uczelnia", "uczelnia")


def test_nawigacja_nauka_i_badania(wsiz_home):
    _open_menu_and_check(wsiz_home, "Nauka i Badania", "nauka")


def test_nawigacja_dla_studenta(wsiz_home):
    _open_menu_and_check(wsiz_home, "Dla studenta", "student")


def test_nawigacja_dla_kandydata(wsiz_home):
    _open_menu_and_check(wsiz_home, "Dla kandydata", "kandydat")


def test_nawigacja_dla_biznesu(wsiz_home):
    _open_menu_and_check(wsiz_home, "Dla biznesu", "biznes")


def test_nawigacja_dla_otoczenia(wsiz_home):
    _open_menu_and_check(wsiz_home, "Dla otoczenia", "otoczenia")
