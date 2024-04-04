import logo from './logo.svg';
import './App.css';
import { List, ListItem, ListItemIcon, TextField,ListItemText } from '@mui/material';
import {useEffect, useState} from 'react'
import LocalMoviesIcon from '@mui/icons-material/LocalMovies'

function App() {
  const [itemId, setItemId] = useState("1")
  const [item, setItem] = useState(null)

  useEffect(() => {
    console.log(`${itemId}`) // !!!! `  `

    if (itemId == "") {
      setItem(null);
    } else {
      fetch(`http://localhost:8000/items/${itemId}`)
      .then( result => result.json() )
      .then( result => {
        console.log(result);
        setItem(result);
      } )
    }


  }, [itemId])

  return (
    <div className="App">
      <header className="App-header">
        <TextField id="item id" label="Item Id"
          variant="outlined" color="warning" focused
          value={itemId}
          onChange={e=>setItemId(e.target.value)}
        />      
      </header>

      <List>
        { item && 
          <ListItem>
            <ListItemIcon><LocalMoviesIcon /></ListItemIcon>
            <ListItemText primary={item['item_id']}></ListItemText>
            <ListItemText primary={item['q']}></ListItemText>
          </ListItem>
        }
      </List>
    </div>
  );
}

export default App;
