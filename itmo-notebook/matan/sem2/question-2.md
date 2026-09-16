---
title: "Основные методы интегрирования"
author: "Sergey"
links:
  - "[2. Свойства неопределенного интеграла. Интегрирование по частям и замена переменной](https://profuse-agenda-583.notion.site/2-bf23c91356ea4e96a212ea7f6060d8eb?pvs=25)"
---
## Основные методы интегрирования

## Замена переменной

### Теорема

Пусть $f$ имеет первообразную на $\langle a,b\rangle$, $\varphi\colon\langle\alpha,\beta\rangle\to\langle a,b\rangle$ дифференцируема. Тогда
$$
\int f(x)\,dx = \int f(\varphi(t))\,\varphi'(t)\,dt\Bigr|_{t=\varphi^{-1}(x)}.
$$

#### Доказательство

Пусть $F$ — первообразная $f$. По теореме о производной сложной функции $F(\varphi(t))$ — первообразная $(f\circ\varphi)\cdot\varphi'$, откуда равенство множеств первообразных. $\square$

На практике: если $x = \varphi(t)$, то $dx = \varphi'(t)\,dt$ — «механическая» замена.

### Пример
$$
\int xe^{x^2}dx = \frac{1}{2}\int e^{x^2}\,d(x^2) = \frac{1}{2}e^{x^2}+C.
$$

## Интегрирование по частям

### Теорема

Пусть $u$, $v$ дифференцируемы на $\langle a,b\rangle$ и существует первообразная $vu'$. Тогда
$$
\int u\,dv = uv - \int v\,du.
$$

#### Доказательство

Из формулы $(uv)' = u'v + uv'$ следует $uv' = (uv)' - u'v$. Интегрируя обе части:
$$
\int uv'\,dx = uv - \int vu'\,dx. \quad\square
$$

### Примеры

$$
\int x\sin x\,dx = \Bigl[\,u=x,\ dv=\sin x\,dx\,\Bigr] = -x\cos x + \int\cos x\,dx = -x\cos x + \sin x + C.
$$
Самосводящийся интеграл (применяем формулу дважды):
$$
\int e^x\sin x\,dx = -e^x\cos x + \int e^x\cos x\,dx = -e^x\cos x + e^x\sin x - \int e^x\sin x\,dx,
$$
$$
\int e^x\sin x\,dx = \frac{e^x(\sin x - \cos x)}{2}+C.
$$
