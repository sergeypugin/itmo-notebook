---
title: "Несобственные интегралы первого рода"
author: "Dimas"
links:
  - "[17. Понятие несобственного интеграла и его свойства](https://profuse-agenda-583.notion.site/17-d38036d0057a43f1826dc208ea5b4fdf?pvs=25)"
  - "[18. Признаки сходимости интеграла от функций, сохраняющих знак](https://profuse-agenda-583.notion.site/18-f36764bb919144758c8dfe918af34517?pvs=25)"
  - "[19. Критерий Коши. Абсолютная и условная сходимости](https://profuse-agenda-583.notion.site/19-fc1fce3857b94304a3ddc66af0edc74e?pvs=25)"
---
## Определение. Понятие локальной интегрируемости

Говорят, что функция $f$ локально интегрируема на множестве $E$, и пишут $f \in R_{loc}(E)$, если $f \in R[a, b]$ для любого $[a, b] \subset E$. 

## Определение. Понятие несобственного интеграла

Пусть $f \in R_{loc}[a, b)$, $-\infty < a < b \leq + \infty$. Тогда символ
$$
\int\limits_a^b f \ dx,
$$

называется несобственным интегралом от функции $f$ по множеству $[a, b)$ и определяется как предел 
$$
\int\limits_a^b f \ dx = \lim\limits_{\omega \to b - 0} \int\limits_a^\omega f \ dx,
$$
где $\omega \in [a, b)$
>Если этот предел существует и конечен (принадлежит $\mathbb{R}$), то несобственный интеграл называется сходящимся. Если предел не существует или равен бесконечности — интеграл называется расходящимся
## Определение. Понятия несобственного интеграла 1 рода
**Несобственный интеграл первого рода** - это несобственный интеграл по неограниченному промежутку:
$$
\int_a^{+\infty}f(x)\,dx,
\qquad
\int_{-\infty}^{b}f(x)\,dx,
\qquad
\int_{-\infty}^{+\infty}f(x)\,dx.
$$

## Пример

Исследуем интеграл
$$
\int_1^{+\infty}\frac{dx}{x^p}.
$$
Тогда
$$
\int_1^{+\infty}\frac{dx}{x^p}
$$
сходится тогда и только тогда, когда
$$
p>1.
$$
## Свойства

### Линейность
Пусть $f \in R_{loc}[a, b)$. Если сходятся интегралы
$$
\int\limits_a^b f \ dx \quad \text{и} \quad \int\limits_a^b g \ dx,
$$

то
$$
\int\limits_a^b (\alpha f + \beta g) \ dx = \alpha \int\limits_a^b f \ dx + \beta \int\limits_a^b g \ dx.
$$
### Доказательство

Для доказательства достаточно перейти к пределу при $\omega \to b-0$ в равенстве, [свойствами интеграла](question-11) для интеграла Римана:
$$
\int\limits_a^\omega (\alpha f + \beta g) \ dx = \alpha \int\limits_a^\omega f \ dx + \beta \int\limits_a^\omega g \ dx.
$$
---

- ### Аддитивность

Пусть $f \in R_{loc}[a, b)$. Тогда для любого $c \in (a, b)$ справедливо равенство
$$
\int\limits_a^b f \ dx = \int\limits_a^c f \ dx + \int\limits_c^b f \ dx,
$$

причем интегралы
$$
\int\limits_a^b f \ dx \quad \text{и} \quad \int\limits_c^b f \ dx
$$

сходятся или нет одновременно.

#### Доказательство

Для доказательства достаточно перейти к пределу при $\omega \to b-0$ в равенстве, [свойствами интеграла](question-11):
$$
\int\limits_a^\omega f \ dx = \int\limits_a^c f \ dx + \int\limits_c^\omega f \ dx.
$$

Данная теорема позволяет свести вопрос сходимости интеграла к вопросу стремления к нулю остатка или, как еще говорят, «хвоста» интеграла.

---
- ### Монотонность

Пусть $f,g \in R_{loc}[a, b)$, причем
$$
\int\limits_a^b f \ dx \in \overline{\mathbb R} \quad \text{и} \quad \int\limits_a^b g \ dx \in \overline{\mathbb R}.
$$

Если $f \leq g$ на $[a, b)$, то
$$
\int\limits_a^b f \ dx \leq \int\limits_a^b g \ dx.
$$

#### Доказательство

Для доказательства достаточно перейти к пределу при $\omega \to b-0$ в неравенстве, [свойствами интеграла](question-11):
$$
\int\limits_a^\omega f \ dx \leq \int\limits_a^\omega g \ dx.
$$

## Теорема. Критерий Коши

Пусть $f \in R_{loc}[a, b)$. Для того чтобы интеграл
$$
\int\limits_a^b f \ dx
$$

сходился необходимо и достаточно, чтобы
$$
\forall \varepsilon > 0 \ \exists \Delta \in (a, b): \ \forall \delta_1, \delta_2 \in (\Delta, b) \Rightarrow \left| \int\limits_{\delta_1}^{\delta_2} f \ dx \right| < \varepsilon.
$$

### Доказательство

Обозначим
$$
F(\omega) := \int\limits_a^\omega f \ dx.
$$

Согласно [понятие несобственного интеграла и его свойства](question-11), сходимость интеграла равносильна существованию предела функции $F(\omega)$ при $\omega \to b-0$. Согласно критерию Коши существования предела функции, это выполнено тогда и только тогда, когда
$$
\forall \varepsilon > 0 \ \exists \Delta \in (a, b): \ \forall \delta_1, \delta_2 \in (\Delta, b) \Rightarrow \left| F({\delta_2}) - F({\delta_1}) \right| < \varepsilon.
$$

Последнее же неравенство, в силу [свойств интеграла](question-11), переписывается как
$$
\left| F({\delta_2}) - F({\delta_1}) \right| < \varepsilon \ \Leftrightarrow \ \left|\int\limits_{\delta_1}^{\delta_2} f \ dx \right| < \varepsilon,
$$

откуда и следует требуемое.

## Теорема. Критерий сходимости интеграла от неотрицательной функции

Пусть $f \in R_{loc}[a, b)$, $f \geq 0$. Тогда функция
$$
F(\omega) := \int\limits_a^\omega f \ dx, \quad \omega \in [a, b),
$$

не убывает, а сходимость интеграла
$$
\int\limits_a^b f\ dx
$$

равносильна ограниченности функции $F(\omega)$.

### Доказательство

Ясно, что если $a \leq \omega_1 \leq \omega_2 < b$, то, так как $f \geq 0$, по [свойствам интеграла](question-11) интеграла Римана,
$$
\int\limits_{\omega_1}^{\omega_2}f \ dx \geq 0.
$$

Но тогда
$$
F(\omega_2) = \int\limits_a^{\omega_2}f \ dx = \int\limits_a^{\omega_1}f \ dx + \int\limits_{\omega_1}^{\omega_2}f \ dx \geq \int\limits_a^{\omega_1}f \ dx = F(\omega_1),
$$

откуда $F(\omega_2) \geq F(\omega_1)$, что и доказывает неубывание $F(\omega)$.

>Значит, вопрос сходимости несобственного интеграла, то есть вопрос существования конечного предела $F(\omega)$ при $\omega \to b-0$, сводится к теореме Вейерштрасса. Как мы знаем, конечность предела (или сходимость заявленного интеграла) в этом случае равносильна ограниченности $F(\omega)$.

## Признаки сравнения

Пусть $f, g \in R_{loc}[a, b)$ и $0 \leq f \leq g$ при $x \in [a, b)$. Тогда:

1. Сходимость интеграла от $g$ по $[a, b)$ влечет сходимость интеграла от $f$ по $[a, b)$ , то есть
    $$
    \int\limits_a^b g \ dx < + \infty \ \Rightarrow \ \int\limits_a^b f \ dx < +\infty.
    $$

2. Расходимость интеграла от $f$ по $[a, b)$ влечет расходимость интеграла от $g$ по $[a, b)$, то есть
    $$
    \int\limits_a^b f \ dx = +\infty \ \Rightarrow \ \int\limits_a^b g \ dx = +\infty.
    $$

3. Если $f \sim g$ при $x\to b-0$, то интегралы от $f$ и $g$ по $[a, b)$ сходятся или расходятся одновременно.
