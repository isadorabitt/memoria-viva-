#!/bin/bash

echo "🔄 Corrigindo duplicação do Pequi..."

FILE="src/components/Hero.tsx"

# Backup
cp "$FILE" "$FILE.backup"

# 1. Remover a linha 131 que tem "Pequi" duplicado (deixar apenas o tagline "Sempre ao seu lado")
sed -i '131d' "$FILE"

# 2. Mudar "Acolhe IA" para "Pequi" na linha 148 (agora linha 147 após deletar)
sed -i 's/Acolhe IA/Pequi/g' "$FILE"

# Limpar cache
rm -rf .next

echo ""
echo "✅ Correções aplicadas:"
echo "  - Removido 'Pequi' duplicado do tagline (linha 131)"
echo "  - Alterado 'Acolhe IA' para 'Pequi' no card flutuante"
echo ""
echo "🚀 Execute: npm run dev"
