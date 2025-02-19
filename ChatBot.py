def chatbot_responder(pergunta):
    pergunta = pergunta.lower()
    respostas = {
        'olá': 'Olá! Como posso ajudar você hoje?',
        'tudo bem': 'Estou bem, obrigado por perguntar!',
        'qual é o seu nome?': 'Eu sou um chatbot criado para ajudar!',
        'adeus': 'Até logo! Foi bom conversar com você.',
        'qual é a sua função?': 'Eu sou um chatbot para responder perguntas simples.',
        'como você está?': 'Eu sou um programa, mas estou pronto para ajudar!',
        'me fale sobre o clima': 'Infelizmente, não sei o clima, mas posso te ajudar a encontrar a previsão!',
        'qual é a capital do brasil?': 'A capital do Brasil é Brasília.',
        'quem é o presidente do brasil?': 'Atualmente, o presidente do Brasil é Luiz Inácio Lula da Silva.',
    }
    
    for chave, valor in respostas.items():
        if chave in pergunta:
            return valor
    
    return 'Desculpe, não entendi sua pergunta. Pode reformular?'

def armazenar_conversa(pergunta, resposta):
    with open("historico_chat.txt", "a") as f:
        f.write(f"Você: {pergunta}\nChatbot: {resposta}\n\n")

def iniciar_chatbot():
    print("Bem-vindo ao chatbot! (Digite 'adeus' para sair)")
    
    while True:
        pergunta = input("Você: ")
        
        if pergunta.lower() == 'adeus':
            print("Chatbot: Até logo!")
            break
        
        resposta = chatbot_responder(pergunta)
        print(f"Chatbot: {resposta}")
        
        armazenar_conversa(pergunta, resposta)

iniciar_chatbot()
