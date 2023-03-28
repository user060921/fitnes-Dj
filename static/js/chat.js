const chat = document.getElementById('chat')
const chat_exit = document.getElementById('chat_exit')
const chat_submit = document.getElementById('chat_submit')
const chat_body = document.getElementById('chat_body')
let user_selected = []
function requestFunc(text) {
    const messageRequest = document.createElement('div')
    messageRequest.innerHTML = `
    <div class="request">
        <div class="message">
            ${text}
        </div>
     </div>
    `
    chat_body.appendChild(messageRequest)
}
function requestFuncLink(text, link) {
    const messageRequest = document.createElement('div')
    messageRequest.innerHTML = `
    <div class="request">
        <a href='${link}'>
            <div class="message">
                ${text}
            </div>
        </a>
     </div>
    `
    chat_body.appendChild(messageRequest)
}
function createBtnFirst() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message first_btn cursor">
                Pas daraja
            </div>
        </div>
        <div class='response'>
            <div class="message first_btn cursor">
                Vashee qiyin daraja
            </div>
        </div>
        <div class='response'>
            <div class="message first_btn cursor">
                O'rtancha daraja
            </div>
        </div>
        <div class='response'>
            <div class="message first_btn cursor">
                Kotta daraja
            </div>
        </div>`
    chat_body.appendChild(messageBtn)
}
function createBtnTwo() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message two_btn cursor">
                Kachka
            </div>
        </div>
        <div class='response'>
            <div class="message two_btn cursor">
                Ozish
            </div>
        </div>`
    chat_body.appendChild(messageBtn)
}
function createBtnTree() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message three_btn cursor">
            Ayol
            </div>
        </div>
        <div class='response'>
            <div class="message three_btn cursor">
            Erkak
            </div>
        </div>`
    chat_body.appendChild(messageBtn)
}
function createBtnFour() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message four_btn cursor">
            Qo'l
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Ko'krak
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Bel+
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Qorin
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Oyoq
            </div>
        </div>
        `
    chat_body.appendChild(messageBtn)
}
function createBtnFive() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message five_btn cursor">
            Raxmat! Yana takrorlashni xoxlayman!
            </div>
        </div>`
    chat_body.appendChild(messageBtn)
}
chat_submit.addEventListener('click', () => {
    chat.classList.add('ative')
    setTimeout(() => {
        // 1-request
        chat_body.innerHTML = `
        <div class="request">
            <div class="message">
                Assalomu Aleykum. Qaysi dasturni tanlaysiz?
            </div>
        </div>`
    }, 500)
    setTimeout(() => {
        createBtnFirst()
    }, 1000)

})
chat_body.addEventListener('click', (e) => {
    let thIs = e.target
    // console.log(thIs);
    if (e.target.classList.contains("first_btn")) {
        // 2-request
        let text = `Siz "${e.target.innerHTML}" ni tanladingiz. Qanday dastur turini tanlaysiz?`
        requestFunc(text)
        createBtnTwo()
        chat_body.scrollTop = chat_body.scrollHeight
        user_selected.push(e.target.innerHTML)
    }
    else if (e.target.classList.contains("two_btn")) {
        // 3-request
        let text = `Siz "${e.target.innerHTML}" tanladingiz. Iltimos jinsingizni tanlang.`
        requestFunc(text)
        createBtnTree()
        chat_body.scrollTop = chat_body.scrollHeight
        user_selected.push(e.target.innerHTML)
    }
    else if (e.target.classList.contains("three_btn")) {
        // 4-request
        let text = `Qaysi tana qismini tanlaysiz?`
        requestFunc(text)
        createBtnFour()
        user_selected.push(e.target.innerHTML)
        chat_body.scrollTop = chat_body.scrollHeight
    }
    else if (e.target.classList.contains("four_btn")) {
        // 5-request
        let text = `Siz "${e.target.innerHTML}" tanladingiz.
        Keyingi variantlarni kurib chiqing:`
        user_selected.push(e.target.innerHTML)
        requestFunc(text)
        ajaxRequest(user_selected);
        // let text1 = `"8 минут на нижний пресс". Короткое, но эффективное занятие из классических упражнений.`
        // let text2 = `"Топ-10 упражнений для похудения живота стоя." 10 эффективных и разнообразных упражнения стоя.`
        // let text3 = `"20 упражнений без прыжков". Эффективная зарядка, которая не только усилит жиросжигание, но и зарядит энергией.`
        // let text4 = `"Топ-10 упражнений для похудения в животе". 10 упражнений для всего пресса и зоны боков.`
        // requestFuncLink(text1)
        // requestFuncLink(text2)
        // requestFuncLink(text3)
        // requestFuncLink(text4)
        // createBtnFive()
        chat_body.scrollTop = chat_body.scrollHeight
    }
    else if (e.target.classList.contains("five_btn")) {
        // 4-request
        let text = `Qaysi dasturni tanladingiz?`
        requestFunc(text)
        createBtnFour()
        chat_body.scrollTop = chat_body.scrollHeight
        user_selected.push(e.target.innerHTML)
    }
})
chat_exit.addEventListener('click', () => {
    chat.classList.remove('ative')
})
