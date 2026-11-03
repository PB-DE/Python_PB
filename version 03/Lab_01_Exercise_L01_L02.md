# Laboratory Exercise 1: Computing Foundations & Python Basics

| Student Details | |
| :--- | :--- |
| **Student Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | **Student ID:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| **Duration:** 2 Hours (120 Minutes) | **Total Points:** 100 Points |

---

## 1. Learning Objectives

- **Binary & Data Types:** Understand binary representation, bit capacity, primitive types (`int`, `float`, `str`, `bool`), dynamic type checking (`type()`), and assignment (`=`) vs. equality (`==`).
- **Operators & Precedence:** Apply arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`) adhering to operator precedence rules (PEMDAS).
- **Interactive I/O & Modeling:** Process console input via `input()` with type casting, translate scientific/aeronautical formulas, and implement conditional branching (`if - elif - else`).

---

## 2. Exercise Structure, Evaluation & Instructor Sign-Off

This 120-minute laboratory session is divided into 5 sequential parts totaling 100 points: **Part 1: Binary Representation & Computing Concepts** (20 mins, 15 pts), **Part 2: Data Types, Operators & Precedence Rules** (25 mins, 20 pts), **Part 3: Interactive I/O, Strings & Type Casting** (25 mins, 20 pts), **Part 4: Formula Modeling: Moore’s Law Calculator** (30 mins, 25 pts), and **Part 5: Challenge: Aircraft Approach Speed Telemetry** (20 mins, 20 pts).

| Instructor Verification | Details |
| :--- | :--- |
| **Score Awarded:** \_\_\_\_\_ / 100 Points | **Instructor Signature:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp;&nbsp;&nbsp; **Date:** \_\_\_\_\_\_ / \_\_\_\_\_\_ / 20\_\_ |
| **Instructor Comments & Feedback:** | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

---

<div style="page-break-after: always;"></div>

## Part 1: Binary Representation & Basic Concepts (15 Points)

### Task 1.1: Binary and Integer Conversions (8 Points)

In computer architecture, data and machine instructions are stored as sequences of binary digits (bits). Complete the following tasks in Python:

1. **(2 Points)** Convert the 8-bit binary literal `0b10110101` into its decimal equivalent and print the integer result.

   **Answer / Output:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
2. **(3 Points)** An aircraft telemetry transponder stores an altitude code as the decimal integer `876`. Convert this number to its binary representation using Python’s `bin()` function and print the result.

   **Answer / Output:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3. **(3 Points)** Using Python exponentiation (`**`), compute and display the maximum unsigned decimal value that can be represented by:

   - A 4-bit unsigned integer ($2^4 - 1$): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
   - An 8-bit unsigned integer ($2^8 - 1$): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
   - A 16-bit unsigned integer ($2^{16} - 1$): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Task 1.2: Assignment vs. Equality Comparison (7 Points)

Examine the code snippet below:

```python
x = 42
y = 40 + 2

print('Check equality:', x == y)
# print('Try assignment inside print:', x = y) # Uncommenting causes an error
```

Explain in your own words why `x == y` evaluates successfully to `True`, but attempting `x = y` inside `print()` raises a `SyntaxError`.

**Student Answer / Explanation:**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## Part 2: Data Types, Operators, and Precedence (20 Points)

### Task 2.1: Flight Duration Decomposer (8 Points)

A regional flight has an elapsed flight duration given as an integer number of minutes:

```python
total_minutes = 278
```

Using **only** integer division (`//`) and modulo (`%`), write code to compute the number of whole hours and remaining minutes.

**Student Answer / Output:**

- **Whole Hours (`//`):** \_\_\_\_\_\_\_\_\_\_ hours
- **Remaining Minutes (`%`):** \_\_\_\_\_\_\_\_\_\_ minutes

### Task 2.2: Scientific Formula Translation & Precedence (12 Points)

Translate the following physics and mathematical expressions into valid Python expressions. Use parentheses explicitly to make operator precedence clear:

1. **(4 Points) Kinetic Energy:**

   $$
   E = \frac{1}{2} m v^2
   $$

   Where mass $m = 1200.0\text{ kg}$, velocity $v = 45.0\text{ m/s}$. Compute and print $E$.

   **Calculated Result ($E$):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Joules **Program Output:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
2. **(4 Points) Gravitational Force:**

   $$
   F = G \frac{m_1 m_2}{r^2}
   $$

   Where $G = 6.674 \times 10^{-11}$, $m_1 = 5.97 \times 10^{24}$, $m_2 = 70.0$, $r = 6.371 \times 10^6$. Compute and print $F$.

   **Calculated Result ($F$):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ N **Program Output:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3. **(4 Points) Precedence Evaluation:**
   Evaluate the following expression, print its numeric result, and print its data type using `type()`:

   ```python
   result = 10 + 3 * 2 ** 3 / 4 // 2 - 1
   ```

   **Program Result Value:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
   **Data Type (`type(result)`):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
   **Step-by-Step Precedence Breakdown:**
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## Part 3: Interactive I/O, Strings & Type Casting (20 Points)

### Task 3.1: Aircraft Fuel Efficiency Calculator (20 Points)

Write a standalone interactive script that prompts the user for flight statistics and computes fuel efficiency indices:

1. Prompt the user to enter the **Aircraft Model Name** (string).
2. Prompt the user to enter the **Total Nautical Miles Flown** (float).
3. Prompt the user to enter the **Total Fuel Consumed in Gallons** (float).
4. Compute:

   $$
   \text{Fuel Efficiency (NM/gal)} = \frac{\text{Distance Flown}}{\text{Fuel Consumed}}
   $$

   $$
   \text{Consumption Rate (gal/NM)} = \frac{\text{Fuel Consumed}}{\text{Distance Flown}}
   $$
5. Display the formatted flight report rounded to 2 decimal places for efficiency and 3 decimal places for consumption rate.

**Example Run:**

```text
Enter aircraft model: Cessna 172 Skyhawk
Enter distance flown (NM): 320.5
Enter fuel consumed (gallons): 38.2

--- Flight Report for Cessna 172 Skyhawk ---
Efficiency: 8.39 NM/gal
Consumption Rate: 0.119 gal/NM
```

**Answer / Program Output:**

- **Aircraft Model Tested:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- **Distance Flown:** \_\_\_\_\_\_\_\_\_\_ NM   |   **Fuel Consumed:** \_\_\_\_\_\_\_\_\_\_ gallons
- **Program Fuel Efficiency:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ NM/gal
- **Program Consumption Rate:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ gal/NM

---

## Part 4: Practical Modeling: Moore’s Law Calculator (25 Points)

In Lecture 1, you explored **Moore’s Law**, which models the historical observation that the number of transistors on microchips roughly doubles every 2 years:

$$
N(t) = N_0 \times 2^{\frac{t - t_0}{2}}
$$

Where:

- $t_0 = 1971$ (Release year of the Intel 4004 microprocessor)
- $N_0 = 2,300$ (Transistor count of the Intel 4004)
- $t$ = Target analysis year entered by the user ($t \ge 1971$)

### Implementation Requirements:

1. Prompt the user to enter a target year $t$ as an integer.
2. Calculate the estimated number of transistors $N(t)$ using the formula.
3. Calculate the **Growth Factor** relative to 1971:

   $$
   \text{Growth Factor} = \frac{N(t)}{N_0}
   $$
4. Display the target year, predicted transistor count, and growth factor (formatted with 2 decimal places).

**Example Run:**

```text
Enter target year: 2023
Estimated transistors in year 2023: 154350387.89
Growth factor since 1971: 67108.86x
```

**Student Answer / Program Output:**

- **Target Year ($t$):** \_\_\_\_\_\_\_\_\_\_
- **Estimated Transistors ($N(t)$):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- **Growth Factor Since 1971:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## Part 5: Challenge Task — Flight Telemetry Descent Speed Check (20 Points)

An airport approach radar records 3 ground speed readings (in knots) from an approaching aircraft during final glide. Write a Python script to verify whether the aircraft is maintaining a safe approach speed:

### Implementation Requirements:

1. Prompt the user to enter 3 sequential speed readings (as floating-point numbers).
2. Compute and display:
   - **Minimum speed** (using `min()`)
   - **Maximum speed** (using `max()`)
   - **Average speed**
3. Implement conditional safety checks using `if - elif - else` statements:
   - If `average_speed > 160.0` knots: Print `"[WARNING] Approach speed is too fast! Go-around recommended."`
   - If `average_speed < 110.0` knots: Print `"[WARNING] Approach speed is too slow! Stall hazard."`
   - Otherwise: Print `"[NORMAL] Approach speed within acceptable landing envelope."`

**Example Run:**

```text
Enter speed reading 1 (knots): 145.5
Enter speed reading 2 (knots): 140.0
Enter speed reading 3 (knots): 138.5

--- Telemetry Summary ---
Min Speed: 138.5 knots
Max Speed: 145.5 knots
Average Speed: 141.33 knots
Status: [NORMAL] Approach speed within acceptable landing envelope.
```

**Student Answer / Program Output:**

- **Speed Readings Entered:** Reading 1: \_\_\_\_\_\_ kt  |  Reading 2: \_\_\_\_\_\_ kt  |  Reading 3: \_\_\_\_\_\_ kt
- **Minimum Speed:** \_\_\_\_\_\_\_\_\_\_ knots
- **Maximum Speed:** \_\_\_\_\_\_\_\_\_\_ knots
- **Average Speed:** \_\_\_\_\_\_\_\_\_\_ knots
- **Status / Warning Message:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
