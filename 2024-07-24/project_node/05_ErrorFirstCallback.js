function fetchData(callback) {
    // Simulate a server request
    setTimeout(() => {
        const error = null; // Assume no errors occurred
        const data = { name: 'Alice' };
        callback(error, data);
    }, 1000);
}

fetchData((error, data) => {
    if (error) {
        console.error('An error occurred:', error);
    } else {
        console.log(data); // { name: 'Alice' }
    }
});