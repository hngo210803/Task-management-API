# API REST Serverless - Gestion de tâches

API REST développée avec FastAPI permettant la gestion complète de tâches via les opérations CRUD. Les données sont stockées dans Amazon DynamoDB afin de bénéficier d'une architecture cloud scalable et serverless.

---

## Fonctionnalités

### CRUD

- Création de tâches
- Consultation de toutes les tâches
- Consultation d'une tâche par ID
- Mise à jour de tâches
- Suppression de tâches

---

## Architecture

```text
FastAPI
   ↓
boto3
   ↓
Amazon DynamoDB
```

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn
- Amazon DynamoDB
- boto3
- AWS CLI
- Pytest
- Docker
- GitHub Actions

---

## Structure du projet

```text
task-api/
├── .github/
│   └── workflows/
│       └── tests.yml
├── src/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── main.py
├── tests/
│   └── test_tasks.py
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Prérequis

- Python 3.14+
- AWS CLI
- Docker
- Un compte AWS

---

## Configuration AWS

### Configurer AWS CLI

```bash
aws configure
```

### Vérifier l'identité AWS

```bash
aws sts get-caller-identity
```

### Créer la table DynamoDB

```bash
aws dynamodb create-table \
  --table-name Tasks \
  --attribute-definitions AttributeName=task_id,AttributeType=S \
  --key-schema AttributeName=task_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

---

## Installation

### Créer un environnement virtuel

```bash
python -m venv .venv
```

### Activer l'environnement

```bash
source .venv/bin/activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Lancer le projet

```bash
uvicorn src.main:app --reload
```

---

## Documentation API

### Swagger UI

```text
http://localhost:8000/docs
```

---

## Tests

### Exécuter les tests

```bash
python -m pytest
```

### Tests implémentés

- Test de l'endpoint principal
- Test de création d'une tâche
- Test de consultation des tâches

---

## Docker

### Construire l'image

```bash
docker build -t task-api .
```

### Lancer le conteneur

```bash
docker run -p 8000:8000 task-api
```

### Accéder à Swagger

```text
http://localhost:8000/docs
```

---

## Intégration Continue (CI)

Le projet utilise GitHub Actions pour exécuter automatiquement les tests à chaque push et pull request.

```text
Push / Pull Request
         ↓
 GitHub Actions
         ↓
      Pytest
         ↓
    Pass / Fail
```

