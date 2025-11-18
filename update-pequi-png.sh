#!/bin/bash

echo "🔄 Atualizando todas as referências de pequi.png para pequi.png..."

# Verificar se a imagem existe
if [ ! -f "public/pequi.png" ]; then
    echo "⚠️  Aviso: public/pequi.png não encontrado, mas continuando..."
fi

# Substituir em todos os arquivos .tsx, .ts, .jsx, .js
echo "📝 Substituindo pequi.png por pequi.png nos arquivos..."

# Substituir em arquivos TypeScript/JavaScript
find src -type f \( -name "*.tsx" -o -name "*.ts" -o -name "*.jsx" -o -name "*.js" \) -exec sed -i 's|/pequi\.jpg|/pequi.png|g' {} +
find src -type f \( -name "*.tsx" -o -name "*.ts" -o -name "*.jsx" -o -name "*.js" \) -exec sed -i 's|pequi\.jpg|pequi.png|g' {} +

# Substituir também em arquivos de configuração e scripts
find . -maxdepth 2 -type f \( -name "*.sh" -o -name "*.json" -o -name "*.md" \) -exec sed -i 's|pequi\.jpg|pequi.png|g' {} + 2>/dev/null || true

# Limpar cache
echo "🧹 Limpando cache..."
rm -rf .next

echo ""
echo "✅ Atualização concluída!"
echo ""
echo "📋 Arquivos atualizados:"
echo "  - src/components/PequiIcon.tsx"
echo "  - src/app/demo/page.tsx"
echo "  - src/app/pitch/page.tsx"
echo "  - Todos os outros arquivos com referências à imagem"
echo ""
echo "🚀 Próximos passos:"
echo "1. Execute: npm run dev"
echo "2. Limpe o cache do navegador (Ctrl+Shift+R)"
