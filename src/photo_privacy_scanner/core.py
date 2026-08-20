from __future__ import annotations

from dataclasses import dataclass

RISK_WEIGHTS = {
    "face": 15,
    "license_plate": 25,
    "screen": 20,
    "badge": 30,
    "document": 35,
    "sensitive_text": 40,
}


@dataclass(frozen=True)
class Detection:
    category: str
    confidence: float


def privacy_risk_score(detections: list[Detection]) -> int:
    """Aggregate weighted detections into a bounded 0-100 privacy-risk score."""
    score = 0.0
    for detection in detections:
        if not 0 <= detection.confidence <= 1:
            raise ValueError("Confidence must be between 0 and 1")
        score += RISK_WEIGHTS.get(detection.category, 10) * detection.confidence

    return round(min(100.0, score))
