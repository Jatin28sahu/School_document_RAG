## 3.1 INTRODUCTION

In Chapter 1, all charges whether free or bound, were considered to be at rest. Charges in motion constitute an electric current. Such currents occur naturally in many situations. Lightning is one such phenomenon in which charges flow from the clouds to the earth through the atmosphere, sometimes with disastrous results. The flow of charges in lightning is not steady, but in our everyday life we see many devices where charges flow in a steady manner, like water flowing smoothly in a river. A torch and a cell-driven clock are examples of such devices. In the present chapter, we shall study some of the basic laws concerning steady electric currents.

## 3.2 ELECTRIC CURRENT

Imagine a small area held normal to the direction of flow of charges. Both the positive and the negative charges may flow forward and backward across the area. In a given time interval $t$, let $q_+$ be the net amount (*i.e.*, forward *minus* backward) of positive charge that flows in the forward direction across the area. Similarly, let $q_-$ be the net amount of negative charge flowing across the area in the forward direction. The net amount of charge flowing across the area in the forward direction in the time interval $t$, then, is $q = q_+ - q_-$. This is proportional to $t$ for steady current

Reprint 2025-26

Physics

Page : 82

and the quotient

I = q/t (3.1)

is defined to be the current across the area in the forward direction. (If it turn out to be a negative number, it implies a current in the backward direction.)

Currents are not always steady and hence more generally, we define the current as follows. Let ΔQ be the net charge flowing across a cross-section of a conductor during the time interval Δt [i.e., between times t and (t + Δt)]. Then, the current at time t across the cross-section of the conductor is defined as the value of the ratio of ΔQ to Δt in the limit of Δt tending to zero,

I(t) = lim ΔQ/Δt (3.2)
Δt→0

In SI units, the unit of current is ampere. An ampere is defined through magnetic effects of currents that we will study in the following chapter. An ampere is typically the order of magnitude of currents in domestic appliances. An average lightning carries currents of the order of tens of thousands of amperes and at the other extreme, currents in our nerves are in microamperes.

## 3.3 Electric Currents in Conductors

An electric charge will experience a force if an electric field is applied. If it is free to move, it will thus move contributing to a current. In nature, free charged particles do exist like in upper strata of atmosphere called the ionosphere. However, in atoms and molecules, the negatively charged electrons and the positively charged nuclei are bound to each other and are thus not free to move. Bulk matter is made up of many molecules, a gram of water, for example, contains approximately 10<sup>22</sup> molecules. These molecules are so closely packed that the electrons are no longer attached to individual nuclei. In some materials, the electrons will still be bound, i.e., they will not accelerate even if an electric field is applied. In other materials, notably metals, some of the electrons are practically free to move within the bulk material. These materials, generally called conductors, develop electric currents in them when an electric field is applied.

If we consider solid conductors, then of course the atoms are tightly bound to each other so that the current is carried by the negatively charged electrons. There are, however, other types of conductors like electrolytic solutions where positive and negative charges both can move. In our discussions, we will focus only on solid conductors so that the current is carried by the negatively charged electrons in the background of fixed positive ions.

Consider first the case when no electric field is present. The electrons will be moving due to thermal motion during which they collide with the fixed ions. An electron colliding with an ion emerges with the same speed as before the collision. However, the direction of its velocity after the collision is completely random. At a given time, there is no preferential direction for the velocities of the electrons. Thus on the average, the

Reprint 2025-26

Current Electricity

Page : 83

number of electrons travelling in any direction will be equal to the number of electrons travelling in the opposite direction. So, there will be no net electric current.

![Charges +Q and -Q put at the ends of a metallic cylinder. The electrons will drift because of the electric field created to neutralise the charges. The current thus will stop after a while unless the charges +Q and -Q are continuously replenished.](image)

Let us now see what happens to such a piece of conductor if an electric field is applied. To focus our thoughts, imagine the conductor in the shape of a cylinder of radius R (Fig. 3.1). Suppose we now take two thin circular discs of the same radius and put positive charge +Q distributed over one disc and similarly -Q at the other disc. We attach the two discs on the two flat surfaces of the cylinder. An electric field will be created and is directed from the positive towards the negative charge. The electrons will be accelerated due to this field towards +Q. They will thus move to neutralise the charges. The electrons, as long as they are moving, will constitute an electric current. Hence in the situation considered, there will be a current for a very short while and no current thereafter.

We can also imagine a mechanism where the ends of the cylinder are supplied with fresh charges to make up for any charges neutralised by electrons moving inside the conductor. In that case, there will be a steady electric field in the body of the conductor. This will result in a continuous current rather than a current for a short period of time. Mechanisms, which maintain a steady electric field are cells or batteries that we shall study later in this chapter. In the next sections, we shall study the steady current that results from a steady electric field in conductors.

## 3.4 OHM’S LAW

A basic law regarding flow of currents was discovered by G.S. Ohm in 1828, long before the physical mechanism responsible for flow of currents was discovered. Imagine a conductor through which a current I is flowing and let V be the potential difference between the ends of the conductor. Then Ohm’s law states that

V $\propto$ I
or, V = R I (3.3)

where the constant of proportionality R is called the resistance of the conductor. The SI units of resistance is ohm, and is denoted by the symbol $\Omega$. The resistance R not only depends on the material of the conductor but also on the dimensions of the conductor. The dependence of R on the dimensions of the conductor can easily be determined as follows.

![Illustrating the relation R = $\rho$l/A for a rectangular slab of length l and area of cross-section A. (a) A single slab of length l and area A. (b) Two identical slabs placed side by side to make a conductor of length 2l. (c) A slab of length l and area A cut into two half-slabs of area A/2.](image)

Consider a conductor satisfying Eq. (3.3) to be in the form of a slab of length l and cross sectional area A [Fig. 3.2(a)]. Imagine placing two such identical slabs side by side [Fig. 3.2(b)], so that the length of the combination is 2l. The current flowing through the combination is the same as that flowing through either of the slabs. If V is the potential difference across the ends of the first slab, then V is also the potential difference across the ends of the second slab since the second slab is

Reprint 2025-26

Physics

Page : 84

identical to the first and the same current I flows through both. The potential difference across the ends of the combination is clearly sum of the potential difference across the two individual slabs and hence equals 2V. The current through the combination is I and the resistance of the combination R<sub>C</sub> is [from Eq. (3.3)],

R<sub>C</sub> = 2V / I = 2R (3.4)

since V/I = R, the resistance of either of the slabs. Thus, doubling the length of a conductor doubles the resistance. In general, then resistance is proportional to length,

R ∝ l (3.5)

Next, imagine dividing the slab into two by cutting it lengthwise so that the slab can be considered as a combination of two identical slabs of length l, but each having a cross sectional area of A/2 [Fig. 3.2(c)]. For a given voltage V across the slab, if I is the current through the entire slab, then clearly the current flowing through each of the two half-slabs is I/2. Since the potential difference across the ends of the half-slabs is V, i.e., the same as across the full slab, the resistance of each of the half-slabs R<sub>1</sub> is

R<sub>1</sub> = V / (I/2) = 2V / I = 2R. (3.6)

Thus, halving the area of the cross-section of a conductor doubles the resistance. In general, then the resistance R is inversely proportional to the cross-sectional area,

R ∝ 1/A (3.7)

Combining Eqs. (3.5) and (3.7), we have

R ∝ l/A (3.8)

and hence for a given conductor

R = ρ l/A (3.9)

where the constant of proportionality ρ depends on the material of the conductor but not on its dimensions. ρ is called resistivity.

Using the last equation, Ohm’s law reads

V = I × R = I ρ l / A (3.10)

Current per unit area (taken normal to the current), I/A, is called current density and is denoted by j. The SI units of the current density are A/m<sup>2</sup>. Further, if E is the magnitude of uniform electric field in the conductor whose length is l, then the potential difference V across its ends is El. Using these, the last equation reads

![Portrait of Georg Simon Ohm](image)
> **Georg Simon Ohm (1787–1854)** German physicist, professor at Munich. Ohm was led to his law by an analogy between the conduction of heat: the electric field is analogous to the temperature gradient, and the electric current is analogous to the heat flow.

Reprint 2025-26

Current Electricity

Page : 85

E l = j r l
or, E = j r (3.11)

The above relation for magnitudes E and j can indeed be cast in a vector form. The current density, (which we have defined as the current through unit area normal to the current) is also directed along E, and is also a vector j (j = j E/E). Thus, the last equation can be written as,

E = j r (3.12)
or, j = s E (3.13)

where s = 1/r is called the conductivity. Ohm’s law is often stated in an equivalent form, Eq. (3.13) in addition to Eq.(3.3). In the next section, we will try to understand the origin of the Ohm’s law as arising from the characteristics of the drift of electrons.

## 3.5 DRIFT OF ELECTRONS AND THE ORIGIN OF RESISTIVITY

As remarked before, an electron will suffer collisions with the heavy fixed ions, but after collision, it will emerge with the same speed but in random directions. If we consider all the electrons, their average velocity will be zero since their directions are random. Thus, if there are N electrons and the velocity of the i<sup>th</sup> electron (i = 1, 2, 3, ... N) at a given time is v<sub>i</sub>, then

1/N Σ<sub>i=1</sub><sup>N</sup> v<sub>i</sub> = 0 (3.14)

Consider now the situation when an electric field is present. Electrons will be accelerated due to this field by

a = -e E / m (3.15)

where -e is the charge and m is the mass of an electron. Consider again the i<sup>th</sup> electron at a given time t. This electron would have had its last collision some time before t, and let t<sub>i</sub> be the time elapsed after its last collision. If v<sub>i</sub> was its velocity immediately after the last collision, then its velocity V<sub>i</sub> at time t is

V<sub>i</sub> = v<sub>i</sub> + (-eE / m) t<sub>i</sub> (3.16)

since starting with its last collision it was accelerated (Fig. 3.3) with an acceleration given by Eq. (3.15) for a time interval t<sub>i</sub>. The average velocity of the electrons at time t is the average of all the V<sub>i</sub>’s. The average of v<sub>i</sub>’s is zero [Eq. (3.14)] since immediately after any collision, the direction of the velocity of an electron is completely random. The collisions of the electrons do not occur at regular intervals but at random times. Let us denote by t, the average time between successive collisions. Then at a given time, some of the electrons would have spent

![A schematic picture of an electron moving from a point A to another point B through repeated collisions, and straight line travel between collisions (full lines). If an electric field is applied as shown, the electron ends up at point B' (dotted lines). A slight drift in a direction opposite the electric field is visible.](image)

**FIGURE 3.3** A schematic picture of an electron moving from a point A to another point B through repeated collisions, and straight line travel between collisions (full lines). If an electric field is applied as shown, the electron ends up at point B' (dotted lines). A slight drift in a direction opposite the electric field is visible.

Reprint 2025-26

Physics

Page : 86

time more than t and some less than t. In other words, the time t<sub>i</sub> in Eq. (3.16) will be less than t for some and more than t for others as we go through the values of i = 1, 2 ..... N. The average value of t<sub>i</sub> then is τ (known as relaxation time). Thus, averaging Eq. (3.16) over the N-electrons at any given time t gives us for the average velocity v<sub>d</sub>

v<sub>d</sub> ≡ ( v<sub>i</sub> ) average = ( v<sub>i</sub> ) average - (eE/m) ( t<sub>i</sub> ) average

= 0 - (eE/m) τ = - (eE/m) τ (3.17)

This last result is surprising. It tells us that the electrons move with an average velocity which is independent of time, although electrons are accelerated. This is the phenomenon of drift and the velocity v<sub>d</sub> in Eq. (3.17) is called the drift velocity. Because of the drift, there will be net transport of charges across any area perpendicular to E. Consider a planar area A, located inside the conductor such that the normal to the area is parallel to E (Fig. 3.4). Then because of the drift, in an infinitesimal amount of time Δt, all electrons to the left of the area at distances upto |v<sub>d</sub>|Δt would have crossed the area. If n is the number of free electrons per unit volume in the metal, then there are n Δt |v<sub>d</sub>|A such electrons. Since each electron carries a charge -e, the total charge transported across this area A to the right in time Δt is -ne A|v<sub>d</sub>|Δt. E is directed towards the left and hence the total charge transported along E across the area is negative of this. The amount of charge crossing the area A in time Δt is by definition [Eq. (3.2)] I Δt, where I is the magnitude of the current. Hence,

![Current in a metallic conductor. The magnitude of current density in a metal is the magnitude of charge contained in a cylinder of unit area and length v<sub>d</sub>.](image)

I Δt = + n e A |v<sub>d</sub>| Δt (3.18)

Substituting the value of |v<sub>d</sub>| from Eq. (3.17)

I Δt = (e^2 A τ n Δt E) / m (3.19)

By definition I is related to the magnitude |j| of the current density by

I = |j|A (3.20)

Hence, from Eqs.(3.19) and (3.20),

j = (n e^2 τ E) / m (3.21)

The vector j is parallel to E and hence we can write Eq. (3.21) in the vector form

j = (n e^2 τ / m) E (3.22)

Comparison with Eq. (3.13) shows that Eq. (3.22) is exactly the Ohm's law, if we identify the conductivity σ as

Reprint 2025-26

Current Electricity

Page : 87

sigma = ne^2 tau / m (3.23)

We thus see that a very simple picture of electrical conduction reproduces Ohm's law. We have, of course, made assumptions that tau and n are constants, independent of E. We shall, in the next section, discuss the limitations of Ohm's law.

### Example 3.1
(a) Estimate the average drift speed of conduction electrons in a copper wire of cross-sectional area 1.0 x 10^-7 m^2 carrying a current of 1.5 A. Assume that each copper atom contributes roughly one conduction electron. The density of copper is 9.0 x 10^3 kg/m^3, and its atomic mass is 63.5 u. (b) Compare the drift speed obtained above with, (i) thermal speeds of copper atoms at ordinary temperatures, (ii) speed of propagation of electric field along the conductor which causes the drift motion.

**Solution**
(a) The direction of drift velocity of conduction electrons is opposite to the electric field direction, i.e., electrons drift in the direction of increasing potential. The drift speed v_d is given by Eq. (3.18)
v_d = (I/neA)
Now, e = 1.6 x 10^-19 C, A = 1.0 x 10^-7 m^2, I = 1.5 A. The density of conduction electrons, n is equal to the number of atoms per cubic metre (assuming one conduction electron per Cu atom as is reasonable from its valence electron count of one). A cubic metre of copper has a mass of 9.0 x 10^3 kg. Since 6.0 x 10^23 copper atoms have a mass of 63.5 g,
n = (6.0 x 10^23 x 9.0 x 10^6) / 63.5
= 8.5 x 10^28 m^-3
which gives,
v_d = 1.5 / (8.5 x 10^28 x 1.6 x 10^-19 x 1.0 x 10^-7)
= 1.1 x 10^-3 m s^-1 = 1.1 mm s^-1

(b) (i) At a temperature T, the thermal speed * of a copper atom of mass M is obtained from [<(1/2) Mv^2> = (3/2) k_B T] and is thus typically of the order of sqrt(k_B T / M), where k_B is the Boltzmann constant. For copper at 300 K, this is about 2 x 10^2 m/s. This figure indicates the random vibrational speeds of copper atoms in a conductor. Note that the drift speed of electrons is much smaller, about 10^-5 times the typical thermal speed at ordinary temperatures.
(ii) An electric field travelling along the conductor has a speed of an electromagnetic wave, namely equal to 3.0 x 10^8 m s^-1 (You will learn about this in Chapter 8). The drift speed is, in comparison, extremely small; smaller by a factor of 10^-11.

* See Eq. (12.23) of Chapter 12 from Class XI book.
Reprint 2025-26

Physics

Page : 88

### Example 3.2
**Solution**
(a) In Example 3.1, the electron drift speed is estimated to be only a few mm s^-1 for currents in the range of a few amperes? How then is current established almost the instant a circuit is closed?
(b) The electron drift arises due to the force experienced by electrons in the electric field inside the conductor. But force should cause acceleration. Why then do the electrons acquire a steady average drift speed?
(c) If the electron drift speed is so small, and the electron’s charge is small, how can we still obtain large amounts of current in a conductor?
(d) When electrons drift in a metal from lower to higher potential, does it mean that all the ‘free’ electrons of the metal are moving in the same direction?
(e) Are the paths of electrons straight lines between successive collisions (with the positive ions of the metal) in the (i) absence of electric field, (ii) presence of electric field?

**Solution**
(a) Electric field is established throughout the circuit, almost instantly (with the speed of light) causing at every point a local electron drift. Establishment of a current does not have to wait for electrons from one end of the conductor travelling to the other end. However, it does take a little while for the current to reach its steady value.
(b) Each ‘free’ electron does accelerate, increasing its drift speed until it collides with a positive ion of the metal. It loses its drift speed after collision but starts to accelerate and increases its drift speed again only to suffer a collision again and so on. On the average, therefore, electrons acquire only a drift speed.
(c) Simple, because the electron number density is enormous, ~10^29 m^-3.
(d) By no means. The drift velocity is superposed over the large random velocities of electrons.
(e) In the absence of electric field, the paths are straight lines; in the presence of electric field, the paths are, in general, curved.

### 3.5.1 Mobility
As we have seen, conductivity arises from mobile charge carriers. In metals, these mobile charge carriers are electrons; in an ionised gas, they are electrons and positive charged ions; in an electrolyte, these can be both positive and negative ions.
An important quantity is the mobility µ defined as the magnitude of the drift velocity per unit electric field:

µ = |v_d| / E (3.24)

The SI unit of mobility is m^2/Vs and is 10^4 of the mobility in practical units (cm^2/Vs). Mobility is positive. From Eq. (3.17), we have

v_d = eτE / m

Reprint 2025-26

Current Electricity

Page : 89

Hence,
$$\mu = \frac{v_d}{E} = \frac{e\tau}{m}$$ (3.25)
where $\tau$ is the average collision time for electrons.

## 3.6 LIMITATIONS OF OHM’S LAW
Although Ohm’s law has been found valid over a large class of materials, there do exist materials and devices used in electric circuits where the proportionality of $V$ and $I$ does not hold. The deviations broadly are one or more of the following types:

(a) $V$ ceases to be proportional to $I$ (Fig. 3.5).


|IMAGE|FIGURE 3.5 The dashed line represents the linear Ohm’s law. The solid line is the voltage V versus current I for a good conductor.|
|-|-|


(b) The relation between $V$ and $I$ depends on the sign of $V$. In other words, if $I$ is the current for a certain $V$, then reversing the direction of $V$ keeping its magnitude fixed, does not produce a current of the same magnitude as $I$ in the opposite direction (Fig. 3.6). This happens, for example, in a diode which we will study in Chapter 14.


|![Characteristic curve of a diode showing current I vs voltage V. The positive V quadrant shows an exponential-like increase in mA, while the negative V quadrant shows a very small leakage current in microamperes.](image)|![Graph of current I versus voltage V for GaAs. The curve rises, dips (negative resistance region), and then rises again.](image)|
|-|-|
|FIGURE 3.6 Characteristic curve of a diode. Note the different scales for negative and positive values of the voltage and current.|FIGURE 3.7 Variation of current versus voltage for GaAs.|


(c) The relation between $V$ and $I$ is not unique, i.e., there is more than one value of $V$ for the same current $I$ (Fig. 3.7). A material exhibiting such behaviour is GaAs.

Materials and devices not obeying Ohm’s law in the form of Eq. (3.3) are actually widely used in electronic circuits. In this and a few subsequent chapters, however, we will study the electrical currents in materials that obey Ohm’s law.

## 3.7 RESISTIVITY OF VARIOUS MATERIALS
The materials are classified as conductors, semiconductors and insulators depending on their resistivities, in an increasing order of their values.

Reprint 2025-26

Physics

Page : 90

Metals have low resistivities in the range of 10^-8 Wm to 10^-6 Wm. At the other end are insulators like ceramic, rubber and plastics having resistivities 10^18 times greater than metals or more. In between the two are the semiconductors. These, however, have resistivities characteristically decreasing with a rise in temperature. The resistivities of semiconductors can be decreased by adding small amount of suitable impurities. This last feature is exploited in use of semiconductors for electronic devices.

## 3.8 TEMPERATURE DEPENDENCE OF RESISTIVITY

The resistivity of a material is found to be dependent on the temperature. Different materials do not exhibit the same dependence on temperatures. Over a limited range of temperatures, that is not too large, the resistivity of a metallic conductor is approximately given by,

rT = r0 [1 + a (T–T0)] (3.26)

where rT is the resistivity at a temperature T and r0 is the same at a reference temperature T0. a is called the temperature co-efficient of resistivity, and from Eq. (3.26), the dimension of a is (Temperature)^-1. For metals, a is positive.

The relation of Eq. (3.26) implies that a graph of rT plotted against T would be a straight line. At temperatures much lower than 0°C, the graph, however, deviates considerably from a straight line (Fig. 3.8). Equation (3.26) thus, can be used approximately over a limited range of T around any reference temperature T0, where the graph can be approximated as a straight line.


|T (K)|r (10^-8 ohm m)|
|-|-|
|0|0|
|50|0.1|
|100|0.4|
|150|1.1|

![Resistivity rT of copper as a function of temperature T.](image)
**FIGURE 3.8** Resistivity rT of copper as a function of temperature T.


|T (K)|r (10^-6 ohm m)|
|-|-|
|0|1.00|
|200|1.04|
|400|1.08|
|600|1.12|
|800|1.16|

![Resistivity rT of nichrome as a function of absolute temperature T.](image)
**FIGURE 3.9** Resistivity rT of nichrome as a function of absolute temperature T.


|T (K)|r (ohm m)|
|-|-|
|0|10^4|
|200|10^2|
|400|10^0|
|600|10^-2|

![Temperature dependence of resistivity for a typical semiconductor.](image)
**FIGURE 3.10** Temperature dependence of resistivity for a typical semiconductor.

Some materials like Nichrome (which is an alloy of nickel, iron and chromium) exhibit a very weak dependence of resistivity with temperature (Fig. 3.9). Manganin and constantan have similar properties. These materials are thus widely used in wire bound standard resistors since their resistance values would change very little with temperatures.

Reprint 2025-26

Current Electricity

Page : 91

Unlike metals, the resistivities of semiconductors decrease with increasing temperatures. A typical dependence is shown in Fig. 3.10.

We can qualitatively understand the temperature dependence of resistivity, in the light of our derivation of Eq. (3.23). From this equation, resistivity of a material is given by

rho = 1 / sigma = m / (n e^2 tau) (3.27)

rho thus depends inversely both on the number n of free electrons per unit volume and on the average time tau between collisions. As we increase temperature, average speed of the electrons, which act as the carriers of current, increases resulting in more frequent collisions. The average time of collisions tau, thus decreases with temperature.

In a metal, n is not dependent on temperature to any appreciable extent and thus the decrease in the value of tau with rise in temperature causes rho to increase as we have observed.

For insulators and semiconductors, however, n increases with temperature. This increase more than compensates any decrease in tau so that for such materials, rho decreases with temperature.

### Example 3.3
An electric toaster uses nichrome for its heating element. When a negligibly small current passes through it, its resistance at room temperature (27.0 °C) is found to be 75.3 Omega. When the toaster is connected to a 230 V supply, the current settles, after a few seconds, to a steady value of 2.68 A. What is the steady temperature of the nichrome element? The temperature coefficient of resistance of nichrome averaged over the temperature range involved, is 1.70 x 10^-4 °C^-1.

**Solution** When the current through the element is very small, heating effects can be ignored and the temperature T_1 of the element is the same as room temperature. When the toaster is connected to the supply, its initial current will be slightly higher than its steady value of 2.68 A. But due to heating effect of the current, the temperature will rise. This will cause an increase in resistance and a slight decrease in current. In a few seconds, a steady state will be reached when temperature will rise no further, and both the resistance of the element and the current drawn will achieve steady values. The resistance R_2 at the steady temperature T_2 is

R_2 = 230 V / 2.68 A = 85.8 Omega

Using the relation
R_2 = R_1 [1 + alpha (T_2 - T_1)]
with alpha = 1.70 x 10^-4 °C^-1, we get

T_2 - T_1 = (85.8 - 75.3) / (75.3) x 1.70 x 10^-4 = 820 °C

that is, T_2 = (820 + 27.0) °C = 847 °C

Thus, the steady temperature of the heating element (when heating effect due to the current equals heat loss to the surroundings) is 847 °C.

Reprint 2025-26

Physics

Page : 92

### Example 3.4
The resistance of the platinum wire of a platinum resistance thermometer at the ice point is 5 Ω and at steam point is 5.23 Ω. When the thermometer is inserted in a hot bath, the resistance of the platinum wire is 5.795 Ω. Calculate the temperature of the bath.

**Solution** R<sub>0</sub> = 5 Ω, R<sub>100</sub> = 5.23 Ω and R<sub>t</sub> = 5.795 Ω

Now, t = (R<sub>t</sub> - R<sub>0</sub>) / (R<sub>100</sub> - R<sub>0</sub>) × 100, R<sub>t</sub> = R<sub>0</sub> (1 + αt)

= (5.795 - 5) / (5.23 - 5) × 100

= (0.795 / 0.23) × 100 = 345.65 °C

## 3.9 ELECTRICAL ENERGY, POWER

Consider a conductor with end points A and B, in which a current I is flowing from A to B. The electric potential at A and B are denoted by V(A) and V(B) respectively. Since current is flowing from A to B, V(A) > V(B) and the potential difference across AB is
V = V(A) – V(B) > 0.

In a time interval Δt, an amount of charge ΔQ = I Δt travels from A to B. The potential energy of the charge at A, by definition, was Q V(A) and similarly at B, it is Q V(B). Thus, change in its potential energy ΔU<sub>pot</sub> is
ΔU<sub>pot</sub> = Final potential energy – Initial potential energy
= ΔQ[(V(B) – V(A)] = –ΔQ V
= –I VΔt < 0 (3.28)

If charges moved without collisions through the conductor, their kinetic energy would also change so that the total energy is unchanged. Conservation of total energy would then imply that,
ΔK = –ΔU<sub>pot</sub> (3.29)
that is,
ΔK = I VΔt > 0 (3.30)

Thus, in case charges were moving freely through the conductor under the action of electric field, their kinetic energy would increase as they move. We have, however, seen earlier that on the average, charge carriers do not move with acceleration but with a steady drift velocity. This is because of the collisions with ions and atoms during transit. During collisions, the energy gained by the charges thus is shared with the atoms. The atoms vibrate more vigorously, i.e., the conductor heats up. Thus, in an actual conductor, an amount of energy dissipated as heat in the conductor during the time interval Δt is,
ΔW = I VΔt (3.31)

The energy dissipated per unit time is the power dissipated
P = ΔW/Δt and we have,
P = I V (3.32)

Reprint 2025-26

Current Electricity

Page : 93

Using Ohm’s law V = IR, we get
P = I^2 R = V^2/R (3.33)
as the power loss (“ohmic loss”) in a conductor of resistance R carrying a current I. It is this power which heats up, for example, the coil of an electric bulb to incandescence, radiating out heat and light.

Where does the power come from? As we have reasoned before, we need an external source to keep a steady current through the conductor. It is clearly this source which must supply this power. In the simple circuit shown with a cell (Fig.3.11), it is the chemical energy of the cell which supplies this power for as long as it can.

The expressions for power, Eqs. (3.32) and (3.33), show the dependence of the power dissipated in a resistor R on the current through it and the voltage across it.

![Heat is produced in the resistor R which is connected across the terminals of a cell. The energy dissipated in the resistor R comes from the chemical energy of the electrolyte.](image)
**FIGURE 3.11** Heat is produced in the resistor R which is connected across the terminals of a cell. The energy dissipated in the resistor R comes from the chemical energy of the electrolyte.

Equation (3.33) has an important application to power transmission. Electrical power is transmitted from power stations to homes and factories, which may be hundreds of miles away, via transmission cables. One obviously wants to minimise the power loss in the transmission cables connecting the power stations to homes and factories. We shall see now how this can be achieved. Consider a device R, to which a power P is to be delivered via transmission cables having a resistance R<sub>c</sub> to be dissipated by it finally. If V is the voltage across R and I the current through it, then
P = V I (3.34)

The connecting wires from the power station to the device has a finite resistance R<sub>c</sub>. The power dissipated in the connecting wires, which is wasted is P<sub>c</sub> with
P<sub>c</sub> = I^2 R<sub>c</sub>
= P^2 R<sub>c</sub> / V^2 (3.35)
from Eq. (3.32). Thus, to drive a device of power P, the power wasted in the connecting wires is inversely proportional to V^2. The transmission cables from power stations are hundreds of miles long and their resistance R<sub>c</sub> is considerable. To reduce P<sub>c</sub>, these wires carry current at enormous values of V and this is the reason for the high voltage danger signs on transmission lines — a common sight as we move away from populated areas. Using electricity at such voltages is not safe and hence at the other end, a device called a transformer lowers the voltage to a value suitable for use.

## 3.10 CELLS, EMF, INTERNAL RESISTANCE

We have already mentioned that a simple device to maintain a steady current in an electric circuit is the electrolytic cell. Basically a cell has two electrodes, called the positive (P) and the negative (N), as shown in

Reprint 2025-26

Physics

Page : 94

![Sketch of an electrolyte cell with positive terminal P and negative terminal N. The gap between the electrodes is exaggerated for clarity. A and B are points in the electrolyte typically close to P and N. (b) the symbol for a cell, + referring to P and - referring to the N electrode. Electrical connections to the cell are made at P and N.](image)

Fig. 3.12. They are immersed in an electrolytic solution. Dipped in the solution, the electrodes exchange charges with the electrolyte. The positive electrode has a potential difference V<sub>+</sub> (V<sub>+</sub> > 0) between itself and the electrolyte solution immediately adjacent to it marked A in the figure. Similarly, the negative electrode develops a negative potential – (V<sub>–</sub>) (V<sub>–</sub> ≥ 0) relative to the electrolyte adjacent to it, marked as B in the figure. When there is no current, the electrolyte has the same potential throughout, so that the potential difference between P and N is V<sub>+</sub> – (–V<sub>–</sub>) = V<sub>+</sub> + V<sub>–</sub>. This difference is called the electromotive force (emf) of the cell and is denoted by ε. Thus

ε = V<sub>+</sub> + V<sub>–</sub> > 0 (3.36)

Note that ε is, actually, a potential difference and not a force. The name emf, however, is used because of historical reasons, and was given at a time when the phenomenon was not understood properly.

To understand the significance of ε, consider a resistor R connected across the cell (Fig. 3.12). A current I flows across R from C to D. As explained before, a steady current is maintained because current flows from N to P through the electrolyte. Clearly, across the electrolyte the same current flows through the electrolyte but from N to P, whereas through R, it flows from P to N.

The electrolyte through which a current flows has a finite resistance r, called the internal resistance. Consider first the situation when R is infinite so that I = V/R = 0, where V is the potential difference between P and N. Now,

V = Potential difference between P and A
+ Potential difference between A and B
+ Potential difference between B and N
= ε (3.37)

Thus, emf ε is the potential difference between the positive and negative electrodes in an open circuit, i.e., when no current is flowing through the cell.

If however R is finite, I is not zero. In that case the potential difference between P and N is

V = V<sub>+</sub> + V<sub>–</sub> – I r
= ε – I r (3.38)

Note the negative sign in the expression I (r) for the potential difference between A and B. This is because the current I flows from B to A in the electrolyte.

In practical calculations, internal resistances of cells in the circuit may be neglected when the current I is such that ε >> I r. The actual values of the internal resistances of cells vary from cell to cell. The internal resistance of dry cells, however, is much higher than the common electrolytic cells.

We also observe that since V is the potential difference across R, we have from Ohm’s law

V = I R (3.39)

Combining Eqs. (3.38) and (3.39), we get

Reprint 2025-26

Current Electricity

Page : 95

I R = ε - I r

Or, I = ε / (R + r) (3.40)

The maximum current that can be drawn from a cell is for R = 0 and it is I<sub>max</sub> = ε/r. However, in most cells the maximum allowed current is much lower than this to prevent permanent damage to the cell.

## 3.11 Cells in Series and in Parallel

Like resistors, cells can be combined together in an electric circuit. And like resistors, one can, for calculating currents and voltages in a circuit, replace a combination of cells by an equivalent cell.

![Two cells of emf's ε₁ and ε₂ in series. r₁, r₂ are their internal resistances. For connections across A and C, the combination can be considered as one cell of emf ε<sub>eq</sub> and an internal resistance r<sub>eq</sub>.](image)

**FIGURE 3.13**

Consider first two cells in series (Fig. 3.13), where one terminal of the two cells is joined together leaving the other terminal in either cell free. ε₁, ε₂ are the emf's of the two cells and r₁, r₂ their internal resistances, respectively.

Let V(A), V(B), V(C) be the potentials at points A, B and C shown in Fig. 3.13. Then V(A) - V(B) is the potential difference between the positive and negative terminals of the first cell. We have already calculated it in Eq. (3.38) and hence,

V<sub>AB</sub> ≡ V(A) - V(B) = ε₁ - I r₁ (3.41)

Similarly,

V<sub>BC</sub> ≡ V(B) - V(C) = ε₂ - I r₂ (3.42)

Hence, the potential difference between the terminals A and C of the combination is

V<sub>AC</sub> ≡ V(A) - V(C) = [V(A) - V(B)] + [V(B) - V(C)]
= (ε₁ + ε₂) - I (r₁ + r₂) (3.43)

If we wish to replace the combination by a single cell between A and C of emf ε<sub>eq</sub> and internal resistance r<sub>eq</sub>, we would have

V<sub>AC</sub> = ε<sub>eq</sub> - I r<sub>eq</sub> (3.44)

Comparing the last two equations, we get

ε<sub>eq</sub> = ε₁ + ε₂ (3.45)

and r<sub>eq</sub> = r₁ + r₂ (3.46)

In Fig. 3.13, we had connected the negative electrode of the first to the positive electrode of the second. If instead we connect the two negatives,

Reprint 2025-26

Physics

Page : 96

Eq. (3.42) would change to V<sub>BC</sub> = -e<sub>2</sub> - Ir<sub>2</sub> and we will get
e<sub>eq</sub> = e<sub>1</sub> - e<sub>2</sub> (3.47)

The rule for series combination clearly can be extended to any number of cells:
(i) The equivalent emf of a series combination of n cells is just the sum of their individual emf's, and
(ii) The equivalent internal resistance of a series combination of n cells is just the sum of their internal resistances.

This is so, when the current leaves each cell from the positive electrode. If in the combination, the current leaves any cell from the negative electrode, the emf of the cell enters the expression for e<sub>eq</sub> with a negative sign, as in Eq. (3.47).

Next, consider a parallel combination of the cells (Fig. 3.14). I<sub>1</sub> and I<sub>2</sub> are the currents leaving the positive electrodes of the cells. At the point B<sub>1</sub>, I<sub>1</sub> and I<sub>2</sub> flow in whereas the current I flows out. Since as much charge flows in as out, we have
I = I<sub>1</sub> + I<sub>2</sub> (3.48)

![Two cells in parallel. For connections across A and C, the combination can be replaced by one cell of emf e<sub>eq</sub> and internal resistances r<sub>eq</sub> whose values are given in Eqs. (3.54) and (3.55).](image)

Let V(B<sub>1</sub>) and V(B<sub>2</sub>) be the potentials at B<sub>1</sub> and B<sub>2</sub>, respectively. Then, considering the first cell, the potential difference across its terminals is V(B<sub>1</sub>) - V(B<sub>2</sub>). Hence, from Eq. (3.38)
V = V(B<sub>1</sub>) - V(B<sub>2</sub>) = e<sub>1</sub> - I<sub>1</sub>r<sub>1</sub> (3.49)

Points B<sub>1</sub> and B<sub>2</sub> are connected exactly similarly to the second cell. Hence considering the second cell, we also have
V = V(B<sub>1</sub>) - V(B<sub>2</sub>) = e<sub>2</sub> - I<sub>2</sub>r<sub>2</sub> (3.50)

Combining the last three equations
I = I<sub>1</sub> + I<sub>2</sub>
= (e<sub>1</sub> - V)/r<sub>1</sub> + (e<sub>2</sub> - V)/r<sub>2</sub> = (e<sub>1</sub>/r<sub>1</sub> + e<sub>2</sub>/r<sub>2</sub>) - V(1/r<sub>1</sub> + 1/r<sub>2</sub>) (3.51)

Hence, V is given by,
V = (e<sub>1</sub>r<sub>2</sub> + e<sub>2</sub>r<sub>1</sub>)/(r<sub>1</sub> + r<sub>2</sub>) - I(r<sub>1</sub>r<sub>2</sub>)/(r<sub>1</sub> + r<sub>2</sub>) (3.52)

If we want to replace the combination by a single cell, between B<sub>1</sub> and B<sub>2</sub>, of emf e<sub>eq</sub> and internal resistance r<sub>eq</sub>, we would have
V = e<sub>eq</sub> - Ir<sub>eq</sub> (3.53)

The last two equations should be the same and hence
e<sub>eq</sub> = (e<sub>1</sub>r<sub>2</sub> + e<sub>2</sub>r<sub>1</sub>)/(r<sub>1</sub> + r<sub>2</sub>) (3.54)
r<sub>eq</sub> = r<sub>1</sub>r<sub>2</sub>/(r<sub>1</sub> + r<sub>2</sub>) (3.55)

We can put these equations in a simpler way,

Reprint 2025-26

Current Electricity

Page : 97

1/r<sub>eq</sub> = 1/r<sub>1</sub> + 1/r<sub>2</sub> (3.56)

ε<sub>eq</sub>/r<sub>eq</sub> = ε<sub>1</sub>/r<sub>1</sub> + ε<sub>2</sub>/r<sub>2</sub> (3.57)

In Fig. (3.14), we had joined the positive terminals together and similarly the two negative ones, so that the currents I<sub>1</sub>, I<sub>2</sub> flow out of positive terminals. If the negative terminal of the second is connected to positive terminal of the first, Eqs. (3.56) and (3.57) would still be valid with ε<sub>2</sub> → –ε<sub>2</sub>.

Equations (3.56) and (3.57) can be extended easily. If there are n cells of emf ε<sub>1</sub>, ... ε<sub>n</sub> and of internal resistances r<sub>1</sub>, ... r<sub>n</sub> respectively, connected in parallel, the combination is equivalent to a single cell of emf ε<sub>eq</sub> and internal resistance r<sub>eq</sub>, such that

1/r<sub>eq</sub> = 1/r<sub>1</sub> + ... + 1/r<sub>n</sub> (3.58)

ε<sub>eq</sub>/r<sub>eq</sub> = ε<sub>1</sub>/r<sub>1</sub> + ... + ε<sub>n</sub>/r<sub>n</sub> (3.59)

<description>
A portrait of Gustav Robert Kirchhoff.
</description>

> **Gustav Robert Kirchhoff (1824 – 1887)** German physicist, professor at Heidelberg and at Berlin. Mainly known for his development of spectroscopy, he also made many important contributions to mathematical physics, among them, his first and second rules for circuits.

## 3.12 KIRCHHOFF’S RULES

Electric circuits generally consist of a number of resistors and cells interconnected sometimes in a complicated way. The formulae we have derived earlier for series and parallel combinations of resistors are not always sufficient to determine all the currents and potential differences in the circuit. Two rules, called Kirchhoff’s rules, are very useful for analysis of electric circuits.

Given a circuit, we start by labelling currents in each resistor by a symbol, say I, and a directed arrow to indicate that a current I flows along the resistor in the direction indicated. If ultimately I is determined to be positive, the actual current in the resistor is in the direction of the arrow. If I turns out to be negative, the current actually flows in a direction opposite to the arrow. Similarly, for each source (i.e., cell or some other source of electrical power) the positive and negative electrodes are labelled, as well as, a directed arrow with a symbol for the current flowing through the cell. This will tell us the potential difference,

V = V(P) – V(N) = ε – I r

[Eq. (3.38) between the positive terminal P and the negative terminal N; I here is the current flowing from N to P through the cell]. If, while labelling the current I through the cell one goes from P to N, then of course

V = ε + I r (3.60)

Having clarified labelling, we now state the rules and the proof:

(a) **Junction rule:** At any junction, the sum of the currents entering the junction is equal to the sum of currents leaving the junction (Fig. 3.15).

Reprint 2025-26
GUSTAV ROBERT KIRCHHOFF (1824 – 1887)

Physics

Page : 98

This applies equally well if instead of a junction of several lines, we consider a point in a line.

The proof of this rule follows from the fact that when currents are steady, there is no accumulation of charges at any junction or at any point in a line. Thus, the total current flowing in, (which is the rate at which charge flows into the junction), must equal the total current flowing out.

(b) **Loop rule**: The algebraic sum of changes in potential around any closed loop involving resistors and cells in the loop is zero (Fig. 3.15).

This rule is also obvious, since electric potential is dependent on the location of the point. Thus starting with any point if we come back to the same point, the total change must be zero. In a closed loop, we do come back to the starting point and hence the rule.

![At junction a the current leaving is I1 + I2 and current entering is I3. The junction rule says I3 = I1 + I2. At point h current entering is I1. There is only one current leaving h and by junction rule that will also be I1. For the loops ‘ahdcba’ and ‘ahdefga’, the loop rules give –30 I1 – 41 I3 + 45 = 0 and –30I1 + 21 I2 – 80 = 0.](image)

### Example 3.5
A battery of 10 V and negligible internal resistance is connected across the diagonally opposite corners of a cubical network consisting of 12 resistors each of resistance 1 ohm (Fig. 3.16). Determine the equivalent resistance of the network and the current along each edge of the cube.

![A cubical network of 12 resistors connected to a 10V battery across diagonally opposite corners A and C'. The current entering at A is 3I, which splits into I along each of the three edges (AB, AD, AA'). Further splitting and recombination of currents are shown at each node, eventually exiting at C' as 3I.](image)

Page : 99

**Solution** The network is not reducible to a simple series and parallel combinations of resistors. There is, however, a clear symmetry in the problem which we can exploit to obtain the equivalent resistance of the network.

The paths AA', AD and AB are obviously symmetrically placed in the network. Thus, the current in each must be the same, say, I. Further, at the corners A', B and D, the incoming current I must split equally into the two outgoing branches. In this manner, the current in all the 12 edges of the cube are easily written down in terms of I, using Kirchhoff’s first rule and the symmetry in the problem.

Next take a closed loop, say, ABCC'EA, and apply Kirchhoff’s second rule:
-IR - (1/2)IR - IR + ε = 0
where R is the resistance of each edge and ε the emf of battery. Thus,
ε = 5/2 I R

The equivalent resistance R<sub>eq</sub> of the network is
R<sub>eq</sub> = ε / 3I = 5/6 R

For R = 1 Ω, R<sub>eq</sub> = (5/6) Ω and for ε = 10 V, the total current (= 3 I) in the network is
3I = 10 V / (5/6) Ω = 12 A, i.e., I = 4 A

The current flowing in each edge can now be read off from the Fig. 3.16.

It should be noted that because of the symmetry of the network, the great power of Kirchhoff’s rules has not been very apparent in Example 3.5. In a general network, there will be no such simplification due to symmetry, and only by application of Kirchhoff’s rules to junctions and closed loops (as many as necessary to solve the unknowns in the network) can we handle the problem. This will be illustrated in Example 3.6.

### Example 3.6
Determine the current in each branch of the network shown in Fig. 3.17.

![A bridge-like circuit diagram with a battery of 10V. The network consists of four resistors forming a diamond shape (AB, BC, CD, DA) with a central branch (BD). Resistance values are: AB = 10 Ω, BC = 5 Ω, CD = 10 Ω, DA = 5 Ω, and BD = 5 Ω. A 10V battery is connected across points A and C.](image)

FIGURE 3.17

```description
A text box at the bottom right contains a URL: http://www.phys.hawaii.edu/~teb/optics/java/kirch3/ and the text "Simulation for application of Kirchhoff's rules:".
```

Physics

Page : 100

**Solution** Each branch of the network is assigned an unknown current to be determined by the application of Kirchhoff’s rules. To reduce the number of unknowns at the outset, the first rule of Kirchhoff is used at every junction to assign the unknown current in each branch. We then have three unknowns I<sub>1</sub>, I<sub>2</sub> and I<sub>3</sub> which can be found by applying the second rule of Kirchhoff to three different closed loops.

Kirchhoff’s second rule for the closed loop ADCA gives,
10 – 4(I<sub>1</sub> – I<sub>2</sub>) + 2(I<sub>2</sub> + I<sub>3</sub> – I<sub>1</sub>) – I<sub>1</sub> = 0 [3.61(a)]
that is, 7I<sub>1</sub> – 6I<sub>2</sub> – 2I<sub>3</sub> = 10

For the closed loop ABCA, we get
10 – 4I<sub>2</sub> – 2 (I<sub>2</sub> + I<sub>3</sub>) – I<sub>1</sub> = 0
that is, I<sub>1</sub> + 6I<sub>2</sub> + 2I<sub>3</sub> = 10 [3.61(b)]

For the closed loop BCDEB, we get
5 – 2 (I<sub>2</sub> + I<sub>3</sub>) – 2 (I<sub>2</sub> + I<sub>3</sub> – I<sub>1</sub>) = 0
that is, 2I<sub>1</sub> – 4I<sub>2</sub> – 4I<sub>3</sub> = –5 [3.61(c)]

Equations (3.61 a, b, c) are three simultaneous equations in three unknowns. These can be solved by the usual method to give
I<sub>1</sub> = 2.5A, I<sub>2</sub> = 5/8 A, I<sub>3</sub> = 17/8 A

The currents in the various branches of the network are
AB : 5/8 A, CA : 2 1/2 A, DEB : 17/8 A
AD : 17/8 A, CD : 0 A, BC : 2 1/2 A

It is easily verified that Kirchhoff’s second rule applied to the remaining closed loops does not provide any additional independent equation, that is, the above values of currents satisfy the second rule for every closed loop of the network. For example, the total voltage drop over the closed loop BADEB
5 V + 5/8 × 4 V − 15/8 × 4 V
equal to zero, as required by Kirchhoff’s second rule.

## 3.13 WHEATSTONE BRIDGE

As an application of Kirchhoff’s rules consider the circuit shown in Fig. 3.18, which is called the Wheatstone bridge. The bridge has four resistors R<sub>1</sub>, R<sub>2</sub>, R<sub>3</sub> and R<sub>4</sub>. Across one pair of diagonally opposite points (A and C in the figure) a source is connected. This (i.e., AC) is called the battery arm. Between the other two vertices, B and D, a galvanometer G (which is a device to detect currents) is connected. This line, shown as BD in the figure, is called the galvanometer arm.

For simplicity, we assume that the cell has no internal resistance. In general there will be currents flowing across all the resistors as well as a current I<sub>g</sub> through G. Of special interest, is the case of a balanced bridge where the resistors are such that I<sub>g</sub> = 0. We can easily get the balance condition, such that there is no current through G. In this case, the Kirchhoff’s junction rule applied to junctions D and B (see the figure)

Reprint 2025-26

Current Electricity

Page : 101

immediately gives us the relations I<sub>3</sub> = I<sub>1</sub> and I<sub>4</sub> = I<sub>2</sub>. Next, we apply Kirchhoff’s loop rule to closed loops ADBA and CBDC. The first loop gives
-I<sub>1</sub> R<sub>1</sub> + 0 + I<sub>2</sub> R<sub>2</sub> = 0 (I<sub>g</sub> = 0) (3.62)
and the second loop gives, upon using I<sub>3</sub> = I<sub>1</sub>, I<sub>4</sub> = I<sub>2</sub>
I<sub>2</sub> R<sub>4</sub> + 0 - I<sub>1</sub> R<sub>3</sub> = 0 (3.63)
From Eq. (3.62), we obtain,
I<sub>1</sub> / I<sub>2</sub> = R<sub>2</sub> / R<sub>1</sub>
whereas from Eq. (3.63), we obtain,
I<sub>1</sub> / I<sub>2</sub> = R<sub>4</sub> / R<sub>3</sub>
Hence, we obtain the condition
R<sub>2</sub> / R<sub>1</sub> = R<sub>4</sub> / R<sub>3</sub> [3.64(a)]

![Diagram of a Wheatstone bridge circuit showing four resistors R1, R2, R3, and R4 arranged in a diamond shape with a galvanometer G connected between points B and D, and a battery connected between points A and C.](image)
FIGURE 3.18

This last equation relating the four resistors is called the balance condition for the galvanometer to give zero or null deflection.

The Wheatstone bridge and its balance condition provide a practical method for determination of an unknown resistance. Let us suppose we have an unknown resistance, which we insert in the fourth arm; R<sub>4</sub> is thus not known. Keeping known resistances R<sub>1</sub> and R<sub>2</sub> in the first and second arm of the bridge, we go on varying R<sub>3</sub> till the galvanometer shows a null deflection. The bridge then is balanced, and from the balance condition the value of the unknown resistance R<sub>4</sub> is given by,
R<sub>4</sub> = R<sub>3</sub> (R<sub>2</sub> / R<sub>1</sub>) [3.64(b)]
A practical device using this principle is called the meter bridge.

### Example 3.7
The four arms of a Wheatstone bridge (Fig. 3.19) have the following resistances:
AB = 100 Ω, BC = 10 Ω, CD = 5 Ω, and DA = 60 Ω.

![Circuit diagram for Example 3.7 showing a Wheatstone bridge with specific resistance values: AB=100 ohms, BC=10 ohms, CD=5 ohms, DA=60 ohms. A galvanometer with 15 ohm resistance is connected between B and D. A 10V battery is connected across A and C.](image)
FIGURE 3.19

Reprint 2025-26

Physics

Page : 102

A galvanometer of 15 W resistance is connected across BD. Calculate the current through the galvanometer when a potential difference of 10 V is maintained across AC.

**Solution** Considering the mesh BADB, we have
100I<sub>1</sub> + 15I<sub>g</sub> – 60I<sub>2</sub> = 0
or 20I<sub>1</sub> + 3I<sub>g</sub> – 12I<sub>2</sub> = 0 [3.65(a)]

Considering the mesh BCDB, we have
10 (I<sub>1</sub> – I<sub>g</sub>) – 15I<sub>g</sub> – 5 (I<sub>2</sub> + I<sub>g</sub>) = 0
10I<sub>1</sub> – 30I<sub>g</sub> – 5I<sub>2</sub> = 0
2I<sub>1</sub> – 6I<sub>g</sub> – I<sub>2</sub> = 0 [3.65(b)]

Considering the mesh ADCEA,
60I<sub>2</sub> + 5 (I<sub>2</sub> + I<sub>g</sub>) = 10
65I<sub>2</sub> + 5I<sub>g</sub> = 10
13I<sub>2</sub> + I<sub>g</sub> = 2 [3.65(c)]

Multiplying Eq. (3.65b) by 10
20I<sub>1</sub> – 60I<sub>g</sub> – 10I<sub>2</sub> = 0 [3.65(d)]

From Eqs. (3.65d) and (3.65a) we have
63I<sub>g</sub> – 2I<sub>2</sub> = 0
I<sub>2</sub> = 31.5I<sub>g</sub> [3.65(e)]

Substituting the value of I<sub>2</sub> into Eq. [3.65(c)], we get
13 (31.5I<sub>g</sub>) + I<sub>g</sub> = 2
410.5 I<sub>g</sub> = 2
I<sub>g</sub> = 4.87 mA.

# SUMMARY

1. Current through a given area of a conductor is the net charge passing per unit time through the area.
2. To maintain a steady current, we must have a closed circuit in which an external agency moves electric charge from lower to higher potential energy. The work done per unit charge by the source in taking the charge from lower to higher potential energy (i.e., from one terminal of the source to the other) is called the electromotive force, or emf, of the source. Note that the emf is not a force; it is the voltage difference between the two terminals of a source in open circuit.
3. Ohm’s law : The electric current I flowing through a substance is proportional to the voltage V across its ends, i.e., V ∝ I or V = RI, where R is called the resistance of the substance. The unit of resistance is ohm: 1W = 1 V A<sup>–1</sup>.

Reprint 2025-26

Current Electricity

Page : 103

4. The resistance R of a conductor depends on its length l and cross-sectional area A through the relation,
R = ρl / A
where ρ, called resistivity is a property of the material and depends on temperature and pressure.

5. Electrical resistivity of substances varies over a very wide range. Metals have low resistivity, in the range of 10^-8 Ω m to 10^-6 Ω m. Insulators like glass and rubber have 10^22 to 10^24 times greater resistivity. Semiconductors like Si and Ge lie roughly in the middle range of resistivity on a logarithmic scale.

6. In most substances, the carriers of current are electrons; in some cases, for example, ionic crystals and electrolytic liquids, positive and negative ions carry the electric current.

7. Current density j gives the amount of charge flowing per second per unit area normal to the flow,
j = nq v_d
where n is the number density (number per unit volume) of charge carriers each of charge q, and v_d is the drift velocity of the charge carriers. For electrons q = - e. If j is normal to a cross-sectional area A and is constant over the area, the magnitude of the current I through the area is nev_d A.

8. Using E = V/l, I = nev_d A, and Ohm’s law, one obtains
eE = ρne^2 v_d / m
The proportionality between the force eE on the electrons in a metal due to the external field E and the drift velocity v_d (not acceleration) can be understood, if we assume that the electrons suffer collisions with ions in the metal, which deflect them randomly. If such collisions occur on an average at a time interval τ,
v_d = aτ = eEτ/m
where a is the acceleration of the electron. This gives
ρ = m / ne^2τ

9. In the temperature range in which resistivity increases linearly with temperature, the temperature coefficient of resistivity α is defined as the fractional increase in resistivity per unit increase in temperature.

10. Ohm’s law is obeyed by many substances, but it is not a fundamental law of nature. It fails if
(a) V depends on I non-linearly.
(b) the relation between V and I depends on the sign of V for the same absolute value of V.
(c) The relation between V and I is non-unique.
An example of (a) is when ρ increases with I (even if temperature is kept fixed). A rectifier combines features (a) and (b). GaAs shows the feature (c).

11. When a source of emf ε is connected to an external resistance R, the voltage V_ext across R is given by
V_ext = IR = R ε / (R + r)
where r is the internal resistance of the source.

Reprint 2025-26

Physics

Page : 104

12. Kirchhoff’s Rules –
(a) Junction Rule: At any junction of circuit elements, the sum of currents entering the junction must equal the sum of currents leaving it.
(b) Loop Rule: The algebraic sum of changes in potential around any closed loop must be zero.
13. The Wheatstone bridge is an arrangement of four resistances – R<sub>1</sub>, R<sub>2</sub>, R<sub>3</sub>, R<sub>4</sub> as shown in the text. The null-point condition is given by
R<sub>1</sub> / R<sub>2</sub> = R<sub>3</sub> / R<sub>4</sub>
using which the value of one resistance can be determined, knowing the other three resistances.


|Physical Quantity|Symbol|Dimensions|Unit|Remark|
|-|-|-|-|-|
|Electric current|I|\[A]|A|SI base unit|
|Charge|Q, q|\[T A]|C||
|Voltage, Electric potential difference|V|\[M L^2 T^-3 A^-1]|V|Work/charge|
|Electromotive force|e|\[M L^2 T^-3 A^-1]|V|Work/charge|
|Resistance|R|\[M L^2 T^-3 A^-2]|W|R = V / I|
|Resistivity|r|\[M L^3 T^-3 A^-2]|W m|R = rl/A|
|Electrical conductivity|s|\[M^-1 L^-3 T^3 A^2]|S|s = 1/r|
|Electric field|E|\[M L T^-3 A^-1]|V m^-1|Electric force / charge|
|Drift speed|v\_d|\[L T^-1]|m s^-1|v\_d = e E t / m|
|Relaxation time|t|\[T]|s||
|Current density|j|\[L^-2 A]|A m^-2|current/area|
|Mobility|m|\[M^-1 L^0 T^2 A^1]|m^2 V^-1 s^-1|v\_d / E|


### POINTS TO PONDER

1. Current is a scalar although we represent current with an arrow. Currents do not obey the law of vector addition. That current is a scalar also follows from it’s definition. The current I through an area of cross-section is given by the scalar product of two vectors:
I = j . DS
where j and DS are vectors.

Reprint 2025-26

Current Electricity

Page : 105

2. Refer to V-I curves of a resistor and a diode as drawn in the text. A resistor obeys Ohm’s law while a diode does not. The assertion that V = IR is a statement of Ohm’s law is not true. This equation defines resistance and it may be applied to all conducting devices whether they obey Ohm’s law or not. The Ohm’s law asserts that the plot of I versus V is linear i.e., R is independent of V.
Equation E = ρ j leads to another statement of Ohm’s law, i.e., a conducting material obeys Ohm’s law when the resistivity of the material does not depend on the magnitude and direction of applied electric field.
3. Homogeneous conductors like silver or semiconductors like pure germanium or germanium containing impurities obey Ohm’s law within some range of electric field values. If the field becomes too strong, there are departures from Ohm’s law in all cases.
4. Motion of conduction electrons in electric field E is the sum of (i) motion due to random collisions and (ii) that due to E. The motion due to random collisions averages to zero and does not contribute to v<sub>d</sub> (Chapter 10, Textbook of Class XI). v<sub>d</sub>, thus is only due to applied electric field on the electron.
5. The relation j = ρ v should be applied to each type of charge carriers separately. In a conducting wire, the total current and charge density arises from both positive and negative charges:
j = ρ<sub>+</sub> v<sub>+</sub> + ρ<sub>–</sub> v<sub>–</sub>
ρ = ρ<sub>+</sub> + ρ<sub>–</sub>
Now in a neutral wire carrying electric current,
ρ<sub>+</sub> = – ρ<sub>–</sub>
Further, v<sub>+</sub> ~ 0 which gives
ρ = 0
j = ρ<sub>–</sub> v<sub>–</sub>
Thus, the relation j = ρv does not apply to the total current charge density.
6. Kirchhoff’s junction rule is based on conservation of charge and the outgoing currents add up and are equal to incoming current at a junction. Bending or reorienting the wire does not change the validity of Kirchhoff’s junction rule.