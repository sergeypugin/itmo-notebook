---
title: "Производные сложных функций и производные высших порядков"
---

# 1.6 Полный дифференциал

**Дифференцируемая функция в точке** — это функция $u = f(x, y, z)$, если её полное приращение в точке $(x_0, y_0, z_0)$ представимо в виде:
$$
\Delta u = f'_x(x_0, y_0, z_0) \cdot \Delta x + f'_y(x_0, y_0, z_0) \cdot \Delta y + f'_z(x_0, y_0, z_0) \cdot \Delta z + o(\rho) \tag{1.15}
$$
где $\rho = \sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}$.

**Полный дифференциал функции** — это главная линейная часть полного приращения функции. Выражение для полного дифференциала имеет вид:
$$
df = f'_x(x_0, y_0, z_0) \cdot \Delta x + f'_y(x_0, y_0, z_0) \cdot \Delta y + f'_z(x_0, y_0, z_0) \cdot \Delta z \tag{1.16}
$$

> [!note]- Геометрический смысл дифференциала
> Дифференциал — это приращение касательной.
>
> ![[differential_geometric_meaning.jpg|400]]

> [!theorem] Теорема 9 (Уравнение касательной плоскости)
> Поверхность задана уравнением $z = f(x, y)$ и имеет касательную плоскость в точке $M_0(x_0, y_0, z_0)$.
>
> Если функция $z = f(x, y)$ дифференцируема в точке $(x_0, y_0)$, то уравнение касательной плоскости в точке $M_0(x_0, y_0, z_0)$ имеет вид:
> $$
> Z - z_0 = f'_x(x_0, y_0) \cdot (x - x_0) + f'_y(x_0, y_0) \cdot (y - y_0) \tag{1.17}
> $$

# 1.7 Производные от сложных функций

Пусть функция $u = f(x, y, z)$ определена в некоторой открытой области $D$, где переменные $x, y, z$ являются функциями от переменной $t$:
$$
x = \varphi(t), \quad y = \psi(t), \quad z = \chi(t)
$$
где $\varphi(t), \psi(t), \chi(t)$ — дифференцируемые функции.

Если в области $D$ существуют непрерывные частные производные $u'_x, u'_y, u'_z$, то полное приращение функции может быть представлено в виде:
$$
\Delta u = u'_x \cdot \Delta x + u'_y \cdot \Delta y + u'_z \cdot \Delta z + \alpha \cdot \Delta x + \beta \cdot \Delta y + \gamma \cdot \Delta z \tag{1.18}
$$
где $\alpha, \beta, \gamma \to 0$ при $\Delta x, \Delta y, \Delta z \to 0$.

Разделив обе части уравнения (1.18) на $\Delta t$ и устремив $\Delta t \to 0$, получаем производную сложной функции:
$$
\frac{du}{dt} = \frac{\partial u}{\partial x} \cdot \frac{dx}{dt} + \frac{\partial u}{\partial y} \cdot \frac{dy}{dt} + \frac{\partial u}{\partial z} \cdot \frac{dz}{dt} \tag{1.19}
$$

> [!note] Производная для $n$ переменных
> Формулу (1.19) можно распространить на случай функции $n$ переменных:
> $$
> \frac{du}{dt} = \frac{\partial u}{\partial x_1} \cdot \frac{dx_1}{dt} + \frac{\partial u}{\partial x_2} \cdot \frac{dx_2}{dt} + \dots + \frac{\partial u}{\partial x_n} \cdot \frac{dx_n}{dt} \tag{1.20}
> $$

Если $x = \varphi(t, s), y = \psi(t, s), z = \chi(t, s)$, то вместо производных по $t$ возникают частные производные:
$$
\frac{\partial u}{\partial t} = \frac{\partial u}{\partial x} \cdot \frac{\partial x}{\partial t} + \frac{\partial u}{\partial y} \cdot \frac{\partial y}{\partial t} + \frac{\partial u}{\partial z} \cdot \frac{\partial z}{\partial t} \tag{1.21}
$$

Если функция $u$ явно зависит от $t$ ($u = u(t, x, y, z)$), то полная производная вычисляется по формуле:
$$
\frac{du}{dt} = \frac{\partial u}{\partial t} + \frac{\partial u}{\partial x} \cdot \frac{dx}{dt} + \frac{\partial u}{\partial y} \cdot \frac{dy}{dt} + \frac{\partial u}{\partial z} \cdot \frac{dz}{dt} \tag{1.22}
$$

# 1.8 Производная степени с переменным основанием и показателем

Для нахождения производной функции $u = (\varphi(t))^{\psi(t)}$ вводятся новые переменные:
$$
x = \varphi(t), \quad y = \psi(t)
$$
Тогда функция принимает вид $u = x^y$. Применяя формулу производной сложной функции, получаем:
$$
\frac{du}{dt} = \frac{\partial u}{\partial x} \cdot \frac{dx}{dt} + \frac{\partial u}{\partial y} \cdot \frac{dy}{dt} = y \cdot x^{y-1} \cdot \frac{dx}{dt} + x^y \cdot \ln x \cdot \frac{dy}{dt} \tag{1.23}
$$

> [!example] Пример нахождения производной
> Найдем производную функции $u = t^{\sin t}$. Введем новые переменные $x = t, y = \sin t$.
>
> Тогда производная равна:
> $$
> \frac{du}{dt} = t^{\sin t} \cdot \left( \sin t \cdot \frac{1}{t} + \ln t \cdot \cos t \right) \tag{1.24}
> $$

# 1.9 Дифференцирование функционального определителя

**Функциональный определитель (якобиан)** — это определитель следующего вида:
$$
u = \begin{vmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nn}
\end{vmatrix} = U(a_{11}, a_{12}, \dots, a_{nn}) \tag{1.25}
$$
где каждый элемент $a_{ik} = a_{ik}(t)$ ($1 \le i \le n, 1 \le k \le n$) является дифференцируемой функцией от переменной $t$.

Для нахождения производной $\frac{du}{dt}$ используется разложение определителя по $k$-му столбцу:
$$
u = a_{1k} \cdot A_{1k} + a_{2k} \cdot A_{2k} + \dots + a_{nk} \cdot A_{nk} \tag{1.26}
$$
где $A_{ik}$ — алгебраическое дополнение элемента $a_{ik}$.

Частная производная определителя по элементу $a_{ik}$ равна его алгебраическому дополнению:
$$
\frac{\partial u}{\partial a_{ik}} = A_{ik} \tag{1.27}
$$

Тогда производная определителя по параметру $t$ выражается в виде суммы определителей, в которых поочередно дифференцируются элементы каждого столбца:
$$
\frac{du}{dt} = \sum_{k=1}^{n} \begin{vmatrix}
a_{11} & \dots & \frac{da_{1k}}{dt} & \dots & a_{1n} \\
a_{21} & \dots & \frac{da_{2k}}{dt} & \dots & a_{2n} \\
\vdots & & \vdots & & \vdots \\
a_{n1} & \dots & \frac{da_{nk}}{dt} & \dots & a_{nn}
\end{vmatrix} \tag{1.28}
$$

> [!note] Дифференцирование по строкам
> Аналогично формуле (1.28) можно продифференцировать определитель по всем строкам:
> $$
> \frac{du}{dt} = \sum_{i=1}^{n} \begin{vmatrix}
> a_{11} & a_{12} & \dots & a_{1n} \\
> \dots & \dots & \dots & \dots \\
> \frac{da_{i1}}{dt} & \frac{da_{i2}}{dt} & \dots & \frac{da_{in}}{dt} \\
> \dots & \dots & \dots & \dots \\
> a_{n1} & a_{n2} & \dots & a_{nn}
> \end{vmatrix} \tag{1.29}
> $$

# 1.10 Производные высших порядков

**Производная второго порядка** — это производная от первой частной производной функции. Для функции двух переменных $u = f(x, y)$ вводятся следующие обозначения:
$$
\frac{\partial}{\partial x}\left(\frac{\partial u}{\partial x}\right) = \frac{\partial^2 u}{\partial x^2} = (u'_x)'_x = u''_{xx}
$$
$$
\frac{\partial}{\partial x}\left(\frac{\partial u}{\partial y}\right) = \frac{\partial^2 u}{\partial x \partial y} = (u'_y)'_x = u''_{yx}
$$
$$
\frac{\partial}{\partial y}\left(\frac{\partial u}{\partial x}\right) = \frac{\partial^2 u}{\partial y \partial x} = (u'_x)'_y = u''_{xy}
$$

> [!theorem] Теорема 10 (Теорема о смешанных производных)
> Пусть функция $f(x, y)$ определена в некоторой открытой области $D$ и в этой области существуют производные $f'_x$, $f'_y$, $f''_{xy}$, $f''_{yx}$.
>
> Если производные $f''_{xy}$ и $f''_{yx}$ непрерывны в некоторой точке $(x_0, y_0) \in D$, то в этой точке смешанные производные равны:
> $$
> f''_{xy}(x_0, y_0) = f''_{yx}(x_0, y_0) \tag{1.30}
> $$

---
[[lection-2|Предыдущая лекция]] | [[matan/sem3/lection_notes/index|Все лекции]]
