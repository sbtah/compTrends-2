"""
Used for local testing.
"""
import time
import re
from scraper.stores.leroy_merlin.leroy_merlin import LeroyMerlinScraper
from backend.operator.task import TaskOperator


# URL for lvl 1 discovery
url_1 = [
{'url': 'https://www.leroymerlin.pl/budowa,a5.html', 'name': 'Budowa', 'category_id': 5, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/technika,a8.html', 'name': 'Technika', 'category_id': 8, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/projekt,a9.html', 'name': 'Projekt', 'category_id': 9, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja,a10.html', 'name': 'Dekoracja', 'category_id': 10, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrod,a11.html', 'name': 'Ogród', 'category_id': 11, 'has_childs': True, 'has_products': False},
]

url_2 = [
{'url': 'https://www.leroymerlin.pl/materialy-budowlane,a132.html', 'name': 'Materiały budowlane', 'category_id': 132, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/izolacja-budynkow,a141.html', 'name': 'Izolacja budynków', 'category_id': 141, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dachy-i-akcesoria,a143.html', 'name': 'Dachy i akcesoria', 'category_id': 143, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie,a2022.html', 'name': 'Ogrzewanie', 'category_id': 2022, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/konstrukcje-drewniane-i-metalowe,a148.html', 'name': 'Konstrukcje drewniane i metalowe', 'category_id': 148, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/materialy-wykonczeniowe,a150.html', 'name': 'Materiały wykończeniowe', 'category_id': 150, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/okna-i-drzwi,a138.html', 'name': 'Okna i drzwi', 'category_id': 138, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy,a152.html', 'name': 'Ogrodzenia i bramy', 'category_id': 152, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-budowlane,a154.html', 'name': 'Narzędzia budowlane', 'category_id': 154, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika,a153.html', 'name': 'Hydraulika', 'category_id': 153, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia,a103.html', 'name': 'Elektronarzędzia', 'category_id': 103, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne,a104.html', 'name': 'Narzędzia ręczne', 'category_id': 104, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat,a105.html', 'name': 'Warsztat', 'category_id': 105, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/odziez-i-artykuly-bhp,a3134.html', 'name': 'Odzież i artykuły BHP', 'category_id': 3134, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika,a107.html', 'name': 'Hydraulika', 'category_id': 107, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie,a110.html', 'name': 'Ogrzewanie', 'category_id': 110, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/klimatyzacja-i-wentylacja,a111.html', 'name': 'Klimatyzacja i wentylacja', 'category_id': 111, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektrycznosc,a114.html', 'name': 'Elektryczność', 'category_id': 114, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe,a117.html', 'name': 'Artykuły metalowe', 'category_id': 117, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/zabezpieczenie-domu,a119.html', 'name': 'Zabezpieczenie domu', 'category_id': 119, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby-lakiery-i-kleje,a120.html', 'name': 'Farby, lakiery i kleje', 'category_id': 120, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-gospodarcze,a121.html', 'name': 'Artykuły gospodarcze', 'category_id': 121, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/drzwi-klamki-i-schody,a126.html', 'name': 'Drzwi, klamki i schody', 'category_id': 126, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/podlogi-drewniane-panele-scienne,a184.html', 'name': 'Podłogi drewniane, Panele ścienne', 'category_id': 184, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/plytki-ceramiczne-na-sciane-i-podloge,a226.html', 'name': 'Płytki ceramiczne na ścianę i podłogę', 'category_id': 226, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kuchnie,a636.html', 'name': 'Kuchnie', 'category_id': 636, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-kuchenne,a3491.html', 'name': 'Akcesoria kuchenne', 'category_id': 3491, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/jadalnia,a3492.html', 'name': 'Jadalnia', 'category_id': 3492, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/meble-lazienkowe-i-lustra,a525.html', 'name': 'Meble łazienkowe i lustra', 'category_id': 525, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ceramika-lazienkowa,a540.html', 'name': 'Ceramika łazienkowa', 'category_id': 540, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/wanny-i-kabiny-prysznicowe,a2106.html', 'name': 'Wanny i kabiny prysznicowe', 'category_id': 2106, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/armatura-lazienkowa,a590.html', 'name': 'Armatura łazienkowa', 'category_id': 590, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/wyposazenie-lazienki,a604.html', 'name': 'Wyposażenie łazienki', 'category_id': 604, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-lazienkowe,a2092.html', 'name': 'Akcesoria łazienkowe', 'category_id': 2092, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/garderoba-i-wnetrze,a724.html', 'name': 'Garderoba i wnętrze', 'category_id': 724, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elementy-mebli-i-okucia,a834.html', 'name': 'Elementy mebli i okucia', 'category_id': 834, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kominki,a894.html', 'name': 'Kominki', 'category_id': 894, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby,a737.html', 'name': 'Farby', 'category_id': 737, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-scian-sufitow-i-innych-powierzchni,a863.html', 'name': 'Dekoracja ścian, sufitów i innych powierzchni', 'category_id': 863, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-okien,a924.html', 'name': 'Dekoracja okien', 'category_id': 924, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie,a953.html', 'name': 'Oświetlenie', 'category_id': 953, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dywany-i-wykladziny,a1210.html', 'name': 'Dywany i wykładziny', 'category_id': 1210, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-wnetrz,a1234.html', 'name': 'Dekoracja wnętrz', 'category_id': 1234, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ramki-obrazy-lustra,a1292.html', 'name': 'Ramki, obrazy, lustra', 'category_id': 1292, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/atelier-artystyczne,a1306.html', 'name': 'Atelier artystyczne', 'category_id': 1306, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/organizacja-miejsca-pracy,a2490.html', 'name': 'Organizacja miejsca pracy', 'category_id': 2490, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/maszyny-ogrodnicze,a19.html', 'name': 'Maszyny ogrodnicze', 'category_id': 19, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/porzadki-w-ogrodzie,a20.html', 'name': 'Porządki w ogrodzie', 'category_id': 20, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-ogrodnicze,a21.html', 'name': 'Narzędzia ogrodnicze', 'category_id': 21, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/nawadnianie,a23.html', 'name': 'Nawadnianie', 'category_id': 23, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie,a22.html', 'name': 'Relaks w ogrodzie', 'category_id': 22, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/architektura-ogrodowa,a24.html', 'name': 'Architektura ogrodowa', 'category_id': 24, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie-doniczki-i-dekoracje,a25.html', 'name': 'Oświetlenie, doniczki i dekoracje', 'category_id': 25, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras,a2368.html', 'name': 'Balkon i taras', 'category_id': 2368, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/rosliny-nasiona-cebule,a26.html', 'name': 'Rośliny, nasiona, cebule', 'category_id': 26, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/uprawa-i-ochrona-roslin,a27.html', 'name': 'Uprawa i ochrona roślin', 'category_id': 27, 'has_childs': True, 'has_products': False},
]

url_3 = [
    {'url': 'https://www.leroymerlin.pl/materialy-budowlane/materialy-budowlane-stan-surowy,a156.html', 'name': 'Materiały budowlane - stan surowy', 'category_id': 156, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157.html', 'name': 'Zaprawy i tynki', 'category_id': 157, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/materialy-budowlane/grunty-i-impregnaty,a160.html', 'name': 'Grunty i impregnaty', 'category_id': 160, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/materialy-budowlane/kleje-i-zaprawy-klejowe,a163.html', 'name': 'Kleje i zaprawy klejowe', 'category_id': 163, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/izolacja-budynkow/welna-mineralna-styropian-izolacja-akustyczna,a167.html', 'name': 'Wełna mineralna, styropian, izolacja akustyczna', 'category_id': 167, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395.html', 'name': 'Kleje, uszczelniacze, izolacje', 'category_id': 395, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dachy-i-akcesoria/pokrycia-dachowe,a196.html', 'name': 'Pokrycia dachowe', 'category_id': 196, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej-z-dachu,a199.html', 'name': 'Odprowadzanie wody deszczowej z dachu', 'category_id': 199, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dachy-i-akcesoria/farby-i-uszczelniacze-dachowe,a203.html', 'name': 'Farby i uszczelniacze dachowe', 'category_id': 203, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/kominy-i-odprowadzanie-spalin,a2031.html', 'name': 'Kominy i odprowadzanie spalin', 'category_id': 2031, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/kotly-piece-ogrzewanie-solarne,a2038.html', 'name': 'Kotły, piece, ogrzewanie solarne', 'category_id': 2038, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/ogrzewanie-podlogowe,a2061.html', 'name': 'Ogrzewanie podłogowe', 'category_id': 2061, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/ogrzewanie-przenosne,a2098.html', 'name': 'Ogrzewanie przenośne', 'category_id': 2098, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/akcesoria-do-piecow,a2064.html', 'name': 'Akcesoria do pieców', 'category_id': 2064, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/grzejniki-i-akcesoria,a2070.html', 'name': 'Grzejniki i akcesoria', 'category_id': 2070, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/konstrukcje-drewniane-i-metalowe/deski-plyty-wykonczeniowe-listwy,a206.html', 'name': 'Deski, płyty wykończeniowe, listwy', 'category_id': 206, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/konstrukcje-drewniane-i-metalowe/prety-i-profile-metalowe,a208.html', 'name': 'Pręty i profile metalowe', 'category_id': 208, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/konstrukcje-drewniane-i-metalowe/okucia-i-mocowania,a210.html', 'name': 'Okucia i mocowania', 'category_id': 210, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/materialy-wykonczeniowe/elewacje,a215.html', 'name': 'Elewacje', 'category_id': 215, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/materialy-wykonczeniowe/plyty-karton-gips-i-akcesoria,a218.html', 'name': 'Płyty karton-gips i akcesoria', 'category_id': 218, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/materialy-wykonczeniowe/sufity-podwieszane,a221.html', 'name': 'Sufity podwieszane', 'category_id': 221, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/materialy-wykonczeniowe/pustaki-szklane-luksfery-i-akcesoria,a1538.html', 'name': 'Pustaki szklane - luksfery i akcesoria', 'category_id': 1538, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/okna-i-drzwi/drzwi-zewnetrzne,a225.html', 'name': 'Drzwi zewnętrzne', 'category_id': 225, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/okna-i-drzwi/drzwi-wewnetrzne-i-oscieznice,a2260.html', 'name': 'Drzwi wewnętrzne i ościeżnice', 'category_id': 2260, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/okna-i-drzwi/okna-swietliki-i-wylazy-dachowe,a227.html', 'name': 'Okna, świetliki i wyłazy dachowe', 'category_id': 227, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/okna-i-drzwi/parapety,a228.html', 'name': 'Parapety', 'category_id': 228, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/okna-i-drzwi/akcesoria-do-okien,a236.html', 'name': 'Akcesoria do okien', 'category_id': 236, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/okna-i-drzwi/akcesoria-do-drzwi-zewnetrznych,a232.html', 'name': 'Akcesoria do drzwi zewnętrznych', 'category_id': 232, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy/ogrodzenia-metalowe-systemowe,a241.html', 'name': 'Ogrodzenia metalowe systemowe', 'category_id': 241, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy/ogrodzenia-metalowe-panelowe,a3012.html', 'name': 'Ogrodzenia metalowe panelowe', 'category_id': 3012, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy/ogrodzenia-drewniane-i-kompozytowe,a3171.html', 'name': 'Ogrodzenia drewniane i kompozytowe', 'category_id': 3171, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy/siatki-ogrodzeniowe-i-akcesoria,a3020.html', 'name': 'Siatki ogrodzeniowe i akcesoria', 'category_id': 3020, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy/ogrodzenia-budowlane-tymczasowe,a3195.html', 'name': 'Ogrodzenia budowlane tymczasowe', 'category_id': 3195, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy/bramy-garazowe-i-akcesoria,a245.html', 'name': 'Bramy garażowe i akcesoria', 'category_id': 245, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy/skrzynki-pocztowe-na-listy,a251.html', 'name': 'Skrzynki pocztowe na listy', 'category_id': 251, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrodzenia-i-bramy/oznakowanie-informacyjne,a248.html', 'name': 'Oznakowanie informacyjne', 'category_id': 248, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-budowlane/drabiny-i-rusztowania,a282.html', 'name': 'Drabiny i rusztowania', 'category_id': 282, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-budowlane/betoniarki-taczki-kastry-worki,a285.html', 'name': 'Betoniarki, taczki, kastry, worki', 'category_id': 285, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-budowlane/maszyny-budowlane-i-przyczepki,a295.html', 'name': 'Maszyny budowlane i przyczepki', 'category_id': 295, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-budowlane/narzedzia-reczne,a287.html', 'name': 'Narzędzia ręczne', 'category_id': 287, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-budowlane/narzedzia-glazurnicze,a290.html', 'name': 'Narzędzia glazurnicze', 'category_id': 290, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/instalacje-wodne-i-gazowe,a269.html', 'name': 'Instalacje wodne i gazowe', 'category_id': 269, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/akcesoria-doprowadzenia-wody,a270.html', 'name': 'Akcesoria doprowadzenia wody', 'category_id': 270, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/akcesoria-doprowadzenia-gazu,a272.html', 'name': 'Akcesoria doprowadzenia gazu', 'category_id': 272, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/kanalizacja-zewnetrzna,a274.html', 'name': 'Kanalizacja zewnętrzna', 'category_id': 274, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/kanalizacja-wewnetrzna,a277.html', 'name': 'Kanalizacja wewnętrzna', 'category_id': 277, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/narzedzia-hydrauliczne,a280.html', 'name': 'Narzędzia hydrauliczne', 'category_id': 280, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia/wiertarki-wkretarki-mloty-udarowe,a123.html', 'name': 'Wiertarki, wkrętarki, młoty udarowe', 'category_id': 123, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia/wyrzynarki-pilarki-pily-szablaste-nozyce,a131.html', 'name': 'Wyrzynarki, pilarki, piły szablaste, nożyce', 'category_id': 131, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia/szlifierki-polerki-strugi,a136.html', 'name': 'Szlifierki, polerki, strugi', 'category_id': 136, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia/wiertla-bity-mieszadla,a149.html', 'name': 'Wiertła, bity, mieszadła', 'category_id': 149, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia/materialy-scierne-i-szczotki-druciane-do-elektronarzedzi,a3052.html', 'name': 'Materiały ścierne i szczotki druciane do elektronarzędzi', 'category_id': 3052, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia/tarcze-brzeszczoty-frezy,a3077.html', 'name': 'Tarcze, brzeszczoty, frezy', 'category_id': 3077, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia/akcesoria-do-elektronarzedzi,a151.html', 'name': 'Akcesoria do elektronarzędzi', 'category_id': 151, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektronarzedzia/systemy-elektronarzedzi-akumulatorowych,a3211.html', 'name': 'Systemy elektronarzędzi akumulatorowych', 'category_id': 3211, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/mlotki-wkretaki,a639.html', 'name': 'Młotki, wkrętaki', 'category_id': 639, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/klucze-reczne,a2624.html', 'name': 'Klucze ręczne', 'category_id': 2624, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/szczypce-pily-nozyce,a1527.html', 'name': 'Szczypce, piły, nożyce', 'category_id': 1527, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/miarki-katowniki-dalmierze,a732.html', 'name': 'Miarki, kątowniki, dalmierze', 'category_id': 732, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/dluta-strugi-sciski,a743.html', 'name': 'Dłuta, strugi, ściski', 'category_id': 743, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/pedzle-walki-kuwety,a752.html', 'name': 'Pędzle, wałki, kuwety', 'category_id': 752, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/zszywacze-pistolety-klejowe-i-akcesoria,a770.html', 'name': 'Zszywacze, pistolety klejowe i akcesoria', 'category_id': 770, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/materialy-scierne-szczotki-druciane,a795.html', 'name': 'Materiały ścierne, szczotki druciane', 'category_id': 795, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-reczne/stoly-i-narzedzia-do-tapetowania,a3048.html', 'name': 'Stoły i narzędzia do tapetowania', 'category_id': 3048, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/organizacja-warsztatu,a2198.html', 'name': 'Organizacja warsztatu', 'category_id': 2198, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/wyposazenie-warsztatu,a830.html', 'name': 'Wyposażenie warsztatu', 'category_id': 830, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/urzadzenia-warsztatowe,a867.html', 'name': 'Urządzenia warsztatowe', 'category_id': 867, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/kompresory-i-urzadzenia-pneumatyczne,a893.html', 'name': 'Kompresory i urządzenia pneumatyczne', 'category_id': 893, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/spawarki-i-akcesoria,a915.html', 'name': 'Spawarki i akcesoria', 'category_id': 915, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/akcesoria-samochodowe,a2934.html', 'name': 'Akcesoria samochodowe', 'category_id': 2934, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/lutownice-i-akcesoria-lutownicze,a1524.html', 'name': 'Lutownice i akcesoria lutownicze', 'category_id': 1524, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/palniki-gazowe-i-akcesoria,a1506.html', 'name': 'Palniki gazowe i akcesoria', 'category_id': 1506, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/narzedzia-modelarskie,a1500.html', 'name': 'Narzędzia modelarskie', 'category_id': 1500, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/warsztat/chemia-warsztatowa,a964.html', 'name': 'Chemia warsztatowa', 'category_id': 964, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/odziez-i-artykuly-bhp/odziez-i-obuwie-ochronne-bhp,a3135.html', 'name': 'Odzież i obuwie ochronne BHP', 'category_id': 3135, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/odziez-i-artykuly-bhp/okulary-maski-nauszniki-kaski-ochronne,a3136.html', 'name': 'Okulary, maski, nauszniki, kaski ochronne', 'category_id': 3136, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/odziez-i-artykuly-bhp/apteczki-gasnice,a3152.html', 'name': 'Apteczki, gaśnice', 'category_id': 3152, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/odziez-i-artykuly-bhp/oznakowanie-bhp,a3137.html', 'name': 'Oznakowanie BHP', 'category_id': 3137, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/hydrofory-i-pompy,a979.html', 'name': 'Hydrofory i pompy', 'category_id': 979, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/ogrzewacze-wody,a981.html', 'name': 'Ogrzewacze wody', 'category_id': 981, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/hydraulika/uzdatnianie-wody,a983.html', 'name': 'Uzdatnianie wody', 'category_id': 983, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/grzejniki-i-akcesoria,a1001.html', 'name': 'Grzejniki i akcesoria', 'category_id': 1001, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/kotly-i-piece,a1002.html', 'name': 'Kotły i piece', 'category_id': 1002, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/akcesoria-do-piecow,a1003.html', 'name': 'Akcesoria do pieców', 'category_id': 1003, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/ogrzewanie-elektryczne,a1004.html', 'name': 'Ogrzewanie elektryczne', 'category_id': 1004, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/ogrzewanie-gazowe-i-naftowe,a1005.html', 'name': 'Ogrzewanie gazowe i naftowe', 'category_id': 1005, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ogrzewanie/regulacja-temperatury,a1006.html', 'name': 'Regulacja temperatury', 'category_id': 1006, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/klimatyzacja-i-wentylacja/klimatyzatory-wentylatory-osuszacze,a1033.html', 'name': 'Klimatyzatory, wentylatory, osuszacze', 'category_id': 1033, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/klimatyzacja-i-wentylacja/instalacje-wentylacyjne,a1034.html', 'name': 'Instalacje wentylacyjne', 'category_id': 1034, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/klimatyzacja-i-wentylacja/termometry-i-stacje-meteo,a1035.html', 'name': 'Termometry i stacje meteo', 'category_id': 1035, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektrycznosc/gniazda-wtyczki-akcesoria,a1051.html', 'name': 'Gniazda, wtyczki, akcesoria', 'category_id': 1051, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektrycznosc/instalacje-elektryczne,a1052.html', 'name': 'Instalacje elektryczne', 'category_id': 1052, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektrycznosc/akcesoria-elektryczne,a1053.html', 'name': 'Akcesoria elektryczne', 'category_id': 1053, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektrycznosc/osprzet-rtv-telefoniczny-i-komputerowy,a1054.html', 'name': 'Osprzęt RTV, telefoniczny i komputerowy', 'category_id': 1054, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektrycznosc/narzedzia-elektroinstalacyjne,a1055.html', 'name': 'Narzędzia elektroinstalacyjne', 'category_id': 1055, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elektrycznosc/baterie-ladowarki-latarki,a1084.html', 'name': 'Baterie, ładowarki, latarki', 'category_id': 1084, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe/gwozdzie-wkrety-sruby,a1089.html', 'name': 'Gwoździe, wkręty, śruby', 'category_id': 1089, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe/kolki-kotwy,a2222.html', 'name': 'Kołki, kotwy', 'category_id': 2222, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe/nakretki-podkladki-zaslepki,a1090.html', 'name': 'Nakrętki, podkładki, zaślepki', 'category_id': 1090, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe/lancuchy-liny-tasmy,a1091.html', 'name': 'Łańcuchy, liny, taśmy', 'category_id': 1091, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe/profile-blachy-i-akcesoria,a1092.html', 'name': 'Profile, blachy i akcesoria', 'category_id': 1092, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe/kolka-sprezyny,a1093.html', 'name': 'Kółka, sprężyny', 'category_id': 1093, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe/haczyki-zawieszki-i-magnesy,a2191.html', 'name': 'Haczyki, zawieszki i magnesy', 'category_id': 2191, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-metalowe/systemy-instalacyjne,a2194.html', 'name': 'Systemy instalacyjne', 'category_id': 2194, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/zabezpieczenie-domu/zamki-do-drzwi-wkladki-klodki,a1117.html', 'name': 'Zamki do drzwi, wkładki, kłódki', 'category_id': 1117, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/zabezpieczenie-domu/dzwonki-gongi-domofony,a1118.html', 'name': 'Dzwonki, gongi, domofony', 'category_id': 1118, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/zabezpieczenie-domu/alarmy-monitoring,a1119.html', 'name': 'Alarmy, monitoring', 'category_id': 1119, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/zabezpieczenie-domu/systemy-smart-home,a3358.html', 'name': 'Systemy Smart Home', 'category_id': 3358, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/zabezpieczenie-domu/sejfy-kasetki-szafy-na-bron,a1120.html', 'name': 'Sejfy, kasetki, szafy na broń', 'category_id': 1120, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby-lakiery-i-kleje/srodki-i-farby-do-drewna,a1145.html', 'name': 'Środki i farby do drewna', 'category_id': 1145, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby-lakiery-i-kleje/farby-i-srodki-specjalistyczne,a1146.html', 'name': 'Farby i środki specjalistyczne', 'category_id': 1146, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby-lakiery-i-kleje/rozpuszczalniki-rozcienczalniki,a1148.html', 'name': 'Rozpuszczalniki, rozcieńczalniki', 'category_id': 1148, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby-lakiery-i-kleje/kleje,a1147.html', 'name': 'Kleje', 'category_id': 1147, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby-lakiery-i-kleje/szpachlowki-i-akcesoria,a1641.html', 'name': 'Szpachlówki i akcesoria', 'category_id': 1641, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-gospodarcze/tasmy-folie-ochronne,a1167.html', 'name': 'Taśmy, folie ochronne', 'category_id': 1167, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-gospodarcze/narzedzia-do-sprzatania,a1165.html', 'name': 'Narzędzia do sprzątania', 'category_id': 1165, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/artykuly-gospodarcze/srodki-czystosci,a1166.html', 'name': 'Środki czystości', 'category_id': 1166, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/drzwi-klamki-i-schody/drzwi-zewnetrzne,a2554.html', 'name': 'Drzwi zewnętrzne', 'category_id': 2554, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/drzwi-klamki-i-schody/drzwi-i-oscieznice-wewnetrzne,a129.html', 'name': 'Drzwi i ościeżnice wewnętrzne', 'category_id': 129, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/drzwi-klamki-i-schody/klamki-i-galki-drzwiowe-wewnetrzne,a134.html', 'name': 'Klamki i gałki drzwiowe wewnętrzne', 'category_id': 134, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/drzwi-klamki-i-schody/klamki-i-galki-drzwiowe-zewnetrzne,a2559.html', 'name': 'Klamki i gałki drzwiowe zewnętrzne', 'category_id': 2559, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/drzwi-klamki-i-schody/akcesoria-do-drzwi,a1833.html', 'name': 'Akcesoria do drzwi', 'category_id': 1833, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/drzwi-klamki-i-schody/schody-balustrady,a139.html', 'name': 'Schody, balustrady', 'category_id': 139, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/drzwi-klamki-i-schody/oznakowanie-drzwi,a3328.html', 'name': 'Oznakowanie drzwi', 'category_id': 3328, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/podlogi-drewniane-panele-scienne/panele-deski-parkiety,a186.html', 'name': 'Panele, deski, parkiety', 'category_id': 186, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/podlogi-drewniane-panele-scienne/listwy-i-akcesoria-wykonczeniowe,a194.html', 'name': 'Listwy i akcesoria wykończeniowe', 'category_id': 194, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/podlogi-drewniane-panele-scienne/srodki-do-podlog-z-drewna,a212.html', 'name': 'Środki do podłóg z drewna', 'category_id': 212, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/podlogi-drewniane-panele-scienne/panele-scienne-i-boazeria,a1550.html', 'name': 'Panele ścienne i boazeria', 'category_id': 1550, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/plytki-ceramiczne-na-sciane-i-podloge/plytki-ceramiczne,a229.html', 'name': 'Płytki ceramiczne', 'category_id': 229, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/plytki-ceramiczne-na-sciane-i-podloge/plytki-scienne,a2992.html', 'name': 'Płytki ścienne', 'category_id': 2992, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/plytki-ceramiczne-na-sciane-i-podloge/plytki-podlogowe,a2525.html', 'name': 'Płytki podłogowe', 'category_id': 2525, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/plytki-ceramiczne-na-sciane-i-podloge/kamienie-naturalne,a2528.html', 'name': 'Kamienie naturalne', 'category_id': 2528, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/plytki-ceramiczne-na-sciane-i-podloge/fugi-silikony-akryle,a517.html', 'name': 'Fugi, silikony, akryle', 'category_id': 517, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/plytki-ceramiczne-na-sciane-i-podloge/listwy-wykonczeniowe-krzyzyki-drzwiczki-rewizyjne,a2366.html', 'name': 'Listwy wykończeniowe, krzyżyki, drzwiczki rewizyjne', 'category_id': 2366, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kuchnie/meble-kuchenne,a637.html', 'name': 'Meble kuchenne', 'category_id': 637, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kuchnie/zlewozmywaki-i-akcesoria,a13.html', 'name': 'Zlewozmywaki i akcesoria', 'category_id': 13, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kuchnie/baterie-kuchenne-i-akcesoria,a670.html', 'name': 'Baterie kuchenne i akcesoria', 'category_id': 670, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kuchnie/blaty-kuchenne-i-akcesoria,a2675.html', 'name': 'Blaty kuchenne i akcesoria', 'category_id': 2675, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kuchnie/sprzet-agd,a1816.html', 'name': 'Sprzęt AGD', 'category_id': 1816, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kuchnie/okapy-kuchenne-i-wentylacja,a677.html', 'name': 'Okapy kuchenne i wentylacja', 'category_id': 677, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kuchnie/oswietlenie-kuchenne,a684.html', 'name': 'Oświetlenie kuchenne', 'category_id': 684, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-kuchenne/zarzadzanie-odpadami,a3493.html', 'name': 'Zarządzanie odpadami', 'category_id': 3493, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-kuchenne/akcesoria-do-zmywania,a3495.html', 'name': 'Akcesoria do zmywania', 'category_id': 3495, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-kuchenne/akcesoria-do-przygotowywania-potraw,a3500.html', 'name': 'Akcesoria do przygotowywania potraw', 'category_id': 3500, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-kuchenne/organizacja-i-przechowywanie-w-kuchni,a3501.html', 'name': 'Organizacja i przechowywanie w kuchni', 'category_id': 3501, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-kuchenne/dzbanki-filtrujace-i-saturatory,a3531.html', 'name': 'Dzbanki filtrujące i saturatory', 'category_id': 3531, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/jadalnia/stoly-i-krzesla,a3502.html', 'name': 'Stoły i krzesła', 'category_id': 3502, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/jadalnia/serwowanie-potraw-i-napojow,a3503.html', 'name': 'Serwowanie potraw i napojów', 'category_id': 3503, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/jadalnia/tekstylia-stolowe,a3504.html', 'name': 'Tekstylia stołowe', 'category_id': 3504, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/jadalnia/dekoracja-stolu,a3542.html', 'name': 'Dekoracja stołu', 'category_id': 3542, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/meble-lazienkowe-i-lustra/zestawy-i-elementy-mebli-lazienkowych,a527.html', 'name': 'Zestawy i elementy mebli łazienkowych', 'category_id': 527, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/meble-lazienkowe-i-lustra/produkty-dla-niepelnosprawnych,a537.html', 'name': 'Produkty dla niepełnosprawnych', 'category_id': 537, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ceramika-lazienkowa/umywalki-i-akcesoria,a572.html', 'name': 'Umywalki i akcesoria', 'category_id': 572, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ceramika-lazienkowa/wc,a576.html', 'name': 'WC', 'category_id': 576, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ceramika-lazienkowa/pisuary-bidety,a585.html', 'name': 'Pisuary, bidety', 'category_id': 585, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ceramika-lazienkowa/stelaze-podtynkowe,a2544.html', 'name': 'Stelaże podtynkowe', 'category_id': 2544, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/wanny-i-kabiny-prysznicowe/wanny-i-akcesoria,a2107.html', 'name': 'Wanny i akcesoria', 'category_id': 2107, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/wanny-i-kabiny-prysznicowe/kabiny-brodziki-i-akcesoria,a2108.html', 'name': 'Kabiny, brodziki i akcesoria', 'category_id': 2108, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/wanny-i-kabiny-prysznicowe/drazki-i-zaslonki-prysznicowe,a2147.html', 'name': 'Drążki i zasłonki prysznicowe', 'category_id': 2147, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/armatura-lazienkowa/baterie-lazienkowe,a591.html', 'name': 'Baterie łazienkowe', 'category_id': 591, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/armatura-lazienkowa/natryski-hydroterapia,a597.html', 'name': 'Natryski, hydroterapia', 'category_id': 597, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/armatura-lazienkowa/akcesoria-do-armatury,a2051.html', 'name': 'Akcesoria do armatury', 'category_id': 2051, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/wyposazenie-lazienki/ogrzewanie-wentylacja,a605.html', 'name': 'Ogrzewanie, wentylacja', 'category_id': 605, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/wyposazenie-lazienki/oswietlenie-lazienkowe,a610.html', 'name': 'Oświetlenie łazienkowe', 'category_id': 610, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-lazienkowe/dozowniki-mydelniczki-dystrybutory,a2094.html', 'name': 'Dozowniki, mydelniczki, dystrybutory', 'category_id': 2094, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-lazienkowe/dywaniki-i-maty-lazienkowe,a2095.html', 'name': 'Dywaniki i maty łazienkowe', 'category_id': 2095, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-lazienkowe/kosze-pojemniki-wagi-lazienkowe,a2133.html', 'name': 'Kosze, pojemniki, wagi łazienkowe', 'category_id': 2133, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-lazienkowe/akcesoria-do-prania,a2139.html', 'name': 'Akcesoria do prania', 'category_id': 2139, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-lazienkowe/przechowywanie-w-lazience,a2695.html', 'name': 'Przechowywanie w łazience', 'category_id': 2695, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/akcesoria-lazienkowe/akcesoria-lazienkowe-dla-dzieci,a2699.html', 'name': 'Akcesoria łazienkowe dla dzieci', 'category_id': 2699, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/garderoba-i-wnetrze/elementy-zabudowy-garderoby-i-wnek,a726.html', 'name': 'Elementy zabudowy garderoby i wnęk', 'category_id': 726, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/garderoba-i-wnetrze/meble,a786.html', 'name': 'Meble', 'category_id': 786, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/garderoba-i-wnetrze/wieszaki-haki,a803.html', 'name': 'Wieszaki, haki', 'category_id': 803, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/garderoba-i-wnetrze/pojemniki-pokrowce,a821.html', 'name': 'Pojemniki, pokrowce', 'category_id': 821, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/garderoba-i-wnetrze/akcesoria-uzytkowe-i-produkty-do-przeprowadzki,a825.html', 'name': 'Akcesoria użytkowe i produkty do przeprowadzki', 'category_id': 825, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elementy-mebli-i-okucia/polki-i-wsporniki,a2616.html', 'name': 'Półki i wsporniki', 'category_id': 2616, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elementy-mebli-i-okucia/plyty-wykonczeniowe,a835.html', 'name': 'Płyty wykończeniowe', 'category_id': 835, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elementy-mebli-i-okucia/galki-uchwyty-klucze,a849.html', 'name': 'Gałki, uchwyty, klucze', 'category_id': 849, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elementy-mebli-i-okucia/okucia-i-zlacza-meblowe,a857.html', 'name': 'Okucia i złącza meblowe', 'category_id': 857, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/elementy-mebli-i-okucia/akcesoria-meblowe,a880.html', 'name': 'Akcesoria meblowe', 'category_id': 880, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kominki/kominki-piece-kominkowe,a897.html', 'name': 'Kominki, piece kominkowe', 'category_id': 897, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kominki/instalacje-kominkowe,a909.html', 'name': 'Instalacje kominkowe', 'category_id': 909, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/kominki/akcesoria-i-materialy-eksploatacyjne,a923.html', 'name': 'Akcesoria i materiały eksploatacyjne', 'category_id': 923, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby/farby-do-scian-i-sufitow,a740.html', 'name': 'Farby do ścian i sufitów', 'category_id': 740, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby/efekty-dekoratorskie,a767.html', 'name': 'Efekty dekoratorskie', 'category_id': 767, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby/emalie-spraye,a808.html', 'name': 'Emalie, spraye', 'category_id': 808, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby/srodki-do-drewna,a813.html', 'name': 'Środki do drewna', 'category_id': 813, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby/przygotowanie-podloza,a848.html', 'name': 'Przygotowanie podłoża', 'category_id': 848, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/farby/walki-pedzle-akcesoria-malarskie,a3183.html', 'name': 'Wałki, pędzle, akcesoria malarskie', 'category_id': 3183, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-scian-sufitow-i-innych-powierzchni/tapety-bordiury,a866.html', 'name': 'Tapety, bordiury', 'category_id': 866, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-scian-sufitow-i-innych-powierzchni/fototapety-naklejki,a903.html', 'name': 'Fototapety, naklejki', 'category_id': 903, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-scian-sufitow-i-innych-powierzchni/kleje-i-akcesoria-do-tapetowania,a910.html', 'name': 'Kleje i akcesoria do tapetowania', 'category_id': 910, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-scian-sufitow-i-innych-powierzchni/okleiny-meblowe-folie-statyczne-akcesoria,a2652.html', 'name': 'Okleiny meblowe, folie statyczne, akcesoria', 'category_id': 2652, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-scian-sufitow-i-innych-powierzchni/sztukateria-dekoracja-sufitu,a914.html', 'name': 'Sztukateria, dekoracja sufitu', 'category_id': 914, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-okien/tkaniny-firany-i-akcesoria,a942.html', 'name': 'Tkaniny, firany i akcesoria', 'category_id': 942, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-okien/karnisze,a933.html', 'name': 'Karnisze', 'category_id': 933, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-okien/szyny-i-akcesoria,a1324.html', 'name': 'Szyny i akcesoria', 'category_id': 1324, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-okien/rolety-i-zaluzje,a927.html', 'name': 'Rolety i żaluzje', 'category_id': 927, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-okien/pasmanteria,a949.html', 'name': 'Pasmanteria', 'category_id': 949, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/oswietlenie-scienne-i-sufitowe,a954.html', 'name': 'Oświetlenie ścienne i sufitowe', 'category_id': 954, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/oswietlenie-podlogowe,a3219.html', 'name': 'Oświetlenie podłogowe', 'category_id': 3219, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/oswietlenie-stolowe-biurkowe,a978.html', 'name': 'Oświetlenie stołowe, biurkowe', 'category_id': 978, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/reflektory-i-halogeny-sufitowe,a972.html', 'name': 'Reflektory i halogeny sufitowe', 'category_id': 972, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/panele-led-oswietlenie-funkcjonalne,a3030.html', 'name': 'Panele LED, oświetlenie funkcjonalne', 'category_id': 3030, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/oswietlenie-do-kuchni,a3032.html', 'name': 'Oświetlenie do kuchni', 'category_id': 3032, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/oswietlenie-do-lazienki,a2507.html', 'name': 'Oświetlenie do łazienki', 'category_id': 2507, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/stworz-wlasna-lampe,a992.html', 'name': 'Stwórz własną lampę', 'category_id': 992, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/tasmy-led-profile-zasilacze,a1185.html', 'name': 'Taśmy LED, profile, zasilacze', 'category_id': 1185, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/zarowki-led-swietlowki,a2447.html', 'name': 'Żarówki LED, świetlówki', 'category_id': 2447, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/akcesoria-i-osprzet-oswietleniowy,a2455.html', 'name': 'Akcesoria i osprzęt oświetleniowy', 'category_id': 2455, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie/oswietlenie-ogrodowe,a2736.html', 'name': 'Oświetlenie ogrodowe', 'category_id': 2736, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dywany-i-wykladziny/dywany,a1211.html', 'name': 'Dywany', 'category_id': 1211, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dywany-i-wykladziny/wykladziny-podlogowe-sztuczne-trawy,a1216.html', 'name': 'Wykładziny podłogowe, sztuczne trawy', 'category_id': 1216, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dywany-i-wykladziny/chodniki-i-nakladki-schodowe,a1221.html', 'name': 'Chodniki i nakładki schodowe', 'category_id': 1221, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dywany-i-wykladziny/wycieraczki-zewnetrzne-i-wewnetrzne,a1224.html', 'name': 'Wycieraczki zewnętrzne i wewnętrzne', 'category_id': 1224, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-wnetrz/swiece-olejki-zapachowe-swieczniki,a3104.html', 'name': 'Świece, olejki zapachowe, świeczniki', 'category_id': 3104, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-wnetrz/poduszki-siedziska-narzuty-posciel-legowiska,a1235.html', 'name': 'Poduszki, siedziska, narzuty, pościel, legowiska', 'category_id': 1235, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-wnetrz/dekoracja-stolu,a3105.html', 'name': 'Dekoracja stołu', 'category_id': 3105, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-wnetrz/artykuly-dekoracyjne,a1246.html', 'name': 'Artykuły dekoracyjne', 'category_id': 1246, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-wnetrz/swiat-dziecka,a3288.html', 'name': 'Świat dziecka', 'category_id': 3288, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/dekoracja-wnetrz/dekoracje-i-ozdoby-swiateczne,a1256.html', 'name': 'Dekoracje i ozdoby świąteczne', 'category_id': 1256, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ramki-obrazy-lustra/ramki-galerie-antyramy,a1293.html', 'name': 'Ramki, galerie, antyramy', 'category_id': 1293, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ramki-obrazy-lustra/obrazy-plakaty-i-dekoracje-scienne,a1294.html', 'name': 'Obrazy, plakaty i dekoracje ścienne', 'category_id': 1294, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/ramki-obrazy-lustra/lustra,a1296.html', 'name': 'Lustra', 'category_id': 1296, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/atelier-artystyczne/artykuly-dla-plastykow,a1309.html', 'name': 'Artykuły dla plastyków', 'category_id': 1309, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/atelier-artystyczne/artykuly-dla-dzieci,a1314.html', 'name': 'Artykuły dla dzieci', 'category_id': 1314, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/organizacja-miejsca-pracy/tablice-kredowe-i-korkowe,a2491.html', 'name': 'Tablice kredowe i korkowe', 'category_id': 2491, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/organizacja-miejsca-pracy/akcesoria-biurowe,a2497.html', 'name': 'Akcesoria biurowe', 'category_id': 2497, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/organizacja-miejsca-pracy/oswietlenie-miejsca-pracy,a2517.html', 'name': 'Oświetlenie miejsca pracy', 'category_id': 2517, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/maszyny-ogrodnicze/kosiarki-traktorki-roboty-koszace,a28.html', 'name': 'Kosiarki, traktorki, roboty koszące', 'category_id': 28, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/maszyny-ogrodnicze/kosy-podkaszarki,a3200.html', 'name': 'Kosy, podkaszarki', 'category_id': 3200, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/maszyny-ogrodnicze/wertykulatory-glebogryzarki,a29.html', 'name': 'Wertykulatory, glebogryzarki', 'category_id': 29, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/maszyny-ogrodnicze/pily-pilarki-luparki,a30.html', 'name': 'Piły, pilarki, łuparki', 'category_id': 30, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/maszyny-ogrodnicze/nozyce-ogrodowe,a1576.html', 'name': 'Nożyce ogrodowe', 'category_id': 1576, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/maszyny-ogrodnicze/oleje-filtry-swiece-zaplonowe,a31.html', 'name': 'Oleje, filtry, świece zapłonowe', 'category_id': 31, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/maszyny-ogrodnicze/przedluzacze-ladowarki-akumulatory,a32.html', 'name': 'Przedłużacze, ładowarki, akumulatory', 'category_id': 32, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/porzadki-w-ogrodzie/myjki-i-akcesoria,a33.html', 'name': 'Myjki i akcesoria', 'category_id': 33, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/porzadki-w-ogrodzie/odkurzacze-rozdrabniacze,a34.html', 'name': 'Odkurzacze, rozdrabniacze', 'category_id': 34, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/porzadki-w-ogrodzie/zamiatarki-odsniezarki-lopaty,a36.html', 'name': 'Zamiatarki, odśnieżarki, łopaty', 'category_id': 36, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/porzadki-w-ogrodzie/gospodarka-odpadami-segregacja-smieci,a35.html', 'name': 'Gospodarka odpadami, segregacja śmieci', 'category_id': 35, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/porzadki-w-ogrodzie/transport-i-przechowywanie,a2582.html', 'name': 'Transport i przechowywanie', 'category_id': 2582, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/porzadki-w-ogrodzie/szczotki-grabie-srodki-czystosci,a37.html', 'name': 'Szczotki, grabie, środki czystości', 'category_id': 37, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/porzadki-w-ogrodzie/suszarki-ogrodowe-i-akcesoria,a38.html', 'name': 'Suszarki ogrodowe i akcesoria', 'category_id': 38, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-ogrodnicze/nozyce-sekatory,a39.html', 'name': 'Nożyce, sekatory', 'category_id': 39, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-ogrodnicze/siekiery-pily-noze,a40.html', 'name': 'Siekiery, piły, noże', 'category_id': 40, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-ogrodnicze/prace-w-ziemi,a41.html', 'name': 'Prace w ziemi', 'category_id': 41, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-ogrodnicze/pielegnacja-trawnika-i-roslin,a2156.html', 'name': 'Pielęgnacja trawnika i roślin', 'category_id': 2156, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-ogrodnicze/serie-narzedzi-i-narzedzia-drobne,a42.html', 'name': 'Serie narzędzi i narzędzia drobne', 'category_id': 42, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-ogrodnicze/odziez-robocza,a43.html', 'name': 'Odzież robocza', 'category_id': 43, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/narzedzia-ogrodnicze/akcesoria-do-narzedzi,a1719.html', 'name': 'Akcesoria do narzędzi', 'category_id': 1719, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/nawadnianie/pompy-i-hydrofory,a1824.html', 'name': 'Pompy i hydrofory', 'category_id': 1824, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/nawadnianie/weze-zlaczki-zraszacze,a1698.html', 'name': 'Węże, złączki, zraszacze', 'category_id': 1698, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/nawadnianie/zbiorniki-na-deszczowke-konewki,a54.html', 'name': 'Zbiorniki na deszczówkę, konewki', 'category_id': 54, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/nawadnianie/nawadnianie-wynurzalne,a53.html', 'name': 'Nawadnianie wynurzalne', 'category_id': 53, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/nawadnianie/nawadnianie-kropelkowe,a52.html', 'name': 'Nawadnianie kropelkowe', 'category_id': 52, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/nawadnianie/automatyka-do-nawadniania,a1691.html', 'name': 'Automatyka do nawadniania', 'category_id': 1691, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie/grille-i-akcesoria,a44.html', 'name': 'Grille i akcesoria', 'category_id': 44, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie/meble-ogrodowe,a45.html', 'name': 'Meble ogrodowe', 'category_id': 45, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie/parasole-pawilony-markizy,a46.html', 'name': 'Parasole, pawilony, markizy', 'category_id': 46, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie/hustawki-ogrodowe-hamaki,a47.html', 'name': 'Huśtawki ogrodowe, hamaki', 'category_id': 47, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie/baseny-i-akcesoria,a1916.html', 'name': 'Baseny i akcesoria', 'category_id': 1916, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie/plac-zabaw-dla-dzieci,a48.html', 'name': 'Plac zabaw dla dzieci', 'category_id': 48, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie/ochrona-przed-owadami,a49.html', 'name': 'Ochrona przed owadami', 'category_id': 49, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/relaks-w-ogrodzie/camping-biwak,a2434.html', 'name': 'Camping, biwak', 'category_id': 2434, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/architektura-ogrodowa/tarasy-sciezki-podjazdy,a55.html', 'name': 'Tarasy, ścieżki, podjazdy', 'category_id': 55, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/architektura-ogrodowa/domki-altany-i-wiaty,a1912.html', 'name': 'Domki, altany i wiaty', 'category_id': 1912, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/architektura-ogrodowa/ploty-pergole-kratki-donice-ogrodowe,a56.html', 'name': 'Płoty, pergole, kratki, donice ogrodowe', 'category_id': 56, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/architektura-ogrodowa/oczka-wodne,a58.html', 'name': 'Oczka wodne', 'category_id': 58, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/architektura-ogrodowa/budy-karmniki-karma-dla-ptakow,a2239.html', 'name': 'Budy, karmniki, karma dla ptaków', 'category_id': 2239, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie-doniczki-i-dekoracje/oswietlenie-ogrodowe-i-zewnetrzne,a61.html', 'name': 'Oświetlenie ogrodowe i zewnętrzne', 'category_id': 61, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie-doniczki-i-dekoracje/doniczki-oslonki-i-kwietniki,a62.html', 'name': 'Doniczki, osłonki i kwietniki', 'category_id': 62, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie-doniczki-i-dekoracje/donice-ogrodowe-i-skrzynki-balkonowe,a63.html', 'name': 'Donice ogrodowe i skrzynki balkonowe', 'category_id': 63, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie-doniczki-i-dekoracje/oslony-na-balkon,a1950.html', 'name': 'Osłony na balkon', 'category_id': 1950, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie-doniczki-i-dekoracje/lampiony-figury-i-fontanny,a1921.html', 'name': 'Lampiony, figury i fontanny', 'category_id': 1921, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/oswietlenie-doniczki-i-dekoracje/dodatki-dekoracyjne,a1631.html', 'name': 'Dodatki dekoracyjne', 'category_id': 1631, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/markizy-maty-oslony,a2383.html', 'name': 'Markizy, maty, osłony', 'category_id': 2383, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/meble-tarasowe-i-balkonowe,a2375.html', 'name': 'Meble tarasowe i balkonowe', 'category_id': 2375, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/plytki-deski-i-podesty-tarasowe,a2369.html', 'name': 'Płytki, deski i podesty tarasowe', 'category_id': 2369, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/oswietlenie-balkonu-i-tarasu,a2417.html', 'name': 'Oświetlenie balkonu i tarasu', 'category_id': 2417, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/doniczki-oslonki-kwietniki,a2389.html', 'name': 'Doniczki, osłonki, kwietniki', 'category_id': 2389, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/skrzynki-balkonowe-donice,a2395.html', 'name': 'Skrzynki balkonowe, donice', 'category_id': 2395, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/dekoracje-i-ozdoby,a2401.html', 'name': 'Dekoracje i ozdoby', 'category_id': 2401, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/rosliny-na-balkon,a2405.html', 'name': 'Rośliny na balkon', 'category_id': 2405, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/balkon-i-taras/podlewanie,a2409.html', 'name': 'Podlewanie', 'category_id': 2409, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/rosliny-nasiona-cebule/kwiaty-doniczkowe-i-pokojowe,a3367.html', 'name': 'Kwiaty doniczkowe i pokojowe', 'category_id': 3367, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/rosliny-nasiona-cebule/rosliny-balkonowe-i-ogrodowe,a64.html', 'name': 'Rośliny balkonowe i ogrodowe', 'category_id': 64, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/rosliny-nasiona-cebule/las-w-sloiku,a3303.html', 'name': 'Las w słoiku', 'category_id': 3303, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/rosliny-nasiona-cebule/obrazy-z-mchu-zielone-sciany,a3383.html', 'name': 'Obrazy z mchu, zielone ściany', 'category_id': 3383, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/rosliny-nasiona-cebule/trawa,a3044.html', 'name': 'Trawa', 'category_id': 3044, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/rosliny-nasiona-cebule/nasiona-i-grzybnie,a65.html', 'name': 'Nasiona i grzybnie', 'category_id': 65, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/rosliny-nasiona-cebule/cebulki,a66.html', 'name': 'Cebulki', 'category_id': 66, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/uprawa-i-ochrona-roslin/podloza-nawozy,a67.html', 'name': 'Podłoża, nawozy', 'category_id': 67, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/uprawa-i-ochrona-roslin/srodki-ochrony-roslin-opryskiwacze,a68.html', 'name': 'Środki ochrony roślin, opryskiwacze', 'category_id': 68, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/uprawa-i-ochrona-roslin/szklarnie-tunele-kompostowniki,a2209.html', 'name': 'Szklarnie, tunele, kompostowniki', 'category_id': 2209, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/uprawa-i-ochrona-roslin/podporki-paletki-do-rozsad,a69.html', 'name': 'Podpórki, paletki do rozsad', 'category_id': 69, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/uprawa-i-ochrona-roslin/agrowlokniny-folie-siatki-ochronne,a70.html', 'name': 'Agrowłókniny, folie, siatki ochronne', 'category_id': 70, 'has_childs': True, 'has_products': False},
{'url': 'https://www.leroymerlin.pl/uprawa-i-ochrona-roslin/przetworstwo-warzyw-i-owocow,a72.html', 'name': 'Przetwórstwo warzyw i owoców', 'category_id': 72, 'has_childs': True, 'has_products': False},
]



## BASE TASK TEST
# tasker = BaseTask()
# scraper = tasker.start_scraper(package='leroy_merlin', module_name='leroy_merlin', class_name='LeroyMerlinScraper')
# with scraper(requested_url="https://www.new.leroymerlin.pl/", store_url="https://www.leroymerlin.pl/") as scr:
#     element = scr.visit_page(url=scr.requested_url)
#     generator = scr.find_categories_data(category_level=0, html_element=element)
#     for cat in generator:
#         print(cat)
#     scr.quit_and_clean()

## LOADER TEST
loader = TaskOperator()
scraper = loader.load_scraper()
with scraper(requested_url="https://www.new.leroymerlin.pl/") as scr:
    element = scr.visit_page(url=scr.requested_url)
    generator = scr.find_categories_data(category_level=0, html_element=element)
    for cat in generator:
        print(cat)
    scr.quit_and_clean()

# FIND CATEGORIES 0
# print('!!!!! STARTING CATS 0 !!!!!')
# scraper = LeroyMerlinScraper(
#     requested_url="https://www.new.leroymerlin.pl/",
#     store_url="https://www.leroymerlin.pl/"
# )
# element = scraper.visit_page(url=scraper.requested_url)
# generator = scraper.find_categories_data(category_level=0, html_element=element)
# for cat in generator:
#     print(cat)
# scraper.quit_and_clean()

# FIND CATEGORIES 1
# print('!!!!! STARTING CATS 1 !!!!!')
# for dict in url_1:
#     scraper = LeroyMerlinScraper(
#         requested_url=dict['url'],
#         store_url="https://www.leroymerlin.pl/"
#     )
#     element = scraper.visit_page(url=scraper.requested_url)
#     generator = scraper.find_categories_data(category_level=1, html_element=element)
#     for cat in generator:
#         print(cat)
#     scraper.quit_and_clean()

# FIND CATEGORIES 2
# print('!!!!! STARTING CATS 2 !!!!!')
# for dict in url_2:
#     scraper = LeroyMerlinScraper(
#         requested_url=dict['url'],
#         store_url="https://www.leroymerlin.pl/"
#     )
#     element = scraper.visit_page(url=scraper.requested_url)
#     generator = scraper.find_categories_data(category_level=2, html_element=element)

#     for cat in generator:
#         print(cat)
#     scraper.quit_and_clean()


# #FIND CATEGORIES 3
# print('!!!!! STARTING CATS 3 !!!!!')
# for dict in url_3:
#     scraper = LeroyMerlinScraper(
#         requested_url=dict['url'],
#         store_url="https://www.leroymerlin.pl/"
#     )
#     element = scraper.visit_page(url=scraper.requested_url)
#     generator = scraper.find_categories_data(category_level=3, html_element=element)
#     with open("manual_url.txt", "a") as myfile:
#         for cat in generator:
#             myfile.write(f"{str(cat)},\n")
#     scraper.quit_and_clean()



# # FIND PRODUCTS 3
# from urls import urls
# print('!!!!! STARTING PRODUCTS 3 !!!!!')
# for dict in urls:
#     scraper = LeroyMerlinScraper(
#         requested_url=dict['url'],
#         store_url="https://www.leroymerlin.pl/"
#     )
#     element = scraper.visit_page(url=scraper.requested_url)
#     generator = scraper.find_all_products_data(category_level=3)
#     for cat in generator:
#         print(cat)
#     scraper.quit_and_clean()