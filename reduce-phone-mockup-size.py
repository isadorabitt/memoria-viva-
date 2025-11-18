#!/usr/bin/env python3
"""
Script para reduzir o tamanho do mockup do telefone, mantendo textos
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Reduzir tamanho do mockup, manter textos
replacements = [
    # Container do telefone
    (r'className="relative mx-auto max-w-sm">', 
     'className="relative mx-auto max-w-xs">'),
    
    # Padding do frame
    (r'className="bg-neutral-dark rounded-\[3rem\] p-4 shadow-2xl">', 
     'className="bg-neutral-dark rounded-[3rem] p-3 shadow-2xl">'),
    
    # Status bar - reduzir padding e tamanho do ícone
    (r'className="bg-gradient-to-r from-ipe to-ipe-dark px-6 py-4 text-white flex items-center justify-between">', 
     'className="bg-gradient-to-r from-ipe to-ipe-dark px-5 py-3 text-white flex items-center justify-between">'),
    (r'width=\{24\} height=\{24\} className="object-contain" />', 
     'width={20} height={20} className="object-contain" />'),
    (r'<span className="font-bold">Memória Viva\+</span>', 
     '<span className="font-bold text-sm">Memória Viva+</span>'),
    
    # Screen content - reduzir altura mínima e padding
    (r'className="min-h-\[600px\] bg-neutral-light/30 p-6">', 
     'className="min-h-[550px] bg-neutral-light/30 p-5">'),
    
    # Bottom navigation - reduzir padding e tamanho dos ícones
    (r'className="bg-white border-t p-4 flex justify-around">', 
     'className="bg-white border-t p-3 flex justify-around">'),
    (r'<item\.icon className="w-6 h-6" />', 
     '<item.icon className="w-5 h-5" />'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Tamanho do mockup reduzido!")
print("📱 Mockup menor, textos mantidos no tamanho aumentado")
print("🚀 Execute: npm run dev")
