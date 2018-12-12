from pprint import pprint

dividas = dict()
dividas['gasp'] = dict(jonck=0,weiss=0)
dividas['jonck'] = dict(gasp=0,weiss=0)
dividas['weiss'] = dict(jonck=0,gasp=0)

def add_divida(me,info):
    who = info.split()[0]
    value = int(info.split()[1])
    if(dividas[who][me]): pagar_divida(who,me+' '+str(value))
    dividas[me][who] += value

def pagar_divida(me,info):
    who = info.split()[0]
    value = int(info.split()[1])
    dividas[me][who] -= value

def show_divida(me):
    t = dividas[me]
    for x in t.items():
        if(x[1]):
            print(x[0],'deve',x[1],'ao',me)


op1 = 'jonck 15'
op2 = 'weiss 1'
op3 = 'jonck 5'
op4 = 'gasp 10'


add('gasp',op1)
add('gasp',op2)
add('gasp',op3)
add('jonck',op4)
show('gasp')


