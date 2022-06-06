import re
from accentuation import stress

def find_cyrrilic_words(s):
    return re.findall(r'\b[а-яА-ЯёЁ-]+\b', s.lower())

jot_dict={
    # а́е́и́о́у́ы́э́ю́я́
    "ё":"йо", "`ё":"`о",
    "е":"йэ", "`е":"`э",
    "я":"йа", "`я":"`а",
    "ю":"йу", "`ю":"`у",
    }

def jot_function(m):
    s=jot_dict[m.group(1)]
    return s

def jot(s):
    s = re.sub(r'[ьъ]+([ёеюя])',jot_function,s)
    s = re.sub(r'\b(^`)([ёеюя])', jot_function,s)
    s = re.sub(r'(`[ёеюя])', jot_function,s)
    return s

def deafen_and_sharpen(s):
    sharpening_map={"к":"г", "т":"д", "п":"б", "с":"з", "ш":"ж", "ф":"в"}
    deafening_map={"г":"к", "д":"т", "б":"п", "з":"с", "ж":"ш", "в":"ф"}

    sharp_sounds="бгвдзжмнл"
    deaf_sounds="пкфтсшщхцч"

    s = re.sub("гк", "хк", s)

    for k in "бгвдзж":
        s=re.sub(k+r"([" + deaf_sounds + r'])',deafening_map[k]+r'\1',s)

    for sharp_sound in deafening_map:
        # оглушение в конце слов
        s=re.sub(rf"([а-я]+){sharp_sound}([^а-яё`'])", r'\1' + deafening_map[sharp_sound] + r'\2',s)
        # оглушение в конце текста
        s=re.sub(rf"{sharp_sound}$", deafening_map[sharp_sound],s)
    
    for k in "пкфтсш":
        s=re.sub(k + rf"ь([{sharp_sounds}])", sharpening_map[k] + "'" + r'\1',s)

    return s

def soften_vowels(s):
    always_softening_vowels="яёюеиь"
    vowels_map={
        "я":"'а", "`я":"'`а", 
        "ё":"'о", "`ё":"'`о",
        "ю":"'у", "`ю":"'`у", 
        "е":"'э", "`е":"'`э",
        "и":"'и", "`и":"'`и", 
        "ь":"'"
    }
    def soften_function(m):
        item=vowels_map[m.group(1)]
        return m.group()[0] + item

    not_always_hard_consonants="бвгдзклмнпрстфхчщ"

    for consonant in not_always_hard_consonants:
        s=re.sub(consonant+r"(`*[" + always_softening_vowels + r'])', soften_function, s)
    return s

def soften_consonants(s):
    always_soft_consonants="чщ"
    for consonant in always_soft_consonants:
        s = re.sub(rf"{consonant}([^'])", consonant+ "'" + r'\1', s)
    return s

def soften(s):
    s = soften_vowels(s)
    s = soften_consonants(s)
    return s

def accentuate(s):
    s = stress.accentuate(s).lower()
    #s = re.sub(r"(^[^ауоиэыеёюя`]*)[о]([^ауоиэыеёюя]*)", r'\1' + "а" + r'\2', s)
    return s

def remove_hard_sign(s):
    # функция удаляет Ъ из транскрипций
    return re.sub("ъ", "", s)

def simplify_transcription(s):
    result = re.findall(r"`[аеёиоуыэюя]|[бвгджзклмнпрстфхцчшщ'` \n]", s)
    return "".join(result).replace('`', '')

def tsya(s):
    result = re.sub(r"ться|тся", "ца", s)
    return result

def transcribe(s):
    s = accentuate(s)
    s = tsya(s)
    s = soften(s)
    s = deafen_and_sharpen(s)
    s = jot(s)
    s = remove_hard_sign(s)
    s = simplify_transcription(s)
    s = re.sub("^ ","",s)
    s = re.sub("\n ","\n",s)
    s = re.sub("[^\S\r\n]+"," ",s)

    return s

# if __name__=='__main__':
#     s = "У лукоморья дуб зелёный;\nЗлатая цепь на дубе том:\nИ днём и ночью кот учёный\nВсё ходит по цепи кругом;\nнапиться и не всратся;щегол поганый"
#     print(transcribe(s))