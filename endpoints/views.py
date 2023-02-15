from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt


# /endpoints/Login
@csrf_exempt
def login(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        # TODO: Consultor a base de datos
        if usuario == "Antony" and password == "901757150":
            # correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error Login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


def obtenerCategoria(request):
    if request.method == "GET":
        categoria = request.GET.get("categoria")

        if categoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        comidas = [
        {
            "id": 1,
            "nombre": "Conchitas a la Parmesana",
            "url": " https://1.bp.blogspot.com/-1gpQXGuUxZY/X-NR-IfTK5I/AAAAAAAAPKk/GPFcQrTeYRQSUctlJjcvOajaoLuElqMSgCLcBGAsYHQ/s1200/Conchitas%2Ba%2Bla%2Bparmesana.jpg",
            "categoria": 1
        },
            {
            "id": 1,
            "nombre": "Causa de Pollo",
            "url": "https://elcomercio.pe/resizer/1xz3w_26FwRA5JuSn02p9afc97g=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/7QDRJTB2DZHB7IQL3HF4IK6OX4.jpg",
            "categoria": 1
        },
            {
            "id": 1,
            "nombre": "Leche de Tigre",
            "url": "https://elcomercio.pe/resizer/6TR0Lcwmg4Z_vm0JlNbscb4JNMA=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/VN5X2O53B5E4VINDN7TGWQLUQ4.jpg",
            "categoria": 1
        },
            {
            "id": 2,
            "nombre": "Ceviche de Pesacdo",
            "url": "https://trome.pe/resizer/-R8GQPfZoAOK4V9uCalvv6FeYEs=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/KMEMVCZ2KJAATPYX2JT7FDPT5Q.jpg",
            "categoria": 2
        },
            {
            "id": 2,
            "nombre": "Jalea Mixta",
            "url": "https://www.comedera.com/wp-content/uploads/2022/06/jalea-mixta.jpg",
            "categoria": 2
        },
            {
            "id": 2,
            "nombre": "Arroz con Mariscos",
            "url": "https://elcomercio.pe/resizer/2NsfDVlLCtb6UlSre99ZthqWhP8=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/NEE6QF2DE5D7VIM3CTX3SBU6FI.jpg",
            "categoria": 2
        },
            {
            "id": 3,
            "nombre": "Chicha Morada",
            "url": "https://elcomercio.pe/resizer/hFBXMzUVwnOLwhZrKRyKUOYx_dU=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/UZW3LRBMABAA5IZPHJ36MJZX5I.jpg",
            "categoria": 3
        },
            {
            "id": 3,
            "nombre": "Limonada ",
            "url": "https://cloudfront-us-east-1.images.arcpublishing.com/infobae/CLWWVAIRGJF4FG4ATXCV7YZZLQ.jpg",
            "categoria": 3
        },
            {
            "id": 3,
            "nombre": "Maracucya",
            "url": "https://peru21.pe/resizer/-DolEImJY18leOPdibu4kyKIjb8=/1200x800/smart/filters:format(jpeg):quality(75)/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/G5XOTKDEENAX7JYZMWI4YYGD24.jpg",
            "categoria": 3
        },
            {
            "id": 4,
            "nombre": "Torta de Chocolate",
            "url": "https://peru21.pe/resizer/YmGwSw9bXc2Hgoua1WgdNhw2hN0=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/EJLK47B5TRBDFPD4FMZXUWCWZQ.png",
            "categoria": 4
        },
            {
            "id": 4,
            "nombre": "Flan",
            "url": "https://www.recetasnestle.com.mx/sites/default/files/srh_recipes/0c7289c004b75116015878c651519e10.jpg",
            "categoria": 4
        },
            {
            "id": 4,
            "nombre": "Mousse de Mango",
            "url": "https://sivarious.com/wp-content/uploads/2022/05/mousse-de-mango.jpg",
            "categoria": 4
        },
            {
            "id": 5,
            "nombre": "Helado de Fresa",
            "url": "https://www.comedera.com/wp-content/uploads/2022/04/Helado-de-fresas-casero-shutterstock_1477385882.jpg",
            "categoria": 5
        },
            {
            "id": 5,
            "nombre": "Helado de Menta",
            "url": "https://t1.uc.ltmcdn.com/es/posts/4/6/9/como_hacer_helado_de_menta_28964_orig.jpg",
            "categoria": 5
        },
            {
            "id": 5,
            "nombre": "Helado de Vainilla",
            "url": "https://i.pinimg.com/originals/fe/2e/ff/fe2eff0b461f9043018b0f995412805d.jpg",
            "categoria": 5
        }
        ]
        comidasFiltradas = []

        if categoria == "-1":
                # no se deberia filtrar nada
                comidasFiltradas = comidas
        else:
            for c in comidas:
                if c["categoria"] == int(categoria):
                    comidasFiltradas.append(c)

            # TODO: Consultas a BD
            dictResponse = {
                "error": "",
                "categorias": list(comidasFiltradas)
            }
            strResponse = json.dumps(dictResponse)
            return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
