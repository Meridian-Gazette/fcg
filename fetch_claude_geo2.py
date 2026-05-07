import anthropic
import os
from datetime import datetime

# Načtení API klíče z prostředí GitHub Actions
client = anthropic.Anthropic(api_key=os.environ["CLAUDE_API_KEY"])

# Tady definuj svůj prompt
MY_PROMPT = "Give me short (not more then 15 sentences) overview on politics - latest news. Only Europa and Russia region! (in English) "

response = client.messages.create(
    model="claude-haiku-4-5-20251001",  # Aktualizované ID modelu
    max_tokens=1024,
    messages=[{"role": "user", "content": MY_PROMPT}]
)

content = response.content[0].text
date_str = datetime.now().strftime("%Y-%m-%d")

# Vytvoření složky pro příspěvky, pokud neexistuje
os.makedirs("_posts", exist_ok=True)

# Uložení do souboru s hlavičkou pro web (Jekyll front matter)
filename = f"_posts/{date_str}-post.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"---\nlayout: post\ntitle: 'Zápis pro {date_str}'\ndate: {date_str}\n---\n\n")
    f.write(content)

print(f"Příspěvek {filename} byl úspěšně vytvořen.")
