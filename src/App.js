import ContentBlock from "./ContentBlock";
import "./app.css";


function App() {
  return (
    <div className="App">
      <header>
        <h1>Pat O'Connor</h1>
        <div>

        <a className="headerLink" href="mailto:patoconnorcode@gmail.com">
          ✉️click here to e-mail pat✉️
        </a>
        <p>
          patoconnorcode@gmail.com
        </p>
        </div>
      </header>

      <ContentBlock
        title="About Me"
        content={<p>I'm a freelance programmer located in the Greater Boston area. Contact me via patoconnorcode@gmail.com</p>}
        style="color1"
      />
      <ContentBlock
        title="Website Design"
        content={<p>I am proficient in creating modern webpages using ReactJS to create intuitive web interfaces, as well as implementing fully functional websites at low cost.</p>}
        style="color2"
      />
      <ContentBlock
        title="Automation, Web Scraping, and More"
        content={<p>Other services I provide include writing python scripts to automate clerical tasks and scrape web data.</p>}
        style="color3"
      />
      <ContentBlock
        title="Creative Work"
        content={<p>I am also available for creative musical work, including mixing, arranging, and composing. Click here for more.</p>}
        style="color4"
      />
    </div>
  );
}

export default App;
