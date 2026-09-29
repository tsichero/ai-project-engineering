# AI Project Engineering — End-to-End AI System

**Portfolio project · AI Engineering · GenAI · RAG · Backend · Evaluation**

## Implementado

- API FastAPI;
- retrieval determinístico;
- base de documentos versionada;
- resposta grounded quando há contexto;
- fallback seguro sem contexto;
- fontes retornadas pela API;
- testes de grounding e fallback;
- ADRs, Docker e CI.

> Esta etapa implementa **retrieval + resposta determinística**. Ainda não há chamada a LLM. Portanto, não é apresentada como RAG com LLM completo.

## Arquitetura atual

~~~text
Client → FastAPI → Retrieval → Contexto → Resposta determinística → Grounding + Sources
~~~

## Testes

~~~bash
pip install -r requirements.txt
pytest -q
~~~

## Próxima evolução

- [ ] embeddings/vector store;
- [ ] RAG com LLM real;
- [ ] validação de saída estruturada;
- [ ] dataset e métricas de avaliação;
- [ ] observabilidade;
- [ ] benchmark de latência/custo.

## Competências

**AI Engineering · RAG · Retrieval · GenAI Architecture · FastAPI · Evaluation · Testing · Python**

[AI & Data Portfolio](https://tsichero.github.io/tsichero.github.io-portfolio-ai/)