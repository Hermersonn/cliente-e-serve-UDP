# Modulo usado para criar a comunicação entre duas pontas 
import socket

# Variavel que recebe a conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# caso ele possa ser criado
print("Cliente criado com sucesso.")

# Passando onde sera o host
host = 'localhost'
# Passando a porta para conexão 
porta = 5433
# Menssagem que sera enviada 
menssagem = 'Óla servidor'

# Ira tentar enviar e receber a menssagem
try:
    # Menssagem que sera enviada
    print(f"Cliente {menssagem}")
    # Destino da conexão UDP
    s.sendto(menssagem.encode(),(host, 5433))

    # Variavel que ira receber a resposta do servidor
    dados, servidor = s.recvfrom(4096)
    # Ira desenpacota e printar os dados
    dados = dados.decode()
    print(f"Cliente {dados}")
# Ira fechar a conexão para não ficar em loop 
finally:
    print(f"Cliente: Fechando a conexão")
    s.close()