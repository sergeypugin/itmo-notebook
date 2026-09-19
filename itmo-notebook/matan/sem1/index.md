---
title: Семестр 1
---

## Вопросы

Вопросы на экзамен первого семестра были даны в [[matan/sem1/_questions.pdf|этом файле]].

## О материалах

Билеты перенесены из [презентации «Шпора»](_slides.pdf) (79 слайдов). Формулы набраны в LaTeX, доказательства оформлены отдельными разделами. Названия взяты из экзаменационного списка, названия ссылок — из оглавления [Математического анализа I в Notion](https://profuse-agenda-583.notion.site/I-980946bf5351477db98624c06e198d55).

Всего 43 Markdown-билета: вопросы 33–35 оставлены одним файлом, как в экзаменационном списке. Совместные слайды вопросов 21–22 распределены по двум билетам, повторяющиеся доказательства связаны внутренними ссылками.

> [!warning] Это перенос слайдов, а не полный курс
> Материал, отсутствующий в презентации, не дописывался. Ошибки формул и существенные ограничения исходных формулировок отмечены в самих билетах.

### Отсутствующие и неполные части

- Вопросы [[matan/sem1/question-31|31]], [[matan/sem1/question-32|32]], [[matan/sem1/question-33-35|33–35]], [[matan/sem1/question-40|40]] и [[matan/sem1/question-45|45]] не представлены в слайдах: файлы содержат явные отметки об отсутствии материала.
- В [[matan/sem1/question-4|вопросе 4]] нет меры множества; в [[matan/sem1/question-6|вопросе 6]] рассмотрен только квадратный корень.
- В [[matan/sem1/question-37|вопросе 37]] нет правила Лопиталя, в [[matan/sem1/question-38|вопросе 38]] — дифференциалов высших порядков и доказательства формулы Лейбница, в [[matan/sem1/question-39|вопросе 39]] — бесконечного ряда Тейлора.
- В [[matan/sem1/question-43|вопрос 43]] перенесён критерий выпуклости со слайда 79; определений и точек перегиба в презентации нет.
- Другие локальные пропуски, в том числе оставленные упражнениями бесконечные случаи, отмечены непосредственно в соответствующих билетах.

## Список билетов

```base
filters:
  and:
    - file.inFolder("matan/sem1")
    - file.name.startsWith("question")
    - file.ext == "md"
formulas:
  q_num: 'number(file.name.replace("question-", "").split("-")[0])'
properties:
  formula.q_num:
    displayName: №
views:
  - type: table
    name: Все вопросы
    order:
      - formula.q_num
      - title
      - author
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Sergey
    filters:
      and:
        - list(note.author).contains("Sergey")
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Alllexey
    filters:
      and:
        - list(note.author).contains("Alllexey")
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
```
