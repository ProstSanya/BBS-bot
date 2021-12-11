from random import randint
print('Хай! Я BBS-bot. Давай поболтаем о чем-нибудь. Нихрена пока не знаю, но быстро учусь)')
print('И еще, чтобы закончить введи "Пока"')
l_rq = ['Я слишком глуп Повелитель, что мне в будущем вам ответить на это?', 'Я не знаю, что ответить. Как надо?', 'Сори, я немного не понял. Объясни, что мне говорить', 'И что мне на это отвечать?']
pod_b=['Слушаю','Что дальше?','Внимаю вашему слову, Владыка!']
bb=['Ууу слился','Ладно бывай','Буду ждать вас вновь, Владыка!']
a = 0
open('в-о.txt','w')
while True:
    while True:
        fr = input('-->').lower()
        fr = fr.split()
        sl = ""
        for i in fr:
            sl = sl + i
        with open("в-о.txt", "r") as vopr:
            for line in vopr:
                line = line.strip()
                line = line.split(":")
                if line[0] == sl:
                    print(line[1])
                    a = -1
                    print(pod_b[randint(0, 2)])
                elif sl == "пока":
                    a = -1
                    break
        a = a+1
        if sl == "пока":
            print(bb[randint(0, 2)])
            exit()
        elif a == 1:
            break
    if a == 1:
        print(l_rq[randint(0, 3)])
        k = input('-->')
        print("Ок я запомнил:", k)
        print(pod_b[randint(0, 2)])
        dob = sl + ":" + k
        with open("в-о.txt", "a") as otv:
            otv.write(dob + '\n')