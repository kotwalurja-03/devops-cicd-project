# devops-cicd-project
# DevOps CI/CD Project – Automated Website Validation and Deployment

![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Deployment](https://img.shields.io/badge/Deployment-GitHub%20Pages-brightgreen)
![Status](https://img.shields.io/badge/Project-Beginner%20DevOps-orange)

## 📌 Project Overview

This project demonstrates the implementation of a basic DevOps Continuous Integration and Continuous Deployment (CI/CD) pipeline for a static website.

The website is developed using HTML, CSS, and JavaScript. Python is used to validate the website and run automated tests. GitHub Actions automates the validation and testing process whenever code is pushed to the `main` branch or a pull request is created.

If the required checks pass, the workflow deploys the website to GitHub Pages.

The main objective is to understand how DevOps practices automate software validation, testing, and deployment.

## 🎯 Project Objectives

- Understand the fundamentals of DevOps and CI/CD.
- Develop and maintain a static website.
- Use Git and GitHub for version control.
- Automate website validation using Python.
- Run automated unit tests.
- Configure GitHub Actions workflows.
- Deploy the website using GitHub Pages.
- Understand how automated checks help prevent faulty deployments.

## 🌐 Live Demo

**Live Website:** https://kotwalurja-03.github.io/devops-cicd-project/

**GitHub Repository:** https://github.com/kotwalurja-03/devops-cicd-project

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Website structure |
| CSS3 | Website styling and layout |
| JavaScript | Website interactivity and status display |
| Python 3 | Website validation and automated tests |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | CI/CD workflow automation |
| GitHub Pages | Website hosting |
| YAML | Workflow configuration |

## 🏗️ Project Architecture

The project follows this automated workflow:

```text
Developer
   |
   v
Modify Website Code
   |
   v
Commit and Push to GitHub
   |
   v
GitHub Actions Workflow
   |
   v
Checkout Repository
   |
   v
Set Up Python
   |
   v
Validate Website
   |
   v
Run Automated Tests
   |
   +-----------------------+
   |                       |
   v                       v
Checks Pass             Checks Fail
   |                       |
   v                       v
Deploy to Pages         Stop Pipeline
   |
   v
Live Website
```

## ⚙️ CI/CD Pipeline Explained

The GitHub Actions workflow is defined in:

`.github/workflows/static.yml`

### 1. Continuous Integration (CI)

The CI stage automatically checks the project whenever code is pushed to the `main` branch or a pull request targets `main`.

It performs the following tasks:

- Checks out the latest repository code.
- Sets up Python.
- Runs the website validation script.
- Runs the automated Python unit tests.

If validation or testing fails, the workflow stops before deployment.

### 2. Continuous Deployment (CD)

After the validation job succeeds, the deployment job:

- Configures GitHub Pages.
- Uploads the website files as a deployment artifact.
- Deploys the files to GitHub Pages.

The deployment job does not run for pull requests. It runs for qualifying non-pull-request events when the validation job passes.

## 🧪 Website Validation and Testing

The project uses a Python validation script and Python's built-in `unittest` framework.

### Website validation

File:

`scripts/validate_site.py`

This script checks required website files and elements to help detect missing components before deployment.

Run the validator locally:

```bash
python scripts/validate_site.py
```

### Automated tests

File:

`test/test_site.py`

The automated tests check:

- Whether required website files exist.
- Whether the HTML contains required elements and references.
- Whether the JavaScript contains the expected status-update logic.

Run the tests locally:

```bash
python -m unittest discover -s test -v
```

A successful test run displays `OK` at the end.

## 📁 Project Structure

```text
devops-cicd-project/
│
├── .github/
│   └── workflows/
│       └── static.yml
│
├── scripts/
│   └── validate_site.py
│
├── test/
│   └── test_site.py
│
├── index.html
├── styles.css
├── script.js
└── README.md
```

**Note:** The `test/__pycache__/` directory may be generated when Python runs the tests. It is not required in the repository.

## 💻 Run the Project Locally

### Prerequisites

Install the following tools:

- Git
- Python 3
- A web browser
- A code editor such as Visual Studio Code

### Step 1: Clone the repository

```bash
git clone https://github.com/kotwalurja-03/devops-cicd-project.git
```

### Step 2: Open the project folder

```bash
cd devops-cicd-project
```

### Step 3: Run website validation

```bash
python scripts/validate_site.py
```

### Step 4: Run automated tests

```bash
python -m unittest discover -s test -v
```

### Step 5: Open the website

Open `index.html` in your web browser to view the static website locally.

## 🔄 How to Trigger the CI/CD Pipeline

After making a change to the project, run:

```bash
git add .
git commit -m "Update website"
git push origin main
```

GitHub Actions automatically starts the workflow after the push.

To monitor it:

1. Open the GitHub repository.
2. Click the **Actions** tab.
3. Select the latest workflow run.
4. Check the validation, testing, and deployment jobs.

You can also open a pull request targeting `main` to run the validation and test jobs before merging.

## 🔐 Security and Best Practices

- Keep source code version-controlled with Git.
- Run automated tests before deployment.
- Use GitHub Actions permissions limited to the required operations.
- Do not commit passwords, API keys, access tokens, or other secrets.
- Keep dependencies and GitHub Actions up to date.
- Review failed workflow logs before changing deployment configuration.

## 📚 What I Learned

Through this project, I practised:

- Basic Git commands and GitHub repository management.
- Creating and maintaining GitHub Actions workflows.
- Writing Python validation scripts and unit tests.
- Automating checks after code changes.
- Understanding CI versus CD.
- Deploying a static website with GitHub Pages.
- Troubleshooting workflow syntax and test failures.

## 🚀 Future Improvements

Planned enhancements include:

- Containerizing the website using Docker.
- Adding HTML and CSS linting.
- Adding dependency and security scanning.
- Improving automated test coverage.
- Adding a pull-request review workflow.
- Documenting Docker-based local deployment.
- Exploring deployment to a cloud hosting platform.

These enhancements will be added as they are implemented.

## 👨‍💻 Author

**Urja Kotwal**

GitHub: https://github.com/kotwalurja-03

## 📄 License

This project is intended for learning and educational purposes. Add a `LICENSE` file if you want to distribute it under a specific open-source license.
