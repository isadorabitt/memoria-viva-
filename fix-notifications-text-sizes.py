#!/usr/bin/env python3
"""
Script para aumentar apenas textos na NotificationsScreen, manter elementos iguais
"""

import re

file_path = "src/app/demo/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Aumentar apenas textos, manter elementos iguais
replacements = [
    # Título principal
    (r'<h3 className="text-xl font-bold text-neutral-dark">Notificações</h3>', 
     '<h3 className="text-2xl font-bold text-neutral-dark">Notificações</h3>'),
    
    # Títulos das notificações
    (r'<h4 className="font-bold text-neutral-dark text-sm mb-1">', 
     '<h4 className="font-bold text-neutral-dark text-lg mb-2">'),
    
    # Mensagens das notificações
    (r'<p className="text-xs text-neutral-dark/70 mb-2">', 
     '<p className="text-base text-neutral-dark/70 mb-3">'),
    
    # Tempo das notificações
    (r'<p className="text-xs text-neutral-dark/50">\{notif\.time\}</p>', 
     '<p className="text-sm text-neutral-dark/50">{notif.time}</p>'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Textos aumentados na NotificationsScreen!")
print("📏 Elementos mantidos no mesmo tamanho")
print("📝 Apenas textos aumentados para melhor leitura")
print("🚀 Execute: npm run dev")
