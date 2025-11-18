#!/bin/bash

echo "🔄 Iniciando atualização completa para Pequi..."

# Verificar se a imagem existe
if [ ! -f "public/pequi.png" ]; then
    echo "❌ Erro: public/pequi.png não encontrado!"
    exit 1
fi

# 1. Criar/atualizar componente PequiIcon
echo "📦 Criando componente PequiIcon..."
cat > src/components/PequiIcon.tsx << 'EOF'
interface PequiIconProps {
  size?: number;
  className?: string;
}

export default function PequiIcon({ size = 32, className = "" }: PequiIconProps) {
  return (
    <img 
      src="/pequi.png" 
      alt="Pequi" 
      width={size} 
      height={size}
      className={`object-contain ${className}`}
    />
  );
}
EOF

# 2. Substituir "Sabichão" por "Pequi"
echo "✏️  Substituindo 'Sabichão' por 'Pequi'..."
find src -type f \( -name "*.tsx" -o -name "*.ts" \) -exec sed -i 's/Sabichão/Pequi/g' {} +

# 3. Atualizar Navbar.tsx
echo "📝 Atualizando Navbar.tsx..."
# Adicionar import
if ! grep -q "import PequiIcon" src/components/Navbar.tsx; then
    sed -i '/import { motion, AnimatePresence }/a import PequiIcon from "./PequiIcon";' src/components/Navbar.tsx
fi
# Substituir emoji
sed -i 's|<div className="text-3xl group-hover:scale-110 transition-transform">\n              🥭\n            </div>|<div className="group-hover:scale-110 transition-transform">\n              <PequiIcon size={32} />\n            </div>|' src/components/Navbar.tsx
# Fallback: substituição simples se a anterior não funcionar
sed -i 's/🥭/<PequiIcon size={32} \/>/g' src/components/Navbar.tsx
# Corrigir se ficou errado
sed -i 's|<div className="text-3xl group-hover:scale-110 transition-transform">|<div className="group-hover:scale-110 transition-transform">|' src/components/Navbar.tsx
sed -i '/group-hover:scale-110 transition-transform">$/,/<\/div>/{ /🥭/d; }' src/components/Navbar.tsx || true

# 4. Atualizar Hero.tsx com layout melhorado
echo "📝 Atualizando Hero.tsx com layout melhorado..."
# Adicionar import
if ! grep -q "import PequiIcon" src/components/Hero.tsx; then
    sed -i '/import { Heart, Users, Sparkles, MapPin }/a import PequiIcon from "./PequiIcon";' src/components/Hero.tsx
fi
# Substituir o card do Pequi com layout melhorado
cat > /tmp/hero_pequi_section.txt << 'HEROEOF'
              {/* Mascot Card - Pequi */}
              <div className="aspect-square bg-gradient-to-br from-cerrado to-cerrado-dark rounded-3xl shadow-2xl p-6 md:p-8 flex items-center justify-center transform rotate-3 hover:rotate-0 transition-all duration-300 hover:shadow-3xl">
                <div className="text-center text-white space-y-5 w-full">
                  {/* Imagem do Pequi - maior e melhor posicionada */}
                  <div className="flex justify-center mb-2">
                    <div className="relative">
                      <PequiIcon size={120} className="drop-shadow-lg" />
                    </div>
                  </div>
                  
                  {/* Nome */}
                  <div>
                    <p className="text-3xl md:text-4xl font-bold tracking-tight">Pequi</p>
                  </div>
                  
                  {/* Tagline */}
                  <div>
                    <p className="text-sm md:text-base opacity-90 font-medium">Seu companheiro digital</p>
                  </div>
                </div>
              </div>
HEROEOF

# Usar Python para substituição mais precisa
python3 << 'PYEOF'
import re

# Ler Hero.tsx
with open('src/components/Hero.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir a seção do card do Pequi
pattern = r'\{/\* Mascot.*?\n.*?<div className="text-center text-white space-y-4">.*?</div>\n.*?</div>\n.*?</div>'
replacement = '''{/* Mascot Card - Pequi */}
              <div className="aspect-square bg-gradient-to-br from-cerrado to-cerrado-dark rounded-3xl shadow-2xl p-6 md:p-8 flex items-center justify-center transform rotate-3 hover:rotate-0 transition-all duration-300 hover:shadow-3xl">
                <div className="text-center text-white space-y-5 w-full">
                  {/* Imagem do Pequi - maior e melhor posicionada */}
                  <div className="flex justify-center mb-2">
                    <div className="relative">
                      <PequiIcon size={120} className="drop-shadow-lg" />
                    </div>
                  </div>
                  
                  {/* Nome */}
                  <div>
                    <p className="text-3xl md:text-4xl font-bold tracking-tight">Pequi</p>
                  </div>
                  
                  {/* Tagline */}
                  <div>
                    <p className="text-sm md:text-base opacity-90 font-medium">Seu companheiro digital</p>
                  </div>
                </div>
              </div>'''

# Substituir usando regex multiline
content = re.sub(
    r'\{/\* Mascot Placeholder - Pequi \*/\}.*?<div className="text-sm opacity-90">Seu companheiro digital</p>\s*</div>\s*</div>',
    replacement,
    content,
    flags=re.DOTALL
)

# Garantir que PequiIcon está importado
if 'import PequiIcon' not in content and 'from "./PequiIcon"' not in content:
    content = content.replace(
        'import { Heart, Users, Sparkles, MapPin } from "lucide-react";',
        'import { Heart, Users, Sparkles, MapPin } from "lucide-react";\nimport PequiIcon from "./PequiIcon";'
    )

# Remover emojis 🥭 restantes
content = content.replace('🥭', '')

with open('src/components/Hero.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero.tsx atualizado!")
PYEOF

# 5. Atualizar AICompanion.tsx
echo "📝 Atualizando AICompanion.tsx..."
# Adicionar import
if ! grep -q "import PequiIcon" src/components/AICompanion.tsx; then
    sed -i '/import { useState }/a import PequiIcon from "./PequiIcon";' src/components/AICompanion.tsx
fi
# Substituir emojis
python3 << 'PYEOF'
import re

with open('src/components/AICompanion.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir emoji no header
content = re.sub(
    r'<div className="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center text-2xl">\s*🥭\s*</div>',
    '<div className="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center p-2">\n                        <PequiIcon size={24} />\n                      </div>',
    content
)

# Substituir emojis nas mensagens
content = re.sub(
    r'<div className="flex-shrink-0 w-8 h-8 bg-wisdom rounded-full flex items-center justify-center text-lg">\s*🥭\s*</div>',
    '<div className="flex-shrink-0 w-8 h-8 bg-wisdom rounded-full flex items-center justify-center p-1">\n                          <PequiIcon size={20} />\n                        </div>',
    content
)

# Garantir import
if 'import PequiIcon' not in content:
    content = content.replace(
        'import { useState } from "react";',
        'import { useState } from "react";\nimport PequiIcon from "./PequiIcon";'
    )

with open('src/components/AICompanion.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("AICompanion.tsx atualizado!")
PYEOF

# 6. Atualizar pitch/page.tsx
echo "📝 Atualizando pitch/page.tsx..."
python3 << 'PYEOF'
import re

with open('src/app/pitch/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir emojis por img tags
content = re.sub(
    r'<div className="text-8xl mb-8">🥭</div>',
    '<div className="flex justify-center mb-8">\n              <img src="/pequi.png" alt="Pequi" width={96} height={96} className="object-contain" />\n            </div>',
    content
)

content = re.sub(
    r'<div className="text-8xl mb-6">🥭</div>',
    '<div className="flex justify-center mb-6">\n                      <img src="/pequi.png" alt="Pequi" width={96} height={96} className="object-contain" />\n                    </div>',
    content
)

with open('src/app/pitch/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("pitch/page.tsx atualizado!")
PYEOF

# 7. Atualizar demo/page.tsx
echo "📝 Atualizando demo/page.tsx..."
python3 << 'PYEOF'
import re

with open('src/app/demo/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir emojis
content = re.sub(
    r'<div className="text-2xl">🥭</div>',
    '<img src="/pequi.png" alt="Pequi" width={24} height={24} className="object-contain" />',
    content
)

content = re.sub(
    r'<div className="text-6xl mb-4">🥭</div>',
    '<div className="flex justify-center pt-8 mb-4">\n          <img src="/pequi.png" alt="Pequi" width={64} height={64} className="object-contain" />\n        </div>',
    content
)

content = re.sub(
    r'<div className="text-3xl">🥭</div>',
    '<img src="/pequi.png" alt="Pequi" width={32} height={32} className="object-contain" />',
    content
)

content = re.sub(
    r'icon: "🥭",',
    'icon: <img src="/pequi.png" alt="Pequi" width={24} height={24} className="object-contain" />,',
    content
)

with open('src/app/demo/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("demo/page.tsx atualizado!")
PYEOF

# 8. Limpar cache
echo "🧹 Limpando cache..."
rm -rf .next

echo ""
echo "✅ Atualização completa concluída!"
echo ""
echo "📋 Próximos passos:"
echo "1. Execute: npm run dev"
echo "2. Limpe o cache do navegador (Ctrl+Shift+R)"
echo "3. Verifique se todas as imagens aparecem corretamente"
