import os
import fitz
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# pdf_path = "data/essay.pdf"  # To'g'ri essay
# pdf_path = "data/essay1.pdf"  # Strukturasi xato essay essay
pdf_path = "data/essay2.pdf"  # Xatolilari bor essay
txt_path = "data/structure.txt"  # Strukturaviy qoida

def read_pdf(file_path):
    """ PDF fayldan matnni o‘qib olish """
    text = ""
    try:
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text("text") + "\n"
        return text
    except Exception as e:
        return f"Xatolik yuz berdi: {str(e)}"

def read_txt(file_path):
    """ TXT fayldan strukturani o‘qib olish """
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "Xatolik: 'structure.txt' fayli topilmadi!"

essay_text = read_pdf(pdf_path)
structure_text = read_txt(txt_path)

if "Xatolik" in essay_text or "Xatolik" in structure_text:
    print("PDF yoki TXT faylni o‘qib bo‘lmadi!")
else:
    model = ChatOpenAI(model_name="gpt-4o")
    
    message = [
        {"role": 'system', "content": 'Siz professional tilshunos va grammatik tahlilchisiz.'},
        {"role": 'user', "content": f"""Quyidagi essayni grammatik jihatdan tahlil qiling, strukturasi to'g'riligini tekshiring va o'zbek tilida javob bering. Agar essayda  hech qanday grammatik xatolar bo'lmasa "Essay to'g'ri yozilgan" degan xabar chiqarish kerak.
        Essay: {essay_text}
    """},
    ]


    response = model.invoke(message)

    print(" Model javobi:\n", response.content)