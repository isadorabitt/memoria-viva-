#!/usr/bin/env python3
"""
Script para ajustar títulos e evitar cortes
"""

import re

file_path = "src/app/sobre/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Ajustar títulos para evitar cortes
replacements = [
    # Reduzir tamanho dos nomes e adicionar break-words
    (r'<h3 className="text-xl font-bold text-neutral-dark mb-1">\s*Nicollas Rezende', 
     '<h3 className="text-lg font-bold text-neutral-dark mb-1 break-words">\n                  Nicollas Rezende'),
    (r'<h3 className="text-xl font-bold text-neutral-dark mb-1">\s*Isadora Bittencourt', 
     '<h3 className="text-lg font-bold text-neutral-dark mb-1 break-words px-2">\n                  Isadora Bittencourt'),
    (r'<h3 className="text-xl font-bold text-neutral-dark mb-1">\s*Eder Veloso', 
     '<h3 className="text-lg font-bold text-neutral-dark mb-1 break-words">\n                  Eder Veloso'),
    
    # Ajustar textos descritivos
    (r'<p className="text-neutral-dark/70">\s*Desenvolvedor Full Stack', 
     '<p className="text-neutral-dark/70 text-sm">\n                  Desenvolvedor Full Stack'),
    (r'<p className="text-neutral-dark/70">\s*Desenvolvedora', 
     '<p className="text-neutral-dark/70 text-sm">\n                  Desenvolvedora'),
    (r'<p className="text-neutral-dark/70">\s*Desenvolvedor</p>', 
     '<p className="text-neutral-dark/70 text-sm">\n                  Desenvolvedor</p>'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Títulos ajustados para evitar cortes!")
print("📝 Nomes com break-words e tamanhos ajustados")
print("🚀 Execute: npm run dev")
