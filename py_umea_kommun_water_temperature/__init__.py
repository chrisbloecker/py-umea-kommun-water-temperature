import requests
import json

url = "https://lora.elsys.se/manage/api_v2.php/sensor/{:}/all?key=Z7SmEmNPt83VC4nWsbRWaR64EjnWsVpYcUulE1beBCY-"

sensors = { "Bettnessand"   : "A81758FFFE044A5A"
          , "Bölesholmarna" : "A81758FFFE044A5E"
          , "Kärleksviken"  : "A81758FFFE044A5B"
          , "Länkebo"       : "A81758FFFE044A59"
          , "Ljumviken"     : "A81758FFFE044A60"
          , "Stöcksjön"     : "A81758FFFE044A62"
          , "Nydalabadet"   : "A81758FFFE044A5C"
          }

def get_temperature(place : str):
    if place in sensors:
        content = requests.get(url.format(sensors[place])).text
        data    = json.loads(content)
        return data[0]["dd"]["exttemp"]
    else:
        raise Exception(f"Unknown place {place}")

def get_bettnessand():
    return get_temperature("Bettnessand")

def get_bolesholmarna():
    return get_temperature("Bölesholmarna")

def get_karleksviken():
    return get_temperature("Kärleksviken")

def get_lankebo():
    return get_temperature("Länkebo")

def get_ljumviken():
    return get_temperature("Ljumviken")

def get_stocksjon():
    return get_temperature("Stöcksjön")

def get_nydalabadet():
    return get_temperature("Nydalabadet")
