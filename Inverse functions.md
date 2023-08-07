## Unlocking the Secrets of Inverses, Exploring Logarithms, Inverse Trig, and Beyond

### Prerequisites
* We should be familiar with **exponents** and **exponential functions**.
* We should be familiar with **trigonometric functions**.
* We should know what the **graphs of exponential functions** look like (base $b >1$ and base $b <1$).
* We should know what a **function** is (in general).
* We should know what **domain**, **co-domain** and **range** of a function is.
* We should know what the **vertical line test** is.

### Learning Outcomes:  
By the end of this session you would like to know the following:  
1. The definition and meaning of the **inverse** of a function.  
2. How to draw the **graph** of the inverse of a function.  
3. How to define a **logarithm function** as the inverse of an exponential function.
4. Prove and use important **properties of logarithms**. 
5. How to **change the base** in logarithmic expressions.  
6. How to use logarithms in some practical examples.
7. How to define and understand **inverse trig functions**.
8. Prove and use important **properties of inverse trig functions**. 
9. How to use inverse trig functions in some practical examples.

**Bonus:** If you are interested, in the afternoon I can show you how to install the editor that I am using (free and works on most devices, including smartphones)
### Inverse Functions:  

First of all, what is a function?

#### The most general answer
**Definition (of a function):** $f$ is a function if $f$ has a **domain** $D$  and a **codomain** $C$  such that for every elements $x\in D$ there exists a unique element $f(x)\in C$. 

Abbreviated as                 $f:D\to C$ 

$f$  is the name of the function.

The domain $D$ is the set of **input values**.    Usually we write $D=dom(f)$.

The codomain $C$  is the set of **possible** **output values**.    $C=cod(f)$

What is the **range** of a function?

$range(f)=\{f(x)\mid x\in D\}$

In English this says that $range(f)$ is the set of all elements $f(x)$ where $x$ ranges over all elements of the domain.

In general, functions can process lots of different kinds of objects (not just numbers). E.g. we can have a function $f$ such that $f(x)= \text{firstname}(x)$.

What is the domain of $f$? Well, it should be a set of things that **have a first name**, e.g. the set of students in this bootcamp.

Then $dom(f)=$ the students in this bootcamp,

$cod(f)=$ the set of all possible first names, and

$range(f)=$ the set of first names of students in this bootcamp.

#### A slightly simpler answer for this bootcamp
Often we just use functions that have **real numbers** as input and output.

The set of real numbers is denoted by $\mathbb R$.

We can also use interval notation $(-\infty,\infty)=\mathbb R$.

In geometry, $\mathbb R$ is pictured as an infinite **line** from left to right (the **number line**).

**Definition** (of a function **on real numbers**): $f$ is a function on (some) real numbers if $f$ has a **domain** $D$ which is a subset of the set $\mathbb R$ (written $D\subseteq\mathbb R$) such that for every real number $x\in D$ the function $f$ produces a **unique real number** $f(x)$. 

Abbreviated as                 $f:D\to \mathbb R$ 

$f$  is the name of the function.

The domain $D$ is the set of **input values**.    Usually we write $D=dom(f)$.

For many functions $dom(f)=\mathbb R$.    E.g. quadratics $f(x)=ax^2+bx+c$ any real number is allowed as input.

But there are other functions where $dom(f)\subsetneq\mathbb R$.   E.g.  $\sqrt{\quad}$ , $f(x)=1/x$

What is the **range** of a function?

$range(f)=\{f(x)\mid x\in D\}$            (<- is an example of set-builder notation)

In English this says that $range(f)$ is the set of all elements $f(x)$ such that $x$ ranges over all elements of the domain, i.e. the **set of all outputs** of $f$.

#### When are two functions equal?

In mathematics it is **very useful** to properly understand when two things are equal (i.e. exactly the same).

**Definition of equality of functions**: Two functions $f$ and $g$  are equal, written $f=g$, if they have the same domain, i.e., $dom(f)=dom(g)$, and $f(x)=g(x)$ for all $x\in dom(f)$.

Short version: $f=g\iff dom(f)=dom(g)\text{ and }\forall_{x\in dom(f)} f(x)=g(x)$

Another way to see that two functions are equal is to look at their graphs.

#### What is the graph of a function?
**Definition of graph:** The graph of a function $f$ is $$graph(f)=\{(x,f(x))\mid x\in dom(f)\}$$
This is a subset of the $xy$-plane, so we can draw a picture of $f$ by plotting all these points.

Two functions are equal if they have exactly the same graph, i.e. $graph(f)=graph(g)$.

#### What is the difference between $f$ and $f(x)$?

$f$ and $f(x)$ are often used interchangeably to refer to a function, but there is actually an important distinction.

$f$  is the **name** of a function (could also be $g,h,\log,\sin,\cos,\dots$).

$f(x)$ is the **value** of a function with input $x$. So if $x$ is a given a specific number as value, then $f(x)$ will be exactly one number as a result, which means that $f(x)$ is not a function.

This can be an important distinction: $f^{-1}(x)$  is the value of the inverse of $f$ when the number $x$ is given as input.

This is **very different** from $f(x)^{-1}$  which is the reciprocal of $f(x)$, i.e. $f(x)^{-1}={1\over f(x)}$ which has **nothing to do** with the inverse of $f$.

This is not just being pedantic. Mathematical notation is supposed to be useful when we calculate with symbols, so it helps (a lot) if we understand it properly.

Note: The reciprocal $x^{-1}={1\over x}$ is sometimes also called the **multiplicative inverse** of $x$. But it is not an inverse function of $x$ since $x$ is a number rather than a function.

Also, $f(x)^{-1}$ is different from $f(x^{-1})=f({1\over x})$.  This is because, by convention, function application has priority over exponent notation. 

However, $2x^{-1}=2(x)^{-1}={2\over x}$ because $2$ is a number and not the name of a function! The difference is that $2x$ means "$2$ times $x$" rather than a function called $2$ applied to a variable $x$.

### Definition of the inverse of a function

A function $f$ takes an element, say $x$, as input from its **domain** and produces an output $f(x)$ in its **range**.

The **inverse** of a function $f$ **(if it exists)** does the reverse:  it is **supposed to** take each element $y$ in $range(f)$ and produce **the original** element $x$ in $dom(f)$ such that $f(x)=y$.

The name of the inverse of $f$ is $f^{-1}$.

So if $y=f(x)$  then we want $f^{-1}(...)=...$

There are two issues with this idea.

1. We want input values for $f^{-1}$ to use the variable $x$ and want to call the output $y$. This is easy to fix: just swap $x$ and $y$.

 2. When does the inverse function $f^{-1}$ exist?

Example: $f(x)=x^2$

`plot(x^2)=?`
Does it have an inverse? 

Many people think that the square root function $\sqrt{\ }$ is the inverse of $x^2$.

This is not completely wrong, but it is half wrong  :).

What is $\sqrt{x^2}=$ ?

Well, when $x=2$, we have $x^2=...$

So $\sqrt{2^2}=2$, which means that the square root reversed the effect of the square.

But what happens when $x=-2$?

Then $x^2=(-2)^2=\dots$ 

So $\sqrt{(-2)^2}=\sqrt{\dots}=\dots$

The problem is that there are two different values $2$ and $-2$ that both produce $4$ when squared.

So if we start with $4$ as input and want to reverse this step, should the inverse function produce $2$ or $-2$? (A function can't produce both!)

A function will have an inverse **exactly when** for any element $y$ in the range of $f$ there is a **unique element** $x$ in domain of $f$ such that $f(x)=y$

This property is important and has a special name:

**Definition of one-to-one:** A function $f$ is **one-to-one** if for all distinct elements $x_1\ne x_2$ in the domain of $f$ it follows that $f(x_1)\ne f(x_2)$.

**Short version**: $f$ is 1-1 if $\forall_{x_1,x_2}(x_1\ne x_2\implies f(x_1)\ne f(x_2))$

(The arrow $\implies$ means "implies". The symbol $\forall$ means "for all")

**Contrapositive** version (which is equivalent):
$$f\text{ is 1-1 if }\forall_{x_1,x_2}(f(x_1)=f(x_2)\implies x_1=x_2)$$
(In English: a function is 1-1 if whenever $f$ maps $x_1$ and $x_2$ to the same value, then $x_1$ and $x_2$ are equal.)

How can we see on a graph whether a function is one-to-one?

This has a special name (which you have probably heard many times):

**Definition of horizontal line test**: A set $S$ of points in $xy$-plane satisfies the **horizontal line test** if every horizontal line on the $xy$-plane contains at **most in one point** of $S$.

**The horizontal line test theorem:** A function $f$ is one-to-one if and only if the graph of $f$ satisfies the horizontal line test.

Finally we get to the main definition:

**Definition of inverse function:** Let $f$ be a one-to-one function. Then the inverse function $f^{-1}$ is defined by
$$y=f^{-1}(x) \iff f(y)=x$$
for all $x\in range(f)$ and all $y\in dom(f)$.

The two-sided arrow $\iff$ means "**is equivalent**".

Notice that it **follows from this definition** that $dom(f^{-1})=range(f)$ and $range(f^{-1})=dom(f)$.

1. In the definition $y=f^{-1}(x) \iff f(y)=x$ we can replace $y$ by $f^{-1}(x)$ then the statement on the left is always true (since $f^{-1}(x)=f^{-1}(x)$).

	Therefore we have **proved** that the statement on the right is true: $$f(f^{-1}(x))=x\text{ for all }x\in range(f).$$
2. In the definition $y=f^{-1}(x) \iff f(y)=x$ we can replace $x$ by $f(y)$ then the statement on the right is always true (since ................).

	Therefore we have **proved** that the statement on the left is true: $$y=f^{-1}(f(y))\text{ \ for all }y\in dom(f).$$
 
How do we **find the inverse** of a function given by $y = f(x)$: 

a) First write $x = f(y)$ (switch $x$ and $y$)  

b) Then solve for $y$. This expression for $y$ in terms of $x$ is the inverse function for $f$.

Example 1: $y = 2x+3$    try it on https://pollev.com/jipsen
> [!question]- a) Switch $x$ and $y$
> $x=2y+3$

> [!question]- b) Solve for $y$
> $2y+3=x$  [flip equation]
> $2y=x-3$  [subtract 3 on both sides]
> $y=\frac12(x-3)$       [multiply by $\frac12$]
> $y = \frac12x -\frac32$ [distribute]

Example 2: Find the inverse of $y=x^2$. 

a) switch $x,y$:   

b) solve for $y$:    But there are TWO solutions

$x=y^2$

$\implies y^2=x$

$\implies y=\pm\sqrt x$ 

Hmmm, also the graph of $x^2$ does not satisfy the horizontal line test!

So we conclude .......

But we can find an inverse for a piece of $x^2$, as long as the piece is a one-to-one function.

Which piece should we try?

How about $y=x^2$, if $x\le 0$

a) switch: $x=y^2$, if $y\le 0$


Solving equations can be difficult (sometimes impossible).

But inverse function can be understood graphically **without solving equations**!

Let's graph the example above:
`plot(2x+3,(1/2)*x-3/2,[-10,10])=?` 
Let's include the line $y=x$ as well:
`plot(2x+3,(1/2)*x-3/2,x,[-10,10])=?`
### Graph of the Inverse function

**Mirror image theorem:** The graph of the inverse of a function is the **mirror image** of the graph of the function about the line $y=x$.

**Proof:** A point $(x,y)$ on the graph of $f$ corresponds to a point $(y,x)$ on the graph of $f^{-1}$   (since the output of $f$ is mapped back to the input by $f^{-1}$).

If $x\ne y$ then the line connecting $(x,y)$ to $(y,x)$ has 
**slope** $m={y-x\over x-y}={-(x-y)\over y-x}=-1$, and 
**midpoint** $({x+y\over 2},{x+y\over 2})$, which is on the line $y=x$.

$y=x$ has slope $1$ and is at **right angle** to any line with slope $-1$. 

Therefore the points $(x,y)$ and $(y,x)$ are equally far from the line $y=x$  and mirror images across this line.

Example:

$y = f(x) = x^2 − 2$

a) Graph the function. 
b) Find the inverse. 
c) Graph the inverse.

Is the inverse a function?


#### A summary of Functions and Inverses
1. Every function has a graph, and if we interchange the $x$ and $y$ coordinates for all points on the graph we get an inverse relation.
2. This inverse relation is a function exactly when the original function is one-to-one (passes the horizontal line test).
3. The domain of a function is the range of its inverse and the range of the function is the domain of the inverse function (if it exists).
4. If $f$ is one-to-one then the name of the inverse function is $f^{-1}$.
5. The graph of a function and its inverse have mirror symmetry over the line $y=x$.

### Logarithms as inverses of exponential functions

Recall that exponential functions have a fixed base (say $b$) and a variable in the exponent:   $y = b^x$

How do we calculate the inverse function?

$x=b^y$

And now solve for $y$. 

But HOW???

**Logarithms** to the rescue!

**Definition of logarithm:** For a positive number $b\ne 1$ define $$y=\log_b x\iff b^y=x$$
So $\log_b$ is exactly the function we need to solve $b^y=x$ for $y$.

Example: for what value $y$  is $10^y=50$ ?  Use the definition.



Why do we need $0<b\ne 1$? 

We can also use the definition in the opposite direction:

Solve for $x$.

a) $\log_3 x = −2$

b) $\log_x 4 = 3$

c) $\log_8 4 = x$

Special Identities (which we **proved** in general from the definition)

$b^{\log_b x} =x$    for all $x>0$    since $f(f^{-1}(x))=x$ for all $x\in range(f)$.

$\log_bb^y =y$    for all $y\in\mathbb R$        since $f^{-1}(f(y))=y$ for all $y\in dom(f)$.

Use them for these problems:

$\log_{10} 10^6 =$

$\log_e e =$

Simplify:

$\log_4(\log_5 5)$

### Graph of the Logarithm function.

Use the graph of the exponential $b^x$ to plot the graph of its inverse $\log_ bx$

Do this for both cases: $b > 1$ and $0< b < 1$.

Here is a graph for $b=2$:
plot(log(x)/log(2),2^x,x)=?`

How about $b={1\over 2}$ ?
plot(log(x)/log(1/2),(1/2)^x,x)=?`


Note:  Input to a logarithm function is always positive. Why? 

$\log$ of negative numbers is NOT defined. Why? 

$\log$ of 0 (to any base) is  

$\log$ of what is 0?

Graph of $a^x$ and $\log_a x$  https://www.geogebra.org/m/aac5hn84

**Theorem for logarithms:** for $b>0$ and $b\ne 1$
1. $\log_b (xy)=$                    if ......
2. $\log_b (\frac xy)=$                     if ......
3. $\log_b (x^y)=$                     if ......

##### Proof of 1:
 $\log_b (xy)$
 $=\log_b({b^{\log_b x}\cdot b^{\log_b y}})$   using $x=b^{\log_b x}$ and .......
 $=\log_b(b^{\log_b x+\log_b y})$      using the rule ${b^p\cdot b^q}=b^{p+q}$ 
 $= \log_b x+\log_b y$         using $\log_b b^z=z$ 

##### Proof of 2:
 $\log_b (\frac xy)$
 $=\log_b({b^{\log_b x}\over b^{\log_b y}})$            using $x=b^{\log_b x}$ and .......
 $=\log_b(b^{\log_b x-\log_b y})$  using the rule ${b^p\over b^q}=b^{p-q}$ 
 $= \log_b x-\log_b y$     using $\log_b b^z=z$ 



Use properties of logarithms to expand each function as much as possible.

$\log_2y^5$ 

$\log_b \frac{xy} z$

$\log_9 \sqrt[3] z$  

$\log_8\sqrt[3]{xy^6}$ 

Solve for x:

$\log_4(x − 2) − \log_4(x + 1) = 1$

$\log_{27}(x) + \log_{27}(x + 8) =\frac23$

### Common Logarithms and Natural Logarithms.

If $\log_b x=y$ then ...

Specifically, if $b= 10$ then $x =$

$x$ is called the Antilogarithm of $y$.

Example:  
$\log 25 = 1.39794$ (What is the base?)

Infer the scale of the antilogarithm from the logarithm  

$\log x = -2.4179$  

This says the logarithm of $x$ to the base ....... is between $-2$ and $-3$

Therefore we infer, $x$ is between .........

We can find the exact value of $x=$ 

### Applications:

**Example 1:** If an earthquake has a shockwave T times greater than the smallest shockwave that can be measured on a seismograph, then the magnitude M on the Richter

scale is given by:

$M = \log_{10} T$

1906 San Francisco earthquake was $8.3$ on Richter Scale 1971 San Fernando earthquake was $6.6$ on Richter Scale.

Find T for each quake and find how much stronger the San Francisco one was compared to the San Fernando one.


**Example 2:** pH  - A scale to measure acidity.

pH $= −\log[H^+]$ (The negative log of the concentration of Hydrogen ions measured in moles per liter).

The concentration of hydrogen ions in acid rain known to kill fish is  
$3.2 \times 10^{−5}$ mole per liter. Find the pH of this acid rain (to the nearest 10th).

Before we calculate, can we guess?

### Natural Logarithms  

When the base of the logartihm is '$e$', we call it a natural logarithm.

We use a special symbol $\ln x$ to mean $\log_e x$

$\ln x = \log_e x$  

All the properties of logarithms holds for natural logarithms as well.

Use the properties of logarithms to expand the expression $\ln Ae^{−2t}$

If $\ln 2 = 0.6931$, $\ln 3 =1.0986$, and $\ln 5 = 1.6094$ find the following:

a) $\ln 10$

b) $\ln 1/3=?$ 

c) $\ln81=$ 


**Change of base theorem**: for $a,b,x>0$ and $a\ne1\ne b$, $$\log_a x=\frac{\log_b x}{\log_b a}$$

How is this useful?

Proof: $a^{\log_a x} = x$ (from identity)

Using the change of base property and a calculator find a decimal approximation of

$\log_5 462$

1. How to define and understand inverse trig functions.
2. Prove and use important properties of inverse trig functions. 
3. How to use inverse trig functions in some practical examples.

Let's start with reviewing $\sin,\cos,\tan,\csc,\sec,\cot$

The most useful way to define $\sin$ and $\cos$ is via the **unit circle** $x^2+y^2=1$.

This has the advantage of clearly showing the meaning of radians, and explains how to calculate (or approximate) $\sin$ and $\cos$ geometrically.

sin https://www.desmos.com/calculator/kxfekf0kgb

cos https://www.desmos.com/calculator/jf2wwsxhzk

The unit circle $x^2+y^2=1$ is not a function, but we can solve for $y$ and graph the **upper unit semicircle** $y=\sqrt{1-x^2}$ and the **lower unit semicircle** $y=-\sqrt{1-x^2}$

`plot(sqrt(1-x^2),-sqrt(1-x^2),sin(x))=?`
`plot(sqrt(1-x^2),-sqrt(1-x^2),cos(x))=?`

(It is interesting to see how the unit circle fits underneath $y=\cos x$. Try to show that $\sqrt{1-x^2}\le\cos x$.)

**Definition of radians:** An angle of $t$ **radians** is a distance $t$ measured counterclockwise along the **arc of a unit circle**, starting from the point $(1,0)$ on the $x$-axis and ending at point $P_t$ on the unit circle.

**Definition of $\sin$ and $\cos$:** For an angle of $t$ radians, if the point $P_t =(x,y)$ on the unit circle then $\cos t=x$ and $\sin t=y$.

Now we can define $\tan t={\sin t \over \cos t}={y\over x}$ 
$\cot t=...$
$\csc t=...$
$\sec t=...$ 

What do they look like? `plot(sin(x),csc(x))=?`
`plot(cos(x),sec(x))=?`
`plot(tan(x),cot(x))=?`
None of these 6 functions is one-to-one so they do not have inverses!

To get inverse trig functions, we have to restrict each trig function to a specific interval on which it is one-to-one. 

Naturally we choose the largest possible interval.

For $\sin x$ we use $[-{\pi\over 2},{\pi\over 2}]$

`plot(sin(x)*sqrt(x+1.57)/(sqrt(x+1.57)+10^-10)*sqrt(-x+1.57)/(sqrt(-x+1.57)+10^-10))=?`
`plot(sin(x)*sqrt(x+1.57)/(sqrt(x+1.57)+10^-10)*sqrt(-x+1.57)/(sqrt(-x+1.57)+10^-10),arcsin(x),x)=?`

`arcsin(0.5)=~?`
`pi/6=?`
`solve(x+2=3,x)=?`

``



Poll Everywhere, Kahoot, MyOpenMath

#### When are two number equal?

In mathematics it is **very useful** to properly understand when two things are equal (i.e. exactly the same).

E.g. two real numbers in decimal form are equal if they have the same sign and exactly the same digits in the same order. Is this correct???? 

Actually NO  :) 

$1/4={1\over 4}=0.25=0.2499999\dots=0.24\bar9$
