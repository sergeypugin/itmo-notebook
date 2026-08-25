---
title: Лемма Римана-Лебега
author: Luisa
links:
  - "[Бойцев база.pdf](https://drive.google.com/file/d/1fd1CA2uUsD9ZnaquCyoEYYzXWVJyVRVN/view?usp=drivesdk)"
---
### Лемма Римана — Лебега
Пусть функция $f(x)$ абсолютно интегрируема на интервале $(a, b)$, то есть $f \in L(a, b)$ и $\int_{a}^{b} |f(x)| \, dx < +\infty$. Тогда:
$$ \lim_{|\lambda| \to +\infty} \int_{a}^{b} f(x) e^{i\lambda x} \, dx = 0, \quad \lambda \in \mathbb{R} $$
*Доказательство:*
**Шаг 1:** Пусть *f(x)=c* Используя формулу Эйлера ($e^{ix}=cosx+i*sinx$), вычислим интеграл в явном виде:
$$ \int_{a}^{b} c e^{i\lambda x} \, dx = c \left( \int_{a}^{b} \cos \lambda x \, dx + i \int_{a}^{b} \sin \lambda x \, dx \right) = $$
$$=c \left( \frac{\sin \lambda b - \sin \lambda a}{\lambda} - i \frac{\cos \lambda b - \cos \lambda a}{\lambda} \right) $$
Так как функции $\sin$ и $\cos$ ограничены по модулю единицей, числитель при любых $\lambda$ ограничен:
$$ \left| \int_{a}^{b} c e^{i\lambda x} \, dx \right| \leq |c| * (\frac{2}{|\lambda|} + \frac{2}{|\lambda|}) = \frac{4|c|}{|\lambda|} \xrightarrow[|\lambda| \to +\infty]{} 0 $$
Для константы утверждение доказано.

**Шаг 2** Пусть задано произвольное $\varepsilon > 0$. В силу абсолютной сходимости интеграла $\int_{a}^{b} |f(x)| \, dx$, выберем внутренний отрезок $[\delta_1, \delta_2] \subset (a, b)$ так, чтобы интегралы по краям области были малы:
$$ \int_{a}^{\delta_1} |f(x)| \, dx < \frac{\varepsilon}{4} \quad \text{и} \quad \int_{\delta_2}^{b} |f(x)| \, dx < \frac{\varepsilon}{4} $$
Оценим разность интегралов по всему промежутку и по внутреннему отрезку, учитывая, что $|e^{i\lambda x}| = 1$:
$$ \left| \int_{a}^{b} f(x)e^{i\lambda x} \, dx - \int_{\delta_1}^{\delta_2} f(x)e^{i\lambda x} \, dx \right| \leq $$
$$\leq \int_{a}^{\delta_1} |f(x)| \, dx + \int_{\delta_2}^{b} |f(x)| \, dx < \frac{\varepsilon}{4} + \frac{\varepsilon}{4} = \frac{2\varepsilon}{4} $$

**Шаг 3:** Поскольку $f \in L[\delta_1, \delta_2]$, существует разбиение $\tau$ отрезка $[\delta_1, \delta_2]$ точками $\delta_1 = x_0 < x_1 < \dots < x_n = \delta_2$, для которого нижняя сумма Дарбу $s_{\tau}(f) = \sum_{i=1}^{n} m_i \Delta x_i$ (где $m_i = \inf_{[x_{i-1}, x_i]} f(x)$) удовлетворяет условию:
$$ 0 \leq \int_{\delta_1}^{\delta_2} f(x) \, dx - s_{\tau}(f) < \frac{\varepsilon}{4} $$
Зададим ступенчатую функцию $g(x) = m_i$ при $x \in (x_{i-1}, x_i)$. Тогда $f(x) \geq g(x)$ и:
$$ \int_{\delta_1}^{\delta_2} (f(x) - g(x)) \, dx = \int_{\delta_1}^{\delta_2} f(x) \, dx - s_{\tau}(f) < \frac{\varepsilon}{4} $$
Оценим разность интегралов от $f(x)$ и $g(x)$ с осциллирующим множителем:
$$ \left| \int_{\delta_1}^{\delta_2} f(x)e^{i\lambda x} \, dx - \int_{\delta_1}^{\delta_2} g(x)e^{i\lambda x} \, dx \right| \leq $$
$$\int_{\delta_1}^{\delta_2} |f(x) - g(x)| \cdot |e^{i\lambda x}| \, dx
= \int_{\delta_1}^{\delta_2} (f(x) - g(x)) \, dx < \frac{\varepsilon}{4} 
$$

**Шаг4:** Запишем интеграл от ступенчатой функции $g(x)$ в виде конечной суммы:
$$ \int_{\delta_1}^{\delta_2} g(x)e^{i\lambda x} \, dx = \sum_{i=1}^{n} \int_{x_{i-1}}^{x_i} m_i e^{i\lambda x} \, dx $$

По Шагу 1 каждое слагаемое в этой конечной сумме стремится к нулю при $|\lambda| \to +\infty$. Следовательно:
$$ \lim_{|\lambda| \to +\infty} \int_{\delta_1}^{\delta_2} g(x)e^{i\lambda x} \, dx = 0 $$
Значит, существует такое $\Lambda > 0$, что для всех $|\lambda| > \Lambda$ выполняется неравенство:
$$ \left| \int_{\delta_1}^{\delta_2} g(x)e^{i\lambda x} \, dx \right| < \frac{\varepsilon}{4} $$

Объединяя оценки из **Шага 2**, **Шага 3** и **Шага 4** по неравенству треугольника, получаем для любого $|\lambda| > \Lambda$:
$$ \left| \int_{a}^{b} f(x)e^{i\lambda x} \, dx \right| \leq \left| \int_{a}^{b} f(x)e^{i\lambda x} \, dx - \int_{\delta_1}^{\delta_2} f(x)e^{i\lambda x} \, dx \right| + $$
$$+\left| \int_{\delta_1}^{\delta_2} f(x)e^{i\lambda x} \, dx - \int_{\delta_1}^{\delta_2} g(x)e^{i\lambda x} \, dx \right| + \left| \int_{\delta_1}^{\delta_2} g(x)e^{i\lambda x} \, dx \right| $$
Откуда получаем:
$$ \left| \int_{a}^{b} f(x)e^{i\lambda x} \, dx \right| < \frac{2\varepsilon}{4} + \frac{\varepsilon}{4} + \frac{\varepsilon}{4} = \varepsilon $$
В силу произвольности выбора $\varepsilon > 0$, предел равен нулю.
