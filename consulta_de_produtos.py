import PySimpleGUI as sg

refs = {"01":"REF:01 – 212",
       "02":"REF:02 – 212 VIP ROSÊ",
       "03":"REF:03 –SEXY",
       "04":"REF:04 – 212 VIP",
       "05":"REF:05 – CHANEL",
       "06":"REF:06 – COCO CHANEL MADEIMOSELLE",
       "07":"REF:07 – LLURE",
       "08":"REF:08 – DOLCE GABBANA the one",
       "09":"REF:09 – DOLCE GABBANA light blue",
       "10":"REF:10 – DOLCE GABBANA red",
       "11":"REF:11 – DESIRE",
       "12":"REF:12 – FANTASY",
       "13":"REF:13 – FANTASY MIDNIGHT",
       "14":"REF:14 – ANGEL",
       "15":"REF:15 – ANGEL OU DEMON",
       "16":"REF:16 – CH CH",
       "17":"REF:17 – GOOG GIRL",
       "18":"REF:18 – rouge royal - MARINA DE BOURBON",
       "19":"REF:19 – Dynastie",
       "20":"REF:20 – CK",
       "21":"REF:21 - EUPHORIA",
       "22":"REF:22 – ETERNITY",
       "23":"REF:23 – LADY MILLION",
       "24":"REF:24 – BLACK XS",
       "25":"REF:25 – OLYMPEA",
       "26":"REF:26 – MISS DIOR",
       "27":"REF:27 – JADORE",
       "28":"REF:28 –  AMOR AMOR",
       "29":"REF:29 – ANAIS ANAIS",
       "30":"REF:30 – LAU LAU",
       "31":"REF:31 – LA VIE EST BELLE",
       "32":"REF:32 – HYPNÓSE",
       "33":"REF:33 – NINA",
       "34":"REF:34 – KENZO",
       "35":"REF:35 – MONT BLANC",
       "36":"REF:36 – LAGUNA",
       "37":"REF:37 – LOVE ANIMALE",
       "38":"REF:38 – GABRIELA SABATINI",
       "39":"REF:39 – CHLOÉ",
       "40":"REF:40 -  HUGO",
       "41":"REF:41 - AMARIGE",
       "42":"REF:42 – SÌ",
       "A01":"REF:A01 – SCANDAL",
       "A02":"REF:A02 – ALIEN",
       "A03":"REF:A03 – AURA MUGLER",
       "A04":"REF:A04 – OLYMPEA AQUA",
       "43":"REF:43 – 212 MEN",
       "44":"REF:44 – 212 VIP MEN",
       "45":"REF:45 – 212 SEXY MEN",
       "46":"REF:46 -  CH MEN",
       "47":"REF:47 – CH PRIME",
       "48":"REF:48 – ALLURE CHANEL SPORT",
       "49":"REF:49 – BLEU CHANEL",
       "50":"REF:50 – COCO CHANEL",
       "51":"REF:51 – ONE MILLION",
       "52":"REF:52 – INVICTUS",
       "53":"REF:53 – BLACK MS",
       "54":"REF:54 – DOLCE GABBANA",
       "55":"REF:55 – ARMANI",
       "56":"REF:56 – ARMANI CODE",
       "57":"REF:57 – FAHRENHEIT - DIOR",
       "58":"REF:58 – SAUVAGE",
       "59":"REF:59 – DIESEL",
       "60":"REF:60 – DIESEL ONLY",
       "61":"REF:61 – AZZARO",
       "62":"REF:62 – SILVER BLACK",
       "63":"REF:63 – SILVER SCENT",
       "64":"REF:64 – EUPHORIA MEN",
       "65":"REF:65 – ETERNITY",
       "66":"REF:66 – CK",
       "67":"REF:67 – FERRARI RED",
       "68":"REF:68 – FERRARI BLACK",
       "69":"REF:69 – JOOP RED",
       "70":"REF:70 – JOOP BLUE",
       "71":"REF:71 – POLO BLACK",
       "72":"REF:72 – POLO BLUE",
       "73":"REF:73 – POLO GREEN",
       "74":"REF:74 – POLO RED",
       "75":"REF:75 – POLO SPORT",
       "76":"REF:76 – LACOSTE",
       "77":"REF:77 – ANIMALE",
       "78":"REF:78 – ACQUA DI GIORGIO ARMANI",
       "79":"REF:79 – LAPIDUS",
       "80":"REF:80 – KOUROS",
       "81":"REF:81 – HUGO BOSS",
       "82":"REF:82 – MONT BLANC",
       "83":"REF:83 – JEAN PAUUL GAULTIER",
       "84":"REF:84 – BVLGARI",
       "85":"REF:85 – ONE MILLION LUCKY",
       "85":"REF:86 – BVLGARI AQUA",
       "87":"REF:87 – 212 VIP BLACK",
       "88":"REF:88 – INVICTUS INTENCE"}


l = []

layout = [
         [sg.Text("Digite um valor:")],
         [sg.Text("REFS:"),sg.Input(size=(25,0),key='txt_input',enable_events=True), sg.Button("OK",size=(5,0),bind_return_key=True),sg.Button('RESET')],
         [sg.Output(key='OUT',size=(50,10))],
         [sg.Button('Save'),sg.Button('Close')]
         ]
window = sg.Window("Catalogo").layout(layout)


while True:
    event, values = window.Read()
    inp = values['txt_input']
    
    if event == 'OK' and inp.upper() in refs:
        l.append(refs[inp.upper()])
        print(refs[inp.upper()])
        window['txt_input']('')
    elif event == 'OK' and inp.upper() not in refs:
        print('Digite um valor válido')
        window['txt_input']('')
        pass
    elif event == 'Save':
        l.sort()
        print('\nLista com {} produtos:\n'.format(len(l)))
        for e in l:
            print(str(e) + " 50ml/100ml")
    elif event == 'RESET':
        l.clear()
        window['OUT']('')
        print('A lista de produtos esta vazia')
    elif event == sg.WIN_CLOSED or event in (None, 'Close'):
        window.close()
        break