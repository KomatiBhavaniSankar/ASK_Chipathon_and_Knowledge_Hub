
---

# Chipathon Knowledge Hub

Chipathon Knowledge Hub is a structured documentation platform designed to help participants understand, implement, and debug OpenROAD-based chip design flows. It provides guides, debugging playbooks, artifact explanations, and chatbot support for quick assistance.

---

## Live Site

https://komatibhavanisankar.github.io/Chitathon_Knowledge_Hub/

---

## Documentation Structure

The documentation is organized inside the `docs/` directory:

```text
docs/
│
├── index.md
│
├── getting-started/
│   ├── overview.md
│   ├── installation.md
│   ├── environment-setup.md
│   └── track-guide.md
│
├── openroad-fundamentals/
│   ├── flow-overview.md
│   ├── rtl-to-gds.md
│   ├── synthesis.md
│   ├── floorplanning.md
│   ├── placement.md
│   ├── routing.md
│   └── signoff.md
│
├── reference-flows/
│   ├── openroad-flow.md
│   ├── orfs.md
│   ├── openroad-mcp.md
│   └── templates.md
│
├── debugging-playbooks/
│   ├── overview.md
│   ├── timing-failures.md
│   ├── drc-errors.md
│   ├── routing-issues.md
│   ├── congestion.md
│   ├── power-issues.md
│   └── common-errors.md
│
├── artifact-map/
│   ├── overview.md
│   ├── logs.md
│   ├── reports.md
│   ├── def-files.md
│   ├── gds-files.md
│   └── metrics.md
│
├── submission/
│   ├── checklist.md
│   ├── required-files.md
│   └── validation.md
│
├── faq/
│   ├── general.md
│   ├── setup.md
│   ├── debugging.md
│   └── chipathon-issues.md
│
├── seen-during-chipathon/
│   ├── real-cases.md
│   └── mentor-answers.md
│
├── contributor-guide/
│   ├── how-to-contribute.md
│   ├── writing-style.md
│   └── adding-answers.md
│
└── chatbot/
    ├── how-it-works.md
    └── limitations.md
```

---

## How to Navigate

* **Start with Getting Started** if you are new
* **Explore OpenROAD Fundamentals** to understand the flow
* **Use Debugging Playbooks** to solve common issues
* **Refer to Artifact Map** for output files and reports
* **Check FAQ** for quick answers
* **Follow Submission guidelines** before final submission

---

## How to Run Locally

### 1. Fork the Repository
Fork the repository using GitHub.

### 2. Clone the Repository
```bash
git clone https://github.com/KomatiBhavaniSankar/Chitathon_Knowledge_Hub.git
cd Chitathon_Knowledge_Hub
```

### 3. Setup Requirements
Ensure the following are installed:
* Python 3.x
* pip

### 4. Create a Virtual Environment
```bash
python -m venv venv
```
**Activate the environment:**

* **Windows (PowerShell):** `.\venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

### 5. Install Dependencies
```bash
pip install mkdocs-material
```

### 6. Run the Documentation
```bash
mkdocs serve
```
Open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Deployment

The project uses GitHub Actions to automatically deploy the site to GitHub Pages.

### Continuous Deployment
* Every commit pushed to the `main` branch is automatically built and deployed.
* The latest changes are reflected on the live GitHub Pages website automatically.

### Deployment Process
1.  Push changes to the `main` branch.
2.  GitHub Actions workflow runs automatically.
3.  MkDocs builds the static site.
4.  The site is deployed to the `gh-pages` branch.
5.  GitHub Pages serves the updated version.

---

## How to Contribute

Contributions are welcome.

### Steps to Contribute
1.  Fork the repository.
2.  Clone your fork.
3.  Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
4.  Make changes.
5.  Commit changes:
    ```bash
    git commit -m "Add new documentation"
    ```
6.  Push to your fork:
    ```bash
    git push origin feature/your-feature-name
    ```
7.  Open a Pull Request.

### Contribution Guidelines
* Follow the structure inside the `docs/` directory.
* Use clear and concise language.
* Add examples where necessary.
* Maintain consistent formatting.
* Avoid duplicate content.

---

## Chatbot

The Knowledge Hub includes a chatbot for assisting users with documentation queries. 

Refer to: `docs/chatbot/how-it-works.md`

---

## License

This project is open-source and available under the MIT License.

---

## Support

If you find this project useful:
* **Star** the repository
* **Fork** and contribute
* **Share** with others

---

**Built for Chipathon participants.**

---
