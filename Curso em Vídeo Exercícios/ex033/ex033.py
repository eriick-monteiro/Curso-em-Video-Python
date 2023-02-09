primeiro = int(input('Primeiro valor: '))
segundo  = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))

# Verificando quem é menor
menor = primeiro
if (segundo < primeiro and segundo < terceiro):
    menor = segundo
if (terceiro < primeiro and terceiro < segundo):
    menor = terceiro

# Verificando quem é maior
maior = primeiro
if (segundo > primeiro and segundo > terceiro):
    maior = segundo
if (terceiro > primeiro and terceiro > segundo):
    maior = terceiro

# Printando o maior e menor valor digitados
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')