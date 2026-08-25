# Вопросы

Вопросы на экзамен второго семестра были даны в [[questions.pdf|этом файле]].

Список расписанных вопросов:
```base
filters:
  and:
    - file.inFolder("matan/questions")
    - file.name.startsWith("question")
    - file.ext == "md"
views:
  - type: table
    name: Все вопросы
    order:
      - file.name
      - title
      - author
    sort:
      - property: file.name
        direction: ASC
      - property: title
        direction: DESC
  - type: table
    name: Sergey
    filters:
      and:
        - note.author == "Sergey"
    order:
      - file.name
      - title
  - type: table
    name: Luisa
    filters:
      and:
        - note.author == "Luisa"
    order:
      - file.name
      - title
  - type: table
    name: Lesha
    filters:
      and:
        - note.author == "Lesha"
    order:
      - file.name
      - title
  - type: table
    name: Ivan
    filters:
      and:
        - note.author == "Ivan"
    order:
      - file.name
      - title
  - type: table
    name: Oleg
    filters:
      and:
        - note.author == "Oleg"
    order:
      - file.name
      - title
  - type: table
    name: Dimas
    filters:
      and:
        - note.author == "Dimas"
    order:
      - file.name
      - title
  - type: table
    name: Nikita
    filters:
      and:
        - note.author == "Nikita"
    order:
      - file.name
      - title
  - type: table
    name: Romchik
    filters:
      and:
        - note.author == "Romchik"
    order:
      - file.name
      - title
```
