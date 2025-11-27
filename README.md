Minimal Interactive Python Web App (Flask)Project OverviewThis project is a minimal, Python-first web application designed to demonstrate the core principles of server-side routing, client-server communication (GET/POST requests), and HTML template rendering using the Flask micro-framework.The goal was to build a functional web app without relying on external frontend frameworks (like React) or dedicated CSS libraries (like Tailwind CSS).🚀 Getting StartedPrerequisitesPython 3.xpip (Python package installer)InstallationClone the Repository:git clone [https://github.com/LingKalmor/Gen-AI](https://github.com/LingKalmor/Gen-AI)
cd Gen-AI
Install Dependencies:pip install flask
File StructureThe project uses the standard Flask template structure:/Gen-AI
├── app.py          # The Flask server logic
├── README.md
├── DOCUMENTATION.md # Full project report and prompt journal
└── /templates      # Required folder for HTML files
    ├── index.html  # Input form (GET)
    └── result.html # Output page (POST)
Running the ApplicationEnsure you are in the root directory (Gen-AI).Run the Python script:python app.py
Open your web browser and navigate to the address shown in your terminal (typically https://www.google.com/search?q=http://127.0.0.1:5000/).Project Documentation and AnalysisFor a detailed report on the development process, AI usage, troubleshooting, and learning reflections, please see the DOCUMENTATION.md file in this repository.
