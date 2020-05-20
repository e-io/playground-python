# Multifilter
Must implement the multifilter class, which is an extended functionality of the standard filter class.

A normal filter accepts a sequence and function. Returns a sequence (more precisely, a sequence iterator) in which elements are filtered out for which the function had a false value (False, None, 0, etc.)

The multifilter should do the same, but take not one function, but an unlimited number and filter out all the elements that at least no function missed (did not give the answer True).

Additionally, the multifilter has the judge parameter, which can be set to filter out elements that at least one function did not miss, or set to filter out elements that half of the functions did not miss

Input example: test.py
Example of output: comments in test.py

The idea of the problem is taken from https://stepik.org/lesson/24464/step/4?discussion=1734792&thread=solutions&unit=6769
___________
## Множественный фильтр

Необходимо реализовать класс multifilter, являющийся расширенным функционалом  стандартного класса filter.

Обычный фильтр принимает последовательность и функцию. Выдает последовательность (точнее, итератор по последовательности), в которой отсеяны элементы по котором функция имела ложное значение (False, None, 0 и т.п.)

Мультифильтр должен делать то же самое, но брать не одну функцию, а неограниченное число и отсеивать все элементы, которые хоть никакая фунция не пропустила (не дала ответ True).

Дополнительно у мультифильтра есть параметр judge, который можно задать так, чтобы отсеивались элементы, которые не пропустила хоть одна функция или задать так, чтобы отсеивались элементы, которые не пропустила половина функций

Пример ввода: test.py
Пример вывода: комментарии в test.py

Идея задачи взята с https://stepik.org/lesson/24464/step/4?discussion=1734792&thread=solutions&unit=6769