# tests/test_logo_redirect.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logo_redirects_to_home(wsiz_home):
    """
    Scenariusz:
    1. Klikamy w menu "Dla studenta".
    2. Czekamy aż załaduje się /dla-studenta/.
    3. Czekamy 5 s na podstronie.
    4. Klikamy logo uczelni.
    5. Czekamy aż wróci na stronę główną.
    6. Czekamy 5 s na stronie głównej.
    """

    driver = wsiz_home

    # 1. Kliknięcie "Dla studenta" po tekście linku w górnym menu
    dla_studenta_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Dla studenta"))
    )
    dla_studenta_link.click()

    # 2. Czekamy aż URL faktycznie przełączy się na podstronę /dla-studenta/
    WebDriverWait(driver, 15).until(
        lambda d: "wsiz.edu.pl/dla-studenta" in d.current_url
    )

    print("Jesteś na podstronie 'Dla studenta' — czekam 5 sekund...")
    time.sleep(5)

    # 3. Logo
    logo_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='mega-menu-item-52539']/a"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", logo_link)

    # 4. Klikamy logo przez JS
    driver.execute_script("arguments[0].click();", logo_link)

    # 5. Powrót na stronę główną
    WebDriverWait(driver, 15).until(
        lambda d: d.current_url.startswith("https://wsiz.edu.pl")
    )

    print("Powrócono na stronę główną — czekam 5 sekund...")
    time.sleep(5)

    assert driver.current_url.startswith("https://wsiz.edu.pl"), (
        f"Oczekiwano powrotu na https://wsiz.edu.pl, "
        f"aktualny adres: {driver.current_url}"
    )
