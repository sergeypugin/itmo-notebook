---
title: "20. Пределы функций по Коши и по Гейне. Равносильность этих двух определений"
author:
  - Alllexey
  - Sergey
links:
  - "[28. Понятие предела функции «по Коши»](https://profuse-agenda-583.notion.site/28-e512f4a7fced41639d814057f12ebeac)"
  - "[29. Понятие предела функции «по Гейне»](https://profuse-agenda-583.notion.site/29-403226484f29450f91f8b9cf4d8290f3)"
---

## Предел функции по Коши

Пусть $f:E\to\mathbb R$, а $x_0$ — предельная точка $E$.

> [!info] Определение для $x_0,A\in\mathbb R$
> Равенство $\lim_{x\to x_0}f(x)=A$ означает
>
> $$
> \forall\varepsilon>0\ \exists\delta>0\ \forall x\in E:
> \quad 0<|x-x_0|<\delta\Rightarrow |f(x)-A|<\varepsilon.
> $$

### Определение через окрестности

Для любой окрестности $V(A)$ существует проколотая окрестность $\mathring U(x_0)$, такая что

$$
f(\mathring U(x_0)\cap E)\subseteq V(A).
$$

**Эквивалентность.** В произвольную окрестность $V(A)=(\alpha,\beta)$ можно вписать $\varepsilon$-окрестность с $\varepsilon=\min\{A-\alpha,\beta-A\}$. Определение Коши даёт подходящую $\delta$-окрестность аргумента. Обратно, применяем окрестностное определение к $V_\varepsilon(A)$ и выбираем внутри полученной окрестности аргумента некоторую $\delta$-окрестность.

## Предел функции по Гейне

> [!info] Определение
> $A\in\overline{\mathbb R}$ — предел $f$ в точке $x_0\in\overline{\mathbb R}$, если для **любой** последовательности
>
> $$
> x_n\in E,\qquad x_n\ne x_0,\qquad x_n\to x_0
> $$
>
> выполнено $f(x_n)\to A$.

## Равносильность определений

> [!important] Теорема
> Определения предела по Коши и по Гейне эквивалентны.

### Из Коши следует Гейне

Пусть $x_0,A\in\mathbb R$, и выполнено определение Коши. Для $\varepsilon>0$ выберем $\delta>0$, такое что

$$
x\in E,\quad0<|x-x_0|<\delta\Rightarrow |f(x)-A|<\varepsilon.
$$

Если $x_n\to x_0$ и $x_n\ne x_0$, то для достаточно больших $n$ имеем $0<|x_n-x_0|<\delta$. Следовательно, $|f(x_n)-A|<\varepsilon$, то есть $f(x_n)\to A$.

### Из Гейне следует Коши

Предположим, что определение Коши не выполнено. Тогда

$$
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in E:
\quad0<|x-x_0|<\delta,\quad |f(x)-A|\ge\varepsilon_0.
$$

Для $\delta_n=1/n$ выберем соответствующие $x_n$. Получаем $x_n\in E$, $x_n\ne x_0$ и $x_n\to x_0$, но $|f(x_n)-A|\ge\varepsilon_0$ при всех $n$. Значит, $f(x_n)$ не стремится к $A$, вопреки определению Гейне.

## Примеры определений на бесконечности со слайда

$$
\lim_{x\to-\infty}f(x)=+\infty
\iff
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in E:
\quad x<-\frac1\delta\Rightarrow f(x)>\frac1\varepsilon.
$$

$$
\lim_{x\to+\infty}f(x)=A\in\mathbb R
\iff
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in E:
\quad x>\frac1\delta\Rightarrow |f(x)-A|<\varepsilon.
$$

> [!warning] Пробел в доказательстве
> Равносильность Коши и Гейне подробно доказана только для конечных $x_0$ и $A$. Остальные случаи на слайдах оставлены упражнениями.

## Источник

[«Шпора», слайды 35–37](_slides.pdf#page=35).
