from flask import Flask, render_template, request
import re
import PyPDF2
import google.generativeai as genai
import io
import os
app = Flask(__name__)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI"))
model = genai.GenerativeModel('gemini-2.0-flash')  

def extract_text_from_file(file):
    filename = file.filename.lower()
    
    if filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    
    elif filename.endswith('.txt'):
        return file.read().decode("utf-8")
    
    else:
        raise ValueError("Formato não suportado. Use .txt ou .pdf")

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", text)
    words = text.split() 
    return " ".join(words)

def classify_email(text):
    text_preview = text[:100]  
    prompt = f"""Analise este email e classifique-o como PRODUTIVO ou IMPRODUTIVO.

    PRODUTIVO: Emails relacionados a trabalho, reuniões, projetos, tarefas, clientes, fornecedores, assuntos profissionais importantes.

    IMPRODUTIVO: Spam, propagandas, newsletters não solicitadas, correntes, emails irrelevantes para o trabalho.

    Email:
    {text_preview}

    Responda APENAS com uma palavra: PRODUTIVO ou IMPRODUTIVO"""
    try:
        response = model.generate_content(prompt)
        result = response.text.strip().upper()
        
        if "PRODUTIVO" in result and "IMPRODUTIVO" not in result:
            return "Produtivo"
        elif "IMPRODUTIVO" in result:
            return "Improdutivo"
    except Exception as e:
        return f"Erro ao classificar: {str(e)}"

def generate_response(category, text):
    text_preview = text[:500]
    
    if category == "Produtivo":
        prompt = f"""Escreva uma resposta (sem assunto) profissional e educada para este email. 
        Mantenha a resposta curta (máximo 3 parágrafos).
        
        Email recebido:
        {text_preview}
        
        Resposta:"""
    else:
        prompt = f"""Escreva uma resposta (sem assunto) educada este email IMPRODUTIVO de forma SIMPLES e profissional.
        Mantenha a resposta curta (máximo 1 parágrafo).
        
        Email recebido:
        {text_preview}
        
        Resposta:"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    text = ""
    error = None
    try:
        file = request.files.get("file")
        if file and file.filename:
            text = extract_text_from_file(file)

        if request.form.get("email_text"):
            text += request.form.get("email_text")

        if not text.strip():
            error = "Por favor, envie um arquivo ou insira texto."
            return render_template("index.html", error=error)

        processed_text = preprocess(text)
        category = classify_email(processed_text)
        response = generate_response(category, text)

        return render_template("index.html", category=category, response=response)
    
    except Exception as e:
        error = f"Erro ao processar: {str(e)}"
        return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
