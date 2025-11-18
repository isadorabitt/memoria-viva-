#!/bin/bash

echo "🔄 Ajustando cards para tamanho uniforme e menor..."

FILE="src/components/Features.tsx"

# Backup
cp "$FILE" "$FILE.backup"
echo "📦 Backup criado: $FILE.backup"

# Usar Python para fazer as alterações precisas
python3 << 'PYEOF'
import re

# Ler o arquivo
with open('src/components/Features.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remover propriedade "size" de todos os objetos do array
content = re.sub(r',\s*size:\s*"(?:large|medium|small)",?\s*', '', content)
content = re.sub(r'size:\s*"(?:large|medium|small)",?\s*', '', content)

# 2. Remover a definição de sizeClasses
content = re.sub(
    r'\s*const sizeClasses = \{[^}]+\};\s*\n',
    '',
    content
)

# 3. Remover auto-rows-fr do grid
content = content.replace(
    'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8 auto-rows-fr',
    'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6'
)

# 4. Remover a classe sizeClasses do className
content = re.sub(
    r'className=\{`\$\{sizeClasses\[feature\.size as keyof typeof sizeClasses\]\} group`\}',
    'className="group"',
    content
)

# 5. Ajustar padding dos cards (menor)
content = content.replace(
    'rounded-3xl p-6 md:p-8 lg:p-10',
    'rounded-2xl p-5 md:p-6'
)

# 6. Ajustar tamanho dos ícones (menor)
content = content.replace(
    'w-14 h-14 md:w-16 md:h-16',
    'w-12 h-12'
)
content = content.replace(
    'w-7 h-7 md:w-8 md:h-8',
    'w-6 h-6'
)

# 7. Ajustar tamanho dos títulos (menor)
content = content.replace(
    'text-xl md:text-2xl lg:text-3xl',
    'text-lg md:text-xl'
)

# 8. Ajustar tamanho das descrições
content = content.replace(
    'text-sm md:text-base',
    'text-sm'
)

# 9. Ajustar padding do header
content = content.replace(
    'py-20 md:py-28',
    'py-16 md:py-20'
)
content = content.replace(
    'mb-16 md:mb-20',
    'mb-12 md:mb-16'
)

# 10. Ajustar tamanho do header
content = content.replace(
    'text-4xl md:text-5xl lg:text-6xl',
    'text-3xl md:text-4xl lg:text-5xl'
)
content = content.replace(
    'text-lg md:text-xl',
    'text-base md:text-lg'
)
content = content.replace(
    'max-w-3xl',
    'max-w-2xl'
)

# 11. Ajustar mb-6 para mb-4 no ícone
content = content.replace(
    'mb-6 shadow-lg',
    'mb-4 shadow-md'
)
content = content.replace(
    'mb-6">',
    'mb-4">'
)

# 12. Ajustar mb-3 para mb-2 no título
content = content.replace(
    'mb-3 leading-tight',
    'mb-2 leading-tight'
)

# 13. Ajustar pt-4 para pt-3 no CTA
content = content.replace(
    'pt-4 border-t',
    'pt-3 border-t'
)

# 14. Remover animações complexas e simplificar
content = content.replace(
    'group-hover:-translate-y-2',
    ''
)
content = content.replace(
    'duration: 0.5,\n                  type: "spring",\n                  stiffness: 100',
    'duration: 0.4'
)
content = content.replace(
    'margin: "-100px"',
    'margin: "-50px"'
)

# 15. Simplificar botão CTA (remover motion.button, usar button normal)
content = content.replace(
    '<motion.button\n                      className={`${colors.text} ${colors.hover} font-semibold flex items-center gap-2 text-sm md:text-base group/btn transition-all`}\n                      whileHover={{ x: 5 }}\n                    >',
    '<button\n                      className={`${colors.text} ${colors.hover} font-medium flex items-center gap-2 text-sm group/btn transition-all`}\n                    >'
)
content = content.replace(
    '</motion.button>',
    '</button>'
)

# 16. Ajustar tamanho da seta
content = content.replace(
    'w-4 h-4',
    'w-3.5 h-3.5'
)

# 17. Ajustar sombras
content = content.replace(
    'shadow-md hover:shadow-2xl',
    'shadow-sm hover:shadow-lg'
)

# 18. Ajustar rounded-3xl para rounded-2xl no card
content = content.replace(
    'rounded-3xl p-6 md:p-8 lg:p-10 shadow-md',
    'rounded-2xl p-5 md:p-6 shadow-sm'
)

# Salvar
with open('src/components/Features.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Cards ajustados para tamanho uniforme e menor!")
print("  - Removidas propriedades 'size'")
print("  - Removida lógica de sizeClasses")
print("  - Todos os cards agora têm o mesmo tamanho")
print("  - Padding e tamanhos reduzidos")
PYEOF

# Limpar cache
echo "🧹 Limpando cache..."
rm -rf .next

echo ""
echo "✅ Correção concluída!"
echo "🚀 Execute: npm run dev"
