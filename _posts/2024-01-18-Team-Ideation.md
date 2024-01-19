---
toc: True
comments: True
layout: post
title: Team Ideation for 2 Tri Project
description: Checkpoint for Ideation Part B
courses: {labnotebook: {week: 19}}
type: tangibles
authors: Rachit Jaiswal
---

# Team Ideation

## Members
**Rachit Jaiswal** - Head Scrum Master, Scrum Master for P3 and responsible for relaying information, backend developer and deployment
**Finn Carpenter** - Scrum Master for P1 and responsible for relaying information, frontend developer
**Luna Iwazaki** - Design manager and frontend developer, project visualizer.
**Tanisha Patil** - Backend developer, design manager
**Theo Huntlas** - Backend developer, deployment
**Justin N** - Backend developer, deployment

## Ideation
Our team decided to create a platform that allows our users–high school students studying for their classes–to learn their material in a fun, engaging way, while also having quick cram resources, such as topic generated cheat sheets and calculators, as well as practice tests to help kids succeed. 

We call it bookNook.

We hope to get a mix of the something like popular game [Prodigy](https://www.prodigygame.com/main-en/) while also incorporating the usefulness of [Fiveable](https://fiveable.me/), however, we are going to head on a completely different path with these projects and try to incorporate something more modern and with better resources, UI, applicability, and tools for our students.

## Courses
We plan to have a set amount of courses in bookNook, with the option and framework to add more courses based on demand. Here is our set of starter courses, and the ones we may include if our project finishes earlier than expected.

Starter Courses (priority ranked):
- AP CSA
- AP CSP
- AP Chemistry
- AP Calculus (AB/BC since BC goes over AB)
- AP Statistics
- AP Biology
- Honors Principles of Engineering

Extended Courses (priority ranked):
- AP World History
- AP US History
- Writing (English and Humanities)

## Wireframes

We built and designed a couple of wireframes for what we want the whole site to look like. Here they are!

Our pre game interface will look something like this, with an access point and statistics to show how students are doing (in the future, maybe we can plan on giving teachers access to this). We also have other basic features like updates, which is our board of posts; register, our sign up/in page; our cram page, with resources like study guides powered by AI, as well as AI generated and answered questions (will use GPT-4 since it is better and Rachit has keys) through an API. The analyze page will be discussed in the next section.

![Wireframe 1](https://rackets-assets.vercel.app/assets/2tprojectwire1.png)

Our game will be designed as a retro game (to save our programmers) and will be using pixelated sprites. It will include basic trading and AI generated conversations from a *very cool* question bank that will be explained in a later section. 

![Wireframe 2](https://rackets-assets.vercel.app/assets/2tprojectwire3.png)

![Wireframe 3](https://rackets-assets.vercel.app/assets/2tprojectwire2.png)

## Code and Progress

### Neural Network

Although our team has been working a lot on our ideation, we have developed some code and progress to get us started. For starters, Finn and Rachit have been reviewing the Neural Network code that Rachit wrote for Stocktify. They are trying to brainstorm and figure out ways to increase the 500 epoch accuracy and add more subunits to the actual code. Finn and Rachit are hoping to integrate this into the website as an indicator of a student's performance. By compiling practice points and patterns, Rachit and Finn are hoping to create a method for the student and for educators to predict where the student will land so that they can take corrective action before. This will be included in the analyze tab of the wireframe.

<details>
    <summary>Click to Toggle Neural Network Code from Stocktify</summary>
    <div>

    class App {
        constructor() {}

        static main() {
            const app = new App();
            app.trainAndPredict(28, -12);
        }

        makeAPrediction(num1, num2) {
            const app = new App();
            return app.trainAndPredict(num1, num2);
        }

        strongerPrediction(input1, input2) {
            const network = new App();
            const list = [];
            for (let i = 0; i <= 10; i++) {
                list.push(network.makeAPrediction(input1, input2));
            }
            const top3 = list.sort((a, b) => b - a).slice(0, 3);
            const averageOfTop3 = top3.reduce((acc, val) => acc + val, 0) / top3.length;
            return averageOfTop3;
        }

        trainAndPredict(num1, num2) {
            const data = [
                [28, -12],
                [28, 21],
                [98, 11],
                [14, -33]
            ];
            const answers = [0.2, 0.7, 0.9, 0.1];

            const network500 = new Network(500);
            network500.train(data, answers);

            const network1000 = new Network(1000);
            network1000.train(data, answers);

            const prediction = network500.predict(num1, num2);
            return prediction;
        }
    }

    class Network {
        constructor(epochs, learnFactor = null) {
            this.epochs = epochs;
            this.learnFactor = learnFactor;
            this.neurons = Array(6).fill().map(() => new Neuron());
        }

        predict(input1, input2) {
            return this.neurons[5].compute(
                this.neurons[4].compute(
                    this.neurons[2].compute(input1, input2),
                    this.neurons[1].compute(input1, input2)
                ),
                this.neurons[3].compute(
                    this.neurons[1].compute(input1, input2),
                    this.neurons[0].compute(input1, input2)
                )
            );
        }

        train(data, answers) {
            let bestEpochLoss = null;
            for (let epoch = 0; epoch < this.epochs; epoch++) {
                const epochNeuron = this.neurons[epoch % 6];
                epochNeuron.mutate(this.learnFactor);

                const predictions = data.map(d => this.predict(d[0], d[1]));
                const thisEpochLoss = Util.meanSquareLoss(answers, predictions);

                if (bestEpochLoss === null) {
                    bestEpochLoss = thisEpochLoss;
                    epochNeuron.remember();
                } else {
                    if (thisEpochLoss < bestEpochLoss) {
                        bestEpochLoss = thisEpochLoss;
                        epochNeuron.remember();
                    } else {
                        epochNeuron.forget();
                    }
                }
            }
        }
    }

    class Neuron {
        constructor() {
            this.random = Math.random;
            this.oldBias = this.random() * 2 - 1;
            this.bias = this.random() * 2 - 1;
            this.oldWeight1 = this.random() * 2 - 1;
            this.weight1 = this.random() * 2 - 1;
            this.oldWeight2 = this.random() * 2 - 1;
            this.weight2 = this.random() * 2 - 1;
        }

        mutate(learnFactor) {
            const changeFactor = learnFactor ? learnFactor * (this.random() * 2 - 1) : this.random() * 2 - 1;
            const propertyToChange = Math.floor(this.random() * 3);
            if (propertyToChange === 0) {
                this.bias += changeFactor;
            } else if (propertyToChange === 1) {
                this.weight1 += changeFactor;
            } else {
                this.weight2 += changeFactor;
            }
        }

        forget() {
            this.bias = this.oldBias;
            this.weight1 = this.oldWeight1;
            this.weight2 = this.oldWeight2;
        }

        remember() {
            this.oldBias = this.bias;
            this.oldWeight1 = this.weight1;
            this.oldWeight2 = this.weight2;
        }

        compute(input1, input2) {
            const preActivation = (this.weight1 * input1) + (this.weight2 * input2) + this.bias;
            const output = Util.sigmoid(preActivation);
            return output;
        }
    }

    class Util {
        static sigmoid(inVal) {
            return 1 / (1 + Math.exp(-inVal));
        }

        static meanSquareLoss(correctAnswers, predictedAnswers) {
            const sumSquare = correctAnswers.reduce((acc, val, idx) => {
                const error = val - predictedAnswers[idx];
                return acc + (error * error);
            }, 0);
            return sumSquare / correctAnswers.length;
        }
    }

    function executePrediction() {
        const num1 = parseInt(document.getElementById('num1').value, 10);
        const num2 = parseInt(document.getElementById('num2').value, 10);

        const app = new App();
        const result = app.trainAndPredict(num1, num2);

        document.getElementById('output').textContent = `Prediction Result: ${result}`;
    }
    function executePrediction() {
        const num1 = parseInt(document.getElementById('num1').value, 10);
        const num2 = parseInt(document.getElementById('num2').value, 10);

        const app = new App();
        const predictions = [];
        for (let i = 0; i < 10; i++) {
            predictions.push(app.trainAndPredict(num1, num2));
        }
        const top3 = predictions.sort((a, b) => b - a).slice(0, 3);
        const averageOfTop3 = top3.reduce((acc, val) => acc + val, 0) / top3.length;

        document.getElementById('output').textContent = `Prediction Result: ${averageOfTop3.toFixed(2)}`;

        // Update the progress bar
        const progressBar = document.getElementById('progressBar');
        progressBar.style.width = `${averageOfTop3 * 100}%`;
    }

    </div>
</details>


### Chatbot

Our team has been working to deploy a chatbot, a new one. Since text-davinci and other easier to use, older models were shut down, we had to learn a new framework for our serverside bot. We chose to go with Next.js since it is supported by OpenAI, instead of Node, which we used last time (it is basically the same thing since Next is built off of Node and they are really similar). 

As of now, posts from this site are not working... we are working on fixing this. However, we have postman testing to make sure our bot works.

<label for="prompt">Enter your prompt:</label><br>
<input type="text" id="prompt" name="prompt" value="hello"><br>
<button id="sendButton">Send Prompt</button>
<p><strong>Response:</strong></p>
<p id="response"></p>
<script>
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById('sendButton').addEventListener('click', sendPrompt);
    });
    async function sendPrompt() {
        const promptText = document.getElementById('prompt').value;
        const responseContainer = document.getElementById('response');
        try {
            const response = await fetch('https://gptbot-git-main-rachit-j.vercel.app/api/openai', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: promptText }),
                mode: 'cors' // This line enables CORS
            });
            const data = await response.json();
            responseContainer.textContent = data.text;
        } catch (error) {
            responseContainer.textContent = 'Error: ' + error;
        }
    }
</script>


![Postman Bot Testing](https://rackets-assets.vercel.app/assets/2tprojectbotpostman.png)

### Frontend/Backend Setup

The frontend and the backend for our project are in the process of being set up. After the deployment lesson (which Rachit, Tanisha, and Luna are presenting), the backend will be deployed, and the frontend will be deployed to Github Pages even earlier. For now, they are both being set up, with our members using pull and merge requests to contribute to code, just like in the real world. This way, we are able to analyze and check each other's code before we merge it into the main branch, which will help us stop problems being put into main. 

![Justin YEAHHH](https://rackets-assets.vercel.app/assets/justin_tesing_pull.png)

![GOING INSANE](https://rackets-assets.vercel.app/assets/rachit_testing_pull_1.png)

![GOING EVEN MORE INSANE](https://rackets-assets.vercel.app/assets/rachit_testing_pull_2.png)

## Diagrams for Finalized Plan

![Look at this](https://rackets-assets.vercel.app/assets/2tprojcleandiagram.png)

<details>
    <summary>Connected boxes for Diagram Under Here. CAUTION</summary>

![Not this](https://rackets-assets.vercel.app/assets/2tprojuncleandiagram.png)

</details>