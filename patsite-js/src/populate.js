var populateProjectLinks = () => {
  placeFragmentAtTargetTag('project-links', '../../static/fragments/project-links.html')
}

var populateBlogLinks = () => {
  placeFragmentAtTargetTag('blog-links', '../../static/fragments/blog-links.html')
}

var placeHeader = () => {
  placeFragmentAtTargetTag('page-header', '../../static/fragments/header.html')
}

var placeFooter = () => {
  placeFragmentAtTargetTag('page-footer', '../../static/fragments/footer.html')
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