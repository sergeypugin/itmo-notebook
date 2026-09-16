---
title: Семестр 1
---
# Вопросы

Вопросы на экзамен первого семестра были даны в [[matan/sem1/_questions.pdf|этом файле]].

Список расписанных вопросов:
```base
filters:
  and:
    - file.inFolder("matan/sem1")
    - file.name.startsWith("question")
    - file.ext == "md"
formulas:
  q_num: 'number(file.name.replace("question-", "").replace("-original", ""))'
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
        - note.author == "Sergey"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Sergey
    filters:
      and:
        - note.author == "Alllexey"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
```
