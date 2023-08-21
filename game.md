---
title: Blogs
---

# The Sleepy Platformer
Warning: Sleepy after activity


<body>
    <canvas id="gameCanvas" width="1400" height="400"></canvas>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const player = {
            x: 50,
            y: 50,
            width: 50,
            height: 50,
            color: 'blue',
            velocityX: 0,
            velocityY: 0,
            inAir: true,
            speed: 8, // added for horizontal movement speed

            update: function() {
                this.x += this.velocityX;
                this.y += this.velocityY;

                if (this.inAir) {
                    this.velocityY += 1; // gravity
                }

                this.velocityX *= 0.95; // friction

                let collidedWithPlatform = false;

                // Check for top collision with platforms
                for (let platform of platforms) {
                    if (this.y + this.height > platform.y &&
                        this.y + this.height < platform.y + this.velocityY &&
                        this.x + this.width > platform.x &&
                        this.x < platform.x + platform.width) {
                            this.y = platform.y - this.height;
                            this.velocityY = 0;
                            this.inAir = false;
                            collidedWithPlatform = true;
                            break;
                        }
                }

                // If we didn't collide with the top of a platform, check the bottom
                if (!collidedWithPlatform) {
                    for (let platform of platforms) {
                        if (this.velocityY < 0 && 
                            this.y <= platform.y + platform.height && 
                            this.y + this.height >= platform.y &&
                            this.x + this.width > platform.x &&
                            this.x < platform.x + platform.width) {
                            this.y = platform.y + platform.height;
                            this.velocityY = 0;
                            collidedWithPlatform = true;
                            break;
                        }
                    }
                }

                let onPlatform = false;

                for (let platform of platforms) {
                    if (this.y + this.height >= platform.y &&
                        this.y + this.height <= platform.y + 10 && // assuming 10 is a slight overlap for detection
                        this.x + this.width > platform.x &&
                        this.x < platform.x + platform.width) {
                            this.y = platform.y - this.height;
                            onPlatform = true;
                            break; // exit the loop as soon as a collision is detected
                    }
                }

                if (!collidedWithPlatform && this.y + this.height !== canvas.height) {
                    this.inAir = true;
                }

                if (this.y + this.height > canvas.height) {
                    this.y = canvas.height - this.height;
                    this.velocityY = 0;
                    this.inAir = false;
                }
            },

            jump: function() {
                if (!this.inAir) {
                    this.velocityY = -15;
                    this.inAir = true;
                }
            },

            moveLeft: function() {
                this.velocityX = -this.speed;
            },

            moveRight: function() {
                this.velocityX = this.speed;
            }
        };

        const platforms = [
            { x: 200, y: 300, width: 100, height: 10, color: 'green' },
            { x: 400, y: 200, width: 150, height: 10, color: 'green' },
            { x: 500, y: 200, width: 10, height: 200, color: 'green' }
        ];

        function drawPlatforms() {
            platforms.forEach(platform => {
                ctx.fillStyle = platform.color;
                ctx.fillRect(platform.x, platform.y, platform.width, platform.height);
            });
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw player
            ctx.fillStyle = player.color;
            ctx.fillRect(player.x, player.y, player.width, player.height);

            // Draw platforms
            drawPlatforms();

            player.update();

            requestAnimationFrame(draw);
        }

        document.addEventListener('keydown', function(event) {
            switch (event.keyCode) {
                case 37: // Left arrow
                    player.moveLeft();
                    break;
                case 39: // Right arrow
                    player.moveRight();
                    break;
                case 38: // Space bar
                    player.jump();
                    break;
            }
        });

        document.addEventListener('keyup', function(event) {
            switch (event.keyCode) {
                case 37: // Left arrow
                case 39: // Right arrow
                    player.velocityX = 0;
                    break;
            }
        });

        draw();
        </script>

