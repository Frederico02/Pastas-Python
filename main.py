import os

# Ler o arquivo de texto
with open('nomes.txt', 'r') as arquivo:
    nomes = arquivo.read().splitlines()

# Gerar as pastas
for nome in nomes:
    # Verificar se o nome não está vazio
    if nome.strip():
        # Criar a pasta com o nome
        os.makedirs(nome, exist_ok=True)
        print(f"Pasta '{nome}' criada com sucesso!")
    else:
        print("Nome vazio encontrado, pulando para o próximo.")

print("Processo concluído.")
