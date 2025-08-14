import time

def test_metrics_initial_state():
    """
    Ao iniciar PackageMetrics:
    - category_counts deve conter chaves para categorias esperadas com valor 0
    - processing_times deve ser uma lista vazia
    - error_count deve ser 0
    - start_time deve ser um float (timestamp)
    """
    from fde.metrics import PackageMetrics  # ainda não implementado — RED

    metrics = PackageMetrics()

    # categorias básicas esperadas (ajuste se tiver outras)
    expected_categories = {"STANDARD", "SPECIAL", "REJECTED"}

    assert isinstance(metrics.start_time, float)
    assert metrics.start_time > 0

    # category_counts tem todas as chaves esperadas e zero como valor inicial
    for cat in expected_categories:
        assert cat in metrics.category_counts
        assert metrics.category_counts[cat] == 0

    # nenhuma observação/processamento ainda
    assert isinstance(metrics.processing_times, list)
    assert metrics.processing_times == []

    # nenhum erro registrado
    assert metrics.error_count == 0

def test_record_classification_increments_count():
    from fde.metrics import PackageMetrics
    m = PackageMetrics()
    m.observe("STANDARD", 0.005)
    assert m.category_counts["STANDARD"] == 1
    assert len(m.processing_times) == 1
    assert m.processing_times[0] == 0.005

def test_get_operational_summary_returns_expected_keys():
    from fde.metrics import PackageMetrics
    m = PackageMetrics()
    m.observe("STANDARD", 0.01)
    summary = m.get_operational_summary()
    assert "category_counts" in summary
    assert "total_processed" in summary
    assert "avg_processing_time" in summary
    assert summary["total_processed"] == 1
    assert summary["processing_samples"] == 1
    assert summary["error_count"] == 0