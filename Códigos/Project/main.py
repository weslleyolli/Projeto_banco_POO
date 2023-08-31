import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Lendo os dados dos arquivos CSV
df_woman = pd.read_csv('worldcup_woman.csv')
df_man = pd.read_csv('worldcup_man.csv')

# Convertendo match_date para datetime
df_woman['match_date'] = pd.to_datetime(df_woman['match_date'])
df_man['match_date'] = pd.to_datetime(df_man['match_date'])

# Evolução de números de gols por copa
# Calculando o total de gols por copa para mulheres
df_woman['year'] = df_woman['match_date'].dt.year
gols_por_ano_woman = df_woman.groupby('year')[['team_a_score', 'team_b_score']].sum().reset_index()
gols_por_ano_woman['total_gols'] = gols_por_ano_woman['team_a_score'] + gols_por_ano_woman['team_b_score']

# Calculando o total de gols por copa para homens
df_man['year'] = df_man['match_date'].dt.year
gols_por_ano_man = df_man.groupby('year')[['team_a_score', 'team_b_score']].sum().reset_index()
gols_por_ano_man['total_gols'] = gols_por_ano_man['team_a_score'] + gols_por_ano_man['team_b_score']

# Criação do gráfico de evolução de gols por copa para homens e mulheres
fig_gols_por_ano = px.line(gols_por_ano_woman, x='year', y='total_gols', title='Evolução do Número de Gols por Copa')
fig_gols_por_ano.add_scatter(x=gols_por_ano_man['year'], y=gols_por_ano_man['total_gols'], mode='lines', name='Homens')
fig_gols_por_ano.add_scatter(x=gols_por_ano_woman['year'], y=gols_por_ano_woman['total_gols'], mode='lines', name='Mulheres')
fig_gols_por_ano.show()

# Calculando o total de vitórias, empates e derrotas por copa para mulheres
df_woman['year'] = df_woman['match_date'].dt.year
vit_der_emp_woman = df_woman.groupby('year')[['team_a_win', 'team_b_win', 'draw']].sum().reset_index()
vit_der_emp_woman['total'] = vit_der_emp_woman['team_a_win'] + vit_der_emp_woman['team_b_win'] + vit_der_emp_woman['draw']

# Calculando o total de vitórias, empates e derrotas por copa para homens
df_man['year'] = df_man['match_date'].dt.year
vit_der_emp_man = df_man.groupby('year')[['team_a_win', 'team_b_win', 'draw']].sum().reset_index()
vit_der_emp_man['total'] = vit_der_emp_man['team_a_win'] + vit_der_emp_man['team_b_win'] + vit_der_emp_man['draw']

# Criação do gráfico de distribuição de vitórias, empates e derrotas por copa para homens e mulheres
fig_vit_der_emp = px.line(vit_der_emp_woman, x='year', y='total', title='Distribuição de Vitórias e Empates por Ano')
fig_vit_der_emp.add_scatter(x=vit_der_emp_man['year'], y=vit_der_emp_man['team_a_win'] + vit_der_emp_man['team_b_win'], mode='lines', name='Homens - Vitórias')
fig_vit_der_emp.add_scatter(x=vit_der_emp_man['year'], y=vit_der_emp_man['total'], mode='lines', name='Homens - Total')
fig_vit_der_emp.add_scatter(x=vit_der_emp_woman['year'], y=vit_der_emp_woman['team_a_win'] + vit_der_emp_woman['team_b_win'], mode='lines', name='Mulheres - Vitórias')
fig_vit_der_emp.show()

# Evolução do número de jogos da copa
jogos_por_ano_woman = df_woman.groupby('year')['match_id'].count().reset_index()
jogos_por_ano_man = df_man.groupby('year')['match_id'].count().reset_index()

fig_jogos_por_ano = px.line(jogos_por_ano_woman, x='year', y='match_id', title='Evolução do Número de Jogos por Ano')
fig_jogos_por_ano.add_scatter(x=jogos_por_ano_man['year'], y=jogos_por_ano_man['match_id'], mode='lines', name='Masculino')
fig_jogos_por_ano.show()

