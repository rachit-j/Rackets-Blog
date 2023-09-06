
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>To-Do List App</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <h1>To-Do List App</h1>
  <input type="text" id="taskInput" placeholder="Enter a new task">
  <button id="addTaskButton">Add Task</button>
  <ul id="taskList"></ul>

  <script>
    // Function to add a new task to the list
    function addTask(task) {
      const taskList = $("#taskList");
      const taskItem = $("<li></li>");
      taskItem.append(`<span>${task}</span>`);
      taskItem.append(`<button class="completeButton">Complete</button>`);
      taskItem.append(`<button class="removeButton">Remove</button>`);
      taskList.append(taskItem);

      // Attach event listeners to buttons
      taskItem.find(".completeButton").click(function() {
        $(this).siblings("span").toggleClass("completed");
      });

      taskItem.find(".removeButton").click(function() {
        $(this).parent().remove();
      });
    }

    // Event handler for adding a new task
    $("#addTaskButton").click(function() {
      const taskInput = $("#taskInput");
      const taskText = taskInput.val().trim();
      if (taskText !== "") {
        addTask(taskText);
        taskInput.val("");
      }
    });

    // Initial setup
    $("#taskInput").keypress(function(event) {
      if (event.key === "Enter") {
        $("#addTaskButton").click();
      }
    });
  </script>

  <style>
    .completed {
      text-decoration: line-through;
      color: gray;
    }
  </style>
</body>
