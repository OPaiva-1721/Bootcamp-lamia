from functools import reduce


def media(*valores):
    return sum(valores) / len(valores)


def normalizar(coluna):
    minimo, maximo = min(coluna), max(coluna)
    return [(x - minimo) / (maximo - minimo) for x in coluna]


def erro_quadratico_medio(reais, previstos):
    erros = map(lambda r, p: (r - p) ** 2, reais, previstos)
    return reduce(lambda acc, e: acc + e, erros) / len(reais)


class Modelo:
    def __init__(self, nome, **config):
        self.nome = nome
        self.config = config

    def treinar(self, X, y):
        raise NotImplementedError

    def prever(self, x):
        raise NotImplementedError

    def prever_varios(self, X):
        return [self.prever(x) for x in X]


class RegressaoLinear(Modelo):
    def __init__(self, **config):
        super().__init__("Regressão Linear", **config)
        self.w, self.b = 0.0, 0.0
        self.__taxa = config.get("taxa", 0.1)

    @property
    def taxa(self):
        return self.__taxa

    @taxa.setter
    def taxa(self, valor):
        if valor > 0:
            self.__taxa = valor

    def treinar(self, X, y):
        n = len(X)
        epoca, erro_anterior = 0, float("inf")
        max_epocas = self.config.get("epocas", 5000)

        while epoca < max_epocas:
            previstos = self.prever_varios(X)
            dw = sum((p - r) * x for p, r, x in zip(previstos, y, X)) * 2 / n
            db = sum(p - r for p, r in zip(previstos, y)) * 2 / n
            self.w -= self.taxa * dw
            self.b -= self.taxa * db

            erro = erro_quadratico_medio(y, self.prever_varios(X))
            if abs(erro_anterior - erro) < 1e-10:
                break
            erro_anterior = erro
            epoca += 1
        return epoca

    def prever(self, x):
        return self.w * x + self.b


class KNN(Modelo):
    def __init__(self, k=3):
        super().__init__("KNN", k=k)
        self.dados = []

    def treinar(self, X, y):
        self.dados = list(zip(X, y))

    def prever(self, x):
        distancia = lambda a, b: sum((ai - bi) ** 2 for ai, bi in zip(a, b)) ** 0.5
        vizinhos = sorted(self.dados, key=lambda d: distancia(d[0], x))[: self.config["k"]]

        votos = {}
        for _, rotulo in vizinhos:
            votos[rotulo] = votos.get(rotulo, 0) + 1
        return max(votos, key=votos.get)


if __name__ == "__main__":
    dados = [(1, 3.1), (2, 4.9), (3, 7.2), (4, 8.8), (5, 11.1), (6, 13.0)]
    horas = [h for h, _ in dados]
    notas = [n for _, n in dados]

    print(f"Média das notas: {media(*notas):.2f}")

    reg = RegressaoLinear(taxa=0.01, epocas=20000)
    epocas = reg.treinar(horas, notas)
    mse = erro_quadratico_medio(notas, reg.prever_varios(horas))
    print(f"{reg.nome}: w={reg.w:.3f}, b={reg.b:.3f}, MSE={mse:.4f} ({epocas} épocas)")

    nova = 7
    print(f"Previsão para {nova}h de estudo: {reg.prever(nova):.2f}")

    X = [(1, 40), (2, 50), (3, 60), (5, 80), (6, 90), (7, 95), (2, 45), (6, 85)]
    y = ["reprovado", "reprovado", "reprovado", "aprovado", "aprovado", "aprovado",
         "reprovado", "aprovado"]
    print("Classes:", set(y))

    cols = [normalizar(list(c)) for c in zip(*X)]
    Xn = list(zip(*cols))

    knn = KNN(k=3)
    knn.treinar(Xn[:-2], y[:-2])
    teste_X, teste_y = Xn[-2:], y[-2:]
    previsoes = knn.prever_varios(teste_X)

    acertos = len(list(filter(lambda par: par[0] == par[1], zip(previsoes, teste_y))))
    for p, r in zip(previsoes, teste_y):
        status = "✔" if p == r else "✘"
        print(f"  previsto={p:9} real={r:9} {status}")
    print(f"Acurácia: {acertos / len(teste_y):.0%}")
