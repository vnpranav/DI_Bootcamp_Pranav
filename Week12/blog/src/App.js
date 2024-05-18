// import logo from './logo.svg';
// import './App.css';
import Actor from './Actor';
import './Actor.css'

// const actorList = [
//   { 
//   firstName: "George",
//   lastName:"Clooney",
//   url:"https://images.unsplash.com/photo-1472457897821-70d3819a0e24?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c21hbGx8ZW58MHx8MHx8fDA%3D"
//   },
//   {
//   firstName: "Emma",
//   lastName:"Watson",
//   url:"https://images.unsplash.com/photo-1472457897821-70d3819a0e24?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c21hbGx8ZW58MHx8MHx8fDA%3D"
// },
//   {
//   firstName: "Tom",
//   lastName:"Holland",
//   url:"https://images.unsplash.com/photo-1472457897821-70d3819a0e24?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c21hbGx8ZW58MHx8MHx8fDA%3D"
// }
// ];

function App() {
  return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Hello this is the <code>src/App.js</code> file! 
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Go to React Website
    //     </a>
    //   </header>
    // </div>

    <div className='ActorList'>
      <Actor/>
    </div>
  );
}

export default App;
