import pytest # type: ignore

def test_sort_records_observation(monkeypatch):
    from fde.metrics import PackageMetrics
    import fde.core as core

    m = PackageMetrics()
    # substitui o default_metrics usado dentro de core pela instância de teste
    monkeypatch.setattr(core, "default_metrics", m)

    result = core.sort(10, 10, 10, 10)  # STANDARD
    assert result == "STANDARD"
    assert m.category_counts.get("STANDARD", 0) == 1
    assert len(m.processing_times) == 1
    assert m.processing_times[0] > 0

def test_sort_records_error_on_exception(monkeypatch):
    from fde.metrics import PackageMetrics
    import fde.core as core

    m = PackageMetrics()
    monkeypatch.setattr(core, "default_metrics", m)

    with pytest.raises(ValueError):
        # dimensões inválidas → validação deve lançar
        core.sort(-1, 10, 10, 10)

    assert m.error_count == 1