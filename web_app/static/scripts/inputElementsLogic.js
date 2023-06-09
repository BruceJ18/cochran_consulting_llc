// rendering select elements with 
// apprrpriate information from input elements
// first select element to render determines second select element --end

// Ajax does not start until the end but everything accumalates to it


let add_input = document.getElementById("add");
let add_select = document.getElementById("form-type__select--add");

let edit_input = document.getElementById("edit");
let edit_select = document.getElementById("form-type__select--edit");

let selects__2 = document.getElementById('form-type__selects--2');

const defaultOption = document.getElementById('entity__option--default')

add_input.addEventListener('input', event => {
    const submitButton = document.getElementById('form-type__button');
    

    if (event.target.checked) {
        add_select.classList.toggle('active');
        edit_select.classList.remove('active');

        submitButton.textContent = "Start Addition";

        selects__2.style.display = 'none'
        
    }
})

edit_input.addEventListener('input', event => {
    const submitButton = document.getElementById('form-type__button');
    if (event.target.checked) {
        edit_select.classList.toggle('active');
        add_select.classList.remove('active');

        submitButton.textContent = "Start Edit";
        if (edit_select.value === '#') selects__2.style.display = 'none';
    }
})


// Waits for the select elementfor  ->
// edit portion to receive input ->
// and based on input sends current -> 
// inputs value (database name) ->
// to flask server --end --below

edit_select.addEventListener('input', event => {
    const edit_select_value = event.target.value;

    
    if (edit_select_value !== 'Options to Edit') selects__2.style.display = 'unset';
    else selects__2.style.display = 'none';

    const edit_select_value_text = (edit_select_value !== '#') 
    ? edit_select_value 
    : console.log('# damn');


    // ------------ start of ajax request and server response handling ------------

    const flaskEndpoint = "/add_or_edit"

    $.post( flaskEndpoint, {

        // post request data sent to flask endpoint
        javascript_data: edit_select_value_text

    },

    // function for handling ->
    // response data --end --below

    function (data, status, jqXHR) {

        // parsing function for ->
        // string data to html data --end --below

        function stringToHtml(data) {
            let parser = new DOMParser();
            // let html = parser.parseFromString(data, 'text/html');
            try {
                let html = parser.parseFromString(data, 'text/html');

                return html;
            } 
            catch(err) {
                return 'parse function may not be supported on this browser';
            }
        }

        let newDocument = stringToHtml(data);


        // replace current incorrect select element ->
        // with correct select element generated from server --end --below

        document.getElementById('form-type__selects--2')
        .replaceWith(
            newDocument
            .getElementById(
                'form-type__selects--2'
                )
            )

        
        // change display for second select -> 
        // element from none to unset ->
        // after we receive response data --end --below

        document
        .getElementById('form-type__selects--2')
        .style.display = 'unset';

        
        
    });
    
})