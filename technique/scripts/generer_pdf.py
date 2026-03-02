import json
import sys
from pathlib import Path
from datetime import datetime

# -------------------------
# Configuration
# -------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
RESULTAT_DIR = ROOT_DIR / "operations" / "resultats"
ENTREPRISE_DIR = ROOT_DIR / "metier" / "entreprise"
LOGO_PATH = ENTREPRISE_DIR / "logo_inn.png"

# -------------------------
# Template HTML
# -------------------------

def build_html(quote, logo_uri):
    d = quote["devis"]
    em = d["emetteur"]
    cl = d["client"]
    cond = d["conditions"]
    planning = d["planning_estime"]

    # Lignes du tableau prestations
    lignes = ""
    for p in d["prestations"]:
        lignes += f"""
        <tr>
            <td class="center">{p['poste']}</td>
            <td>{p['description']}</td>
            <td class="center">{p['quantite']}</td>
            <td class="center">{p['unite']}</td>
            <td class="right">{format_chf(p['prix_unitaire_chf'])}</td>
            <td class="right">{format_chf(p['montant_chf'])}</td>
        </tr>"""

    # Lignes planning
    phases = ""
    for phase in planning["phases"]:
        phases += f"<li>{phase}</li>\n"

    # Hypotheses
    hypotheses = ""
    for h in d["hypotheses"]:
        hypotheses += f"<li>{h}</li>\n"

    # Logo HTML
    logo_html = ""
    if logo_uri:
        logo_html = f'<img src="{logo_uri}" alt="Logo" class="logo">'

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Devis {d['id']}</title>
    <style>
        @page {{
            size: A4;
            margin: 20mm 18mm 25mm 18mm;
            @bottom-center {{
                content: "Page " counter(page) " / " counter(pages);
                font-size: 9px;
                color: #999;
            }}
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-size: 11px;
            color: #333;
            line-height: 1.5;
        }}

        .header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 30px;
            border-bottom: 3px solid #2c5282;
            padding-bottom: 20px;
        }}

        .logo {{
            max-height: 70px;
            max-width: 200px;
        }}

        .company-info {{
            text-align: right;
            font-size: 10px;
            color: #555;
        }}

        .company-info .name {{
            font-size: 16px;
            font-weight: bold;
            color: #2c5282;
        }}

        .devis-title {{
            background-color: #2c5282;
            color: white;
            padding: 12px 20px;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }}

        .devis-meta {{
            background-color: #ebf4ff;
            padding: 8px 20px;
            font-size: 10px;
            color: #2c5282;
            margin-bottom: 25px;
        }}

        .two-columns {{
            display: flex;
            gap: 40px;
            margin-bottom: 25px;
        }}

        .column {{
            flex: 1;
        }}

        .section-title {{
            font-size: 12px;
            font-weight: bold;
            color: #2c5282;
            border-bottom: 1px solid #cbd5e0;
            padding-bottom: 4px;
            margin-bottom: 8px;
        }}

        .client-box {{
            background-color: #f7fafc;
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            padding: 12px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 10.5px;
        }}

        table th {{
            background-color: #2c5282;
            color: white;
            padding: 8px 10px;
            text-align: left;
            font-weight: 600;
        }}

        table td {{
            padding: 7px 10px;
            border-bottom: 1px solid #e2e8f0;
        }}

        table tr:nth-child(even) td {{
            background-color: #f7fafc;
        }}

        .center {{ text-align: center; }}
        .right {{ text-align: right; }}

        .totals {{
            width: 320px;
            margin-left: auto;
            margin-bottom: 25px;
        }}

        .totals table td {{
            padding: 5px 10px;
        }}

        .totals .total-row td {{
            font-weight: bold;
            font-size: 13px;
            background-color: #2c5282 !important;
            color: white;
            border: none;
        }}

        .totals .remise td {{
            color: #c53030;
        }}

        .info-section {{
            margin-bottom: 20px;
        }}

        .info-section ul {{
            margin-left: 20px;
        }}

        .info-section li {{
            margin-bottom: 3px;
        }}

        .conditions-grid {{
            display: flex;
            gap: 20px;
            margin-bottom: 25px;
        }}

        .condition-box {{
            flex: 1;
            background-color: #f7fafc;
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            padding: 12px;
            text-align: center;
        }}

        .condition-box .value {{
            font-size: 18px;
            font-weight: bold;
            color: #2c5282;
        }}

        .condition-box .label {{
            font-size: 9px;
            color: #718096;
            margin-top: 2px;
        }}

        .signature-area {{
            margin-top: 40px;
            display: flex;
            justify-content: space-between;
        }}

        .signature-block {{
            width: 45%;
            border-top: 1px solid #cbd5e0;
            padding-top: 8px;
            font-size: 10px;
            color: #718096;
        }}
    </style>
</head>
<body>

    <!-- EN-TETE -->
    <div class="header">
        <div>
            {logo_html}
            {f'<div style="font-size:16px;font-weight:bold;color:#2c5282;margin-top:5px;">{em["nom"]}</div>' if not logo_uri else ''}
        </div>
        <div class="company-info">
            <div class="name">{em['nom']}</div>
            {em['adresse']}<br>
            IDE : {em['ide']}<br>
            {em['email']}<br>
            {em['telephone']}
        </div>
    </div>

    <!-- TITRE DEVIS -->
    <div class="devis-title">Devis {d['id']}</div>
    <div class="devis-meta">
        Date d'emission : {format_date(d['date_emission'])} &nbsp;|&nbsp;
        Valable jusqu'au : {format_date(d['date_validite'])}
    </div>

    <!-- CLIENT -->
    <div class="two-columns">
        <div class="column">
            <div class="section-title">Objet</div>
            <p>{d['titre']}</p>
        </div>
        <div class="column">
            <div class="section-title">Client</div>
            <div class="client-box">
                <strong>{cl['nom']}</strong><br>
                {cl['contact']}<br>
                {cl['adresse']}<br>
                {cl['email']}<br>
                {cl['telephone']}
            </div>
        </div>
    </div>

    <!-- PRESTATIONS -->
    <div class="section-title" style="margin-bottom:10px;">Prestations</div>
    <table>
        <thead>
            <tr>
                <th class="center" style="width:5%">No</th>
                <th style="width:40%">Description</th>
                <th class="center" style="width:8%">Qte</th>
                <th class="center" style="width:12%">Unite</th>
                <th class="right" style="width:15%">Prix unit.</th>
                <th class="right" style="width:15%">Montant</th>
            </tr>
        </thead>
        <tbody>
            {lignes}
        </tbody>
    </table>

    <!-- TOTAUX -->
    <div class="totals">
        <table>
            <tr>
                <td>Sous-total</td>
                <td class="right">{format_chf(d['sous_total_chf'])}</td>
            </tr>
            <tr class="remise">
                <td>Remise {d['remise']['taux_pct']}% ({d['remise']['motif']})</td>
                <td class="right">- {format_chf(d['remise']['montant_chf'])}</td>
            </tr>
            <tr>
                <td>Montant apres remise</td>
                <td class="right">{format_chf(d['montant_apres_remise_chf'])}</td>
            </tr>
            <tr>
                <td>TVA {d['tva']['taux_pct']}%</td>
                <td class="right">{format_chf(d['tva']['montant_chf'])}</td>
            </tr>
            <tr class="total-row">
                <td>Total TTC</td>
                <td class="right">{format_chf(d['total_ttc_chf'])}</td>
            </tr>
        </table>
    </div>

    <!-- CONDITIONS -->
    <div class="section-title" style="margin-bottom:10px;">Conditions de paiement</div>
    <div class="conditions-grid">
        <div class="condition-box">
            <div class="value">{format_chf(cond['acompte_chf'])}</div>
            <div class="label">Acompte {cond['acompte_pct']}% a la signature</div>
        </div>
        <div class="condition-box">
            <div class="value">{cond['delai_paiement']}</div>
            <div class="label">Delai de paiement</div>
        </div>
        <div class="condition-box">
            <div class="value">{cond['garantie']}</div>
            <div class="label">Garantie bugs</div>
        </div>
    </div>

    <!-- PLANNING -->
    <div class="info-section">
        <div class="section-title">Planning estime ({planning['demarrage']} > {planning['livraison']})</div>
        <ul>
            {phases}
        </ul>
    </div>

    <!-- HYPOTHESES -->
    <div class="info-section">
        <div class="section-title">Hypotheses</div>
        <ul>
            {hypotheses}
        </ul>
    </div>

    <!-- SIGNATURES -->
    <div class="signature-area">
        <div class="signature-block">
            <strong>Pour Alpinova Solutions SA</strong><br>
            Date et signature
        </div>
        <div class="signature-block">
            <strong>Pour {cl['nom']}</strong><br>
            Date et signature (bon pour accord)
        </div>
    </div>

</body>
</html>"""

# -------------------------
# Helpers
# -------------------------

def format_chf(amount):
    """Format un montant en style suisse : CHF 12'345"""
    formatted = f"{amount:,.0f}".replace(",", "'")
    return f"CHF {formatted}"

def format_date(date_str):
    """Convertit 2026-02-11 en 11 fevrier 2026"""
    mois = [
        "", "janvier", "fevrier", "mars", "avril", "mai", "juin",
        "juillet", "aout", "septembre", "octobre", "novembre", "decembre"
    ]
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return f"{d.day} {mois[d.month]} {d.year}"

# -------------------------
# Validation humaine
# -------------------------

def afficher_recapitulatif_et_valider(quote):
    """Affiche un recapitulatif des infos cles et demande validation."""
    d = quote["devis"]
    cl = d["client"]
    rem = d["remise"]
    tva = d["tva"]
    cond = d["conditions"]

    print()
    print("=" * 58)
    print("   RECAPITULATIF DU DEVIS - VALIDATION AVANT GENERATION")
    print("=" * 58)
    print()
    print(f"  Devis :     {d['id']}")
    print(f"  Date :      {d['date_emission']}")
    print(f"  Validite :  {d['date_validite']}")
    print()
    print(f"  Client :    {cl['nom']}")
    print(f"  Contact :   {cl['contact']}")
    print()
    print("-" * 58)
    print("  PRESTATIONS")
    print("-" * 58)
    for p in d["prestations"]:
        label = f"  {p['poste']}. {p['description']}"
        montant = format_chf(p['montant_chf'])
        if len(label) > 44:
            label = label[:41] + "..."
        print(f"{label:<45} {montant:>12}")
    print("-" * 58)
    print()
    print(f"  Sous-total :              {format_chf(d['sous_total_chf']):>16}")
    print(f"  Remise {rem['taux_pct']}% ({rem['motif']})")
    print(f"                            {('- ' + format_chf(rem['montant_chf'])):>16}")
    print(f"  Montant apres remise :    {format_chf(d['montant_apres_remise_chf']):>16}")
    print(f"  TVA {tva['taux_pct']}% :                 {format_chf(tva['montant_chf']):>16}")
    print()
    print(f"  >>> TOTAL TTC :           {format_chf(d['total_ttc_chf']):>16} <<<")
    print()
    print(f"  Acompte {cond['acompte_pct']}% :             {format_chf(cond['acompte_chf']):>16}")
    print()
    print("=" * 58)
    print()

    reponse = input("  Valider et generer le devis ? (o/n) : ").strip().lower()
    if reponse not in ("o", "oui", "y", "yes"):
        print()
        print("  Generation annulee.")
        print("  Modifiez operations/resultats/devis.json puis relancez le script.")
        sys.exit(0)

    print()
    print("  Validation OK. Generation en cours...")
    print()

# -------------------------
# Principal
# -------------------------

def main():
    # Charger le devis
    chemin_devis = RESULTAT_DIR / "devis.json"
    if not chemin_devis.exists():
        raise FileNotFoundError(f"Fichier manquant : {chemin_devis}")

    with open(chemin_devis, "r", encoding="utf-8") as f:
        quote = json.load(f)

    # Etape de validation humaine
    afficher_recapitulatif_et_valider(quote)

    # Logo (optionnel)
    logo_uri = None
    if LOGO_PATH.exists():
        import base64
        with open(LOGO_PATH, "rb") as img:
            encoded = base64.b64encode(img.read()).decode("utf-8")
            logo_uri = f"data:image/png;base64,{encoded}"
        print(f"[OK] Logo charge : {LOGO_PATH}")
    else:
        print(f"[!] Pas de logo trouve dans {LOGO_PATH} -- le PDF sera genere sans logo.")

    # Generer le HTML
    html_content = build_html(quote, logo_uri)

    # Sauvegarder le HTML
    html_path = RESULTAT_DIR / "devis.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[OK] HTML genere : {html_path}")

    # Tenter la conversion PDF avec weasyprint
    pdf_path = RESULTAT_DIR / "devis.pdf"
    try:
        from weasyprint import HTML
        HTML(string=html_content, base_url=str(ROOT_DIR)).write_pdf(str(pdf_path))
        print(f"[OK] PDF genere : {pdf_path}")
    except ImportError:
        print()
        print("-" * 50)
        print("weasyprint n'est pas installe.")
        print("Pour generer le PDF automatiquement :")
        print("  pip install weasyprint")
        print()
        print("Alternative : ouvrez le fichier HTML dans")
        print("votre navigateur et faites Ctrl+P > PDF")
        print(f"  {html_path}")
        print("-" * 50)

if __name__ == "__main__":
    main()
