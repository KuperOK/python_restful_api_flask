// post method (Rest GET-operation)
    let form_get = document.querySelector('form[name="get_dep"]');
    let input_get = document.querySelector('.get_dep_id_name');
    let get_result = document.querySelector('.get_result');

    form_get.addEventListener('submit', (evt) => {
        evt.preventDefault();
    if (!isExist(input_get, 'Input Dept Name or Id')) return;
        try {
    fetch(`/api/departments/${input_get.value}`).then(res => {
        // console.log(res);
        if (res.status == "204") {
        get_result.textContent = `Department not found`
      }
        // console.log(res.status);
        return res.json()
    } ).then(data => {
        // console.log(data);
        get_result.innerHTML = `<b>Department dep_id:</b> ${data[0].dep_id}, <b>Department name:</b> ${data[0].dep_name}`
    }) ;
        input_get.value = '';
} catch (e) {alert('Department not found')}
});

// post method (Rest CREATE-operation)
    let form = document.querySelector('form[name="add_dep"]');
    let input = document.querySelector('.dep_name');

    form.addEventListener('submit', (evt) => {
        evt.preventDefault();
        // object.push({index: '', value: input.value})
        if (!isExist(input, 'Input Dept Name')){
            return ;
        }
        try {
    fetch('/api/departments/add', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
        'Content-Type': 'application/json'
            },
    body: JSON.stringify({'dep_name':input.value}) // body data type must match "Content-Type" header
});
        alert(`Department ${input.value} has been added`);
        input.value = '';
} catch (e) {alert('query failed')}
});

//  delete method (Rest DELETE-operation)
    let form_del = document.querySelector('form[name="del_dep"]');
    let input_del = document.querySelector('.dep_name_or_id');

    form_del.addEventListener('submit', (evt) => {
        evt.preventDefault();
        // object.push({index: '', value: input.value})
    if (!isExist(input_del, 'Input Dept Name or Id')) return ;
        try {
    fetch(`/api/departments/${input_del.value}`, {
    method: 'DELETE', // *GET, POST, PUT, DELETE, etc
}).then(res => {
        if (res.status == '204') {
            alert(`Department ${input_del.value} has been deleted`);
        } else {
            alert(`No department ${input_del.value} to delete`);
        }
    });

        input_del.value = '';
} catch (e) {alert('query failed')}
});

// put method (Rest Update-operation)
    let form_put = document.querySelector('form[name="put_dep"]');
    let input_put_id = document.querySelector('.put_dep_id_name');
    let input_put_new_name = document.querySelector('.put_new_name');
    // let field_name = input_put_id ? 'dep_id' : 'dep_name'

    form_put.addEventListener('submit', (evt) => {
        evt.preventDefault();
        // object.push({index: '', value: input.value})
    if  (!isExist(input_put_new_name, 'Input New Dept Name')) return ;
    if  (!isExist(input_put_id, 'Input Dept Id')) return ;

        try {
    // if( input_put_id.value) {
        fetch(`/api/departments/${input_put_id.value ? input_put_id.value : input_put_new_name.value}`, {
            method: 'PUT', // *GET, POST, PUT, DELETE, etc.
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'dep_name': input_put_new_name.value}) // body data type must match "Content-Type" header
        }).then(response => {
            console.log(response);
            if (response.status == '204') {
                alert(`Department ${input_put_id.value ? input_put_id.value : input_put_new_name.value} has been updated`);
                // alert(`Department ${input_put_id.value} has been updated to ${input_put_new_name.value} `);

            } else {
                alert('No such department')
            }

        });
        input_put_id.value = '';
        input_put_new_name.value = '';
    // }
} catch (e) {alert('query failed')}
});

    function isExist(input, message) {
        if (input.value != ''){
            return true;
        } else {
            alert (message);
            return false;
        }
    }