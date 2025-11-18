#!/usr/bin/env python3
"""
Script para corrigir definitivamente o corte do título
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Ajustar para evitar qualquer corte
replacements = [
    # Adicionar overflow-x-hidden no main
    (r'<main className="min-h-screen bg-gradient-to-br from-neutral-light via-white to-cerrado-light/30 py-12">', 
     '<main className="min-h-screen bg-gradient-to-br from-neutral-light via-white to-cerrado-light/30 py-12 overflow-x-hidden">'),
    
    # Aumentar padding do container
    (r'<div className="container mx-auto px-4 sm:px-6">', 
     '<div className="container mx-auto px-4 sm:px-6 lg:px-8">'),
    
    # Adicionar overflow-visible e ajustar padding do header
    (r'className="text-center mb-12 px-4"', 
     'className="text-center mb-12 px-2 sm:px-4 overflow-visible"'),
    
    # Adicionar overflow-visible e whitespace-normal no título
    (r'<h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-neutral-dark mb-4 break-words">', 
     '<h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-neutral-dark mb-4 break-words overflow-visible whitespace-normal">'),
    
    # Adicionar padding no subtítulo também
    (r'<p className="text-lg sm:text-xl text-neutral-dark/70 max-w-2xl mx-auto">', 
     '<p className="text-lg sm:text-xl text-neutral-dark/70 max-w-2xl mx-auto px-2">'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Título corrigido definitivamente!")
print("📝 Overflow-x-hidden no main, overflow-visible no título")
print("🚀 Execute: npm run dev")
