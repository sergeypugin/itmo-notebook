# Вопросы

Вопросы на экзамен второго семестра были даны в [[questions.pdf|этом файле]].

Список расписанных вопросов:
```base
filters:
  and:
    - file.inFolder("matan/questions")
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
    name: Luisa
    filters:
      and:
        - note.author == "Luisa"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Lesha
    filters:
      and:
        - note.author == "Lesha"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Ivan
    filters:
      and:
        - note.author == "Ivan"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Oleg
    filters:
      and:
        - note.author == "Oleg"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Dimas
    filters:
      and:
        - note.author == "Dimas"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Nikita
    filters:
      and:
        - note.author == "Nikita"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
  - type: table
    name: Romchik
    filters:
      and:
        - note.author == "Romchik"
    order:
      - formula.q_num
      - title
    sort:
      - property: formula.q_num
        direction: ASC
```
