'''
Created on Aug 21, 2023

@author: daniel
'''
import requests
import json

# url = 'http://127.0.0.1:5000/is_alive'
# response = requests.get(url)
#
# if response.status_code == 200:
#     values = response.json()
#     print("Received values:", values)
# else:
#     print("Error:", response.status_code)
    
    


# url = 'http://127.0.0.1:5000/search_text'
# data = {
#     "all_text": "genera un quiz a crocette come test di ingresso di prima superiore.",
#     "alunno_id": 1
#     }
# response = requests.get(url, params=data)
#
# if response.status_code == 200:
#     values = response.json()
#     print("Received values:", values.get('result'))
# else:
#     print("Error:", response.status_code)
    
    
# url = 'http://127.0.0.1:5000/get_students'
# data = {
#     "alunno_id": 1
#     }
# response = requests.get(url, params=data)
#
# if response.status_code == 200:
#     values = response.json()
#     print("Received values:", values.get('result'))
# else:
#     print("Error:", response.status_code)



# url = 'http://127.0.0.1:5000/get_file_generati'
# data = {
#     "alunno_id": 1
#     }
# response = requests.get(url, params=data)
#
# if response.status_code == 200:
#     values = response.json()
#     print("Received values:", values.get('result'))
# else:
#     print("Error:", response.status_code)
    
    
    
# url = 'http://127.0.0.1:5000/update_alunno'
# data = {
#     "alunno_id": 1,
#     "to_update": json.dumps({
#         "additional_req": "Chi ha vinto la serie A nel 2022?",
#         "fake_attrib": "test fake"
#         })
#     }
# response = requests.get(url, params=data)
#
# if response.status_code == 200:
#     values = response.json()
#     print("Received values:", values.get('result'))
# else:
#     print("Error:", response.status_code)


# url = 'http://127.0.0.1:5000/create_alunno'
# data = {
#     "alunno_id": 1,
#     "to_create": json.dumps({
#         "additional_req": "ma dammi il testo con lettere maiuscole e minuscole alternate.",
#         "fake_attrib": " dgbf",
#         "name": "Giovanniiii",
#         "eta": 89
#         })
#     }
# response = requests.get(url, params=data)
#
# if response.status_code == 200:
#     values = response.json()
#     print("Received values:", values.get('result'))
# else:
#     print("Error:", response.status_code)
    
    

alunni = [
    ['Giovanni Rossi', 30, " ma creami solo 5 domande",  "48qzHgc26cQJ~schAhVP3VLjMSViCsPIQ-kgIKyWW96hIKaRZtxX0cN0dTAidys9KvpA9dfC~im2WqfGuYHBF3eHrJLpSdxIMHLuIJcVuKWb4GD~LLc3AemceV9BHvOm9NZRCGq5joYHv-7TQsqK6pi--THUQ4DVRVi5NshbJlTijHJhmDdXuPAFKLB1yhbUsyRNs~8584m0SWIUDwJlhu-L5I2aPg1iTOgwdnX9jZYeL~q6CtmYgcQkNWXoIz2X4Txi4ANndM4mLuLECaMi7MRK2EdhnVwJnu7XQ~PXGVkCUpG6mcEZDW5UOSUfxFUPw__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"],
    ['Marco Bianchi', 28, " facendo le prime 5 domande molto semplici e le altre cinque molto complesse",   "https://s3-alpha-sig.figma.com/img/49ea/3ccc/a15f777b5cb6a9eb61cc7d40b2aa62d2?Expires=1697414400&Signature=jxSwLbmsttO21Lg91uYLjiSgPRjHuotReXFHVuMuadD5EnevgwQLUwdKw-AF~1PAlcuHhfJt6IFMfEoHFmUlB4mHQ6vE8qGyYpdDUsSGkt5y~GPxS63xKUR7aL75Pv~g9KQUfSelEBn6IOZyz5K-egY-bWUpS0ZSEU~26V8NGJCvIVKjt9aL8GAx02IYfOqz-NL9ee0iiNKYCGj8CEj8dGRNuquhlbrh~ybDqJb2~71hEi9m~sVcV28x8jfZlNfBmrHCDoB1Be-pWDWjwf0X0mohkqVtPe~5BFoOAKkc54-QpJ4MPzBgt1dA3IxQ6WrEZXgfPqhuxUvc8kgcV0TdwQ__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"],
    ['Maria Russo', 25, " con domande che toccano vari temi",     "https://s3-alpha-sig.figma.com/img/a840/f091/1e90cb31bb602fdfeba32c552f575cae?Expires=1697414400&Signature=Vvdn4dxX-O5L7dbZ4iqs66rb0tZD2dlfObB1YAa1ADhhd7lLGbcYYNnrq8bjlEsnRsTooXtSMw0NIArA6rlQK6JokEDqwTDUoNeF-Gl2DnCCPPx7xQ7gXr2eh4nb31CiIEp-W9I7EdyOFdy5gzKBueMRgPlIumJMYDWDi02bqW4mKigNr5ZIa-y5lRj466v9XkhEkYUhmIBCT297CEZbo1RdcZkjkj41DauEi6bGEPpG4cniiyWWG4ylUnwufrrK8CoXC~jNJj-eOxovN0t6hsjQxErDjBo~2WXQclUf-0T1Z7PIz-SHVkf5o1YW4ChpFJ-H2xSPHIJ39CHYFvubhg__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"],
    ['Laura Esposito', 32, " usando solo addizioni",  "https://s3-alpha-sig.figma.com/img/713f/5eb3/acace5ff076951a42883b4c1d5f1cca1?Expires=1697414400&Signature=GA2nzqxGx9UKFXcVJHzJR2W~rFVAplGzjjYrPN0ARowQPYjj6dtqM9FixOiWEotWro8odyQ~bip~SsT5URbuUJGOFjZ0~pKXf1TKlEL-n9FBVESZOiHhKUfUp7R6XCI3CFlrD43reV1QKl64CK5krGLsz2n1fUY-R7jLOM4E1aTb3hI0Vi4oeiNTJ1kK0ajw9FFP8nnlc7lzr6AGgLNkiezezY-CwR-VuDEaxPPpmgGpiM48kO2huYPXbkGfERQbXoFRBGOJmuhzgsheqkhMrWSNxX9RhnrVKZ~8LtsOnFT9aIWwFZDb27MRTczfRTLbcqlUOxngo3yVUOcjDDoioQ__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"],
    ['Anna Martini', 27, " usando solo sottrazioni",    "https://s3-alpha-sig.figma.com/img/23e6/0144/b7caabc004af4808d3d8a5529ce2e2b5?Expires=1697414400&Signature=MsW5yYgmaaWtWgkhzo9tDwCNFMnYNwh2p8NIVHLA9wl3w9tgP7FfHWESWa34V5dSGJC0-zouZpdLz6-nrckHbYY2iZ7BrrCMj1LDyOkZLkjkVhwgNb0jeHQVhFzAaLO9Jh4sbfxjFK8qX0gL-HudSNXk~klME067jWTcU8HYLbGIuQvalbk46PGQKJhE06R7P8d0qm-Nt3NVSkyAYZL~PpXYuzEZSRnzEO7aGsCVi-nDh6lvvo14PGbllBnNz8LzHgwG38d4NC3w6BE71kdWFpeHBYzHBJOuhIr0RXFAs52ZxK~0CPqAER1QS6wqmkfTyos0oBSCN0oT7FdjeQroiA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"],
    ['Sofia Ferrari', 29, " solo divisioni",   "https://s3-alpha-sig.figma.com/img/2274/d0d1/4c1980e089dfda05334c2bbf424831fb?Expires=1697414400&Signature=L~XyyYYdfFzxz3dlyLu6lKJpjz~9b1q64yIizYjV4sABRtx3Q9uMYOIvnrQLeYDdGZqDQdIiDK6qEFYfHG5OAJ3tRw2Xe0yoVhayYxJYPZGQk0X6Ha-bGtzfk7uDe8-VJww~7mrVCsLSPIcQZyIiSz~0Wmd3ehEhs1s7UbYJIES75kQ1JfWCbhURUHdGdTHyDl3jscQPODI6YtKlMgszB17gdEkV0HOhRh1hqkl-4n1sbW5L2rnEPwpRvJASy6PyHpP4siBpv9Bm-0PbEk3Pr7A-ue1Xo5IhuEhTnz3MClVw8icNhp~AM291-xy5kq8WX0KAeN6xRO-eGTS~amfEzA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"],
    ['Giulia Conti', 26, "solo tre domande",    "https://s3-alpha-sig.figma.com/img/e722/0ebc/5950f4d3287e1169bc98b8802490233c?Expires=1697414400&Signature=KAe3EPz6ES-4gGKxfELbUbRVmmPPrgFFmTzcAyEpTn5eY9jFsT1FVeMltE3htK8dIyJUtXuonF7pvyQdO6MI0rMmPSC1Gep8miYDGLN9pinEYfF3SrRMM3G5pcVJ9Su6AwXJImmRcUBZqR4TlHU76JT3aylhS4u707Zrqbqe66cfIkrVwIUrmyeDpu8RVkVUQXICAMT62s~CV7rcGAol3CvxnvbqxUY2pt4ufXZOr3si9uiOIkZa47zGP3tuaXAhC6JDgLo0oF2JDiifds8JMQBmQL1xdjxjkcabVZBkDtxMQeR62ld--CaC293Km12l91k5uJMD1K0lnp~IoW70jA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"],
    ['Elena Romano', 31, " 7 domande in ordine crescente di difficoltà",    "https://s3-alpha-sig.figma.com/img/e7ec/8fe2/83118f026c26cc521f718e10153b7478?Expires=1697414400&Signature=KYfoSSp-zgVM~BEpdkzfwgBD4VI-jH8hXydyVbc5374uNr5SkLlORk-0hX-Hf9EX9rye2a4ObBkp7Nak2jmWibGmhpj~PZ~Ub2TDaDdzRwEum2ssxRL-pbQt5qYFP6B4DGtoCEqAy13nPd2xFTrw3sxdhQefygPHFcmfv4VPNwtMG8U1ef~KnNCY9qVti3yK2dwkJ8GXHR3LB~vz~po~nXCw9c~gIdpr8wNJwmgTPbbp9H6jyiyhHkaI228rZOTWgaALN6lm1TLtcuYeHvrdtxcJSX6A1yFUBKQe50Hn9TCgEPSS52LOSTnFyaGPbCQ0s0xvZghz1KBfETbqjtRdXw__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4"],
]
        
for name, age, ext, image in alunni:
    url = 'http://127.0.0.1:5000/create_alunno'
    data = {
        "to_create": json.dumps({
            "additional_req": ext,
            "name": name,
            "eta": age,
            "image_url": image
            })
        }
    print("Created %s" % (name))
    response = requests.get(url, params=data)
    
    if response.status_code == 200:
        values = response.json()
        print("Received values:", values.get('result'))
    else:
        print("Error:", response.status_code)
    
    