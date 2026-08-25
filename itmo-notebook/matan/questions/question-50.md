---
title: Полиномы Чебышева и разложения по ним
author: Ivan
links:
  - "[Кудрявцев_Л_Д_Математический_анализ_том_2_2.pdf](https://drive.google.com/file/d/1A9iwsI2Uh7gHamAWOprOR81lh0qZg71d/view?usp=drivesdk)"
---
Данный билет - упрощённая версия [[question-50-original]].

## Полиномы Чебышёва и разложения по ним

### Многочлены Чебышёва первого рода $T_n(x)$

**Определение:**
$$
T_n(x) = \cos(n\arccos x), \quad x \in [-1,1].
$$
При замене $x = \cos\theta$: $T_n(\cos\theta) = \cos(n\theta)$.

Первые значения: $T_0=1$, $T_1=x$, $T_2=2x^2-1$, $T_3=4x^3-3x$.

**Рекуррентное соотношение:**
$$
T_{n+1}(x) = 2x\,T_n(x) - T_{n-1}(x).
$$
*Доказательство:* из тригонометрического тождества $\cos((n+1)\theta)+\cos((n-1)\theta)=2\cos\theta\cos(n\theta)$ при $x=\cos\theta$.

**Ортогональность** на $[-1,1]$ с весом $\frac{1}{\sqrt{1-x^2}}$:
$$
\int_{-1}^{1} T_n(x)T_m(x)\frac{dx}{\sqrt{1-x^2}} = \begin{cases} 0, & n\neq m,\\ \pi/2, & n=m\neq 0,\\ \pi, & n=m=0.\end{cases}
$$
*Доказательство:* замена $x=\cos\theta$ сводит интеграл к $\int_0^\pi\cos(n\theta)\cos(m\theta)\,d\theta$, который вычисляется через формулу произведения косинусов.

### Многочлены Чебышёва второго рода $U_n(x)$

**Определение:**
$$
U_n(x) = \frac{\sin((n+1)\arccos x)}{\sqrt{1-x^2}}, \quad x \in (-1,1).
$$
При $x=\cos\theta$: $U_n(\cos\theta) = \frac{\sin((n+1)\theta)}{\sin\theta}$.

Первые значения: $U_0=1$, $U_1=2x$, $U_2=4x^2-1$.

Рекуррента та же: $U_{n+1}(x) = 2x\,U_n(x)-U_{n-1}(x)$.

**Ортогональность** на $[-1,1]$ с весом $\sqrt{1-x^2}$:
$$
\int_{-1}^{1} U_n(x)U_m(x)\sqrt{1-x^2}\,dx = \begin{cases} 0, & n\neq m,\\ \pi/2, & n=m.\end{cases}
$$
*Доказательство:* замена $x=\cos\theta$ сводит к $\int_0^\pi\sin((n+1)\theta)\sin((m+1)\theta)\,d\theta$.

### Разложения по $T_n$ и $U_n$

**Ряд по $T_n$:**
$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n T_n(x), \quad a_n = \frac{2}{\pi}\int_{-1}^{1} f(x)T_n(x)\frac{dx}{\sqrt{1-x^2}}=$$
$$= \frac{2}{\pi}\int_0^\pi f(\cos\theta)\cos(n\theta)\,d\theta.
$$

**Ряд по $U_n$:**
$$
f(x) = \sum_{n=0}^{\infty} b_n U_n(x), \quad b_n = \frac{2}{\pi}\int_{-1}^{1} f(x)U_n(x)\sqrt{1-x^2}\,dx = $$
$$=\frac{2}{\pi}\int_0^\pi f(\cos\theta)\sin((n+1)\theta)\sin\theta\,d\theta.
$$

Коэффициенты получаются умножением на соответствующий многочлен с весом и использованием ортогональности.

### Связь между родами

$$
T_n'(x) = n\,U_{n-1}(x).
$$
*Доказательство:* дифференцируем $T_n(x)=\cos(n\arccos x)$ по $x$ и сравниваем с определением $U_{n-1}$.

Следствие: если $F(x) = \frac{a_0}{2}+\sum a_n T_n(x)$, то $F'(x)=\sum_{n=0}^\infty (n+1)a_{n+1}U_n(x)$, то есть $b_n = (n+1)a_{n+1}$.
