# Holy Shoot PL

## Instalacja

1. Zamknij grę i wypakuj paczkę do katalogu Holy Shoot, zawierającego folder `Windows`.
2. Uruchom grę normalnie. W `Settings → Language` wybierz `Polski`, dopisany na końcu listy. Usuń wcześniejszy parametr `-culture=pl`, jeśli go dodano.
3. Sprawdź menu, ustawienia i samouczek oraz zapamiętanie języka po restarcie. To próbka 37 tekstów; pozostałe zostają po angielsku. Paczka zawiera nakładkę tekstów i rozszerzenie selektora z loaderem UE4SS.

Aby usunąć próbkę, wybierz English i zamknij grę, następnie skasuj trzy pliki `Windows/PVD/Content/Paks/pakchunk99-NieGesiPL_P` (`.pak`, `.utoc`, `.ucas`), `Windows/PVD/Binaries/Win64/dwmapi.dll` i dodany przez paczkę folder `Windows/PVD/Binaries/Win64/ue4ss`. Przy innych modach UE4SS zachowaj wspólny loader, usuwając tylko `Mods/NieGesiPL` i jego wpisy w `mods.txt` oraz `mods.json`. Oryginalne pliki gry nie są zmieniane.
