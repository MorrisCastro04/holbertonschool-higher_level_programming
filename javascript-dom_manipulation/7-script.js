const api = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(api)
  .then(response => response.json())
  .then(data => {
    const films = document.getElementById('list_movies');
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      films.appendChild(li);
    });
  })
  .catch(error => console.error('Error fetching data:', error));
