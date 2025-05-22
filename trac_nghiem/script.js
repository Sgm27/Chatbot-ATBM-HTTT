// Quiz data will be loaded from JSON
let quizData = [];
let userAnswers = [];
let timerInterval;
let seconds = 0;
let minutes = 0;
let hours = 0;

// DOM Elements
const questionsContainer = document.getElementById('questions-container');
const totalQuestionsEl = document.getElementById('total-questions');
const submitBtn = document.getElementById('submit-btn');
const resultsContainer = document.getElementById('results');
const scoreDisplay = document.getElementById('score-display');
const questionsReview = document.getElementById('questions-review');
const restartBtn = document.getElementById('restart-btn');
const timerEl = document.getElementById('timer');

// Initialize quiz
window.addEventListener('DOMContentLoaded', () => {
    loadQuizData();
    startTimer();
});

// Load quiz data from JSON file
async function loadQuizData() {
    try {
        const response = await fetch('questions.json');
        quizData = await response.json();
        
        // Initialize user answers array with null values (no answer selected)
        userAnswers = new Array(quizData.length).fill(null);
        
        // Update total questions
        totalQuestionsEl.textContent = quizData.length;
        
        // Show all questions
        displayAllQuestions();
    } catch (error) {
        console.error('Error loading quiz data:', error);
        questionsContainer.innerHTML = '<p class="error">Lỗi khi tải dữ liệu câu hỏi. Vui lòng tải lại trang.</p>';
    }
}

// Display all questions
function displayAllQuestions() {
    let questionsHTML = '';
    
    quizData.forEach((question, questionIndex) => {
        questionsHTML += `
            <div class="question-card">
                <div class="question-text">${question.number}. ${question.question}</div>
                <ul class="options" data-question="${questionIndex}">
                    ${question.options.map((option, optionIndex) => `
                        <li class="option" data-index="${optionIndex}" data-question="${questionIndex}">
                            <div class="option-label">
                                <span class="option-text">${option.label} ${option.text}</span>
                            </div>
                        </li>
                    `).join('')}
                </ul>
            </div>
        `;
    });
    
    questionsContainer.innerHTML = questionsHTML;
    
    // Add event listeners to all options
    document.querySelectorAll('.option').forEach(option => {
        option.addEventListener('click', () => {
            selectOption(option);
        });
    });
}

// Select an option
function selectOption(selectedOption) {
    const optionIndex = parseInt(selectedOption.dataset.index);
    const questionIndex = parseInt(selectedOption.dataset.question);
    
    userAnswers[questionIndex] = optionIndex;
    
    // Update UI to show selected option
    const questionOptions = document.querySelectorAll(`.option[data-question="${questionIndex}"]`);
    questionOptions.forEach(option => {
        option.classList.remove('selected');
    });
    selectedOption.classList.add('selected');
}

// Submit quiz
function submitQuiz() {
    // Stop timer
    clearInterval(timerInterval);
    
    // Calculate score
    let score = 0;
    const reviewHTML = [];
    
    quizData.forEach((question, index) => {
        const userAnswer = userAnswers[index];
        
        // Skip unanswered questions
        if (userAnswer === null) {
            reviewHTML.push(`
                <div class="review-item review-incorrect">
                    <p><strong>Câu ${question.number}:</strong> ${question.question}</p>
                    <p><strong>Trả lời của bạn:</strong> Chưa trả lời</p>
                </div>
            `);
            return;
        }
        
        // Add to review HTML
        reviewHTML.push(`
            <div class="review-item ${isCorrectAnswer(index) ? 'review-correct' : 'review-incorrect'}">
                <p><strong>Câu ${question.number}:</strong> ${question.question}</p>
                <p><strong>Trả lời của bạn:</strong> ${question.options[userAnswer].label} ${question.options[userAnswer].text}</p>
            </div>
        `);
        
        if (isCorrectAnswer(index)) {
            score++;
        }
    });
    
    // Display score
    const percentage = ((score / quizData.length) * 100).toFixed(1);
    scoreDisplay.innerHTML = `
        <p>Điểm của bạn: <strong>${score}/${quizData.length} (${percentage}%)</strong></p>
        <p>Thời gian làm bài: ${formatTime(hours, minutes, seconds)}</p>
    `;
    
    // Display review
    questionsReview.innerHTML = reviewHTML.join('');
    
    // Show results container
    questionsContainer.style.display = 'none';
    document.querySelector('.navigation-buttons').style.display = 'none';
    resultsContainer.classList.remove('hide');
    
    // Scroll to top to see results
    window.scrollTo(0, 0);
}

// Check if user selected the correct answer
function isCorrectAnswer(questionIndex) {
    // This is a simplified way for demonstration
    // You would need to update this with the actual correct answers
    // For now, we'll just use the first option (option index 0) as correct
    return userAnswers[questionIndex] === 0;
}

// Timer functions
function startTimer() {
    timerInterval = setInterval(updateTimer, 1000);
}

function updateTimer() {
    seconds++;
    if (seconds === 60) {
        seconds = 0;
        minutes++;
        if (minutes === 60) {
            minutes = 0;
            hours++;
        }
    }
    timerEl.textContent = formatTime(hours, minutes, seconds);
}

function formatTime(h, m, s) {
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

// Event listeners
submitBtn.addEventListener('click', submitQuiz);
restartBtn.addEventListener('click', () => {
    // Reset quiz state
    userAnswers = new Array(quizData.length).fill(null);
    
    // Reset timer
    clearInterval(timerInterval);
    seconds = 0;
    minutes = 0;
    hours = 0;
    timerEl.textContent = formatTime(hours, minutes, seconds);
    startTimer();
    
    // Show all questions again
    displayAllQuestions();
    
    // Show quiz container
    questionsContainer.style.display = 'block';
    document.querySelector('.navigation-buttons').style.display = 'flex';
    resultsContainer.classList.add('hide');
}); 