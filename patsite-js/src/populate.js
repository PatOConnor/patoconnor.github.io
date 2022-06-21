
function populateProjectLinks(){
    return
}

function populateBlogLinks(){
    return
}

//grabs header div from /static/
var placeHeader = () => {
    const tagId = 'page-header'
    const url   = '../../static/fragments/header.html'
    targetDiv = document.getElementById(tagId)
    console.log(targetDiv, url)    
    fetch(url)
      .then(response => response.text())
      .then(data => {
        targetDiv.innerHTML += data
      });
    }

//grabs footer div from /static/
var placeFooter = () => {
    const tagId = 'page-footer'
    const url   = '../../static/fragments/footer.html'
    targetDiv = document.getElementById(tagId)
    console.log(targetDiv, url)    
    fetch(url)
      .then(response => response.text())
      .then(data => {
        targetDiv.append(data)
      });
    }