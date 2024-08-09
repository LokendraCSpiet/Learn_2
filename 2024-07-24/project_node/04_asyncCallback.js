function fetchData(callback) {
    setTimeout(() => { // Simulate a server request
        const data = { name: 'Alice' };
        callback(data);
    }, 3000);
}

    fetchData((data) => {
        console.log(data); // { name: 'Alice' }
    });