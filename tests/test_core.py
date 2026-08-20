import pytest

from photo_privacy_scanner.core import Detection, privacy_risk_score


def test_risk_score_uses_category_weights() -> None:
    detections = [
        Detection("license_plate", 1.0),
        Detection("face", 0.5),
    ]
    assert privacy_risk_score(detections) == 32


def test_risk_score_is_bounded() -> None:
    detections = [Detection("sensitive_text", 1.0) for _ in range(3)]
    assert privacy_risk_score(detections) == 100


def test_invalid_confidence_fails() -> None:
    with pytest.raises(ValueError):
        privacy_risk_score([Detection("face", 1.1)])
