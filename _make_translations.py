"""Génère les fichiers de traduction FR -> EN pour CEREMAC sans gettext."""
import os
import re
import polib

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIRS = [
    os.path.join(ROOT, 'main', 'templates'),
    os.path.join(ROOT, 'members', 'templates') if os.path.isdir(os.path.join(ROOT, 'members', 'templates')) else None,
    os.path.join(ROOT, 'admin_panel', 'templates') if os.path.isdir(os.path.join(ROOT, 'admin_panel', 'templates')) else None,
]
TEMPLATES_DIRS = [d for d in TEMPLATES_DIRS if d]

# Dictionnaire de traductions FR -> EN
TRANSLATIONS = {
    # Navbar
    "Accueil": "Home",
    "À propos": "About",
    "Départements et Services": "Departments & Services",
    "Publications": "Publications",
    "Partenaires": "Partners",
    "Actualités": "News",
    "Contact": "Contact",
    "Espace Membres": "Members Area",
    "Administration": "Administration",
    "Connexion": "Sign In",
    "Déconnexion": "Sign Out",
    # Hero
    "Centre de Recherche Marine et Côtière de Guinée": "Marine and Coastal Research Center of Guinea",
    "Nos publications scientifiques": "Our scientific publications",
    "Organisation scientifique et services d'excellence": "Scientific organization and excellence services",
    # Sections
    "Newsletter": "Newsletter",
    "Restez informé de nos actualités": "Stay informed of our news",
    "Votre email": "Your email",
    "S'abonner": "Subscribe",
    # Common
    "En savoir plus": "Read more",
    "Lire la suite": "Read more",
    "Retour": "Back",
    "Télécharger": "Download",
    "Télécharger le document": "Download document",
    "En cours": "In progress",
    "Terminé": "Completed",
    "Aucune publication pour le moment.": "No publication available at this time.",
    "Les départements seront bientôt disponibles.": "Departments will be available soon.",
    # Structure
    "Structure Organisationnelle": "Organizational Structure",
    "Nos 5 Départements de Recherche": "Our 5 Research Departments",
    "Nos Services": "Our Services",
    "Le CEREMAC est organisé en Départements de recherche spécialisés et offre une gamme complète de services scientifiques et techniques pour répondre aux besoins de la recherche, de l'industrie et des institutions partenaires dans les domaines de l'océanographie, de l'environnement marin et côtier.":
        "CEREMAC is organized into specialized research Departments and offers a complete range of scientific and technical services to meet the needs of research, industry and partner institutions in the fields of oceanography, marine and coastal environment.",
    # Services
    "Études et Expertises": "Studies and Expertise",
    "Réalisation d'études d'impact environnemental, expertises marines et évaluations écologiques pour les projets côtiers.":
        "Environmental impact assessments, marine expertise and ecological evaluations for coastal projects.",
    "Analyses et Laboratoire": "Analyses and Laboratory",
    "Analyses physico-chimiques et biologiques des eaux, sédiments et organismes marins dans nos laboratoires équipés.":
        "Physico-chemical and biological analyses of water, sediments and marine organisms in our equipped laboratories.",
    "Formation et Stages": "Training and Internships",
    "Accueil de stagiaires, formation continue et ateliers spécialisés en sciences marines et environnementales.":
        "Internship hosting, continuing education and specialized workshops in marine and environmental sciences.",
    "Conseil et Consultation": "Consulting",
    "Conseil scientifique et consultation pour les acteurs publics et privés impliqués dans la gestion des zones côtières.":
        "Scientific advice and consulting for public and private stakeholders involved in coastal zone management.",
    # About
    "À propos du CEREMAC": "About CEREMAC",
    "Notre mission": "Our mission",
    "Notre vision": "Our vision",
    "Nos valeurs": "Our values",
    "Historique": "History",
    "Équipe de Direction": "Management Team",
    "Directeur Général": "General Director",
    # Contact
    "Adresse": "Address",
    "Téléphone": "Phone",
    "Email": "Email",
    "Nom complet": "Full name",
    "Sujet": "Subject",
    "Message": "Message",
    "Envoyer": "Send",
    "Envoyer le message": "Send message",
    "Nous contacter": "Contact us",
    # News
    "Voir l'article": "View article",
    "Lire l'article": "Read article",
    "Publié le": "Published on",
    "Par": "By",
    "Aucune actualité pour le moment.": "No news at this time.",
    # Auth / Members
    "Nom d'utilisateur": "Username",
    "Mot de passe": "Password",
    "Se connecter": "Sign in",
    "S'inscrire": "Sign up",
    "Mot de passe oublié ?": "Forgot password?",
    "Rester connecté": "Remember me",
    "Bienvenue": "Welcome",
    "Tableau de bord": "Dashboard",
    "Mon profil": "My profile",
    "Mes documents": "My documents",
    "Paramètres": "Settings",
    # Footer
    "Tous droits réservés": "All rights reserved",
    "Tous droits réservés.": "All rights reserved.",
    "Mentions légales": "Legal notice",
    "Politique de confidentialité": "Privacy policy",
    # --- Compléments (lot 2) ---
    "Accéder à l'admin": "Access admin",
    "Accédez aux documents exclusifs aux membres": "Access member-only documents",
    "Actif": "Active",
    "Actions": "Actions",
    "Actions rapides": "Quick actions",
    "Actualités & Événements": "News & Events",
    "Admin": "Admin",
    "Administrateur": "Administrator",
    "Ajouter un partenaire": "Add a partner",
    "Ajouter un projet": "Add a project",
    "Ajouter un utilisateur": "Add a user",
    "Ajouter une actualité": "Add a news item",
    "Ajouter une publication": "Add a publication",
    "Aucun abonné pour le moment.": "No subscribers at this time.",
    "Aucun document disponible.": "No document available.",
    "Aucun message pour le moment.": "No messages at this time.",
    "Aucun partenaire pour le moment.": "No partner at this time.",
    "Aucun projet disponible.": "No project available.",
    "Aucun projet pour le moment.": "No project at this time.",
    "Aucun utilisateur pour le moment.": "No users at this time.",
    "Auteur": "Author",
    "CEREMAC": "CEREMAC",
    "Chef de département": "Department Head",
    "Collaboration": "Collaboration",
    "Conduire des recherches de haut niveau en océanographie physique, biologie marine, écologie côtière et changements climatiques.":
        "Conduct high-level research in physical oceanography, marine biology, coastal ecology and climate change.",
    "Conseil aux décideurs, accompagnement de projets et appui technique aux institutions partenaires.":
        "Advisory services to decision-makers, project support and technical assistance to partner institutions.",
    "Conseil et Accompagnement": "Advisory & Support",
    "Consultez les projets internes du centre": "Browse the center's internal projects",
    "Contactez le département": "Contact the department",
    "Contactez-nous": "Contact us",
    "Contactez-nous pour discuter de vos besoins en recherche, expertise ou formation.":
        "Contact us to discuss your research, expertise or training needs.",
    "Date": "Date",
    "Date d'inscription": "Registration date",
    "Dernières Actualités": "Latest News",
    "Description": "Description",
    "Direction Générale": "General Management",
    "Documents réservés": "Restricted documents",
    "Domaines de Recherche": "Research Areas",
    "Du": "From",
    "Durabilité": "Sustainability",
    "Découvrir le CEREMAC": "Discover CEREMAC",
    "Découvrir nos Projets": "Discover our Projects",
    "Départements": "Departments",
    "Développement Technologique": "Technological Development",
    "Engagement en faveur du développement durable et de la protection environnementale.":
        "Commitment to sustainable development and environmental protection.",
    "Environnement": "Environment",
    "Envoyer un email": "Send an email",
    "Excellence": "Excellence",
    "Excellence en recherche et innovation": "Excellence in research and innovation",
    "Formation & Éducation": "Training & Education",
    "Former la prochaine génération de chercheurs, de spécialistes et de professionnels en environnement marin.":
        "Train the next generation of researchers, specialists and professionals in marine environment.",
    "Formulaire de contact": "Contact form",
    "Galerie CEREMAC": "CEREMAC Gallery",
    "Gérer les abonnés": "Manage subscribers",
    "Gérer les abonnés à la newsletter": "Manage newsletter subscribers",
    "Gérer les actualités": "Manage news",
    "Gérer les messages": "Manage messages",
    "Gérer les partenaires": "Manage partners",
    "Gérer les projets": "Manage projects",
    "Gérer les publications": "Manage publications",
    "Gérer les utilisateurs": "Manage users",
    "Gérez votre profil utilisateur": "Manage your user profile",
    "Historique et Évolution": "History and Evolution",
    "Inactif": "Inactive",
    "Informations personnelles": "Personal information",
    "Innovation": "Innovation",
    "Innovation et développement scientifique et technologique en Guinée.":
        "Scientific and technological innovation and development in Guinea.",
    "International": "International",
    "Intéressé par nos services ?": "Interested in our services?",
    "Laboratoires": "Laboratories",
    "Le CEREMAC (Centre de Recherche Marine et Côtière de Guinée) est un établissement public scientifique guinéen, issu de la transformation du CERESCOR entre 2022 et 2025. Notre mission est de développer la recherche scientifique et technologique dans les domaines de l'océanographie, de l'environnement, et des écosystèmes marins et côtiers de la Guinée.":
        "CEREMAC (Marine and Coastal Research Center of Guinea) is a Guinean public scientific institution, resulting from the transformation of CERESCOR between 2022 and 2025. Our mission is to develop scientific and technological research in the fields of oceanography, environment, and marine and coastal ecosystems of Guinea.",
    "Lu": "Read",
    "Membre": "Member",
    "Messages": "Messages",
    "Mission": "Mission",
    "Missions": "Missions",
    "Modifier": "Edit",
    "Musées": "Museums",
    "National": "National",
    "Nom": "Name",
    "Non lu": "Unread",
    "Nos Départements": "Our Departments",
    "Nos Partenaires": "Our Partners",
    "Nos Valeurs": "Our Values",
    "Notre Mission": "Our Mission",
    "Nous Contacter": "Contact Us",
    "Nous visons l'excellence dans toutes nos recherches et publications scientifiques.":
        "We aim for excellence in all our research and scientific publications.",
    "Océanographie": "Oceanography",
    "Organisation Administrative": "Administrative Organization",
    "Organisation Scientifique": "Scientific Organization",
    "Panneau d'administration": "Administration panel",
    "Partenaires Internationaux": "International Partners",
    "Partenaires Nationaux": "National Partners",
    "Participez à nos projets de recherche ou collaborez avec notre équipe pour un avenir durable des océans":
        "Take part in our research projects or collaborate with our team for a sustainable future of the oceans",
    "Pour toute information sur nos activités de recherche ou collaborations":
        "For any information about our research activities or collaborations",
    "Projets": "Projects",
    "Projets Actifs": "Active Projects",
    "Projets du département": "Department projects",
    "Projets internes": "Internal projects",
    "Protection et préservation de l'environnement marin et côtier de la Guinée.":
        "Protection and preservation of Guinea's marine and coastal environment.",
    "Protection et préservation de l'environnement marin et côtier. Surveillance de la qualité des eaux, protection de la biodiversité marine.":
        "Protection and preservation of the marine and coastal environment. Water quality monitoring, marine biodiversity protection.",
    "Précédent": "Previous",
    "Présentation de l'Institution": "About the Institution",
    "Publications du département": "Department publications",
    "Publications scientifiques dans des revues internationales, projets de recherche innovants, formation de la prochaine génération de chercheurs.":
        "Scientific publications in international journals, innovative research projects, training of the next generation of researchers.",
    "Recherche": "Research",
    "Recherche Scientifique": "Scientific Research",
    "Recherche approfondie sur les océans, les courants marins, la température, la salinité et les écosystèmes océaniques.":
        "In-depth research on oceans, marine currents, temperature, salinity and oceanic ecosystems.",
    "Recherche de solutions innovantes pour les défis environnementaux marins.":
        "Search for innovative solutions to marine environmental challenges.",
    "Rejoignez-nous dans notre mission": "Join us in our mission",
    "Retour aux actualités": "Back to news",
    "Retour à l'espace membres": "Back to members area",
    "Rôle": "Role",
    "Services administratifs": "Administrative services",
    "Services d'Appui": "Support Services",
    "Services techniques": "Technical services",
    "Site web": "Website",
    "Sous-structures Scientifiques et Techniques": "Scientific and Technical Sub-structures",
    "Statistiques": "Statistics",
    "Statut": "Status",
    "Structure Scientifique": "Scientific Structure",
    "Suivant": "Next",
    "Titre": "Title",
    "Travail en partenariat avec des institutions nationales et internationales.":
        "Working in partnership with national and international institutions.",
    "Type": "Type",
    "Utilisateurs": "Users",
    "Voir": "View",
    "Voir les documents": "View documents",
    "Voir les détails": "View details",
    "Voir les projets": "View projects",
    "Voir mon profil": "View my profile",
    "Voir tout": "View all",
    "au": "to",
    "Écosystèmes Marins": "Marine Ecosystems",
    "Équipe du département": "Department team",
    "Établissement public scientifique guinéen dédié à l'océanographie, l'environnement et les écosystèmes marins et côtiers":
        "Guinean public scientific institution dedicated to oceanography, environment and marine and coastal ecosystems",
    "Étude des océans, des courants marins, de la température et de la salinité des eaux guinéennes.":
        "Study of oceans, marine currents, temperature and salinity of Guinean waters.",
    "Étude et conservation de la biodiversité marine et des habitats côtiers.":
        "Study and conservation of marine biodiversity and coastal habitats.",
}

# Extraction des chaînes depuis les templates
def extract_strings():
    strings = set()
    patterns = [
        re.compile(r'\{%\s*trans\s+"([^"]+)"\s*%\}'),
        re.compile(r"\{%\s*trans\s+'([^']+)'\s*%\}"),
        re.compile(r'\{%\s*blocktrans\s*%\}(.*?)\{%\s*endblocktrans\s*%\}', re.DOTALL),
    ]
    for tpl_dir in TEMPLATES_DIRS:
        for root, _, files in os.walk(tpl_dir):
            for f in files:
                if not f.endswith('.html'):
                    continue
                path = os.path.join(root, f)
                try:
                    content = open(path, encoding='utf-8').read()
                except Exception:
                    continue
                for pat in patterns:
                    for m in pat.findall(content):
                        strings.add(m.strip())
    return strings

def write_locale(lang_code, translations):
    locale_dir = os.path.join(ROOT, 'locale', lang_code, 'LC_MESSAGES')
    os.makedirs(locale_dir, exist_ok=True)
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': 'CEREMAC 1.0',
        'Report-Msgid-Bugs-To': '',
        'POT-Creation-Date': '2026-01-01 00:00+0000',
        'PO-Revision-Date': '2026-01-01 00:00+0000',
        'Last-Translator': 'CEREMAC',
        'Language-Team': lang_code,
        'Language': lang_code,
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Content-Transfer-Encoding': '8bit',
    }
    extracted = extract_strings()
    # Inclure aussi toutes les clés du dictionnaire (au cas où certaines viendraient du Python)
    all_keys = extracted | set(translations.keys())
    for s in sorted(all_keys):
        entry = polib.POEntry(msgid=s, msgstr=translations.get(s, ''))
        po.append(entry)
    po_path = os.path.join(locale_dir, 'django.po')
    mo_path = os.path.join(locale_dir, 'django.mo')
    po.save(po_path)
    po.save_as_mofile(mo_path)
    print(f"[{lang_code}] {len(po)} entrees -> {po_path}")
    print(f"[{lang_code}] compile -> {mo_path}")

if __name__ == '__main__':
    write_locale('en', TRANSLATIONS)
    # Pour le français : msgstr identique au msgid (langue par défaut)
    fr_dict = {k: k for k in (extract_strings() | set(TRANSLATIONS.keys()))}
    write_locale('fr', fr_dict)
    print("Termine. Redemarrez le serveur Django pour appliquer.")
