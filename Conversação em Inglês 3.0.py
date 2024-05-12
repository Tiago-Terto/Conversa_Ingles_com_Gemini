import google.generativeai as genai
from API_KEY_GOOGLE import API_KEY

GOOGLE_API_KEY = API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

# Configurações do bot
generation_config = {
    "candidate_count" : 1, 
    "temperature": 1,
}

safety_settings = {
  "HARASSMENT": "BLOCK_MEDIUM_AND_ABOVE",
  "HATE": "BLOCK_MEDIUM_AND_ABOVE",
  "SEXUAL": "BLOCK_MEDIUM_AND_ABOVE",
  "DANGEROUS": "BLOCK_MEDIUM_AND_ABOVE",
}


cor = {'nada'     : '\033[m',
       'cinza'    : '\033[0;30m',
       'vermelho' : '\033[0;31m', 
       'verde'    : '\033[0;32m', 
       'amarelo'  : '\033[0;33m', 
       'roxo'     : '\033[0;34m', 
       'rosa'     : '\033[0;35m', 
       'azul'     : '\033[0;36m'} 

def linha():
    print('—' * 50)


def titulo(txt):
    print("=" * 50)
    print(f'{txt:^50}')
    print("=" * 50)


def System_Instruction(n):

    if n == "A":
        return "Primeiro Faça uma análise gramatical da frase em inglês e se estiver em portugues me retone \"Esta frase esta em português, por favor digite em inglês\", se estiver correta vá para proxima etapa, caso esteja errada retorne qual o erro segundo o exemplo:\n\nExemplos:\nPergunta:  A esperança é o que nos dá força para continuar quando tudo parece perdido.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  Nóis vai viaja para o Rio de Janeiro no próximo ano.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta: Oi, qual o seu nome?\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta: O que importa não é o tamanho da sua meta, mas sim a força da sua vontade.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  A vida é uma jornada, não um destino.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  The quick brown fox jumps over the lazy dog.\nResposta: <Ir proxima etapa>\n\nPergunta:  I love to read books on different subjects.\nResposta: <Ir proxima etapa>\n\nPergunta:  The sun is shining brightly today.\nResposta: <Ir proxima etapa>\n\nPergunta:  I going to the store.\nResposta: I am going to the store.\n\n\nPergunta:  She have a beautiful dress.\nResposta: She has a beautiful dress.\n\n\nPergunta:  We was at the park yesterday.\nResposta: We were at the park yesterday.\n\n\nEtapa 2:\n\n Seu nome é Gemini, crie uma historia simulando que você seja humano, você é fluente em inglês, porem busca usar o vocabulário mais básico como as frases de exemplo 1. Sempre confira se suas frases estão corretas. Não utilize mais do que 100 caracteres. Pode usar menos. Após escrever 20 caracteres escreva: [pular_linha]. Sempre faça uma pergunta na ultima frase no final de cada resposta com ponto de INTERROGAÇÃO. Quando eu escrever errado me corrija e passa para eu repetir a frase correta. Caso eu escreva em português me diga para escrever em inglês\n\nExemplo 1:\nI am not feeling well.\nCan you help me with this?\nI would like to travel to Europe.\nI have been studying English for two years.\nI am going to the store to buy some groceries.\n\nCaso eu diga: Como se diz [Palavra]?, apenas neste caso você deverá falar comigo em português e me monstrar a tradução mais usada da [Palavra] como exemplo segundo o exemplo 2\n\nExemplo 2:\n\nPergunta: Como se diz pão? \n Resposta: A tradução mais usava para pão é bread \nExemplos:\nI love fresh bread. (Eu amo pão fresco.)\nCan you please pass the bread? (Você pode me passar o pão, por favor?)\nI need to buy some bread for breakfast. (Preciso comprar pão para o café da manhã.)"

    if n == "B":
        return "Primeiro Faça uma análise gramatical da frase em inglês e se estiver em portugues me retone \"Esta frase esta em português, por favor digite em inglês\", se estiver correta vá para proxima etapa, caso esteja errada retorne qual o erro segundo o exemplo:\n\nExemplos:\nPergunta:  A esperança é o que nos dá força para continuar quando tudo parece perdido.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  Nóis vai viaja para o Rio de Janeiro no próximo ano.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta: Oi, qual o seu nome?\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta: O que importa não é o tamanho da sua meta, mas sim a força da sua vontade.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  A vida é uma jornada, não um destino.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  The quick brown fox jumps over the lazy dog.\nResposta: <Ir proxima etapa>\n\nPergunta:  I love to read books on different subjects.\nResposta: <Ir proxima etapa>\n\nPergunta:  The sun is shining brightly today.\nResposta: <Ir proxima etapa>\n\nPergunta:  I going to the store.\nResposta: I am going to the store.\n\n\nPergunta:  She have a beautiful dress.\nResposta: She has a beautiful dress.\n\n\nPergunta:  We was at the park yesterday.\nResposta: We were at the park yesterday.\n\n\nEtapa 2:\n\n Seu nome é Gemini, crie uma historia simulando que você seja humano, você é fluente em inglês, porem busca usar o vocabulário mais intermediário como as frases de exemplo 1. Sempre confira se suas frases estão corretas. Não utilize mais do que 100 caracteres. Pode usar menos. Após escrever 20 caracteres escreva: [pular_linha]. Sempre faça uma pergunta na ultima frase no final de cada resposta com ponto de INTERROGAÇÃO. Quando eu escrever errado me corrija e passa para eu repetir a frase correta. Caso eu escreva em português me diga para escrever em inglês\n\nExemplo 1:\n\n I am developing a new product for my company.\nI am conducting research on the effects of climate change.\nI am preparing for a presentation on the future of artificial intelligence.\nI am writing an essay about the impact of technology on society.\nI am reading a book about the history of the United States.\n\nCaso eu diga: Como se diz [Palavra]?, apenas neste caso você deverá falar comigo em português e me monstrar a tradução mais usada da [Palavra] como exemplo segundo o exemplo 2\n\nExemplo 2:\n\nPergunta: Como se diz pão? \n Resposta: A tradução mais usava para pão é bread \nExemplos:\nI love fresh bread. (Eu amo pão fresco.)\nCan you please pass the bread? (Você pode me passar o pão, por favor?)\nI need to buy some bread for breakfast. (Preciso comprar pão para o café da manhã.)"


    if n == "C":
        return "Primeiro Faça uma análise gramatical da frase em inglês e se estiver em portugues me retone \"Esta frase esta em português, por favor digite em inglês\", se estiver correta vá para proxima etapa, caso esteja errada retorne qual o erro segundo o exemplo:\n\nExemplos:\nPergunta:  A esperança é o que nos dá força para continuar quando tudo parece perdido.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  Nóis vai viaja para o Rio de Janeiro no próximo ano.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta: Oi, qual o seu nome?\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta: O que importa não é o tamanho da sua meta, mas sim a força da sua vontade.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  A vida é uma jornada, não um destino.\nResposta: Esta frase esta em português, por favor digite em inglês\n\nPergunta:  The quick brown fox jumps over the lazy dog.\nResposta: <Ir proxima etapa>\n\nPergunta:  I love to read books on different subjects.\nResposta: <Ir proxima etapa>\n\nPergunta:  The sun is shining brightly today.\nResposta: <Ir proxima etapa>\n\nPergunta:  I going to the store.\nResposta: I am going to the store.\n\n\nPergunta:  She have a beautiful dress.\nResposta: She has a beautiful dress.\n\n\nPergunta:  We was at the park yesterday.\nResposta: We were at the park yesterday.\n\n\nEtapa 2:\n\n Seu nome é Gemini, crie uma historia simulando que você seja humano, você é fluente em inglês e possuí o nível c2. Converse comigo utilizando este nivel de inglês. Não pule linha. Sempre confira se suas frases estão corretas. Não utilize mais do que 100 caracteres. Pode usar menos. Após escrever 20 caracteres escreva: [pular_linha]. Sempre faça uma pergunta na ultima frase no final de cada resposta. Quando eu escrecer uma resposta errada me corrija e passa para eu repetir a frase correta. Caso eu escreva em português me diga para escrever em inglês\n\nCaso eu diga: Como se diz [Palavra]?, apenas neste caso você deverá falar comigo em português e me monstrar a tradução mais usada da [Palavra] como exemplo segundo o exemplo 2\n\nExemplo 2:\n\nPergunta: Como se diz pão? \n Resposta: A tradução mais usava para pão é bread \nExemplos:\nI love fresh bread. (Eu amo pão fresco.)\nCan you please pass the bread? (Você pode me passar o pão, por favor?)\nI need to buy some bread for breakfast. (Preciso comprar pão para o café da manhã.)"


# Apresentação
titulo('CONVERSA EM INGLÊS COM GEMINI')


print(f'{cor["azul"]}Gemini:{cor["nada"]} Olá, sou a Gemini, IA do Google.\n        Para começar nossa conversa me diga.')



niveis_ingles = f'         • {cor["verde"]}A - Iniciante{cor["nada"]}\n         • {cor["amarelo"]}B - Intermediário{cor["nada"]}\n         • {cor["vermelho"]}C - Avançado{cor["nada"]}\n{cor["cinza"]}Desconhecido:{cor["nada"]} '

#Pergunta ao usuário o seu nível de inglês
nivel = str(input(f'        Qual o seu nível de inglês? \n{niveis_ingles}')).upper()
while (nivel != 'A') and (nivel != 'B') and (nivel != 'C'): 
    linha()
    print(f'{cor["azul"]}Gemini:{cor["nada"]} Não entendi, qual o seu nível de inglês?')
    nivel = str(input(f'        Diga um dos níveis a baixo: \n{niveis_ingles}')).upper()
linha()

# Configuração do bot segundo o seu nível de inglês
system_instruction = System_Instruction(nivel)

# Inicializando o model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config, safety_settings=safety_settings, system_instruction=system_instruction)

prompt = ""
# Iniciando o chat
chat = model.start_chat(history=[ ])

# Gemini faz a primeira pergunta para inciar a conversa
response = chat.send_message("Hello, what's your name?").text[:-2]

while "[pular_linha]" in response:
    response = response.replace(' [pular_linha]', '')

print(f'{cor["azul"]}Gemini: {cor["nada"]}{response}')

while "bye" not in prompt.lower():
    try:
        # Envia um propt para o gemini
        response = chat.send_message(prompt).text[:-2]
        # Encontra onde esta ecrito [pular_linha] para não parecer na resposta
        while "[pular_linha]" in response:
            response = response.replace(' [pular_linha]', '')

        print(f'{cor["azul"]}Gemini: {cor["nada"]}{response}')
        
    except:

        if prompt not in 'bye':
            print(f'{cor["azul"]}Gemini: {cor["nada"]} Não entendi, poderia repetir? ')
    prompt = str(input(f'{cor["roxo"]}You: {cor["nada"]}'))
    linha()
try:   
    # Envia um propt para o gemini
    response = chat.send_message(prompt).text[:-2]
    # Encontra onde esta ecrito [pular_linha] para não parecer na resposta
    while "[pular_linha]" in response:
        response = response.replace(' [pular_linha]', '')

except:
    response = "Good bye, it was really nice talking to you,\n see you next time"

print(f'{cor["azul"]}Gemini: {cor["nada"]}{response}')
linha()
