#!/usr/bin/env python3
"""
Script para ajustar título da página de demo e evitar cortes
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Ajustar título para evitar cortes
replacements = [
    # Adicionar mais padding no container
    (r'<div className="container mx-auto px-4">', 
     '<div className="container mx-auto px-4 sm:px-6">'),
    
    # Adicionar padding no header e ajustar tamanhos responsivos
    (r'className="text-center mb-12"', 
     'className="text-center mb-12 px-4"'),
    
    # Ajustar tamanhos do título com breakpoints mais suaves
    (r'<h1 className="text-4xl md:text-6xl font-bold text-neutral-dark mb-4">', 
     '<h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-neutral-dark mb-4 break-words">'),
    
    # Ajustar subtítulo também
    (r'<p className="text-xl text-neutral-dark/70 max-w-2xl mx-auto">', 
     '<p className="text-lg sm:text-xl text-neutral-dark/70 max-w-2xl mx-auto">'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Título da página de demo ajustado!")
print("📝 Tamanhos responsivos e break-words adicionados")
print("🚀 Execute: npm run dev")
