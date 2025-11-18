#!/usr/bin/env python3
"""
Script para mover o título mais para baixo
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Ajustar espaçamento superior
replacements = [
    # Aumentar padding-top do main
    (r'className="min-h-screen bg-gradient-to-br from-neutral-light via-white to-cerrado-light/30 py-12 overflow-x-hidden">', 
     'className="min-h-screen bg-gradient-to-br from-neutral-light via-white to-cerrado-light/30 pt-20 pb-12 overflow-x-hidden">'),
    
    # Adicionar margin-top no header
    (r'className="text-center mb-12 px-2 sm:px-4 overflow-visible"', 
     'className="text-center mb-12 px-2 sm:px-4 overflow-visible mt-8"'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Título movido mais para baixo!")
print("📏 Padding-top aumentado para pt-20, margin-top adicionado")
print("🚀 Execute: npm run dev")
