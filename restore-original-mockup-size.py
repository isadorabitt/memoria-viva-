#!/usr/bin/env python3
"""
Script para restaurar o mockup ao tamanho original
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Restaurar tamanho original
replacements = [
    # Container - restaurar para max-w-sm
    (r'className="relative mx-auto max-w-\[240px\]">', 
     'className="relative mx-auto max-w-sm">'),
    
    # Frame - restaurar padding e border radius
    (r'className="bg-neutral-dark rounded-\[2\.5rem\] p-2 shadow-2xl">', 
     'className="bg-neutral-dark rounded-[3rem] p-4 shadow-2xl">'),
    (r'className="bg-white rounded-\[2rem\] overflow-hidden relative">', 
     'className="bg-white rounded-[2.5rem] overflow-hidden relative">'),
    
    # Status bar - restaurar
    (r'className="bg-gradient-to-r from-ipe to-ipe-dark px-3 py-2 text-white flex items-center justify-between">', 
     'className="bg-gradient-to-r from-ipe to-ipe-dark px-6 py-4 text-white flex items-center justify-between">'),
    (r'className="flex items-center gap-1\.5">', 
     'className="flex items-center gap-2">'),
    (r'width=\{16\} height=\{16\} className="object-contain" />', 
     'width={24} height={24} className="object-contain" />'),
    (r'<span className="font-bold text-\[10px\]">Memória Viva\+</span>', 
     '<span className="font-bold">Memória Viva+</span>'),
    (r'<div className="text-\[9px\] opacity-80">9:41</div>', 
     '<div className="text-xs opacity-80">9:41</div>'),
    
    # Screen content - restaurar altura e padding
    (r'className="min-h-\[380px\] bg-neutral-light/30 p-3">', 
     'className="min-h-[600px] bg-neutral-light/30 p-6">'),
    
    # Bottom navigation - restaurar
    (r'className="bg-white border-t p-2 flex justify-around">', 
     'className="bg-white border-t p-4 flex justify-around">'),
    (r'className="flex flex-col items-center gap-0\.5 text-neutral-dark/60 hover:text-ipe transition-colors">', 
     'className="flex flex-col items-center gap-1 text-neutral-dark/60 hover:text-ipe transition-colors">'),
    (r'<item\.icon className="w-4 h-4" />', 
     '<item.icon className="w-6 h-6" />'),
    (r'<span className="text-\[9px\]">\{item\.label\}</span>', 
     '<span className="text-xs">{item.label}</span>'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Mockup restaurado ao tamanho original!")
print("📱 Tamanho: max-w-sm (384px), altura: 600px")
print("🚀 Execute: npm run dev")
