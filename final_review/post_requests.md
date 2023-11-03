---
layout: post
title: Post Requests for API and Chatbot
description: 
toc: False
permalink: /tri1review-post
courses: {'csa': {'week': 11}}
type: tangibles
---
## API POST REQUEST
```js
    var num = 0;
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById('searchbut').addEventListener('click', getStockData);
        
        async function getStockData() {
            const userInput = document.getElementById('searchresult').value.trim().toUpperCase();
            const stockHistory = document.getElementById('scrollbox');
            console.log(userInput);
            // Clear previous data
            // stockHistory.innerHTML = "";

            // Display stock name in bold at the top
            //<!-- stockHistory.innerHTML += `<div id="results"><b>${userInput}</b>`; -->

            const controller = new AbortController();
            const signal = controller.signal;

            // Set a timeout to abort the fetch request
            const timeoutId = setTimeout(() => controller.abort(), 10000); // 10 seconds

            try {
                const response = await fetch(`https://stocktify.stu.nighthawkcodingsociety.com/api/stockdata?symbol=${userInput}`, {
                    method: 'GET',
                    signal: signal,
                    mode: 'cors' // Add this line to enable CORS
                });

                const data = await response.json();

                // Parse and display the "Last Refreshed" data and stock details
                const lastRefreshed = data["Meta Data"]["3. Last Refreshed"];
                const dailyData = data["Time Series (Daily)"][lastRefreshed];
                const openData = dailyData["1. open"];

                stockHistory.innerHTML += `<div class="results" id="${num}re"><b>${userInput}</b>: ${lastRefreshed} --> ${dailyData["1. open"]} <button id="${num}rebut" class="butto" onclick="redirect()">Predict</button><button id="playAdd" class="butto" onclick="saveStockLocal(${userInput})">+</button></div>`;
                stockHistory.innerHTML += "<hr>"; // Add a horizontal line after the data
                stockHistory.innerHTML += `<div></div>`;
                num++;

            } catch (error) {
                if (error.name === 'AbortError') {
                    stockHistory.innerHTML += `<div>Error: Request timed out</div>`;
                } else {
                    stockHistory.innerHTML += `<div>Error: Please enter in a valid stock</div>`;
                    stockHistory.innerHTML += "<hr>"; // Add a horizontal line after the data
                    stockHistory.innerHTML += `<div></div>`;
                    stockHistory.innerHTML += `<div></div>`;

                }
            } finally {
                clearTimeout(timeoutId);
            }
        }
    });
```

## CHATBOT POST REQUEST
```js
        async function sendMessage() {
            const userInput = document.getElementById('user-inputbut').value;
            const chatHistory = document.getElementById('chat-historybut');

            // Display user's message
            chatHistory.innerHTML += `<div>User: ${userInput}</div>`;

            const controller = new AbortController();
            const signal = controller.signal;

            // Set a timeout to abort the fetch request
            const timeoutId = setTimeout(() => controller.abort(), 10000); // 10 seconds

            try {
                const response = await fetch('https://stocktifybot.vercel.app/api/generate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ stockbot: userInput }),
                    signal: signal,
                    mode: 'cors' // Add this line to enable CORS
                });

                const data = await response.json();

                // Display Chatbot's response
                chatHistory.innerHTML += `<div>Bot: ${removeSpecialCharsAtStart(data.result)}</div>`;
                //const responseText = await response.text();
                //console.log(responseText);

            } catch (error) {
                if (error.name === 'AbortError') {
                    chatHistory.innerHTML += `<div>Error: Request timed out</div>`;
                } else {
                    chatHistory.innerHTML += `<div>Error: ${error.message}</div>`;
                }
            } finally {
                clearTimeout(timeoutId);
            }
        }

```