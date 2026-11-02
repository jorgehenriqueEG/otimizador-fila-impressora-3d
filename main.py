peças = [
    {"nome": "Prototipo", "bateria": 15, "camadas": 5, "tempo_camada": 2},
    {"nome": "Suporte", "bateria": 80, "camadas": 10, "tempo_camada": 1},
    {"nome": "Engrenagem", "bateria": 10, "camadas": 3, "tempo_camada": 1},
    {"nome": "Moldura", "bateria": 95, "camadas": 20, "tempo_camada": 0.5}
]

urgentes = []
normais = []

for p in peças:
    tempo_total = p["camadas"] * p["tempo_camada"]
    if p["bateria"] < 20:
        p["tempo_total"] = tempo_total
        p["prioridade"] = "Urgente"
        urgentes.append(p)
    else:
        p["tempo_total"] = tempo_total
        p["prioridade"] = "Normal"
        normais.append(p)

urgentes.sort(key=lambda x: x["bateria"])
normais.sort(key=lambda x: x["tempo_total"])

fila_final = urgentes + normais

print("Fila de Impressão:")
for i, p in enumerate(fila_final):
    print(f"{i+1}. {p['nome']} ({p['prioridade']})")