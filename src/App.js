// import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import { TodoPage } from './Pages/TodoPage'
import { Show } from './Pages/Show'

function App() {
  return (

    <div className="App">
      <Router>
        <Switch>
          <Route exact path='/'>
            <TodoPage />
          </Route>
          <Route path='/:id'>
            <Show />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
