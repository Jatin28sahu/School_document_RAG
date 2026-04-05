
## 2.1 Introduction

In Chapter 1, we have studied that the inverse of a function f, denoted by f^-1, exists if f is one-one and onto. There are many functions which are not one-one, onto or both and hence we can not talk of their inverses. In Class XI, we studied that trigonometric functions are not one-one and onto over their natural domains and ranges and hence their inverses do not exist. In this chapter, we shall study about the restrictions on domains and ranges of trigonometric functions which ensure the existence of their inverses and observe their behaviour through graphical representations. Besides, some elementary properties will also be discussed.


The inverse trigonometric functions play an important role in calculus for they serve to define many integrals. The concepts of inverse trigonometric functions is also used in science and engineering.

## 2.2 Basic Concepts

In Class XI, we have studied trigonometric functions, which are defined as follows:

sine function, i.e., sine : R -> [- 1, 1]

cosine function, i.e., cos : R -> [- 1, 1]

tangent function, i.e., tan : R - { x : x = (2n + 1) π/2 , n ∈ Z} -> R

cotangent function, i.e., cot : R - { x : x = nπ, n ∈ Z} -> R

secant function, i.e., sec : R - { x : x = (2n + 1) π/2 , n ∈ Z} -> R - (- 1, 1)

cosecant function, i.e., cosec : R - { x : x = nπ, n ∈ Z} -> R - (- 1, 1)



Page : 19

We have also learnt in Chapter 1 that if f : X→Y such that f(x) = y is one-one and onto, then we can define a unique function g : Y→X such that g(y) = x, where x ∈ X and y = f(x), y ∈ Y. Here, the domain of g = range of f and the range of g = domain of f. The function g is called the inverse of f and is denoted by f^-1. Further, g is also one-one and onto and inverse of g is f. Thus, g^-1 = (f^-1)^-1 = f. We also have
(f^-1 o f) (x) = f^-1 (f(x)) = f^-1 (y) = x
and (f o f^-1) (y) = f (f^-1 (y)) = f (x) = y

Since the domain of sine function is the set of all real numbers and range is the closed interval [-1, 1]. If we restrict its domain to [-π/2, π/2], then it becomes one-one and onto with range [-1, 1]. Actually, sine function restricted to any of the intervals [-3π/2, -π/2], [-π/2, π/2], [π/2, 3π/2] etc., is one-one and its range is [-1, 1]. We can, therefore, define the inverse of sine function in each of these intervals. We denote the inverse of sine function by sin^-1 (arc sine function). Thus, sin^-1 is a function whose domain is [-1, 1] and range could be any of the intervals [-3π/2, -π/2], [-π/2, π/2] or [π/2, 3π/2], and so on. Corresponding to each such interval, we get a branch of the function sin^-1. The branch with range [-π/2, π/2] is called the principal value branch, whereas other intervals as range give different branches of sin^-1. When we refer to the function sin^-1, we take it as the function whose domain is [-1, 1] and range is [-π/2, π/2]. We write sin^-1 : [-1, 1] -> [-π/2, π/2].

From the definition of the inverse functions, it follows that sin (sin^-1 x) = x if -1 ≤ x ≤ 1 and sin^-1 (sin x) = x if -π/2 ≤ x ≤ π/2. In other words, if y = sin^-1 x, then sin y = x.

**Remarks**

(i) We know from Chapter 1, that if y = f(x) is an invertible function, then x = f^-1 (y). Thus, the graph of sin^-1 function can be obtained from the graph of original function by interchanging x and y axes, i.e., if (a, b) is a point on the graph of sine function, then (b, a) becomes the corresponding point on the graph of inverse


Page : 20

of sine function. Thus, the graph of the function y = sin<sup>-1</sup> x can be obtained from the graph of y = sin x by interchanging x and y axes. The graphs of y = sin x and y = sin<sup>-1</sup> x are as given in Fig 2.1 (i), (ii), (iii). The dark portion of the graph of y = sin<sup>-1</sup> x represent the principal value branch.

It can be shown that the graph of an inverse function can be obtained from the corresponding graph of original function as a mirror image (i.e., reflection) along the line y = x. This can be visualised by looking the graphs of y = sin x and y = sin<sup>-1</sup> x as given in the same axes (Fig 2.1 (iii)).

![Graph of y = sin x showing the periodic wave along the x-axis.](image)
Fig 2.1 (i)

![Graph of y = sin-1 x showing the periodic wave along the y-axis with the principal value branch highlighted in bold.](image)
Fig 2.1 (ii)

![Combined graph of y = sin x, y = sin-1 x, and the line y = x showing their reflectional symmetry.](image)
Fig 2.1 (iii)

Like sine function, the cosine function is a function whose domain is the set of all real numbers and range is the set [-1, 1]. If we restrict the domain of cosine function to [0, π], then it becomes one-one and onto with range [-1, 1]. Actually, cosine function


Page : 21

restricted to any of the intervals [-π, 0], [0, π], [π, 2π] etc., is bijective with range as [-1, 1]. We can, therefore, define the inverse of cosine function in each of these intervals. We denote the inverse of the cosine function by cos^-1 (arc cosine function). Thus, cos^-1 is a function whose domain is [-1, 1] and range could be any of the intervals [-π, 0], [0, π], [π, 2π] etc. Corresponding to each such interval, we get a branch of the function cos^-1. The branch with range [0, π] is called the principal value branch of the function cos^-1. We write
cos^-1 : [-1, 1] -> [0, π].
The graph of the function given by y = cos^-1 x can be drawn in the same way as discussed about the graph of y = sin^-1 x. The graphs of y = cos x and y = cos^-1 x are given in Fig 2.2 (i) and (ii).

![Graph of y = cos x showing the wave pattern from -3π/2 to 5π/2 on the x-axis and -1 to 1 on the y-axis.](image)
Fig 2.2 (i)

![Graph of y = cos^-1 x showing the curve from -1 to 1 on the x-axis and 0 to π on the y-axis.](image)
Fig 2.2 (ii)

Let us now discuss cosec^-1 x and sec^-1 x as follows:
Since, cosec x = 1 / sin x, the domain of the cosec function is the set {x : x ∈ R and x ≠ nπ, n ∈ Z} and the range is the set {y : y ∈ R, y ≥ 1 or y ≤ -1} i.e., the set R - (-1, 1). It means that y = cosec x assumes all real values except -1 < y < 1 and is not defined for integral multiple of π. If we restrict the domain of cosec function to [-π/2, π/2] - {0}, then it is one to one and onto with its range as the set R - (-1, 1). Actually, cosec function restricted to any of the intervals [[-3π/2, -π/2] - {-π}], [[-π/2, π/2] - {0}], [[π/2, 3π/2] - {π}] etc., is bijective and its range is the set of all real numbers R - (-1, 1).


Page : 22

Thus cosec^-1 can be defined as a function whose domain is R - (-1, 1) and range could be any of the intervals [-3π/2, -π/2] - {-π}, [-π/2, π/2] - {0}, [π/2, 3π/2] - {π} etc. The function corresponding to the range [-π/2, π/2] - {0} is called the principal value branch of cosec^-1. We thus have principal branch as

cosec^-1 : R - (-1, 1) -> [-π/2, π/2] - {0}

The graphs of y = cosec x and y = cosec^-1 x are given in Fig 2.3 (i), (ii).

![Graph of y = cosec x showing periodic curves with vertical asymptotes at multiples of π.](image)
**Fig 2.3 (i)**

![Graph of y = cosec^-1 x showing two branches defined for x ≤ -1 and x ≥ 1.](image)
**Fig 2.3 (ii)**

Also, since sec x = 1 / cos x, the domain of y = sec x is the set R - {x : x = (2n + 1) π/2, n ∈ Z} and range is the set R - (-1, 1). It means that sec (secant function) assumes all real values except -1 < y < 1 and is not defined for odd multiples of π/2. If we restrict the domain of secant function to [0, π] - {π/2}, then it is one-one and onto with


Page : 23

its range as the set R – (–1, 1). Actually, secant function restricted to any of the intervals [–π, 0] – { -π/2 }, [0, π] – { π/2 }, [π, 2π] – { 3π/2 } etc., is bijective and its range is R – {–1, 1}. Thus sec^-1 can be defined as a function whose domain is R – (–1, 1) and range could be any of the intervals [–π, 0] – { -π/2 }, [0, π] – { π/2 }, [π, 2π] – { 3π/2 } etc. Corresponding to each of these intervals, we get different branches of the function sec^-1. The branch with range [0, π] – { π/2 } is called the principal value branch of the function sec^-1. We thus have

sec^-1 : R – (–1, 1) → [0, π] – { π/2 }

The graphs of the functions y = sec x and y = sec^-1 x are given in Fig 2.4 (i), (ii).

![Graph of y = sec x showing periodic curves with vertical asymptotes at odd multiples of π/2.](image)
**Fig 2.4 (i)**

![Graph of y = sec^-1 x showing two branches, one from 0 to π/2 and another from π/2 to π, with a horizontal asymptote at y = π/2.](image)
**Fig 2.4 (ii)**

Finally, we now discuss tan^-1 and cot^-1. We know that the domain of the tan function (tangent function) is the set {x : x ∈ R and x ≠ (2n + 1) π/2, n ∈ Z} and the range is R. It means that tan function is not defined for odd multiples of π/2. If we restrict the domain of tangent function to


Page : 24

(-pi/2, pi/2), then it is one-one and onto with its range as R. Actually, tangent function restricted to any of the intervals (-3pi/2, -pi/2), (-pi/2, pi/2), (pi/2, 3pi/2) etc., is bijective and its range is R. Thus tan^-1 can be defined as a function whose domain is R and range could be any of the intervals (-3pi/2, -pi/2), (-pi/2, pi/2), (pi/2, 3pi/2) and so on. These intervals give different branches of the function tan^-1. The branch with range (-pi/2, pi/2) is called the principal value branch of the function tan^-1.

We thus have
tan^-1 : R -> (-pi/2, pi/2)

The graphs of the function y = tan x and y = tan^-1 x are given in Fig 2.5 (i), (ii).

![Graph of y = tan x showing multiple vertical branches separated by asymptotes at odd multiples of pi/2.](image)
Fig 2.5 (i)

![Graph of y = tan^-1 x showing a single continuous curve bounded by horizontal asymptotes at y = pi/2 and y = -pi/2.](image)
Fig 2.5 (ii)

We know that domain of the cot function (cotangent function) is the set {x : x belongs to R and x != n*pi, n belongs to Z} and range is R. It means that cotangent function is not defined for integral multiples of pi. If we restrict the domain of cotangent function to (0, pi), then it is bijective and its range as R. In fact, cotangent function restricted to any of the intervals (-pi, 0), (0, pi), (pi, 2π) etc., is bijective and its range is R. Thus cot^-1 can be defined as a function whose domain is the R and range as any of the

Page : 25

intervals (-π, 0), (0, π), (π, 2π) etc. These intervals give different branches of the function cot^-1. The function with range (0, π) is called the principal value branch of the function cot^-1. We thus have
cot^-1 : R → (0, π)
The graphs of y = cot x and y = cot^-1 x are given in Fig 2.6 (i), (ii).

![Graph of y = cot x](image)
Fig 2.6 (i)

![Graph of y = cot^-1 x](image)
Fig 2.6 (ii)

The following table gives the inverse trigonometric function (principal value branches) along with their domains and ranges.


|Inverse Function|Domain|Range|
|-|-|-|
|sin^-1|\[-1, 1]|\[-π/2, π/2]|
|cos^-1|\[-1, 1]|\[0, π]|
|cosec^-1|R - (-1, 1)|\[-π/2, π/2] - {0}|
|sec^-1|R - (-1, 1)|\[0, π] - {π/2}|
|tan^-1|R|(-π/2, π/2)|
|cot^-1|R|(0, π)|



Page : 26

Note
1. sin<sup>–1</sup>x should not be confused with (sin x)<sup>–1</sup>. In fact (sin x)<sup>–1</sup> = 1/sin x and similarly for other trigonometric functions.
2. Whenever no branch of an inverse trigonometric functions is mentioned, we mean the principal value branch of that function.
3. The value of an inverse trigonometric functions which lies in the range of principal branch is called the principal value of that inverse trigonometric functions.

We now consider some examples:

### Example 1
Find the principal value of sin<sup>–1</sup> (1/√2).

**Solution** Let sin<sup>–1</sup> (1/√2) = y. Then, sin y = 1/√2.
We know that the range of the principal value branch of sin<sup>–1</sup> is [–π/2, π/2] and sin (π/4) = 1/√2. Therefore, principal value of sin<sup>–1</sup> (1/√2) is π/4.

### Example 2
Find the principal value of cot<sup>–1</sup> (–1/√3)

**Solution** Let cot<sup>–1</sup> (–1/√3) = y. Then,
cot y = –1/√3 = – cot (π/3) = cot (π – π/3) = cot (2π/3)
We know that the range of principal value branch of cot<sup>–1</sup> is (0, π) and cot (2π/3) = –1/√3. Hence, principal value of cot<sup>–1</sup> (–1/√3) is 2π/3.



## 2.3 Properties of Inverse Trigonometric Functions

In this section, we shall prove some important properties of inverse trigonometric functions. It may be mentioned here that these results are valid within the principal value branches of the corresponding inverse trigonometric functions and wherever they are defined. Some results may not be valid for all values of the domains of inverse trigonometric functions. In fact, they will be valid only for some values of x for which inverse trigonometric functions are defined. We will not go into the details of these values of x in the domain as this discussion goes beyond the scope of this textbook.

Let us recall that if y = sin^-1 x, then x = sin y and if x = sin y, then y = sin^-1 x. This is equivalent to

sin (sin^-1 x) = x, x in [-1, 1] and sin^-1 (sin x) = x, x in [-pi/2, pi/2]

For suitable values of domain similar results follow for remaining trigonometric functions.

Page : 23

its range as the set R - (-1, 1). Actually, secant function restricted to any of the intervals [-π, 0] - {-π/2}, [π, 2π] - {3π/2} etc., is bijective and its range is R - {-1, 1}. Thus sec^-1 can be defined as a function whose domain is R - (-1, 1) and its range as the set [0, π] - {π/2}. Corresponding to each of these intervals, we get different branches of the function sec^-1.

We now consider some examples.

### Example 3
Show that
(i) sin^-1 (2x sqrt(1 - x^2)) = 2 sin^-1 x, -1/sqrt(2) <= x <= 1/sqrt(2)
(ii) sin^-1 (2x sqrt(1 - x^2)) = 2 cos^-1 x, 1/sqrt(2) <= x <= 1

**Solution**
(i) Let x = sin θ. Then sin^-1 x = θ. We have
sin^-1 (2x sqrt(1 - x^2)) = sin^-1 (2 sin θ sqrt(1 - sin^2 θ))
= sin^-1 (2 sin θ cos θ) = sin^-1 (sin 2θ) = 2θ
= 2 sin^-1 x

(ii) Take x = cos θ, then proceeding as above, we get, sin^-1 (2x sqrt(1 - x^2)) = 2 cos^-1 x

### Example 4
Express tan^-1 (cos x / (1 - sin x)), -3π/2 < x < π/2 in the simplest form.

**Solution**
We write
tan^-1 (cos x / (1 - sin x)) = tan^-1 [(cos^2 (x/2) - sin^2 (x/2)) / (cos^2 (x/2) + sin^2 (x/2) - 2 sin (x/2) cos (x/2))]
= tan^-1 [((cos (x/2) + sin (x/2)) (cos (x/2) - sin (x/2))) / (cos (x/2) - sin (x/2))^2]
= tan^-1 [(cos (x/2) + sin (x/2)) / (cos (x/2) - sin (x/2))]
= tan^-1 [(1 + tan (x/2)) / (1 - tan (x/2))]
= tan^-1 [tan (π/4 + x/2)] = π/4 + x/2

![Graph of y = sec x showing multiple branches and the restricted principal value branch.](image)
Fig 2.4 (i)

![Graph of y = sec^-1 x showing the principal value branch with domain R - (-1, 1) and range [0, π] - {π/2}.](image)
Fig 2.4 (ii)

Reprint 2025-26

INVERSE TRIGONOMETRIC FUNCTIONS 25

Page : 25

intervals (π, 0), (0, π), (π, 2π) etc. These intervals give different branches of the function cot^-1. The function with range (0, π) is called the principal value branch of the function cot^-1. We thus have
cot^-1 : R → (0, π)
The graphs of y = cot x and y = cot^-1 x are given in Fig 2.6 (i), (ii)

### Example 5
Write cot^-1 (1 / (x^2 - 1)^1/2), x > 1 in the simplest form.

**Solution** Let x = sec θ, then (x^2 - 1)^1/2 = (sec^2 θ - 1)^1/2 = tan θ
Therefore, cot^-1 (1 / (x^2 - 1)^1/2) = cot^-1 (cot θ) = θ = sec^-1 x, which is the simplest form.


## Miscellaneous Examples

### Example 6
Find the value of sin^-1 (sin 3π/5)

**Solution** We know that sin^-1(sin x) = x. Therefore, sin^-1(sin 3π/5) = 3π/5.
But 3π/5 ∉ [-π/2, π/2], which is the principal branch of sin^-1 x.
However sin (3π/5) = sin(π - 3π/5) = sin 2π/5 and 2π/5 ∈ [-π/2, π/2].
Therefore sin^-1(sin 3π/5) = sin^-1(sin 2π/5) = 2π/5.

Reprint 2025-26

INVERSE TRIGONOMETRIC FUNCTIONS 31

Page : 31


### Summary

- The domains and ranges (principal value branches) of inverse trigonometric functions are given in the following table:


|Functions|Domain|Range (Principal Value Branches)|
|-|-|-|
|y = sin^-1 x|\[-1, 1]|\[-π/2, π/2]|
|y = cos^-1 x|\[-1, 1]|\[0, π]|
|y = cosec^-1 x|R - (-1, 1)|\[-π/2, π/2] - {0}|
|y = sec^-1 x|R - (-1, 1)|\[0, π] - {π/2}|
|y = tan^-1 x|R|(-π/2, π/2)|
|y = cot^-1 x|R|(0, π)|


- sin^-1 x should not be confused with (sin x)^-1. In fact (sin x)^-1 = 1 / sin x and similarly for other trigonometric functions.
- The value of an inverse trigonometric functions which lies in its principal value branch is called the principal value of that inverse trigonometric functions.
- For suitable values of domain, we have
- y = sin^-1 x => x = sin y
- x = sin y => y = sin^-1 x
- sin (sin^-1 x) = x
- sin^-1 (sin x) = x

We know that domain of the cot function (cotangent function) is the set {x : x ∈ R and x ≠ nπ, n ∈ Z} and range is R. It means that cotangent function is not defined for integral multiples of π. If we restrict the domain of cotangent function to (0, π), then it is bijective with and its range as R. In fact, cotangent function restricted to any of the intervals (-π, 0), (0, π), (π, 2π) etc., is bijective and its range is R. Thus cot^-1 can be defined as a function whose domain is the R and range as any of the intervals (-π, 0), (0, π), (π, 2π) and so on. These range could be any of the intervals.


Page : 33

then it is one-one and onto with its range as R. Actually, tangent function restricted to any of the intervals (-3π/2, -π/2), (-π/2, π/2), (π/2, 3π/2) etc., is bijective and its range is R. Thus tan<sup>-1</sup> can be defined as a function whose domain is R and range could be any of the intervals (-3π/2, -π/2), (-π/2, π/2), (π/2, 3π/2) and so on. These intervals give different branches of the function tan<sup>-1</sup>. The branch with range (-π/2, π/2) is called the principal value branch of the function tan<sup>-1</sup>. We thus have

tan<sup>-1</sup> : R → (-π/2, π/2)

The graphs of the function y = tan x and y = tan<sup>-1</sup> x are given in Fig 2.5 (i) and (ii).

![Graph of y = tan x showing multiple vertical branches separated by asymptotes at odd multiples of pi/2.](image)
Fig 2.5 (i)

![Graph of y = tan inverse x showing a single continuous curve bounded by horizontal asymptotes at y = pi/2 and y = -pi/2.](image)
Fig 2.5 (ii)

We know that domain of the cot function (cotangent function) is the set {x : x ∈ R and x ≠ nπ, n ∈ Z}, i.e., the set of all real numbers except those which are integral multiples of π. If we restrict the domain of cotangent function to (0, π), then it is bijective with its range as R. In fact, cotangent function restricted to any of the intervals (-π, 0), (0, π), (π, 2π) etc., is bijective and its range is R. Thus cot<sup>-1</sup> can be defined as a function whose domain is R and range as any of the intervals (-π, 0), (0, π), (π, 2π) etc. The branch with range (0, π) is called the principal value branch of the function cot<sup>-1</sup>. We thus have

cot<sup>-1</sup> : R → (0, π)

The graphs of y = cot x and y = cot<sup>-1</sup> x are given in Fig 2.6 (i) and (ii).

