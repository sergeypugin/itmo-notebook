---
title: "Специальные функции, задаваемые определенными интегралами: Гамма-функция, Интеграл вероятности, Интегральные синус (Si) и косинус (Ci), Эллиптические интегралы, Интегралы Френеля"
author: "Oleg"
links:
  - "[Старков.pdf](https://drive.google.com/file/d/15dyVcOLYvRGXzo-sKg3NRY5eRYYYYO-e/view?usp=drivesdk)"
  - "[Зорич 2 часть.pdf](https://drive.google.com/file/d/1940bipaz-BE3m5uGkuGskZCHAKCG-f91/view?usp=drivesdk)"
---
## Специальные функции, задаваемые несобственными интегралами

### 1. Гамма-функция

#### Определение

**Гамма-функцией Эйлера** называется:
$$ \Gamma(\alpha) := \int_0^{+\infty} x^{\alpha - 1} e^{-x} dx $$
#### Область определения

Интеграл имеет две потенциальные особенности:

- **В нуле** ($\alpha < 1$): подынтегральная функция ведёт себя как $x^{\alpha-1}$, а именно как $\frac{1}{x^{1-\alpha}}$, интеграл сходится при $1- \alpha < 1$, то есть при $\alpha > 0$.
- **На бесконечности**: множитель $e^{-x}$ гасит любую степень, интеграл сходится при любом $\alpha \in \mathbb{R}$.

Таким образом, $\Gamma(\alpha)$ определена при $\alpha > 0$.

#### Рекуррентная формула (формула понижения)

**Утверждение**: $$ \Gamma(\alpha + 1) = \alpha\Gamma(\alpha), \quad \alpha > 0 $$

#### Доказательство

Интегрируем по частям, полагая $u = x^\alpha$,  $dv = e^{-x}dx$, то есть $du = \alpha x^{\alpha - 1}dx$,  $v = -e^{-x}$: $$ \Gamma(\alpha + 1) = \int_0^{+\infty} x^\alpha e^{-x} dx = \left[-x^\alpha e^{-x}\right]_0^{+\infty} + \alpha \int_0^{+\infty} x^{\alpha-1} e^{-x} dx $$

Граничный член: при $x \to +\infty$ имеем $x^\alpha e^{-x} \to 0$ (экспонента побеждает любую степень); при $x = 0$ имеем $0^\alpha \cdot 1 = 0$ при $\alpha > 0$. Итого: $$ \Gamma(\alpha + 1) = 0 + \alpha\Gamma(\alpha) = \alpha\Gamma(\alpha).$$

#### Связь с факториалом

Из определения: $\Gamma(1) = \int_0^{+\infty} e^{-x}dx = 1$. Применяя рекуррентную формулу $n$ раз: $$ \Gamma(n+1) = n \cdot \Gamma(n) = n(n-1)\cdot\Gamma(n-1) = \cdots = n!\cdot\Gamma(1) = n! $$

---

### 2. Интеграл вероятности

#### Определение

$$ \operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt $$

Дополнительная функция ошибок: $\operatorname{erfc}(x) = 1 - \operatorname{erf}(x)$.

#### Свойства

- $\operatorname{erf}(x)$ — нечётная: $\operatorname{erf}(-x) = -\operatorname{erf}(x)$.
- $\operatorname{erf}(0) = 0$, $\lim_{x\to+\infty}\operatorname{erf}(x) = 1$.

---

### 3. Интегральные синус и косинус

#### Определения

$$ \operatorname{Si}(x) = \int_0^x \frac{\sin t}{t} dt, \qquad \operatorname{Ci}(x) = -\int_x^{+\infty} \frac{\cos t}{t} dt \quad (x > 0) $$

#### Поведение на бесконечности

Из вычисления интеграла Дирихле: $$ \operatorname{Si}(+\infty) = \int_0^{+\infty} \frac{\sin t}{t},dt = \frac{\pi}{2} $$

Для $\operatorname{Ci}$: интеграл $\int_x^{+\infty} \frac{\cos t}{t},dt$ сходится условно по признаку Дирихле и $\operatorname{Ci}(x) \to 0$ при $x \to +\infty$.


---

### 4. Эллиптические интегралы

#### Определения

Эллиптические интегралы возникают при вычислении длины дуги эллипса и в задачах о маятнике. Они делятся на три рода:

- **Первого рода:** $$ F(\varphi, k) = \int_0^{\varphi} \frac{d\theta}{\sqrt{1 - k^2 \sin^2\theta}} $$
    
- **Второго рода:** $$ E(\varphi, k) = \int_0^{\varphi} \sqrt{1 - k^2 \sin^2\theta} d\theta $$
    
- **Третьего рода:** $$ \Pi(n, \varphi, k) = \int_0^{\varphi} \frac{d\theta}{(1 - n\sin^2\theta)\sqrt{1 - k^2\sin^2\theta}} $$
    

Здесь $k \in (0,1)$ это эксцентриситет, $n$ — параметр. При $\varphi = \pi/2$ говорят о **полных** эллиптических интегралах $K(k) = F(\pi/2,k)$ и $E(k) = E(\pi/2,k)$.

#### Физический смысл

Период колебаний математического маятника длины $l$ при амплитуде $\theta_0$ равен: $$ T = 4\sqrt{\frac{l}{g}} F\left(\frac{\pi}{2}, \sin\frac{\theta_0}{2}\right) $$

Длина дуги эллипса $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ с эксцентриситетом $e = \sqrt{1 - b^2/a^2}$ равна $4aE(e)$.


---

### 5. Интегралы Френеля

#### Определения

$$ C(x) = \int_0^x \cos\left(\frac{\pi t^2}{2}\right) dt, \qquad S(x) = \int_0^x \sin\left(\frac{\pi t^2}{2}\right) dt $$
#### Свойства

- Нечётность: $C(-x) = -C(x)$, $S(-x) = -S(x)$.
- Асимптотика при малых $x$: $C(x) \approx x$, $S(x) \approx \tfrac{\pi x^3}{6}$, при больших x: $C(x) \approx \tfrac{1}{2} + \frac{\sin\left(\frac{\pi x^2}{2}\right)}{\pi x}$, $S(x) \approx \tfrac{1}{2} - \frac{\cos\left(\frac{\pi x^2}{2}\right)}{\pi x}$
- Связь с комплексной экспонентой: $$ C(x) + iS(x) = \int_0^x e^{i\pi t^2/2}dt $$
- $C(+\infty) = S(+\infty) = \tfrac{1}{2}$
