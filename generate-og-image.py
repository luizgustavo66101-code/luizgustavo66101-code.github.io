#!/usr/bin/env python3
"""
Script para gerar imagem Open Graph (OG) para o Portal IA 2025
Requisitos: pip install pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Configurações
WIDTH = 1200
HEIGHT = 630
OUTPUT_PATH = "og-image.png"

# Cores
BG_COLOR = "#0F172A"  # Azul escuro
PRIMARY_COLOR = "#3B82F6"  # Azul primário
TEXT_COLOR = "#FFFFFF"  # Branco
ACCENT_COLOR = "#60A5FA"  # Azul claro

def create_og_image():
    """Cria a imagem Open Graph"""
    
    # Criar imagem com fundo gradiente (simular com cor sólida)
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Adicionar gradiente visual com retângulos
    for i in range(HEIGHT):
        ratio = i / HEIGHT
        # Gradiente do azul escuro para azul primário
        r = int(15 + (59 - 15) * ratio)
    
    try:
        # Tentar usar fonte do sistema, caso contrário usar padrão
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    except:
        try:
            # Windows
            title_font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 80)
            subtitle_font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 40)
            small_font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 28)
        except:
            # Fallback para fonte padrão
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
    
    # Desenhar círculos decorativos (canto superior direito)
    circle_radius = 150
    draw.ellipse(
        [(WIDTH - circle_radius - 50, -50), (WIDTH + 50, circle_radius + 50)],
        fill=PRIMARY_COLOR,
        outline=ACCENT_COLOR,
        width=3
    )
    
    # Desenhar linha decorativa
    draw.line([(50, 150), (WIDTH - 50, 150)], fill=PRIMARY_COLOR, width=4)
    
    # Textos
    title = "Portal IA 2025"
    subtitle = "O Futuro da Inteligência Artificial"
    footer = "luizgustavo66101-code.github.io"
    
    # Calcular posições centralizadas
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (WIDTH - title_width) // 2
    
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (WIDTH - subtitle_width) // 2
    
    footer_bbox = draw.textbbox((0, 0), footer, font=small_font)
    footer_width = footer_bbox[2] - footer_bbox[0]
    footer_x = (WIDTH - footer_width) // 2
    
    # Desenhar textos
    draw.text((title_x, 150), title, font=title_font, fill=TEXT_COLOR)
    draw.text((subtitle_x, 280), subtitle, font=subtitle_font, fill=ACCENT_COLOR)
    draw.text((footer_x, 550), footer, font=small_font, fill=PRIMARY_COLOR)
    
    # Salvar imagem
    img.save(OUTPUT_PATH)
    print(f"✅ Imagem OG criada com sucesso: {OUTPUT_PATH}")
    print(f"📐 Dimensões: {WIDTH}x{HEIGHT}px")

if __name__ == "__main__":
    create_og_image()
