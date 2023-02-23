import socket

# Objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s der certo a conexão essa mensagem sera printada
print("Socket criado com sucesso")

# Variavel para armazenar o host
host = 'localhost'
# VAriavel para armazenar a porta 
port = 5433

# Objeto de conexão fazendo uma ligação host e porta
s.bind((host, port))
menssagem = '\nServidor: Olá cliente!! '

# enquando a liçaão entiver acontecendo
while 1:
    # Ira receber os bits e guarda dentro do dados
    dados, end = s.recvfrom(4096)

    # se dados tiver algum bit ira criar a conexão
    if dados:
        print("Servidor enviando menssagem...")
        # Menssagem enviada no final 
        s.sendto(dados + (menssagem.encode()),end )