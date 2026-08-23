---
title: Вопросы
---
Распределение вопросов по темам мы можете увидеть в следующей таблице:

```base
filters:
  and:
    - file.ext == "md"
    - file.inFolder("OPD/questions")
properties:
  ticket:
    displayName: № билета
  title:
    displayName: Вопрос
  theme:
    displayName: Тема
  author:
    displayName: Автор
views:
  - type: table
    name: Все вопросы
    order:
      - ticket
      - title
      - theme
      - author
    sort:
      - property: ticket
        direction: ASC
      - property: file.name
        direction: ASC

  - type: table
    name: Представление информации
    filters:
      and:
        - theme == "data-representation"
    order:
      - ticket
      - title
      - author
    sort:
      - property: ticket
        direction: ASC

  - type: table
    name: Основы ОС Unix
    filters:
      and:
        - theme == "unix-os-basics"
    order:
      - ticket
      - title
      - author
    sort:
      - property: ticket
        direction: ASC

  - type: table
    name: БЭВМ
    filters:
      and:
        - theme == "bcomp-programming"
    order:
      - ticket
      - title
      - author
    sort:
      - property: ticket
        direction: ASC

  - type: table
    name: Микрокод
    filters:
      and:
        - theme == "microcode"
    order:
      - ticket
      - title
      - author
    sort:
      - property: ticket
        direction: ASC

  - type: table
    name: Архитектура памяти
    filters:
      and:
        - theme == "memory-architecture"
    order:
      - ticket
      - title
      - author
    sort:
      - property: ticket
        direction: ASC

  - type: table
    name: Сети
    filters:
      and:
        - theme == "networks"
    order:
      - ticket
      - title
      - author
    sort:
      - property: ticket
        direction: ASC

  - type: table
    name: Интерфейсы ввода-вывода
    filters:
      and:
        - theme == "io-interfaces"
    order:
      - ticket
      - title
      - author
    sort:
      - property: ticket
        direction: ASC
```
