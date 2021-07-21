def text_to_vk_inters(lines):
    lines = lines.split('\n')
    result = []
    max = 42
    for line in lines:
        to_underscore = [' ', '-', ':']
        for s in to_underscore:
            line = line.replace(s, '_')
        length = len(line)
        if length > max:
            line = line[0:max]
        elif length < max:
            line = line + '_' * (max-length)
        result.append(line)
    return('\n'.join(result))

def test():
    Подкасты = '''
Любимые подкасты

IT:
- О Чём Речь
- Вы находитесь здесь
- Запуск Завтра
- Podlodka Podcast
- АйТиБорода
- Moscow Python
                              
Наука:
- Голый землекоп
- The Big Beard Theory

Чай:
- Пуэр FM
- TeaPOD
               
Другие темы:
- Laowaicast (о Китае)
- ObRetu.ru (саморазвитие)           
'''

    Музыка = '''
Медитативная
- LinDi
- Yoko Kanno

Со смыслом
- Нейромонах Феофан
- Научно-технический рэп

Вокал
- Regina Spektor
'''
    Ютуб = '''
Любимые каналы на Ютубе

Путешествия 
- Орел и Решка 
- DW на русском 

Общество 
- Кацламовщина
- DW на русском 
 
Чай 
- Чай без церемоний
- Сергей Шевелев

Юмор
- Barakuda
- Мед
 
Наука 
- Kurzgesagt
- Veritasium 
'''

    interests = {
        'podcasts': Подкасты[1:-1],
        'music': Музыка[1:-1],
        'youtube': Ютуб[1:-1],
    }
    result = text_to_vk_inters(interests['youtube'])
    print(result)


if __name__ == '__main__':
    test()
