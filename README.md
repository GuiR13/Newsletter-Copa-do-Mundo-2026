# Copa 2026 - AI Sports Newsletter Agent

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Agno](https://img.shields.io/badge/Framework-Agno-FF6F61?style=for-the-badge)

Um agente autônomo de inteligência artificial desenvolvido em **Python** utilizando o framework **Agno** (antigo *Phidata*). O agente atua como um jornalista esportivo sênior focado na cobertura em tempo real da **Copa do Mundo da FIFA 2026**, realizando pesquisas autônomas na web para compilar uma newsletter diária estruturada, analítica e rica em dados estatísticos.

---

## 📌 Visão Geral do Sistema

O core deste projeto consiste em um agente inteligente capaz de mitigar alucinações por meio de buscas direcionadas na internet (RAG baseado em busca). Ele varre os principais portais de notícias esportivas mundiais e nacionais para extrair dados brutos da Copa de 2026, processá-los e gerar um arquivo final formatado em Markdown pronto para distribuição por e-mail ou publicação.

### 📰 Seções Geradas na Newsletter:
1. **Análise Editorial:** Panorama atual da competição.
2. **Giro da Rodada:** Resultados do último jogo e calendário dos próximos confrontos.
3. **Chaveamento Dinâmico:** Atualização das fases eliminatórias (mata-mata).
4. **Métricas Individuais:** Tabelas de Artilharia (Top 10), Assistências (Top 5) e Passes Certos (Top 5).
5. **Métricas Coletivas:** Ataques/defesas mais eficientes e ranking disciplinar (Cartões).

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.10 ou superior.
* **Orquestração de Agentes:** Framework **Agno** (Gerenciamento de contexto, ferramentas e instruções do sistema).
* **LLM Base:** Modelos de última geração com suporte nativo a ferramentas (ex: `gpt-4o`, `gemini-1.5-pro` ou `claude-3-5-sonnet` - usado: `deepseek-v4-flash`).
