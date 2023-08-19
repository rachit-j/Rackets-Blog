# Some Random Calculator

Below is some random calculator.

<div>
    <input type="text" id="result" readonly />
    <br />
    <button onclick="clearResult()">C</button>
    <button onclick="appendToResult('7')">7</button>
    <button onclick="appendToResult('8')">8</button>
    <button onclick="appendToResult('9')">9</button>
    <button onclick="appendToResult('/')">/</button>
    <br />
    <button onclick="appendToResult('4')">4</button>
    <button onclick="appendToResult('5')">5</button>
    <button onclick="appendToResult('6')">6</button>
    <button onclick="appendToResult('*')">*</button>
    <br />
    <button onclick="appendToResult('1')">1</button>
    <button onclick="appendToResult('2')">2</button>
    <button onclick="appendToResult('3')">3</button>
    <button onclick="appendToResult('-')">-</button>
    <br />
    <button onclick="appendToResult('0')">0</button>
    <button onclick="appendToResult('.')">.</button>
    <button onclick="calculate()">=</button>
    <button onclick="appendToResult('+')">+</button>
</div>

<script>
    function appendToResult(value) {
        document.getElementById("result").value += value;
    }

    function clearResult() {
        document.getElementById("result").value = "";
    }

    function calculate() {
        try {
            document.getElementById("result").value = 
            eval(document.getElementById("result").value);
        } catch (e) {
            alert('Invalid calculation');
            clearResult();
        }
    }
</script>
