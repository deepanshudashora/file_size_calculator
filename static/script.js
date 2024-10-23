document.addEventListener('DOMContentLoaded', () => {
    const animalSelect = document.getElementById('animalSelect');
    const animalImageContainer = document.getElementById('animalImageContainer');
    const fileUpload = document.getElementById('fileUpload');
    const fileInfo = document.getElementById('fileInfo');

    animalSelect.addEventListener('change', (e) => {
        const animal = e.target.value;
        if (animal) {
            fetch(`/get_animal_image/${animal}`)
                .then(response => response.json())
                .then(data => {
                    animalImageContainer.innerHTML = `<img id="animalImage" src="data:image/jpeg;base64,${data.image}" alt="${animal}">`;
                });
        } else {
            animalImageContainer.innerHTML = '';
        }
    });

    fileUpload.addEventListener('change', (e) => {
        const file = e.target.files[0];
        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload_file', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            fileInfo.innerHTML = `
                <p><strong>Name:</strong> ${data.name}</p>
                <p><strong>Size:</strong> ${data.size}</p>
                <p><strong>Type:</strong> ${data.type}</p>
            `;
        });
    });
});