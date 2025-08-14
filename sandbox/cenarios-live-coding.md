# 🎯 Cenários de Live Coding - FDE Package Sorting System

## 📋 **5 Cenários Essenciais para Preparação (20 minutos)**

---

## **1. 🔧 Error Handling & Input Validation** ⭐⭐⭐⭐⭐
**Probabilidade:** 95% | **Tempo:** 6-10 min | **Complexidade:** Baixa

**Solicitação:** *"Adicione validação robusta e tratamento de erros para a função sort"*

**O que implementar:**
- Função `validate_package_data(width, height, length, mass)`
- Verificar se todos os valores são números positivos
- Levantar exceções específicas (`InvalidPackageDataError`, `NegativeValueError`)
- Adicionar testes para casos inválidos (valores negativos, zero, None, strings)
- Integrar validação na função `sort()` com try/catch

**Casos de teste essenciais:**
```python
# Valores negativos
sort(-10, 20, 30, 5)  # Should raise NegativeValueError

# Valores zero
sort(0, 20, 30, 5)    # Should raise InvalidPackageDataError

# Tipos inválidos
sort("10", 20, 30, 5) # Should raise TypeError
```

**Dicas:**
- Use `isinstance()` para verificar tipos
- Crie hierarquia de exceções customizadas
- Mensagens de erro descritivas e úteis

---

## **2. 🎯 Extensibility: New Classification Criteria** ⭐⭐⭐⭐
**Probabilidade:** 85% | **Tempo:** 12-16 min | **Complexidade:** Média

**Solicitação:** *"Torne o sistema extensível para aceitar novos critérios de classificação configuráveis"*

**O que implementar:**
- Classe `ClassificationConfig` com critérios configuráveis
- Função `sort_with_config(config, width, height, length, mass)`
- Suporte a múltiplos critérios (não só heavy/bulky)
- Nova categoria: "FRAGILE" (alta densidade ou baixo volume)
- Manter compatibilidade com função `sort()` original

**Estrutura sugerida:**
```python
@dataclass
class ClassificationConfig:
    heavy_threshold: float = 20.0
    bulky_volume_threshold: float = 1_000_000
    bulky_dimension_threshold: float = 150.0
    fragile_density_threshold: float = 5.0  # kg per 1000 cm³
    
def sort_with_config(config: ClassificationConfig, ...) -> str:
    # Implementar lógica extensível
```

**Dicas:**
- Use dataclass para configuração
- Mantenha função `sort()` original como wrapper
- Teste diferentes configurações

---

## **3. � Observability: Logging & Metrics** ⭐⭐⭐⭐
**Probabilidade:** 80% | **Tempo:** 10-14 min | **Complexidade:** Média

**Solicitação:** *"Adicione sistema de observabilidade com logs e métricas operacionais"*

**O que implementar:**
- Classe `PackageMetrics` para tracking
- Logging estruturado com diferentes níveis
- Contadores por categoria e estatísticas em tempo real
- Método `get_operational_summary()` com métricas
- Rate limiting e alertas para anomalias

**Métricas essenciais:**
```python
class PackageMetrics:
    def __init__(self):
        self.category_counts = {"STANDARD": 0, "SPECIAL": 0, "REJECTED": 0}
        self.processing_times = []
        self.error_count = 0
        self.start_time = time.time()
    
    def get_summary(self) -> dict:
        # Retornar estatísticas agregadas
```

**Dicas:**
- Use módulo `logging` do Python
- Timestamps e structured logging (JSON)
- Considere singleton pattern para métricas globais

---

## **4. � External System Integration** ⭐⭐⭐
**Probabilidade:** 70% | **Tempo:** 15-18 min | **Complexidade:** Média-Alta

**Solicitação:** *"Integre o sistema com APIs externas para validação de dados ou notificações"*

**O que implementar:**
- Interface `ExternalValidator` para validação de pacotes
- Mock de API externa para weight verification
- Sistema de notificações para packages REJECTED
- Retry logic e circuit breaker pattern básico
- Fallback para funcionamento offline

**Estrutura sugerida:**
```python
class ExternalValidator:
    def validate_weight(self, mass: float) -> bool:
        # Simular chamada API externa
    
    def notify_rejection(self, package_data: dict) -> bool:
        # Enviar notificação externa

def sort_with_external_validation(width, height, length, mass) -> str:
    # Integrar validação externa com lógica existente
```

**Dicas:**
- Mock das APIs para testes
- Timeout e error handling para APIs
- Graceful degradation quando API falha

---

## **5. ⚡ Performance Optimization for High Volume** ⭐⭐⭐
**Probabilidade:** 65% | **Tempo:** 12-18 min | **Complexidade:** Média-Alta

**Solicitação:** *"Otimize o sistema para processar milhares de pacotes por segundo"*

**O que implementar:**
- Função `sort_batch(packages: List[dict]) -> List[str]`
- Otimizações: pré-cálculo, vectorização, caching
- Processamento paralelo com `concurrent.futures`
- Profiling e benchmarks de performance
- Memory-efficient processing para datasets grandes

**Otimizações específicas:**
```python
# Batch processing otimizado
def sort_batch_optimized(packages: List[dict]) -> List[str]:
    # Pre-calculate volumes
    volumes = [p['width'] * p['height'] * p['length'] for p in packages]
    
    # Vectorized operations
    heavy_mask = [p['mass'] >= 20 for p in packages]
    bulky_mask = [vol >= 1_000_000 or any(dim >= 150 for dim in [p['width'], p['height'], p['length']]) 
                  for vol, p in zip(volumes, packages)]
    
    # Classify in batch
    results = []
    for heavy, bulky in zip(heavy_mask, bulky_mask):
        if heavy and bulky:
            results.append("REJECTED")
        elif heavy or bulky:
            results.append("SPECIAL")
        else:
            results.append("STANDARD")
    
    return results
```

**Dicas:**
- Use list comprehensions para eficiência
- Benchmark com `timeit` module
- Considere `numpy` se disponível
- Profile com `cProfile` para bottlenecks

---

# 🚀 **Estratégias de Implementação**

## **🎯 Priorização por Probabilidade:**
1. **Error Handling** (95%) - Sempre pedem isso
2. **Extensibility** (85%) - Demonstra design thinking
3. **Observability** (80%) - Crucial para sistemas reais
4. **Integration** (70%) - Mostra experiência com sistemas
5. **Performance** (65%) - Diferencial técnico

## **⏱️ Gestão de Tempo:**
- **5-10 min:** Cenário 1 (Error Handling)
- **10-15 min:** Cenários 2, 3 (Extensibility, Observability)
- **15-20 min:** Cenários 4, 5 (Integration, Performance)

## **🧠 Abordagem Mental:**
1. **Entenda o requisito** (30 seg)
2. **Escreva o teste primeiro** (2-3 min)
3. **Implemente incrementalmente** (60-70% do tempo)
4. **Refatore e otimize** (2-3 min)
5. **Documente brevemente** (1 min)

## **⚠️ Armadilhas Comuns:**
- Não quebrar a função `sort()` original
- Over-engineering em 20 minutos
- Esquecer de casos edge nos testes
- Não explicar o raciocínio durante implementação
- Focar na perfeição vs funcionalidade

## **�‍♂️ Dicas de Velocidade:**
- Tenha templates de classes/funções prontos
- Imports comuns memorizados (`from typing import`, `import time`, etc.)
- Use TDD para ir mais direto ao ponto
- Fale enquanto codifica (mostre o pensamento)
- Priorize funcionalidade working sobre código perfeito

## **💡 Demonstre Pensamento Técnico:**
- Sempre mencione trade-offs das decisões
- Explique como escalaria para produção
- Considere edge cases desde o início
- Mostre preocupação com maintainability
- Relate com experiências reais quando possível

---

**🎯 Lembre-se:** O objetivo é demonstrar capacidade de implementar rapidamente com boa qualidade, não código de produção perfeito!
