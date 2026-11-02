# otimizador-fila-impressora-3d
## Descrição do Problema
Um sistema para priorizar a impressão de peças em uma fila de impressoras 3D com base no tempo restante de bateria e na urgência da tarefa.
## Requisitos
- Receber a lista de peças com suas informações.
- Calcular o tempo total necessário para imprimir cada peça (camadas * tempo_por_camada).
- Separar as peças em "urgente" (bateria < 20%) e "normal".
- Ordenar as peças urgentes pelo tempo restante de bateria (menor primeiro) e as normais pelo tempo total de impressão (menor primeiro).
- Imprimir a fila final de impressão.
## Exemplo de Uso
Peças: [{"nome": "Prototipo", "bateria": 15, "camadas": 5, "tempo_camada": 2}, {"nome": "Suporte", "bateria": 80, "camadas": 10, "tempo_camada": 1}]
Saída:
Fila de Impressão:
1. Prototipo (Urgente)
2. Suporte (Normal)