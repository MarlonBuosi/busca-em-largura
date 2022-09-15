

def buscaEmLargura(cidadeDeSaida, cidadeDeDestino, grafo):

    cidades = [cidadeDeSaida]
    verticesExplorado = []
    caminho = []

    verticeAtual = ''

    while (verticeAtual != cidadeDeDestino):
        if len(cidades) == 0:
            return

        verticeAtual = cidades.pop(0)
        verticesExplorado.append(verticeAtual)

        for cidade in grafo[verticeAtual]:
            if not cidade in verticesExplorado and not cidade in cidades:
                caminhoParcial = [cidade, verticeAtual]
                caminho.append(caminhoParcial)
                cidades.append(cidade)

    rotaPercorrida = []
    destinoAtualizado = cidadeDeDestino
    while (destinoAtualizado != cidadeDeSaida):

        for list in caminho:
            if list[0] == destinoAtualizado:
                rotaPercorrida.append(destinoAtualizado)
                destinoAtualizado = list[1]

    rotaPercorrida.append(cidadeDeSaida)
    rotaInvertida = rotaPercorrida[::-1]

    return rotaInvertida


grafo = {
    'Brasilia': ['Belo Horizonte', 'Fortaleza'],
    'Belo Horizonte': ['Brasilia', 'Rio de Janeiro', 'Cuiaba', 'Sao Paulo'],
    'Cuiaba': ['Belo Horizonte', 'Manaus'],
    'Curitiba': ['Sao Paulo', 'Florianopolis', 'Rio de Janeiro'],
    'Fortaleza': ['Brasilia', 'Manaus', 'Salvador'],
    'Florianopolis': ['Curitiba', 'Porto Alegre'],
    'Manaus': ['Cuiaba', 'Fortaleza'],
    'Porto Alegre': ['Florianopolis', 'Sao Paulo'],
    'Rio de Janeiro': ['Belo Horizonte', 'Cuiaba', 'Curitiba'],
    'Sao Paulo': ['Belo Horizonte', 'Curitiba', 'Salvador'],
    'Salvador': ['Sao Paulo', 'Fortaleza'],

}

cidadeDeSaida = 'Curitiba'
cidadeDeDestino = 'Fortaleza'

rota = buscaEmLargura(cidadeDeSaida, cidadeDeDestino, grafo)

print("Cidade de saída:", cidadeDeSaida)
print("Cidade de destino:", cidadeDeDestino)
print("Rota com menor caminho possível: ", rota)
