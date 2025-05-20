# 🚀 Mini-projet API – Cloud & IA

Ce projet consiste à développer une mini API en **FastAPI**, déployée sur **Google Cloud Run** via **Docker**, avec :

- Lecture/écriture de données sur **Google Cloud Storage**
- Génération de blagues aléatoires via **Vertex AI (Gemini)**
- API exposée publiquement via des endpoints simples

## 🔧 Stack technique
- Python 3.x
- FastAPI
- Google Cloud Storage
- Vertex AI (Gemini)
- Docker
- GCP (Cloud Run)

## 📌 Endpoints prévus

| Endpoint       | Méthode | Description |
|----------------|---------|-------------|
| `/hello`       | GET     | Message de bienvenue |
| `/status`      | GET     | Date/heure actuelle |
| `/data`        | GET     | Lecture d’un fichier CSV/JSON depuis GCS |
| `/data`        | POST    | Ajout d’une ligne dans ce fichier |
| `/joke`        | GET     | Blague générée par un modèle IA (Gemini) |

## 🧑‍🤝‍🧑 Équipe

- **Antoine JIANG** – Structure du projet, Docker
- **Roman LACAZE** – Développement API FastAPI, gestion GCP
- **Baptiste DECANTER** – Intégration Vertex AI, README, doc finale

## 🚀 Lancement local

```bash
# Activer l’environnement
venv\Scripts\activate

# Lancer le serveur
uvicorn main:app --reload
