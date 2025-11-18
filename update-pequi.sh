#!/bin/bash

echo "🔄 Iniciando atualização para Pequi..."

# 1. Criar componente PequiIcon
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

# 2. Substituir "Sabichão" por "Pequi" em todos os arquivos
echo "✏️  Substituindo 'Sabichão' por 'Pequi'..."
find src -type f \( -name "*.tsx" -o -name "*.ts" \) -exec sed -i 's/Sabichão/Pequi/g' {} +

# 3. Atualizar Navbar.tsx
echo "📝 Atualizando Navbar.tsx..."
sed -i 's|import { motion, AnimatePresence } from "framer-motion";|import { motion, AnimatePresence } from "framer-motion";\nimport PequiIcon from "./PequiIcon";|' src/components/Navbar.tsx
sed -i 's|<div className="text-3xl group-hover:scale-110 transition-transform">\n              🥭\n            </div>|<div className="group-hover:scale-110 transition-transform">\n              <PequiIcon size={32} />\n            </div>|' src/components/Navbar.tsx

# 4. Atualizar Hero.tsx
echo "📝 Atualizando Hero.tsx..."
sed -i 's|import { Heart, Users, Sparkles, MapPin } from "lucide-react";|import { Heart, Users, Sparkles, MapPin } from "lucide-react";\nimport PequiIcon from "./PequiIcon";|' src/components/Hero.tsx
sed -i 's|{/\* Mascot Placeholder - Pequi \*/}|{/\* Mascot Placeholder - Pequi \*/}|' src/components/Hero.tsx
sed -i 's|<div className="text-8xl">🥭</div>|<div className="flex justify-center">\n                    <PequiIcon size={96} />\n                  </div>|' src/components/Hero.tsx

# 5. Atualizar AICompanion.tsx
echo "📝 Atualizando AICompanion.tsx..."
sed -i 's|import { useState } from "react";|import { useState } from "react";\nimport PequiIcon from "./PequiIcon";|' src/components/AICompanion.tsx
sed -i 's|<div className="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center text-2xl">\n                        🥭\n                      </div>|<div className="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center p-2">\n                        <PequiIcon size={24} />\n                      </div>|' src/components/AICompanion.tsx
sed -i 's|<div className="flex-shrink-0 w-8 h-8 bg-wisdom rounded-full flex items-center justify-center text-lg">\n                          🥭\n                        </div>|<div className="flex-shrink-0 w-8 h-8 bg-wisdom rounded-full flex items-center justify-center p-1">\n                          <PequiIcon size={20} />\n                        </div>|g' src/components/AICompanion.tsx

# 6. Atualizar pitch/page.tsx
echo "📝 Atualizando pitch/page.tsx..."
sed -i 's|import Link from "next/link";|import Link from "next/link";\nimport Image from "next/image";|' src/app/pitch/page.tsx
sed -i 's|<div className="text-8xl mb-8">🥭</div>|<div className="flex justify-center mb-8">\n              <img src="/pequi.png" alt="Pequi" width={96} height={96} className="object-contain" />\n            </div>|' src/app/pitch/page.tsx
sed -i 's|<div className="text-8xl mb-6">🥭</div>|<div className="flex justify-center mb-6">\n                      <img src="/pequi.png" alt="Pequi" width={96} height={96} className="object-contain" />\n                    </div>|' src/app/pitch/page.tsx

# 7. Atualizar demo/page.tsx
echo "📝 Atualizando demo/page.tsx..."
sed -i 's|<div className="text-2xl">🥭</div>|<img src="/pequi.png" alt="Pequi" width={24} height={24} className="object-contain" />|' src/app/demo/page.tsx
sed -i 's|<div className="text-6xl mb-4">🥭</div>|<div className="flex justify-center pt-8 mb-4">\n          <img src="/pequi.png" alt="Pequi" width={64} height={64} className="object-contain" />\n        </div>|' src/app/demo/page.tsx
sed -i 's|<div className="text-3xl">🥭</div>|<img src="/pequi.png" alt="Pequi" width={32} height={32} className="object-contain" />|' src/app/demo/page.tsx
sed -i 's|icon: "🥭",|icon: <img src="/pequi.png" alt="Pequi" width={24} height={24} className="object-contain" />,|' src/app/demo/page.tsx

# 8. Limpar cache do Next.js
echo "🧹 Limpando cache..."
rm -rf .next

echo "✅ Atualização concluída!"
echo ""
echo "📋 Próximos passos:"
echo "1. Verifique se a imagem está em public/pequi.png"
echo "2. Execute: npm run dev"
echo "3. Limpe o cache do navegador (Ctrl+Shift+R)"
