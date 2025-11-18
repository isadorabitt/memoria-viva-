#!/usr/bin/env python3
"""
Script para ajustar CircleFeedScreen: manter tamanhos de elementos iguais aos outros,
mas aumentar apenas os tamanhos de texto
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Reverter tamanhos de elementos para igual aos outros mockups
# Mas manter textos maiores
replacements = [
    # Reverter espaçamentos e padding
    (r'className="space-y-5"', 'className="space-y-4"'),
    (r'className="bg-ipe text-white rounded-xl p-6">', 
     'className="bg-ipe text-white rounded-xl p-4">'),
    (r'className="bg-white rounded-xl p-6 shadow-sm">', 
     'className="bg-white rounded-xl p-4 shadow-sm">'),
    (r'className="flex items-start gap-4 mb-4">', 
     'className="flex items-start gap-3 mb-3">'),
    
    # Reverter tamanhos de avatares e emojis
    (r'className="w-16 h-16 bg-cerrado rounded-full flex items-center justify-center text-3xl">', 
     'className="w-10 h-10 bg-cerrado rounded-full flex items-center justify-center text-lg">'),
    (r'className="w-16 h-16 bg-wisdom rounded-full flex items-center justify-center text-3xl">', 
     'className="w-10 h-10 bg-wisdom rounded-full flex items-center justify-center text-lg">'),
    (r'<span className="text-4xl">🍲</span>', 
     '<span className="text-2xl">🍲</span>'),
    
    # Reverter título do header
    (r'<h3 className="font-bold text-2xl flex items-center gap-3">', 
     '<h3 className="font-bold text-xl flex items-center gap-2">'),
    
    # Manter textos maiores mas ajustar espaçamentos
    (r'<h4 className="font-bold text-neutral-dark text-xl">Dona Ana</h4>', 
     '<h4 className="font-bold text-neutral-dark text-lg">Dona Ana</h4>'),
    (r'<h4 className="font-bold text-neutral-dark text-xl">Seu João</h4>', 
     '<h4 className="font-bold text-neutral-dark text-lg">Seu João</h4>'),
    (r'<p className="text-xl text-neutral-dark/80 mb-4 leading-relaxed">', 
     '<p className="text-lg text-neutral-dark/80 mb-3 leading-relaxed">'),
    (r'className="flex gap-3">', 
     'className="flex gap-2">'),
    (r'className="flex items-center gap-2 text-ipe text-lg font-medium">', 
     'className="flex items-center gap-1 text-ipe text-base font-medium">'),
    (r'className="flex items-center gap-2 text-neutral-dark/60 text-lg font-medium">', 
     'className="flex items-center gap-1 text-neutral-dark/60 text-base font-medium">'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ CircleFeedScreen ajustado!")
print("📏 Elementos mantidos no mesmo tamanho dos outros mockups")
print("📝 Apenas textos aumentados para melhor leitura")
print("🚀 Execute: npm run dev")
