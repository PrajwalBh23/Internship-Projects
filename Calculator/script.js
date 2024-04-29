let input = document.getElementById("display_point");
let buttons = document.querySelectorAll(".operator");

let expression = ""; 
let shouldEvaluate = false;

buttons.forEach(button => {
    button.addEventListener("click", (e) => {
        let buttonText = e.target.getAttribute("value");
    
        if (buttonText === 'C') {
            expression = "";
        } else if (buttonText === 'CE') {
            expression = expression.substring(0, expression.length - 1);
        } else if (buttonText === 'delect') {
            expression = expression.slice(0, -1);
        } else {
            switch(buttonText) {
                case "=":
                    try {
                        expression = eval(expression);
                        shouldEvaluate = false;
                    } catch (error) {
                        expression = "Error";
                    }
                    break;
                case "x²":
                    expression += "**2";
                    break;
                case "1/x":
                    expression += "1/";
                    break;
                case "√":
                    expression = `Math.sqrt(${expression})`;
                    break;
                case "/":
                    expression += "/";
                    shouldEvaluate = false;
                    break;
                case "x":
                    expression += "*";
                    shouldEvaluate = false;
                    break;
                case "add":
                    expression += "+";
                    shouldEvaluate = false;
                    break;
                case "sub":
                    expression += "-";
                    shouldEvaluate = false;
                    break;
                case "%":
                    expression += "%";
                    shouldEvaluate = false;
                    break;
                default:
                    if (shouldEvaluate) {
                        expression = buttonText;
                        shouldEvaluate = false;
                    } else {
                        expression += buttonText;
                    }
            }
        }
        input.value = expression;
    });
});
