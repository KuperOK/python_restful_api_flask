// get method (Read operation)
    let form_get = document.querySelector('form[name="get_emp"]');
    let input_get = document.querySelector('.get_emp_id_name');
    let get_result = document.querySelector('.get_result');

    form_get.addEventListener('submit', (evt) => {
        evt.preventDefault();
    try {
    fetch(`/api/employees/${input_get.value}`).then(res => {
      if (res.status == "204") {
        get_result.textContent = `Employee not found`
      }
         console.log(res.status);
        return res.json()
    } ).then(data => {
         console.log(data);
        console.log(data[0].date_of_birth.split(' ').slice(1,4));
        get_result.innerHTML = `<b> Data of birth: </b> ${data[0].date_of_birth.split(' ').slice(1,4).join('-')}; <b>Dept id:</b> ${data[0].dep_id};
         <b>Employee id:</b> ${data[0].emp_id}, <b>Employee name:</b> ${data[0].emp_name}; <b>Salary:</b> ${data[0].salary}`
    }) ;
        input_get.value = '';


} catch (e) {alert('Employee not found')}
});

// post method (Rest CREATE-operation)
    let form = document.querySelector('form[name="add_emp"]');
    let input_name = document.querySelector('.emp_name');
    let input_date = document.querySelector('.date');
    let input_sal = document.querySelector('.salary');
    let input_did = document.querySelector('.dep_id');

    form.addEventListener('submit', (evt) => {
        evt.preventDefault();
        // object.push({index: '', value: input.value})
    try {
    fetch('/api/employees/add', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
        'Content-Type': 'application/json'
            },
    body: JSON.stringify({'emp_name':input_name.value, 'date_of_birth':input_date.value,
        'salary':input_sal.value, 'dep_id':input_did.value}) // body data type must match "Content-Type" header
});
        alert(`Employee ${input_name.value} has been added`);
        input_name.value = '';
        input_date.value = '';
        input_sal.value = '';
        input_did.value = '';

} catch (e) {alert('query failed')}
});

//  delete method (Rest DELETE-operation)
    let form_del = document.querySelector('form[name="del_emp"]');
    let input_del = document.querySelector('.emp_name_or_id');

    form_del.addEventListener('submit', (evt) => {
        evt.preventDefault();
    try {
    fetch(`/api/employees/${input_del.value}`, {
    method: 'DELETE', // *GET, POST, PUT, DELETE, etc
}).then(res => {
        if (res.status == '204') {
            alert(`Department ${input_del.value} has been deleted`);
        } else {
            alert(`No employee ${input_del.value} to delete`);
        }
        input_del.value = '';
    });
    // console.log()
    //     input_del.value = '';

} catch (e) {alert('query failed')}
});

// put method (Rest Update-operation)
    let form_put = document.querySelector('form[name="put_emp"]');
    let input_put_id = document.querySelector('.put_emp_id_name');
    let input_put_new_name = document.querySelector('.put_new_name');
    // let field_name = input_put_id ? 'dep_id' : 'dep_name'

    form_put.addEventListener('submit', (evt) => {
        evt.preventDefault();
        // object.push({index: '', value: input.value})
    if  (!isExist(input_put_new_name, 'Input New Emp Name')) return ;
    if  (!isExist(input_put_id, 'Input Emp Id')) return ;

        try {
    // if( input_put_id.value) {
        fetch(`/api/employees/${input_put_id.value ? input_put_id.value : input_put_new_name.value}`, {
            method: 'PUT', // *GET, POST, PUT, DELETE, etc.
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'dep_name': input_put_new_name.value}) // body data type must match "Content-Type" header
        }).then(response => {
            console.log(response);
            if (response.status == '204') {
                alert(`Employee ${input_put_id.value ? input_put_id.value : input_put_new_name.value} has been updated`);
            } else {
                alert('No such employee to update')
            }
        })
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