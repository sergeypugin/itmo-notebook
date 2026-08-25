---
title: "Длина дуги"
author: "Sergey"
links:
  - "[Фихтенгольц 2 том.pdf](https://drive.google.com/file/d/1RRCWeDROdFIdbMdNo52RVGiSe-ACLSnW/view?usp=drivesdk) стр. 185"
  - "[Фихтенгольц 1 том.pdf](https://drive.google.com/file/d/1eUg814bvl7_PxvIERKeeDR_MHhGSjQIj/view?usp=drivesdk) стр. 628"
---
## Вычисление длины дуги плоской кривой

### 1. Параметрическое задание кривой

Пусть непрерывная простая кривая $AB$ задана уравнениями:
$$
x = \phi(t), \ y = \psi(t) \quad (t_0 \leqslant t \leqslant T)
$$
Длина кривой определяется как точная верхняя граница периметров вписанных ломаных: $S = \sup\{p\}$.

**Обоснование формулы:**
Если функции $\phi(t)$ и $\psi(t)$ имеют непрерывные производные, то кривая функция длины переменной дуги $s(t)$ дифференцируема. Её производная равна:
$$
s'_t = \sqrt{x'_t{}^2 + y'_t{}^2} = \sqrt{[\phi'(t)]^2 + [\psi'(t)]^2}
$$
По формуле Ньютона-Лейбница, интегрируя производную $s'_t$ в пределах от $t_0$ до $T$, получаем полную длину кривой:
$$
S = s(T) - s(t_0) = \int_{t_0}^T \sqrt{x'_t{}^2 + y'_t{}^2} \, dt = \int_{t_0}^T \sqrt{[\phi'(t)]^2 + [\psi'(t)]^2} \, dt
$$
Длина переменной дуги с началом в точке $t_0$:
$$
s(t) = \int_{t_0}^t \sqrt{x'_t{}^2 + y'_t{}^2} \, dt
$$
---

### 2. Явное задание в декартовых координатах

Пусть кривая задана уравнением $y = f(x)$ на отрезке $[x_0, X]$. 

**Вывод из общего случая:**
Принимая абсциссу $x$ за параметр, имеем: $x = x \implies x'_x = 1$, а $y'_x = f'(x)$. По формуле 1 пункта:
$$
S = \int_{x_0}^X \sqrt{1 + y'_x{}^2} \, dx = \int_{x_0}^X \sqrt{1 + [f'(x)]^2} \, dx
$$
Длина переменной дуги:
$$
s(x) = \int_{x_0}^x \sqrt{1 + y'_x{}^2} \, dx
$$
---

### 3. Задание в полярных координатах

Пусть кривая задана полярным уравнением $r = g(\theta)$ при $\theta_0 \leqslant \theta \leqslant \Theta$.

**Вывод из общего случая:**
$$
x = r \cos \theta = g(\theta) \cos \theta, \quad y = r \sin \theta = g(\theta) \sin \theta
$$
Дифференцируя по $\theta$:
$$
x'_\theta = r' \cos \theta - r \sin \theta, \quad y'_\theta = r' \sin \theta + r \cos \theta
$$
Т. к. ($\sin^2\theta + \cos^2\theta = 1$) получаем:
$$
x'_\theta{}^2 + y'_\theta{}^2 = (r' \cos \theta - r \sin \theta)^2 + (r' \sin \theta + r \cos \theta)^2 = r^2 + r'_\theta{}^2
$$
По формуле 1 пункта:
$$
S = \int_{\theta_0}^{\Theta} \sqrt{r^2 + r'_\theta{}^2} \, d\theta = \int_{\theta_0}^{\Theta} \sqrt{[g(\theta)]^2 + [g'(\theta)]^2} \, d\theta
$$
Длина переменной дуги:
$$
s(\theta) = \int_{\theta_0}^\theta \sqrt{r^2 + r'_\theta{}^2} \, d\theta
$$
