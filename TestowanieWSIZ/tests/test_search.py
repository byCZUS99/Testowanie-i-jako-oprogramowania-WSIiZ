# tests/test_search.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_TOGGLE_XPATH = "//*[@id='mega-menu-item-52922']/div/form/span"
SEARCH_INPUT_ID = "mega-search-52922"


def _search_results_loaded(driver, query: str) -> bool:
    try:
        url = driver.current_url or ""
        source = (driver.page_source or "").lower()
        return ("?s=" in url) or (query.lower() in source)
    except Exception:
        return False


def _get_search_input(driver):
    return WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, SEARCH_INPUT_ID))
    )


def test_search_works(wsiz_home):
    driver = wsiz_home
    query = "informatyka"

    print("\nKliknij ręcznie 'Zezwól na wszystkie' — masz 5 sekund...")
    time.sleep(5)

    # 1. Kliknięcie ikony lupy
    search_toggle = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, SEARCH_TOGGLE_XPATH))
    )
    driver.execute_script("arguments[0].click();", search_toggle)

    # 2. Poczekaj aż aria-expanded zmieni się na true
    try:
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, SEARCH_TOGGLE_XPATH).get_attribute("aria-expanded") == "true"
        )
    except Exception:
        pass

    # 3. Pobieramy input
    search_input = _get_search_input(driver)

    # Fokus + czyszczenie
    driver.execute_script("arguments[0].focus();", search_input)

    try:
        search_input.clear()
    except Exception:
        pass

    # 4. Wpisanie zapytania
    search_input.send_keys(query)
    search_input.send_keys(Keys.ENTER)

    # 5. Czekamy na wyniki
    WebDriverWait(driver, 20).until(
        lambda d: _search_results_loaded(d, query)
    )

    page_text = driver.page_source.lower()
    assert query in page_text, (
        f"Po wyszukaniu '{query}' nie znaleziono tej frazy. "
        f"Adres: {driver.current_url}"
    )

    print("\nWyniki znalezione — zatrzymuję na 5 sekund...")
    time.sleep(5)
