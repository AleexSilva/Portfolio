# 🌐 Portfolio Website

This project is a personal portfolio website showcasing my projects, skills, and experiences. Built with Python and Streamlit, it offers an interactive and responsive interface for visitors to explore my work.  
🔗 [Visit the Portfolio](https://alex-silva-portfolio.streamlit.app/)

---

## 📑 Table of Contents

- [📂 Project Structure](#-project-structure)
- [📦 Required Libraries](#-required-libraries)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [📄 Files](#-files)

---

## 📂 Project Structure

```plaintext
.
├── README.md
├── app.py
├── environment.yml
└── test
    └── test_connection.py
```

---

## 📦 Required Libraries

The project relies on the libraries specified in the `environment.yml` file.

---

## ⚙️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AleexSilva/Portfolio.git
   cd Portfolio
   ```

2. **Set Up the Environment**:
   - If using Conda:
     ```bash
     conda env create -f environment.yml
     conda activate portfolio-env
     ```
   - If using pip, manually install the packages listed in `environment.yml`.

---

## 🚀 Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Portfolio**:
   Open the provided local URL in your web browser to view the portfolio.

---

## 📄 Files

- `app.py`: Main application script that initializes and runs the Streamlit app.
- `environment.yml`: Specifies the dependencies and environment configuration for the project.
- `test/test_connection.py`: Contains tests to verify the application's connectivity and functionality.

---
