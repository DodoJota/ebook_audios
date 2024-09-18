import pandas as pd
import pdfkit
from datetime import datetime

#lendo a coluna 'Terça' e armazenando em variavel stock_3
stock_3 = pd.read_excel('Bottles_2024.xlsx', sheet_name=-1)
stock_3 = stock_3[['Bebida','Terça']].copy()
stock_3.rename(columns={'Terça':'Total'}, inplace=True)

#lendo a coluna 'Quinta' e armazenando em variavel stock_5
stock_5 = pd.read_excel('Bottles_2024.xlsx', sheet_name=-1)
stock_5 = stock_5[['Bebida','Quinta']].copy()
stock_5.rename(columns={'Quinta':'Total'}, inplace=True)

quantidades = pd.read_excel('Para_ter_stock.xlsx')

print(stock_3.columns)
print(stock_5.columns)
print(quantidades.columns)



hoje = datetime.now().weekday()
hora_atual = datetime.now().hour
minuto_atual = datetime.now().minute

if hoje == 1 and hora_atual == 14 and minuto_atual == 15:
    stock = stock_3
elif hoje == 0 and hora_atual == 15 and minuto_atual == 50:
    stock = stock_5
else:
    print("Hoje não é nem terça-feira nem quinta-feira.")

# Executar a lógica de merge e filtragem
if hoje in [0, 3] and hora_atual == 15 and minuto_atual == 50:  # Executar apenas se for terça ou quinta
    merged = stock.merge(quantidades, on='Bebida', how='left')

print(list(merged.columns))
agora = datetime.now()
agora

merged['Encomendar'] = merged.apply(lambda row: max(0, row['Para_ter'] - row['Total']), axis=1)

# uma célula antes eu fiz o drop das colunas Total e Para ter,
# que antes eram Total_x e Total_y
merged.drop(columns=['Total', 'Para_ter'], inplace=True)

# Converter o DataFrame para HTML, sem indice e com texto alinhado
html = merged.to_html(index=False, classes='text-center')

# Adicionar CSS para o alinhamento centralizado
css = """
<style>
.text-center {
  text-align: center;
}
</style>
"""

# Gerar o PDF usando pdfkit
pdfkit.from_string(css + html, 'Encomenda_para_Amanhã.pdf')