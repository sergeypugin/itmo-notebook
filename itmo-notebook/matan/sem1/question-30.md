---
title: "30. Равномерная непрерывность. Теорема Кантора"
author:
  - Alllexey
  - Sergey
links:
  - "[46. Равномерная непрерывность. Теорема Кантора](https://profuse-agenda-583.notion.site/46-48cf79b4aacd407ea13bdbc422900e32)"
---

## Равномерная непрерывность

> [!info] Определение
> Функция $f:E\to\mathbb R$ равномерно непрерывна на $D\subseteq E$, если
>
> $$
> \forall\varepsilon>0\ \exists\delta=\delta(\varepsilon)>0\ \forall x,x'\in D:
> \quad |x-x'|<\delta\Rightarrow |f(x)-f(x')|<\varepsilon.
> $$

## Теорема Кантора

> [!important] Теорема
> Непрерывная на отрезке функция равномерно непрерывна на нём.

### Доказательство через конечное покрытие

Пусть $f\in C[a,b]$ и $\varepsilon>0$. Для каждой точки $t\in[a,b]$ выберем $\delta_t>0$, такое что

$$
x\in U_{\delta_t}(t)\cap[a,b]
\Rightarrow |f(x)-f(t)|<\frac\varepsilon2.
$$

Окрестности **половинных радиусов** $U_{\delta_t/2}(t)$ покрывают $[a,b]$. По лемме Бореля–Лебега выделим конечное покрытие

$$
U_{\delta_1/2}(t_1),\ldots,U_{\delta_n/2}(t_n).
$$

Положим $\delta'=\min\{\delta_1/2,\ldots,\delta_n/2\}>0$. Пусть $x,x'\in[a,b]$ и $|x-x'|<\delta'$.

Выберем $i$, для которого $x\in U_{\delta_i/2}(t_i)$. Тогда

$$
|x'-t_i|\le|x'-x|+|x-t_i|
<\delta'+\frac{\delta_i}{2}\le\delta_i.
$$

Обе точки лежат в $U_{\delta_i}(t_i)$, поэтому

$$
|f(x)-f(x')|
\le|f(x)-f(t_i)|+|f(t_i)-f(x')|
<\frac\varepsilon2+\frac\varepsilon2=\varepsilon.
$$

Число $\delta'$ выбрано сразу для всех $x,x'$, что доказывает равномерную непрерывность.

## Источник

[«Шпора», слайд 65](_slides.pdf#page=65).
