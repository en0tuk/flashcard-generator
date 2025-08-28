import axios from 'axios';

let splide = new Splide('.splide', {
    type: "loop",
    gap: "1rem",
    drag: false
}).mount();

const myForm = document.querySelector('#flashcardForm');
const flashcardInfoInput = document.querySelector('#flashcardInfo');
const flashcardList = document.querySelector('#flashcards')

myForm.addEventListener('submit', function (event) {
    event.preventDefault();

    let flashcardInfo = flashcardInfoInput.value

    if (!flashcardInfo) return
    
    splide.root.classList.add("hidden")
    flashcardList.innerHTML = ''
    axios.post(import.meta.env.VITE_BACKEND_ADDRESS, String(flashcardInfo), { headers: {"Content-Type": "text/plain"} })
    .then((data) => {
        splide.root.classList.remove("hidden")
        data.data.flashcards.forEach(flashcard => {
            splide.add(`
            <li class="splide__slide">
              <div class="flashcard">
                <div class="flashcard-content">
                    ${flashcard}
                </div>
              </div>
            </li>
            `)
        });
        splide.go(0)
        splide.refresh()
    })
    
});