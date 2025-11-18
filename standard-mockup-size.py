#!/usr/bin/env python3
"""
Script para ajustar mockup para tamanho padrão de smartphone
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Ajustar para tamanho padrão
replacements = [
    # Container - reduzir de max-w-sm (384px) para max-w-xs (320px)
    (r'className="relative mx-auto max-w-sm">', 
     'className="relative mx-auto max-w-xs">'),
    
    # Frame - reduzir padding
    (r'className="bg-neutral-dark rounded-\[3rem\] p-4 shadow-2xl">', 
     'className="bg-neutral-dark rounded-[3rem] p-3 shadow-2xl">'),
    
    # Status bar - reduzir proporcionalmente
    (r'className="bg-gradient-to-r from-ipe to-ipe-dark px-6 py-4 text-white flex items-center justify-between">', 
     'className="bg-gradient-to-r from-ipe to-ipe-dark px-5 py-3 text-white flex items-center justify-between">'),
    (r'width=\{24\} height=\{24\} className="object-contain" />', 
     'width={20} height={20} className="object-contain" />'),
    (r'<span className="font-bold">Memória Viva\+</span>', 
     '<span className="font-bold text-sm">Memória Viva+</span>'),
    
    # Screen content - reduzir altura proporcionalmente
    (r'className="min-h-\[600px\] bg-neutral-light/30 p-6">', 
     'className="min-h-[500px] bg-neutral-light/30 p-5">'),
    
    # Bottom navigation - reduzir proporcionalmente
    (r'className="bg-white border-t p-4 flex justify-around">', 
     'className="bg-white border-t p-3 flex justify-around">'),
    (r'<item\.icon className="w-6 h-6" />', 
     '<item.icon className="w-5 h-5" />'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Mockup ajustado para tamanho padrão!")
print("📱 Tamanho: max-w-xs (320px), altura: 500px")
print("🚀 Execute: npm run dev")
