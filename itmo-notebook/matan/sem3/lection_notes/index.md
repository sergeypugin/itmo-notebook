---
title: "Список лекций"
---

```base
filters:
  and:
    - file.inFolder("matan/sem3/lection_notes")
    - file.name.startsWith("lection-")
    - file.ext == "md"
formulas:
  c_num: 'number(file.name.replace("lection-", ""))'
properties:
  formula.c_num:
    displayName: №
views:
  - type: table
    name: Все главы
    order:
      - formula.c_num
      - title
    sort:
      - property: formula.c_num
        direction: ASC
```
