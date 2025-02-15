<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VTU Notes Hub</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>VTU Notes Hub</h1>
        <nav>
            <a href="#login">Login</a>
        </nav>
    </header>
    <main>
        <section id="subjects">
            <h2>Subjects</h2>
            <ul id="subject-list">
                <li>Maths</li>
                <li>Physics</li>
                <li>Chemistry</li>
                <li>POP Using C</li>
                <li>Basics of Java</li>
                <li>Introduction to Python</li>
                <li>Introduction to Mechanical Engineering</li>
                <li>Introduction to Electronics and Communication</li>
            </ul>
            <button id="add-subject" style="display: none;">Add Subject</button>
            <input type="text" id="new-subject" placeholder="Enter new subject" style="display: none;">
        </section>
        <section id="upload" style="display: none;">
            <h2>Upload Notes</h2>
            <input type="file" id="file-upload" accept="application/pdf">
            <button id="upload-btn">Upload</button>
            <ul id="uploaded-files"></ul>
        </section>
    </main>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const addSubjectButton = document.getElementById("add-subject");
            const newSubjectInput = document.getElementById("new-subject");
            const subjectList = document.getElementById("subject-list");
            const uploadSection = document.getElementById("upload");
            const uploadBtn = document.getElementById("upload-btn");
            const fileUpload = document.getElementById("file-upload");
            const uploadedFiles = document.getElementById("uploaded-files");
            
            const userIsAdmin = true; // Change this logic as per authentication

            if (userIsAdmin) {
                addSubjectButton.style.display = "block";
                newSubjectInput.style.display = "block";
                uploadSection.style.display = "block";
            }

            addSubjectButton.addEventListener("click", function() {
                const newSubject = newSubjectInput.value.trim();
                if (newSubject) {
                    const li = document.createElement("li");
                    li.textContent = newSubject;
                    subjectList.appendChild(li);
                    newSubjectInput.value = "";
                }
            });

            uploadBtn.addEventListener("click", function() {
                const file = fileUpload.files[0];
                if (file) {
                    const li = document.createElement("li");
                    li.textContent = file.name;
                    uploadedFiles.appendChild(li);
                    fileUpload.value = "";
                }
            });
        });
    </script>
    <script src="script.js"></script>
</body>
</html>
