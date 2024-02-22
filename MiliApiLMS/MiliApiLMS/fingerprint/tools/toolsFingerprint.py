import os
from datetime import datetime
from PIL import Image
from imagehash import dhash
import io
import random
from datetime import datetime
import numpy as np
from scipy.spatial import distance
import numpy as np
import base64
import matplotlib.pyplot as plt


###################### Función para comparar dhashes y encontrar coincidencias
def encontrar_coincidencias(hash_prueba):
    import imagehash
    from config import Humbral
    from MiliApiLMS.models.fingerprint.modelACAHuellasDactilares import ACAHuellaDactilar
    umbral_hash = Humbral.HUMBRAL_DHASH
    coincidencias = []
    dedo=[]
    huellas = ACAHuellaDactilar.query.with_entities(ACAHuellaDactilar.Huella, ACAHuellaDactilar.CodigoPersona, ACAHuellaDactilar.CodigoDedo).all()
    for huella_registrada, codigo_persona, codigo_dedo in huellas:
        # Convertir las huellas a enteros
        hash_registrada = imagehash.hex_to_hash(huella_registrada)
        # Calcular la distancia de Hamming
        distancia =hash_prueba - hash_registrada
        if distancia < umbral_hash:
            cp=encrypt(str(codigo_persona))
            coincidencias.append(cp)
            dedo.append(codigo_dedo)
    return coincidencias, dedo

def cargar_imagen_base64(base64_str):
    imagen_bytes = base64.b64decode(base64_str)
    with io.BytesIO(imagen_bytes) as f:
        imagen_pil = Image.open(f).convert('RGB')
        imagen_pil = imagen_pil.resize((360, 320))  # Redimensionar la imagen al tamaño deseado
        img_array = np.array(imagen_pil)
        img_array = img_array / 255.0  # Normalizar la imagen
        return np.expand_dims(img_array, axis=0)
############## END Función para comparar dhashes y encontrar coincidencias


################# otros 
def verImgPillow(imgPillow):# agregar a toolsfinger
    # Tamaño de las imágenes en la visualización
    tamanio_imagen = (4, 4)
    # Mostrar la imagen de prueba
    plt.figure(figsize=tamanio_imagen)
    plt.imshow(imgPillow, cmap='gray')
    plt.title('Imagen de prueba')
    plt.axis('on')
    plt.show()
    
def encrypt(clear_text):
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    from Crypto.Protocol.KDF import PBKDF2
    import hashlib
    import base64
    if not clear_text:
        return ""
    
    encryption_key = b'C0NTR0LT0T@LCR3AR3'
    #salt = b'Ivan Medvedev'
    salt = b'\x49\x76\x61\x6e\x20\x4d\x65\x64\x76\x65\x64\x65\x76'
    kdf = PBKDF2(encryption_key, salt, 48, 1000, my_prf)
    key = kdf[:32]
    iv = kdf[32:48]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    clear_text_bytes = clear_text.encode('utf-8')
    padded_data = clear_text_bytes + ((16 - len(clear_text_bytes) % 16) * chr(16 - len(clear_text_bytes) % 16)).encode()
    cipher_text = cipher.encrypt(padded_data)
    return base64.b64encode(cipher_text).decode()

def decrypt(cipher_text):
    from Crypto.Cipher import AES
    from Crypto.Protocol.KDF import PBKDF2
    import hashlib
    import base64
    if not cipher_text:
        return ""
    
    encryption_key = b'C0NTR0LT0T@LCR3AR3'
    #salt = b'Ivan Medvedev'
    salt = b'\x49\x76\x61\x6e\x20\x4d\x65\x64\x76\x65\x64\x65\x76'
    kdf = PBKDF2(encryption_key, salt, 48, 1000, my_prf)
    key = kdf[:32]
    iv = kdf[32:48]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = base64.b64decode(cipher_text)
    clear_text_bytes = cipher.decrypt(padded_data)
    clear_text = clear_text_bytes.decode('utf-8').rstrip(chr((16 - len(clear_text_bytes) % 16)))
    return clear_text

def my_prf(p, s):
    import hashlib
    return hashlib.sha256(p + s).digest()


######### test################################
#lista huellas
def ListaHuellas():
    from MiliApiLMS.models.fingerprint.modelACAHuellasDactilares import ACAHuellaDactilar

    huella=ACAHuellaDactilar.query.with_entities(ACAHuellaDactilar.Huella).all()
    return huella

# carga imagens dhash a DB
def CargaImg_a_db_temp():
    from MiliApiLMS.models.fingerprint.modelACAHuellasDactilares import ACAHuellaDactilar
    from MiliApiLMS import sqlServer   
    # Ruta a la carpeta img
    carpeta_img = 'MiliApiLMS/img/huellas'
    cont =0
    u=None
    # Recorre la carpeta img y sus subcarpetas
    for ruta, _, archivos in os.walk(carpeta_img):
        for archivo in archivos:
            # Solo procesa archivos de imagen (puedes ajustar según los tipos de imagen que deseas procesar)
            if archivo.endswith(('.jpg', '.jpeg', '.png')):
                # Ruta completa de la imagen
                imagen_path = os.path.join(ruta, archivo)
                hash_bytes = calcular_hash(imagen_path)
                #crea usuario
                cont =cont+1
                if cont<=3:
                    u='lec_cmayorga'
                else:
                    u='lec_cvalladares'
                    cont=0
                # Guarda el registro en la base de datos
                nueva_huella = ACAHuellaDactilar(
                    CodigoDedo=random.randint(1, 10),  # Ingresa el código del dedo según sea necesario
                    CodigoPersona=random.randint(2345, 5412),  # Ingresa el código de la persona según sea necesario
                    FechaRegistro=datetime.now(),
                    Huella=hash_bytes,  # Cambiado a bytes
                    CodigoUsuario=u,  # Ingresa el código del usuario según sea necesario
                    HuellaEsValida=True  # Ingresa si la huella es válida o no según sea necesario
                )
                sqlServer.session.add(nueva_huella)
    # Guarda los cambios en la base de datos
    sqlServer.session.commit()

#calcula el hash de la imagen
def calcular_hash(imagen_path):
    # Cargar la imagen
    imagen = Image.open(imagen_path)    
    # Calcular el hash de la imagen usando dhash
    hash_imagen = dhash(imagen)
    # Convierte el hash en una cadena hexadecimal y luego a bytes
    hash_bytes = bytes(str(hash_imagen), 'utf-8')
    return hash_bytes

#lista huellas y codigo persona
def ListarHuellasPersonas():
    from MiliApiLMS.models.fingerprint.modelACAHuellasDactilares import ACAHuellaDactilar

    huella=ACAHuellaDactilar.query.with_entities(ACAHuellaDactilar.Huella, ACAHuellaDactilar.CodigoPersona).all()
    return huella
