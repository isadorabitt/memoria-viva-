#!/usr/bin/env python3
"""
Script para aumentar AGressivamente todos os tamanhos de texto na página de demo
para melhorar acessibilidade para idosos - FOCO NO MOCKUP DO TELEFONE
"""

import re

file_path = "src/app/demo/page.tsx"

# Ler o arquivo
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Substituições AGRESSIVAS de tamanhos de texto - FOCO NO MOCKUP
replacements = [
    # Status bar do telefone
    (r'text-xs opacity-80">9:41', 'text-base opacity-80">9:41'),
    (r'font-bold">Memória Viva\+', 'font-bold text-lg">Memória Viva+'),
    
    # Bottom navigation
    (r'text-xs">\{item\.label\}', 'text-base font-medium">{item.label}'),
    
    # WelcomeScreen
    (r'<h2 className="text-2xl font-bold text-neutral-dark mb-2">', '<h2 className="text-4xl font-bold text-neutral-dark mb-3">'),
    (r'<p className="text-neutral-dark/70">Que bom', '<p className="text-xl text-neutral-dark/70">Que bom'),
    (r'<p className="text-neutral-dark leading-relaxed">', '<p className="text-xl text-neutral-dark leading-relaxed">'),
    (r'className="bg-white border-2 border-ipe/20 hover:border-ipe hover:bg-ipe/5 py-4 rounded-xl font-medium transition-colors">', 
     'className="bg-white border-2 border-ipe/20 hover:border-ipe hover:bg-ipe/5 py-6 rounded-xl font-medium transition-colors text-xl">'),
    
    # MoodScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark mb-2">', '<h3 className="text-3xl font-bold text-neutral-dark mb-3">'),
    (r'<p className="text-sm text-neutral-dark/70">', '<p className="text-lg text-neutral-dark/70">'),
    (r'<div className="text-lg">\{mood\.label\}</div>', '<div className="text-2xl">{mood.label}</div>'),
    (r'<p className="text-sm text-neutral-dark/80">', '<p className="text-lg text-neutral-dark/80">'),
    
    # RecordScreen
    (r'<p className="text-sm text-neutral-dark/70">\s*Aperte', '<p className="text-lg text-neutral-dark/70">\n          Aperte'),
    (r'<p className="mt-6 font-medium text-neutral-dark">', '<p className="mt-6 font-medium text-xl text-neutral-dark">'),
    (r'className="bg-cerrado-light rounded-xl p-4 text-sm text-neutral-dark/80 italic"', 
     'className="bg-cerrado-light rounded-xl p-6 text-lg text-neutral-dark/80 italic"'),
    (r'className="bg-neutral-dark/10 hover:bg-neutral-dark/20 px-4 py-2 rounded-full text-sm transition-colors">', 
     'className="bg-neutral-dark/10 hover:bg-neutral-dark/20 px-6 py-3 rounded-full text-lg transition-colors">'),
    (r'className="bg-ipe hover:bg-ipe-dark text-white px-6 py-2 rounded-full text-sm transition-colors">', 
     'className="bg-ipe hover:bg-ipe-dark text-white px-8 py-3 rounded-full text-lg transition-colors">'),
    
    # TimelineScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark">Suas Memórias</h3>', 
     '<h3 className="text-2xl font-bold text-neutral-dark">Suas Memórias</h3>'),
    (r'<p className="text-sm text-neutral-dark/60">\s*\{mem\.count\}', 
     '<p className="text-base text-neutral-dark/60">\n                {mem.count}'),
    (r'className="w-full bg-gradient-to-r from-ipe to-ipe-dark text-white py-3 rounded-xl font-medium shadow-lg hover:opacity-90 transition-opacity">', 
     'className="w-full bg-gradient-to-r from-ipe to-ipe-dark text-white py-4 rounded-xl font-medium text-lg shadow-lg hover:opacity-90 transition-opacity">'),
    
    # MemoryDetailScreen - CRÍTICO PARA ACESSIBILIDADE
    (r'<p className="text-xs text-neutral-dark/60">Gravado em', 
     '<p className="text-base text-neutral-dark/60">Gravado em'),
    (r'<h3 className="font-bold text-neutral-dark mb-2">\s*Festas', 
     '<h3 className="font-bold text-2xl text-neutral-dark mb-3">\n          Festas'),
    (r'<p className="text-sm text-neutral-dark/80 leading-relaxed mb-4">', 
     '<p className="text-xl text-neutral-dark/80 leading-relaxed mb-5">'),
    (r'className="flex-1 bg-ipe/10 text-ipe py-2 rounded-lg text-sm font-medium flex items-center justify-center gap-2">', 
     'className="flex-1 bg-ipe/10 text-ipe py-3 rounded-lg text-lg font-medium flex items-center justify-center gap-2">'),
    (r'className="flex-1 bg-neutral-dark/10 text-neutral-dark py-2 rounded-lg text-sm font-medium">', 
     'className="flex-1 bg-neutral-dark/10 text-neutral-dark py-3 rounded-lg text-lg font-medium">'),
    (r'<div className="bg-cerrado-light/30 rounded-xl p-4 text-sm">', 
     '<div className="bg-cerrado-light/30 rounded-xl p-5 text-lg">'),
    (r'<p className="font-medium text-neutral-dark mb-2">💡 Sugestão', 
     '<p className="font-medium text-xl text-neutral-dark mb-3">💡 Sugestão'),
    (r'<p className="text-neutral-dark/80">\s*Que tal', 
     '<p className="text-lg text-neutral-dark/80">\n          Que tal'),
    
    # CirclesScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark">Meus Círculos</h3>', 
     '<h3 className="text-2xl font-bold text-neutral-dark">Meus Círculos</h3>'),
    (r'<p className="text-sm text-neutral-dark/60 flex items-center gap-1">', 
     '<p className="text-base text-neutral-dark/60 flex items-center gap-1">'),
    (r'<span className="text-xs bg-green-100', 
     '<span className="text-sm bg-green-100'),
    (r'className="w-full bg-white border-2 border-ipe text-ipe py-3 rounded-xl font-medium hover:bg-ipe/10 transition-colors">', 
     'className="w-full bg-white border-2 border-ipe text-ipe py-4 rounded-xl font-medium text-lg hover:bg-ipe/10 transition-colors">'),
    
    # CircleFeedScreen
    (r'<h4 className="font-bold text-neutral-dark text-sm">Dona Ana</h4>', 
     '<h4 className="font-bold text-neutral-dark text-lg">Dona Ana</h4>'),
    (r'<h4 className="font-bold text-neutral-dark text-sm">Seu João</h4>', 
     '<h4 className="font-bold text-neutral-dark text-lg">Seu João</h4>'),
    (r'<p className="text-xs text-neutral-dark/60">Há 2 horas</p>', 
     '<p className="text-sm text-neutral-dark/60">Há 2 horas</p>'),
    (r'<p className="text-xs text-neutral-dark/60">Ontem</p>', 
     '<p className="text-sm text-neutral-dark/60">Ontem</p>'),
    (r'<p className="text-sm text-neutral-dark/80 mb-3">\s*Meu empadão', 
     '<p className="text-lg text-neutral-dark/80 mb-4">\n          Meu empadão'),
    (r'<p className="text-sm text-neutral-dark/80 mb-3">\s*Quem lembra', 
     '<p className="text-lg text-neutral-dark/80 mb-4">\n          Quem lembra'),
    (r'className="flex items-center gap-1 text-ipe text-sm">', 
     'className="flex items-center gap-1 text-ipe text-base">'),
    (r'className="flex items-center gap-1 text-neutral-dark/60 text-sm">', 
     'className="flex items-center gap-1 text-neutral-dark/60 text-base">'),
    
    # EventsScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark">Eventos Próximos</h3>', 
     '<h3 className="text-2xl font-bold text-neutral-dark">Eventos Próximos</h3>'),
    (r'<p className="text-sm text-neutral-dark/60">\s*Centro de Convivência', 
     '<p className="text-base text-neutral-dark/60">\n              Centro de Convivência'),
    (r'<p className="text-sm text-neutral-dark/60">Parque Vaca Brava</p>', 
     '<p className="text-base text-neutral-dark/60">Parque Vaca Brava</p>'),
    (r'<span className="bg-cerrado text-cerrado-dark text-xs px-2 py-1 rounded-full font-medium">', 
     '<span className="bg-cerrado text-cerrado-dark text-sm px-3 py-2 rounded-full font-medium">'),
    (r'<span className="bg-ipe-light text-ipe-dark text-xs px-2 py-1 rounded-full font-medium">', 
     '<span className="bg-ipe-light text-ipe-dark text-sm px-3 py-2 rounded-full font-medium">'),
    (r'<div className="flex gap-3 text-xs text-neutral-dark/60 mb-3">', 
     '<div className="flex gap-3 text-sm text-neutral-dark/60 mb-4">'),
    (r'className="w-full bg-ipe text-white py-2 rounded-lg font-medium hover:bg-ipe-dark transition-colors">', 
     'className="w-full bg-ipe text-white py-3 rounded-lg font-medium text-lg hover:bg-ipe-dark transition-colors">'),
    (r'className="w-full bg-white border-2 border-ipe text-ipe py-2 rounded-lg font-medium hover:bg-ipe/10 transition-colors">', 
     'className="w-full bg-white border-2 border-ipe text-ipe py-3 rounded-lg font-medium text-lg hover:bg-ipe/10 transition-colors">'),
    
    # NotificationsScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark">Notificações</h3>', 
     '<h3 className="text-2xl font-bold text-neutral-dark">Notificações</h3>'),
    (r'<h4 className="font-bold text-neutral-dark text-sm mb-1">', 
     '<h4 className="font-bold text-neutral-dark text-lg mb-2">'),
    (r'<p className="text-xs text-neutral-dark/70 mb-2">', 
     '<p className="text-base text-neutral-dark/70 mb-3">'),
    (r'<p className="text-xs text-neutral-dark/50">\{notif\.time\}</p>', 
     '<p className="text-sm text-neutral-dark/50">{notif.time}</p>'),
    
    # ProfileScreen
    (r'<h3 className="font-bold text-xl mb-1">Maria Silva</h3>', 
     '<h3 className="font-bold text-2xl mb-2">Maria Silva</h3>'),
    (r'<p className="text-sm opacity-90">Membro desde', 
     '<p className="text-base opacity-90">Membro desde'),
    (r'<p className="text-xs text-neutral-dark/70">Memórias</p>', 
     '<p className="text-sm text-neutral-dark/70">Memórias</p>'),
    (r'<p className="text-xs text-neutral-dark/70">Amigos</p>', 
     '<p className="text-sm text-neutral-dark/70">Amigos</p>'),
    (r'<p className="text-xs text-neutral-dark/70">Círculos</p>', 
     '<p className="text-sm text-neutral-dark/70">Círculos</p>'),
    (r'<h4 className="font-bold text-neutral-dark mb-3 text-sm">', 
     '<h4 className="font-bold text-neutral-dark mb-4 text-lg">'),
    (r'className="w-full bg-neutral-dark/10 hover:bg-neutral-dark/20 text-neutral-dark py-3 rounded-xl font-medium transition-colors flex items-center justify-center gap-2">', 
     'className="w-full bg-neutral-dark/10 hover:bg-neutral-dark/20 text-neutral-dark py-4 rounded-xl font-medium text-lg transition-colors flex items-center justify-center gap-2">'),
]

# Aplicar substituições
for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

# Escrever o arquivo
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Tamanhos de texto aumentados AGRESSIVAMENTE!")
print("📱 Foco especial nos textos dentro do mockup do telefone")
print("🚀 Execute: npm run dev")
