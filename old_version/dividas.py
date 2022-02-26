from pprint import pprint

names = {
    'viniciuszeiko':'Gasparini',
    'luizaes':'Luiza',
    'fweiss':'Weiss',
    'jonckjunior':'Jonck',
    'carolinesala':'Carol'
}

dividas = dict()
dividas['gasparini'] = dict(jonck=0,weiss=0,luiza=0)
dividas['luiza'] = dict(gasparini=0,weiss=0,jonckr=0)
dividas['weiss'] = dict(jonck=0,gasparini=0,luiza=0)
dividas['jonck'] = dict(weiss=0,gasparini=0,luiza=0)

def add_div(me,info):
    me = names[me].lower()
    who = info.split()[0].lower()
    value = float(info.split()[1])
    if(dividas[who][me]): pagar_divida(who,me+' '+str(value))
    dividas[me][who] += value

def pagar_div(me,info):
    me = names[me].lower()
    who = info.split()[0].lower()
    value = float(info.split()[1])
    dividas[me][who] -= value

def show_div(me):
    me = names[me].lower()
    t = dividas[me]
    for x in t.items():
        if(x[1]):
            return '{} deve {:.2f} ao {}'.format(x[0].capitalize(),x[1],me.capitalize())