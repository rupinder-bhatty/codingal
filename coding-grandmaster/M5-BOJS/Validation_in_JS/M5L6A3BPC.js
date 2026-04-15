/*
1) Create a function `clearScreen()`:
   a) Select the display/input element using `document.getElementById("result")`.
   b) Clear the display by setting `.value = ""`.

2) Create a function `setScreenValue(value)`:
   a) Select the display element and store it in a variable (example: `r`).
   b) If the display currently shows:
      - "Enter an expression" OR
      - "Invalid expression"
      then clear it before adding new input.
   c) Append the clicked button’s value to the display:
      `r.value += value`

3) Create a function `calculateResult()`:
   a) Select the display element (example: `resultElement`).
   b) Read the expression from the display using `.value` and remove extra spaces using `.trim()`.

4) Handle empty input:
   a) If the expression is empty:
      - Show "Enter an expression" in the display
      - Stop the function using `return`

5) Evaluate the expression safely using `try...catch`:
   a) In `try` block:
      - Use `eval(expression)` to calculate the result
      - Store the answer back in `resultElement.value`
   b) In `catch` block:
      - If an error happens, show "Invalid expression" in the display
*/