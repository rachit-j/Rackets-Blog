---
layout: post
title: Trimester 1 Final Review
description: Review ticket for Trimester 1
toc: True
permalink: /tri1review
courses: {'csa': {'week': 11}, 'labnotebook': {'week': 11}}
type: tangibles
---

## Monitoring Recap
During our project, we keep track of important updates and log our structures with other important information through clickUp, our Scrum and information app!

Major Tasks: ![Major Tasks](/Rackets-Blog/images/major-tasks.png)

#### 1) Project Proposal
Links: [ClickUp](https://app.clickup.com/t/8685rkpkb) | [Proposal](https://theoh32.github.io/Stocktify/documentation/proposal)

Description: Our initial project proposal written by Grace and I outlined the complete vision for our website. This would change slightly in the future, but this was our major outline which we stuck to for the duration of the project. 

#### 2) Added Chatbot to the Frontend
Links: [ClickUp](https://app.clickup.com/t/86863rce8) | [Github Backend](https://github.com/rachit-j/stocktifybot/tree/main)

Description: By using a dynamic vercel backup, I was able to create a node server and deploy it on the backend while the rest of the Spring framework was still being created, which allowed me to deploy a side feature–the chatbot–earlier and get some features up and running. This feature was created off of AWS so my API key was not exposed (as this is a special API key, and other people have copied our repository on AWS many times). Note that this repository has also been forked by other people, so similarities may show up.

#### 3) Neural Network
Links: [ClickUp - Creation](https://app.clickup.com/t/8685rkj37) | [ClickUp - Connection](https://app.clickup.com/t/8685u06gc) | [Analysis Page](https://theoh32.github.io/Stocktify/analysis) | [Raw JavaScript For Development](/Rackets-Blog/tri1review-nnjs)

Description: By using Object Oriented Javascript, I was able to program one of the main features of our project: our neural network analysis. I coded this network to have its own weight, biases, and neurons independently using different classes. Originally, this was in Java, but upon suggestion for ease of access, we moved this to a frontend embed. However, this is still very heavy on object oriented Javascript, and is one of the core features that our team's project has to offer.

#### 4) Async Post/Get Request with Parser in Javascript
Links: [Details](/Rackets-Blog/tri1review-post)

Description: Not really that big, but I had to make the Post and Get requests for our API and our Chatbot. Here, we ran into a lot of CORS errors, but we were able to slowly but surely overcome each and EVERY one (I am not joking I got every single HTTP error known to man). 

#### 5) Documentation and Diagrams

Description: As the scrum master and the planner for our team, I was also primarily involved in making sure my team knew our goal and what everything looked like. To accomplish this, I created a lot of diagrams for our vision, and have documented them below. This allowed us to keep track and maintain our project without everyone getting confused.

- [ClickUp](https://app.clickup.com/9011012769/v/l/f/90110525775?pr=90110133665)
- [Vercel Readme](https://github.com/rachit-j/stocktifybot/tree/main#readme)
- [Frontend Readme](https://github.com/TheoH32/Stocktify#readme)
- [Backend Readme - Doesn't do Much](https://github.com/TheoH32/stocktifyBackend/blob/master/README.md)

#### 6) A little Caveat

I just wanted to include this fun part, but together with Theo, we were originally able to deploy our SpringBoot backend and configure everything from the users to helping make our first original API for the neural network (which was later removed) and starting the stock API (which Grace later redid and completed). 

- [Neural Network Commit](https://github.com/TheoH32/stocktifyBackend/commit/bf75f3eaa2d2e2c3dad387cea2a95860d4bf8bd8) (doing cors here but this is where it was done)
- Until where I did the stock api: [link](https://github.com/TheoH32/stocktifyBackend/commit/bf66c3a4c4fc26584420ff77ca15a2d25a3b0738)

Note: You can see in all my commits how I slowly go **insane**. I *love* that.


## Digging Deep into the Main Code I wrote

[Neural Network Commit](https://github.com/TheoH32/Stocktify/commit/cbbe7e8a389a66b46e287f442d6c903c76955c95)

```js
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
                [5000000, 150], // volume, price --> early on when I got this to work there wasn't as much data
                [4500000, 120],
                [5000, 20],
                [6000, 15]
            ];
            const answers = [0.9, 0.8, 0.3, 0.2];

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

```


## Github Analytics
#### Key Commits
- [Neural Network Commit](https://github.com/TheoH32/Stocktify/commit/cbbe7e8a389a66b46e287f442d6c903c76955c95)
- [Backend Chatbot](https://github.com/rachit-j/stocktifybot/commit/f0a9f12bdcd139dae4f6ce3674ebe0f1c6463c30) | [Link to Deployment](stocktifybot-pe40dssoc-rachit-j.vercel.app)
- [CORS Frontend](https://github.com/TheoH32/Stocktify/commit/1bc9f6fba2de8151f890f0993aa119fe72e4535d)

#### Challenges
A couple challenges that I faced include:
- CORS
- API Endpoints
- More CORS
- API Key Exposure
- CORS Again
- Response Time
- API not allowing testing from LocalHost
- API Rate limits
- CORS

#### Analytics
I don't really like to commit things until I'm done and it works on local, but even then, I still think I was able to do a lot!
![Analytics](/Rackets-Blog/images/analytics.png)
Note: Max number of commits/day is 22 (api not allowing testing from localhost)


## [Individual Review](/Rackets-Blog/labnotebook)

## [CollegeBoard Quiz](/Rackets-Blog/tri1review-cqz)

## [Extra Credit for N@TM](/Rackets-Blog/tri1review-ec)

## [Grades for Student Teaching](/Rackets-Blog/tri1review-grds)

## Reflection
This trimester was interesting. It seems like everyone knows what they're doing, but I've been thrown into the deep end. This is my first time in a CS class at this school, and even though I know a lot about Java and Python, I still had no idea what "code code code" meant when I first came in. Regardless, I feel like I have made tremendous project, both as a programmer and as a person. My Java skills and web design skills have definatley iproved since they were out of practice, and I got to work with new errors and new problems that required innovative strategies to overcome. This has been a pretty hard trimester for me, but I was able to look forward to AP CSA as a class that I felt that I enjoyed, felt comfortable in, and one that I was able to enjoy, not as a class, but more like a community of learning: something I find hard to get at Del Norte. Moreover, I've learned so much as a person. I know that other people are going through a lot, and I've learned to be humble. Humble yourself so you smooth over arguments when people do not want to work. Use correct strategies to prod people in the right way to help others. Overall, just try to play the mediator and work towards the common goal. For our group, it was not easy with our huge task. We had around 6 features, and 4 people, and so we also had to learn a lot of time management and critical thinking when everything broke down before our presentations (which it usually did). Overall, I think CSA has changed me for the better... I think that I will be able to continue as a better programmmer and a better lead/scrum master throughout CSA, and I believe that this class will continue to hit every weak point to continue making me stronger. This trimester, I learned how to collaborate at peak efficiency and to not bite off more than I can chew. I'm excited for what new experiences lie on the horizon as we sail into Trimester 2!