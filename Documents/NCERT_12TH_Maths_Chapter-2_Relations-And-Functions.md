
## 1.1 Introduction

Recall that the notion of relations and functions, domain, co-domain and range have been introduced in Class XI along with different types of specific real valued functions and their graphs. The concept of the term ‘relation’ in mathematics has been drawn from the meaning of relation in English language, according to which two objects or quantities are related if there is a recognisable connection or link between the two objects or quantities. Let A be the set of students of Class XII of a school and B be the set of students of Class XI of the same school. Then some of the examples of relations from A to B are

![Lejeune Dirichlet (1805-1859)](page_1_image_1_v2.jpg)

Lejeune Dirichlet
(1805-1859)

(i) {(a, b) ∈ A × B: a is brother of b},

(ii) {(a, b) ∈ A × B: a is sister of b},

(iii) {(a, b) ∈ A × B: age of a is greater than age of b},

(iv) {(a, b) ∈ A × B: total marks obtained by a in the final examination is less than the total marks obtained by b in the final examination},

(v) {(a, b) ∈ A × B: a lives in the same locality as b}. However, abstracting from this, we define mathematically a relation R from A to B as an arbitrary subset of A × B.

If (a, b) ∈ R, we say that a is related to b under the relation R and we write as a R b. In general, (a, b) ∈ R, we do not bother whether there is a recognisable connection or link between a and b. As seen in Class XI, functions are special kind of relations.

In this chapter, we will study different types of relations and functions, composition of functions, invertible functions and binary operations.

Reprint 2025-26

2 MATHEMATICS

Page : 2

## 1.2 Types of Relations

In this section, we would like to study different types of relations. We know that a relation in a set A is a subset of A × A. Thus, the empty set φ and A × A are two extreme relations. For illustration, consider a relation R in the set A = {1, 2, 3, 4} given by R = {(a, b): a – b = 10}. This is the empty set, as no pair (a, b) satisfies the condition a – b = 10. Similarly, R′ = {(a, b) : | a – b | ≥ 0} is the whole set A × A, as all pairs (a, b) in A × A satisfy | a – b | ≥ 0. These two extreme examples lead us to the following definitions.

**Definition 1** A relation R in a set A is called empty relation, if no element of A is related to any element of A, i.e., R = φ ⊂ A × A.

**Definition 2** A relation R in a set A is called universal relation, if each element of A is related to every element of A, i.e., R = A × A.

Both the empty relation and the universal relation are some times called trivial relations.

### Example 1
Let A be the set of all students of a boys school. Show that the relation R in A given by R = {(a, b) : a is sister of b} is the empty relation and R′ = {(a, b) : the difference between heights of a and b is less than 3 meters} is the universal relation.

**Solution** Since the school is boys school, no student of the school can be sister of any student of the school. Hence, R = φ, showing that R is the empty relation. It is also obvious that the difference between heights of any two students of the school has to be less than 3 meters. This shows that R′ = A × A is the universal relation.

**Remark** In Class XI, we have seen two ways of representing a relation, namely roster method and set builder method. However, a relation R in the set {1, 2, 3, 4} defined by R = {(a, b) : b = a + 1} is also expressed as a R b if and only if b = a + 1 by many authors. We may also use this notation, as and when convenient.

If (a, b) ∈ R, we say that a is related to b and we denote it as a R b.

One of the most important relation, which plays a significant role in Mathematics, is an equivalence relation. To study equivalence relation, we first consider three types of relations, namely reflexive, symmetric and transitive.

**Definition 3** A relation R in a set A is called
(i) reflexive, if (a, a) ∈ R, for every a ∈ A,
(ii) symmetric, if (a<sub>1</sub>, a<sub>2</sub>) ∈ R implies that (a<sub>2</sub>, a<sub>1</sub>) ∈ R, for all a<sub>1</sub>, a<sub>2</sub> ∈ A.
(iii) transitive, if (a<sub>1</sub>, a<sub>2</sub>) ∈ R and (a<sub>2</sub>, a<sub>3</sub>) ∈ R implies that (a<sub>1</sub>, a<sub>3</sub>) ∈ R, for all a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> ∈ A.

Reprint 2025-26

RELATIONS AND FUNCTIONS 3

Page : 3

Definition 4 A relation R in a set A is said to be an equivalence relation if R is reflexive, symmetric and transitive.

### Example 2
Let T be the set of all triangles in a plane with R a relation in T given by R = {(T<sub>1</sub>, T<sub>2</sub>) : T<sub>1</sub> is congruent to T<sub>2</sub>}. Show that R is an equivalence relation.

**Solution** R is reflexive, since every triangle is congruent to itself. Further, (T<sub>1</sub>, T<sub>2</sub>) ∈ R ⇒ T<sub>1</sub> is congruent to T<sub>2</sub> ⇒ T<sub>2</sub> is congruent to T<sub>1</sub> ⇒ (T<sub>2</sub>, T<sub>1</sub>) ∈ R. Hence, R is symmetric. Moreover, (T<sub>1</sub>, T<sub>2</sub>), (T<sub>2</sub>, T<sub>3</sub>) ∈ R ⇒ T<sub>1</sub> is congruent to T<sub>2</sub> and T<sub>2</sub> is congruent to T<sub>3</sub> ⇒ T<sub>1</sub> is congruent to T<sub>3</sub> ⇒ (T<sub>1</sub>, T<sub>3</sub>) ∈ R. Therefore, R is an equivalence relation.

### Example 3
Let L be the set of all lines in a plane and R be the relation in L defined as R = {(L<sub>1</sub>, L<sub>2</sub>) : L<sub>1</sub> is perpendicular to L<sub>2</sub>}. Show that R is symmetric but neither reflexive nor transitive.

![Three lines L1, L2, and L3 where L1 is horizontal, L2 is vertical intersecting L1, and L3 is horizontal intersecting L2. L1 and L3 are parallel to each other.](image)
Fig 1.1

**Solution** R is not reflexive, as a line L<sub>1</sub> can not be perpendicular to itself, i.e., (L<sub>1</sub>, L<sub>1</sub>) ∉ R. R is symmetric as (L<sub>1</sub>, L<sub>2</sub>) ∈ R ⇒ L<sub>1</sub> is perpendicular to L<sub>2</sub> ⇒ L<sub>2</sub> is perpendicular to L<sub>1</sub> ⇒ (L<sub>2</sub>, L<sub>1</sub>) ∈ R. R is not transitive. Indeed, if L<sub>1</sub> is perpendicular to L<sub>2</sub> and L<sub>2</sub> is perpendicular to L<sub>3</sub>, then L<sub>1</sub> can never be perpendicular to L<sub>3</sub>. In fact, L<sub>1</sub> is parallel to L<sub>3</sub>, i.e., (L<sub>1</sub>, L<sub>2</sub>) ∈ R, (L<sub>2</sub>, L<sub>3</sub>) ∈ R but (L<sub>1</sub>, L<sub>3</sub>) ∉ R.

### Example 4
Show that the relation R in the set {1, 2, 3} given by R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)} is reflexive but neither symmetric nor transitive.

**Solution** R is reflexive, since (1, 1), (2, 2) and (3, 3) lie in R. Also, R is not symmetric, as (1, 2) ∈ R but (2, 1) ∉ R. Similarly, R is not transitive, as (1, 2) ∈ R and (2, 3) ∈ R but (1, 3) ∉ R.

### Example 5
Show that the relation R in the set Z of integers given by R = {(a, b) : 2 divides a - b} is an equivalence relation.

**Solution** R is reflexive, as 2 divides (a - a) for all a ∈ Z. Further, if (a, b) ∈ R, then 2 divides a - b. Therefore, 2 divides b - a. Hence, (b, a) ∈ R, which shows that R is symmetric. Similarly, if (a, b) ∈ R and (b, c) ∈ R, then a - b and b - c are divisible by 2. Now, a - c = (a - b) + (b - c) is even (Why?). So, (a - c) is divisible by 2. This shows that R is transitive. Thus, R is an equivalence relation in Z.

Reprint 2025-26

Page : 4

In Example 5, note that all even integers are related to zero, as (0, ± 2), (0, ± 4) etc., lie in R and no odd integer is related to 0, as (0, ± 1), (0, ± 3) etc., do not lie in R. Similarly, all odd integers are related to one and no even integer is related to one. Therefore, the set E of all even integers and the set O of all odd integers are subsets of Z satisfying following conditions:

(i) All elements of E are related to each other and all elements of O are related to each other.
(ii) No element of E is related to any element of O and vice-versa.
(iii) E and O are disjoint and Z = E ∪ O.

The subset E is called the equivalence class containing zero and is denoted by [0]. Similarly, O is the equivalence class containing 1 and is denoted by [1]. Note that [0] ≠ [1], [0] = [2r] and [1] = [2r + 1], r ∈ Z. Infact, what we have seen above is true for an arbitrary equivalence relation R in a set X. Given an arbitrary equivalence relation R in an arbitrary set X, R divides X into mutually disjoint subsets A<sub>i</sub> called partitions or subdivisions of X satisfying:

(i) all elements of A<sub>i</sub> are related to each other, for all i.
(ii) no element of A<sub>i</sub> is related to any element of A<sub>j</sub>, i ≠ j.
(iii) ∪ A<sub>j</sub> = X and A<sub>i</sub> ∩ A<sub>j</sub> = φ, i ≠ j.

The subsets A<sub>i</sub> are called equivalence classes. The interesting part of the situation is that we can go reverse also. For example, consider a subdivision of the set Z given by three mutually disjoint subsets A<sub>1</sub>, A<sub>2</sub> and A<sub>3</sub> whose union is Z with

A<sub>1</sub> = {x ∈ Z : x is a multiple of 3} = {..., – 6, – 3, 0, 3, 6, ...}
A<sub>2</sub> = {x ∈ Z : x – 1 is a multiple of 3} = {..., – 5, – 2, 1, 4, 7, ...}
A<sub>3</sub> = {x ∈ Z : x – 2 is a multiple of 3} = {..., – 4, – 1, 2, 5, 8, ...}

Define a relation R in Z given by R = {(a, b) : 3 divides a – b}. Following the arguments similar to those used in Example 5, we can show that R is an equivalence relation. Also, A<sub>1</sub> coincides with the set of all integers in Z which are related to zero, A<sub>2</sub> coincides with the set of all integers which are related to 1 and A<sub>3</sub> coincides with the set of all integers in Z which are related to 2. Thus, A<sub>1</sub> = [0], A<sub>2</sub> = [1] and A<sub>3</sub> = [2]. In fact, A<sub>1</sub> = [3r], A<sub>2</sub> = [3r + 1] and A<sub>3</sub> = [3r + 2], for all r ∈ Z.

### Example 6
Let R be the relation defined in the set A = {1, 2, 3, 4, 5, 6, 7} by R = {(a, b) : both a and b are either odd or even}. Show that R is an equivalence relation. Further, show that all the elements of the subset {1, 3, 5, 7} are related to each other and all the elements of the subset {2, 4, 6} are related to each other, but no element of the subset {1, 3, 5, 7} is related to any element of the subset {2, 4, 6}.

RELATIONS AND FUNCTIONS 5

Page : 5

Solution Given any element a in A, both a and a must be either odd or even, so that (a, a) ∈ R. Further, (a, b) ∈ R ⇒ both a and b must be either odd or even ⇒ (b, a) ∈ R. Similarly, (a, b) ∈ R and (b, c) ∈ R ⇒ all elements a, b, c, must be either even or odd simultaneously ⇒ (a, c) ∈ R. Hence, R is an equivalence relation. Further, all the elements of {1, 3, 5, 7} are related to each other, as all the elements of this subset are odd. Similarly, all the elements of the subset {2, 4, 6} are related to each other, as all of them are even. Also, no element of the subset {1, 3, 5, 7} can be related to any element of {2, 4, 6}, as elements of {1, 3, 5, 7} are odd, while elements of {2, 4, 6} are even.



## 1.3 Types of Functions

The notion of a function along with some special functions like identity function, constant function, polynomial function, rational function, modulus function, signum function etc. along with their graphs have been given in Class XI. Addition, subtraction, multiplication and division of two functions have also been studied. As the concept of function is of paramount importance in mathematics and among other disciplines as well, we would like to extend our study about function from where we finished earlier. In this section, we would like to study different types of functions.

Consider the functions f<sub>1</sub>, f<sub>2</sub>, f<sub>3</sub> and f<sub>4</sub> given by the following diagrams.

![Four diagrams showing mappings between sets X1 and X2, X1 and X3, and X1 and X4, illustrating different types of functions (one-one, many-one, onto).](image)

In Fig 1.2, we observe that the images of distinct elements of X<sub>1</sub> under the function f<sub>1</sub> are distinct, but the image of two distinct elements 1 and 2 of X<sub>1</sub> under f<sub>2</sub> is same, namely b. Further, there are some elements like e and f in X<sub>2</sub> which are not images of any element of X<sub>1</sub> under f<sub>1</sub>, while all elements of X<sub>3</sub> are images of some elements of X<sub>1</sub> under f<sub>3</sub>. The above observations lead to the following definitions:

**Definition 5** A function f : X → Y is defined to be one-one (or injective), if the images of distinct elements of X under f are distinct, i.e., for every x<sub>1</sub>, x<sub>2</sub> ∈ X, f (x<sub>1</sub>) = f (x<sub>2</sub>) implies x<sub>1</sub> = x<sub>2</sub>. Otherwise, f is called many-one.

The function f<sub>1</sub> and f<sub>4</sub> in Fig 1.2 (i) and (iv) are one-one and the function f<sub>2</sub> and f<sub>3</sub> in Fig 1.2 (ii) and (iii) are many-one.

**Definition 6** A function f : X → Y is said to be onto (or surjective), if every element of Y is the image of some element of X under f, i.e., for every y ∈ Y, there exists an element x in X such that f (x) = y.

The function f<sub>3</sub> and f<sub>4</sub> in Fig 1.2 (iii), (iv) are onto and the function f<sub>1</sub> in Fig 1.2 (i) is not onto as elements e, f in X<sub>2</sub> are not the image of any element in X<sub>1</sub> under f<sub>1</sub>.

Reprint 2025-26

8 MATHEMATICS

Page : 8

![Four diagrams illustrating different types of function mappings between sets X and Y. (i) shows a one-one but not onto function. (ii) shows a many-one but not onto function. (iii) shows a one-one and onto function. (iv) shows a many-one and onto function.](image)

Fig 1.2 (i) to (iv)

Remark f : X → Y is onto if and only if Range of f = Y.

Definition 7 A function f : X → Y is said to be one-one and onto (or bijective), if f is both one-one and onto.

The function f<sub>4</sub> in Fig 1.2 (iv) is one-one and onto.

### Example 7
Let A be the set of all 50 students of Class X in a school. Let f : A → N be function defined by f (x) = roll number of the student x. Show that f is one-one but not onto.

**Solution** No two different students of the class can have same roll number. Therefore, f must be one-one. We can assume without any loss of generality that roll numbers of students are from 1 to 50. This implies that 51 in N is not roll number of any student of the class, so that 51 can not be image of any element of X under f. Hence, f is not onto.

### Example 8
Show that the function f : N → N, given by f (x) = 2x, is one-one but not onto.

**Solution** The function f is one-one, for f (x1) = f (x2) ⇒ 2x1 = 2x2 ⇒ x1 = x2. Further, f is not onto, as for 1 ∈ N, there does not exist any x in N such that f (x) = 2x = 1.

Reprint 2025-26

RELATIONS AND FUNCTIONS 9

Page : 9

### Example 9
Prove that the function f : R -> R, given by f(x) = 2x, is one-one and onto.

**Solution** f is one-one, as f(x1) = f(x2) => 2x1 = 2x2 => x1 = x2. Also, given any real number y in R, there exists y/2 in R such that f(y/2) = 2 . (y/2) = y. Hence, f is onto.

![Graph of the function f(x) = 2x showing a straight line passing through the origin.](image)
Fig 1.3

### Example 10
Show that the function f : N -> N, given by f(1) = f(2) = 1 and f(x) = x - 1, for every x > 2, is onto but not one-one.

**Solution** f is not one-one, as f(1) = f(2) = 1. But f is onto, as given any y in N, y != 1, we can choose x as y + 1 such that f(y + 1) = y + 1 - 1 = y. Also for 1 in N, we have f(1) = 1.

### Example 11
Show that the function f : R -> R, defined as f(x) = x^2, is neither one-one nor onto.

**Solution** Since f(-1) = 1 = f(1), f is not one-one. Also, the element -2 in the co-domain R is not image of any element x in the domain R (Why?). Therefore f is not onto.

![Graph of the function f(x) = x^2 showing a parabola opening upwards. The image of 1 and -1 under f is 1.](image)
Fig 1.4

### Example 12
Show that f : N -> N, given by
f(x) = x + 1, if x is odd,
       x - 1, if x is even
is both one-one and onto.

Solution

Suppose \( f(x_1) = f(x_2) \). Note that if \( x_1 \) is odd and \( x_2 \) is even, then we will have  
\( x_1 + 1 = x_2 - 1 \), i.e., \( x_2 - x_1 = 2 \), which is impossible. Similarly, the possibility of \( x_1 \) being even and \( x_2 \) being odd can also be ruled out, using the similar argument. Therefore, both \( x_1 \) and \( x_2 \) must be either odd or even.

Suppose both \( x_1 \) and \( x_2 \) are odd. Then  
\( f(x_1) = f(x_2) \Rightarrow x_1 - 1 = x_2 - 1 \Rightarrow x_1 = x_2 \).  

Similarly, if both \( x_1 \) and \( x_2 \) are even, then also  
\( f(x_1) = f(x_2) \Rightarrow x_1 = x_2 \).  

Thus, \( f \) is one-one. Also, any odd number \( 2r + 1 \) in the co-domain \( \mathbb{N} \) is the image of \( 2r + 2 \) in the domain \( \mathbb{N} \), and any even number \( 2r \) in the co-domain \( \mathbb{N} \) is the image of \( 2r - 1 \) in the domain \( \mathbb{N} \). Thus, \( f \) is onto.

---

### Example 13
Show that an onto function \( f : \{1, 2, 3\} \to \{1, 2, 3\} \) is always one-one.

Solution

Suppose \( f \) is not one-one. Then there exist two elements, say 1 and 2 in the domain whose image in the co-domain is same. Also, the image of 3 under \( f \) can be only one element. Therefore, the range set can have at most two elements of the co-domain \( \{1, 2, 3\} \), showing that \( f \) is not onto, a contradiction. Hence, \( f \) must be one-one.


### Example 14
Show that a one-one function \( f : \{1, 2, 3\} \to \{1, 2, 3\} \) must be onto.

Solution

Since \( f \) is one-one, three elements of \( \{1, 2, 3\} \) must be taken to 3 different elements of the co-domain \( \{1, 2, 3\} \) under \( f \). Hence, \( f \) has to be onto.


Remark

The results mentioned in Examples 13 and 14 are also true for an arbitrary finite set \( X \), i.e., a one-one function \( f : X \to X \) is necessarily onto and an onto map \( f : X \to X \) is necessarily one-one, for every finite set \( X \).  

In contrast to this, Examples 8 and 10 show that for an infinite set, this may not be true. In fact, this is a characteristic difference between a finite and an infinite set.

## 1.4 Composition of Functions and Invertible Function

**Definition 8** Let f : A → B and g : B → C be two functions. Then the composition of f and g, denoted by gof, is defined as the function gof : A → C given by
gof (x) = g(f (x)), ∀ x ∈ A.

![Diagram showing the composition of functions f and g. Set A maps to set B via function f, and set B maps to set C via function g. The direct mapping from A to C is labeled gof.](image)

### Example 15
Let f : {2, 3, 4, 5} → {3, 4, 5, 9} and g : {3, 4, 5, 9} → {7, 11, 15} be functions defined as f (2) = 3, f (3) = 4, f (4) = 5, f (5) = 5 and g (3) = g (4) = 7 and g (5) = g (9) = 11. Find gof.

**Solution** We have gof (2) = g (f (2)) = g (3) = 7, gof (3) = g (f (3)) = g (4) = 7, gof (4) = g (f (4)) = g (5) = 11 and gof (5) = g (f (5)) = g (5) = 11.

### Example 16
Find gof and fog, if f : R → R and g : R → R are given by f (x) = cos x and g(x) = 3x^2. Show that gof ≠ fog.

**Solution** We have gof (x) = g (f (x)) = g(cos x) = 3 (cos x)^2 = 3 cos^2 x. Similarly, fog (x) = f (g(x)) = f (3x^2) = cos (3x^2). Note that 3cos^2 x ≠ cos 3x^2, for x = 0. Hence, gof ≠ fog.

**Definition 9** A function f : X → Y is defined to be invertible, if there exists a function g : Y → X such that gof = I_X and fog = I_Y. The function g is called the inverse of f and is denoted by f^-1.

Thus, if f is invertible, then f must be one-one and onto and conversely, if f is one-one and onto, then f must be invertible. This fact significantly helps for proving a function f to be invertible by showing that f is one-one and onto, specially when the actual inverse of f is not to be determined.

### Example 17
Let f : N → Y be a function defined as f (x) = 4x + 3, where, Y = {y ∈ N : y = 4x + 3 for some x ∈ N }. Show that f is invertible. Find the inverse.

**Solution** Consider an arbitrary element y of Y. By the definition of Y, y = 4x + 3, for some x in the domain N. This shows that x = (y - 3) / 4. Define g : Y → N by g(y) = (y - 3) / 4.

 Now, gof(x) = g(f(x)) = g(4x + 3) = (4x + 3 - 3) / 4 = x and
 fog(y) = f(g(y)) = f((y - 3) / 4) = 4((y - 3) / 4) + 3 = y - 3 + 3 = y. This shows that gof = I<sub>N</sub>
 and fog = I<sub>Y</sub>, which implies that f is invertible and g is the inverse of f.

## Miscellaneous Examples

### Example 18
If R<sub>1</sub> and R<sub>2</sub> are equivalence relations in a set A, show that R<sub>1</sub> ∩ R<sub>2</sub> is also an equivalence relation.

**Solution** Since R<sub>1</sub> and R<sub>2</sub> are equivalence relations, (a, a) ∈ R<sub>1</sub>, and (a, a) ∈ R<sub>2</sub> ∀ a ∈ A. This implies that (a, a) ∈ R<sub>1</sub> ∩ R<sub>2</sub>, ∀ a, showing R<sub>1</sub> ∩ R<sub>2</sub> is reflexive. Further, (a, b) ∈ R<sub>1</sub> ∩ R<sub>2</sub> ⇒ (a, b) ∈ R<sub>1</sub> and (a, b) ∈ R<sub>2</sub> ⇒ (b, a) ∈ R<sub>1</sub> and (b, a) ∈ R<sub>2</sub> ⇒ (b, a) ∈ R<sub>1</sub> ∩ R<sub>2</sub>, hence, R<sub>1</sub> ∩ R<sub>2</sub> is symmetric. Similarly, (a, b) ∈ R<sub>1</sub> ∩ R<sub>2</sub> and (b, c) ∈ R<sub>1</sub> ∩ R<sub>2</sub> ⇒ (a, c) ∈ R<sub>1</sub> and (a, c) ∈ R<sub>2</sub> ⇒ (a, c) ∈ R<sub>1</sub> ∩ R<sub>2</sub>. This shows that R<sub>1</sub> ∩ R<sub>2</sub> is transitive. Thus, R<sub>1</sub> ∩ R<sub>2</sub> is an equivalence relation.

### Example 19
Let R be a relation on the set A of ordered pairs of positive integers defined by (x, y) R (u, v) if and only if xv = yu. Show that R is an equivalence relation.

**Solution** Clearly, (x, y) R (x, y), ∀ (x, y) ∈ A, since xy = yx. This shows that R is reflexive. Further, (x, y) R (u, v) ⇒ xv = yu ⇒ uy = vx and hence (u, v) R (x, y). This shows that R is symmetric. Similarly, (x, y) R (u, v) and (u, v) R (a, b) ⇒ xv = yu and ub = va ⇒ xva / u = yua / u ⇒ xvb = yua / u × v ⇒ xb = ya and hence (x, y) R (a, b). Thus, R is transitive. Thus, R is an equivalence relation.

### Example 20
Let X = {1, 2, 3, 4, 5, 6, 7, 8, 9}. Let R<sub>1</sub> be a relation in X given by R<sub>1</sub> = {(x, y) : x – y is divisible by 3} and R<sub>2</sub> be another relation on X given by R<sub>2</sub> = {(x, y): {x, y} ⊂ {1, 4, 7} or {x, y} ⊂ {2, 5, 8} or {x, y} ⊂ {3, 6, 9}}. Show that R<sub>1</sub> = R<sub>2</sub>.

**Solution** Note that the characteristic of sets {1, 4, 7}, {2, 5, 8} and {3, 6, 9} is that difference between any two elements of these sets is a multiple of 3. Therefore, (x, y) ∈ R<sub>1</sub> ⇒ x – y is a multiple of 3 ⇒ {x, y} ⊂ {1, 4, 7} or {x, y} ⊂ {2, 5, 8} or {x, y} ⊂ {3, 6, 9} ⇒ (x, y) ∈ R<sub>2</sub>. Hence, R<sub>1</sub> ⊂ R<sub>2</sub>. Similarly, {x, y} ∈ R<sub>2</sub> ⇒ {x, y}

Chapter 1
RELATIONS AND FUNCTIONS
14 MATHEMATICS

Page : 14

subset {1, 4, 7} or {x, y} subset {2, 5, 8} or {x, y} subset {3, 6, 9} => x - y is divisible by 3 => {x, y} in R<sub>1</sub>. This shows that R<sub>2</sub> subset R<sub>1</sub>. Hence, R<sub>1</sub> = R<sub>2</sub>.

### Example 21
Let f : X -> Y be a function. Define a relation R in X given by R = {(a, b): f(a) = f(b)}. Examine whether R is an equivalence relation or not.

**Solution** For every a in X, (a, a) in R, since f(a) = f(a), showing that R is reflexive. Similarly, (a, b) in R => f(a) = f(b) => f(b) = f(a) => (b, a) in R. Therefore, R is symmetric. Further, (a, b) in R and (b, c) in R => f(a) = f(b) and f(b) = f(c) => f(a) = f(c) => (a, c) in R, which implies that R is transitive. Hence, R is an equivalence relation.

### Example 22
Find the number of all one-one functions from set A = {1, 2, 3} to itself.

**Solution** One-one function from {1, 2, 3} to itself is simply a permutation on three symbols 1, 2, 3. Therefore, total number of one-one maps from {1, 2, 3} to itself is same as total number of permutations on three symbols 1, 2, 3 which is 3! = 6.

### Example 23
Let A = {1, 2, 3}. Then show that the number of relations containing (1, 2) and (2, 3) which are reflexive and transitive but not symmetric is three.

**Solution** The smallest relation R<sub>1</sub> containing (1, 2) and (2, 3) which is reflexive and transitive but not symmetric is {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}. Now, if we add the pair (2, 1) to R<sub>1</sub> to get R<sub>2</sub>, then the relation R<sub>2</sub> will be reflexive, transitive but not symmetric. Similarly, we can obtain R<sub>3</sub> by adding (3, 2) to R<sub>1</sub> to get the desired relation. However, we can not add two pairs (2, 1), (3, 2) or single pair (3, 1) to R<sub>1</sub> at a time, as by doing so, we will be forced to add the remaining pair in order to maintain transitivity and in the process, the relation will become symmetric also which is not required. Thus, the total number of desired relations is three.

### Example 24
Show that the number of equivalence relation in the set {1, 2, 3} containing (1, 2) and (2, 1) is two.

**Solution** The smallest equivalence relation R<sub>1</sub> containing (1, 2) and (2, 1) is {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}. Now we are left with only 4 pairs namely (2, 3), (3, 2), (1, 3) and (3, 1). If we add any one, say (2, 3) to R<sub>1</sub>, then for symmetry we must add (3, 2) also and now for transitivity we are forced to add (1, 3) and (3, 1). Thus, the only equivalence relation bigger than R<sub>1</sub> is the universal relation. This shows that the total number of equivalence relations containing (1, 2) and (2, 1) is two.

### Example 25
Consider the identity function I<sub>N</sub> : N -> N defined as I<sub>N</sub>(x) = x for all x in N. Show that although I<sub>N</sub> is onto but I<sub>N</sub> + I<sub>N</sub> : N -> N defined as (I<sub>N</sub> + I<sub>N</sub>)(x) = I<sub>N</sub>(x) + I<sub>N</sub>(x) = x + x = 2x is not onto.

Reprint 2025-26

RELATIONS AND FUNCTIONS 15

Page : 15

**Solution** Clearly I<sub>N</sub> is onto. But I<sub>N</sub> + I<sub>N</sub> is not onto, as we can find an element 3 in the co-domain N such that there does not exist any x in the domain N with (I<sub>N</sub> + I<sub>N</sub>) (x) = 2x = 3.

### Example 26
Consider a function f : [0, π/2] → R given by f(x) = sin x and g : [0, π/2] → R given by g(x) = cos x. Show that f and g are one-one, but f + g is not one-one.

**Solution** Since for any two distinct elements x<sub>1</sub> and x<sub>2</sub> in [0, π/2], sin x<sub>1</sub> ≠ sin x<sub>2</sub> and cos x<sub>1</sub> ≠ cos x<sub>2</sub>, both f and g must be one-one. But (f + g) (0) = sin 0 + cos 0 = 1 and (f + g) (π/2) = sin π/2 + cos π/2 = 1. Therefore, f + g is not one-one.



### Summary

In this chapter, we studied different types of relations and equivalence relation, composition of functions, invertible functions and binary operations. The main features of this chapter are as follows:

* Empty relation is the relation R in X given by R = φ ⊂ X × X.
* Universal relation is the relation R in X given by R = X × X.
* Reflexive relation R in X is a relation with (a, a) ∈ R ∀ a ∈ X.
* Symmetric relation R in X is a relation satisfying (a, b) ∈ R implies (b, a) ∈ R.
* Transitive relation R in X is a relation satisfying (a, b) ∈ R and (b, c) ∈ R implies that (a, c) ∈ R.
* Equivalence relation R in X is a relation which is reflexive, symmetric and transitive.
* Equivalence class [a] containing a ∈ X for an equivalence relation R in X is the subset of X containing all elements b related to a.
* A function f : X → Y is one-one (or injective) if f (x<sub>1</sub>) = f (x<sub>2</sub>) ⇒ x<sub>1</sub> = x<sub>2</sub> ∀ x<sub>1</sub>, x<sub>2</sub> ∈ X.
* A function f : X → Y is onto (or surjective) if given any y ∈ Y, ∃ x ∈ X such that f (x) = y.
* A function f : X → Y is one-one and onto (or bijective), if f is both one-one and onto.
* Given a finite set X, a function f : X → X is one-one (respectively onto) if and only if f is onto (respectively one-one). This is the characteristic property of a finite set. This is not true for infinite set.
