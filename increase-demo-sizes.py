#!/usr/bin/env python3
"""
Script para aumentar tamanhos de texto, botões e elementos na página de demo
para melhorar acessibilidade para idosos.
"""

import re

file_path = "src/app/demo/page.tsx"

# Ler o arquivo
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Substituições de tamanhos de texto
replacements = [
    # Header
    (r'text-4xl md:text-6xl', 'text-5xl md:text-7xl'),
    (r'text-xl text-neutral-dark/70', 'text-2xl md:text-3xl text-neutral-dark/70'),
    
    # Floating hint
    (r'px-4 py-2', 'px-6 py-3'),
    (r'w-4 h-4', 'w-6 h-6'),
    (r'text-sm font-medium">Interaja!', 'text-lg font-medium">Interaja!'),
    
    # Phone frame
    (r'max-w-sm', 'max-w-md'),
    (r'p-4 shadow-2xl', 'p-5 shadow-2xl'),
    (r'px-6 py-4', 'px-8 py-5'),
    (r'width=\{24\} height=\{24\}', 'width={32} height={32}'),
    (r'text-xs opacity-80">9:41', 'text-base opacity-80">9:41'),
    (r'font-bold">Memória Viva\+', 'font-bold text-lg">Memória Viva+'),
    (r'min-h-\[600px\]', 'min-h-[700px]'),
    (r'p-6', 'p-8'),
    
    # Bottom navigation
    (r'p-4 flex justify-around', 'p-5 flex justify-around'),
    (r'gap-1', 'gap-2'),
    (r'w-6 h-6', 'w-8 h-8'),
    (r'text-xs">\{item\.label\}', 'text-base font-medium">{item.label}'),
    
    # Step indicator
    (r'h-2 rounded-full', 'h-3 rounded-full'),
    (r'bg-ipe w-12', 'bg-ipe w-16'),
    (r'bg-ipe/50 w-8', 'bg-ipe/50 w-12'),
    (r'bg-neutral-dark/20 w-8', 'bg-neutral-dark/20 w-12'),
    (r'gap-2 flex-wrap', 'gap-3 flex-wrap'),
    
    # Step content
    (r'space-y-6', 'space-y-8'),
    (r'gap-4', 'gap-5'),
    (r'w-16 h-16', 'w-20 h-20'),
    (r'w-8 h-8 text-white', 'w-10 h-10 text-white'),
    (r'text-sm text-neutral-dark/60', 'text-base text-neutral-dark/60'),
    (r'text-3xl font-bold', 'text-4xl md:text-5xl font-bold'),
    (r'text-xl text-neutral-dark/80', 'text-2xl md:text-3xl text-neutral-dark/80'),
    
    # Features card
    (r'p-6 shadow-lg', 'p-8 shadow-lg'),
    (r'w-5 h-5 text-ipe', 'w-7 h-7 text-ipe'),
    (r'mb-4', 'mb-5'),
    (r'text-sm text-neutral-dark/70', 'text-lg text-neutral-dark/70'),
    (r'space-y-2', 'space-y-3'),
    (r'gap-2', 'gap-3'),
    (r'text-ipe">✓', 'text-ipe text-xl">✓'),
    
    # Navigation buttons
    (r'pt-4', 'pt-6'),
    (r'gap-4', 'gap-5'),
    (r'px-6 py-4', 'px-8 py-5'),
    (r'w-5 h-5', 'w-6 h-6'),
    (r'Anterior', 'Anterior'),
    (r'Próximo', 'Próximo'),
    (r'border-2 border-neutral-dark/20 text-neutral-dark px-6 py-4 rounded-xl font-medium hover:border-ipe hover:text-ipe transition-colors disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-2', 
     'border-2 border-neutral-dark/20 text-neutral-dark px-8 py-5 rounded-xl font-medium hover:border-ipe hover:text-ipe transition-colors disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-3 text-lg'),
    (r'bg-gradient-to-r from-ipe to-ipe-dark text-white px-6 py-4 rounded-xl font-medium hover:opacity-90 transition-opacity disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-2 shadow-lg',
     'bg-gradient-to-r from-ipe to-ipe-dark text-white px-8 py-5 rounded-xl font-medium hover:opacity-90 transition-opacity disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-3 shadow-lg text-lg'),
    
    # WelcomeScreen
    (r'space-y-6', 'space-y-8'),
    (r'pt-8 mb-4', 'pt-8 mb-6'),
    (r'width=\{64\} height=\{64\}', 'width={96} height={96}'),
    (r'text-2xl font-bold', 'text-4xl font-bold'),
    (r'mb-2', 'mb-3'),
    (r'text-neutral-dark/70">Que bom', 'text-xl text-neutral-dark/70">Que bom'),
    (r'p-6 shadow-sm', 'p-8 shadow-sm'),
    (r'gap-3', 'gap-4'),
    (r'width=\{32\} height=\{32\}', 'width={48} height={48}'),
    (r'text-neutral-dark leading-relaxed', 'text-xl text-neutral-dark leading-relaxed'),
    (r'grid grid-cols-2 gap-3', 'grid grid-cols-2 gap-4'),
    (r'py-4 rounded-xl', 'py-6 rounded-xl'),
    (r'font-medium transition-colors">', 'font-medium transition-colors text-lg">'),
    
    # MoodScreen
    (r'text-xl font-bold', 'text-3xl font-bold'),
    (r'text-sm text-neutral-dark/70', 'text-lg text-neutral-dark/70'),
    (r'grid grid-cols-2 gap-3', 'grid grid-cols-2 gap-4'),
    (r'py-6 rounded-2xl', 'py-8 rounded-2xl'),
    (r'text-lg">\{mood\.label\}', 'text-xl">{mood.label}'),
    (r'text-4xl mb-2', 'text-5xl mb-3'),
    (r'p-4', 'p-6'),
    (r'text-sm text-neutral-dark/80', 'text-lg text-neutral-dark/80'),
    
    # RecordScreen
    (r'text-xl font-bold', 'text-3xl font-bold'),
    (r'text-sm text-neutral-dark/70', 'text-lg text-neutral-dark/70'),
    (r'p-8 text-center', 'p-10 text-center'),
    (r'w-32 h-32', 'w-40 h-40'),
    (r'w-16 h-16', 'w-20 h-20'),
    (r'mt-6', 'mt-8'),
    (r'font-medium text-neutral-dark', 'font-medium text-xl text-neutral-dark'),
    (r'gap-2', 'gap-3'),
    (r'w-3 h-3', 'w-4 h-4'),
    (r'p-4 text-sm', 'p-6 text-lg'),
    (r'gap-2 justify-center', 'gap-3 justify-center'),
    (r'px-4 py-2 rounded-full text-sm', 'px-6 py-3 rounded-full text-lg'),
    (r'px-6 py-2 rounded-full text-sm', 'px-8 py-3 rounded-full text-lg'),
    
    # TimelineScreen
    (r'space-y-4', 'space-y-5'),
    (r'text-xl font-bold', 'text-2xl font-bold'),
    (r'p-4 border-l-4', 'p-5 border-l-4'),
    (r'text-sm text-neutral-dark/60', 'text-base text-neutral-dark/60'),
    (r'w-6 h-6', 'w-8 h-8'),
    (r'py-3 rounded-xl', 'py-4 rounded-xl'),
    
    # MemoryDetailScreen
    (r'p-4 shadow-sm', 'p-6 shadow-sm'),
    (r'gap-2 mb-3', 'gap-3 mb-4'),
    (r'w-8 h-8', 'w-12 h-12'),
    (r'text-sm', 'text-lg'),
    (r'text-xs text-neutral-dark/60', 'text-sm text-neutral-dark/60'),
    (r'text-sm text-neutral-dark/80', 'text-base text-neutral-dark/80'),
    (r'mb-4', 'mb-5'),
    (r'gap-2', 'gap-3'),
    (r'py-2 rounded-lg text-sm', 'py-3 rounded-lg text-base'),
    (r'w-4 h-4', 'w-5 h-5'),
    (r'p-4 text-sm', 'p-5 text-base'),
    (r'font-medium text-neutral-dark mb-2', 'font-medium text-lg text-neutral-dark mb-3'),
    
    # CirclesScreen
    (r'text-xl font-bold', 'text-2xl font-bold'),
    (r'p-4 shadow-sm', 'p-5 shadow-sm'),
    (r'gap-3 mb-2', 'gap-4 mb-3'),
    (r'text-3xl', 'text-4xl'),
    (r'text-sm text-neutral-dark/60', 'text-base text-neutral-dark/60'),
    (r'w-4 h-4', 'w-5 h-5'),
    (r'text-xs bg-green-100', 'text-sm bg-green-100'),
    (r'px-2 py-1', 'px-3 py-2'),
    (r'py-3 rounded-xl', 'py-4 rounded-xl'),
    
    # CircleFeedScreen
    (r'space-y-4', 'space-y-5'),
    (r'p-4', 'p-5'),
    (r'text-2xl', 'text-3xl'),
    (r'gap-3 mb-3', 'gap-4 mb-4'),
    (r'w-10 h-10', 'w-14 h-14'),
    (r'text-lg', 'text-xl'),
    (r'text-sm">Dona Ana', 'text-base">Dona Ana'),
    (r'text-xs text-neutral-dark/60', 'text-sm text-neutral-dark/60'),
    (r'text-sm text-neutral-dark/80 mb-3', 'text-base text-neutral-dark/80 mb-4'),
    (r'gap-2', 'gap-3'),
    (r'text-ipe text-sm', 'text-ipe text-base'),
    (r'text-neutral-dark/60 text-sm', 'text-neutral-dark/60 text-base'),
    
    # EventsScreen
    (r'text-xl font-bold', 'text-2xl font-bold'),
    (r'p-4 shadow-sm', 'p-5 shadow-sm'),
    (r'mb-3', 'mb-4'),
    (r'text-sm text-neutral-dark/60', 'text-base text-neutral-dark/60'),
    (r'text-xs px-2 py-1', 'text-sm px-3 py-2'),
    (r'gap-3 text-xs', 'gap-4 text-sm'),
    (r'py-2 rounded-lg', 'py-3 rounded-lg'),
    
    # NotificationsScreen
    (r'space-y-3', 'space-y-4'),
    (r'text-xl font-bold', 'text-2xl font-bold'),
    (r'width=\{24\} height=\{24\}', 'width={32} height={32}'),
    (r'p-4 shadow-sm', 'p-5 shadow-sm'),
    (r'gap-3', 'gap-4'),
    (r'text-2xl', 'text-3xl'),
    (r'text-sm mb-1', 'text-base mb-2'),
    (r'text-xs text-neutral-dark/70 mb-2', 'text-sm text-neutral-dark/70 mb-3'),
    (r'text-xs text-neutral-dark/50', 'text-sm text-neutral-dark/50'),
    
    # ProfileScreen
    (r'space-y-4', 'space-y-5'),
    (r'p-6 text-center', 'p-8 text-center'),
    (r'w-20 h-20', 'w-24 h-24'),
    (r'mb-3', 'mb-4'),
    (r'text-4xl', 'text-5xl'),
    (r'text-xl mb-1', 'text-2xl mb-2'),
    (r'text-sm opacity-90', 'text-base opacity-90'),
    (r'gap-3', 'gap-4'),
    (r'p-3 text-center', 'p-4 text-center'),
    (r'text-2xl font-bold', 'text-3xl font-bold'),
    (r'text-xs text-neutral-dark/70', 'text-sm text-neutral-dark/70'),
    (r'p-4 shadow-sm', 'p-5 shadow-sm'),
    (r'mb-3 text-sm', 'mb-4 text-base'),
    (r'gap-3', 'gap-4'),
    (r'w-12 h-12', 'w-16 h-16'),
    (r'text-2xl', 'text-3xl'),
    (r'py-3 rounded-xl', 'py-4 rounded-xl'),
    (r'w-5 h-5', 'w-6 h-6'),
]

# Aplicar substituições
for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

# Escrever o arquivo
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Tamanhos aumentados com sucesso!")
print("🚀 Execute: npm run dev")
