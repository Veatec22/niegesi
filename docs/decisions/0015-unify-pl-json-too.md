# Docelowo ujednolicamy też pl.json

Status: zastąpione przez [0021](0021-one-translation-file.md) · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Oprócz pliku review ([0013](0013-one-review-file-format.md)) do jednego kształtu
doprowadzamy też `pl.json`. Ma to być płaska mapa identyfikator → PL, zgodna z plikiem
review. Wtedy jedno wspólne narzędzie nanosi eksport w każdej grze. Wymaga to dostosowania
buildów poszczególnych gier, ale 26 gier powstało w tydzień, więc na ujednolicenie
znajdzie się czas. Dopóki gra nie jest ujednolicona, jej eksport nanosi agent ręcznie.
Stan z 2026-09-25: 18 gier ma już płaską mapę zgodną z review. Odstają Anger Foot,
Holy Shoot, BPM, SPRAWL, Dread Templar, a Heat Signature, OTXO, Turbo Overkill
i Wild Bastards mają w review wpisy spoza `pl.json`.

## Rozważone warianty

- **Ujednolicić tylko to, co czyta pracownia, a `pl.json` zostawić każdej grze**:
  odrzucone. Wszystko i tak może się zmienić, więc lepiej iść od razu w docelowy kształt.
