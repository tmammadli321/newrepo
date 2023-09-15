document.addEventListener('DOMContentLoaded', () => {
    const dataContainer = document.getElementById('data-container');

    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            dataContainer.innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error fetching data:', error));
});
