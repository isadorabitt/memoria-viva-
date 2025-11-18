#!/bin/bash

echo "🔄 Substituindo 'Acolhe' por 'Pequi' em todos os arquivos..."

# Substituir em todos os arquivos .tsx e .ts
find src -type f \( -name "*.tsx" -o -name "*.ts" \) -exec sed -i 's/Acolhe/Pequi/g' {} +

# Substituições específicas para manter contexto correto
# 1. AICompanion.tsx - "Conheça o Acolhe" -> "Conheça o Pequi"
# 2. AICompanion.tsx - "Conversar com Acolhe" -> "Conversar com Pequi"
# 3. demo/page.tsx - "Boas-vindas com Acolhe" -> "Boas-vindas com Pequi"
# 4. demo/page.tsx - "IA Acolhe" -> "Pequi"
# 5. demo/page.tsx - "Acolhe tem uma sugestão" -> "Pequi tem uma sugestão"
# 6. pitch/page.tsx - "IA Acolhe" -> "Pequi"

# Limpar cache
rm -rf .next

echo ""
echo "✅ Substituição concluída!"
echo "  - Todas as ocorrências de 'Acolhe' foram substituídas por 'Pequi'"
echo ""
echo "🚀 Execute: npm run dev"
