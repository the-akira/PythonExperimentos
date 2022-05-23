# Optical Character Recognition (OCR)

**Optical Character Recognition** (OCR) é a conversão eletrônica ou mecânica de imagens de texto digitado, manuscrito ou impresso em texto codificado por máquina, seja de um documento digitalizado, uma foto de um documento, uma foto de cena (por exemplo, o texto em letreiros e outdoors em uma foto de paisagem) ou de texto de legenda sobreposto a uma imagem (por exemplo: de uma transmissão de televisão).

Amplamente utilizado como forma de entrada de dados a partir de registros de dados impressos em papel – sejam documentos de passaporte, faturas, extratos bancários, recibos computadorizados, cartões de visita, correspondência, impressões de dados estáticos ou qualquer documentação adequada – é um método comum de digitalização de textos impressos para que possam ser editados eletronicamente, pesquisados, armazenados de forma mais compacta, exibidos online e usados em processos de máquina, como computação cognitiva, tradução automática, conversão de texto em fala (extraído), dados-chave e mineração de texto. OCR é um campo de pesquisa em reconhecimento de padrões, inteligência artificial e visão computacional.

## Python-Tesseract

[Python-Tesseract](https://pypi.org/project/pytesseract/) é uma ferramenta de **Optical Character Recognition** (OCR) para Python. Ou seja, ele irá reconhecer e “ler” o texto embutido nas imagens.

### Instalação

Atualmente, o [Tesseract](https://github.com/tesseract-ocr/tesseract) está funcionando adequadamente nas plataformas Windows, macOS e Linux. O Tesseract suporta Unicode (UTF-8) e suporta mais de 100 idiomas. Neste exemplo, começaremos com o processo de instalação do Tesseract OCR e testaremos a extração de texto em imagens.

O primeiro passo é instalar o Tesseract. Para usar a biblioteca Tesseract, primeiro precisamos instalá-la em nosso sistema. Se você estiver usando Linux, você pode simplesmente usar o **apt-get** para instalar o Tesseract OCR:

```
sudo apt-get install tesseract-ocr
```

Para usuários do macOS, usaremos o Homebrew para instalar o Tesseract:

```
brew install tesseract
```

Para Windows, consulte a [documentação do Tesseract](https://tesseract-ocr.github.io/tessdoc/).

Agora que temos Tesseract em nossa máquina, podemos finalmente instalar a biblioteca **Python-Tesseract**:

```
pip install pytesseract
```