# Veilig en bewust werken aan reproduceerbaarheid


Dit bewijsstuk beschrijft hoe ik tijdens mijn project een risico in mijn werkomgeving heb herkend en mijn werkwijze hierop heb aangepast. Ik heb gerichte maatregelen genomen om de betrouwbaarheid en reproduceerbaarheid van mijn project te vergroten.

Dit sluit aan bij criterium 3 (veilig en bewust werken), omdat ik risico's in mijn werkwijze heb ontdekt en maatregelen heb ingebouwd om de kans op fouten te verkleinen. Daarnaast draagt dit ook bij aan criterium 11 (verantwoordelijkheid voor de eigen ontwikkeling) omdat ik mijn manier van werken heb aanpast op basis van ervaring. Ik leer van mijn "fouten" en wil dit meenemen naar volgende projecten.


### Geconstateerd risico

Tijdens het werken in JupyterLab merkte ik dat een geopende terminal op de standaard conda-omgeving (`base`) stond, terwijl mijn notebook draaide in mijn projectomgeving (`ml_oncoresponse`). Ik ben er vervolgens achter gekomen dat wanneer je een (nieuwe) terminal opent in JupyterLab, deze standaard in de `base`-omgeving start, zelfs wanneer JupyterLab is opgestart vanuit een andere conda-omgeving. Hierdoor raakte ik onzeker over de betrouwbaarheid van mijn werkomgeving. Ik wist niet zeker of alle gebruikte libraries daadwerkelijk in mijn projectomgeving waren geinstalleerd, of dat sommige notebooks onbewust afhankelijk waren van packages uit de base-omgeving. Dit zou voor zowel mijzelf als voor anderen tot niet herhaalbare resultaten kunnen leiden.


### Acties die ik heb ondernomen

Naar aanleiding van dit risico heb ik mijn werkwijze aangepast en mijn project stapsgewijs gecontroleerd en opgeschoond. Ik heb daarbij de volgende acties uitgevoerd:

- Gecontroleerd of alle notebooks in dezelfde kernel werken die gekoppeld is aan één conda-omgeving (`ml_oncoresponse`),
- In elk notebook een automatische environment check toegevoegd,
- Alle notebooks opnieuw uitgevoerd van boven naar beneden vanuit de terminal in de juiste conda-omgeving,
- Tijdens dit proces fouten opgespoord en opgelost (foutieve imports, niet-gedefinieerde variabelen en padproblemen),
- De automatisch gegenereerde testbestanden (`*.nbconvert.ipynb`) weer verwijderd na succesvolle uitoering,
- Mijn conda-omgeving vastgelegd en opgeschoond in een nieuw `environment.yml` bestand,
- Outputbestanden (zoals PDF's) uitgesloten van versiebeheer om de repository schoon en reproduceerbaar te houden.


### Ingebouwde veiligheidsmaatregel

Om te voorkomen dat notebooks in de toekomst perongeluk toch in een verkeerde conda-omgeving worden uitgevoerd, heb ik in elk notebook een automatische controle ingebouwd. Deze controle staat bovenaan onder de YAML-header en verifieert of de verwachte projectomgeving actief is. Wanneer een notebook niet in de juiste omgeving wordt uitgevoerd, verschijnt er een waarschuwing. Zie de codecel hieronder:

```python
import sys

EXPECTED_ENV = "ml_oncoresponse"

if EXPECTED_ENV not in sys.prefix:
    print(
        "⚠️ WAARSCHUWING: mogelijk verkeerde conda environment\n"
        f"Verwacht: {EXPECTED_ENV}\n"
        f"Huidig: {sys.prefix}\n"
        "Resultaten kunnen afwijken."
    )
```

Deze maatregel moet voorkomen dat er onbewust in de verkeerde werkomgeving zal worden gewerkt.


### Reflectie

Ik ben me bewust van het feit dat omgevingen niet altijd werken zoals je verwacht. Het is belangrijk om te blijven controleren of je werk reproduceerbaar is. Vaak lijkt het van wel maar blijkt het eigenlijk toch niet zo te zijn. Daarnaast kan je het altijd vergeten om in een nieuwe terminal de juiste omgeving te activeren. Daarom heb ik bovenstaande veiligheidsmaatregel in mijn notebooks ingebouwd. Naast een environment-controle bestaan er ook andere controles die standaard kunnen worden ingebouwd, zoals checks op databestanden of versies. In toekomstige projecten wil ik deze manier van werken structureel toepassen.



