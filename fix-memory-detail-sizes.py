#!/usr/bin/env python3
"""
Script para ajustar MemoryDetailScreen: aumentar apenas textos, manter elementos iguais
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Aumentar apenas textos, manter elementos iguais
replacements = [
    # Categoria
    (r'<h4 className="font-bold text-neutral-dark">Infância</h4>', 
     '<h4 className="font-bold text-lg text-neutral-dark">Infância</h4>'),
    
    # Data
    (r'<p className="text-xs text-neutral-dark/60">Gravado em', 
     '<p className="text-sm text-neutral-dark/60">Gravado em'),
    
    # Título da memória
    (r'<h3 className="font-bold text-neutral-dark mb-2">\s*Festas', 
     '<h3 className="font-bold text-2xl text-neutral-dark mb-2">\n          Festas'),
    
    # Descrição da memória
    (r'<p className="text-sm text-neutral-dark/80 leading-relaxed mb-4">', 
     '<p className="text-lg text-neutral-dark/80 leading-relaxed mb-4">'),
    
    # Botões
    (r'className="flex-1 bg-ipe/10 text-ipe py-2 rounded-lg text-sm font-medium flex items-center justify-center gap-2">', 
     'className="flex-1 bg-ipe/10 text-ipe py-2 rounded-lg text-base font-medium flex items-center justify-center gap-2">'),
    (r'className="flex-1 bg-neutral-dark/10 text-neutral-dark py-2 rounded-lg text-sm font-medium">', 
     'className="flex-1 bg-neutral-dark/10 text-neutral-dark py-2 rounded-lg text-base font-medium">'),
    
    # Card de sugestão da IA
    (r'<div className="bg-cerrado-light/30 rounded-xl p-4 text-sm">', 
     '<div className="bg-cerrado-light/30 rounded-xl p-4 text-base">'),
    (r'<p className="font-medium text-neutral-dark mb-2">💡 Sugestão', 
     '<p className="font-medium text-lg text-neutral-dark mb-2">💡 Sugestão'),
    (r'<p className="text-neutral-dark/80">\s*Que tal', 
     '<p className="text-base text-neutral-dark/80">\n          Que tal'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ MemoryDetailScreen ajustado!")
print("📏 Elementos mantidos no mesmo tamanho")
print("📝 Apenas textos aumentados para melhor leitura")
print("🚀 Execute: npm run dev")
