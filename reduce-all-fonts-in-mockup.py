#!/usr/bin/env python3
"""
Script para reduzir todas as fontes dentro do mockup para diminuir o tamanho
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Reduzir todas as fontes dentro do mockup (dentro das funções de tela)
replacements = [
    # WelcomeScreen
    (r'<h2 className="text-2xl font-bold text-neutral-dark mb-2">', 
     '<h2 className="text-lg font-bold text-neutral-dark mb-2">'),
    (r'<p className="text-neutral-dark/70">Que bom', 
     '<p className="text-sm text-neutral-dark/70">Que bom'),
    (r'<p className="text-neutral-dark leading-relaxed">', 
     '<p className="text-sm text-neutral-dark leading-relaxed">'),
    (r'className="bg-white border-2 border-ipe/20 hover:border-ipe hover:bg-ipe/5 py-4 rounded-xl font-medium transition-colors">', 
     'className="bg-white border-2 border-ipe/20 hover:border-ipe hover:bg-ipe/5 py-3 rounded-xl font-medium text-sm transition-colors">'),
    
    # MoodScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark mb-2">\s*Check-in', 
     '<h3 className="text-base font-bold text-neutral-dark mb-2">\n        Check-in'),
    (r'<p className="text-sm text-neutral-dark/70">\s*Como está', 
     '<p className="text-xs text-neutral-dark/70">\n          Como está'),
    (r'<div className="text-lg">\{mood\.label\}</div>', 
     '<div className="text-sm">{mood.label}</div>'),
    (r'<div className="text-4xl mb-2">\{mood\.emoji\}</div>', 
     '<div className="text-3xl mb-2">{mood.emoji}</div>'),
    (r'<p className="text-sm text-neutral-dark/80">\s*🌟', 
     '<p className="text-xs text-neutral-dark/80">\n            🌟'),
    
    # RecordScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark mb-2">\s*Conte', 
     '<h3 className="text-base font-bold text-neutral-dark mb-2">\n        Conte'),
    (r'<p className="text-sm text-neutral-dark/70">\s*Aperte', 
     '<p className="text-xs text-neutral-dark/70">\n          Aperte'),
    (r'className="bg-cerrado-light rounded-xl p-4 text-sm text-neutral-dark/80 italic"', 
     'className="bg-cerrado-light rounded-xl p-3 text-xs text-neutral-dark/80 italic"'),
    (r'className="bg-neutral-dark/10 hover:bg-neutral-dark/20 px-4 py-2 rounded-full text-sm transition-colors">', 
     'className="bg-neutral-dark/10 hover:bg-neutral-dark/20 px-3 py-1.5 rounded-full text-xs transition-colors">'),
    (r'className="bg-ipe hover:bg-ipe-dark text-white px-6 py-2 rounded-full text-sm transition-colors">', 
     'className="bg-ipe hover:bg-ipe-dark text-white px-4 py-1.5 rounded-full text-xs transition-colors">'),
    
    # TimelineScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark">Suas Memórias</h3>', 
     '<h3 className="text-base font-bold text-neutral-dark">Suas Memórias</h3>'),
    (r'<p className="text-sm text-neutral-dark/60">\s*\{mem\.count\}', 
     '<p className="text-xs text-neutral-dark/60">\n                {mem.count}'),
    (r'className="w-full bg-gradient-to-r from-ipe to-ipe-dark text-white py-3 rounded-xl font-medium shadow-lg hover:opacity-90 transition-opacity">', 
     'className="w-full bg-gradient-to-r from-ipe to-ipe-dark text-white py-2 rounded-xl font-medium text-sm shadow-lg hover:opacity-90 transition-opacity">'),
    
    # MemoryDetailScreen
    (r'<h4 className="font-bold text-lg text-neutral-dark">Infância</h4>', 
     '<h4 className="font-bold text-base text-neutral-dark">Infância</h4>'),
    (r'<p className="text-sm text-neutral-dark/60">Gravado em', 
     '<p className="text-xs text-neutral-dark/60">Gravado em'),
    (r'<h3 className="font-bold text-2xl text-neutral-dark mb-2">\s*Festas', 
     '<h3 className="font-bold text-lg text-neutral-dark mb-2">\n          Festas'),
    (r'<p className="text-lg text-neutral-dark/80 leading-relaxed mb-4">', 
     '<p className="text-sm text-neutral-dark/80 leading-relaxed mb-3">'),
    (r'className="flex-1 bg-ipe/10 text-ipe py-2 rounded-lg text-base font-medium flex items-center justify-center gap-2">', 
     'className="flex-1 bg-ipe/10 text-ipe py-1.5 rounded-lg text-sm font-medium flex items-center justify-center gap-1.5">'),
    (r'className="flex-1 bg-neutral-dark/10 text-neutral-dark py-2 rounded-lg text-base font-medium">', 
     'className="flex-1 bg-neutral-dark/10 text-neutral-dark py-1.5 rounded-lg text-sm font-medium">'),
    (r'<div className="bg-cerrado-light/30 rounded-xl p-4 text-base">', 
     '<div className="bg-cerrado-light/30 rounded-xl p-3 text-sm">'),
    (r'<p className="font-medium text-lg text-neutral-dark mb-2">💡', 
     '<p className="font-medium text-sm text-neutral-dark mb-2">💡'),
    (r'<p className="text-base text-neutral-dark/80">\s*Que tal', 
     '<p className="text-sm text-neutral-dark/80">\n          Que tal'),
    
    # CirclesScreen
    (r'<h3 className="text-xl font-bold text-neutral-dark">Meus Círculos</h3>', 
     '<h3 className="text-base font-bold text-neutral-dark">Meus Círculos</h3>'),
    (r'<p className="text-sm text-neutral-dark/60 flex items-center gap-1">', 
     '<p className="text-xs text-neutral-dark/60 flex items-center gap-1">'),
    (r'<span className="text-xs bg-green-100', 
     '<span className="text-[10px] bg-green-100'),
    (r'className="w-full bg-white border-2 border-ipe text-ipe py-3 rounded-xl font-medium hover:bg-ipe/10 transition-colors">', 
     'className="w-full bg-white border-2 border-ipe text-ipe py-2 rounded-xl font-medium text-sm hover:bg-ipe/10 transition-colors">'),
    
    # CircleFeedScreen
    (r'<h3 className="font-bold text-xl flex items-center gap-2">', 
     '<h3 className="font-bold text-base flex items-center gap-2">'),
    (r'<span className="text-2xl">🍲</span>', 
     '<span className="text-xl">🍲</span>'),
    (r'<h4 className="font-bold text-neutral-dark text-lg">Dona Ana</h4>', 
     '<h4 className="font-bold text-neutral-dark text-base">Dona Ana</h4>'),
    (r'<h4 className="font-bold text-neutral-dark text-lg">Seu João</h4>', 
     '<h4 className="font-bold text-neutral-dark text-base">Seu João</h4>'),
    (r'<p className="text-base text-neutral-dark/60">Há 2 horas</p>', 
     '<p className="text-sm text-neutral-dark/60">Há 2 horas</p>'),
    (r'<p className="text-base text-neutral-dark/60">Ontem</p>', 
     '<p className="text-sm text-neutral-dark/60">Ontem</p>'),
    (r'<p className="text-lg text-neutral-dark/80 mb-3 leading-relaxed">', 
     '<p className="text-sm text-neutral-dark/80 mb-3 leading-relaxed">'),
    (r'className="flex items-center gap-1 text-ipe text-base font-medium">', 
     'className="flex items-center gap-1 text-ipe text-sm font-medium">'),
    (r'className="flex items-center gap-1 text-neutral-dark/60 text-base font-medium">', 
     'className="flex items-center gap-1 text-neutral-dark/60 text-sm font-medium">'),
    
    # EventsScreen
    (r'<h3 className="text-2xl font-bold text-neutral-dark">Eventos Próximos</h3>', 
     '<h3 className="text-base font-bold text-neutral-dark">Eventos Próximos</h3>'),
    (r'<h4 className="font-bold text-lg text-neutral-dark">Oficina de Violão</h4>', 
     '<h4 className="font-bold text-base text-neutral-dark">Oficina de Violão</h4>'),
    (r'<h4 className="font-bold text-lg text-neutral-dark">Dança de Salão</h4>', 
     '<h4 className="font-bold text-base text-neutral-dark">Dança de Salão</h4>'),
    (r'<p className="text-base text-neutral-dark/60">\s*Centro de Convivência', 
     '<p className="text-sm text-neutral-dark/60">\n              Centro de Convivência'),
    (r'<p className="text-base text-neutral-dark/60">Parque Vaca Brava</p>', 
     '<p className="text-sm text-neutral-dark/60">Parque Vaca Brava</p>'),
    (r'className="bg-cerrado text-cerrado-dark text-sm px-2 py-1 rounded-full font-medium">', 
     'className="bg-cerrado text-cerrado-dark text-xs px-1.5 py-0.5 rounded-full font-medium">'),
    (r'className="bg-ipe-light text-ipe-dark text-sm px-2 py-1 rounded-full font-medium">', 
     'className="bg-ipe-light text-ipe-dark text-xs px-1.5 py-0.5 rounded-full font-medium">'),
    (r'className="flex gap-3 text-sm text-neutral-dark/60 mb-3">', 
     'className="flex gap-2 text-xs text-neutral-dark/60 mb-2">'),
    (r'className="w-full bg-ipe text-white py-3 rounded-lg font-medium text-lg hover:bg-ipe-dark transition-colors">', 
     'className="w-full bg-ipe text-white py-2 rounded-lg font-medium text-sm hover:bg-ipe-dark transition-colors">'),
    (r'className="w-full bg-white border-2 border-ipe text-ipe py-3 rounded-lg font-medium text-lg hover:bg-ipe/10 transition-colors">', 
     'className="w-full bg-white border-2 border-ipe text-ipe py-2 rounded-lg font-medium text-sm hover:bg-ipe/10 transition-colors">'),
    
    # NotificationsScreen
    (r'<h3 className="text-2xl font-bold text-neutral-dark">Notificações</h3>', 
     '<h3 className="text-base font-bold text-neutral-dark">Notificações</h3>'),
    (r'<h4 className="font-bold text-neutral-dark text-lg mb-2">', 
     '<h4 className="font-bold text-neutral-dark text-base mb-2">'),
    (r'<p className="text-base text-neutral-dark/70 mb-3">', 
     '<p className="text-sm text-neutral-dark/70 mb-2">'),
    (r'<p className="text-sm text-neutral-dark/50">\{notif\.time\}</p>', 
     '<p className="text-xs text-neutral-dark/50">{notif.time}</p>'),
    
    # ProfileScreen
    (r'<h3 className="font-bold text-xl mb-1">Maria Silva</h3>', 
     '<h3 className="font-bold text-base mb-1">Maria Silva</h3>'),
    (r'<p className="text-sm opacity-90">Membro desde', 
     '<p className="text-xs opacity-90">Membro desde'),
    (r'<div className="text-2xl font-bold text-cerrado">35</div>', 
     '<div className="text-lg font-bold text-cerrado">35</div>'),
    (r'<div className="text-2xl font-bold text-ipe">12</div>', 
     '<div className="text-lg font-bold text-ipe">12</div>'),
    (r'<div className="text-2xl font-bold text-wisdom">3</div>', 
     '<div className="text-lg font-bold text-wisdom">3</div>'),
    (r'<p className="text-xs text-neutral-dark/70">Memórias</p>', 
     '<p className="text-[10px] text-neutral-dark/70">Memórias</p>'),
    (r'<p className="text-xs text-neutral-dark/70">Amigos</p>', 
     '<p className="text-[10px] text-neutral-dark/70">Amigos</p>'),
    (r'<p className="text-xs text-neutral-dark/70">Círculos</p>', 
     '<p className="text-[10px] text-neutral-dark/70">Círculos</p>'),
    (r'<h4 className="font-bold text-neutral-dark mb-3 text-sm">', 
     '<h4 className="font-bold text-neutral-dark mb-2 text-xs">'),
    (r'className="w-full bg-neutral-dark/10 hover:bg-neutral-dark/20 text-neutral-dark py-3 rounded-xl font-medium transition-colors flex items-center justify-center gap-2">', 
     'className="w-full bg-neutral-dark/10 hover:bg-neutral-dark/20 text-neutral-dark py-2 rounded-xl font-medium text-sm transition-colors flex items-center justify-center gap-2">'),
    
    # Reduzir também padding e espaçamentos
    (r'className="space-y-4"', 'className="space-y-3"'),
    (r'className="bg-white rounded-2xl p-6 shadow-sm">', 
     'className="bg-white rounded-2xl p-4 shadow-sm">'),
    (r'className="bg-white rounded-xl p-4 shadow-sm">', 
     'className="bg-white rounded-xl p-3 shadow-sm">'),
    (r'className="bg-ipe text-white rounded-xl p-4">', 
     'className="bg-ipe text-white rounded-xl p-3">'),
    (r'pt-8 mb-4', 'pt-6 mb-3'),
    (r'mb-4', 'mb-3'),
    (r'mb-3', 'mb-2'),
    (r'gap-3', 'gap-2'),
    (r'gap-2', 'gap-1.5'),
    (r'py-4', 'py-3'),
    (r'py-3', 'py-2'),
    (r'py-2', 'py-1.5'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Todas as fontes reduzidas dentro do mockup!")
print("📱 Mockup ficará menor com conteúdo mais compacto")
print("🚀 Execute: npm run dev")
