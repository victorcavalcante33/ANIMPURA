# ANIMA PURA — MVP técnico inicial

Este repositório agora contém o primeiro núcleo jogável de **ANIMA PURA** em Python para validar as mecânicas antes da implementação em engine mobile.

## O que já está implementado

- Criação de **Meta-Humano** com:
  - classe mística
  - habilidade inicial
  - história e destino
  - código da alma
- Geração de **quest inicial** por contexto do personagem.
- Simulação de **combate por turno** (jogador vs inimigo).
- **Loop demonstrativo** em `main.py`.

## Como rodar

```bash
python3 main.py
```

## Como testar

```bash
pytest -q
```

## Próximos passos sugeridos

1. Persistência de save local (JSON/SQLite).
2. Mapa de ilha com navegação em nós.
3. Sistema de progressão numerológica (árvore de atributos).
4. Portar este core para Godot/Unity como lógica de gameplay.
