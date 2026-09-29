# AI Project Engineering — End-to-End AI System

> **Portfolio project · AI Engineering · GenAI · RAG · Backend · Evaluation**

Projeto central do portfólio para demonstrar o ciclo completo de construção de uma solução de IA: **problema → requisitos → arquitetura → implementação → avaliação → testes → documentação → evolução**.

A proposta é mostrar engenharia de produto de IA, e não apenas uma chamada isolada para um modelo.

## 🎯 Problema

Aplicações de IA precisam equilibrar qualidade de resposta, contexto, validação, observabilidade e requisitos de produto.

Este projeto cria uma base modular para investigar esse ciclo de forma reproduzível.

## 🏗️ Arquitetura

~~~text
Client
  │
  ▼
FastAPI
  │
  ▼
Application Service
  │
  ├── Retrieval / RAG
  ├── Prompt Layer
  ├── LLM Layer
  ├── Output Validation
  └── Evaluation
  │
  ▼
Structured Response
~~~

## 🔎 Fluxo

1. receber a solicitação;
2. validar o contrato;
3. recuperar contexto quando necessário;
4. construir o contexto para geração;
5. gerar uma resposta;
6. validar a saída;
7. avaliar qualidade e grounding;
8. registrar evidências e falhas.

## 🧩 Princípios de engenharia

### RAG antes de aumentar complexidade do modelo

Quando o problema depende de conhecimento externo ou atualizado, recuperação de contexto pode ser uma alternativa arquitetural antes de considerar fine-tuning.

### Retrieval separado da geração

Separar recuperação e geração facilita testar cada componente e investigar falhas.

### Avaliação como parte do produto

Uma aplicação de IA precisa de critérios de avaliação e casos de regressão, não apenas de uma demonstração visual.

### Falha segura

Respostas sem contexto suficiente devem ser tratadas explicitamente, em vez de mascarar incerteza.

## 🛠️ Stack

**Python · FastAPI · RAG · LLMs · Prompt Engineering · Evaluation · Pydantic · Testing · Docker · REST**

## 📁 Estrutura

~~~text
ai-project-engineering/
├── README.md
├── app/
├── data/
├── evaluation/
├── tests/
├── docs/
│   └── adr/
├── output/
├── Dockerfile
└── requirements.txt
~~~

## 🧪 Qualidade

O projeto deve manter:

- testes unitários;
- testes de contrato da API;
- casos de avaliação;
- documentação de decisões;
- evidências reproduzíveis;
- registro explícito de limitações.

## 📐 ADRs

Decisões arquiteturais são documentadas em docs/adr/.

Exemplos:

- ADR-001 — RAG versus fine-tuning
- ADR-002 — separação entre retrieval e generation
- ADR-003 — FastAPI como camada de serviço
- ADR-004 — avaliação e regressão de prompts

## 📊 Avaliação

| Dimensão | Objetivo |
|---|---|
| Relevância | contexto recuperado atende à pergunta |
| Grounding | resposta permanece apoiada no contexto |
| Aderência | segue instruções e contrato |
| Latência | observar custo temporal |
| Robustez | testar variações de entrada |
| Falhas | registrar comportamento inadequado |

## 🔐 Limitações

Este repositório é um projeto de portfólio e não representa automaticamente um sistema de produção.

Resultados experimentais dependem dos dados, modelo, parâmetros e conjunto de avaliação utilizados.

## 🚀 Roadmap

- [ ] implementar pipeline RAG completo
- [ ] adicionar dataset de avaliação
- [ ] implementar avaliação automática
- [ ] adicionar API
- [ ] adicionar observabilidade
- [ ] containerizar
- [ ] CI/CD
- [ ] adicionar benchmark de latência e custo
- [ ] documentar deployment cloud

## 💼 Competências demonstradas

**AI Engineering · Generative AI · RAG · LLM Applications · Backend · API Design · Evaluation · Prompt Engineering · Testing · Architecture · Technical Documentation**

## 🔗 Portfólio

[AI & Data Portfolio](https://tsichero.github.io/tsichero.github.io-portfolio-ai/)
