#Automated UI Testing of WSIiZ Website (Selenium + Python + Pytest)
Opis projektu

Projekt przedstawia kompletny zestaw automatycznych testów interfejsu użytkownika dla oficjalnej strony internetowej Wyższej Szkoły Informatyki i Zarządzania w Rzeszowie — https://wsiz.edu.pl
.
Testy zostały przygotowane w Pythonie przy użyciu bibliotek Selenium WebDriver, Pytest oraz standardowych narzędzi wspomagających automatyzację i analizę zachowania dynamicznych stron WWW
.

Celem projektu było odwzorowanie rzeczywistych scenariuszy użytkownika odwiedzającego stronę, weryfikacja poprawności działania kluczowych elementów i ocena stabilności interfejsu. Zestaw testów obejmuje zarówno podstawową nawigację, jak i interakcje z wyszukiwarką, przełączanie wersji językowych oraz poprawność linków prowadzących do usług zewnętrznych.

Łącznie przygotowano 19 w pełni działających testów, wszystkie kończące się statusem PASSED.

Zakres funkcjonalny testów

Testy pokrywają kluczowe elementy strony:

1. Testy ładowania i głównej nawigacji

weryfikacja poprawnego wczytywania strony głównej,

przejścia przez główne sekcje:

Uczelnia

Nauka i Badania

Dla studenta

Dla kandydata

Dla biznesu

Dla otoczenia

2. Testy górnego paska odnośników

Testy sprawdzają działanie linków otwierających:

Wirtualną Uczelnię,

e-Learning,

Pocztę,

e-Usługi,

Bibliotekę,

System wydruków,

e-Praktyki,

z obsługą zarówno linków otwierających się w tej samej karcie, jak i takich, które otwierają nową kartę.

3. Test wyszukiwarki

otwarcie pola wyszukiwania,

wpisanie zapytania,

automatyczne zatwierdzenie,

oczekiwanie na wyniki i weryfikacja treści.

4. Testy wersji językowych

przełączanie z PL → EN → PL,

przełączanie z PL → UA → PL,

przełączanie z PL → RU → PL.

5. Test powrotu na stronę główną

wejście do sekcji „Dla studenta”,

kliknięcie logo uczelni w nagłówku,

weryfikacja powrotu do strony głównej.

Rozwiązania techniczne

Testy uruchamiane są lokalnie przy użyciu Google Chrome + ChromeDriver.

Każdy test działa w izolowanej sesji WebDrivera dzięki wykorzystaniu fixture’a wsiz_home.

W celu zapewnienia stabilności zastosowano:

WebDriverWait,

selektory odporne na zmiany,

klikanie przez execute_script,

obsługę dynamicznych opóźnień oraz przewijanie strony,

obsługę wielokrotnych przeładowań strony oraz elementów DOM.

Projekt od początku był dostosowany do pracy z dynamiczną stroną WWW, w której niektóre elementy generowane są asynchronicznie lub mogą być zasłaniane przez pojawiające się banery.

Struktura repozytorium
/tests
    test_homepage_basic.py
    test_top_bar_links.py
    test_language_switch.py
    test_search.py
    test_logo_redirect.py

conftest.py
requirements.txt
README.md

Wnioski

Gotowy zestaw testów wskazuje, że kluczowe funkcje strony działają poprawnie. Projekt pokazał również, że dynamiczne strony wymagają stosowania bardziej elastycznych metod automatyzacji niż klasyczne „kliknij i sprawdź”.
Zestaw testów może stanowić podstawę do:

włączenia automatycznej regresji (CI/CD),

monitorowania działania serwisu na bieżąco,

dalszej rozbudowy testów o scenariusze negatywne i wydajnościowe.
