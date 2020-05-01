function addQuestion() {
    const div = document.createElement('div');

    div.className = 'row';

    div.innerHTML = `
            <form method="post" novalidate>
                {{ form.csrf_token }}
                    <dl>
                        {{ render_field (form.target_gender, class='form-control') }}
                        {{ render_field (form.target_minimum_age, class='form-control') }}
                        {{ render_field (form.target_maximum_age, class='form-control') }}
                        {{ render_field(form.nationality, class='form-control') }}
                    </dl>
                </form>
                <h4>Question</h4>
            <h4>Question <input class="border border-dark form-control-sm" placeholder="Question Number" style="margin-bottom: 2px"></h4>
            <input class="btn btn-outline-dark" type="button" value="- Delete the question" onclick="removeQuestion(this)" style="margin-left: 5px;margin-bottom: 8px">
            <div class="form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Compulsory Question</label>
            </div>
        <div class="input-group mb-3" style="margin-top: 5px">
            <input type="text" class="form-control" placeholder="Enter your question here." aria-label="Question"><div class="input-group input-group-sm survey-question-create mb-2">
        </div>
        <div class="input-group input-group-sm mb-2">
            <input type="text" class="form-control" placeholder="Enter your choice here." aria-label="Choice">
        </div>
        <div class="input-group input-group-sm mb-2">
            <input type="text" class="form-control" placeholder="Enter your choice here." aria-label="Choice">
        </div>

        <div class="input-group input-group-sm mb-2">
            <input type="text" class="form-control" placeholder="Enter your choice here." aria-label="Choice">
        </div>
        <div class="input-group input-group-sm mb-2">
            <input type="text" class="form-control" placeholder="Enter your choice here." aria-label="Choice">
        </div>
        </form>`;

    document.getElementById('question').appendChild(div);
}

function removeQuestion(input) {
    document.getElementById('question').removeChild(input.parentNode);
}

function addCommentBox() {
    const div = document.createElement('div');

    div.className = 'row';

    div.innerHTML = `
            <h4>Question <input class="border border-dark form-control-sm" placeholder="Question Number" style="margin-bottom: 2px"></h4>
            <input class="btn btn-outline-dark" type="button" value="- Delete the question" onclick="removeCommentBox(this)" style="margin-left: 5px;margin-bottom: 8px">
            <div class="input-group mb-3" style="margin-top: 5px">
            <input type="text" class="form-control" placeholder="Enter your question here." aria-label="Question">
            <div class="input-group input-group-sm survey-question-create mb-2">
        </div>
</div>`;

    document.getElementById('question').appendChild(div);
}

function removeCommentBox(input) {
    document.getElementById('question').removeChild(input.parentNode);
}
//Reference: https://stackoverflow.com/questions/17650776/add-remove-html-inside-div-using-javascript

//Reference: https://stackoverflow.com/questions/22402777/html-javascript-button-click-counter