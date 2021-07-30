import re

l="Красивое, лучше чем уродливое."
matches=re.findall("Красивое", l)
print(matches)



l="Красивое, лучше чем уродливое."
matches=re.findall("красивое", l, re.IGNORECASE)
print(matches)



zen = """ Хотя никогда зачастую
лучше, чем прямо сейчас.
Если реализацию сложно
объяснить - идея плоха.
Если реализацию легко объяснить
- идея, возможно, хороша.
Пространства имен - отличная
штука! Будем делать их побольше!
"""

m=re.findall("^Если", zen, re.MULTILINE)
print(m)
m=re.findall("сейчас.$", zen, re.MULTILINE)
print(m)


string="Два даа."
m=re.findall("д[ав]а", string, re.IGNORECASE)
print(m)



line="123?34 привет?"
m=re.findall("\d",
             line,
             re.IGNORECASE)
print(m)



t="__one__ __two__ __three__"
found=re.findall("__.*?__", t)
found2=re.findall("__.*__", t)
print(found)
print(found2)
for match in found:
    print(match)
    
    
    
text = """Жирафы любят таскать
 различные __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__
 целый день напролет. Жирафы
 также славятся тем, что поедают
 прекрасные __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__, но
 после этого у них часто
 болит __ЧАСТЬ_ТЕЛА__. Если же
 жирафы находят __ЧИСЛО__
 __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__, у
 них моментально отваливается __ЧАСТЬ ТЕЛА__.
"""


def mad_libs(mls):
    """
    :param mls: В строках
    пользовательский ввод
    должен быть окружен двойными
    подчеркиваниями. Подчеркивания
    нельзя вставлять в подсказку:
    __подсказка_подсказка__ (нельзя);
    __подсказка__ (можно).
    """
    hints = re.findall("__.*?__",
                      mls)
    if hints is not None:
        for word in hints:
            q = "Введите {}"\
                   .format(word)
            new = input(q)
            mls = mls.replace(word,
                              new,
                              1)
            #1: count	Optional. A number specifying how many occurrences 
            #of the old value you want to replace. Default is all occurrences
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("ошибка ввода")

#mad_libs(text)



line="I love $"
m=re.findall("\\$", #??? same, finds $
             line,
             re.IGNORECASE)
print(m)

line="I love $"
m=re.findall("\$", #??? same, finds $
             line,
             re.IGNORECASE)
print(m)




f=re.findall("[аз]ло", "Привидение прошуршало и исчезло в углу.")
for match in f:
    print(match)

match = re.findall(".ло", "Привидение прошуршало и и исчезло в углу.")
print(match)

#The "\w" means "any word character" which usually means alphanumeric 
#(letters, numbers, regardless of case) plus underscore (_)
f=re.findall("\w+ло", "Привидение прошуршало и исчезло в углу.")
for match in f:
    print(match)
print(f)
    
s="sharing all the information you are hearing"
t=re.findall(r'\b(\w+ing)\b',s)
print(t)