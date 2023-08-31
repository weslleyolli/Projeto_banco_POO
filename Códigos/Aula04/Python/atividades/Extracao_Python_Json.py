import requests
import json

def get_dados_filme(titulo_filme):
    requisicao = requests.get(f"http://www.omdbapi.com/?t={titulo_filme}&apikey=f30db950")

# Confirmando a conexão com a API e retornando dados_filme como json
    if requisicao.status_code == 200:# Criando o nome do arquivo .json a partir do título do filme
        dados_filme = requisicao.json()
        return dados_filme
    else:
        print("A requisição à API falhou.")
        return None

def main():
    print("Exemplos para consulta:\n \n Barbie \n Blade Runner  \n Madagascar \n Minions \n ")
    titulo_filme = input("Digite o título do filme: ")
    dados_filme = get_dados_filme(titulo_filme)

    if dados_filme: # Se dados_filme não for None: cria um dicionário para armazenar os valores buscados
        informacoes_filtradas = {
            'Titulo': dados_filme['Title'],
            'Ano de lancamento': dados_filme['Year'],
            'Duracao': dados_filme['Runtime'],
            'Genero': dados_filme['Genre'],
            'Roteiro': dados_filme['Plot'],
            'Pais de origem': dados_filme['Country']
        }

        # Criando o nome do arquivo .json a partir do título do filme
        nome_arquivo = f"{titulo_filme.replace(' ', '_').lower()}.json"
        with open(nome_arquivo, 'w') as json_file:
            json.dump(informacoes_filtradas, json_file,indent=4)
            print(f"\n Arquivo JSON '{nome_arquivo}' gerado com sucesso!")


if __name__ == "__main__":
    main()
