---
title: "2. Отображения и функции"
author:
  - Alllexey
  - Sergey
links:
  - "[3. Функции и отображения](https://profuse-agenda-583.notion.site/3-61e1baa337254818b783cdb8a66e6342)"
---

## Отображение и функция

> [!info] Определение
> Отображение $f:X\to Y$ — правило, сопоставляющее каждому $x\in X$ ровно один элемент $y\in Y$.

В записи $y=f(x)$ переменная $x$ называется **аргументом**, или независимой переменной, а $y$ — **значением отображения**, или зависимой переменной.

- **Область определения:** $D(f)=X$.
- **Область значений:** $E(f)=\{y\in Y:\exists x\in X\ f(x)=y\}$.
- **График:** $\Gamma_f=\{(x,y)\in X\times Y:y=f(x)\}$.

## Образ и прообраз

Для $A\subseteq X$ его **образ** равен

$$
f(A)=\{y\in Y:\exists x\in A\ f(x)=y\}.
$$

Для $B\subseteq Y$ его **полный прообраз** равен

$$
f^{-1}(B)=\{x\in X:f(x)\in B\}.
$$

### Свойства

Для $A,B\subseteq X$:

1. $A\subseteq B\Rightarrow f(A)\subseteq f(B)$.
2. $f(A\cap B)\subseteq f(A)\cap f(B)$.
3. $f(A\cup B)=f(A)\cup f(B)$.

Для $A',B'\subseteq Y$:

4. $A'\subseteq B'\Rightarrow f^{-1}(A')\subseteq f^{-1}(B')$.
5. $f^{-1}(A'\cap B')=f^{-1}(A')\cap f^{-1}(B')$.
6. $f^{-1}(A'\cup B')=f^{-1}(A')\cup f^{-1}(B')$.
7. При $B'\subseteq A'$: $f^{-1}(A'\setminus B')=f^{-1}(A')\setminus f^{-1}(B')$.
8. $f^{-1}(Y\setminus A')=X\setminus f^{-1}(A')$.

### Доказательства

**1.** Если $y\in f(A)$, то $y=f(x)$ для некоторого $x\in A$. Из $A\subseteq B$ следует $x\in B$, поэтому $y\in f(B)$.

**2.** Если $y\in f(A\cap B)$, существует $x\in A\cap B$ с $y=f(x)$. Тогда $x\in A$ и $x\in B$, значит $y\in f(A)\cap f(B)$.

**3.** По определению образа:

$$
\begin{aligned}
y\in f(A\cup B)
&\iff \exists x\in A\cup B:\ y=f(x)\\
&\iff y\in f(A)\ \lor\ y\in f(B)\\
&\iff y\in f(A)\cup f(B).
\end{aligned}
$$

**5.** По определению прообраза:

$$
\begin{aligned}
x\in f^{-1}(A'\cap B')
&\iff f(x)\in A'\cap B'\\
&\iff f(x)\in A'\ \land\ f(x)\in B'\\
&\iff x\in f^{-1}(A')\cap f^{-1}(B').
\end{aligned}
$$

Доказательства пунктов 4 и 6–8 на слайдах оставлены в качестве упражнения.

## Инъекция, сюръекция и биекция

- **Инъекция:** различные аргументы имеют различные образы:
  $x_1\ne x_2\Rightarrow f(x_1)\ne f(x_2)$.
- **Сюръекция:** $E(f)=Y$.
- **Биекция:** отображение одновременно инъективно и сюръективно.

### Обратное отображение

Для биекции $f:X\to Y$ отображение $f^{-1}:Y\to X$ задаётся правилом

$$
x=f^{-1}(y)\iff y=f(x).
$$

При этом

$$
(f\circ f^{-1})(y)=y,\qquad (f^{-1}\circ f)(x)=x.
$$

## Композиция

Для $f:X\to Y$ и $g:Y\to Z$ композиция $g\circ f:X\to Z$ определяется равенством

$$
(g\circ f)(x)=g(f(x)).
$$

### Ассоциативность композиции

Если $f:X\to Y$, $g:W\to X$, $h:Z\to W$, то

$$
(f\circ g)\circ h=f\circ(g\circ h).
$$

**Доказательство.** Для любого $z\in Z$ обе части равны $f(g(h(z)))$.

## Источник

[«Шпора», слайды 3–5](_slides.pdf#page=3).
