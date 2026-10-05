# Analyse approfondie du repository historique ESILV

## 1. Objet du document

Ce document analyse le repository historique :

```text
tawounfouet/intro_git_linux_bloomberg
```

utilisé pour l'enseignement précédent autour de :

```text
Python
Git
Linux
Bloomberg
```

L'objectif n'est pas de répliquer l'ancien cours.

L'objectif est de comprendre :

- ce qui était réellement enseigné ;
- la profondeur technique couverte ;
- les choix pédagogiques sous-jacents ;
- les points forts du dispositif ;
- les risques de surcharge ;
- les éléments encore utiles ;
- les éléments qui ne doivent pas revenir dans le CORE actuel ;
- la relation entre cet ancien contenu, le questionnaire diagnostique et le nouveau fil rouge MarketPulse.

Le repository courant de référence est :

```text
tawounfouet/esilv-marketpulse
```

## 2. Base d'analyse

L'analyse a été réalisée à partir de la branche :

```text
main
```

du repository historique.

Commit observé :

```text
d7a463819a7c52195c6f58151203ac3077482278
```

Le repository historique est privé et non archivé au moment de l'analyse.

Les principales sources inspectées sont :

```text
README.md

CM0_Context.pdf
CM1_Linux.pdf
CM2_Git_local.pdf
CM3_Git_remote.pdf
CM4_bloomberg.pdf
Project.pdf

TD1_1_linux_fundamentals.pdf
TD1_2_linux_tools.pdf
TD1_3_linux_Grep.pdf
TD1_4_linux_SSH.pdf
TD2_Git_local.pdf
TD3_Git_branches.pdf

src/CM0_Context.tex
src/CM1_Linux.tex
src/CM2_Git_local.tex
src/CM3_Git_remote.tex
src/CM4_bloomberg.tex
src/Project.tex
src/TD1_1_linux_fundamentals.tex
src/TD1_2_linux_tools.tex
src/TD1_3_linux_Grep.tex
src/TD1_4_linux_SSH.tex
src/TD2_Git_local.tex
src/TD3_Git_branches.tex
src/TD4_Bloomberg.tex

exam/Exam linux git S1 rattrapage.docx
```

## 3. Résumé exécutif

L'ancien dispositif est techniquement riche, ambitieux et professionnellement intéressant.

Il couvre beaucoup plus que ce que le titre "Python, Git, Linux" pourrait laisser penser.

Le périmètre réel inclut notamment :

```text
Linux
+
shell
+
permissions
+
package management
+
environment variables
+
shell scripting
+
cron
+
hashing
+
compression
+
ACL
+
grep / awk / sed / regex
+
SSH / SCP
+
cloud instance
+
Git local
+
Git internals
+
staging
+
undo
+
.gitignore
+
hash objects
+
compression internals
+
Git remote
+
branches
+
conflicts
+
rebase
+
Pull Requests
+
Bloomberg Terminal
+
Bloomberg API
+
xbbg
+
blpapi
+
historical data
+
reference data
+
intraday data
+
web application
+
remote Linux deployment
+
real-time refresh
+
cron reports
+
backtesting
+
portfolio analytics
+
Sharpe ratio
+
max drawdown
+
optional machine learning
```

Le principal constat est donc :

```text
ancien cours
=
très large couverture technique

nouveau MarketPulse
=
périmètre volontairement plus étroit
+
progression fil rouge
+
CORE / OPTIONAL explicites
```

La richesse de l'ancien repository est une excellente source de contenu avancé.

Elle ne constitue pas un bon modèle de charge à réintroduire intégralement dans 18 heures de TD.

## 4. Inventaire du repository historique

Le repository contient environ :

```text
79 fichiers
4 répertoires
environ 16 MB de contenu versionné
```

Répartition principale observée :

| Type | Nombre approximatif |
|---|---:|
| PDF | 26 |
| TEX | 20 |
| PNG | 24 |
| JPG | 3 |
| JPEG | 1 |
| Markdown | 1 |
| DOCX | 1 |
| Shell scripts | 2 |

Le repository est donc principalement un repository de :

```text
supports de cours
+
sources LaTeX
+
supports PDF
+
illustrations
```

et non un repository d'application pédagogique exécutable.

C'est une différence structurelle importante avec MarketPulse.

## 5. Architecture documentaire historique

La structure principale est :

```text
CM0 - Context
CM1 - Linux
CM2 - Git Local
CM3 - Git Remote
CM4 - Bloomberg

TD Linux
TD Git Local
TD Git Branches
TD Bloomberg

Project
Exam
```

Le repository historique fonctionne donc selon une logique :

```text
cours théorique
      |
      v
exercices spécialisés
      |
      v
projet plus large
```

MarketPulse suit une logique différente :

```text
besoin métier
      |
      v
notion technique
      |
      v
évolution du même projet
      |
      v
trace Git
```

## 6. CM0 - Contexte numérique et soutenabilité

Le CM0 ne commence pas immédiatement par Linux.

Il introduit un contexte beaucoup plus large :

- histoire de l'informatique moderne ;
- infrastructure numérique ;
- dimension économique ;
- importance sociotechnique ;
- environnement ;
- consommation énergétique ;
- data centers ;
- PUE ;
- trafic réseau ;
- impact des fichiers binaires dans Git ;
- émissions embarquées et opérationnelles ;
- carbon-aware computing ;
- CodeCarbon ;
- choix d'hébergement ;
- hyperscalers ;
- alternatives plus durables ;
- open source et Linux.

Cette partie donne une profondeur culturelle réelle au cours.

Elle permet de comprendre que :

```text
Linux
Git
APIs
Cloud
```

ne sont pas uniquement des commandes à mémoriser.

Ils s'inscrivent dans une infrastructure technique, économique et environnementale.

### Valeur à conserver

Cette contextualisation est pertinente pour un CM.

Elle ne doit cependant pas être reproduite dans les TD MarketPulse au détriment de la pratique.

Une partie de ce contenu pourrait être conservée dans :

```text
CM
ressources complémentaires
lecture optionnelle
```

plutôt que dans le CORE des 18 heures de TD.

## 7. CM1 - Linux

Le CM1 est très large.

Les thèmes observés comprennent :

- histoire d'Unix ;
- GNU ;
- Linux ;
- POSIX ;
- open source ;
- rôle d'un système d'exploitation ;
- CLI ;
- virtualisation ;
- machines virtuelles ;
- conteneurs ;
- Docker ;
- Kubernetes ;
- Linux en finance ;
- shells ;
- Bash ;
- zsh ;
- fish ;
- commandes de navigation ;
- éditeurs de texte ;
- aide système ;
- sudo ;
- apt ;
- PATH ;
- .profile ;
- variables ;
- structures de contrôle ;
- boucles ;
- SSH ;
- téléchargement de données ;
- wget ;
- curl ;
- grep ;
- sed ;
- expressions régulières ;
- shell scripts ;
- historique shell ;
- sécurité des scripts Bash.

Ce contenu est très riche, mais il correspond davantage à une introduction large à l'environnement Linux qu'à une simple compétence "savoir utiliser Linux pour les TD".

### Différence avec MarketPulse

Le CORE actuel TD01 retient seulement les commandes immédiatement utiles :

```text
pwd
ls
cd
cat
head
grep
python --version
git --version
python src/main.py
```

Ce choix est volontaire.

Le nouvel objectif n'est pas :

```text
maîtriser Linux
```

mais :

```text
être suffisamment autonome dans un terminal Linux
pour exécuter et inspecter MarketPulse
```

## 8. TD Linux historiques

### 8.1 TD1.1 - Fondamentaux Linux

Le TD1.1 couvre beaucoup plus que la navigation.

Il demande notamment :

- navigation dans le système de fichiers ;
- création de répertoires ;
- création de fichiers ;
- renommage ;
- copie ;
- suppression ;
- scripts shell ;
- permissions ;
- chmod ;
- accès root ;
- chown ;
- installation de packages ;
- arguments de fonctions / scripts.

On retrouve ainsi directement plusieurs notions du questionnaire diagnostique actuel :

```text
mkdir
cp
chmod
```

### 8.2 TD1.2 - Linux tools

Le TD1.2 couvre :

- informations système ;
- variables shell ;
- portée des scripts ;
- scheduling ;
- daemon ;
- hashing ;
- compression ;
- ACL.

Ce niveau dépasse largement ce qui est requis dans MarketPulse.

### 8.3 TD1.3 - Grep

Le TD1.3 couvre :

- grep ;
- awk ;
- pipes ;
- regex ;
- sed ;
- extraction sur données tabulaires ;
- extraction sur HTML téléchargé avec curl.

Il demande par exemple de chaîner :

```bash
ls
grep
awk
```

puis d'extraire du contenu depuis une page Wikipédia.

C'est une vraie initiation à la philosophie Unix :

```text
small tools
+
pipes
+
text processing
```

mais cette compétence n'est pas nécessaire pour faire fonctionner le fil rouge actuel.

### 8.4 TD1.4 - SSH / SCP

Le TD demande aux étudiants :

- de créer un compte chez un fournisseur cloud ;
- de saisir une carte bancaire ;
- de créer une VM ;
- de gérer une clé privée ;
- d'utiliser chmod 400 ;
- de se connecter en SSH ;
- de créer un script de connexion ;
- d'utiliser SCP ;
- d'automatiser l'envoi et la récupération de fichiers.

C'est professionnellement très intéressant.

Mais c'est aussi l'un des plus gros risques pédagogiques et logistiques de l'ancien dispositif.

Les points de friction potentiels sont :

```text
création de compte cloud
carte bancaire
quotas
régions
facturation
clé privée
permissions
réseau
SSH
OS différent
shell différent
suppression de ressources
```

La décision MarketPulse actuelle de placer :

```text
VPS
SSH
systemd
Docker
GitHub Actions
```

dans une piste avancée optionnelle est donc cohérente.

## 9. CM2 - Git local

Le CM Git local est conceptuellement profond.

Il couvre :

- définition d'un VCS ;
- histoire de Git ;
- configuration ;
- création de repository ;
- status ;
- add ;
- commit ;
- fichiers Git internes ;
- blobs ;
- hash cryptographique ;
- représentation en graphe ;
- tree ;
- commit objects ;
- HEAD ;
- branches ;
- diff ;
- staging area ;
- staging interactif ;
- navigation entre commits ;
- restore ;
- undo ;
- ignore ;
- aliases ;
- plumbing vs porcelain.

Le message pédagogique est clair :

```text
ne pas seulement mémoriser les commandes
comprendre le modèle interne de Git
```

C'est une vraie force de l'ancien cours.

## 10. TD2 - Git local

Le TD2 confirme cette profondeur.

### Partie raisonnablement alignée avec MarketPulse

Les premières sections couvrent :

```text
git init
git status
git add
git commit
git log
.gitignore
git diff
```

Ces notions sont toujours très pertinentes.

### Partie beaucoup plus avancée

Le TD va ensuite vers :

- restore ;
- checkout historique ;
- revert ;
- reset --hard ;
- aliases ;
- SHA-1 ;
- git hash-object ;
- structure interne des blobs ;
- compression zlib ;
- git cat-file ;
- manipulation directe de .git/objects.

Des durées sont explicitement prévues dans la source :

```text
Hashing       30 à 45 min
Compressing   30 à 45 min
```

À elles seules, ces deux sections peuvent consommer environ une séance complète.

### Analyse

Ces exercices sont excellents pour un cours spécialisé Git.

Ils ne sont pas réalistes dans le CORE d'un module où Git partage les 18 heures avec :

```text
Linux
Python
data
Yahoo
Bloomberg
Dash
```

La refonte MarketPulse qui conserve :

```text
status
diff
add
commit
log
show
```

puis déplace rapidement la pratique vers le projet réel est donc plus adaptée au volume horaire.

## 11. CM3 - Git remote

Le CM distant couvre :

- repository local vs distant ;
- clone ;
- pull ;
- push ;
- SSH vs HTTPS ;
- plateformes Git ;
- tags ;
- branches ;
- merge ;
- rebase ;
- fetch ;
- workflows ;
- Merge Requests / Pull Requests ;
- Gitflow ;
- nettoyage d'historique.

La matière est riche et professionnellement solide.

Elle est néanmoins plus large que le besoin MarketPulse.

## 12. TD3 - Branches et collaboration

Le TD3 est particulièrement intéressant pour comparer les deux approches.

Il prévoit des équipes de 3 à 4 étudiants.

Les sections incluent :

| Section | Durée indiquée dans la source |
|---|---:|
| Clone repository | 5 à 10 min |
| Push files | 10 à 20 min |
| Merge simple | 10 à 20 min |
| Resolve merge conflicts | 20 à 40 min |
| Update local branch from master | 10 à 20 min |
| Delete a branch | 5 à 10 min |
| Interactive rebase | 20 à 30 min |
| Pull Request | 20 à 30 min |

En prenant les minima :

```text
5 + 10 + 10 + 20 + 10 + 5 + 20 + 20
=
100 minutes
```

En prenant les maxima :

```text
10 + 20 + 20 + 40 + 20 + 10 + 30 + 30
=
180 minutes
```

Ce TD contient donc objectivement entre environ :

```text
1h40
et
3h
```

de matière annoncée.

C'est un indicateur très fort du problème de densité.

### Différence avec le nouveau parcours

MarketPulse répartit désormais ces notions sur plusieurs TD :

```text
TD03 Git local
TD04 branches + merge
TD05 remote branch + PR
TD06 code review
```

Ce découpage est beaucoup plus réaliste pour des étudiants hétérogènes.

## 13. Gestion des conflits

L'ancien TD crée volontairement un vrai conflit.

Chaque membre modifie les mêmes lignes du README afin de provoquer une collision.

C'est un exercice utile.

Mais il consomme :

```text
20 à 40 minutes
```

selon le document.

La refonte actuelle a choisi :

```text
comprendre le conflit
=
CORE

fabriquer et résoudre un conflit complet
=
OPTIONAL / démonstration
```

Cette décision est cohérente avec le temps disponible.

## 14. Rebase interactif

L'ancien TD demande :

- huit commits artificiels ;
- réécriture d'historique ;
- interactive rebase ;
- squash ;
- validation du graphe ;
- push de la branche.

C'est une compétence intéressante pour des développeurs plus avancés.

Elle n'est pas nécessaire pour comprendre :

```text
branch
PR
review
merge
```

Le fait de l'avoir retirée du CORE actuel réduit fortement le risque de surcharge et de confusion.

## 15. Bloomberg dans l'ancien cours

Le CM Bloomberg est riche.

Il présente :

- rôle de Bloomberg ;
- business model ;
- Terminal ;
- navigation ;
- fonctions ;
- Excel Add-In ;
- API ;
- Request / Response ;
- Subscription ;
- Publishing ;
- BDP ;
- BDS ;
- BDH ;
- FLDS ;
- services de market data ;
- market bars ;
- VWAP ;
- B-PIPE ;
- xbbg ;
- blpapi.

Le CM montre un exemple :

```python
from xbbg import blp
```

avec récupération historique.

Il compare également :

```text
xbbg
vs
blpapi
```

## 16. TD Bloomberg historique

Le fichier :

```text
src/TD4_Bloomberg.tex
```

est daté dans sa source :

```text
2024-2025-S2
```

alors que les commits du repository observés sont principalement datés de septembre à novembre 2025.

Cela suggère qu'au moins une partie du support a été reprise ou maintenue sur plusieurs périodes académiques.

Le TD demande :

### Exercice 1

- Bloomberg Terminal ouvert ;
- API access ;
- environnement Python ;
- installation de `blpapi` ;
- connexion ;
- première requête historique ;
- plusieurs tickers ;
- OHLC ;
- volume ;
- matplotlib.

La source écrit :

```text
APPL US
```

dans l'instruction du premier appel.

Le document ne précise pas davantage si cette valeur est volontaire ou s'il s'agit d'une erreur de saisie.

### Exercice 2

ReferenceDataRequest sur :

```text
TSLA US Equity
EURUSD Curncy
IBM US Equity
```

avec :

```text
NAME
SECURITY_TYPE
CRNCY
EXCH_CODE
```

### Exercice 3

IntradayBarRequest sur :

```text
META US Equity
```

avec intervalle :

```text
5 minutes
```

et :

```text
open
high
low
close
volume
```

### Risque principal

Le TD dépend fortement d'un environnement Bloomberg opérationnel.

Sans environnement valide :

```text
pas de connexion
=
pas de progression
```

Le nouveau modèle :

```text
LIVE
ou
APPROVED_SAMPLE
```

avec distinction explicite entre les deux modes est donc une amélioration importante de résilience pédagogique.

## 17. Ancien projet final

Le fichier :

```text
src/Project.tex
```

est extrêmement ambitieux.

Le scénario demande une plateforme de type quant / asset management capable de :

- récupérer des données dynamiques ;
- afficher des valeurs en temps réel ;
- rafraîchir toutes les 5 minutes ;
- générer des rapports quotidiens ;
- utiliser cron ;
- fonctionner 24/7 ;
- être déployée sur Linux ;
- fournir un dashboard interactif ;
- implémenter du backtesting ;
- faire de l'analyse univariée ;
- faire de l'analyse multi-actifs ;
- calculer max drawdown ;
- calculer Sharpe ratio ;
- faire de la simulation de portefeuille ;
- afficher des corrélations ;
- gérer des poids ;
- proposer du rebalancing ;
- utiliser Streamlit ou équivalent ;
- éventuellement faire du ML ;
- éventuellement utiliser Bloomberg.

Les équipes sont de deux étudiants avec séparation de rôles :

```text
Quant A
=
Single Asset Analysis

Quant B
=
Multi-Asset Portfolio
```

### Analyse

Pris isolément, c'est un projet très intéressant.

Mais il exige simultanément :

```text
software engineering
+
Linux
+
cloud
+
Git collaboration
+
data acquisition
+
web application
+
scheduling
+
finance quantitative
+
portfolio analytics
+
robustesse
```

Pour un module où Git et Linux doivent aussi être enseignés depuis zéro, le risque de surcharge est élevé.

## 18. Évaluation historique

Le README historique indique :

```text
1/3 project
1/3 final semester exam
1/3 continuous assessment through graded tutorials
```

Le cursus actuel de référence utilise une répartition différente :

```text
Exam
35%

Lab work / Projects
35%

Final project
30%
```

Il ne faut donc pas réutiliser l'ancienne pondération comme référence actuelle.

## 19. Build system et maintenance des supports

Le repository historique utilise LaTeX.

Les scripts :

```text
src/build.sh
src/build_all.sh
```

font notamment appel à :

```bash
pdflatex -shell-escape
```

et construisent des variantes de TD avec réponses.

Ce système permet de produire des PDF de qualité et des versions corrigées.

Mais il introduit aussi une chaîne technique supplémentaire :

```text
LaTeX
+
minted
+
Pygments
+
shell escape
+
packages locaux
```

Le nouveau repository Markdown est plus simple à :

- lire ;
- corriger ;
- versionner ;
- revoir en Pull Request ;
- mettre à jour rapidement ;
- consulter directement depuis GitHub.

## 20. Forces de l'ancien dispositif

### 20.1 Profondeur technique

L'ancien cours ne se limite pas à des recettes.

Il essaie d'expliquer les mécanismes.

Exemple Git :

```text
working tree
staging
objects
hash
tree
commit
HEAD
branch
```

### 20.2 Culture professionnelle

Le cours relie les outils à :

- finance ;
- infrastructure ;
- serveurs ;
- collaboration ;
- Bloomberg ;
- data ;
- cloud.

### 20.3 Unix réel

Les étudiants voient réellement :

```text
grep
awk
sed
pipes
scripts
SSH
permissions
```

### 20.4 Git réel

Les étudiants rencontrent :

```text
branch
merge
conflict
remote
PR
rebase
```

### 20.5 Bloomberg non superficiel

Le contenu distingue :

```text
Terminal
Excel
Request/Response
Subscription
BDP
BDS
BDH
B-PIPE
xbbg
blpapi
```

### 20.6 Projet professionnel

Le projet tente d'imiter une vraie chaîne :

```text
data
+
analytics
+
dashboard
+
deployment
+
collaboration
```

Ce principe est excellent et doit être conservé.

## 21. Limites principales

### 21.1 Périmètre trop large

Le même cours veut couvrir :

```text
Linux administration
shell scripting
Git internals
Git workflows
cloud
SSH
Bloomberg
Python
web apps
quant finance
deployment
```

Le coût cognitif est très élevé.

### 21.2 Beaucoup de dépendances environnementales

Plusieurs exercices supposent :

- Linux local ;
- VM ;
- accès cloud ;
- carte bancaire ;
- clés SSH ;
- droits d'installation ;
- Bloomberg Terminal ;
- Bloomberg API ;
- packages système.

Chaque prérequis multiplie les risques de blocage.

### 21.3 TD Git trop longs

Les durées écrites dans la source montrent elles-mêmes que certaines séances dépassent largement 90 minutes.

### 21.4 Git internals trop tôt

Hashing, zlib et manipulation de `.git/objects` sont pédagogiquement intéressants.

Ils arrivent cependant avant que tous les étudiants aient nécessairement stabilisé :

```text
status
add
commit
diff
branch
```

### 21.5 Rebase trop tôt

Le rebase interactif est une compétence avancée.

Il peut détourner l'attention de la collaboration de base.

### 21.6 Cloud obligatoire fragile

Demander une carte bancaire pour un TD commun crée une contrainte non technique importante.

### 21.7 Bloomberg sans fallback explicite

L'ancienne architecture suppose davantage que l'environnement Bloomberg fonctionnera.

Le dispositif actuel est plus robuste grâce au mode `APPROVED_SAMPLE`.

### 21.8 Projet final très dense

Le projet mélange apprentissage des outils et concepts quantitatifs avancés.

Cela rend plus difficile l'identification de la compétence réellement évaluée.

## 22. Comparaison ancien dispositif vs MarketPulse

| Dimension | Repository historique | MarketPulse actuel |
|---|---|---|
| Structure | CM + TD spécialisés + projet | 12 TD autour d'un fil rouge |
| Linux | Large initiation Linux | Minimum utile au projet |
| Git local | Très profond jusqu'aux internals | Modèle mental + workflow quotidien |
| Git remote | Branches, conflicts, rebase, Gitflow | Branch, PR, review, merge |
| Python | Support du projet, peu centralisé dans les TD historiques | Progression directement dans le fil rouge |
| Data locale | Pas de contrat unique dominant | CSV / JSON starter explicite |
| Remote public data | Projet ouvert à diverses APIs | Yahoo Finance étape pédagogique |
| Bloomberg | Direct API et intraday | Mapping + provider + LIVE / APPROVED_SAMPLE |
| Dashboard | Streamlit ou équivalent dans projet | Dash explicitement cadré |
| Finance | Backtest, Sharpe, portfolio | Return, Base 100, relative performance |
| Deployment | VM Linux 24/7 | Optionnel |
| SSH | TD dédié | Optionnel avancé |
| Docker | Présent en contexte | Hors CORE |
| CI/CD | Présent en contexte | Hors CORE |
| ML | Bonus projet | Hors CORE |
| Reproducibilité | Via infra / projet | Contrat de release TD12 |
| Évaluation pratique | TD + projet | Checkpoints A / B / C |
| Traces individuelles | Commit history implicite | Evidence contract explicite |

## 23. Ce que MarketPulse améliore

### 23.1 Un fil rouge unique

L'ancien cours enchaîne plusieurs exercices spécialisés.

MarketPulse conserve le même objet métier pendant toute la séquence.

```text
MarketPulse
TD01
  |
TD02
  |
TD03
  |
...
  |
TD12
```

Cela réduit les changements de contexte.

### 23.2 Progression par besoin

Chaque nouveau concept doit répondre à une exigence.

Exemple :

```text
need collaboration
-> branch + PR

need remote market data
-> Yahoo provider

need professional provider
-> Bloomberg mapping + provider

need visual interface
-> Dash
```

### 23.3 CORE / OPTIONAL

L'ancien contenu est riche mais distingue moins clairement :

```text
must know
nice to know
advanced
```

MarketPulse formalise cette séparation.

### 23.4 Résilience

Le mode Bloomberg :

```text
LIVE
or
APPROVED_SAMPLE
```

évite qu'une dépendance externe bloque tout le TD.

### 23.5 Charge contrôlée

Chaque TD vise :

```text
environ 80 min CORE
+
10 min buffer
```

### 23.6 Évaluation observable

Le modèle :

```text
artefact
+
Git trace
+
screenshots
+
execution
+
explanation
```

rend l'évaluation plus explicite.

## 24. Ce que l'ancien repository fait mieux ou plus profondément

Il ne faut pas conclure que le nouveau dispositif est "meilleur partout".

L'ancien repository est supérieur sur plusieurs dimensions de profondeur.

### Linux

Il donne une vraie culture :

```text
permissions
shell
pipes
regex
SSH
system environment
```

### Git internals

Il explique réellement pourquoi Git fonctionne.

### Git avancé

Il fait pratiquer :

```text
rebase
conflict resolution
history cleanup
```

### Bloomberg

Il couvre plus largement l'écosystème Bloomberg.

### Infrastructure

Il confronte les étudiants à de vraies contraintes serveur.

Ces contenus peuvent devenir une excellente banque de ressources avancées.

## 25. Contenus à réutiliser

### Priorité haute

À réutiliser sous forme adaptée :

```text
Git mental model
working tree / staging / commit
branch graphs
PR concepts
merge conflict explanation
Bloomberg BDP / BDS / BDH overview
Bloomberg xbbg vs blpapi overview
Linux CLI culture
Unix philosophy
SSH concept
```

### Priorité moyenne

À proposer comme OPTIONAL :

```text
chmod
PATH
environment variables
pipes
awk
sed
regex
SSH
SCP
Git aliases
Git restore / revert
interactive rebase
Bloomberg reference requests
intraday bars
```

### Ressources avancées

À conserver en lecture ou atelier bonus :

```text
Git plumbing
hash-object
zlib internals
ACL
cron
cloud VM
system administration
portfolio simulation
Sharpe
max drawdown
ML bonus
```

## 26. Contenus à ne pas remettre dans le CORE

Les éléments suivants ne devraient pas redevenir obligatoires dans les 18 heures communes :

```text
cloud account creation
credit card requirement
SSH deployment
SCP automation
ACL
cron
system daemons
Git object internals
zlib exercise
interactive rebase
Gitflow
intraday Bloomberg
multi-asset portfolio
Sharpe ratio
max drawdown
real-time 5-minute refresh
24/7 hosting
machine learning
Docker
Kubernetes
CI/CD
```

Ils peuvent rester utiles en extension.

## 27. Lien avec le questionnaire diagnostique

La découverte du repository historique permet de mieux comprendre la forme du questionnaire diagnostique actuel.

Plusieurs questions qui semblaient très avancées correspondent directement à l'ancien périmètre.

### Linux

Le questionnaire demande :

```text
mkdir
cp
grep + pipe
redirection
chmod
stderr
environment variable
&&
```

Or l'ancien cours couvrait précisément :

```text
filesystem operations
permissions
shell variables
scripts
pipes
grep / awk / sed
```

### Git

Le questionnaire demande :

```text
git fetch
fork vs branch
staging nuance
merge conflict
.gitignore
```

L'ancien cours allait même au-delà avec :

```text
rebase
Git internals
hashing
compression
```

### Python / Bloomberg / Dash

Le questionnaire demande :

```text
virtual environment
missing-data policy
Bloomberg data-access layer
Dash callback
```

L'ancien projet et le TD Bloomberg utilisaient :

```text
Python environment
Bloomberg API
web application
interactive controls
```

### Interprétation

Cela suggère que le questionnaire a probablement été conçu avec une vision du module plus proche de l'ancien périmètre technique que du CORE MarketPulse actuel.

Ce n'est pas un problème si le questionnaire reste diagnostique.

Mais cela renforce la règle :

```text
questionnaire diagnostic
!=
liste des prérequis actuels
```

Les questions avancées doivent rester des questions de plafond.

## 28. Lien avec le nouveau découpage des TD

On peut presque voir la refonte MarketPulse comme une décomposition contrôlée de certaines grandes masses de l'ancien cours.

### Ancien bloc Git

```text
Git local
+
branches
+
remote
+
conflicts
+
rebase
+
PR
```

devient :

```text
TD03 Git local
TD04 Branches + Merge
TD05 Remote Branch + PR
TD06 Code Review
```

### Ancien bloc Bloomberg

```text
Terminal
+
blpapi
+
requests
+
intraday
```

devient :

```text
TD09 Bloomberg Introduction
TD10 Bloomberg Provider
```

avec fallback explicite.

### Ancien projet final

```text
open data
+
analytics
+
web app
+
deployment
+
finance
```

devient une progression guidée :

```text
CSV
Yahoo
Bloomberg
analytics
snapshot
Dash
release
```

## 29. Recommandation documentaire

Le repository historique ne doit pas être copié dans MarketPulse.

Il devrait être traité comme :

```text
legacy teaching reference
```

Une future structure possible dans le repository courant pourrait être :

```text
docs/legacy/
├── 01_PREVIOUS_COURSE_REPOSITORY_ANALYSIS.md
├── 02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
└── 03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
```

Le présent document constitue le premier élément de cette série.

## 30. Recommandation pédagogique

Le principe recommandé est :

```text
ancien cours
=
banque de profondeur

MarketPulse
=
parcours commun maîtrisable

diagnostic
=
outil de calibration

optional track
=
lieu de réutilisation des contenus avancés
```

Cela permet de ne perdre ni :

```text
la richesse historique
```

ni :

```text
la maîtrise de la charge pédagogique
```

## 31. Conclusion

Le repository historique montre un enseignement techniquement ambitieux et riche.

Il possède une vraie valeur sur :

- Linux ;
- philosophie Unix ;
- Git internals ;
- Git collaboration ;
- Bloomberg ;
- infrastructure ;
- projet professionnel.

Son principal défaut n'est pas la qualité du contenu.

Le problème est la quantité de concepts que les étudiants doivent absorber dans un même module.

Le nouveau parcours MarketPulse ne doit donc pas chercher à remplacer cette richesse par un cursus superficiel.

Il doit faire autre chose :

```text
sélectionner
ordonner
contextualiser
timeboxer
rendre observable
rendre reproductible
```

Le meilleur usage de l'ancien repository est donc :

```text
reference
+
source d'extensions
+
source de supports avancés
+
source de contexte
```

et non :

```text
template à reproduire intégralement
```

La prochaine étape logique est de construire une cartographie explicite :

```text
contenu historique
        |
        +-> déjà couvert par MarketPulse
        |
        +-> à conserver en OPTIONAL
        |
        +-> à conserver comme ressource enseignant
        |
        +-> à abandonner
```

afin de tirer parti de l'ancien matériel sans réintroduire sa surcharge.

Cette cartographie est maintenant documentée dans :

```text
docs/legacy/02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
```
