# Photo Privacy Scanner

[![CI](https://github.com/Felandim/photo-privacy-scanner/actions/workflows/ci.yml/badge.svg)](https://github.com/Felandim/photo-privacy-scanner/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Resumo
Ferramenta para revisar fotos antes da publicação e apontar possíveis exposições de privacidade.
O MVP recebe detecções classificadas, atribui pesos de risco e produz um score agregado.
A evolução prevista inclui detecção automática de rostos, placas, telas, crachás e texto sensível.

## Stack
Python, OpenCV/OCR na próxima etapa, pytest e Ruff.

## Problema → Abordagem → Resultado
**Problema:** fotos aparentemente inocentes podem expor pessoas, placas, documentos, telas ou outras informações identificáveis no fundo.

**Abordagem:** classificar elementos detectados por categoria e severidade, agregando-os em um score de risco antes da publicação.

**Resultado esperado do MVP:** produzir score de 0 a 100 e listar os elementos que mais contribuem para o risco da imagem.

## Como rodar
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
ruff check .
```

## Estrutura
```text
src/photo_privacy_scanner/   # regras de classificação de risco
tests/                       # testes automatizados
.github/workflows/            # CI
```

## Limitações / Próximos passos
Ainda não há detecção automática em imagens. Próximos passos: face detection, OCR, placas, regiões de tela, explicação visual e interface web.

## Tópicos sugeridos
`privacy` `computer-vision` `image-analysis` `ocr` `security` `python`
