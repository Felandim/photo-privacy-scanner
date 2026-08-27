SITE = "site/index.html"


def read_site() -> str:
    with open(SITE, encoding="utf-8") as handle:
        return handle.read()


def test_metadata_stripping_export_is_present() -> None:
    html = read_site()

    assert 'id="strip"' in html
    assert "canvas.toBlob" in html
    assert "exifr.gps(cleanBlob)" in html
    assert "-sem-metadados" in html


def test_metadata_export_warns_about_visible_content() -> None:
    html = read_site()

    assert "Conteúdo visível (rostos, texto e placas) não é alterado." in html
