import re
import transcriptor
from collections import Counter
import matplotlib.pylab as plt
s = "У лукоморья дуб зелёный;\nЗлатая цепь на дубе том:\nИ днём и ночью кот учёный\nВсё ходит по цепи кругом;"
print(s)

print(transcriptor.transcribe(s))

"""
по вертикали звуки
по горизонтали статистика

анализ конкретных стихов (он пришлет)
по стеки у оки
какое то маяковского про смерть есенина
люблю грозу в начале  мая

аллитерация
"""

"""
посмотреть что такое фонетика фоника и пр литературоведческие
холшевников - основы русского стихосложения
"""

def sound_spectre(text, plot=False):
    text = transcriptor.transcribe(text)
    sounds = re.findall(r"[а-я]'*", text)
    result = Counter(sounds)
    for sound in result:
        result[sound] = result[sound] / len(result)

    lists = sorted(result.items())
    if plot:
        x, y = zip(*lists)
        plt.plot(x, y)
        plt.show()
    """
    должны быть текстовые файлы которые мы обрабатываем (какой нибудь фрагмент евгения онегина)
    """
    return result

print(sound_spectre(s))

def sound_spectre_grouped(text):
    text = transcriptor.transcribe(text)
    # Спектр фильтрованный – ищем не все звуки а из какого-то класса (допустим все шипящие) и смотрим как меняется спектр по шипящим. 
    """
    иметь возможность не только Ш но и ШЩ считать за 1 звук (не следующие друг за другом а просто группы)
    еще возможность выбрать звуки: из всех возможных звуков выбираем отдельные и по выбранным делаем спектр
    """

    """
    свистящие: «З», «Зь», «С», «Сь»;
    шипящие: «Ж», «Ш», «Щ», «Ч»;
    твердые: «Ц», «Ш», «Ж», «Н», «Б», «В», «Г», «Д», «З», «К», «Л», «М», «П», «Р», «С», «Т», «Ф», «Х»;
    мягкие: «Й», «Ч», «Щ», «Бь», «Вь», «Гь», «Дь», «Зь», «Кь», «Ль», «Мь», «Нь», «Пь», «Рь», «Сь», «Ть», «Фь», «Хь».
    """

    whistling_count = len(re.findall(r"з|з'|с|с'", text))
    hissing_count = len(re.findall(r"ж|ш|щ'|ч", text))
    hard_count = len(re.findall(r"ц|ш|ж|н|б|в|г|д|з|к|л|м|п|р|с|т|ф|х", text))
    soft_count = len(re.findall(r"й|ч|щ'|б'|в'|г'|д'|з'|к'|л'|м'|н'|п'|р'|с'|т'|ф'|х'", text))
    sum_count = whistling_count + hissing_count + hard_count + soft_count

    return {"свистящие": whistling_count / sum_count, "шипящие": hissing_count / sum_count, "твердые": hard_count / sum_count, "мягкие": soft_count / sum_count}

print(sound_spectre_grouped(s))

def sound_spectre_common(text):
    #???????????????????????????????????????
    # Обобщающий спектр (все шипящие, все гласные итд). 
    # Сначала строку разбиваем на слова с помощью регулярных выражений 
    # (хорошо бы иметь словарь, словарь ударений тк если хотим делать транскриптор гласных, словарь ударений должен быть). 
    # .split лучше не надо т к что делать с дефисами, тире… анализируем эти слова на предмет спектра. 
    pass

def dynamic_spectre(text, window: int):
    # Спектр динамики позволит просматривать фрагмент текста постепенно 
    # (т е будет вызывать звуковой спектр от фрагмента текста но кормить ему разные фрагменты 
    # этого фрагмента текста и показывать результат в зависимости от позиции)
    # calls sound_spectre(text) feeding repositioning window of text (window = number of words)
    pass

def dynamic_spectre_length(text):
    # Другая штука будет вызывать тоже но кормить разные длины этого фрагмента увеличивая постепенно
    # calls sound_spectre(text) feeding different number of words
    pass

def sound_spectre_combinations(text):
    # Звуковой спектр с учетом сочетаний: 
    # Еще есть сочетания звуков которые друг за другом идут и создают характерные сочетания. 
    # Их тоже надо бы вылавливать «дзынь» «дрынь»
    pass

def common_sound_combination(text):
    # Обобщенное сочетание звуков 
    # (обобщаем исходя из того что главный звук в сочетании – второй. А в тех которые первые, они близкие. Или просто по главному звуку)
    pass