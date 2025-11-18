#!/usr/bin/env python3
"""
Script para aumentar tamanhos na tela CircleFeedScreen
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Substituições específicas para CircleFeedScreen
replacements = [
    # Header do círculo
    (r'<div className="bg-ipe text-white rounded-xl p-4">', 
     '<div className="bg-ipe text-white rounded-xl p-6">'),
    (r'<h3 className="font-bold flex items-center gap-2">', 
     '<h3 className="font-bold text-2xl flex items-center gap-3">'),
    (r'<span className="text-2xl">🍲</span>', 
     '<span className="text-4xl">🍲</span>'),
    
    # Cards de post
    (r'<div className="bg-white rounded-xl p-4 shadow-sm">', 
     '<div className="bg-white rounded-xl p-6 shadow-sm">'),
    (r'className="flex items-start gap-3 mb-3">', 
     'className="flex items-start gap-4 mb-4">'),
    (r'className="w-10 h-10 bg-cerrado rounded-full flex items-center justify-center text-lg">', 
     'className="w-16 h-16 bg-cerrado rounded-full flex items-center justify-center text-3xl">'),
    (r'className="w-10 h-10 bg-wisdom rounded-full flex items-center justify-center text-lg">', 
     'className="w-16 h-16 bg-wisdom rounded-full flex items-center justify-center text-3xl">'),
    (r'<h4 className="font-bold text-neutral-dark text-sm">Dona Ana</h4>', 
     '<h4 className="font-bold text-neutral-dark text-xl">Dona Ana</h4>'),
    (r'<h4 className="font-bold text-neutral-dark text-sm">Seu João</h4>', 
     '<h4 className="font-bold text-neutral-dark text-xl">Seu João</h4>'),
    (r'<p className="text-xs text-neutral-dark/60">Há 2 horas</p>', 
     '<p className="text-base text-neutral-dark/60">Há 2 horas</p>'),
    (r'<p className="text-xs text-neutral-dark/60">Ontem</p>', 
     '<p className="text-base text-neutral-dark/60">Ontem</p>'),
    (r'<p className="text-sm text-neutral-dark/80 mb-3">\s*Meu empadão', 
     '<p className="text-xl text-neutral-dark/80 mb-4 leading-relaxed">\n          Meu empadão'),
    (r'<p className="text-sm text-neutral-dark/80 mb-3">\s*Quem lembra', 
     '<p className="text-xl text-neutral-dark/80 mb-4 leading-relaxed">\n          Quem lembra'),
    (r'className="flex gap-2">', 
     'className="flex gap-3">'),
    (r'className="flex items-center gap-1 text-ipe text-sm">', 
     'className="flex items-center gap-2 text-ipe text-lg font-medium">'),
    (r'className="flex items-center gap-1 text-neutral-dark/60 text-sm">', 
     'className="flex items-center gap-2 text-neutral-dark/60 text-lg font-medium">'),
    (r'className="space-y-4"', 
     'className="space-y-5"'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Tamanhos aumentados no CircleFeedScreen!")
print("🚀 Execute: npm run dev")
