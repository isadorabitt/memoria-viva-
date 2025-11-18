#!/usr/bin/env python3
"""
Script para criar página de Video Demo e adicionar no menu
"""

import os
import re

# 1. Adicionar no Navbar
navbar_path = "src/components/Navbar.tsx"
with open(navbar_path, "r", encoding="utf-8") as f:
    navbar_content = f.read()

# Adicionar link no menu - encontrar onde está o array navLinks
if 'href: "/video-demo"' not in navbar_content:
    navbar_content = re.sub(
        r'(\{ href: "/demo", label: "Demo Interativa" \},)',
        r'\1\n  { href: "/video-demo", label: "Video Demo" },',
        navbar_content
    )

with open(navbar_path, "w", encoding="utf-8") as f:
    f.write(navbar_content)

# 2. Criar diretório e página
os.makedirs("src/app/video-demo", exist_ok=True)

video_demo_content = '''"use client";

import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import {
  Mic,
  BookOpen,
  Heart,
  Bell,
  User,
  Users,
  MapPin,
  Play,
  Pause,
} from "lucide-react";
import Link from "next/link";

const demoSteps = [
  { 
    id: 1, 
    title: "Boas-vindas com Pequi", 
    description: "Ao abrir o app, o Pequi te dá boas-vindas personalizadas e pergunta como você está.",
    screen: "welcome", 
    icon: Heart, 
    duration: 3000 
  },
  { 
    id: 2, 
    title: "Check-in Emocional", 
    description: "A IA acompanha seu humor diariamente. Escolha como está se sentindo e receba sugestões personalizadas.",
    screen: "mood", 
    icon: Heart, 
    duration: 3000 
  },
  { 
    id: 3, 
    title: "Gravação de Memórias", 
    description: "Aperte o botão e conte suas histórias. A IA organiza tudo automaticamente por temas e períodos.",
    screen: "record", 
    icon: Mic, 
    duration: 4000 
  },
  { 
    id: 4, 
    title: "Linha do Tempo", 
    description: "Veja suas memórias organizadas em capítulos: Infância, Juventude, Família, Trabalho...",
    screen: "timeline", 
    icon: BookOpen, 
    duration: 3000 
  },
  { 
    id: 5, 
    title: "Visualizar Memória", 
    description: "Leia e ouça suas histórias gravadas. Adicione fotos e compartilhe com familiares.",
    screen: "memory-detail", 
    icon: BookOpen, 
    duration: 3000 
  },
  { 
    id: 6, 
    title: "Círculos de Sabedoria", 
    description: "Entre em grupos com pessoas que compartilham seus interesses. Comente por voz ou texto.",
    screen: "circles", 
    icon: Users, 
    duration: 3000 
  },
  { 
    id: 7, 
    title: "Dentro do Círculo", 
    description: "Veja publicações dos membros, curta e comente. Tudo com interface simples e acessível.",
    screen: "circle-feed", 
    icon: Users, 
    duration: 3000 
  },
  { 
    id: 8, 
    title: "Eventos Próximos", 
    description: "Descubra atividades perto de você. Integrado com Goiás Social, CRAS e Centros de Convivência.",
    screen: "events", 
    icon: MapPin, 
    duration: 3000 
  },
  { 
    id: 9, 
    title: "Notificações", 
    description: "Receba lembretes de eventos, mensagens de amigos e sugestões do Pequi.",
    screen: "notifications", 
    icon: Bell, 
    duration: 3000 
  },
  { 
    id: 10, 
    title: "Perfil Pessoal", 
    description: "Veja suas conquistas, estatísticas de bem-estar e personalize suas preferências.",
    screen: "profile", 
    icon: User, 
    duration: 3000 
  },
];

export default function VideoDemoPage() {
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isPaused, setIsPaused] = useState(false);

  useEffect(() => {
    if (!isPlaying || isPaused) return;

    const step = demoSteps[currentStep];
    const timer = setTimeout(() => {
      if (currentStep < demoSteps.length - 1) {
        setCurrentStep(currentStep + 1);
      } else {
        setIsPlaying(false);
        setCurrentStep(0);
      }
    }, step.duration);

    return () => clearTimeout(timer);
  }, [currentStep, isPlaying, isPaused]);

  const togglePlay = () => {
    if (isPlaying) {
      setIsPaused(!isPaused);
    } else {
      setIsPlaying(true);
      setIsPaused(false);
    }
  };

  const reset = () => {
    setCurrentStep(0);
    setIsPlaying(false);
    setIsPaused(false);
  };

  const step = demoSteps[currentStep];

  return (
    <main className="min-h-screen bg-gradient-to-br from-neutral-light via-white to-cerrado-light/30 pt-20 pb-12 overflow-x-hidden">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          className="text-center mb-12 px-2 sm:px-4 overflow-visible mt-8"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-neutral-dark mb-4 break-words overflow-visible whitespace-normal">
            Video <span className="text-ipe-dark">Demo</span>
          </h1>
          <p className="text-lg sm:text-xl text-neutral-dark/70 max-w-2xl mx-auto px-2">
            Assista a demonstração automática de todas as funcionalidades
          </p>
        </motion.div>

        {/* Controls */}
        <div className="flex justify-center items-center gap-4 mb-8">
          <button
            onClick={togglePlay}
            className="bg-gradient-to-r from-ipe to-ipe-dark text-white px-8 py-3 rounded-full font-medium hover:opacity-90 transition-opacity shadow-lg flex items-center gap-2"
          >
            {isPaused ? (
              <>
                <Play className="w-5 h-5" />
                Continuar
              </>
            ) : isPlaying ? (
              <>
                <Pause className="w-5 h-5" />
                Pausar
              </>
            ) : (
              <>
                <Play className="w-5 h-5" />
                Iniciar Demo
              </>
            )}
          </button>
          <button
            onClick={reset}
            className="bg-white border-2 border-neutral-dark/20 text-neutral-dark px-6 py-3 rounded-full font-medium hover:border-ipe hover:text-ipe transition-colors"
          >
            Reiniciar
          </button>
        </div>

        {/* Progress */}
        <div className="max-w-4xl mx-auto mb-8">
          <div className="flex items-center justify-center gap-2 mb-2">
            <span className="text-sm text-neutral-dark/60">
              Passo {currentStep + 1} de {demoSteps.length}
            </span>
            <span className="text-sm text-neutral-dark/60">• {step.title}</span>
          </div>
          <div className="w-full bg-neutral-dark/10 rounded-full h-2">
            <motion.div
              className="bg-gradient-to-r from-ipe to-ipe-dark h-full"
              initial={{ width: "0%" }}
              animate={{
                width: isPlaying && !isPaused
                  ? `${((currentStep + 1) / demoSteps.length) * 100}%`
                  : `${(currentStep / demoSteps.length) * 100}%`,
              }}
              transition={{ duration: 0.3 }}
            />
          </div>
        </div>

        {/* Step Info */}
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-2xl p-8 shadow-lg text-center">
            <div className="flex items-center justify-center gap-4 mb-4">
              <div className="w-16 h-16 bg-gradient-to-br from-cerrado to-cerrado-dark rounded-2xl flex items-center justify-center">
                <step.icon className="w-8 h-8 text-white" />
              </div>
              <div>
                <p className="text-sm text-neutral-dark/60 font-medium">
                  Passo {step.id} de {demoSteps.length}
                </p>
                <h2 className="text-3xl font-bold text-neutral-dark">
                  {step.title}
                </h2>
              </div>
            </div>
            <p className="text-xl text-neutral-dark/80 leading-relaxed mb-6">
              {step.description}
            </p>
            <Link
              href={`/demo`}
              className="inline-flex items-center gap-2 bg-gradient-to-r from-ipe to-ipe-dark text-white px-6 py-3 rounded-full font-medium hover:opacity-90 transition-opacity shadow-lg"
            >
              Ver Demo Interativa Completa
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
}
'''

with open("src/app/video-demo/page.tsx", "w", encoding="utf-8") as f:
    f.write(video_demo_content)

print("✅ Video Demo criado!")
print("📱 Nova página: /video-demo")
print("🚀 Execute: npm run dev")
