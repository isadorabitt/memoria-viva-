#!/bin/bash

echo "🔄 Corrigindo TODOS os cards para tamanho uniforme e menor..."

FILE="src/components/Features.tsx"

# Backup
cp "$FILE" "$FILE.backup"
echo "📦 Backup criado: $FILE.backup"

# Reescrever o arquivo completo
cat > "$FILE" << 'FEATURESEOF'
"use client";

import { motion } from "framer-motion";
import { BookOpen, Users, Bot, Map, Mic, Heart, ArrowRight } from "lucide-react";

const features = [
  {
    icon: BookOpen,
    title: "Memória Viva",
    description: "Grave suas histórias por voz e crie seu Livro da Vida digital com IA",
    color: "cerrado",
  },
  {
    icon: Users,
    title: "Círculos de Sabedoria",
    description: "Conecte-se com pessoas que compartilham seus interesses",
    color: "ipe",
  },
  {
    icon: Bot,
    title: "Pequi",
    description: "Companheiro digital que aprende com você e oferece suporte emocional",
    color: "wisdom",
  },
  {
    icon: Map,
    title: "Mapa de Eventos",
    description: "Descubra atividades e eventos perto de você em Goiás",
    color: "ipe",
  },
  {
    icon: Mic,
    title: "Controle por Voz",
    description: "Navegue inteiramente por comandos de voz, sem complexidade",
    color: "cerrado",
  },
  {
    icon: Heart,
    title: "Bem-Estar Mental",
    description: "Check-ins emocionais e acompanhamento do seu humor",
    color: "wisdom",
  },
];

export default function Features() {
  return (
    <section className="py-16 md:py-20 bg-gradient-to-br from-neutral-light via-white to-cerrado-light/20 relative overflow-hidden">
      {/* Background decorations */}
      <div className="absolute top-0 left-0 w-1/3 h-full bg-gradient-to-r from-ipe-light/10 to-transparent opacity-50" />
      <div className="absolute bottom-0 right-0 w-1/2 h-1/2 bg-gradient-to-tl from-wisdom-light/10 to-transparent opacity-50" />

      <div className="container mx-auto px-4 md:px-6 relative z-10">
        {/* Header Section */}
        <motion.div
          className="text-center mb-12 md:mb-16"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-neutral-dark mb-3 leading-tight">
            Funcionalidades <span className="text-ipe-dark">Principais</span>
          </h2>
          <p className="text-base md:text-lg text-neutral-dark/70 max-w-2xl mx-auto">
            Um ecossistema completo de tecnologia afetiva para o bem-estar de pessoas 60+
          </p>
        </motion.div>

        {/* Grid uniforme - TODOS os cards EXATAMENTE do mesmo tamanho */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
          {features.map((feature, index) => {
            const colorClasses = {
              cerrado: {
                icon: "from-cerrado-light to-cerrado",
                text: "text-cerrado-dark",
                hover: "hover:text-cerrado",
              },
              ipe: {
                icon: "from-ipe-light to-ipe",
                text: "text-ipe-dark",
                hover: "hover:text-ipe",
              },
              wisdom: {
                icon: "from-wisdom-light to-wisdom",
                text: "text-wisdom-dark",
                hover: "hover:text-wisdom",
              },
            };

            const colors = colorClasses[feature.color as keyof typeof colorClasses];

            return (
              <motion.div
                key={index}
                className="group"
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-50px" }}
                transition={{ 
                  delay: index * 0.08,
                  duration: 0.4,
                }}
              >
                <div className="bg-white rounded-2xl p-5 md:p-6 shadow-sm hover:shadow-lg transition-all duration-300 h-full flex flex-col border border-neutral-200/50 hover:border-neutral-300">
                  {/* Icon Section */}
                  <div className="mb-4">
                    <div
                      className={`w-12 h-12 rounded-xl bg-gradient-to-br ${colors.icon} flex items-center justify-center mb-4 shadow-md group-hover:scale-105 transition-transform duration-300`}
                    >
                      <feature.icon className="w-6 h-6 text-white" />
                    </div>

                    <h3 className="text-lg md:text-xl font-bold text-neutral-dark mb-2 leading-tight">
                      {feature.title}
                    </h3>

                    <p className="text-sm text-neutral-dark/70 leading-relaxed">
                      {feature.description}
                    </p>
                  </div>

                  {/* CTA Button */}
                  <div className="mt-auto pt-3 border-t border-neutral-100">
                    <button
                      className={`${colors.text} ${colors.hover} font-medium flex items-center gap-2 text-sm group/btn transition-all`}
                    >
                      Saiba mais
                      <ArrowRight className="w-3.5 h-3.5 group-hover/btn:translate-x-1 transition-transform" />
                    </button>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </div>

        {/* CTA Section */}
        <motion.div
          className="mt-16 md:mt-20"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <div className="bg-gradient-to-r from-ipe via-ipe-dark to-ipe rounded-2xl p-8 md:p-10 shadow-xl relative overflow-hidden">
            <div className="relative z-10 text-center">
              <h3 className="text-2xl md:text-3xl font-bold mb-3 md:mb-4 leading-tight">
                Pronto para transformar o envelhecimento em Goiás?
              </h3>
              <p className="text-base md:text-lg mb-6 md:mb-8 opacity-95 max-w-2xl mx-auto">
                10.000 idosos incluídos digitalmente no primeiro ano
              </p>
              <motion.button
                className="bg-white text-ipe-dark px-6 py-3 md:px-8 md:py-4 rounded-full text-base font-semibold hover:bg-cerrado hover:text-white transition-all duration-300 shadow-lg hover:shadow-xl hover:scale-105"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Participar do Projeto
              </motion.button>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
FEATURESEOF

# Limpar cache
echo "🧹 Limpando cache..."
rm -rf .next

echo ""
echo "✅ Arquivo reescrito completamente!"
echo "  ✓ Removidas TODAS as propriedades 'size'"
echo "  ✓ Removida TODA a lógica de sizeClasses"
echo "  ✓ Removido auto-rows-fr"
echo "  ✓ Todos os cards têm EXATAMENTE o mesmo tamanho"
echo "  ✓ Grid uniforme sem col-span ou row-span"
echo "  ✓ Padding reduzido (p-5 md:p-6)"
echo "  ✓ Tamanhos menores e alinhados"
echo ""
echo "🚀 Execute: npm run dev"
