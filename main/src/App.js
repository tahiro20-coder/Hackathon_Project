import '../src/Styles/App.css';
import "./Styles/Fonts.css";
import Header from './Components/Header.jsx';
import Footer from './Components/Footer.jsx';
import PageContent from './Components/PageContent.jsx';
import React from 'react'



function App() {

  return (
    <>
    <Header/>
    <PageContent />
    <Footer/>
    </>
  );
}

export default App;
