# Criar uma lista de comentários fictícios
comentarios = [
    "Adorei minha estadia! Ótimo serviço e comida deliciosa.",
    "O quarto estava limpo, mas o Wi-Fi era um pouco lento.",
    "A localização do hotel é perfeita, perto de todas as atrações.",
    "Não gostei do atendimento na recepção, mas o café da manhã era incrível.",
    "As instalações do hotel são excelentes, especialmente a piscina."
]

# Palavras-chave para determinar sentimento
palavras_positivas = ['adorei', 'ótimo', 'perfeito', 'incrível', 'excelentes', 'deliciosa']
palavras_negativas = ['não gostei', 'lento', 'ruim']

# Determinar o sentimento dos comentários
for comentario in comentarios:
    comentario_lower = comentario.lower()

    if any(palavra in comentario_lower for palavra in palavras_positivas):
        sentimento = "positivo"
    elif any(palavra in comentario_lower for palavra in palavras_negativas):
        sentimento = "negativo"
    else:
        sentimento = "neutro"

    print(f"Comentário: {comentario}")
    print(f"Sentimento: {sentimento}\n")