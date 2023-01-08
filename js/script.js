document.getElementById("addNote").addEventListener('click', async() => {
    const inputTitle = document.getElementById("noteTitle");
    const title = inputTitle.value;
    const inputContent = document.getElementById("noteContent");
    const content = inputContent.value;

    if (!!title.trim()){
        if (!!content.trim()){
            const res = await fetch("http://0.0.0.0:8000/api/v1/notes", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({title, content})
            });

            console.log(inputTitle)
            console.log(inputContent)

            const note = await res.json();
            noteToHTML(note);
            inputTitle.value = '';
            inputContent.value = '';
            showToast('createToast')
        }
    }
})

async function getAllNotes(){
            const res = await fetch("http://0.0.0.0:8000/api/v1/notes");
            const notes = await res.json();
            console.log(notes);
            notes.forEach(note => noteToHTML(note))
        }
        window.addEventListener('DOMContentLoaded', getAllNotes)

function noteToHTML({id, title, content}) {
    const noteList = document.getElementById('notes')
    noteList.insertAdjacentHTML('beforeend',
    `<div id="note${id}" class="row mb-3 card text-bg-light mb-1">
        <button onclick="deleteNote(${id})" type="button" class="btn-close" aria-label="Close" style="font-size: 20px; position: absolute; right: 5px; top: 5px"></button>
        <label class="form-check-label fs-2 mb-1 mt-1">
            ${title}
        </label>
        <label class="form-check-label fs-6 mb-3 mt-1">
            ${content}
        </label>
    </div>`
    );
}

async function deleteNote(id) {
    console.log(id);
    const res = await fetch(`http://0.0.0.0:8000/api/v1/notes/${id}`,{
    method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    if (res.status == 204) {
        document.getElementById(`note${id}`).remove();
        showToast('deleteToast');
    }
}

function showToast(text){
    var option =
    {
        animation : true,
        delay : 3000
    };
    const toastLive = document.getElementById(text);
    var toastElement = new bootstrap.Toast(toastLive, option);
    toastElement.show();

}