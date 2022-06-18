import apinasa,twitter,image

from flask import Flask
from flask import render_template
from googletrans import Translator

texto_explanation =apinasa.imageexplanation()
image_title =apinasa.imagetitle()

#Iniciar el objeto de traduccion
translator = Translator()
#Traducir el texto
translated_texto_explanation = translator.translate(texto_explanation, src='en', dest='es')
translated_title = translator.translate(image_title, src='en', dest='es')
#explanation_corto =Texto corto para la descripcion de la imagen
explanation_corto = translated_texto_explanation.text[0:150] + '...'
print(explanation_corto)

#Instancia de Flask
app = Flask(__name__)

#Rutas:
#Ruta principal:
@app.route('/')
def incio():
    explanation=translated_texto_explanation.text
    title=translated_title.text
    url_img=apinasa.imageurl()
    return render_template('index.html',explanation=explanation,title=title,url_img=url_img)
#Ruta de twitter:
@app.route('/send')
def enviar():
    twitter.tweet('🚀 Imagen del dia via la NASA: ' + translated_title.text + '\n'+ explanation_corto +' \n' + apinasa.imageurl())
    return "Send"
#Ruta de download:
@app.route('/download')
def download():
    image.image_download(apinasa.imageurl())
    return "download successfu"
#Iniciar el servidor:
if __name__ == '__main__':
    app.run(debug=True,port=80)


    