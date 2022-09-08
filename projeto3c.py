# Notícias Página do GE e salvar em arquivo html 

!pip install requests
import requests

def leitor(endereco: str) -> requests.models.Response:
  pagina = requests.get(endereco)
  return pagina

def grava(resposta: requests.models.Response) -> None: 
  arquivo = open('esporte.html', 'wb')
  for texto in pagina.iter_content(1048576):
    arquivo.write(texto)
arquivo.close()

def main(): 
  endereco = "https://ge.globo.com/"
  esporte = leitor (endereco)
  grava (esporte)

if __name__ == "__main__":
  main()