import time
import threading
import logging
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

class PackageMetrics:
    """Simple, thread-safe metrics collector for package classifications."""

    def __init__(self, categories: Optional[List[str]] = None):
        if categories is None:
            categories = ["STANDARD", "SPECIAL", "REJECTED"]
        self._lock = threading.Lock()
        self.category_counts: Dict[str, int] = {c: 0 for c in categories}
        self.processing_times: List[float] = []
        self.error_count: int = 0
        self.start_time: float = time.time()

    def observe(self, category: str, duration: float) -> None:
        """Record a successful classification with processing duration (seconds)."""
        with self._lock:
            if category not in self.category_counts:
                # keep permissive: add unknown categories dynamically
                self.category_counts[category] = 0
            self.category_counts[category] += 1
            self.processing_times.append(duration)

        logger.info(
            "classification_observed",
            extra={"category": category, "duration": duration}
        )

    def record_error(self) -> None:
        """Increment error counter."""
        with self._lock:
            self.error_count += 1
        logger.error("classification_error", extra={})

    def get_operational_summary(self) -> Dict[str, object]:
        """Return aggregated metrics summary."""
        with self._lock:
            total_processed = sum(self.category_counts.values())
            avg_time = None
            if self.processing_times:
                avg_time = sum(self.processing_times) / len(self.processing_times)
            uptime_seconds = time.time() - self.start_time

            # shallow copy to avoid test races
            counts_copy = dict(self.category_counts)

        return {
            "category_counts": counts_copy,
            "total_processed": total_processed,
            "avg_processing_time": avg_time,
            "processing_samples": len(self.processing_times),
            "error_count": self.error_count,
            "uptime_seconds": uptime_seconds,
        }

# optional module-level default (testable; can be monkeypatched in tests)
default_metrics = PackageMetrics()