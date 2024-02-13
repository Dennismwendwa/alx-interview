#!/usr/bin/node
// get movies
const request = require('request');


function getMovieCharacters(movieId) {
  const swapiBaseUrl = 'https://swapi.dev/api/films/';

  request.get(`${swapiBaseUrl}${movieId}/`, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode === 200) {
     const filmData = JSON.parse(body);
     const characterUrls = filmData.characters;

     charactersUrls.forEach((characterUrl) => {
       request.get(characterUrl, (charError, charResponse, charBody) => {
         if (charError) {
           console.error('Error fetching character:', charError);
         } else if (charResponse.statusCode === 200) {
           const characterData = JSON.parse(charBody);
           console.log(characterData.name);
         } else {
           console.error(`Error fetching character. Status code: ${charResponse.statusCode}`);
         }
       });
     });
    } else {
      console.error(`Error: Unable to Movie ID ${movieId}. Status code: ${response.statusCode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
}

const movieId = process.argv[2];

getMovieCharacters(movieId);
