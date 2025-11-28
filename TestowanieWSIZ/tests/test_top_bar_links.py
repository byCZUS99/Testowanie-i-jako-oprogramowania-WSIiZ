# tests/test_top_bar_links.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _click_link_same_tab_xpath(driver, link_xpath: str, expected_substrings: list[str]):
    """
    Link otwierany w TEJ SAMEJ karcie:
    - przewijamy na górę,
    - klikamy po XPATH,
    - czekamy na zmianę URL,
    - 5 sekund na obejrzenie,
    - sprawdzamy czy URL zawiera któryś z oczekiwanych fragmentów.
    """
    base_url = driver.current_url

    # zawsze na górę – żeby top bar był widoczny
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, link_xpath))
    )

    # na wszelki wypadek przewijamy i klikamy przez JS
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    driver.execute_script("arguments[0].click();", link)

    WebDriverWait(driver, 20).until(lambda d: d.current_url != base_url)

    # chwila na obejrzenie strony
    time.sleep(5)

    current_url = driver.current_url.lower()
    print(f"[XPATH={link_xpath}] -> {current_url}")

    assert any(sub.lower() in current_url for sub in expected_substrings), (
        f"Po kliknięciu linku ({link_xpath}) spodziewano się jednego z: "
        f"{expected_substrings}, a jest: {current_url}"
    )


def _click_link_new_tab_xpath(driver, link_xpath: str, expected_substrings: list[str]):
    """
    Link otwierany w NOWEJ karcie:
    - przewijamy na górę,
    - klikamy po XPATH,
    - przełączamy się na nową kartę,
    - 5 sekund na obejrzenie,
    - sprawdzamy URL,
    - wracamy do karty bazowej.
    """
    original_handles = driver.window_handles
    base_handle = driver.current_window_handle

    # na górę
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, link_xpath))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    driver.execute_script("arguments[0].click();", link)

    # czekamy aż pojawi się nowa karta
    WebDriverWait(driver, 20).until(
        lambda d: len(d.window_handles) > len(original_handles)
    )

    new_handles = [h for h in driver.window_handles if h not in original_handles]
    assert new_handles, "Nie wykryto nowej karty po kliknięciu linku"

    driver.switch_to.window(new_handles[0])

    WebDriverWait(driver, 20).until(
        lambda d: d.current_url and d.current_url != "about:blank"
    )

    time.sleep(5)

    current_url = driver.current_url.lower()
    print(f"[XPATH={link_xpath}] (nowa karta) -> {current_url}")

    assert any(sub.lower() in current_url for sub in expected_substrings), (
        f"Po kliknięciu linku (nowa karta, {link_xpath}) spodziewano się jednego z: "
        f"{expected_substrings}, a jest: {current_url}"
    )

    # wracamy do karty bazowej (nie zamykamy nic)
    driver.switch_to.window(base_handle)


def test_top_link_wirtualna_uczelnia(wsiz_home):
    driver = wsiz_home
    _click_link_same_tab_xpath(
        driver,
        "//*[@id='mega-menu-item-52540']/a",
        ["my.wsiz.edu.pl"],
    )


def test_top_link_e_learning(wsiz_home):
    driver = wsiz_home
    _click_link_same_tab_xpath(
        driver,
        "//*[@id='mega-menu-item-52541']/a",
        ["moodle.wsiz.edu.pl"],
    )


def test_top_link_poczta(wsiz_home):
    driver = wsiz_home
    _click_link_same_tab_xpath(
        driver,
        "//*[@id='mega-menu-item-52542']/a",
        [
            "poczta.wsiz.edu.pl",
            "outlook.office365.com",
            "office.com",
            "microsoftonline.com",
        ],
    )


def test_top_link_e_uslugi(wsiz_home):
    driver = wsiz_home
    _click_link_new_tab_xpath(
        driver,
        "//*[@id='mega-menu-item-52543']/a",
        ["euslugi.wsiz.pl"],
    )


def test_top_link_biblioteka(wsiz_home):
    driver = wsiz_home
    _click_link_same_tab_xpath(
        driver,
        "//*[@id='mega-menu-item-52544']/a",
        [
            "wsiz.edu.pl/uczelnia/jednostki-wsiiz/biblioteka-wsiiz",
            "biblioteka-wsiiz",
        ],
    )


def test_top_link_system_wydrukow(wsiz_home):
    driver = wsiz_home
    _click_link_new_tab_xpath(
        driver,
        "//*[@id='mega-menu-item-52545']/a",
        ["print.wsiz.rzeszow.pl"],
    )


def test_top_link_e_praktyki(wsiz_home):
    driver = wsiz_home
    _click_link_same_tab_xpath(
        driver,
        "//*[@id='mega-menu-item-99388']/a",
        ["portal.wsiz.edu.pl"],
    )
