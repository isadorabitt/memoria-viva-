#!/bin/bash

echo "🔄 Corrigindo duplicação do nome Pequi..."

# Arquivo a ser corrigido
FILE="src/components/Hero.tsx"

# Verificar se o arquivo existe
if [ ! -f "$FILE" ]; then
    echo "❌ Erro: $FILE não encontrado!"
    exit 1
fi

# Criar backup
cp "$FILE" "$FILE.backup"
echo "📦 Backup criado: $FILE.backup"

# Usar Python para fazer as correções precisas
python3 << 'PYEOF'
import re

# Ler o arquivo
with open('src/components/Hero.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Corrigir linha 131: remover "Pequi" duplicado e deixar apenas o tagline
# Procurar pela seção do tagline que tem "Pequi" duplicado
content = re.sub(
    r'(\{/\* Tagline \*/\}\s*<div>\s*)<p className="text-sm font-medium text-neutral-dark">Pequi</p>\s*',
    r'\1',
    content
)

# 2. Mudar "Acolhe IA" para "Pequi" no card flutuante
content = content.replace(
    '<p className="text-sm font-medium text-neutral-dark">Acolhe IA</p>',
    '<p className="text-sm font-medium text-neutral-dark">Pequi</p>'
)

# Salvar
with open('src/components/Hero.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Correções aplicadas!")
print("  - Removido 'Pequi' duplicado do tagline")
print("  - Alterado 'Acolhe IA' para 'Pequi' no card flutuante")
PYEOF

# Limpar cache
echo "🧹 Limpando cache..."
rm -rf .next

echo ""
echo "✅ Correção concluída!"
echo "🚀 Execute: npm run dev"
