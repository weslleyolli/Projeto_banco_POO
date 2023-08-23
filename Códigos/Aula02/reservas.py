import pandas as pd

# Criar um DataFrame com os dados das reservas
data_reservas = {
    'Nome do Hóspede': ['Hóspede 1', 'Hóspede 2', 'Hóspede 3', 'Hóspede 4', 'Hóspede 5'],
    'Data de Check-in': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05'],
    'Data de Check-out': ['2023-08-04', '2023-08-05', '2023-08-06', '2023-08-07', '2023-08-08'],
    'Número de Quartos Reservados': [1, 2, 1, 1, 3],
    'Tipo de Quarto': ['Standard', 'Deluxe', 'Standard', 'Suite', 'Deluxe'],
    'Valor Total da Reserva': [300, 600, 350, 800, 900]
}

df_reservas = pd.DataFrame(data_reservas)

# Realizar análises dos dados de reservas
media_valor_total = df_reservas['Valor Total da Reserva'].mean()
tipo_quarto_mais_reservado = df_reservas['Tipo de Quarto'].value_counts().idxmax()
media_noites = (pd.to_datetime(df_reservas['Data de Check-out']) - pd.to_datetime(df_reservas['Data de Check-in'])).mean().days

print(f"Média do Valor Total das Reservas: ${media_valor_total:.2f}")
print(f"Tipo de Quarto Mais Reservado: {tipo_quarto_mais_reservado}")
print(f"Média de Noites por Reserva: {media_noites:.1f} noites")

