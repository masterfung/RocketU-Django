/**
 * Created by @masterfung on 8/4/14.
 */

$(document).ready(function () {
    // Let's set up some variables to save the canvas elements and properties
    var canvas = $("#canvas")[0];
    var canvasContext = canvas.getContext("2d");
    var width = $("#canvas").width();
    var height = $("#canvas").height();

	// Will represent each body cell of the snake
	var snakeBody;

	var cellWidth = 10;

	var currentDirection;

	function gameLoop() {
        getNextPosition();
        checkGameOver();
        checkEatFood();
        paintCanvas();
    }

    // Get the next position of the snake
    function getNextPosition() {}

    // Check if snake has collided with walls or itself
    function checkGameOver() {}

    // Check if snake is on the same space as food
    function checkEatFood() {}

	function paintCanvas() {
        // Lets fill in the canvas colors
        canvasContext.fillStyle = "white";
        canvasContext.fillRect(0, 0, width, height);
        canvasContext.strokeStyle = "black";
        canvasContext.strokeRect(0, 0, width, height);

		// Paint the snake body
	    for (var i = 0; i < snakeBody.length; i++) {
	        var cell = snakeBody[i];
	        paintCell(cell.x, cell.y);
        }
    }

	//Lets first create a generic function to paint cells
	function paintCell(x, y) {
	    canvasContext.fillStyle = "purple";
	    canvasContext.fillRect(x * cellWidth, y * cellWidth, cellWidth, cellWidth);
	    canvasContext.strokeStyle = "white";
	    canvasContext.strokeRect(x * cellWidth, y * cellWidth, cellWidth, cellWidth);
	}

	var gameLoopInterval;

    function startGame() {
	    // Create the initial snake
        createSnake();
        // Let's set the game loop to run every 60 milliseconds
        gameLoopInterval = setInterval(gameLoop, 60);

	    // Default the snake going right
        currentDirection = "right";
    }

	function createSnake() {
    // Starting length of the snake will be 5 cells
    var length = 5;

    // Let's set the snake body back to an empty array
    snakeBody = [];

    // Add cells to the snake body starting from the top left hand corner of the screen
    for (var i = length - 1; i >= 0; i--) {
        snakeBody.push({x: i, y: 0});
    }
	}



	startGame();

});


