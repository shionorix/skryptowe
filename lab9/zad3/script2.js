class valDecrement extends HTMLElement {
    constructor() {
        super();
        this.shadow = this.attachShadow({mode: "open"});
    }

    set value(val) {
        this.setAttribute("value", val);
    }

    get value() {
        return this.getAttribute("value");
    }

    render() {
        this.shadow.innerHTML = `<span>${this.value === null ? document.forms[0].number.value: this.value}</span>`
    }

    connectedCallback() {
        this.render();
    }

    static get observedAttributes(){
        return ["value"];
    }

    attributeChangedCallback(prop, oldVal, newVal) {
        if (prop === 'value') 
            this.render()
    }    
}

customElements.define("val-decrement", valDecrement);


val = 0;

function loopFuntion() {
    val = document.forms[0].number.value;
    if (val > 0) {
        val--;
        document.forms[0].number.value = val;
        for (let i = 0; i < 10; i++) {
            document.getElementsByTagName('val-decrement')[i].setAttribute("value", val);
        }
    }
}

setInterval(loopFuntion, 500);
