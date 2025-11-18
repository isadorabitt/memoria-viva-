#!/bin/bash

echo "🔄 Corrigindo cards de forma simples e direta..."

FILE="src/components/Features.tsx"

# Backup
cp "$FILE" "$FILE.backup"

# 1. Remover propriedades size de cada objeto
sed -i '/size: "large",/d' "$FILE"
sed -i '/size: "medium",/d' "$FILE"
sed -i '/size: "small",/d' "$FILE"

# 2. Remover o bloco sizeClasses completo (linhas 99-103)
sed -i '99,103d' "$FILE"

# 3. Substituir a linha que usa sizeClasses
sed -i 's/className={`${sizeClasses\[feature\.size as keyof typeof sizeClasses\]} group`}/className="group"/' "$FILE"

# 4. Remover auto-rows-fr
sed -i 's/ gap-6 md:gap-8 auto-rows-fr/ gap-4 md:gap-6/' "$FILE"

# 5. Reduzir padding
sed -i 's/rounded-3xl p-6 md:p-8 lg:p-10/rounded-2xl p-5 md:p-6/' "$FILE"

# 6. Reduzir tamanho dos ícones
sed -i 's/w-14 h-14 md:w-16 md:h-16/w-12 h-12/' "$FILE"
sed -i 's/w-7 h-7 md:w-8 md:h-8/w-6 h-6/' "$FILE"

# 7. Reduzir tamanho dos títulos
sed -i 's/text-xl md:text-2xl lg:text-3xl/text-lg md:text-xl/' "$FILE"

# 8. Reduzir tamanho das descrições
sed -i 's/text-sm md:text-base/text-sm/' "$FILE"

# 9. Reduzir espaçamentos
sed -i 's/mb-6 shadow-lg/mb-4 shadow-md/' "$FILE"
sed -i 's/mb-6">/mb-4">/' "$FILE"
sed -i 's/mb-3 leading-tight/mb-2 leading-tight/' "$FILE"
sed -i 's/pt-4 border-t/pt-3 border-t/' "$FILE"

# 10. Reduzir padding do header
sed -i 's/py-20 md:py-28/py-16 md:py-20/' "$FILE"
sed -i 's/mb-16 md:mb-20/mb-12 md:mb-16/' "$FILE"

# 11. Reduzir tamanho do header
sed -i 's/text-4xl md:text-5xl lg:text-6xl/text-3xl md:text-4xl lg:text-5xl/' "$FILE"
sed -i 's/text-lg md:text-xl/text-base md:text-lg/' "$FILE"
sed -i 's/max-w-3xl/max-w-2xl/' "$FILE"

# 12. Simplificar sombras
sed -i 's/shadow-md hover:shadow-2xl/shadow-sm hover:shadow-lg/' "$FILE"

# 13. Remover animações complexas
sed -i 's/group-hover:-translate-y-2//' "$FILE"
sed -i 's/duration: 0.5,$/duration: 0.4,/' "$FILE"
sed -i '/type: "spring",/d' "$FILE"
sed -i '/stiffness: 100/d' "$FILE"
sed -i 's/margin: "-100px"/margin: "-50px"/' "$FILE"

# 14. Simplificar botão
sed -i 's/font-semibold flex items-center gap-2 text-sm md:text-base/font-medium flex items-center gap-2 text-sm/' "$FILE"
sed -i 's/w-4 h-4/w-3.5 h-3.5/' "$FILE"

# Limpar cache
rm -rf .next

echo ""
echo "✅ Correções aplicadas!"
echo "🚀 Execute: npm run dev"
