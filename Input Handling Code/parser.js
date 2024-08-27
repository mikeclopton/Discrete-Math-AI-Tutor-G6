//BAREBONES LATEX PARSER CODE AS A PROOF OF CONCEPT FOR LATEX INPUT IMPLEMENTATION

// Questions to demonstrate the latex parser functionality
const questions = [
    { question: "1. What is the LaTeX representation of the fraction one-half?", answer: "\\frac{1}{2}" },
    { question: "2. What is the LaTeX representation of the square root of x?", answer: "\\sqrt{x}" },
    { question: "3. What is the LaTeX representation of the summation of i from 1 to n?", answer: "\\sum_{i=1}^{n}" },
    { question: "4. What is the LaTeX representation of the integral of f(x)dx?", answer: "\\int f(x)\\,dx" },
    { question: "5. What is the LaTeX representation of a binomial coefficient (n choose k)?", answer: "\\binom{n}{k}" }
];

// Track the current question index
let currentQuestionIndex = 0;

// Get the HTML elements
const questionDisplay = document.getElementById('question-display');
const latexInput = document.getElementById('latex-input');
const output = document.getElementById('output');
const result = document.getElementById('result');
const submitButton = document.getElementById('submit-button');

// Function to display the current question
function displayQuestion() {
    questionDisplay.textContent = questions[currentQuestionIndex].question;
    latexInput.value = ""; // Clear the input box
    result.textContent = ""; // Clear the previous result
    output.innerHTML = ""; // Clear the previous LaTeX output
}

// Function to handle the LATEX code input and render it
function handleInput() {
    const latexCode = latexInput.value;
    output.innerHTML = `\\(${latexCode}\\)`;
    MathJax.typesetPromise();
}

// Function to normalize LaTeX strings for comparison
function normalizeLatex(latexString) {
    return latexString
        .replace(/\s+/g, '') // Remove all whitespace
        .replace(/[\u00A0]/g, '') // Remove non-breaking spaces
        .trim();
}

// Function to check the answer and move to the next question
function checkAnswer() {
    // Extract the properly formatted LaTeX output
    const userAnswer = normalizeLatex(output.textContent); // Get the LaTeX rendered output and normalize it

    // Render the correct answer in a temporary container and normalize it
    const tempContainer = document.createElement('div');
    tempContainer.innerHTML = `\\(${questions[currentQuestionIndex].answer}\\)`;
    document.body.appendChild(tempContainer); // Append to body for MathJax rendering

    MathJax.typesetPromise([tempContainer]).then(() => {
        const correctAnswer = normalizeLatex(tempContainer.textContent); // Normalize the correct rendered answer
        document.body.removeChild(tempContainer); // Clean up the temporary container

        // Compare the normalized answers
        if (userAnswer === correctAnswer) {
            result.textContent = "Correct!";
            result.style.color = "green";
        } else {
            result.textContent = "Incorrect!";
            result.style.color = "red";
        }

        // Move to the next question after a short delay
        setTimeout(() => {
            currentQuestionIndex++;
            if (currentQuestionIndex < questions.length) {
                displayQuestion(); // Display the next question
            } else {
                questionDisplay.textContent = "Quiz Completed!";
                latexInput.disabled = true;
                submitButton.disabled = true;
            }
        }, 1000); // 1 second delay
    });
}

// Event listeners
latexInput.addEventListener('input', handleInput);
submitButton.addEventListener('click', checkAnswer);

// Initialize the quiz by displaying the first question
displayQuestion();
