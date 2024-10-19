"""
Este script gera arquivos de áudio em pt-pt
a partir de dicionários separados por categorias.
Autor: Dorian Junior
Data: Outubro 2024

"""
import os
from gtts import gTTS

# Dicionário com as listas fornecidas
listas = {
    '1_Palavras_básicas': [
        "Sim", "Naun", "Talvez", "Não sei", "Obrigado", "Obrigada",
        "De nada", "Por favor", "Desculpe", "Muito Prazer", "Igualmente"
    ],
    '2_Frases_básicas': [
        "Não entendo", "Pode repetir", "Pode falar mais devagar",
        "Pode ajudar-me", "Como se diz", "O que significa"
    ],
    '3_Números': [
        "Um", "Uma", "Dois", "Duas", "Três", "Quatro", "Cinco",
        "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze",
        "Treze", "Catorze", "Quinze", "Dezasseis", "Dezassete",
        "Dezoito", "Dezanove", "Vinte", "Vinte e um", "Trinta",
        "Quarenta", "Cinquenta", "Sessenta", "Setenta" "Oitenta", "Noventa",
        "Cem", "Cento e um"
    ],
    '4_Dias_da_Semana': [
        "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
        "Sexta-feira", "Sábado", "Domingo"
    ],
    '5_Estações_do_Ano': [
        "A primavera", "O verão", "O outono", "O inverno"
    ],
    '6_O_Clima': [
        "Calor", "Frio", "Ameno", "Sol", "Vento", "Chuva", "Nublado",
        "Nevoeiro", "Neve", "Sé u"
    ],
    '7_Meses_do_Ano': [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro",
        "Dezembro"
    ],
    '8_Tempo': [
        "A hora", "O dia", "A semana", "O mês", "O ano",
        "O fim de semana", "A folga", "As férias", "O feriado",
        "A manhã", "A tarde", "A noite", "Ontem", "Hoje", "Amanhã"
    ],
    '9_Verbos_regulares_mais_utilizados': [
        "Falar", "Conversar", "Morar", "Viver", "Gostar", "Trabalhar",
        "Estudar", "Ensinar", "Aprender", "Pensar", "Achar",
        "Compreender", "Escrever", "Comer", "Beber", "Tomar",
        "Almoçar", "Jantar", "Comprar", "Vender", "Usar", "Preferir",
        "Decidir", "Acreditar", "Assistir", "Passear", "Acordar",
        "Dormir", "Descansar", "Arrumar", "Abrir", "Fechar", "Partir",
        "Chegar", "Viajar", "Apanhar", "Permitir"
    ],
    '10_Verbos_irregulares_mais_utilizados': [
        "Ser", "Estar", "Ter", "Fazer", "Ir", "Vir", "Sair", "Ver",
        "Ler", "Ouvir", "Querer", "Saber", "Poder", "Pedir", "Dar",
        "Conduzir"
    ],
    '11_Família': [
        "O pái", "A mãi", "Os pais", "O avô", "A avó", "Os avós",
        "O filho", "A filha", "Os filhos", "O irmão", "A irmã",
        "Os irmãos", "O neto", "A neta", "Os netos", "O tio",
        "A tia", "Os tios", "O primo", "A prima", "Os primos",
        "O sobrinho", "A sobrinha", "Os sobrinhos", "O esposo", "O marido",
        "A esposa", "A mulher", "O casal", "O namorado", "A namorada",
        "O amigo", "A amiga", "Os amigos", "O cão", "A cadela",
        "Os cães", "O gato", "A gata", "Os gatos"
    ],
    '12_A_casa': [
        "O apartamento", "A vivenda", "O andar", "O piso",
        "O resh do chão", "O primeiro piso", "O sótão", "A cave",
        "O quarto", "A sala", "A cozinha", "A casa de banho",
        "A despensa", "O escritório", "A lavandaria", "O jardim"
    ],
    '13_A_cidade': [
        "A cidade", "O centro da cidade", "A avenida", "A rua",
        "A estrada", "A rotunda", "Os semáforos", "A ponte",
        "O cruzamento", "O banco", "O multibanco", "O centro comercial",
        "A loja", "O mercado", "O museu", "A farmácia", "O hospital",
        "A eixtação", "A paragem", "O aeroporto", "Os correios",
        "O posto de gasolina"
    ],
    '14_Direções': [
        "à esquerda", "à direita", "em frente", "atrás", "ao lado",
        "entre", "em baixo", "em cima", "na esquina", "A duas quadras",
        "perto de", "longe de"
    ],
    '15_Os_transportes': [
        "O carro", "O autocarro", "A mota", "O comboio", "O metro",
        "O barco", "O avião", "A bicicleta", "O táxi", "O elétrico"
    ],
    '16_Na_loja': [
        "Comprar", "Pagar", "O dinheiro", "As moedas", "As notas",
        "O troco", "A fatura", "O talão", "O recibo", "A conta",
        "O número de contribuinte", "O cartão de débito",
        "O cartão de crédito", "O multibanco", "O banco", "A gorjeta",
        "Caro", "Barato"
    ],
    '17_No_restaurante': [
        "O menu", "A ementa", "As entradas", "O prato principal",
        "O prato do dia", "As bebidas", "A sobremesa", "O garfo",
        "A faca", "A colher", "O guardanapo", "O prato", "O copo",
        "A reserva", "A mesa", "A conta", "A refeição",
        "Bom apetite", "Está delicioso"
    ],
    '18_Na_festa': [
        "O convite", "O plano", "Os bilhetes", "A festa",
        "O número do telefone", "Beber um copo", "Jantar fora",
        "Sair à noite"
    ]
}

def gerar_audio(lista_nome):
    """
    esta função checa se a lista não foi encontrada
    no conjunto de listas.

    Args:
        lista_nome: argumento dado pelo usuário

    Returns:
        retorna verdadeiro se a lista não tiver sido encontrada
        e imprime a mensagem "lista não encontrada".

    """

    if lista_nome not in listas:
        print(f"Lista {lista_nome} não encontrada.")
        return

    # Juntar palavras/frases com pausas
    texto = ' ... '.join(listas[lista_nome])  # Criar pausas entre as palavras/frases

    # Gerar o áudio em pt-pt
    tts = gTTS(text=texto, lang='pt', slow=True)  # `slow=True` para fala pausada
    nome_arquivo = f"{lista_nome}.mp3"

    # Criar diretório de áudio se não existir
    if not os.path.exists('audios'):
        os.makedirs('audios')

    caminho_arquivo = os.path.join('audios', nome_arquivo)
    tts.save(caminho_arquivo)
    print(f"Áudio gerado: {caminho_arquivo}")

# Gerar áudios para todas as listas
if __name__ == "__main__":
    for lista_nome in listas:
        gerar_audio(lista_nome)

# PARA IMPLEMENTAR O LINK NO PDF DO LIVRO

"""
# Nome do PDF original e o nome do novo PDF que será criado com o link
input_pdf_path = "Free Portuguese Vocabulary Guide.pdf-6.pdf"
output_pdf_path = "Ebook_teste.pdf"
link = "https://drive.google.com/drive/folders/1c_CY0GbPGa8WcyiYxF1-GekCjUdPk0wG?usp=share_link"

# Cria um PDF em branco contendo o link com um botão circular amarelo
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)

# Definindo a posição do círculo e do texto
circle_x = 300  # Posição X do círculo (centro da página)
circle_y = 400  # Posição Y do círculo (mais ou menos no meio da página)
radius = 50     # Raio do círculo

# Desenha um círculo amarelo
can.setFillColor(colors.yellow)
can.circle(circle_x, circle_y, radius, stroke=0, fill=1)

# Adiciona o texto "Download áudios" no centro do círculo
can.setFillColor(colors.black)
can.setFont("Helvetica-Bold", 12)
text_x = circle_x - 40  # Ajusta a posição X do texto (centrado no círculo)
text_y = circle_y - 5   # Ajusta a posição Y do texto
can.drawString(text_x, text_y, "Download áudios")

# Cria um link clicável sobre o botão
link = "https://drive.google.com/file/d/11hESi0sr4f0tmiX0M1DWzxvXfbFqwdPs/view?usp=sharing"
can.linkURL(link, (circle_x - radius, circle_y - radius, circle_x + radius, circle_y + radius))

# Finaliza o PDF
can.save()

# Move o ponteiro de volta para o início do buffer
packet.seek(0)

# Ler o conteúdo do novo PDF em branco criado com o link
new_pdf = PdfReader(packet)

# Ler o conteúdo do PDF original
existing_pdf = PdfReader(open(input_pdf_path, "rb"))

# Criar um PdfWriter para o novo arquivo
output = PdfWriter()

# Adicionar as páginas do PDF original ao novo PDF
for page_num in range(len(existing_pdf.pages)):
    page = existing_pdf.pages[page_num]
    if page_num == 0:  # Adiciona o link apenas à primeira página
        page.merge_page(new_pdf.pages[0])
    output.add_page(page)

# Escrever o PDF atualizado com o link no arquivo de saída
with open(output_pdf_path, "wb") as outputStream:
    output.write(outputStream)

print(f"Novo PDF criado: {output_pdf_path}")
"""

# link = https://drive.google.com/drive/folders/1c_CY0GbPGa8WcyiYxF1-GekCjUdPk0wG?usp=share_link
