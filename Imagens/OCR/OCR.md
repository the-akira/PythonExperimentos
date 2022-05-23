# Optical Character Recognition (OCR)

**Optical Character Recognition** (OCR) é o processo que converte uma imagem de texto em um formato de texto legível por máquina. Por exemplo, se você digitalizar um formulário ou recibo, seu computador salvará a digitalização como um arquivo de imagem. Você não pode usar um editor de texto para editar, pesquisar nem contar as palavras no arquivo de imagem. No entanto, você pode usar o OCR para converter a imagem em um documento de texto com o conteúdo armazenado como dados de texto.

Amplamente utilizado como forma de entrada de dados a partir de registros de dados impressos em papel – sejam documentos de passaporte, faturas, extratos bancários, recibos computadorizados, cartões de visita, correspondência, impressões de dados estáticos ou qualquer documentação adequada – é um método comum de digitalização de textos impressos para que possam ser editados eletronicamente, pesquisados, armazenados de forma mais compacta, exibidos online e usados em processos de máquina, como computação cognitiva, tradução automática, conversão de texto em fala (extraído), dados-chave e mineração de texto. OCR é um campo de pesquisa em reconhecimento de padrões, inteligência artificial e visão computacional.

## Python-Tesseract

[Python-Tesseract](https://pypi.org/project/pytesseract/) é uma ferramenta de **Optical Character Recognition** (OCR) para Python. Ou seja, ele irá reconhecer e “ler” o texto embutido nas imagens.

### Instalação

Atualmente, o [Tesseract](https://github.com/tesseract-ocr/tesseract) está funcionando adequadamente nas plataformas Windows, macOS e Linux. O Tesseract suporta Unicode (UTF-8) e suporta mais de 100 idiomas. Neste exemplo, começaremos com o processo de instalação do Tesseract OCR e testaremos a extração de texto em imagens.

O primeiro passo é instalar o Tesseract. Para usar a biblioteca Tesseract, primeiro precisamos instalá-la em nosso sistema. Se você estiver usando Linux, você pode simplesmente usar o **apt-get** para instalar o Tesseract OCR:

```
sudo apt-get install tesseract-ocr
```

Para Windows e macOS, consulte a [documentação do Tesseract](https://tesseract-ocr.github.io/tessdoc/).

Agora que temos Tesseract em nossa máquina, podemos finalmente instalar a biblioteca **Python-Tesseract**:

```
pip install pytesseract
```

### Experimento

Uma vez que concluímos as devidas instalações, vamos avançar aplicando Tesseract com Python. 

Primeiro, importamos as dependências necessárias:

```python
from PIL import Image
import pytesseract
import numpy as np
```

Para este exemplo, irei utilizar a seguinte imagem:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/Imagens/OCR/text.png)

Vamos então carregá-la e convertê-la para texto:

```python
filename = 'text.png'
image = np.array(Image.open(filename))
text = pytesseract.image_to_string(image).strip()
```

E então podemos imprimir o resultado:

```python
print(text)
"""
As alchemists used the term, transmutation meant the passage of a thing
from one level to another or the metamorphosis of its elements into other
elements. According to the alchemists, transmutation of lead into gold or silver
requires that active knowledge (gnosis) work together with inner experience
(or active imagination). Such illuminated knowledge promotes a “second
birth” and elevates the secular element to the religious level of God, who
created all higher things out of lower ones (as he formed Adam from the dust
of the earth).
"""
```

 Tesseract pode ser adequado na construção de um [pipeline](https://en.wikipedia.org/wiki/Pipeline_(computing)) de processamento de documentos onde as imagens são digitalizadas e processadas. Isso funciona melhor para situações com *input* de alta resolução em que o texto em primeiro plano é segmentado com precisão a partir do plano de fundo.

## Referências

- [O que é OCR?](https://aws.amazon.com/pt/what-is/ocr/)
- [Build Optical Character Recognition (OCR) in Python](https://towardsdatascience.com/build-optical-character-recognition-ocr-in-python-28d1c7b77da3)