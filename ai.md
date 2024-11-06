```javascript
const MovieList = ({movies, onMovieSelect}) => {
  return (
    <ul>
      {movies.map((movie) => (
        <li key={movie.id}>
          <input type="checkbox" id={movie.id} checked={movie.selected} onChange={() => onMovieSelect(movie.id)} />
          <label htmlFor={movie.id}>{movie.title}</label>
        </li>
      ))}
    </ul>
  )
}
```
