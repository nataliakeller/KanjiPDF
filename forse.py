import unicodedata
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import math

# Caminhos dos arquivos
template_path = 'template.jpg'
csv_file_path = 'kanjis.csv'
output_path = 'Filled_Page_{}.jpg'  # Nome do arquivo de saída com índice para páginas

# Carregar o template e o CSV
template_image = Image.open(template_path)
kanji_data = pd.read_csv(csv_file_path)

# Carregar a fonte japonesa
font_path = "C:/Windows/Fonts/BIZ-UDMinchoM.ttc"  # Substitua se necessário
font_size = 92  # Aumentado para preencher melhor o espaço
font = ImageFont.truetype(font_path, font_size)

# Função para verificar se o caractere é kanji
def is_kanji(char):
    return 'CJK' in unicodedata.name(char)  # Verifica se o caractere pertence ao bloco CJK (Kanji)

# Função para separar os kanjis e filtrar apenas os caracteres de kanji
def separate_kanji(kanji_str):
    return [char for char in kanji_str if is_kanji(char)]

# Lista de kanjis
kanji_list = kanji_data['Sort Field'].tolist()

# Filtrar os kanjis e separar os caracteres, ignorando katakana e hiragana
filtered_kanji_list = []
for kanji_str in kanji_list:
    kanji_chars = separate_kanji(kanji_str)
    filtered_kanji_list.extend(kanji_chars)  # Adicionar os kanjis filtrados à lista final

# Definir coordenadas dos campos de kanji no template
kanji_positions = [
    (100, 135), (100, 400), (100, 650), (100, 910), (100, 1180), (100, 1430)
]

# Número máximo de kanjis por imagem
kanjis_per_page = len(kanji_positions)

# Calcular o número de páginas necessárias
num_pages = math.ceil(len(filtered_kanji_list) / kanjis_per_page)

# Criar uma imagem para cada página
for page in range(num_pages):
    # Carregar uma cópia do template para cada página
    template_copy = template_image.copy()
    draw = ImageDraw.Draw(template_copy)
    
    # Determinar o intervalo de kanjis para esta página
    start_idx = page * kanjis_per_page
    end_idx = start_idx + kanjis_per_page
    kanjis_on_page = filtered_kanji_list[start_idx:end_idx]
    
    # Desenhar os kanjis no template
    for idx, kanji in enumerate(kanjis_on_page):
        x, y = kanji_positions[idx]
        
        # Calcular posição centralizada usando textbbox para medir o tamanho do kanji
        bbox = draw.textbbox((0, 0), kanji, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        centered_x = x - text_width // 2 + 50  # Ajuste para centralizar no quadrado
        centered_y = y - text_height // 2 + 50
        
        draw.text((centered_x, centered_y), kanji, fill="black", font=font)
    
    # Salvar o resultado para esta página
    template_copy.save(output_path.format(page + 1))
    print(f"Imagem salva como {output_path.format(page + 1)}")
