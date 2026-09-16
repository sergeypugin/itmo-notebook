---
title: "Усиленные признаки сходимости рядов: Куммера, Раабе, Бертрана, Гаусса"
author: "Sergey"
links:
  - "[31. Признаки Куммера, Раабе, Бертрана и Гаусса](https://profuse-agenda-583.notion.site/31-3a4b0c8575e4435eba12224d19957069?pvs=25)"
---
## Усиленные признаки сходимости рядов

### 1. Признак Куммера

Пусть $a_k, b_k > 0$, ряд $\sum \frac{1}{b_k}$ расходится и $l = \lim_{k\to\infty}\!\left(b_k\frac{a_k}{a_{k+1}} - b_{k+1}\right)$.
*   $l > 0 \implies$ ряд $\sum a_k$ сходится;
*   $l < 0 \implies$ ряд $\sum a_k$ расходится.

#### Доказательство:

  - **Случай $l > 0$.**
	Выберем $r \in (0, l)$. С некоторого $k_0$:
	$$
	b_k \frac{a_k}{a_{k+1}} - b_{k+1} \ge r \implies b_k a_k - b_{k+1} a_{k+1} \ge r a_{k+1} > 0
	$$
	Последовательность $b_k a_k$ убывает и ограничена снизу нулём $\implies$ имеет предел $A \ge 0$. Суммируем от $k_0$ до $n-1$ (телескопическая сумма сократится):
	$$
	r \sum_{k=k_0}^{n-1} a_{k+1} \le \sum_{k=k_0}^{n-1}(b_k a_k - b_{k+1} a_{k+1}) =
	$$
	$$
	= b_{k_0}a_{k_0} - b_n a_n \le b_{k_0}a_{k_0} - A
	$$
	Частичные суммы ограничены сверху $\implies$ ряд сходится.
---

- **Случай $l < 0$.**  
	С некоторого $k_0$: $b_k \frac{a_k}{a_{k+1}} - b_{k+1} < 0 \implies b_{k+1}a_{k+1} > b_k a_k$. 
	Последовательность возрастает и $b_k a_k \ge b_{k_0} a_{k_0} \implies a_k \ge \frac{\text{const}}{b_k}$. 
	Так как $\sum \frac{1}{b_k}$ расходится, по признаку сравнения $\sum a_k$ расходится.

---

### 2. Признак Раабе

>Тот же признак Куммера при $b_k = k$, но тут $l_{new}=l+1$

Пусть $a_k > 0$ и $l = \lim_{k\to\infty} k\left(\frac{a_k}{a_{k+1}} - 1\right)$.
*   $l > 1 \implies \sum a_k$ сходится;
*   $l < 1 \implies \sum a_k$ расходится.

#### Доказательство:
Подставим $b_k = k$ в предел Куммера (обозначим его $L$):
$$
L = \lim_{k\to\infty} \left(k\frac{a_k}{a_{k+1}} - (k+1)\right) = \lim_{k\to\infty} \left[k\left(\frac{a_k}{a_{k+1}} - 1\right) - 1\right] = l - 1
$$
Условие Куммера $L > 0 \implies l > 1$.
Условие Куммера $L < 0 \implies l < 1$.

---

### 3. Признак Бертрана (Куммер при $b_k = k \ln k$)

Пусть $a_k > 0$ и $l = \lim_{k\to\infty} \ln k \cdot \left(k\left(\frac{a_k}{a_{k+1}} - 1\right) - 1\right)$.
*   $l > 1 \implies \sum a_k$ сходится;
*   $l < 1 \implies \sum a_k$ расходится.

#### Доказательство:
1. Ряд $\sum \frac{1}{k\ln k}$ расходится, т.к. по теореме Лагранжа $\ln\ln(k+1) - \ln\ln k \sim \frac{1}{k\ln k}$, а телескопическая сумма приращений стремится к $+\infty$.
2. Подставим $b_k = k\ln k$ в предел Куммера, используя $\ln(k+1) = \ln k + \frac{1}{k} + O(\frac{1}{k^2})$:
	$$
	L = \lim_{k\to\infty} \left( k \ln k \frac{a_k}{a_{k+1}} - (k+1)\left[\ln k + \frac{1}{k} + O\left(\frac{1}{k^2}\right)\right] \right) =
	$$
	$$
	= \lim_{k\to\infty} \left( \ln k \left[ k\left(\frac{a_k}{a_{k+1}} - 1\right) - 1 \right] - 1 + O\left(\frac{1}{k}\right) \right) = l - 1
	$$
Как и в Раабе: $L > 0 \implies l > 1$ и $L < 0 \implies l < 1$.

---

### 4. Признак Гаусса

Пусть отношение членов представимо в виде:
$$
\frac{a_k}{a_{k+1}} = \lambda + \frac{\mu}{k} + \frac{\theta_k}{k^{1+\gamma}}, \quad \text{где } |\theta_k| \le C, \ \gamma > 0.
$$
Тогда:
*   $\lambda > 1 \implies$ сходится, $\lambda < 1 \implies$ расходится.
*   $\lambda = 1, \mu > 1 \implies$ сходится.
*   $\lambda = 1, \mu \le 1 \implies$ расходится.

#### Доказательство:

- **Случай $\lambda \ne 1$.**  
	$\lim \frac{a_k}{a_{k+1}} = \lambda \implies \lim \frac{a_{k+1}}{a_k} = \frac{1}{\lambda}$. По признаку Даламбера сходится при $\frac{1}{\lambda} < 1 \implies \lambda > 1$, расходится при $\lambda < 1$.
---
- **Случай $\lambda = 1, \mu \ne 1$.**  
	Применяем признак Раабе:
	$$
	l = \lim_{k\to\infty} k\left(\frac{a_k}{a_{k+1}} - 1\right) = \lim_{k\to\infty} k\left(1 + \frac{\mu}{k} + \frac{\theta_k}{k^{1+\gamma}} - 1\right) = \mu
	$$
	По Раабе сходится при $\mu > 1$, расходится при $\mu < 1$.
---
- **Случай $\lambda = 1, \mu = 1$.**  
	Применяем признак Бертрана:
	$$
	l = \lim_{k\to\infty} \ln k \cdot \left(k\left(\frac{a_k}{a_{k+1}} - 1\right) - 1\right) = \lim_{k\to\infty} \ln k \cdot \left(k\left(\frac{1}{k} + \frac{\theta_k}{k^{1+\gamma}}\right) - 1\right) =
	$$
	$$
	= \lim_{k\to\infty} \frac{\theta_k \ln k}{k^\gamma} = 0
	$$
	Так как $l = 0 < 1$, по Бертрану ряд расходится (что закрывает и все $\mu \le 1$).
