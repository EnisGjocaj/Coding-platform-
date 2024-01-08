const codeContainer = document.getElementById('code-container');
const codeSnippets = [
    "console.log('Hello, world!');",
    "for (let i = 0; i < 10; i++) {",
    "    console.log(i);",
    "}",
    "HTML, CSS, JS",
    "<div class='div-container'>Hello</div>",
    "pro fireship ? 'Programer i mire' : 'ChatGPT??'"
];

function getRandomColorClass() {
    const colorClasses = ['text-red-500', 'text-blue-500', 'text-green-500', 'text-yellow-500'];
    const randomIndex = Math.floor(Math.random() * colorClasses.length);
    return colorClasses[randomIndex];
}

function getRandomCodeSnippet() {
    const randomIndex = Math.floor(Math.random() * codeSnippets.length);
    return codeSnippets[randomIndex];
}

function writeCode() {
    const codeSnippet = getRandomCodeSnippet();
    const colorClass = getRandomColorClass();

    const codeLine = document.createElement('div');
    codeLine.innerHTML = `<span class="${colorClass}">${codeSnippet}</span>`;
    codeContainer.appendChild(codeLine);

    codeContainer.scrollTop = codeContainer.scrollHeight;
}

setInterval(writeCode, 1000);