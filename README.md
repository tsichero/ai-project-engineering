# AI Project Engineering — End-to-End AI System

**Portfolio project · AI Engineering · GenAI · RAG · Backend · Evaluation**

## Implementado

- API FastAPI;
- retrieval por vetores sobre base de documentos versionada;
- embeddings locais determinísticos para testes, com modo opcional Sentence Transformers;
- contexto recuperado separado da geração;
- integração com LLM por API compatível com Chat Completions;
- modo **demo** determinístico para testes sem credenciais;
- modo **real** configurável por variáveis de ambiente;
- resposta grounded com fontes;
- fallback quando não existe contexto;
- dataset inicial de avaliação;
- testes automatizados, ADRs, Docker e CI.

> **Importante:** o código implementa o caminho de RAG + LLM, mas a chamada a um provedor externo depende de configuração de ambiente. A execução real contra um modelo não é declarada como validada neste repositório sem uma execução com credenciais.

## Arquitetura

~~~text
Client
  ↓
FastAPI
  ↓
Retrieval
  ↓
Contexto relevante
  ↓
LLM Service
  ↓
Resposta grounded + Sources
~~~

O serviço de LLM é desacoplado do restante da aplicação. O padrão de endpoint permite trabalhar com provedores compatíveis com a API de Chat Completions.

## Execução demo

~~~bash
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
~~~

Por padrão, `LLM_MODE=demo`, portanto não é necessária chave de API.

## Execução com LLM real

Configure as variáveis de ambiente:

~~~bash
export LLM_MODE=real
export LLM_API_KEY="sua-chave"
export LLM_MODEL="seu-modelo"
export LLM_BASE_URL="https://api.openai.com/v1"
~~~

Depois:

~~~bash
uvicorn app.main:app --reload
~~~

**Nenhuma chave deve ser commitada no repositório.**

## Avaliação

O diretório `evaluation/` contém casos versionados para testar:

- recuperação de contexto;
- presença de fontes;
- comportamento sem contexto;
- grounding;
- regressão funcional.

A avaliação atual é uma base inicial para evolução para métricas de qualidade de resposta, faithfulness, relevância, latência e custo.

## Limitações atuais

- modo local de embeddings usa vetores hash determinísticos para manter os testes reproduzíveis;
- modo `sentence-transformers` é opcional e requer instalação/modelo;
- base de conhecimento pequena e versionada no código;
- nenhuma chamada real a LLM é executada durante a suíte padrão;
- ainda não há vector database;
- métricas de qualidade semântica ainda estão no roadmap.

## Próxima evolução

- [x] embeddings e vector store;
- [ ] reranking;
- [ ] dataset maior de avaliação;
- [ ] métricas de relevância e faithfulness;
- [ ] tracing e observabilidade;
- [ ] benchmark de latência/custo;
- [ ] autenticação e rate limiting;
- [ ] deploy cloud.

## Competências

**AI Engineering · RAG · Retrieval · LLM Integration · GenAI Architecture · FastAPI · Evaluation · Testing · Python**

[AI & Data Portfolio](https://tsichero.github.io/tsichero.github.io-portfolio-ai/)