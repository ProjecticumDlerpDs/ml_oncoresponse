---
output:
  pdf_document:
    latex_engine: xelatex
  html_document: default
---

# Bioinformatica project (DlerpB): Predictie van Longkanker Therapie  Respons met Machine Learning

---

## Inhoud

- [Beschrijving](#beschrijving)
- [Benodigdheden](#benodigdheden)
- [Reproduceerbare omgeving](#reproduceerbare-omgeving)
- [Bestandenstructuur](#bestandenstructuur)
- [Data](#data)
- [Uitvoering](#uitvoering)
- [Resultaten](#resultaten)
- [Auteur en contact](#auteurs-en-contact)

---

## Beschrijving

Dit project richt zich op het ontwikkelen van een machine learning-pipeline om de respons van longkanker-cellijnen op verschillende therapieën te voorspellen. Hierbij worden moleculaire kenmerken van de cellijnen gebruikt, zoals mutaties en methylatieprofielen, om te bepalen welke features en modellen het meest voorspellend zijn.

#### **Hoofdvraag:**
Kan een model op basis van mutatie en/of methylatieprofielen van tumorcellijnen voorspellen of een patiënt baat heeft bij een specifiek geneesmiddel?

#### **Deelvragen:**
1.	Data-preparatie: Hoe kan cellijn-data (mutaties, methylatie, drug-response) worden verzameld, opgeschoond en geschikt gemaakt voor machine learning?
2.	Feature-vergelijking: Welke voorspellende waarde hebben mutatieprofielen, methylatieprofielen en de combinatie daarvan voor therapierespons? 
3.	Model-evaluatie: Hoe goed presteren verschillende machine learning-modellen bij het voorspellen van therapierespons voor een specifiek medicijn (gemeten aan de hand van AUC en F1-score)?


---

## Benodigdheden

#### Vereisten

Voordat je begint, zorg dat de volgende software geinstalleerd is op je systeem:

- **Python** (versie 3.9 of hoger)
- **Anaconda Navigator** (voor het beheren van omgevingen en het starten van JupyterLab)
- **JupyterLab** (voor het uitvoeren van de notebooks)
- **Git** (voor versiebeheer en het clonen van de repository)
   
Alternatief voor Anaconda Navigator: je kunt ook Miniconda gebruiken (zie [https://www.anaconda.com/docs/getting-started/miniconda/main](https://www.anaconda.com/docs/getting-started/miniconda/main))

#### Python-packages

De volgende Python-packages worden gebruikt in dit project:

  - pandas (data verwerking)
  - numpy (numerieke berekeningen)
  - scikit-learn (machine learning en evaluatie)
  - matplotlib, seaborn (visualisaties)
  - xgboost (gradient boosting modellen)
 
---

## Reproduceerbare omgeving

Voor dit project wordt gebruikgemaakt van een conda-environment genaamd **ml_oncoresponse**. Deze bevat de benodigde Python-packages.

#### Stappen:

1. Clone dit project:
   
```bash
git clone https://github.com/ProjecticumDlerpDs/ml_oncoresponse.git
cd ml_oncoresponse
```

2. Maak de conda-omgeving aan:
   
```bash
conda create -n ml_oncoresponse python=3.10 
conda activate ml_oncoresponse
```

3. Installeer de benodigde libraries:
   
``` bash
conda install pandas numpy scikit-learn matplotlib seaborn
conda install -c conda-forge xgboost
```

4. Voeg de kernel toe aan JupyterLab:
   
```
python -m ipykernel install --user --name=ml_oncoresponse --display-name "Python (ml_oncoresponse)"
```

5. Open JupyterLab en kies in elk notebook de kernel Python (ml_oncoresponse) om te zorgen dat de juiste environment wordt gebruikt.


---

## Bestandenstructuur

Het project is opgedeeld in twee hoofdmappen, elk met eigen data, scripts en output:

```
ml_oncoresponse/
├── README.md
├── converting_format.ipynb
├── converting_format.pdf
├── data
│   ├── processed
│   └── raw
├── docs
│   ├── git_integratie.ipynb
│   └── git_integratie.md
├── git_integratie.md
├── notebooks
│   └── deelvraag1_dataprep.ipynb
├── output
│   ├── figures
│   └── tables
└── tutorials
    ├── data
    ├── notebooks
    └── output

```

---

## Data

Voor dit project wordt gebruik gemaakt van data afkomstig uit de **Cancer Cell Line Encyclopedia (CCLE)** via **DepMap**. De analyses zijn gebaseerd op de **DepMap Public 25Q2 release**.

#### Gebruikte bestanden

- **Mutaties**

  Somatische mutaties per cellijn. De raw data bevat vaak meerdere annotaties per variant en is nog niet binair gecodeerd.
    - Bestand: `OmicsSomaticMutations.csv`
    - Download: [https://depmap.org/portal/data_page/?tab=currentRelease](https://depmap.org/portal/data_page/?tab=currentRelease)
    
- **Methylatie**:

  Epigenetische profielen van de cellijnen, gegroepeerd in CpG-clusters rond transcription start sites (TSS).
    - Bestand: `CCLE_RRBS_TSS_CpG_clusters_20180614.txt`
    - Download: [https://depmap.org/portal/data_page/?tab=allData](https://depmap.org/portal/data_page/?tab=allData)
  
- **Drug response (AUC)**:

    Gevoeligheid van de cellijnen voor verschillende medicijnen, gemeten als Area Under the Curve (AUC).
  - Bestand:
  - Downloadopties bij DepMap Custom Downloads:
      - Dataset: Drug sensitivity AUC (PRISM Repurposing Secondary Screen)
      - Cell lines: Use all
      - Compounds: Use all
      - Merge into single file:
      - Add metadata: 
      - Exclude NA's:
    - URL: [https://depmap.org/portal/data_page/?tab=customDownloads&utm_source=chatgpt.com](https://depmap.org/portal/data_page/?tab=customDownloads&utm_source=chatgpt.com)
      

#### Verwerkte data in dit project

- De verwerkte data die daadwerkelijk in de notebooks wordt gebruikt, is gefilterd op gemeenschapelijke cellijnen, en cellijn-specifieke features zijn gecombineerd: mutatie + methylatie.

- Target (y) is de AUC voor een specifiek medicijn (één model per medicijn).

- Longkanker analyses zijn gefilterd op `lineage_1 = "Lung"`  # dit moet nog worden aangepast, hier ben ik nog mee bezig

- De verwerkte data is beschikbaar in de map:

  `xxx` # deze is nog niet af

- De notebooks refereren automatisch naar deze map, zodat analyses repdroduceerbaar zijn zonder de volledige raw datasets te hoeven downloaden. # dit moet ik nog aanpassen

---

## Uitvoering

Om de analyses uit te voeren, volg je de onderstaande stappen:

1. Voorbereidingen en harmonisatie van data
   - Ga naar de map `data/raw/` en controleer dat de drie bestanden aanwezig zijn:
       - OmicsSomaticMutations.csv (mutaties
       - CCLE_RRBS_TSS_CpG_clusters_20180614.txt (methylatie)
       - PRISM_AUC.csv (drug response)
    - Gebruik het Python-script of notebook `xxx` om de datasets te harmoniseren:
       - xxx
       - xxx
2. Train/test splots en preprocessing:
    - Verwerk missende waarden...
    - Splots de data in train- en testsets met `train_test_split` uit Scikit-learn
    - Schaal of normaliseerde features indien gewenst (afhankelijk van het model)
3. Modeltraining met Scikit-learn
    - Train meerdere modellen met één medicijn???
    - xxx
4. Resultaten opslaan en visualiseren
    - Sla de getrainde modellen en resultaten op in `results/` of `models/`.
    - Maak plots ..

Zorg ervoor dat alle vereiste Python packages geïnstalleerd zijn zoals beaschreven in de sectie [benodigdheden](benodigdheden), waaronder: pandas, numpy, scikit-learn, matplotlib en seaborn voor visualisaties.

---

## Resultaten

De analyses leveren de volgende outputs op:

- Verwerkte datasets
    - Samengevoegd datavestand met mutatie-, methylatie- en drugresponse-data per cellijn.
    - gefilterde subset per weefseltype (longkanker)
- Invloed van feature-sets
    - Vergelijking van modelprestaties met alleen mutatie-features, alleen methylatie-features, en de combinatie van beide.
    - Hiermee wordt getest of gecombineerde data van de voorspelbaarheid van drug response verbetert.
- Modelprestaties
    - Voor elk medicijn een voorspellingsmodel getrains met Scikit-learn.
    - Evaluatiemetrics (R^2, RMSE) opgeslagen in tabellen.
- Visualisaties
    - Plots van voorspelde vs. waargenomen AUC-waarden.
    - Overzicht van prestaties per medicijn.

Alle resultaten en figuren zijn terug te vinden in de map `results/`.


--- 

## Auteur en contact

**Naam:** Jalisa van der Zeeuw    
**E-mail:** Jalisavanderzeeuw@hotmail.com    
**GitHub:** [https://github.com/ProjecticumDlerpDs/ml_oncoresponse.git](https://github.com/ProjecticumDlerpDs/ml_oncoresponse.git)

Voor vragen, suggesties of feedback kun je contact opnemen via e-mail of een issue aanmaken op de GitHub repository.

---