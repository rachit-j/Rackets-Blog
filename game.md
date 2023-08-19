---
title: Blogs
---

# Some cool platformer game



<body>
    <canvas id="gameCanvas" width="800" height="600"></canvas>
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        const player = {
            x: 50,
            y: 400,
            width: 50,
            height: 50,
            velocityX: 0,
            velocityY: 0,
            inAir: true,
            moveLeft: function() {
                this.velocityX = -5;
            },
            moveRight: function() {
                this.velocityX = 5;
            },
            jump: function() {
                if (!this.inAir) {
                    this.velocityY = -15;
                    this.inAir = true;
                }
            },
            update: function() {
                this.x += this.velocityX;
                this.y += this.velocityY;

                if (this.inAir) {
                    this.velocityY += 1;  // gravity
                }

                this.velocityX *= 0.9;  // friction

                // Collision with platform
                if (this.y + this.height > platform.y && this.x + this.width > platform.x && this.x < platform.x + platform.width) {
                    this.y = platform.y - this.height;
                    this.velocityY = 0;
                    this.inAir = false;
                }
                
                if (this.y + this.height > canvas.height) {
                    this.y = canvas.height - this.height;
                    this.velocityY = 0;
                    this.inAir = false;
                }
            },
            draw: function() {
                ctx.fillStyle = 'blue';
                ctx.fillRect(this.x, this.y, this.width, this.height);
            }
        };

        const platform = {
            x: 200,
            y: 500,
            width: 400,
            height: 50,
            draw: function() {
                ctx.fillStyle = 'green';
                ctx.fillRect(this.x, this.y, this.width, this.height);
            }
        };

        const platform2 = {
            x: 400,
            y: 800,
            width: 200,
            height: 50,
            draw: function() {
                ctx.fillStyle = 'green';
                ctx.fillRect(this.x, this.y, this.width, this.height);
            }
        };

        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            player.update();
            player.draw();
            platform.draw();
            platform2.draw();

            requestAnimationFrame(gameLoop);
        }

        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') player.moveLeft();
            if (e.key === 'ArrowRight') player.moveRight();
            if (e.key === 'ArrowUp') player.jump();
        });

        gameLoop();

    </script>