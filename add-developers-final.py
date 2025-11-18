#!/usr/bin/env python3
"""
Script para adicionar Isadora Bittencourt e Eder Veloso, remover links do Nicollas
"""

import re

file_path = "src/app/sobre/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Substituir título
content = re.sub(
    r'<h2 className="text-3xl font-bold text-neutral-dark">Desenvolvedor</h2>',
    '<h2 className="text-3xl font-bold text-neutral-dark">Desenvolvedores</h2>',
    content
)

# Substituir a seção completa do desenvolvedor
old_pattern = r'<div className="flex items-center gap-6">.*?</div>\s*</div>\s*</div>'

new_section = '''<div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {/* Nicollas Rezende */}
              <div className="flex flex-col items-center text-center">
                <div className="w-20 h-20 bg-gradient-to-br from-ipe to-ipe-dark rounded-full flex items-center justify-center text-white text-2xl font-bold mb-4">
                  NR
                </div>
                <h3 className="text-xl font-bold text-neutral-dark mb-1">
                  Nicollas Rezende
                </h3>
                <p className="text-neutral-dark/70">
                  Desenvolvedor Full Stack
                </p>
              </div>

              {/* Isadora Bittencourt */}
              <div className="flex flex-col items-center text-center">
                <div className="w-20 h-20 bg-gradient-to-br from-cerrado to-cerrado-dark rounded-full flex items-center justify-center text-white text-2xl font-bold mb-4">
                  IB
                </div>
                <h3 className="text-xl font-bold text-neutral-dark mb-1">
                  Isadora Bittencourt
                </h3>
                <p className="text-neutral-dark/70">
                  Desenvolvedora
                </p>
              </div>

              {/* Eder Veloso */}
              <div className="flex flex-col items-center text-center">
                <div className="w-20 h-20 bg-gradient-to-br from-wisdom to-wisdom-dark rounded-full flex items-center justify-center text-white text-2xl font-bold mb-4">
                  EV
                </div>
                <h3 className="text-xl font-bold text-neutral-dark mb-1">
                  Eder Veloso
                </h3>
                <p className="text-neutral-dark/70">
                  Desenvolvedor
                </p>
              </div>
            </div>
          </div>'''

# Substituir usando padrão mais específico
pattern = r'(<div className="flex items-center gap-6">)(.*?)(</div>\s*</div>\s*</div>)'

def replace_developer_section(match):
    return new_section

content = re.sub(
    r'<div className="flex items-center gap-6">.*?<div className="flex gap-3">.*?</div>.*?</div>.*?</div>.*?</div>',
    new_section,
    content,
    flags=re.DOTALL
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Desenvolvedores atualizados!")
print("👥 Adicionados: Isadora Bittencourt e Eder Veloso")
print("🔗 Links do Nicollas removidos")
print("🚀 Execute: npm run dev")
