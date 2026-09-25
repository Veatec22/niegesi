# Pierwsza wersja nie przenosi wpisów między grupami

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Pracownia pokazuje grupy i sekwencje z `structure.yaml` na main
([0010](0010-groups-and-sequences-live-in-repo.md)), ale ich nie zmienia. Nie ma akcji
„Przenieś do grupy”, szkiców przeniesień, stanu przeniesienia ani listy przeniesień
w eksporcie. Zmianę podziału użytkownik zgłasza w komentarzu eksportu albo wprost
agentowi, który poprawia `structure.yaml` w repo.

Użytkownik nie ma jeszcze potrzeby ani pomysłu na przenoszenie. Wracamy do tematu,
gdy pojawi się w praktyce; wtedy punktem wyjścia jest wariant opisany niżej.

## Rozważone warianty

- **Przeniesienie rozliczane jak korekta** (grupa przed/po, rozliczenie z main,
  konflikt przy innej grupie albo usuniętej grupie docelowej, wycofanie po eksporcie):
  odłożone, nie odrzucone.
- **Main zawsze wygrywa, niezgodne przeniesienie porzucane z wpisem w dzienniku**:
  odłożone razem z całym tematem.
