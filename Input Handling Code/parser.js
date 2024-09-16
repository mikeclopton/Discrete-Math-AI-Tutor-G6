
// Get  HTML elements
const questionDisplay = document.getElementById('question-display');
const latexInput = document.getElementById('latex-input');
const output = document.getElementById('output');
const result = document.getElementById('result');

// Resize box to fit content
function adjHeight() {
    latexInput.style.height = 'auto';  // Reset the height to auto
    latexInput.style.height = latexInput.scrollHeight + 'px';  // Set the height based on scroll height
}

// LATEX code and renderer
function handleInput() {
    adjHeight();  // Adjust height on every input
    const latexCode = latexInput.value;
    output.innerHTML = `\\[${latexCode}\\]`;
    MathJax.typesetPromise();
}

// LaTeX normalizer for comparisons
function normalizeLatex(latexString) {
    return latexString
        .replace(/\s+/g, '') // Remove all whitespace
        .replace(/[\u00A0]/g, '') // Remove non-breaking spaces
        .trim();
}

// Event listeners
latexInput.addEventListener('input', handleInput);
