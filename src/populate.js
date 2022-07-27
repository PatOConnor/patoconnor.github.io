var linksPerPage = 3

populateBlogLinks = () => {
  let targetDiv = document.getElementById('blogposts-list');
  response = fetch("./src/blogposts.json")
  .then(response => response.json())
  .then(data => {
    var postsCount = 0;
    data.forEach((elem) => {
      var newTextNode = document.createTextNode(elem.name);
      var linkNode = document.createElement('a');
      var newNode = document.createElement('li');
      newNode.appendChild(newTextNode);
      linkNode.setAttribute('href', elem.contentLocalLink);
      linkNode.appendChild(newNode)
      targetDiv.appendChild(linkNode)
      postsCount++;
      if (postsCount >= linksPerPage){
        // break out of foreach loop
        return false
      }
    })
  })
}

var placeLogo = () => {
  placeFragmentAtTargetTag('header-logo', '../static/fragments/logo.html')
}


var placeHeader = () => {
  placeFragmentAtTargetTag('page-header', '../static/fragments/header.html')
}

var placeFooter = () => {
  placeFragmentAtTargetTag('page-footer', '../static/fragments/footer.html')
}



//grabs header div from /static/
var placeFragmentAtTargetTag = (tagId, url) => {
    let targetDiv = document.getElementById(tagId)
    console.log(targetDiv, url)    
    fetch(url)
    .then(response => response.text())
    .then(data => {
        console.log('within fetch call', targetDiv, url)    
        targetDiv.innerHTML += data
      });
    }