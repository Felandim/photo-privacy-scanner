from pathlib import Path


SITE = Path(__file__).parents[1] / "site" / "index.html"


def test_metadata_stripping_export_is_present() -> None:
    html = SITE.read_text(encoding="utf-8")

    assert 'id="strip"' in html
    assert "canvas.toBlob" in html
    assert "exifr.gps(cleanBlob)" in html
    assert "-sem-metadados" in html


def test_metadata_export_warns_about_visible_content() -> None:
    html = SITE.read_text(encoding="utf-8")

    assert "Conteúdo visível (rostos, texto e placas) não é alterado." in html
