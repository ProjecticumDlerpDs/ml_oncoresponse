"""
Een script met functies voor project: ml_oncoresponse.
Geschreven door: Jalisa van der Zeeuw
Datum: 2025-12-25

Bevat functies voor:
- Inlezen van MSigDB GMT-bestanden
- X
"""

def read_gmt(filepath):
    """Lees een GMT-bestand van MSigDB in en zet om in een dictionary.
    filepath : str
        Pad naar het GMT-bestand
    Returns: dict
        Dictionary met key = pathway naam, value = lijst van genen (HUGO-symbolen)
    Opmerkingen
        GMT-bestanden hebben over het algemeen 3+ kolommen:
        1. pathway naam
        2. link 
        3. lijst van genen (tab-separated)
    """
    pathways = {}
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split("\t")
            name = parts[0] # pathway naam
            genes = parts[2:] # genen derde kolom
            pathways[name] = genes
    return pathways



