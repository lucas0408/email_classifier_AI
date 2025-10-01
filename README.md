# 📧 Email Classifier AI

Aplicação web que **classifica emails como produtivos ou improdutivos** e gera uma **resposta automática** utilizando inteligência artificial.

O sistema foi desenvolvido com **Flask (Python)** e integrado ao modelo **Gemini (Google Generative AI)**.

👉 **Deploy na Vercel:** [Acesse aqui](https://email-classifier-ecru.vercel.app/)

---

## 🚀 Funcionalidades

- Upload de arquivos **.pdf** ou **.txt**
- Inserção de texto diretamente na interface
- Classificação automática do email em:
  - **Produtivo** (assuntos de trabalho, reuniões, projetos etc.)
  - **Improdutivo** (spam, propagandas, newsletters, correntes etc.)
- Geração de resposta automática e profissional:
  - Até **3 parágrafos** para emails produtivos
  - Resposta curta e educada para emails improdutivos
- Copiar resposta gerada com **1 clique**

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** [Flask](https://flask.palletsprojects.com/)
- **IA:** [Google Generative AI (Gemini 2.0 Flash)](https://ai.google.dev/)
- **Leitura de Arquivos:** PyPDF2
- **Frontend:** HTML + CSS + JavaScript (renderizado com Jinja2)
- **Deploy:** [Vercel](https://vercel.com/)

---

## 📂 Estrutura do Projeto

```
📦 email-classifier-ai
┣ 📂 static/
┃ ┗ 📂 css/              # Arquivos de estilo
┣ 📂 templates/          # Páginas HTML
┣ 📄 index.py              # Backend Flask
┣ 📄 requirements.txt    # Dependências do projeto
┗ 📄 README.md
```

---

## ⚙️ Como Rodar Localmente

### 1. Clone o repositório:

```bash
git clone https://github.com/lucas0408/email-classifier-ai.git
cd email-classifier-ai
```

### 2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3. Configure sua chave da API do Google Generative AI:

```bash
export GEMINI_API_KEY="sua_chave_aqui"   # Linux/Mac
set GEMINI_API_KEY="sua_chave_aqui"      # Windows
```

### 4. Rode a aplicação:

```bash
python app.py
```

### 5. Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 📸 Demonstração

🔹 **Tela inicial:** Upload ou inserção de texto  
🔹 **Resultado:** Classificação + resposta gerada automaticamente

*(adicione prints depois que subir no GitHub para ficar mais atrativo)*

---

## 👨‍💻 Autor

Desenvolvido por **Lucas Gabriel** 🚀

- [LinkedIn](https://linkedin.com/in/seu-perfil)
- [GitHub](https://github.com/lucas0408)

---
