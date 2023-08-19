# Some Random Calculator

Here is some random calculator.

<div>
    <input type="text" id="result" read-write />
    <br />
    <button onclick="clear()">C</button>
    <button onclick="append('7')">7</button>
    <button onclick="append('8')">8</button>
    <button onclick="append('9')">9</button>
    <button onclick="append('/')">/</button>
    <br />
    <button onclick="append('4')">4</button>
    <button onclick="append('5')">5</button>
    <button onclick="append('6')">6</button>
    <button onclick="append('*')">*</button>
    <br />
    <button onclick="append('1')">1</button>
    <button onclick="append('2')">2</button>
    <button onclick="append('3')">3</button>
    <button onclick="append('-')">-</button>
    <br />
    <button onclick="append('0')">0</button>
    <button onclick="append('.')">.</button>
    <button onclick="calculate()">=</button>
    <button onclick="append('+')">+</button>
</div>

<script>
    function append(value) {
        document.getElementById("result").value += value;
    }

    function clear() {
        document.getElementById("result").value = "";
    }

    function calculate() {
        try {
            document.getElementById("result").value = 
            eval(document.getElementById("result").value);
        } catch (e) {
            alert('Invalid calculation');
            clear();
        }
    }
</script>
