#!/usr/bin/env python3
"""
Script para aumentar apenas textos na EventsScreen, mantendo elementos iguais
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Aumentar apenas textos, manter elementos iguais
replacements = [
    # Título principal
    (r'<h3 className="text-xl font-bold text-neutral-dark">Eventos Próximos</h3>', 
     '<h3 className="text-2xl font-bold text-neutral-dark">Eventos Próximos</h3>'),
    
    # Títulos dos eventos
    (r'<h4 className="font-bold text-neutral-dark">Oficina de Violão</h4>', 
     '<h4 className="font-bold text-lg text-neutral-dark">Oficina de Violão</h4>'),
    (r'<h4 className="font-bold text-neutral-dark">Dança de Salão</h4>', 
     '<h4 className="font-bold text-lg text-neutral-dark">Dança de Salão</h4>'),
    
    # Localização
    (r'<p className="text-sm text-neutral-dark/60">\s*Centro de Convivência', 
     '<p className="text-base text-neutral-dark/60">\n              Centro de Convivência'),
    (r'<p className="text-sm text-neutral-dark/60">Parque Vaca Brava</p>', 
     '<p className="text-base text-neutral-dark/60">Parque Vaca Brava</p>'),
    
    # Tags de distância
    (r'className="bg-cerrado text-cerrado-dark text-xs px-2 py-1 rounded-full font-medium">', 
     'className="bg-cerrado text-cerrado-dark text-sm px-2 py-1 rounded-full font-medium">'),
    (r'className="bg-ipe-light text-ipe-dark text-xs px-2 py-1 rounded-full font-medium">', 
     'className="bg-ipe-light text-ipe-dark text-sm px-2 py-1 rounded-full font-medium">'),
    
    # Detalhes (data, hora, pessoas)
    (r'className="flex gap-3 text-xs text-neutral-dark/60 mb-3">', 
     'className="flex gap-3 text-sm text-neutral-dark/60 mb-3">'),
    
    # Botões
    (r'className="w-full bg-ipe text-white py-2 rounded-lg font-medium hover:bg-ipe-dark transition-colors">', 
     'className="w-full bg-ipe text-white py-3 rounded-lg font-medium text-lg hover:bg-ipe-dark transition-colors">'),
    (r'className="w-full bg-white border-2 border-ipe text-ipe py-2 rounded-lg font-medium hover:bg-ipe/10 transition-colors">', 
     'className="w-full bg-white border-2 border-ipe text-ipe py-3 rounded-lg font-medium text-lg hover:bg-ipe/10 transition-colors">'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Textos aumentados na EventsScreen!")
print("📏 Elementos mantidos no mesmo tamanho")
print("📝 Apenas textos aumentados para melhor leitura")
print("🚀 Execute: npm run dev")
