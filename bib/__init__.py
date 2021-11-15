import pytesseract
import cv2
import os


def extensao(arquivo):
    index = arquivo.rfind('.')
    return arquivo[index:]


def imagens(diretorio):
    ext_img = ['.png', '.jpg', '.jpeg']
    if not os.path.isdir(diretorio):
        print("Não existe esse diretório")
    else:
        arquivos = os.listdir(diretorio)
        if arquivos == []:
            print('Não existe imagens na pasta.')

        lista = []
        for nome in arquivos:
            if os.path.isfile(os.path.join(diretorio, nome)):
                ext = str.lower(extensao(nome))
                if ext in ext_img:
                    arquivo = os.path.join(diretorio, nome)
                    lista.append([arquivo, nome])
        return lista


def txt(diretorio, texto):
    # Salva o arquivo no formato txt
    endereco = f'{diretorio}/txt'
    if not os.path.isdir(endereco):
        os.mkdir(endereco)
    destino = f'{endereco}/textos.txt'
    with open(destino, 'w', encoding='utf8') as arquivo:
        arquivo.write(texto)
    print(f"Arquivo '.../textos.txt' salvo com sucesso.")


def converter(diretorio):
    ts = r'C:\Program Files\Tesseract-OCR'
    pytesseract.pytesseract.tesseract_cmd = ts + r'\tesseract.exe'
    if diretorio == '':
        print('ERRO! Forneça os dados.')
    else:
        lista = imagens(diretorio)
        textos = ''
        for num, item in enumerate(lista):
            imagem = item[0]
            arquivo = item[1]
            img = cv2.imread(imagem)
            convertido = pytesseract.image_to_string(img, lang='por')
            if num != 0:
                prefixo = '\n\n'
            else:
                prefixo = '''Convertido de uma imagem ou conjunto de imagens\nAutor: Tião Nazário\nAno: 2021\n\n\n'''
            texto = f"{prefixo}====== {arquivo} ======\n\n{convertido}\n"
            textos += texto
            print(f"=====> '{arquivo}' convertido com sucesso!!!")

        txt(diretorio, textos)
