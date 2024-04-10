import pandas as pd

villes = ['Aigues Mortes', 
           'Aix en Provence', 
           'Amiens', 
           'Annecy', 
           'Ariege',
           'Avignon', 
           'Bayeux', 
           'Bayonne', 
           'Besancon', 
           'Biarritz', 
           'Bormes les Mimosas',
           'Carcassonne', 
           'Cassis',
           'Chateau du Haut Koenigsbourg', 
           'Collioure', 
           'Colmar', 
           'Dijon',
           'Eguisheim', 
           'Gorges du Verdon',
           'Grenoble',
           'La Rochelle', 
           'Le Havre', 
           'Lille', 
           'Lyon', 
           'Marseille',
           'Mont Saint Michel', 
           'Montauban', 
           'Nimes', 
           'Paris', 
           'Rouen', 
           'Saintes Maries de la mer',
           'St Malo',
           'Strasbourg',
           'Toulouse', 
           'Uzes'
          ]

urls_ville = [
    "https://www.booking.com/searchresults.fr.html?ss=Aigues-Mortes%2C+Languedoc-Roussillon%2C+France&efdco=1&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AoKD0LAGwAIB0gIkYTAwNTk0MWMtNTUyYS00YmM2LThmNDQtY2RmMmI3YzQwMTc52AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1406800&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3832670114890016&ac_meta=GhAzODMyNjcwMTE0ODkwMDE2IAAoATICZnI6DUFpZ3VlcyBNb3J0ZXNAAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Aix+en+Provence&label=gen173rf-1FCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGiAhBzZWFyY2guYnJhdmUuY29tqAIDuAKLldCwBsACAdICJGI4Yjk0MjU0LWJmN2ItNGVmMi1hODkzLWI1NzE0YzZiODgwNdgCBeACAQ&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1406939&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3f026b859bd2007e&ac_meta=GhAzZjAyNmI4NTliZDIwMDdlIAAoATICZnI6D0FpeCBlbiBQcm92ZW5jZUAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Amiens&label=gen173rf-1FCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGiAhBzZWFyY2guYnJhdmUuY29tqAIDuAKLldCwBsACAdICJGI4Yjk0MjU0LWJmN2ItNGVmMi1hODkzLWI1NzE0YzZiODgwNdgCBeACAQ&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1407447&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3f026b859bd2007e&ac_meta=GhAzZjAyNmI4NTliZDIwMDdlIAAoATICZnI6BkFtaWVuc0AASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Annecy&label=gen173rf-1FCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGiAhBzZWFyY2guYnJhdmUuY29tqAIDuAKLldCwBsACAdICJGI4Yjk0MjU0LWJmN2ItNGVmMi1hODkzLWI1NzE0YzZiODgwNdgCBeACAQ&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1407760&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3f026b859bd2007e&ac_meta=GhAzZjAyNmI4NTliZDIwMDdlIAAoATICZnI6BkFubmVjeUAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Ariege&label=gen173rf-1FCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGiAhBzZWFyY2guYnJhdmUuY29tqAIDuAKLldCwBsACAdICJGI4Yjk0MjU0LWJmN2ItNGVmMi1hODkzLWI1NzE0YzZiODgwNdgCBeACAQ&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Avignon&label=gen173rf-1FCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGiAhBzZWFyY2guYnJhdmUuY29tqAIDuAKLldCwBsACAdICJGI4Yjk0MjU0LWJmN2ItNGVmMi1hODkzLWI1NzE0YzZiODgwNdgCBeACAQ&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1409631&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3f026b859bd2007e&ac_meta=GhAzZjAyNmI4NTliZDIwMDdlIAAoATICZnI6B0F2aWdub25AAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Bayeux&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Bayonne&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Besancon&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1412198&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6CEJlc2FuY29uQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Biarritz&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Bormes+les+Mimosas&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Carcassonne&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Cassis&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1416912&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BkNhc3Npc0AASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Chateau+du+Haut+Koenigsbourg&ssne=Paris&ssne_untouched=Paris&efdco=1&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_id=204055&dest_type=landmark&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=4&search_selected=true&search_pageview_id=f0676c97f79d07d2&ac_meta=GhBmMDY3NmM5N2Y3OWQwN2QyIAAoATICZnI6HENoYXRlYXUgZHUgSGF1dCBLb2VuaWdzYm91cmdAAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Collioure&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Colmar&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1421049&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BkNvbG1hckAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Dijon&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1423981&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BURpam9uQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Eguisheim&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1425030&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6CUVndWlzaGVpbUAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Gorges+du+Verdon&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=2746&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6EEdvcmdlcyBkdSBWZXJkb25AAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Grenoble&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=La+Rochelle&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1438604&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6C0xhIFJvY2hlbGxlQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Le+Havre&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1441598&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6CExlIEhhdnJlQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Lille&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1447079&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BUxpbGxlQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Lyon&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1448468&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BEx5b25AAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Marseille&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1449947&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6CU1hcnNlaWxsZUAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Mont+Saint+Michel&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=900039327&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6EU1vbnQgU2FpbnQgTWljaGVsQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Montauban&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1452421&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6CU1vbnRhdWJhbkAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Nimes&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1455068&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BU5pbWVzQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Paris&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BVBhcmlzQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Rouen&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1462807&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BVJvdWVuQABKAFAA&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Saintes+Maries+de+la+mer&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1465138&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6GFNhaW50ZXMgTWFyaWVzIGRlIGxhIG1lckAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=St+Malo&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1466824&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6B1N0IE1hbG9AAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Strasbourg&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1471697&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6ClN0cmFzYm91cmdAAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Toulouse&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1456928&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
    "https://www.booking.com/searchresults.fr.html?ss=Uzes&label=gen173nr-1FCAEoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQKIAgGoAgO4AvGX0LAGwAIB0gIkMzJhZGM0ZjAtMWU0MC00YTEzLTg5OGQtZDc0M2Q3MzEyNGU32AIF4AIB&aid=304142&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1474231&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38326c38b7230074&ac_meta=GhAzODMyNmMzOGI3MjMwMDc0IAAoATICZnI6BVV6ZXMgQABKAFAA&group_adults=2&no_rooms=1&group_children=0"
]

# Ajoût param pour filtrer sur la note client, Très bien : 8+ et trier par catégorie (ordre croissant)
params_url_note_8plus_order_by_categorie = "&nflt=review_score%3D80&order=class_asc"

#compose urls avec les paramètres supplémentaires
for i  in range(len(urls_ville)):
    urls_ville[i] = urls_ville[i] + params_url_note_8plus_order_by_categorie
#print(urls_ville)

#coordonnées gps des villes
gps_ville = [('Aigues Mortes', '43.5661521', '4.19154'), 
             ('Aix en Provence', '43.5298424', '5.4474738'), 
             ('Amiens', '49.8941708', '2.2956951'), 
             ('Annecy', '45.8992348', '6.1288847'), 
             ('Ariege', '42.9455368', '1.4065544156065486'),
             ('Avignon', '43.9492493', '4.8059012'), 
             ('Bayeux', '49.2764624', '-0.7024738'), 
             ('Bayonne', '43.4945144', '-1.4736657'), 
             ('Besancon', '47.2380222', '6.0243622'), 
             ('Biarritz', '43.4832523', '-1.5592776'), 
             ('Bormes les Mimosas', '43.1506968', '6.3419285'), 
             ('Carcassonne', '43.2130358', '2.3491069'), 
             ('Cassis', '43.2140359', '5.5396318'), 
             ('Chateau du Haut Koenigsbourg', '48.249489800000006', '7.34429620253195'), 
             ('Collioure', '42.52505', '3.0831554'), 
             ('Colmar', '48.0777517', '7.3579641'), 
             ('Dijon', '47.3215806', '5.0414701'), 
             ('Eguisheim', '48.0447968', '7.3079618'), 
             ('Gorges du Verdon', '43.7496562', '6.3285616'), 
             ('Grenoble', '45.1875602', '5.7357819'), 
             ('La Rochelle', '46.1591126', '-1.1520434'), 
             ('Le Havre', '49.4938975', '0.1079732'), 
             ('Lille', '50.6365654', '3.0635282'), 
             ('Lyon', '45.7578137', '4.8320114'), 
             ('Marseille', '43.2961743', '5.3699525'), 
             ('Mont Saint Michel', '48.6359541', '-1.511459954959514'), 
             ('Montauban', '44.0175835', '1.3549991'), 
             ('Nimes', '43.8374249', '4.3600687'), 
             ('Paris', '48.8588897', '2.3200410217200766'), 
             ('Rouen', '49.4404591', '1.0939658'), 
             ('Saintes Maries de la mer', '43.4515922', '4.4277202'), 
             ('St Malo', '49.314695', '-96.9538228'), 
             ('Strasbourg', '48.584614', '7.7507127'), 
             ('Toulouse', '43.6044622', '1.4442469'), 
             ('Uzes', '44.0121279', '4.4196718')]

gps_lat = []
gps_long = []
for ville,lat, long in gps_ville:
    gps_lat.append((lat))
    gps_long.append((long))

#Crée une Map ville_infos : {dest, id, lat, long, url}
keys = ['dest', 'id', 'lat', 'long', 'url']
villes_infos = [{}]
for (dest, id, lat, long, url) in zip(villes, range(len(villes)), gps_lat, gps_long, urls_ville):
    villes_infos.append(dict(zip(keys,(dest, id, lat, long, url))))
#car à l'initialisation créé un élément vide
del villes_infos[0]

start_urls = []
df = pd.read_csv("fichier_final/top_dest.csv")
for index, row in df.iterrows():
    start_urls = start_urls + ([sub['url'] for sub in villes_infos if sub['dest'] == row['destination']])
print(len(start_urls))
print(start_urls)