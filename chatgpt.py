import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 📁 Strukturaviy qoida fayli
txt_path = "data/structure.txt"

def read_txt(file_path):
    """ TXT fayldan strukturani o‘qib olish """
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "Xatolik: 'structure.txt' fayli topilmadi!"

# 📜 Strukturani o‘qish
structure_text = read_txt(txt_path)

# ✅ Essayni o‘zgaruvchidan olish
text_essay = """
Problem & Solution

Today, there is ongoing demand for tree products and cutting down trees has become a huge
problem in some parts of the world. The problem of deforestation can lead to several severe issues in
our life. However, we still have practical solutions to combat these problems.

Human activities like defarestation can bring about many negative effects like habitat destruction. In
other words, millions of trees are cut every year in the world, which can disrupt ecosystems. As a
result, millions of animals can suffer from hunger and water shortages, which can lead them to go
extinct. Also, trees can help us combat climate change. They have a vital function to absorb significant
amount of CO2. If these human activities continue, global warming can be accelerated, resulting in
melting ice caps in some parts of the world. Another problem can be that many communities are
dependent on forests for their income from farming or eco-tourism. A good local example can be
Zomin, which is highly forested. Thausands of peoples make money by tourism. Cutting down trees in
these places can lead people into poverty and economic problems.

One way to reduce deforestation is by making stricter laws. If people or companies cut down trees
illegally, they should get strong punishments. This can stop illegal logging and help protect forests.
Another good solution is planting more trees. For example, China has been planting billions of trees
since the 1980s to bring back forests and fight climate change. This helps nature recover and
improves the environment. Also, teaching people about deforestation is important. Schools and
programs can show people how to use less wood and paper. If people waste less, fewer trees will be
cut down.

In conclusion, cutting down too many trees causes big problems for nature, the climate, and people's
live. But we can fix this by making strict rules, planting more trees, and educating people about the
environment. If we act now, we can save forests and help the planet.
"""

if "Xatolik" in structure_text:
    print("❌ Strukturaviy qoida faylini o‘qib bo‘lmadi!")
else:
    model = ChatOpenAI(model_name="gpt-4o")

    message = [
        {"role": 'system', "content": 'Siz professional tilshunos va grammatik tahlilchisiz.'},
        {"role": 'user', "content": f"""Quyidagi essayni grammatik jihatdan tahlil qiling, strukturasi to'g'riligini tekshiring va o'zbek tilida javob bering. Agar essayda  hech qanday grammatik xatolar bo'lmasa "Essay to'g'ri yozilgan" degan xabar chiqarish kerak.
        Essay: {text_essay}
    """},
    ]


    response = model.invoke(message)

    print("\n🔹 Model javobi:\n", response.content)