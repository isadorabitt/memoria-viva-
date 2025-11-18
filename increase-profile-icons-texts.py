#!/usr/bin/env python3
"""
Script para aumentar ícones e textos na tela de perfil para idosos
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Aumentar ícones e textos na ProfileScreen
replacements = [
    # Avatar - aumentar tamanho
    (r'className="w-20 h-20 bg-white rounded-full mx-auto mb-3 flex items-center justify-center text-4xl">', 
     'className="w-24 h-24 bg-white rounded-full mx-auto mb-4 flex items-center justify-center text-5xl">'),
    
    # Nome - aumentar
    (r'<h3 className="font-bold text-xl mb-1">Maria Silva</h3>', 
     '<h3 className="font-bold text-2xl mb-2">Maria Silva</h3>'),
    
    # Texto "Membro desde" - aumentar
    (r'<p className="text-sm opacity-90">Membro desde', 
     '<p className="text-base opacity-90">Membro desde'),
    
    # Cards de estatísticas - aumentar números e labels
    (r'className="bg-white rounded-xl p-3 text-center shadow-sm">', 
     'className="bg-white rounded-xl p-4 text-center shadow-sm">'),
    (r'<div className="text-2xl font-bold text-cerrado">35</div>', 
     '<div className="text-3xl font-bold text-cerrado">35</div>'),
    (r'<div className="text-2xl font-bold text-ipe">12</div>', 
     '<div className="text-3xl font-bold text-ipe">12</div>'),
    (r'<div className="text-2xl font-bold text-wisdom">3</div>', 
     '<div className="text-3xl font-bold text-wisdom">3</div>'),
    (r'<p className="text-xs text-neutral-dark/70">Memórias</p>', 
     '<p className="text-sm text-neutral-dark/70">Memórias</p>'),
    (r'<p className="text-xs text-neutral-dark/70">Amigos</p>', 
     '<p className="text-sm text-neutral-dark/70">Amigos</p>'),
    (r'<p className="text-xs text-neutral-dark/70">Círculos</p>', 
     '<p className="text-sm text-neutral-dark/70">Círculos</p>'),
    
    # Título "Conquistas" - aumentar
    (r'<h4 className="font-bold text-neutral-dark mb-3 text-sm">', 
     '<h4 className="font-bold text-neutral-dark mb-4 text-base">'),
    
    # Ícones de conquistas - aumentar
    (r'className="flex gap-3">', 
     'className="flex gap-4">'),
    (r'className="w-12 h-12 bg-cerrado-light rounded-lg flex items-center justify-center text-2xl">', 
     'className="w-16 h-16 bg-cerrado-light rounded-lg flex items-center justify-center text-3xl">'),
    
    # Botão Configurações - aumentar ícone e texto
    (r'className="w-full bg-neutral-dark/10 hover:bg-neutral-dark/20 text-neutral-dark py-3 rounded-xl font-medium transition-colors flex items-center justify-center gap-2">', 
     'className="w-full bg-neutral-dark/10 hover:bg-neutral-dark/20 text-neutral-dark py-4 rounded-xl font-medium text-base transition-colors flex items-center justify-center gap-3">'),
    (r'<Settings className="w-5 h-5" />', 
     '<Settings className="w-6 h-6" />'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Ícones e textos aumentados na tela de perfil!")
print("👴 Melhor visibilidade para idosos")
print("🚀 Execute: npm run dev")
